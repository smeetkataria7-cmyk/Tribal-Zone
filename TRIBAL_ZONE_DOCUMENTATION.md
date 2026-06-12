# Tribal Zone — Project Documentation

> **Brand:** Tribal Zone (`tribalzone.in`)
> **Type:** Indian fashion jewellery e-commerce (Shopify + static HTML preview)
> **Reference design:** liliorigin.com (authorized recreation)
> **Last updated:** June 2026

---

## 1. Project Overview

Tribal Zone is an Indian fashion jewellery brand selling earrings, necklaces, bangles, maang tikka, rings, zodiac and festive hamper collections. This project is a full Shopify-ready storefront with:

- **Static HTML/CSS/JS preview files** — for design and layout testing (no framework)
- **Shopify Liquid templates** — for the live store deployment (`sections/` and `snippets/`)
- **Reference design:** Lili Origin–style product-first layout (horizontal scroll carousels, clean white background, product cards with hover image-swap + visible "Add to Cart" + ratings + MRP strikethrough + % OFF)

---

## 2. Tech Stack

| Layer | Technology |
|---|---|
| Preview (design) | Pure HTML5 / CSS3 / Vanilla JS |
| Live store | Shopify Debut theme + Liquid |
| Fonts | Google Fonts — Poppins + Cormorant Garamond |
| Images | Unsplash (preview) → real product photos (live) |
| Version control | Git → GitHub (`smeetkataria7-cmyk/Tribal-Zone`) |
| Auto-deploy hook | `.claude/autopush.ps1` — pushes on every `git commit` |

---

## 3. Brand Design Tokens

| Token | CSS Variable | Value |
|---|---|---|
| Primary accent (hot pink) | `--gold` | `#F2157B` |
| Accent light | `--gold-lt` | `#f5488e` |
| Accent background tint | `--gold-bg` | `#fff0f8` |
| Near-black (dark text/bg) | `--dark` | `#120101` |
| Navy | `--navy` | `#162950` |
| Sale red | `--red` | `#ED1A43` |
| Success green | `--green` | `#27ae60` |
| Body font | `--sans` | `'Poppins', system-ui, sans-serif` |
| Display/serif font | `--serif` | `'Cormorant Garamond', Georgia, serif` |
| Logo file | — | `logo.png` (dragonfly + "TRIBAL ZONE" text) |

**Font weights loaded:** Poppins 300, 400, 500, 600 · Cormorant Garamond 300, 400, 600 (normal + italic)

---

## 4. File Structure

```
Tribal Zone/
├── index.html                    ← Homepage
├── product.html                  ← Product detail page
├── collection-earrings.html      ← Earrings collection
├── collection-necklaces.html     ← Necklaces collection
├── collection-bangles.html       ← Bangles & Bracelets
├── collection-maangtikka.html    ← Maang Tikka
├── collection-rings.html         ← Rings
├── collection-zodiac.html        ← Zodiac collection
├── collection-hampers.html       ← Festive Hampers (to build)
├── collection-sale.html          ← Sale page (to build)
├── logo.png                      ← Brand logo (dragonfly SVG)
├── REFERENCE_MAPPING.md          ← Lili Origin component map
├── TRIBAL_ZONE_DOCUMENTATION.md  ← This file
├── sections/
│   └── collection-template.liquid
├── snippets/
│   └── product-card-grid.liquid
└── .claude/
    ├── settings.json             ← Auto-push hook config
    └── autopush.ps1              ← PowerShell auto-push script
```

---

## 5. Page-by-Page Breakdown

### 5.1 `index.html` — Homepage

