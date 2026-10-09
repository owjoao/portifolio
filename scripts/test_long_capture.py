# -*- coding: utf-8 -*-
import subprocess
from PIL import Image
import os

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

test_dest = r'f:\Nova pasta\site\test_long_preview.png'
url = 'file:///f:/Nova%20pasta/site/barbearia/index.html'

cmd = f'"{edge_path}" --headless --disable-gpu --screenshot="{test_dest}" --window-size=1280,2400 "{url}"'
subprocess.run(cmd, shell=True, timeout=20)

if os.path.exists(test_dest):
    im = Image.open(test_dest)
    print('Long screenshot dimensions:', im.size, 'File size:', os.path.getsize(test_dest))
    os.remove(test_dest)
else:
    print('Failed to capture test screenshot')
