# Elle & Olyv Baking Co. Website Build Instructions

## Project Setup

1. Required Python packages:
```
flask
flask-sqlalchemy
```

2. Directory Structure:
```
├── main.py                 # Flask server
├── static/
│   ├── css/
│   │   └── style.css      # Website styling
│   ├── img/
│   │   └── placeholder.svg # SVG placeholder
│   └── js/
│       └── script.js      # Frontend interactivity
├── templates/
│   └── index.html         # Main webpage template
```

## Running the Website

1. Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

2. Start the Flask server:
```bash
python main.py
```

3. Access the website at `http://localhost:5000`

## Key Features

1. Responsive Design:
   - Mobile-first approach
   - Landscape mode optimization
   - Tablet and desktop support

2. Shopping Cart:
   - Add/remove items
   - Update quantities
   - Calculate totals

3. Navigation:
   - Mobile menu
   - Cart popup
   - Fixed promotion bar

4. Product Display:
   - Dynamic product grid
   - Add to cart functionality
   - Product images and descriptions

## Customization

1. Colors:
   - Edit CSS variables in `style.css`:
   ```css
   :root {
       --sage-green: #8BA888;
       --promotion-blue: #CBD3F9;
       --dark-purple: #483D8B;
       --dark-text: #333;
       --light-text: #666;
       --golden: #FFD700;
   }
   ```

2. Products:
   - Update `MENU_ITEMS` in `main.py` to modify products

3. Content:
   - Edit `index.html` to update text and images
   - Modify testimonials and business hours in the footer

## Mobile Testing

1. Verify display in portrait and landscape modes
2. Test menu and cart functionality
3. Check promotion bar visibility
4. Ensure proper spacing and alignment

## Production Deployment

1. Set environment variables:
   - SESSION_SECRET
   - DATABASE_URL (if using a database)

2. Update Google Maps iframe with your location

3. Replace placeholder images with your product photos

4. Update business information in the footer
