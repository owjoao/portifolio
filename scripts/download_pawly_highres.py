# -*- coding: utf-8 -*-
import urllib.request
import os

ASSETS_DIR = r"f:\Nova pasta\site\banho-e-tosa\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Curated high-res (1200px - 1600px) Unsplash pet photos with crystal-clear professional photography
PHOTO_URLS = {
    # Hero: Golden retriever and cat cuddling together on couch
    "hero-pets-clean.jpg": "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=1600&auto=format&fit=crop&q=90",
    "hero-pets.jpg": "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=1600&auto=format&fit=crop&q=90",
    
    # Golden retriever happy family
    "dog-familia.jpg": "https://images.unsplash.com/photo-1552053831-71594a27632d?w=1200&auto=format&fit=crop&q=90",
    
    # Promo banner: cute pet with toy/treat
    "promo-banner-art.jpg": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=1200&auto=format&fit=crop&q=90",
    
    # Categories:
    "cat-racoes.jpg": "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=800&auto=format&fit=crop&q=90",
    "cat-brinquedos.jpg": "https://images.unsplash.com/photo-1576201836106-db1758fd1c97?w=800&auto=format&fit=crop&q=90",
    "cat-banho.jpg": "https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?w=800&auto=format&fit=crop&q=90",
    "cat-acessorios.jpg": "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=800&auto=format&fit=crop&q=90",
    "cat-adocao.jpg": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=800&auto=format&fit=crop&q=90",
    "cat-petiscos.jpg": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=800&auto=format&fit=crop&q=90",
    "cat-saude.jpg": "https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?w=800&auto=format&fit=crop&q=90",
    "cat-camas.jpg": "https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?w=800&auto=format&fit=crop&q=90",

    # Review Avatars: real high-res people with pets
    "avatar-mariana.jpg": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&auto=format&fit=crop&q=90",
    "avatar-carlos.jpg": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&auto=format&fit=crop&q=90",
    "avatar-fernanda.jpg": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=90",

    # Adoption Pets
    "pet-thor.jpg": "https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=800&auto=format&fit=crop&q=90",
    "pet-luna.jpg": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&auto=format&fit=crop&q=90",
    "pet-mel.jpg": "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?w=800&auto=format&fit=crop&q=90",

    # Products:
    "prod-racao.jpg": "https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?w=800&auto=format&fit=crop&q=90",
    "prod-brinquedo.jpg": "https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?w=800&auto=format&fit=crop&q=90",
    "prod-cama.jpg": "https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?w=800&auto=format&fit=crop&q=90",
    "prod-higiene.jpg": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=800&auto=format&fit=crop&q=90",

    # Life stages:
    "fase-filhotes.jpg": "https://images.unsplash.com/photo-1591160690555-5debfba289f0?w=800&auto=format&fit=crop&q=90",
    "fase-adultos.jpg": "https://images.unsplash.com/photo-1530281700549-e82e7bf110d6?w=800&auto=format&fit=crop&q=90",
    "fase-senior.jpg": "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=800&auto=format&fit=crop&q=90",
    "fase-gatos.jpg": "https://images.unsplash.com/photo-1513360309081-38f076278f1e?w=800&auto=format&fit=crop&q=90",
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in PHOTO_URLS.items():
    dest = os.path.join(ASSETS_DIR, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
        print(f"Downloaded {fname}: {len(data)} bytes")
    except Exception as e:
        print(f"Error downloading {fname}: {e}")

print("All high-res images processed.")
