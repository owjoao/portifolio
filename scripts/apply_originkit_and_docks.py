"""
Script to apply:
1. OriginKit Comparison Matrix
2. Mobile Conversion Dock (ADR-002) with pulse indicator, official name & WhatsApp msg
3. Slider Antes & Depois for niches that lacked it (barbearia, lavanderia, personal-trainer, gtmotors)
Across all targeted landing pages.
"""

import os, re
from originkit_data import ORIGINKIT_DATA

def build_matrix_html(data):
    comp_items = "\n".join([f'            <li class="flex items-start gap-3"><span class="text-rose-500 font-bold">✕</span> <span>{item}</span></li>' for item in data['competitor_items']])
    our_items = "\n".join([f'            <li class="flex items-start gap-3 text-emerald-400 font-medium"><span class="font-black text-emerald-400">✓</span> <span>{item}</span></li>' for item in data['our_items']])

    return f'''
  <!-- ========================================================================= -->
  <!-- SEÇÃO COMPARATIVA: ORIGINKIT MATRIX (POR QUE NOS ESCOLHER)                -->
  <!-- ========================================================================= -->
  <section id="comparativo-originkit" class="py-20 bg-[#060913] text-white border-t border-slate-800/80 relative overflow-hidden">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-4">
          <i class="fa-solid fa-shield-check"></i> Transparência & Rigor Técnico
        </span>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight">
          {data['headline']}
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-3 leading-relaxed">
          {data['subheadline']}
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-stretch">
        
        <!-- Opções Comuns do Mercado -->
        <div class="p-8 rounded-3xl bg-slate-900/60 border border-slate-800 shadow-lg flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-6">
              <div class="w-10 h-10 rounded-2xl bg-rose-500/10 border border-rose-500/20 text-rose-400 flex items-center justify-center font-bold text-lg">
                ✕
              </div>
              <div>
                <h3 class="text-lg font-bold text-slate-300">{data['competitor_title']}</h3>
                <span class="text-[11px] text-slate-500 font-medium">Práticas comuns que geram dor de cabeça</span>
              </div>
            </div>
            <ul class="space-y-4 text-slate-400 text-xs sm:text-sm leading-relaxed">
{comp_items}
            </ul>
          </div>
          <div class="mt-8 pt-4 border-t border-slate-800/80 text-[11px] text-slate-500 flex items-center gap-2">
            <i class="fa-solid fa-triangle-exclamation text-amber-500"></i> Risco de prejuízos e retrabalho para o cliente.
          </div>
        </div>

        <!-- Nosso Padrão de Excelência -->
        <div class="p-8 rounded-3xl bg-gradient-to-b from-slate-900 via-[#0D1527] to-slate-900 border-2 border-emerald-500/60 shadow-2xl relative flex flex-col justify-between ring-4 ring-emerald-500/10">
          <div class="absolute -top-3.5 right-6 bg-gradient-to-r from-emerald-500 to-teal-500 text-slate-950 font-black text-[10px] uppercase tracking-wider px-3.5 py-1 rounded-full shadow-lg">
            {data['our_badge']}
          </div>
          <div>
            <div class="flex items-center gap-3 mb-6">
              <div class="w-10 h-10 rounded-2xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center font-bold text-lg shadow-sm">
                ✓
              </div>
              <div>
                <h3 class="text-lg font-black text-white">{data['our_title']}</h3>
                <span class="text-[11px] text-emerald-400 font-semibold">Compromisso formal com o seu resultado</span>
              </div>
            </div>
            <ul class="space-y-4 text-xs sm:text-sm leading-relaxed">
{our_items}
            </ul>
          </div>
          <div class="mt-8 pt-4 border-t border-slate-800 flex items-center justify-between text-xs">
            <span class="text-emerald-400 font-bold flex items-center gap-1.5">
              <i class="fa-solid fa-circle-check"></i> Garantia Contratual
            </span>
            <a href="https://wa.me/5532999292311?text={data['dock_msg'].replace(' ', '%20')}" target="_blank" class="text-white hover:text-emerald-400 font-bold transition flex items-center gap-1">
              <span>Saber Mais</span> <i class="fa-solid fa-arrow-right text-[10px]"></i>
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>
'''

