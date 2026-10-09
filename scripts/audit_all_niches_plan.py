import os, json, re
from bs4 import BeautifulSoup

with open('scripts/projects_catalog.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)

niches = list(cat.keys())

report = []
for k in niches:
    url = cat[k].get('url', k)
    niche_dir = url.split('/')[0]
    index_path = os.path.join(niche_dir, 'index.html')
    if not os.path.exists(index_path):
        continue

    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check images
    imgs = [img.get('src') for img in soup.find_all('img') if img.get('src')]
    local_imgs = [i for i in imgs if not i.startswith(('http', 'data:'))]
    external_imgs = [i for i in imgs if i.startswith('http')]
    missing_local = [i for i in local_imgs if not os.path.exists(os.path.join(niche_dir, i.split('?')[0].split('#')[0]))]

    # Check animations
    has_gsap = 'gsap' in html.lower() or 'scrolltrigger' in html.lower()
    has_anime = 'anime' in html.lower()
    has_motion = 'motion' in html.lower() or 'framer' in html.lower() or 'aos' in html.lower()

    # Check interactive elements
    has_faq_accordion = 'faq' in html.lower() and ('accordion' in html.lower() or 'details' in html.lower() or 'toggle' in html.lower())
    has_tabs = 'tab' in html.lower()
    has_before_after = 'before' in html.lower() and 'after' in html.lower() or 'antes' in html.lower() and 'depois' in html.lower()
    has_carousel = 'carousel' in html.lower() or 'swiper' in html.lower() or 'slider' in html.lower() or 'scroll' in html.lower()

    # Check SEO / Meta
    has_schema = 'application/ld+json' in html.lower()
    has_geo = 'geo.position' in html.lower() or 'geo.region' in html.lower()
    has_meta_desc = bool(soup.find('meta', attrs={'name': 'description'}))

    # Check WA contact
    has_wa = '99929' in html or '5532999292311' in html

    report.append({
        'niche': niche_dir,
        'title': cat[k].get('title'),
        'total_imgs': len(imgs),
        'missing_imgs': len(missing_local),
        'missing_list': missing_local[:3],
        'has_gsap': has_gsap,
        'has_schema': has_schema,
        'has_faq': has_faq_accordion,
        'has_wa': has_wa
    })

print(f"{'NICHE':22} | {'IMGS':4} | {'MISSING':7} | {'GSAP':5} | {'SCHEMA':6} | {'FAQ':5} | {'WA':5}")
print("-" * 70)
for r in report:
    print(f"{r['niche']:22} | {r['total_imgs']:4} | {r['missing_imgs']:7} | {str(r['has_gsap']):5} | {str(r['has_schema']):6} | {str(r['has_faq']):5} | {str(r['has_wa']):5}")

