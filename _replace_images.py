"""
Replace all Unsplash placeholder images with real Shopify CDN product images.
Fetches product catalog from tribalzone.in and maps images to HTML files.
"""
import json
import re
import urllib.request
import os

BASE = r'C:\Users\smeet\OneDrive\Desktop\Tribal Zone'
CDN = 'https://cdn.shopify.com/s/files/1/0301/2793/files/'

# ── Fetch all products from Shopify ──────────────────────────────
def fetch_products():
    products = []
    page = 1
    while True:
        url = f'https://www.tribalzone.in/products.json?limit=250&page={page}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        if not data.get('products'):
            break
        products.extend(data['products'])
        if len(data['products']) < 250:
            break
        page += 1
    return products

print("Fetching products from Shopify...")
products = fetch_products()
print(f"  Got {len(products)} products")

# ── Build image pools by category ────────────────────────────────
# Each product has images; first image = _1 (main), second = _2 (hover)
earring_imgs = []
necklace_imgs = []
ring_imgs = []
all_imgs = []

for p in products:
    imgs = [img['src'] for img in p.get('images', [])]
    if len(imgs) < 2:
        continue
    entry = {'title': p['title'], 'img1': imgs[0], 'img2': imgs[1], 'all': imgs}
    all_imgs.append(entry)

    title_lower = p['title'].lower()
    handle_lower = p.get('handle', '').lower()
    product_type = p.get('product_type', '').lower()

    if any(kw in title_lower or kw in handle_lower or kw in product_type
           for kw in ['earring', 'hoop', 'stud', 'jhumka', 'drop earring']):
        earring_imgs.append(entry)
    elif any(kw in title_lower or kw in handle_lower or kw in product_type
             for kw in ['necklace', 'pendant', 'chain']):
        necklace_imgs.append(entry)
    elif any(kw in title_lower or kw in handle_lower or kw in product_type
             for kw in ['ring', 'band']):
        ring_imgs.append(entry)

print(f"  Earring images: {len(earring_imgs)}")
print(f"  Necklace images: {len(necklace_imgs)}")
print(f"  Ring images: {len(ring_imgs)}")
print(f"  All images: {len(all_imgs)}")

# ── Helper: pick images round-robin from a pool ──────────────────
def make_picker(pool):
    if not pool:
        pool = all_imgs  # fallback
    idx = [0]
    def pick():
        entry = pool[idx[0] % len(pool)]
        idx[0] += 1
        return entry
    return pick

# ── Count unsplash URLs in a string ──────────────────────────────
def count_unsplash(text):
    return len(re.findall(r'https://images\.unsplash\.com/[^\s\'")\]]+', text))

