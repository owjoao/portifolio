# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'assets/previews/[\w\-\.]+', text)
unique = sorted(set(matches))
print(f'Total unique preview image paths in index.html: {len(unique)}')
for u in unique:
    print(u)