def build_dock_html(company, msg):
    encoded_msg = msg.replace(' ', '%20')
    return f'''
  <!-- ========================================================================= -->
  <!-- ADR-002: MOBILE CONVERSION DOCK (1-TOQUE NO WHATSAPP)                     -->
  <!-- ========================================================================= -->
  <aside class="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-[#070A12]/95 backdrop-blur-md border-t border-slate-800 p-2.5 px-4 shadow-[0_-4px_25px_rgba(0,0,0,0.5)]">
    <div class="flex items-center justify-between gap-3 max-w-lg mx-auto">
      <div class="flex flex-col">
        <span class="text-[10px] uppercase font-bold text-slate-400 leading-tight tracking-wider">{company}</span>
        <span class="text-xs text-emerald-400 font-bold flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          <span>Online agora</span>
        </span>
      </div>
      <a href="https://wa.me/5532999292311?text={encoded_msg}" target="_blank" class="shimmer-btn flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-emerald-950/50 transition-transform active:scale-95" rel="noopener noreferrer">
        <i class="fa-brands fa-whatsapp text-base"></i>
        <span>Atendimento</span>
      </a>
    </div>
  </aside>
'''

def build_barber_slider():
    return '''
  <!-- ========================================================================= -->
  <!-- SKIPER UI: SLIDER INTERATIVO ANTES & DEPOIS (ALINHAMENTO & VISAGISMO)     -->
  <!-- ========================================================================= -->
  <section id="transformacao-visual" class="py-20 bg-[#090D18] text-white border-t border-slate-800/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500/10 text-amber-300 text-xs font-bold uppercase tracking-wider mb-3">
          <i class="fa-solid fa-arrows-left-right"></i> Prova Visual Imediata
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-white">Transformação em Barba & Visagismo</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">Arraste a linha para comparar o antes e o depois do corte com toalha quente e navalhete.</p>
      </div>

      <div class="ba-container relative w-full aspect-[16/10] rounded-3xl overflow-hidden border border-slate-800 shadow-2xl select-none cursor-ew-resize">
        <!-- DEPOIS (Base) -->
        <img src="assets/barber-hero.jpg" alt="Depois do Corte e Barboterapia" class="absolute inset-0 w-full h-full object-cover" />
        <span class="absolute bottom-4 right-4 bg-black/80 backdrop-blur-md text-amber-300 border border-amber-400/30 text-xs px-3.5 py-1.5 rounded-full font-bold">DEPOIS: Perfil Alinhado</span>

        <!-- ANTES (Layer Cortada) -->
        <div class="ba-after-layer absolute inset-0 w-1/2 overflow-hidden pointer-events-none border-r-2 border-amber-400 shadow-[0_0_15px_rgba(251,191,36,0.5)]">
          <img src="assets/barber-shave.jpg" alt="Antes do Tratamento na Barbearia" class="absolute inset-0 w-full h-full object-cover max-w-none filter grayscale contrast-125" />
          <span class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white text-xs px-3.5 py-1.5 rounded-full font-bold">ANTES: Sem Alinhamento</span>
        </div>

        <!-- Slider Handle -->
        <div class="ba-slider-handle absolute top-0 bottom-0 left-1/2 w-1 bg-amber-400 flex items-center justify-center -translate-x-1/2 pointer-events-none">
          <div class="w-9 h-9 rounded-full bg-slate-950 border-2 border-amber-400 text-amber-300 shadow-xl flex items-center justify-center text-xs font-bold">
            ⇄
          </div>
        </div>
      </div>
    </div>
  </section>
'''

