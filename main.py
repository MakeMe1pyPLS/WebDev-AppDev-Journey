from flask import Flask, render_template, session, jsonify, request, send_from_directory
import os
import random
import string
from datetime import datetime
from app import app, db
from models import Order, OrderItem

# Menu items with prices
MENU_ITEMS = {
    'chocolate_chip': {
        'name': 'Classic Chocolate Chip Cookies',
        'price': 12.99,
        'description': 'Classic cookies loaded with rich chocolate chips'
    },
    'peanut_butter_cup': {
        'name': 'Peanut Butter Cup Cookies',
        'price': 13.99,
        'description': 'Soft cookies filled with peanut butter cup goodness'
    },
    'macaron_box': {
        'name': 'French Macaron Box',
        'price': 24.99,
        'description': 'Assorted flavors of delicate French macarons'
    },
    'brownie_box': {
        'name': 'Fudgy Brownie Box',
        'price': 18.99,
        'description': 'Rich, fudgy brownies with a perfect crackly top'
    },
    'cookie_box': {
        'name': 'Assorted Cookie Box',
        'price': 22.99,
        'description': 'A variety of our most popular cookie flavors'
    },
    'cupcake_box': {
        'name': 'Signature Cupcake Box',
        'price': 26.99,
        'description': 'Beautifully decorated cupcakes in assorted flavors'
    },
    'cake_pops': {
        'name': 'Cake Pops',
        'price': 15.99,
        'description': 'Delicious bite-sized cake pops in various flavors'
    },
    'mini_cakes': {
        'name': 'Mini Celebration Cakes',
        'price': 16.99,
        'description': 'Perfect individual-sized celebration cakes'
    }
}

def generate_tracking_number():
    """Generate a unique tracking number for orders"""
    prefix = 'EO'  # Elle & Olyv prefix
    timestamp = datetime.now().strftime('%y%m%d')
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{prefix}{timestamp}{random_chars}"

@app.route('/static/js/service-worker.js')
def service_worker():
    return send_from_directory('static/js', 'service-worker.js')

@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/')
def home():
    if 'cart' not in session:
        session['cart'] = {}
    return render_template('index.html', menu_items=MENU_ITEMS)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    item_id = request.json.get('item_id')
    if item_id in MENU_ITEMS:
        cart = session.get('cart', {})
        cart[item_id] = cart.get(item_id, 0) + 1
        session['cart'] = cart
        return jsonify({'success': True, 'message': 'Item added to cart', 'cart': cart})
    return jsonify({'success': False, 'message': 'Invalid item'}), 400

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    item_id = request.json.get('item_id')
    cart = session.get('cart', {})
    if item_id in cart:
        del cart[item_id]
        session['cart'] = cart
        return jsonify({'success': True, 'message': 'Item removed from cart', 'cart': cart})
    return jsonify({'success': False, 'message': 'Item not in cart'}), 400

@app.route('/cart')
def get_cart():
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    for item_id, quantity in cart.items():
        if item_id in MENU_ITEMS:
            item = MENU_ITEMS[item_id]
            subtotal = item['price'] * quantity
            total += subtotal
            cart_items.append({
                'id': item_id,
                'name': item['name'],
                'price': item['price'],
                'quantity': quantity,
                'subtotal': subtotal
            })
    return jsonify({
        'items': cart_items,
        'total': total
    })

@app.route('/order/create', methods=['POST'])
def create_order():
    cart = session.get('cart', {})
    if not cart:
        return jsonify({'success': False, 'message': 'Cart is empty'}), 400

    # Calculate total and create order
    total = sum(MENU_ITEMS[item_id]['price'] * quantity
                for item_id, quantity in cart.items())

    order = Order(
        tracking_number=generate_tracking_number(),
        total_amount=total,
        status='pending'
    )
    db.session.add(order)
    db.session.flush()  # Get the order ID before adding items

    # Add order items
    for item_id, quantity in cart.items():
        item = MENU_ITEMS[item_id]
        order_item = OrderItem(
            order_id=order.id,
            product_id=item_id,
            quantity=quantity,
            price=item['price']
        )
        db.session.add(order_item)

    db.session.commit()

    # Clear the cart
    session['cart'] = {}

    return jsonify({
        'success': True,
        'message': 'Order created successfully',
        'tracking_number': order.tracking_number
    })

@app.route('/order/track/<tracking_number>')
def track_order(tracking_number):
    order = Order.query.filter_by(tracking_number=tracking_number).first()
    if not order:
        return jsonify({'success': False, 'message': 'Order not found'}), 404

    return jsonify({
        'success': True,
        'order': {
            'tracking_number': order.tracking_number,
            'status': order.status,
            'created_at': order.created_at.isoformat(),
            'total_amount': order.total_amount,
            'items': [{
                'product_id': item.product_id,
                'quantity': item.quantity,
                'price': item.price
            } for item in order.items]
        }
    })

@app.route('/cart/update', methods=['POST'])
def update_cart():
    item_id = request.json.get('item_id')
    quantity = request.json.get('quantity')

    if item_id in MENU_ITEMS and isinstance(quantity, int) and quantity >= 0:
        cart = session.get('cart', {})
        if quantity == 0:
            cart.pop(item_id, None)
        else:
            cart[item_id] = quantity
        session['cart'] = cart
        return jsonify({'success': True, 'message': 'Cart updated'})
    return jsonify({'success': False, 'message': 'Invalid request'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)