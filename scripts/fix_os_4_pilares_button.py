# -*- coding: utf-8 -*-
import os

print("--- 1. Updating index_nexus_landing.html ---")
nexus_file = "index_nexus_landing.html"
if os.path.exists(nexus_file):
    with open(nexus_file, "r", encoding="utf-8") as f:
        html = f.read()
    
    # 1.1 Insert id="pilares" wrapper and badge
    target_grid_start = '<div class="grid grid-cols-1 md:grid-cols-4 gap-6 relative">'
    new_grid_start = """<div id="pilares" class="scroll-mt-28">
        <div class="flex items-center justify-center gap-3 mb-8">
          <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-nexus-indigo/20 to-nexus-cyan/20 border border-nexus-cyan/40 text-nexus-cyan text-xs font-mono font-bold uppercase tracking-wider shadow-glow-cyan">
            <i class="fa-solid fa-layer-group"></i> Os 4 Pilares de Alta Conversão
          </span>
        </div>
        <div id="pilares-cards" class="grid grid-cols-1 md:grid-cols-4 gap-6 relative transition-all duration-500">"""
    
    if target_grid_start in html and 'id="pilares"' not in html:
        # Find where Step 4 ends to close the div
        step4_end = html.find('<!-- Step 4: CRM & Fechamento -->')
        if step4_end != -1:
            # find the end of this div (the grid closing div)
            grid_close = html.find('</div>\n\n    </div>\n  </section>', step4_end)
            if grid_close == -1:
                grid_close = html.find('</div>\r\n\r\n    </div>\r\n  </section>', step4_end)
            
            html = html.replace(target_grid_start, new_grid_start, 1)
            # Add an extra </div> to close #pilares
            if grid_close != -1:
                # after the grid </div>, add another </div>
                closing_target = '</div>\n\n    </div>\n  </section>' if '</div>\n\n    </div>\n  </section>' in html else '</div>\r\n\r\n    </div>\r\n  </section>'
                html = html.replace(closing_target, '</div>\n      </div>\n\n    </div>\n  </section>', 1)
            print("Successfully injected #pilares section in index_nexus_landing.html!")

    # 1.2 Add Mobile Menu Button & Drawer to index_nexus_landing.html
    if 'id="mobile-menu-drawer"' not in html:
        header_end = '</header>'
        mobile_drawer = """
    <!-- Mobile Hamburger Menu Drawer -->
    <div id="mobile-menu-drawer" class="hidden md:hidden bg-nexus-dark/98 border-b border-white/10 px-6 py-6 space-y-4 backdrop-blur-xl">
      <nav class="flex flex-col gap-3 font-semibold text-slate-200">
        <a href="#fluxo" onclick="toggleMobileMenu()" class="py-2 border-b border-white/5 hover:text-nexus-cyan">O Fluxo</a>
        <a href="#pilares" onclick="toggleMobileMenu()" class="py-2 border-b border-white/5 hover:text-nexus-cyan flex items-center justify-between">
          <span>Os 4 Pilares</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-nexus-cyan/20 text-nexus-cyan">4 Etapas</span>
        </a>
        <a href="#portfolio" onclick="toggleMobileMenu()" class="py-2 border-b border-white/5 hover:text-nexus-cyan">Portfólio (25 Projetos)</a>
        <a href="#objecoes" onclick="toggleMobileMenu()" class="py-2 border-b border-white/5 hover:text-nexus-cyan">Por Que Nós?</a>
        <a href="#simulador" onclick="toggleMobileMenu()" class="py-2 hover:text-nexus-cyan">Calculadora ROI</a>
      </nav>
      <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20gostaria%20de%20um%20diagn%C3%B3stico%20gratuito." target="_blank" class="w-full py-3 rounded-xl bg-gradient-to-r from-nexus-indigo to-nexus-cyan text-white text-center font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2">
        <i class="fa-brands fa-whatsapp text-sm"></i> Falar no WhatsApp
      </a>
    </div>
"""
        html = html.replace(header_end, mobile_drawer + '\n  ' + header_end, 1)
        
        # Add hamburger button to header next to CTA
        cta_container = '<div class="flex items-center gap-3">'
        new_cta_container = """<div class="flex items-center gap-3">
        <button onclick="toggleMobileMenu()" class="md:hidden text-slate-300 hover:text-white p-2 text-xl focus:outline-none" aria-label="Abrir Menu">
          <i class="fa-solid fa-bars"></i>
        </button>"""
        html = html.replace(cta_container, new_cta_container, 1)
        print("Added mobile hamburger menu drawer to index_nexus_landing.html!")

    # 1.3 Add smooth scroll & highlight pulse JS
    js_scroll = """
    function toggleMobileMenu() {
      const d = document.getElementById('mobile-menu-drawer');
      if (d) d.classList.toggle('hidden');
    }

    // Smooth Scroll & Visual Highlight for #pilares
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('a[href="#pilares"]').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const target = document.getElementById('pilares');
          if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            const cards = document.getElementById('pilares-cards') || target;
            cards.classList.add('ring-4', 'ring-nexus-cyan/50', 'rounded-3xl');
            setTimeout(() => {
              cards.classList.remove('ring-4', 'ring-nexus-cyan/50', 'rounded-3xl');
            }, 1800);
          }
        });
      });
    });
"""
    if 'function toggleMobileMenu' not in html:
        html = html.replace('</script>\n\n</body>', js_scroll + '\n  </script>\n\n</body>')
        html = html.replace('</script>\r\n\r\n</body>', js_scroll + '\r\n  </script>\r\n\r\n</body>')
        print("Added smooth scroll & visual highlight for #pilares!")

    with open(nexus_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("index_nexus_landing.html updated successfully!")


print("\n--- 2. Updating root index.html ---")
main_file = "index.html"
if os.path.exists(main_file):
    with open(main_file, "r", encoding="utf-8") as f:
        html_main = f.read()

    # 2.1 Add "Os 4 Pilares" in desktop navbar
    old_nav = """      <!-- Desktop Nav Links Reais do Site -->
      <nav class="hidden md:flex items-center gap-8 text-xs lg:text-sm font-semibold text-slate-300">
        <a href="#hero-banner" class="hover:text-cyan-400 transition-colors">Início</a>
        <a href="#row-crm" class="hover:text-cyan-400 transition-colors flex items-center gap-2">
          <span>Sistemas com CRM</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">8 Nichos</span>
        </a>
        <a href="#row-todos" class="hover:text-cyan-400 transition-colors">Portfólio Completo (32)</a>
      </nav>"""

    new_nav = """      <!-- Desktop Nav Links Reais do Site -->
      <nav class="hidden md:flex items-center gap-8 text-xs lg:text-sm font-semibold text-slate-300">
        <a href="#hero-banner" class="hover:text-cyan-400 transition-colors">Início</a>
        <a href="#pilares" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5">
          <i class="fa-solid fa-layer-group text-xs text-cyan-400"></i>
          <span>Os 4 Pilares</span>
        </a>
        <a href="#row-crm" class="hover:text-cyan-400 transition-colors flex items-center gap-2">
          <span>Sistemas com CRM</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">8 Nichos</span>
        </a>
        <a href="#row-todos" class="hover:text-cyan-400 transition-colors">Portfólio Completo (32)</a>
      </nav>"""

    if old_nav in html_main:
        html_main = html_main.replace(old_nav, new_nav, 1)
        print("Added 'Os 4 Pilares' to desktop navbar in index.html!")

    # 2.2 Add Section "Os 4 Pilares" right before #row-crm
    pilares_section = """
  <!-- ========================================================================= -->
  <!-- SEÇÃO OFICIAL: OS 4 PILARES DO ECOSSISTEMA NEXUS FLOW                     -->
  <!-- ========================================================================= -->
  <section id="pilares" class="py-16 sm:py-20 bg-[#0A0D15] border-y border-white/5 relative overflow-hidden scroll-mt-20">
    <!-- Ambient Glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[300px] bg-cyan-500/10 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-14">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-xs font-mono font-bold uppercase tracking-wider mb-3">
          <i class="fa-solid fa-layer-group"></i> Engenharia de Vendas & Escala
        </div>
        <h2 class="font-outfit font-black text-3xl sm:text-4xl lg:text-5xl text-white tracking-tight">
          Os 4 Pilares do Ecossistema NEXUS FLOW
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-3 leading-relaxed">
          Uma arquitetura contínua e sem atritos que transforma visitantes casuais em clientes pagantes com alta previsibilidade e agilidade de fechamento.
        </p>
      </div>

      <!-- 4 Pillars Cards Grid -->
      <div id="pilares-cards-main" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 transition-all duration-500">
        
        <!-- Pilar 1 -->
        <div class="p-6 rounded-3xl bg-[#111624] border border-white/10 hover:border-cyan-400/50 shadow-xl transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 flex items-center justify-center font-outfit font-black text-xl mb-4 group-hover:scale-110 transition-transform">
              01
            </div>
            <div class="flex items-center gap-2 mb-2">
              <i class="fa-solid fa-bullseye text-cyan-400 text-base"></i>
              <h3 class="font-outfit font-bold text-lg text-white">Tráfego de Precisão</h3>
            </div>
            <p class="text-slate-400 text-xs leading-relaxed mb-4">
              Campanhas no Google e Meta hiper-segmentadas que atraem apenas compradores prontos com alta intenção de fechamento, sem desperdício de verba.
            </p>
          </div>
          <div class="pt-3 border-t border-white/5 flex items-center justify-between text-[11px] text-cyan-400 font-mono">
            <span>Público Qualificado</span>
            <i class="fa-solid fa-arrow-right"></i>
          </div>
        </div>

        <!-- Pilar 2 -->
        <div class="p-6 rounded-3xl bg-[#111624] border-2 border-indigo-500/40 hover:border-indigo-400 shadow-xl shadow-indigo-500/10 transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1 relative">
          <div class="absolute -top-3 right-6 bg-gradient-to-r from-indigo-500 to-cyan-500 text-white text-[10px] font-black uppercase tracking-wider px-3 py-0.5 rounded-full shadow">
            Ultra Conversão
          </div>
          <div>
            <div class="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 flex items-center justify-center font-outfit font-black text-xl mb-4 group-hover:scale-110 transition-transform">
              02
            </div>
            <div class="flex items-center gap-2 mb-2">
              <i class="fa-solid fa-bolt text-indigo-400 text-base"></i>
              <h3 class="font-outfit font-bold text-lg text-white">Landing Page Ágil</h3>
            </div>
            <p class="text-slate-400 text-xs leading-relaxed mb-4">
              Carregamento instantâneo (&lt;0.8s), quebra de objeções por nicho, pré-seleção automática e fechamento completo em poucos cliques.
            </p>
          </div>
          <div class="pt-3 border-t border-white/5 flex items-center justify-between text-[11px] text-indigo-400 font-mono">
            <span>Zero Fricção</span>
            <i class="fa-solid fa-arrow-right"></i>
          </div>
        </div>

        <!-- Pilar 3 -->
        <div class="p-6 rounded-3xl bg-[#111624] border border-white/10 hover:border-purple-400/50 shadow-xl transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-purple-500/10 border border-purple-500/30 text-purple-400 flex items-center justify-center font-outfit font-black text-xl mb-4 group-hover:scale-110 transition-transform">
              03
            </div>
            <div class="flex items-center gap-2 mb-2">
              <i class="fa-solid fa-robot text-purple-400 text-base"></i>
              <h3 class="font-outfit font-bold text-lg text-white">Automação & IA WhatsApp</h3>
            </div>
            <p class="text-slate-400 text-xs leading-relaxed mb-4">
              Resposta imediata em 3 segundos 24/7. A IA tira dúvidas frequentes, qualifica a urgência e prepara o agendamento sem deixar o cliente esperar.
            </p>
          </div>
          <div class="pt-3 border-t border-white/5 flex items-center justify-between text-[11px] text-purple-400 font-mono">
            <span>Sem Espera 24/7</span>
            <i class="fa-solid fa-arrow-right"></i>
          </div>
        </div>

        <!-- Pilar 4 -->
        <div class="p-6 rounded-3xl bg-[#111624] border border-white/10 hover:border-emerald-400/50 shadow-xl transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 flex items-center justify-center font-outfit font-black text-xl mb-4 group-hover:scale-110 transition-transform">
              04
            </div>
            <div class="flex items-center gap-2 mb-2">
              <i class="fa-solid fa-chart-line text-emerald-400 text-base"></i>
              <h3 class="font-outfit font-bold text-lg text-white">CRM & Pipeline Ativo</h3>
            </div>
            <p class="text-slate-400 text-xs leading-relaxed mb-4">
              O lead chega organizado no funil Kanban com histórico, cálculo de ROI e disparo de lembretes automáticos para maximizar a conversão.
            </p>
          </div>
          <div class="pt-3 border-t border-white/5 flex items-center justify-between text-[11px] text-emerald-400 font-mono">
            <span>Venda Fechada & ROI</span>
            <i class="fa-solid fa-check"></i>
          </div>
        </div>

      </div>

    </div>
  </section>
"""

    if 'id="pilares"' not in html_main:
        html_main = html_main.replace('  <!-- ========================================================================= -->\n  <!-- 3. ROW 1: EM ALTA', pilares_section + '\n  <!-- ========================================================================= -->\n  <!-- 3. ROW 1: EM ALTA', 1)
        print("Added Section 'Os 4 Pilares' to index.html!")

    # 2.3 Add JavaScript smooth scroll handler
    main_js_scroll = """
    // Smooth Scroll & Visual Highlight for #pilares
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('a[href="#pilares"]').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const target = document.getElementById('pilares');
          if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            const cards = document.getElementById('pilares-cards-main') || target;
            cards.classList.add('ring-4', 'ring-cyan-400/50', 'rounded-3xl');
            setTimeout(() => {
              cards.classList.remove('ring-4', 'ring-cyan-400/50', 'rounded-3xl');
            }, 1800);
          }
        });
      });
    });
"""
    if 'a[href="#pilares"]' not in html_main:
        html_main = html_main.replace('</body>', '<script>' + main_js_scroll + '</script>\n</body>', 1)
        print("Added JS smooth scroll for #pilares in index.html!")

    with open(main_file, "w", encoding="utf-8") as f:
        f.write(html_main)
    print("index.html updated successfully!")

print("\n--- ALL DONE! ---")
