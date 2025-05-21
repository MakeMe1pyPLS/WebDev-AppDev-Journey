# Complete Codebase Documentation

## 1. Flask Server (main.py)
```python
from flask import Flask, render_template, session, jsonify, request
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key")

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
```

## 2. Placeholder SVG (static/img/placeholder.svg)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg width="100" height="100" version="1.1" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="40" r="25" fill="#8BA888"/>
  <path d="M15,85 Q50,65 85,85" stroke="#8BA888" stroke-width="4" fill="none"/>
  <circle cx="50" cy="100" r="40" fill="#8BA888" opacity="0.3"/>
</svg>
```

The remaining files (style.css, script.js, and index.html) are quite long. Would you like me to show them as well?
