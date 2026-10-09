# -*- coding: utf-8 -*-
import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
base_dir = r"f:\Nova pasta\site"
html_abs = os.path.join(base_dir, "podologo", "index.html")
preview_custom = os.path.join(base_dir, "podologo", "assets", "preview_podosaude_full.jpg")
preview_portfolio = os.path.join(base_dir, "assets", "previews", "preview_podologo.jpg")

url = f"file:///{html_abs.replace(os.sep, '/')}"

cmd = f'"{edge_path}" --headless --disable-gpu --screenshot="{preview_custom}" --window-size=1280,6600 "{url}"'
subprocess.run(cmd, shell=True, timeout=25, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

cmd2 = f'"{edge_path}" --headless --disable-gpu --screenshot="{preview_portfolio}" --window-size=1280,3200 "{url}"'
subprocess.run(cmd2, shell=True, timeout=25, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.path.exists(preview_custom):
    print("Full preview updated:", os.path.getsize(preview_custom)//1024, "KB")
if os.path.exists(preview_portfolio):
    print("Portfolio preview updated:", os.path.getsize(preview_portfolio)//1024, "KB")

