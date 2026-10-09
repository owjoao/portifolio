# -*- coding: utf-8 -*-
from PIL import Image
import urllib.request
import os

ASSETS_DIR = r"f:\Nova pasta\site\arquiteto\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

mockup_path = r"C:\Users\jvna1\.gemini\antigravity\brain\b28a8cf9-f9da-40fd-96f7-f4464143af22\.user_uploaded\media_1790808040134.jpg"
im = Image.open(mockup_path)
w, h = im.size

# Let's crop key segments from the mockup for exact visual reference
# 1. Hero right/background with the 3D wall art and sofa (y: 20 to 285)
hero_crop = im.crop((int(w * 0.35), int(h * 0.03), w, int(h * 0.285)))
hero_crop.save(os.path.join(ASSETS_DIR, "mockup-hero-art.jpg"), quality=95)

# 2. Promo banner bedroom (y: 625 to 725)
promo_crop = im.crop((0, int(h * 0.625), int(w * 0.45), int(h * 0.725)))
promo_crop.save(os.path.join(ASSETS_DIR, "mockup-promo-bedroom.jpg"), quality=95)

# High-resolution Unsplash assets for ArtVista Wall Art & Interior Design
PHOTO_URLS = {
    # Hero: Ultra-luxurious living room with stunning backlit sculptural wall art and modern sofa
    "hero-wall-art.jpg": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&auto=format&fit=crop&q=90",
    "hero-room-ambience.jpg": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600&auto=format&fit=crop&q=90",

    # Collections:
    # Nature
    "col-nature.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=90",
    # Abstract
    "col-abstract.jpg": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800&auto=format&fit=crop&q=90",
    # Animals (Lion sculpture / art)
    "col-animals.jpg": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=800&auto=format&fit=crop&q=90",
    # Cities (Skyline)
    "col-cities.jpg": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=90",
    # 3D Art (Geometric sculpture / architectural relief)
    "col-3d-art.jpg": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800&auto=format&fit=crop&q=90",

    # Best Sellers:
    # 1. Golden Horizon
    "prod-golden-horizon.jpg": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=900&auto=format&fit=crop&q=90",
    # 2. Elegant Lion
    "prod-elegant-lion.jpg": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=900&auto=format&fit=crop&q=90",
    # 3. Golden Lines
    "prod-golden-lines.jpg": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=900&auto=format&fit=crop&q=90",
    # 4. Mountain Escape
    "prod-mountain-escape.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=900&auto=format&fit=crop&q=90",

    # Promo Banner: Luxury master bedroom with gold/warm lighting and wall art
    "promo-bedroom.jpg": "https://images.unsplash.com/photo-1540518614846-7ede433c4550?w=1400&auto=format&fit=crop&q=90",

    # Real Homes Inspiration (4 photos):
    "inspire-1.jpg": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=900&auto=format&fit=crop&q=90",
    "inspire-2.jpg": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=900&auto=format&fit=crop&q=90",
    "inspire-3.jpg": "https://images.unsplash.com/photo-1617806118233-18e1de247200?w=900&auto=format&fit=crop&q=90",
    "inspire-4.jpg": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=900&auto=format&fit=crop&q=90",

    # Reviews Avatars:
    "avatar-sarah.jpg": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=90",
    "avatar-james.jpg": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&auto=format&fit=crop&q=90",
    "avatar-emily.jpg": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&auto=format&fit=crop&q=90",
}

headers = {'User-Agent': 'Mozilla/5.0'}

for fname, url in PHOTO_URLS.items():
    dest = os.path.join(ASSETS_DIR, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            with open(dest, 'wb') as f:
                f.write(resp.read())
        print(f"Downloaded {fname} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"Error {fname}: {e}")

print("Assets ready for ArtVista!")