| Section | CSS Class | Description |
|---|---|---|
| Announce bar | `.announce` | Rotating 3-message strip (free shipping / gift / promo code) |
| Sticky header | `.hdr` | Logo left · search bar centre · wishlist + bag right |
| Category nav | `.cat-nav` | Horizontal scrollable nav with all 8 collections + Sale |
| Mobile drawer | `.mob-dr` | Hamburger-triggered slide-in nav |
| Cart drawer | `.cart-dr` | Slide-in cart from right with qty controls |
| Hero carousel | `.hero` | 3-slide auto-play carousel, arrows + dot nav |
| Perks strip | `.perks` | 5 trust icons: free shipping, anti-tarnish, India-made, returns, payments |
| Category circles | `.cats-scroll` | Horizontal scroll of 8 round category tiles |
| New Arrivals row | `#newArrivals` | Horizontal scroll product carousel |
| Earrings row | `#earringsSec` | Horizontal scroll product carousel |
| Offer banner | `.offer-banner` | Buy 1 Get 2 Free full-width promo strip |
| Necklaces row | `#necklacesSec` | Horizontal scroll product carousel |
| Collection banners | `.coll-banners` | 3-col editorial image banners (Bangles / Maang Tikka / Rings) |
| Bestsellers row | `#bestsellersSec` | Horizontal scroll product carousel |
| Zodiac row | `#zodiacSec` | Horizontal scroll product carousel |
| Trust strip | `.trust` | 4 stats: 5L+ customers · 500+ designs · 4.8★ · 20+ years |
| Newsletter | `.nl` | Email signup bar |
| Footer | `.footer` | 4-col: brand + 3 link columns + social icons + payment chips |

**Product data:** Defined in `var PRODUCTS = [...]` JS array. `makeCard()` generates each card HTML. `renderSection()` populates each carousel by filter.

---

### 5.2 `collection-earrings.html` — Collection Page

| Section | CSS Class | Description |
|---|---|---|
| Same header/nav/drawers | (shared) | Identical to homepage |
| Collection banner | `.coll-banner` | Full-width hero with collection name + product count |
| Active filter tags | `.active-filters` | Dismissable filter pills |
| Sidebar filters | `.sidebar` | 5 collapsible groups: Type, Price, Metal, Occasion, Rating |
| Sort dropdown | `.sort-select` | Sort by: Featured / Price low-high / Newest / Rating |
| Product count | `.prod-count` | "Showing X of Y products" |
| Product grid | `.prod-grid` | 3-col (desktop) / 2-col (mobile) product cards |
| Pagination | `.pagination` | Numbered + prev/next |
| Mobile filter drawer | `.filter-drawer` | Full-screen filter panel on mobile |

**JS filtering:** `tzFilterCards()` client-side filter. Products in `TZ_PRODUCTS` array.

**Same structure applies to:** `collection-necklaces.html`, `collection-bangles.html`, `collection-maangtikka.html`, `collection-rings.html`, `collection-zodiac.html`

---

### 5.3 `product.html` — Product Detail Page

| Section | CSS Class | Description |
|---|---|---|
| Same header/nav/drawers | (shared) | Identical to other pages |
| Breadcrumb | `.breadcrumb` | Home › Category › Product name |
| Image gallery | `.gallery` | 4-image gallery with thumbnail strip + prev/next arrows |
| Hover-to-zoom | JS on `#galleryMain` | Mouse-tracking 2.4× magnifier on main image |
| Product info | `.prod-info` | Brand · title · stars · price |
| Price row | `.prod-price-row` | Sale price · MRP strikethrough · % OFF badge |
| Offer tag | `.prod-offer-tag` | "Buy 1 Get 2 Free" promo pill |
| Variant selectors | `.variant-section` | Metal Finish (4 options) · Size (3 options) |
| Qty + Add to Bag | `.qty-row` | Stepper + dark "Add to Bag" button + wishlist |
| Buy Now | `.btn-buy` | Pink full-width CTA |
| Delivery info | `.delivery-box` | Free delivery / 7-day returns / skin-safe |
| Accordion | `.accordion` | Product Details · Care · Shipping · Why Tribal Zone |
| Reviews | `.reviews-sec` | Star breakdown bars + 4 customer review cards |
| Related products | `.related-row` | Horizontal scroll of 5 related product cards |
| Sticky mobile CTA | `.sticky-cta` | Fixed bar at bottom on mobile (< 900px) |

---

## 6. Shared Components (all pages)

