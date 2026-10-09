# -*- coding: utf-8 -*-
import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all cards and their preview images
card_pattern = r'onclick="openNetflixModal\(\'([^\']+)\'\)"[\s\S]*?<img src="([^"]+)"'
cards = re.findall(card_pattern, text)

print(f'Total cards found in index.html: {len(cards)}')
unique_cards = {}
for niche_id, img_src in cards:
    if niche_id not in unique_cards:
        unique_cards[niche_id] = []
    if img_src not in unique_cards[niche_id]:
        unique_cards[niche_id].append(img_src)

for niche_id, imgs in unique_cards.items():
    html_path = f"{niche_id}/index.html"
    exists = os.path.exists(html_path)
    print(f"{niche_id}: html_exists={exists}, imgs={imgs}")