def build_laundry_slider():
    return '''
  <!-- ========================================================================= -->
  <!-- SKIPER UI: SLIDER INTERATIVO ANTES & DEPOIS (HIGIENIZAÇÃO A VAPOR)        -->
  <!-- ========================================================================= -->
  <section id="transformacao-visual" class="py-20 bg-[#090D18] text-white border-t border-slate-800/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-300 text-xs font-bold uppercase tracking-wider mb-3">
          <i class="fa-solid fa-arrows-left-right"></i> Prova Visual Têxtil
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-white">Restauração de Cores & Fibras a Vapor</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">Arraste a linha para comparar tecidos amarelados e manchados com o resultado após a lavagem ecológica.</p>
      </div>

      <div class="ba-container relative w-full aspect-[16/10] rounded-3xl overflow-hidden border border-slate-800 shadow-2xl select-none cursor-ew-resize">
        <!-- DEPOIS (Base) -->
        <img src="assets/laundry-clean.jpg" alt="Tecido Limpo e Passado" class="absolute inset-0 w-full h-full object-cover" />
        <span class="absolute bottom-4 right-4 bg-black/80 backdrop-blur-md text-cyan-300 border border-cyan-400/30 text-xs px-3.5 py-1.5 rounded-full font-bold">DEPOIS: Fibras Renovadas</span>

        <!-- ANTES (Layer Cortada) -->
        <div class="ba-after-layer absolute inset-0 w-1/2 overflow-hidden pointer-events-none border-r-2 border-cyan-400 shadow-[0_0_15px_rgba(6,182,212,0.5)]">
          <img src="assets/laundry-machines.jpg" alt="Tecido com Manchas e Amarelado" class="absolute inset-0 w-full h-full object-cover max-w-none filter sepia contrast-125" />
          <span class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white text-xs px-3.5 py-1.5 rounded-full font-bold">ANTES: Manchas & Ácaros</span>
        </div>

        <!-- Slider Handle -->
        <div class="ba-slider-handle absolute top-0 bottom-0 left-1/2 w-1 bg-cyan-400 flex items-center justify-center -translate-x-1/2 pointer-events-none">
          <div class="w-9 h-9 rounded-full bg-slate-950 border-2 border-cyan-400 text-cyan-300 shadow-xl flex items-center justify-center text-xs font-bold">
            ⇄
          </div>
        </div>
      </div>
    </div>
  </section>
'''

def build_fitness_slider():
    return '''
  <!-- ========================================================================= -->
  <!-- SKIPER UI: SLIDER INTERATIVO ANTES & DEPOIS (EVOLUÇÃO CORPORAL)           -->
  <!-- ========================================================================= -->
  <section id="transformacao-visual" class="py-20 bg-[#090D18] text-white border-t border-slate-800/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">
          <i class="fa-solid fa-arrows-left-right"></i> Resultados Reais
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-white">Evolução de Composição Corporal</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">Arraste a linha para ver a transformação após 16 semanas de periodização e acompanhamento 1-on-1.</p>
      </div>

      <div class="ba-container relative w-full aspect-[16/10] rounded-3xl overflow-hidden border border-slate-800 shadow-2xl select-none cursor-ew-resize">
        <!-- DEPOIS (Base) -->
        <img src="assets/trainer-results.jpg" alt="Definição e Ganho de Massa Magra" class="absolute inset-0 w-full h-full object-cover" />
        <span class="absolute bottom-4 right-4 bg-black/80 backdrop-blur-md text-emerald-400 border border-emerald-500/30 text-xs px-3.5 py-1.5 rounded-full font-bold">DEPOIS: -12kg Gordura & +4kg Músculo</span>

        <!-- ANTES (Layer Cortada) -->
        <div class="ba-after-layer absolute inset-0 w-1/2 overflow-hidden pointer-events-none border-r-2 border-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.5)]">
          <img src="assets/hero-trainer.jpg" alt="Início do Treinamento" class="absolute inset-0 w-full h-full object-cover max-w-none filter grayscale contrast-125" />
          <span class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white text-xs px-3.5 py-1.5 rounded-full font-bold">ANTES: Sedentarismo & Fadiga</span>
        </div>

        <!-- Slider Handle -->
        <div class="ba-slider-handle absolute top-0 bottom-0 left-1/2 w-1 bg-emerald-400 flex items-center justify-center -translate-x-1/2 pointer-events-none">
          <div class="w-9 h-9 rounded-full bg-slate-950 border-2 border-emerald-400 text-emerald-300 shadow-xl flex items-center justify-center text-xs font-bold">
            ⇄
          </div>
        </div>
      </div>
    </div>
  </section>
'''

