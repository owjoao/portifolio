# -*- coding: utf-8 -*-
import subprocess
import os

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

dest_png = r'f:\Nova pasta\site\assets\previews\arquiteto.png'
dest_jpg = r'f:\Nova pasta\site\assets\previews\preview_arquiteto.jpg'
url = 'http://localhost:8080/arquiteto/index.html'

cmd_png = f'"{edge_path}" --headless --disable-gpu --screenshot="{dest_png}" --window-size=1280,820 {url}'
cmd_jpg = f'"{edge_path}" --headless --disable-gpu --screenshot="{dest_jpg}" --window-size=1280,820 {url}'

subprocess.run(cmd_png, shell=True, timeout=20)
print('PNG size:', os.path.getsize(dest_png))

subprocess.run(cmd_jpg, shell=True, timeout=20)
print('JPG size:', os.path.getsize(dest_jpg))
print('Screenshot capture completed successfully!')