### Header `.hdr`
```
[Logo] [Search bar ________________ 🔍] [♡] [👤] [🛍 Bag (0)]
```
- Logo: `<img src="logo.png">` height 44–48px
- Search: border-radius 4px, focus glow in `--gold`
- Bag: dark pill button, pink badge count

### Product Card `.pcard`
```
┌─────────────────┐
│   [BADGE]    [♡] │  ← badge top-left, wishlist top-right
│                  │
│   Product image  │  ← aspect-ratio: 1, hover swaps to 2nd image
│                  │
│ [ Add to Bag ]   │  ← slides up from bottom on hover
└─────────────────┘
CATEGORY
Product Name (2-line min-height)
★★★★★ 4.8 (128)
₹379          ← bold
₹699  −46%    ← grey strikethrough + red discount
✓ Free delivery
```

### Cart Drawer `.cart-dr`
- Opens on "Add to Bag" or clicking bag icon
- Shows items with image, name, variant, qty stepper, price, remove
- Footer: subtotal + "Proceed to Checkout" CTA

---

## 7. Navigation Links

| Label | File | Notes |
|---|---|---|
| New Arrivals | `index.html` | Homepage |
| Earrings | `collection-earrings.html` | With sub-dropdown: Jhumkas / Studs / Hoops / Chandbalis / Danglers |
| Necklaces | `collection-necklaces.html` | With sub-dropdown: Chokers / Long Chains / Layered Sets / Temple |
| Bangles & Bracelets | `collection-bangles.html` | |
| Maang Tikka | `collection-maangtikka.html` | |
| Rings | `collection-rings.html` | |
| Zodiac | `collection-zodiac.html` | |
| Festive Hampers | `collection-hampers.html` | Not yet built |
| Sale | `collection-sale.html` | Styled in `--red`, not yet built |
| All product cards | `product.html` | Single shared preview page |

---

## 8. Shopify Liquid Files

| File | Purpose |
|---|---|
| `sections/collection-template.liquid` | Collection page Shopify section — renders `product-card-grid` snippet per product |
| `snippets/product-card-grid.liquid` | Product card snippet — renders individual product cards in collection grids |

> **Sync rule:** Any layout or style changes made to HTML preview files must be mirrored in the corresponding Liquid files before deploying to the live Shopify store.

---

## 9. Git & Deployment

| Item | Detail |
|---|---|
| Remote | `https://github.com/smeetkataria7-cmyk/Tribal-Zone.git` |
| Branch | `main` |
| Auto-push | `.claude/autopush.ps1` — fires after every `git commit` via PostToolUse hook |
| Hook config | `.claude/settings.json` |

**Auto-push hook (PowerShell):**
Reads Claude's tool-use stdin JSON → checks if the bash command was a `git commit` → runs `git push` automatically. Replaced the original bash+jq version which didn't work on Windows.

---

## 10. Lili Origin Reference Mapping