def build_gtmotors_slider():
    return '''
  <!-- ========================================================================= -->
  <!-- SKIPER UI: SLIDER INTERATIVO ANTES & DEPOIS (VITRIFICAÇÃO & POLIMENTO)    -->
  <!-- ========================================================================= -->
  <section id="transformacao-visual" class="py-20 bg-[#090D18] text-white border-t border-slate-800/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-500/10 text-red-400 text-xs font-bold uppercase tracking-wider mb-3">
          <i class="fa-solid fa-arrows-left-right"></i> Detalhamento Automotivo
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-white">Proteção Cerâmica & Brilho Espelhado</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">Arraste a linha para comparar a pintura opaca com marcas de lavagem e a cura cerâmica 9H.</p>
      </div>

      <div class="ba-container relative w-full aspect-[16/10] rounded-3xl overflow-hidden border border-slate-800 shadow-2xl select-none cursor-ew-resize">
        <!-- DEPOIS (Base) -->
        <img src="assets/gt-hero.jpg" alt="Pintura Vitrificada com Brilho Profundo" class="absolute inset-0 w-full h-full object-cover" />
        <span class="absolute bottom-4 right-4 bg-black/80 backdrop-blur-md text-red-400 border border-red-500/30 text-xs px-3.5 py-1.5 rounded-full font-bold">DEPOIS: Vitrificação 9H</span>

        <!-- ANTES (Layer Cortada) -->
        <div class="ba-after-layer absolute inset-0 w-1/2 overflow-hidden pointer-events-none border-r-2 border-red-500 shadow-[0_0_15px_rgba(239,68,68,0.5)]">
          <img src="assets/gt-detail.jpg" alt="Pintura com Micro-riscos" class="absolute inset-0 w-full h-full object-cover max-w-none filter grayscale contrast-125" />
          <span class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white text-xs px-3.5 py-1.5 rounded-full font-bold">ANTES: Micro-riscos & Opacidade</span>
        </div>

        <!-- Slider Handle -->
        <div class="ba-slider-handle absolute top-0 bottom-0 left-1/2 w-1 bg-red-500 flex items-center justify-center -translate-x-1/2 pointer-events-none">
          <div class="w-9 h-9 rounded-full bg-slate-950 border-2 border-red-500 text-red-300 shadow-xl flex items-center justify-center text-xs font-bold">
            ⇄
          </div>
        </div>
      </div>
    </div>
  </section>
'''

SLIDER_JS = '''
  <script>
    // Skiper UI Before/After Slider Interaction (Mouse & Touch)
    document.querySelectorAll('.ba-container').forEach(container => {
      const afterLayer = container.querySelector('.ba-after-layer');
      const handle = container.querySelector('.ba-slider-handle');
      if (!afterLayer || !handle) return;
      let isDown = false;

      const move = (e) => {
        if (!isDown) return;
        const rect = container.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        let x = clientX - rect.left;
        if (x < 0) x = 0;
        if (x > rect.width) x = rect.width;
        const percent = (x / rect.width) * 100;
        afterLayer.style.width = percent + '%';
        handle.style.left = percent + '%';
      };

      container.addEventListener('mousedown', () => isDown = true);
      window.addEventListener('mouseup', () => isDown = false);
      container.addEventListener('mousemove', move);

      container.addEventListener('touchstart', () => isDown = true);
      window.addEventListener('touchend', () => isDown = false);
      container.addEventListener('touchmove', move);
    });
  </script>
'''

