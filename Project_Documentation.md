# Elle & Olyv Baking Co. Website Documentation

## Project Structure
```
├── main.py                 # Flask server and routing
├── static/
│   ├── css/
│   │   └── style.css      # All website styling
│   ├── img/
│   │   └── placeholder.svg # SVG placeholder for testimonials
│   └── js/
│       └── script.js      # Frontend interactivity
├── templates/
│   └── index.html         # Main webpage template
```

## Key Features
1. Responsive design for all devices (mobile, tablet, desktop)
2. Dynamic promotion bar with animated text rotation
3. Interactive shopping cart system
4. Mobile-friendly navigation menu
5. Product grid with add-to-cart functionality
6. Newsletter subscription with animation
7. Responsive footer with business information
8. Touch-optimized interactions for mobile devices

## Files Overview

### 1. main.py
- Flask server configuration
- Shopping cart functionality
- Product menu items database
- API endpoints for cart operations

### 2. style.css
- Complete website styling
- Responsive design rules
- Animations and transitions
- Device-specific adjustments

### 3. script.js
- Interactive features
- Shopping cart management
- Promotion bar animations
- Mobile menu handling
- Newsletter subscription

### 4. index.html
- Main website structure
- Product display templates
- Shopping cart interface
- Newsletter signup form
- Footer information

## Implementation Details

### Cart Functionality
- Session-based cart storage
- Real-time cart updates
- Interactive quantity controls
- Subtotal calculations

### Responsive Design
- Mobile-first approach
- Portrait and landscape orientations
- Tablet and desktop optimizations
- Touch-friendly interfaces

### User Interface Elements
- Fixed promotion bar
- Sliding mobile menu
- Cart popup
- Interactive product cards
- Newsletter subscription form

### Animation Features
- Promotion text typing animation
- Add to cart button feedback
- Menu transitions
- Newsletter success feedback

## Environment Setup
The website runs on Flask and requires:
- Python 3.x
- Flask framework
- Modern web browser
- Port 5000 for development

## Running the Application
The application starts with:
```python
python main.py
```
Server runs on http://0.0.0.0:5000
