"""
Main execution script to apply the master upgrade plan to all 17 niches.
"""

import os, re
from bs4 import BeautifulSoup
from niche_configs import NICHES_DATA, GSAP_CDN, GSAP_SCRIPT

def generate_schema_json(niche_key, data):
    schema = {
        "@context": "https://schema.org",
        "@type": data['schema_type'],
        "name": data['business_name'],
        "description": data['desc'],
        "telephone": "+55-32-99929-2311",
        "url": f"https://nexusflow.digital/{niche_key}/",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Av. Paulista, 1000 - Bela Vista / Jardins",
            "addressLocality": "São Paulo",
            "addressRegion": "SP",
            "postalCode": "01310-100",
            "addressCountry": "BR"
        },
        "priceRange": "$$$"
    }
    import json
    return f'\n  <!-- Schema.org SEO & GEO Data -->\n  <script type="application/ld+json">\n  {json.dumps(schema, indent=2, ensure_ascii=False)}\n  </script>\n'

def generate_gallery_section(data):
    cards_html = []
    for item in data['gallery']:
        cards_html.append(f'''
        <div class="card-lift bg-slate-900/90 rounded-2xl overflow-hidden border border-slate-800 shadow-xl group">
          <div class="aspect-[16/10] overflow-hidden relative">
            <img src="{item['img']}" alt="{item['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
          </div>
          <div class="p-5 space-y-2">
            <h3 class="text-base font-bold text-white group-hover:text-amber-300 transition-colors">{item['title']}</h3>
            <p class="text-xs text-slate-400 leading-relaxed">{item['desc']}</p>
          </div>
        </div>
        ''')
    
    grid = "\n".join(cards_html)
    return f'''
  <!-- ========================================================================= -->
  <!-- SEÇÃO DE GALERIA VISUAL & ESTRUTURA PREMIUM                               -->
  <!-- ========================================================================= -->
  <section id="galeria-nicho" class="py-20 bg-slate-950 text-white border-t border-slate-800/80 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center max-w-2xl mx-auto mb-14">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/10 text-amber-300 text-xs font-bold uppercase tracking-wider mb-3">
          <i class="fa-solid fa-sparkles text-xs"></i> Excelência & Detalhes
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-white">{data['gallery_title']}</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">{data['gallery_subtitle']}</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {grid}
      </div>
    </div>
  </section>
    '''

def generate_faq_and_reviews_section(data):
    faq_items = []
    for i, (q, a) in enumerate(data['faqs']):
        faq_items.append(f'''
        <div class="border border-slate-800 rounded-2xl overflow-hidden bg-slate-900/60 transition">
          <button type="button" onclick="toggleFaqItem(this)" class="w-full p-4 sm:p-5 text-left flex items-center justify-between text-xs sm:text-sm font-bold text-white hover:text-amber-300 transition">
            <span>{q}</span>
            <i class="fa-solid fa-chevron-down faq-icon text-xs text-slate-400 transition-transform duration-300 ml-3 shrink-0"></i>
          </button>
          <div class="faq-content hidden px-4 pb-4 sm:px-5 sm:pb-5 text-xs text-slate-400 border-t border-slate-800/60 pt-3 leading-relaxed">
            {a}
          </div>
        </div>
        ''')
    faqs_html = "\n".join(faq_items)

    review_items = []
    for name, text, stars in data['reviews']:
        review_items.append(f'''
        <div class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-xs text-white">{name}</span>
            <span class="text-xs text-amber-400">{stars}</span>
          </div>
          <p class="text-xs text-slate-400 italic leading-relaxed">"{text}"</p>
        </div>
        ''')
    reviews_html = "\n".join(review_items)

    return f'''
  <!-- ========================================================================= -->
  <!-- SEÇÃO DE AVALIAÇÕES & FAQ INTERATIVO                                      -->
  <!-- ========================================================================= -->
  <section id="faq-depoimentos" class="py-20 bg-[#090D18] text-white border-t border-slate-800/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        
        <!-- Left: FAQ Accordion -->
        <div class="lg:col-span-7 space-y-6">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-300">Dúvidas Frequentes</span>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-white mt-1">Perguntas & Respostas Rápidas</h2>
            <p class="text-xs text-slate-400 mt-1">Clique para ver os detalhes sobre prazos, agendamento e formas de pagamento.</p>
          </div>
          <div class="space-y-3">
            {faqs_html}
          </div>
        </div>

        <!-- Right: Social Proof & WhatsApp CTA -->
        <div class="lg:col-span-5 space-y-6">
          <div class="bg-slate-900/90 rounded-3xl p-6 sm:p-8 border border-slate-800 shadow-2xl space-y-6">
            <div>
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Depoimentos Verificados</span>
              <h3 class="text-xl font-bold text-white mt-1">O que nossos clientes dizem</h3>
            </div>
            <div class="space-y-4">
              {reviews_html}
            </div>
            <div class="pt-2 border-t border-slate-800">
              <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostaria%20de%20agendar%20um%20atendimento%20priorit%C3%A1rio." target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:opacity-95 text-white font-extrabold text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition transform hover:scale-[1.02]">
                <i class="fa-brands fa-whatsapp text-base"></i>
                <span>Agendar no WhatsApp com Prioridade</span>
              </a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
    '''

def upgrade_niche(niche_key, data):
    html_path = os.path.join(niche_key, 'index.html')
    if not os.path.exists(html_path):
        print(f"[-] {niche_key}/index.html not found.")
        return False

    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. GSAP CDN
    if 'gsap.min.js' not in html:
        html = html.replace('</head>', f'{GSAP_CDN}\n</head>')

    # 2. Schema.org JSON-LD
    if 'application/ld+json' not in html:
        schema_html = generate_schema_json(niche_key, data)
        html = html.replace('</head>', f'{schema_html}\n</head>')

    # 3. Add Gallery if not already present
    if 'id="galeria-nicho"' not in html:
        gallery_section = generate_gallery_section(data)
        # Insert before #localizacao or <footer>
        if '<section id="localizacao"' in html:
            html = html.replace('<section id="localizacao"', f'{gallery_section}\n  <section id="localizacao"')
        elif '<footer' in html:
            html = html.replace('<footer', f'{gallery_section}\n  <footer')

    # 4. Add FAQ & Reviews if not already present
    if 'id="faq-depoimentos"' not in html:
        faq_section = generate_faq_and_reviews_section(data)
        if '<section id="localizacao"' in html:
            html = html.replace('<section id="localizacao"', f'{faq_section}\n  <section id="localizacao"')
        elif '<footer' in html:
            html = html.replace('<footer', f'{faq_section}\n  <footer')

    # 5. GSAP Animation & FAQ JS
    if 'toggleFaqItem' not in html:
        html = html.replace('</body>', f'{GSAP_SCRIPT}\n</body>')

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"[+] Successfully upgraded {niche_key}!")
    return True

if __name__ == '__main__':
    print(f"Starting upgrade of {len(NICHES_DATA)} niches to Master Plan standard...")
    count = 0
    for n, d in NICHES_DATA.items():
        if upgrade_niche(n, d):
            count += 1
    print(f"Upgrade completed! Successfully updated {count}/{len(NICHES_DATA)} niches.")

