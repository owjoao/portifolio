# -*- coding: utf-8 -*-
import re
import os

with open('arquiteto/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

wpp_links = re.findall(r'href=["\'](https://wa\.me/[^"\']+)["\']', text)
print(f'Total WhatsApp CTA links found: {len(wpp_links)}')

correct_target = 'https://wa.me/5532999292311?text=gostei%20desse%20site%2C%20qual%20o%20valor%3F'

all_ok = True
for i, l in enumerate(wpp_links):
    if l == correct_target:
        print(f'  [OK] CTA Link {i+1}: Validated successfully')
    else:
        print(f'  [ERR] CTA Link {i+1}: MISMATCH -> {l}')
        all_ok = False

imgs = set(re.findall(r'assets/[\w\-\.]+', text))
print(f'\nTotal unique local images referenced: {len(imgs)}')
for img in sorted(imgs):
    path = os.path.join('arquiteto', img)
    exists = os.path.exists(path)
    size = os.path.getsize(path) if exists else 0
    status = 'OK' if exists and size > 0 else 'MISSING'
    print(f'  [{status}] {img} ({size} bytes)')
    if not exists or size == 0:
        all_ok = False

if all_ok:
    print('\n===> AUDIT 100% PASSED: All links and images verified! <===')
else:
    print('\n===> AUDIT FAILED! <===')
