import os, json

with open('scripts/projects_catalog.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)

for k in cat:
    url = cat[k].get('url', k)
    niche = url.split('/')[0]
    if not os.path.exists(niche):
        continue
    
    img_files = []
    for root, dirs, files in os.walk(niche):
        if 'admin' in root or '.git' in root or '.kilo' in root:
            continue
        for f in files:
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg')):
                img_files.append(os.path.relpath(os.path.join(root, f), niche))
    
    print(f"{niche:22}: {len(img_files):2} images -> {img_files[:4]}")

