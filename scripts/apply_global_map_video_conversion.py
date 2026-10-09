# -*- coding: utf-8 -*-
import os
import sys

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__)))
from sites_configs import SITE_CONFIGS
from components_builder import build_map_section, build_video_modal, build_mobile_sticky, build_js_helpers

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

results = []

for site_key, cfg in SITE_CONFIGS.items():
    html_path = os.path.join(base_dir, site_key, "index.html")
    if not os.path.exists(html_path):
        print(f"Skipping {site_key}: file not found.")
        continue
    
    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    
    modified = False
    
    # 1. Add São Paulo Map Section if not present
    if 'id="localizacao"' not in html and 'pb=!1m18!1m12!1m3!1d3657.098485293405!2d-46.6549887237894' not in html:
        map_html = build_map_section(cfg)
        # Insert before footer
        if '<footer' in html:
            html = html.replace('<footer', map_html + '\n  <footer', 1)
            modified = True
            print(f"[{site_key}] Added São Paulo Map section before <footer>")
        else:
            print(f"[{site_key}] Warning: <footer> tag not found for map insertion")
    else:
        print(f"[{site_key}] Map section already present")

    # 2. Add Video & Qualidade de Vida Modal
    if 'id="video-qv-modal"' not in html:
        video_modal_html = build_video_modal(cfg)
        if '</body>' in html:
            html = html.replace('</body>', video_modal_html + '\n</body>', 1)
            modified = True
            print(f"[{site_key}] Added Video Qualidade de Vida Modal")
    else:
        print(f"[{site_key}] Video modal already present")

    # 3. Add Mobile Bottom Sticky Bar
    if '<!-- MOBILE BOTTOM STICKY BAR' not in html and 'MOBILE BOTTOM STICKY BAR' not in html:
        sticky_html = build_mobile_sticky(cfg)
        if '</body>' in html:
            html = html.replace('</body>', sticky_html + '\n</body>', 1)
            modified = True
            print(f"[{site_key}] Added Mobile Bottom Sticky Bar")

    # 4. Add JS Helpers
    if 'function openVideoQvModal' not in html:
        js_helpers = build_js_helpers(cfg)
        if '</body>' in html:
            html = html.replace('</body>', js_helpers + '\n</body>', 1)
            modified = True
            print(f"[{site_key}] Added JS Helpers (openVideoQvModal, scrollToFormFast)")

    # 5. Add Hero Video Trigger Button if not present
    if 'openVideoQvModal()' not in html:
        # Look for first Hero or CTA section
        hero_btn = f"""
        <!-- Botão Vídeo Qualidade de Vida -->
        <button onclick="openVideoQvModal()" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-full bg-emerald-600/90 hover:bg-emerald-500 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-lg hover:scale-105 cursor-pointer z-20">
          <i class="fa-solid fa-circle-play text-white text-sm animate-pulse"></i>
          <span>Vídeo: Qualidade de Vida & Bem-Estar</span>
        </button>
        """
        # Find where to inject in Hero:
        injected_hero = False
        for cta_pattern in ['href="https://wa.me', 'href="#contato"', 'href="#agendamento"', 'href="#orcamento"', 'href="#simulador"']:
            pos = html.find(cta_pattern)
            if pos != -1:
                # Find the closing tag </a> of this button
                end_tag = html.find('</a>', pos)
                if end_tag != -1:
                    html = html[:end_tag+4] + '\n' + hero_btn + html[end_tag+4:]
                    injected_hero = True
                    modified = True
                    print(f"[{site_key}] Injected Video Button next to primary CTA")
                    break
        if not injected_hero:
            # Fallback: inject floating video quality badge on bottom left
            floating_btn = f"""
            <button onclick="openVideoQvModal()" class="fixed bottom-20 left-4 z-40 hidden sm:inline-flex items-center gap-2 px-4 py-2.5 rounded-full bg-slate-900/95 hover:bg-black text-white border border-emerald-500/40 font-bold text-xs shadow-2xl transition hover:scale-105" title="Assistir ao Vídeo">
              <i class="fa-solid fa-circle-play text-emerald-400 text-base animate-pulse"></i>
              <span>Vídeo: Qualidade de Vida</span>
            </button>
            """
            html = html.replace('</body>', floating_btn + '\n</body>', 1)
            modified = True
            print(f"[{site_key}] Injected floating Video Button")

    if modified:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        results.append(site_key)

print(f"\nFinished processing! Total sites updated: {len(results)} / {len(SITE_CONFIGS)}")
