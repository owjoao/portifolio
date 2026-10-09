# -*- coding: utf-8 -*-
import subprocess
import os
from PIL import Image

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

test_sites = [
    ('banho-e-tosa', 'file:///f:/Nova%20pasta/site/banho-e-tosa/index.html', 'f:/Nova pasta/site/assets/previews/banho-e-tosa.png'),
    ('barbearia', 'file:///f:/Nova%20pasta/site/barbearia/index.html', 'f:/Nova pasta/site/assets/previews/barbearia.png'),
    ('arquiteto', 'file:///f:/Nova%20pasta/site/arquiteto/index.html', 'f:/Nova pasta/site/assets/previews/arquiteto.png'),
]

for niche_id, url, dest in test_sites:
    cmd = f'"{edge_path}" --headless --disable-gpu --screenshot="{dest}" --window-size=1280,2400 "{url}"'
    subprocess.run(cmd, shell=True, timeout=20)
    if os.path.exists(dest):
        im = Image.open(dest)
        print(f'{niche_id}: dimensions={im.size}, size={os.path.getsize(dest)} bytes')

print('Test completed successfully!')
