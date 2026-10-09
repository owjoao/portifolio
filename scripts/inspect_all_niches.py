import os, json

with open('scripts/projects_catalog.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)

print(f"Total catalog projects: {len(cat)}")
for k, v in list(cat.items()):
    url = v.get('url', k)
    niche_dir = url.split('/')[0]
    exists = os.path.exists(niche_dir)
    title = v.get('title', '')
    index_path = os.path.join(niche_dir, 'index.html')
    has_index = os.path.exists(index_path)
    size = os.path.getsize(index_path) if has_index else 0
    print(f"{niche_dir:25}: exists={exists} | has_index={has_index} (size={size:6} bytes) | title={title}")

