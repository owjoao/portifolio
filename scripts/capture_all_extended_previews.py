# -*- coding: utf-8 -*-
import subprocess
import os
import time

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

BASE_DIR = r'f:\Nova pasta\site'

SITES = [
    ('advogado', 'advogado/index.html', 'assets/previews/advogado.png'),
    ('arquiteto', 'arquiteto/index.html', 'assets/previews/arquiteto.png'),
    ('banho-e-tosa', 'banho-e-tosa/index.html', 'assets/previews/banho-e-tosa.png'),
    ('barbearia', 'barbearia/index.html', 'assets/previews/barbearia.png'),
    ('concessionaria-honda', 'concessionaria-honda/index.html', 'assets/previews/concessionaria-honda.png'),
    ('corretor-imoveis', 'corretor-imoveis/index.html', 'assets/previews/corretor-imoveis.png'),
    ('dentista', 'dentista/index.html', 'assets/previews/dentista.png'),
    ('energia-solar', 'energia-solar/index.html', 'assets/previews/energia-solar.png'),
    ('acupunturista', 'acupunturista/index.html', 'assets/previews/preview_acupunturista.jpg'),
    ('boteco-portugues', 'boteco-portugues/index.html', 'assets/previews/preview_boteco_portugues.jpg'),
    ('caxixi', 'caxixi/index.html', 'assets/previews/preview_caxixi.jpg'),
    ('contador', 'contador/index.html', 'assets/previews/preview_contador.jpg'),
    ('fotografo-casamento', 'fotografo-casamento/index.html', 'assets/previews/preview_fotografo_casamento.jpg'),
    ('fumaca-motos', 'fumaca-motos/index.html', 'assets/previews/preview_fumaca_motos.jpg'),
    ('gtmotors', 'gtmotors/index.html', 'assets/previews/preview_gtmotors.jpg'),
    ('lavanderia', 'lavanderia/index.html', 'assets/previews/preview_lavanderia.jpg'),
    ('nutricionista', 'nutricionista/index.html', 'assets/previews/preview_nutricionista.jpg'),
    ('oftalmologista', 'oftalmologista/index.html', 'assets/previews/preview_oftalmologista.jpg'),
    ('personal-trainer', 'personal-trainer/index.html', 'assets/previews/preview_personal_trainer.jpg'),
    ('podologo', 'podologo/index.html', 'assets/previews/preview_podologo.jpg'),
    ('professor-idiomas', 'professor-idiomas/index.html', 'assets/previews/preview_professor_idiomas.jpg'),
    ('professor-musica', 'professor-musica/index.html', 'assets/previews/preview_professor_musica.jpg'),
    ('professor-particular', 'professor-particular/index.html', 'assets/previews/preview_professor_particular.jpg'),
    ('psicologia', 'psicologia/index.html', 'assets/previews/preview_psicologia.jpg'),
    ('quiropraxista', 'quiropraxista/index.html', 'assets/previews/preview_quiropraxista.jpg'),
    ('rampabike', 'rampabike/index.html', 'assets/previews/preview_rampabike.jpg'),
    ('reconcavo', 'reconcavo/index.html', 'assets/previews/preview_reconcavo.jpg'),
    ('reforma-moveis', 'reforma-moveis/index.html', 'assets/previews/preview_reforma_moveis.jpg'),
    ('restaurante-egeu', 'restaurante-egeu/index.html', 'assets/previews/preview_restaurante_egeu.jpg'),
    ('shineray-uba', 'shineray-uba/index.html', 'assets/previews/preview_shineray_uba.jpg'),
    ('topmotos032', 'topmotos032/index.html', 'assets/previews/preview_topmotos032.jpg'),
    ('vrum-motos', 'vrum-motos/index.html', 'assets/previews/preview_vrum_motos.jpg')
]

print(f"Starting extended screenshot capture (1280x2400) for {len(SITES)} sites...")
start_time = time.time()

success = 0
for idx, (niche_id, rel_html, rel_preview) in enumerate(SITES, 1):
    html_abs = os.path.join(BASE_DIR, rel_html)
    preview_abs = os.path.join(BASE_DIR, rel_preview)
    
    if not os.path.exists(html_abs):
        print(f"[{idx}/{len(SITES)}] SKIPPED (HTML not found): {rel_html}")
        continue
        
    url = f"file:///{html_abs.replace(os.sep, '/')}"
    cmd = f'"{edge_path}" --headless --disable-gpu --screenshot="{preview_abs}" --window-size=1280,2400 "{url}"'
    
    try:
        subprocess.run(cmd, shell=True, timeout=25, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(preview_abs):
            size_kb = os.path.getsize(preview_abs) / 1024
            print(f"[{idx}/{len(SITES)}] OK: {niche_id} -> {rel_preview} ({size_kb:.1f} KB)")
            success += 1
        else:
            print(f"[{idx}/{len(SITES)}] FAILED (file not created): {niche_id}")
    except Exception as e:
        print(f"[{idx}/{len(SITES)}] ERROR: {niche_id} -> {e}")

elapsed = time.time() - start_time
print(f"\nFinished in {elapsed:.1f} seconds! Successfully captured {success}/{len(SITES)} extended previews.")
