# -*- coding: utf-8 -*-
import subprocess
import os
import time

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

dest_png = r'f:\Nova pasta\site\assets\previews\barbearia.png'
dest_jpg = r'f:\Nova pasta\site\assets\previews\preview_barbearia.jpg'
url = 'file:///f:/Nova%20pasta/site/barbearia/index.html'

cmd_png = f'"{edge_path}" --headless --disable-gpu --screenshot="{dest_png}" --window-size=1280,820 "{url}"'
cmd_jpg = f'"{edge_path}" --headless --disable-gpu --screenshot="{dest_jpg}" --window-size=1280,820 "{url}"'

subprocess.run(cmd_png, shell=True, timeout=20)
subprocess.run(cmd_jpg, shell=True, timeout=20)

print('Updated PNG size:', os.path.getsize(dest_png), 'Modified:', time.ctime(os.path.getmtime(dest_png)))
print('Updated JPG size:', os.path.getsize(dest_jpg), 'Modified:', time.ctime(os.path.getmtime(dest_jpg)))