# ── Replace unsplash URLs in file, return (before, after) counts ─
def process_file(filepath, description=""):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    before = count_unsplash(content)
    if before == 0:
        return 0, 0

    # Find all unique unsplash URLs
    urls = re.findall(r'https://images\.unsplash\.com/[^\s\'")\]]+', content)

    # Build replacement map: each unique unsplash URL -> a Shopify image
    unique_urls = list(dict.fromkeys(urls))  # preserve order, dedupe

    # For each file, use appropriate category pool
    fname = os.path.basename(filepath).lower()
    if 'earring' in fname:
        picker = make_picker(earring_imgs)
    elif 'necklace' in fname:
        picker = make_picker(necklace_imgs)
    elif 'ring' in fname:
        picker = make_picker(ring_imgs)
    elif 'bangle' in fname or 'maangtikka' in fname or 'zodiac' in fname:
        picker = make_picker(all_imgs)
    elif 'product' in fname:
        picker = make_picker(earring_imgs)
    elif 'index' in fname:
        picker = make_picker(all_imgs)
    else:
        picker = make_picker(all_imgs)

    replacements = {}
    for url in unique_urls:
        entry = picker()
        # Determine if this is a _1 or _2 context based on URL usage patterns
        # For simplicity: first occurrence of each unique URL gets img1
        replacements[url] = entry['img1']

    # Now do smarter replacement: for i1/i2 pairs and img property pairs
    new_content = content

    # Strategy: Find all unsplash URLs and replace them sequentially
    # using round-robin from the pool, but pair i1/i2 from same product

    # For static HTML cards with i1/i2 pattern:
    # <img class="i1" src="UNSPLASH_1" .../> <img class="i2" src="UNSPLASH_2" .../>
    i1_i2_pattern = re.compile(
        r'(<img\s+class="i1"\s+src=")([^"]+unsplash[^"]+)("[^/]*/>\s*'
        r'<img\s+class="i2"\s+src=")([^"]+unsplash[^"]+)(")',
        re.DOTALL
    )

    card_picker = make_picker(earring_imgs if 'earring' in fname else
                              necklace_imgs if 'necklace' in fname else
                              ring_imgs if 'ring' in fname else all_imgs)

    def replace_i1_i2(m):
        entry = card_picker()
        return m.group(1) + entry['img1'] + m.group(3) + entry['img2'] + m.group(5)

    new_content = i1_i2_pattern.sub(replace_i1_i2, new_content)

    # For JS TZ_PRODUCTS arrays with img: property (single image)
    js_img_pattern = re.compile(r"(img:')([^']*unsplash[^']*)(')")

    js_picker = make_picker(earring_imgs if 'earring' in fname else
                            necklace_imgs if 'necklace' in fname else
                            ring_imgs if 'ring' in fname else all_imgs)

    def replace_js_img(m):
        entry = js_picker()
        return m.group(1) + entry['img1'] + m.group(3)

    new_content = js_img_pattern.sub(replace_js_img, new_content)

    # For _product-data.js with image1/image2 properties
    img12_pattern = re.compile(
        r"(image1:\s*')([^']*unsplash[^']*)('\s*,\s*\n\s*image2:\s*')([^']*unsplash[^']*)(')",
        re.DOTALL
    )

    data_picker = make_picker(earring_imgs if 'earring' in fname or 'product-data' in fname else all_imgs)

    def replace_img12(m):
        entry = data_picker()
        return m.group(1) + entry['img1'] + m.group(3) + entry['img2'] + m.group(5)

    new_content = img12_pattern.sub(replace_img12, new_content)

    # For hero/banner background images
    hero_pattern = re.compile(r"(background-image:\s*url\(['\"]?)([^'\")\s]*unsplash[^'\")\s]*)(['\"]?\))")
    hero_picker = make_picker(all_imgs)

    def replace_hero(m):
        entry = hero_picker()
        # Use a larger image for heroes
        url = entry['img1']
        return m.group(1) + url + m.group(3)

    new_content = hero_pattern.sub(replace_hero, new_content)

    # For banner <img> tags (coll-banner-bg)
    banner_pattern = re.compile(r'(<img[^>]*class="[^"]*banner[^"]*"[^>]*src=")([^"]*unsplash[^"]*)(")')
    banner_picker = make_picker(all_imgs)

    def replace_banner(m):
        entry = banner_picker()
        return m.group(1) + entry['img1'] + m.group(3)

    new_content = banner_pattern.sub(replace_banner, new_content)

    # Also try the reverse order: src before class
    banner_pattern2 = re.compile(r'(<img[^>]*src=")([^"]*unsplash[^"]*)("[^>]*class="[^"]*banner[^"]*")')
    def replace_banner2(m):
        entry = banner_picker()
        return m.group(1) + entry['img1'] + m.group(3)
    new_content = banner_pattern2.sub(replace_banner2, new_content)

    # For zodiac IMGS array
    imgs_array_pattern = re.compile(r"(var IMGS=\[)([^\]]+)(\])")
    def replace_imgs_array(m):
        # 12 zodiac signs need 12 images
        picker = make_picker(all_imgs)
        urls = []
        for _ in range(12):
            entry = picker()
            urls.append(f"'{entry['img1']}'")
        return m.group(1) + ','.join(urls) + m.group(3)
    new_content = imgs_array_pattern.sub(replace_imgs_array, new_content)

    # For product.html gallery images (JS array)
    gallery_pattern = re.compile(r"(var galImgs\s*=\s*\[|const galImgs\s*=\s*\[|'https://images\.unsplash\.com/[^']*')")

    # For remaining unsplash URLs (cart items, category tiles, gallery thumbs, etc.)
    # Replace any remaining ones with round-robin from all pool
    remaining_picker = make_picker(all_imgs)

    def replace_remaining(m):
        entry = remaining_picker()
        return entry['img1']

    remaining = re.compile(r'https://images\.unsplash\.com/[^\s\'")\]]+')
    new_content = remaining.sub(replace_remaining, new_content)

    after = count_unsplash(new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return before, after

# ── Process all target files ─────────────────────────────────────
target_files = [
    'index.html',
    'collection-earrings.html',
    'collection-necklaces.html',
    'collection-bangles.html',
    'collection-maangtikka.html',
    'collection-rings.html',
    'collection-zodiac.html',
    'product.html',
    '_product-data.js',
]

total_before = 0
total_after = 0

print("\n--- Replacing Unsplash images ---")
for fname in target_files:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"  SKIP {fname} (not found)")
        continue
    before, after = process_file(fpath)
    total_before += before
    total_after += after
    print(f"  {fname}: {before} unsplash -> {after} remaining")

print(f"\n=== TOTAL: {total_before} unsplash URLs before, {total_after} remaining ===")

# Also check other files that had unsplash
for extra in ['preview-collection.html', '_products-sample.html', 'inventory-to-html.py']:
    fpath = os.path.join(BASE, extra)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = count_unsplash(f.read())
        if c > 0:
            print(f"  NOTE: {extra} still has {c} unsplash URLs (not modified)")
