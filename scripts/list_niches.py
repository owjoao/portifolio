# -*- coding: utf-8 -*-
import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const NICHES_DATA = (\[[\s\S]*?\]);', text)
if m:
    niches = json.loads(m.group(1))
    print(f'Total niches in NICHES_DATA: {len(niches)}')
    for n in niches:
        print(f"- {n.get('id')}: {n.get('publicUrl')}")
else:
    print('NICHES_DATA not found')