| Lili Origin Component | Tribal Zone Implementation | Status |
|---|---|---|
| Announce bar (rotating) | All pages — `.announce` | ✅ |
| Sticky header | All pages — `.hdr` | ✅ |
| Desktop nav + dropdowns | All pages — `.nav` / `.cat-nav` | ✅ |
| Mobile hamburger drawer | All pages — `.mob-dr` | ✅ |
| Cart drawer (right slide-in) | All pages — `.cart-dr` | ✅ |
| Hero carousel | `index.html` — `.hero` | ✅ |
| Perks/trust strip | `index.html` — `.perks` | ✅ |
| Category circles | `index.html` — `.cats-scroll` | ✅ |
| Horizontal scroll product rows | `index.html` — multiple `psec-scroll` carousels | ✅ |
| Product card (hover image swap) | All pages — `.pcard` + `.i1/.i2` | ✅ |
| Product card quick-add (slide up) | All pages — `.pcard-atb` | ✅ |
| Product card wishlist heart | All pages — `.pcard-wish` | ✅ |
| Ratings + MRP strikethrough + % OFF | All pages — `.pcard-stars`, `.pcard-price` | ✅ |
| 3-col collection banners | `index.html` — `.coll-banners` | ✅ |
| Offer strip (B1G2) | `index.html` — `.offer-banner` | ✅ |
| Brand trust stats | `index.html` — `.trust` | ✅ |
| Newsletter signup | `index.html` — `.nl` | ✅ |
| Footer (4-col) | All pages — `.footer` | ✅ |
| Collection page banner | All collection pages — `.coll-banner` | ✅ |
| Left sidebar filters | Collection pages — `.sidebar` | ✅ |
| Active filter tags | Collection pages — `.active-filters` | ✅ |
| Sort dropdown | Collection pages — `.sort-select` | ✅ |
| 3-col product grid | Collection pages — `.prod-grid` | ✅ |
| Pagination | Collection pages — `.pagination` | ✅ |
| Mobile filter drawer | Collection pages — `.filter-drawer` | ✅ |
| Product image gallery + thumbnails | `product.html` — `.gallery` | ✅ |
| Hover-to-zoom magnifier | `product.html` — JS on `#galleryMain` | ✅ |
| Variant selectors | `product.html` — `.variant-section` | ✅ |
| Qty stepper | `product.html` — `.qty-ctrl` | ✅ |
| Add to Cart + Buy Now | `product.html` — `.btn-atc`, `.btn-buy` | ✅ |
| Delivery info box | `product.html` — `.delivery-box` | ✅ |
| Description/care accordion | `product.html` — `.accordion` | ✅ |
| Review rating bars | `product.html` — `.review-bars` | ✅ |
| Customer reviews grid | `product.html` — `.reviews-grid` | ✅ |
| Related products scroll | `product.html` — `.related-row` | ✅ |
| Sticky mobile CTA bar | `product.html` — `.sticky-cta` | ✅ |

---

## 11. Pages Status

| Page | File | Status |
|---|---|---|
| Homepage | `index.html` | ✅ Complete |
| Product Detail | `product.html` | ✅ Complete |
| Earrings | `collection-earrings.html` | ✅ Complete |
| Necklaces | `collection-necklaces.html` | ✅ Complete |
| Bangles & Bracelets | `collection-bangles.html` | ✅ Complete |
| Maang Tikka | `collection-maangtikka.html` | ✅ Complete |
| Rings | `collection-rings.html` | ✅ Complete |
| Zodiac | `collection-zodiac.html` | ✅ Complete |
| Festive Hampers | `collection-hampers.html` | 🔲 To build |
| Sale | `collection-sale.html` | 🔲 To build |

---

## 12. Known Issues & Fixes Applied

| Issue | Root Cause | Fix Applied |
|---|---|---|
| Logo showing as broken image in preview | Preview server can't serve local files | Use browser file:// or local server |
| Great Vibes font persisting on index | `--serif` var not updated | Removed Great Vibes from all imports + stacks |
| Hardcoded `#1c1c1c` remaining after theme change | CSS vars only updated, inline hex missed | `replace_all` across all files |
| Cross-referenced product images | Unsplash IDs reused across wrong categories | Audited all 14+ cards, assigned category-correct photos |
| Price row misaligned across cards | `flex-wrap` on price + varying name line count | `.pcard-name` gets `min-height: 2 lines`, price stacked vertically |
| Auto-push hook not firing (11h gap) | Hook used `jq` + `bash` — not available on Windows | Rewrote as PowerShell `.ps1` script |
| File not read error on Edit | Attempted Edit before Read in same session | Always Read before Edit |

---

## 13. Commit History (significant)

| Commit | Change |
|---|---|
| `2c3034e` | Fix auto-push hook for Windows — PowerShell script |
| `b9fd4d6` | Remove necklace photo from all earring cards |
| `8b92528` | Fix price row alignment — 2-line min-height on name |
| `e3bbb1c` | Fix cross-referenced images across all product cards |
| `94dca7b` | Fix price alignment — stack sale price above MRP |
| `eb0fca5` | Add hover-to-zoom magnifier on product gallery |
| `adf2f43` | Full Lili Origin-style redesign — index, collection, product |
| `cd607d7` | Remove Great Vibes — Poppins + Cormorant Garamond only |
| `5fbd760` | Fix hardcoded `#1c1c1c` across all pages |
