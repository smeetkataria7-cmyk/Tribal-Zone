#!/usr/bin/env python3
"""
Convert Tribal Zone inventory to HTML product cards.
Usage: python inventory-to-html.py [category] [output-file]
"""

import pandas as pd
import json
import sys

def read_inventory(filename='New Style Inventory.xlsx'):
    """Read all category sheets from inventory"""
    return pd.read_excel(filename, sheet_name=None)

def generate_product_objects(category_name, df):
    """Convert DataFrame to product objects for JS array"""
    products = []
    for _, row in df.iterrows():
        if pd.isna(row['SKU']):
            continue

        product = {
            'id': str(row['SKU']),
            'title': str(row['Product Name']),
            'category': category_name,
            'color': str(row['Colour']),
            'price': int(row['MRP']) if pd.notna(row['MRP']) else 0,
            'compareAtPrice': int(row['MRP'] * 1.15) if pd.notna(row['MRP']) else 0,
            'quantity': int(row['Quantity']) if pd.notna(row['Quantity']) else 0,
            'barcode': str(row['Barcode']) if pd.notna(row['Barcode']) else '',
            'image': str(row['Image']) if pd.notna(row['Image']) else '',
            'featured': row['Upload'] == 'Done' if pd.notna(row['Upload']) else False,
        }
        products.append(product)
    return products

def generate_html_cards(category, products, limit=None):
    """Generate HTML for product cards"""
    html = f'\n<!-- {category.upper()} -->\n'

    if limit:
        products = products[:limit]

    for prod in products:
        price = prod['price']
        compare = prod['compareAtPrice']
        discount = int((compare - price) / compare * 100) if compare > 0 else 0

        html += f'''
        <a class="pcard" href="product.html">
          <div class="pcard-img">
            <img class="i1" src="https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70" alt="{prod['title']}"/>
            <img class="i2" src="https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70" alt="hover"/>
            <button class="pcard-wish" onclick="event.preventDefault();toggleWish(this)">♡</button>
            <div class="pcard-atb">Add to Bag</div>
          </div>
          <div class="pcard-info">
            <span class="pcard-badge b-new">New</span>
            <div class="pcard-cat">{category}</div>
            <div class="pcard-name">{prod['title']}</div>
            <div class="pcard-price"><span class="p-now">₹{price}</span><div class="p-meta"><span class="p-was">₹{compare}</span><span class="p-off">{discount}% OFF</span></div></div>
            <div class="pcard-stars">★★★★★ <span>(128)</span></div>
          </div>
        </a>
'''

    return html

def generate_js_array(all_products):
    """Generate JavaScript PRODUCTS array"""
    js = "var PRODUCTS = [\n"

    for prod in all_products:
        js += f'''  {{
    id: '{prod['id']}',
    title: '{prod['title'].replace("'", "\\'")}',
    category: '{prod['category']}',
    price: {prod['price']},
    compareAtPrice: {prod['compareAtPrice']},
    featured: {str(prod['featured']).lower()},
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  }},
'''

    js += "];"
    return js

def main():
    sheets = read_inventory()
    all_products = []

    # Skip Master sheet
    for category in ['Earrings', 'Necklaces', 'Bangles', 'Maang Tikka', 'Rings', 'Zodiac']:
        if category in sheets:
            df = sheets[category].dropna(subset=['SKU'])
            products = generate_product_objects(category, df)
            all_products.extend(products)
            print("[OK] {}: {} products".format(category, len(products)))

    # Generate outputs
    js_code = generate_js_array(all_products)
    with open('_product-data.js', 'w', encoding='utf-8') as f:
        f.write(js_code)

    # Generate sample HTML for each category
    html_output = '<div class="products-export">\n'
    for category in ['Earrings', 'Necklaces', 'Bangles', 'Maang Tikka', 'Rings', 'Zodiac']:
        if category in sheets:
            df = sheets[category].dropna(subset=['SKU'])
            products = generate_product_objects(category, df)
            html_output += generate_html_cards(category, products, limit=5)

    html_output += '\n</div>'

    with open('_products-sample.html', 'w', encoding='utf-8') as f:
        f.write(html_output)

    print("\n[DONE] Generated:")
    print("   - _product-data.js (JS array with {} products)".format(len(all_products)))
    print("   - _products-sample.html (sample cards)")
    print("\nUse in HTML: <script src='_product-data.js'></script>")

if __name__ == '__main__':
    main()