def update_niche(niche, data):
    html_path = os.path.join(niche, 'index.html')
    if not os.path.exists(html_path):
        return False
    
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. Clean broken placeholders (e.g. '(Prime Imóveis SP)', 'gostei%20desse%20site%2C%20qual%20o%20valor%3F')
    html = re.sub(r'\(Prime\s+Im[óo]veis\s+SP\)', f"({data['dock_company']})", html)
    html = re.sub(r'Prime\s+Im[óo]veis\s+SP', data['dock_company'], html)
    html = html.replace('gostei%20desse%20site%2C%20qual%20o%20valor%3F', data['dock_msg'].replace(' ', '%20'))

    # 2. Inject OriginKit Matrix if not present
    if 'id="comparativo-originkit"' not in html:
        matrix_html = build_matrix_html(data)
        if '<section id="faq-depoimentos"' in html:
            html = html.replace('<section id="faq-depoimentos"', f'{matrix_html}\n  <section id="faq-depoimentos"')
        elif '<section id="galeria-nicho"' in html:
            html = html.replace('<section id="galeria-nicho"', f'{matrix_html}\n  <section id="galeria-nicho"')
        elif '<section id="localizacao"' in html:
            html = html.replace('<section id="localizacao"', f'{matrix_html}\n  <section id="localizacao"')
        elif '<footer' in html:
            html = html.replace('<footer', f'{matrix_html}\n  <footer')

    # 3. Inject Slider for niches that need it
    if niche == 'barbearia' and 'id="transformacao-visual"' not in html:
        slider = build_barber_slider()
        html = html.replace('<section id="comparativo-originkit"', f'{slider}\n  <section id="comparativo-originkit"')
    elif niche == 'lavanderia' and 'id="transformacao-visual"' not in html:
        slider = build_laundry_slider()
        html = html.replace('<section id="comparativo-originkit"', f'{slider}\n  <section id="comparativo-originkit"')
    elif niche == 'personal-trainer' and 'id="transformacao-visual"' not in html:
        slider = build_fitness_slider()
        html = html.replace('<section id="comparativo-originkit"', f'{slider}\n  <section id="comparativo-originkit"')
    elif niche == 'gtmotors' and 'id="transformacao-visual"' not in html:
        slider = build_gtmotors_slider()
        html = html.replace('<section id="comparativo-originkit"', f'{slider}\n  <section id="comparativo-originkit"')

    # 4. Inject Slider JS if not present
    if 'ba-slider-handle' in html and 'const move =' not in html:
        html = html.replace('</body>', f'{SLIDER_JS}\n</body>')

    # 5. Overhaul or update Mobile Conversion Dock (ADR-002)
    dock_html = build_dock_html(data['dock_company'], data['dock_msg'])
    if '<!-- ADR-002: MOBILE CONVERSION DOCK' not in html:
        # Remove any old mobile docks to prevent duplicate bars
        html = re.sub(r'<div class="fixed bottom-0 left-0 right-0 z-40 bg-white/95.*?</button>\s*</div>', '', html, flags=re.DOTALL)
        html = re.sub(r'<aside class="md:hidden fixed bottom-0 left-0 right-0.*?</aside>', '', html, flags=re.DOTALL)
        html = html.replace('</body>', f'{dock_html}\n</body>')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"[+] Updated {niche} with OriginKit Matrix & ADR-002 Dock!")
    return True

if __name__ == '__main__':
    count = 0
    for niche, data in ORIGINKIT_DATA.items():
        if update_niche(niche, data):
            count += 1
    print(f"Total niches upgraded: {count}/{len(ORIGINKIT_DATA)}")

