"""
Script to build the clean light portal for NEXUS FLOW:
- 3 buttons in navbar (Projetos, Serviços, Contato)
- High-tech, sophisticated button (White, Black, Emerald) with live tech pulse indicator (no glitched avatar)
- Button name: "Iniciar Projeto"
- Brand Logo adapted: High-tech emblem in Obsidian and Emerald, zero blue!
- Zero blue/cyan colors anywhere in the website
- Centered and adapted header navigation
- Smart Niche Omnibar with 32 niches
- Hidden catalog accordion
- Refactored visual Transparência Total
"""

import json, os, re
from build_niche_db import build_new_portal

def generate_light_portal():
    niche_db_json = build_new_portal()
    projects = json.loads(niche_db_json)
    
    # Generate the 32 portfolio cards for the hidden full catalog tab (ZERO BLUE, ONLY TECH EMERALD & WHITE)
    full_catalog_cards = []
    for p in projects:
        has_crm = p['has_crm']
        admin_btn = f'''
        <a href="{p['admin_url']}" target="_blank" class="py-2 px-3 rounded-xl bg-slate-900 text-emerald-400 hover:text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition-all">
          <i class="fa-solid fa-lock text-[10px]"></i> Painel CRM
        </a>
        ''' if has_crm else ''

        tags_html = "".join([f'<span class="px-2 py-0.5 rounded text-[10px] font-mono bg-slate-100 border border-slate-200 text-slate-600">{t}</span>' for t in p['tags'][:3]])

        card = f'''
        <div class="rounded-2xl bg-white border border-slate-200/80 hover:border-emerald-500/50 p-3 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div>
            <div class="h-44 w-full relative rounded-xl overflow-hidden bg-slate-100 cursor-pointer" onclick="window.open('{p['url']}', '_blank')">
              <img src="{p['image']}" alt="{p['title']}" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/60 via-transparent to-transparent"></div>
              <div class="absolute top-2.5 left-2.5 right-2.5 flex items-center justify-between pointer-events-none">
                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-white/90 text-slate-800 backdrop-blur-md shadow-sm border border-slate-200">
                  {p['title'].split('•')[0].strip()}
                </span>
                {'<span class="text-[10px] font-bold text-emerald-700 font-mono bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 backdrop-blur-md">CRM</span>' if has_crm else ''}
              </div>
            </div>
            <div class="p-3 space-y-2">
              <h4 class="text-sm font-bold text-slate-900 group-hover:text-emerald-600 transition-colors line-clamp-1">{p['title']}</h4>
              <p class="text-xs text-slate-500 line-clamp-2 leading-relaxed">{p['desc']}</p>
              <div class="flex flex-wrap gap-1 pt-1">
                {tags_html}
              </div>
            </div>
          </div>
          <div class="p-3 pt-2 border-t border-slate-100 flex items-center gap-2">
            <a href="{p['url']}" target="_blank" class="flex-1 py-2 px-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-center font-bold text-xs flex items-center justify-center gap-1.5 transition-colors shadow-sm">
              <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i> Ver Site
            </a>
            {admin_btn}
          </div>
        </div>
        '''
        full_catalog_cards.append(card)

    cards_grid_html = "\n".join(full_catalog_cards)

    # Clean HTML template
    html = f"""<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta http-equiv="X-Content-Type-Options" content="nosniff" />
  <meta name="referrer" content="strict-origin-when-cross-origin" />
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NEXUS FLOW — Engenharia Digital & Sistemas de Vendas</title>
  <meta name="description" content="Engenharia de sistemas de vendas: Landing Pages de alta conversão, CRMs especializados por segmento e automação de atendimento." />

  <!-- Fonts: Plus Jakarta Sans & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet" />

  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

  <!-- Tailwind CSS Engine -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              bg: '#f8fafc',
              surface: '#ffffff',
              border: '#e2e8f0',
              dark: '#09090b',
              emerald: '#059669',
              tech: '#10b981',
              amber: '#d97706'
            }}
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            heading: ['Outfit', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace']
          }}
        }}
      }}
    }};
  </script>

  <style>
    /* Technical top ruler markings */
    .header-ruler {{
      background-size: 20px 10px;
      background-image: linear-gradient(to right, rgba(0, 0, 0, 0.08) 1px, transparent 1px);
    }}
    .no-scrollbar::-webkit-scrollbar {{
      display: none;
    }}
    .no-scrollbar {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}
  </style>
</head>

<body class="bg-[#f8fafc] text-slate-800 font-sans antialiased overflow-x-hidden selection:bg-slate-900 selection:text-white">

  <!-- ========================================================================= -->
  <!-- 1. HEADER MINIMALISTA & CENTRALIZADO (3 BOTÕES + NOVO BOTÃO HIGH-TECH)    -->
  <!-- ========================================================================= -->
  <header id="site-header" class="sticky top-0 z-50 transition-all duration-300 bg-white/92 backdrop-blur-md border-b border-slate-200/80">
    <!-- Subtle technical tick marks on header top -->
    <div class="h-1.5 w-full header-ruler border-b border-slate-100 opacity-60"></div>
    
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
      
      <!-- Brand Logo (Adaptado: Obsidian + Emerald, sem azul) -->
      <a href="#hero" class="flex items-center gap-3 group focus:outline-none shrink-0" aria-label="NEXUS FLOW Início">
        <div class="w-10 h-10 rounded-xl bg-slate-950 p-[2px] shadow-sm group-hover:scale-105 transition-transform duration-300 shrink-0 flex items-center justify-center border border-slate-800">
          <i class="fa-solid fa-layer-group text-emerald-400 text-sm sm:text-base"></i>
        </div>
        <div class="flex flex-col">
          <div class="flex items-center gap-1.5">
            <span class="font-extrabold text-base sm:text-lg tracking-tight text-slate-950">NEXUS</span>
            <span class="font-bold text-base sm:text-lg tracking-tight text-emerald-600">FLOW</span>
          </div>
          <span class="text-[8.5px] text-slate-400 font-semibold tracking-wider uppercase">Sistemas & Vendas</span>
        </div>
      </a>

      <!-- Exact 3 Buttons Navigation: Centralizada com precisão (Projetos ⁰¹, Serviços ⁰², Contato ⁰³) -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-700 mx-auto" aria-label="Navegação Principal">
        <a href="#projetos" class="hover:text-black transition-colors flex items-center gap-1 py-1 group">
          <span class="group-hover:translate-x-0.5 transition-transform">Projetos</span>
          <sup class="text-[10px] text-slate-400 font-mono">01</sup>
        </a>
        <a href="#servicos" class="hover:text-black transition-colors flex items-center gap-1 py-1 group">
          <span class="group-hover:translate-x-0.5 transition-transform">Serviços</span>
          <sup class="text-[10px] text-slate-400 font-mono">02</sup>
        </a>
        <a href="#contato" class="hover:text-black transition-colors flex items-center gap-1 py-1 group">
          <span class="group-hover:translate-x-0.5 transition-transform">Contato</span>
          <sup class="text-[10px] text-slate-400 font-mono">03</sup>
        </a>
      </nav>

      <!-- Action Group: Language Switcher + Novo Botão Tecnológico e Sofisticado -->
      <div class="flex items-center gap-3 sm:gap-5 shrink-0">
        
        <!-- Language Switcher -->
        <div class="hidden lg:flex items-center gap-1.5 text-xs font-mono font-bold text-slate-400">
          <span class="hover:text-slate-800 cursor-pointer">ES</span>
          <span>/</span>
          <span class="text-slate-900 cursor-pointer">PT</span>
          <span>/</span>
          <span class="hover:text-slate-800 cursor-pointer">EN</span>
        </div>

        <!-- NOVO BOTÃO RECONSTRUÍDO (Sofisticação, Tecnologia, Branco + Preto + Indicador Esmeralda) -->
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostaria%20de%20iniciar%20um%20projeto%20com%20a%20NEXUS%20FLOW." target="_blank" class="inline-flex items-center justify-between gap-3 sm:gap-4 pl-2 sm:pl-2.5 pr-2 sm:pr-2.5 py-1.5 rounded-full bg-slate-950 hover:bg-black text-white border border-slate-800 hover:border-emerald-500/50 shadow-[0_4px_16px_rgba(0,0,0,0.12)] hover:shadow-[0_6px_24px_rgba(16,185,129,0.2)] transition-all duration-300 group shrink-0">
          
          <!-- Ícone Tecnológico com Pulso Ativo de Sistema (Substitui o avatar recortado) -->
          <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-900 border border-slate-700/80 flex items-center justify-center shrink-0">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-[0_0_8px_#34d399] animate-pulse"></span>
          </div>

          <!-- Nome Reconstruído do Botão: "Iniciar Projeto" -->
          <span class="text-xs sm:text-sm font-bold tracking-tight text-white group-hover:text-emerald-300 transition-colors hidden min-[380px]:inline">
            Iniciar Projeto
          </span>
          <span class="text-xs font-bold tracking-tight text-white min-[380px]:hidden">
            Projeto
          </span>

          <!-- Seta Circular de Ação em Branco Puro -->
          <div class="w-6 h-6 sm:w-7 sm:h-7 rounded-full bg-white text-slate-950 flex items-center justify-center text-xs group-hover:translate-x-1 transition-transform shrink-0 shadow-sm">
            <i class="fa-solid fa-arrow-right text-[9px] sm:text-[10px]"></i>
          </div>

        </a>

        <!-- Mobile Menu Toggle Button -->
        <button id="mobile-menu-toggle" aria-label="Abrir Menu" class="md:hidden p-2 sm:p-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition-colors shrink-0">
          <i class="fa-solid fa-bars text-sm sm:text-base"></i>
        </button>

      </div>

    </div>
  </header>

  <!-- Mobile Navigation Drawer -->
  <div id="mobile-drawer" class="fixed inset-0 z-[100] bg-white/98 backdrop-blur-2xl transition-all duration-300 md:hidden flex flex-col p-6 overflow-y-auto pointer-events-none opacity-0">
    <div class="flex items-center justify-between pb-6 border-b border-slate-200">
      <div class="flex items-center gap-2">
        <span class="font-extrabold text-lg text-slate-900">NEXUS</span>
        <span class="font-bold text-lg text-emerald-600">FLOW</span>
      </div>
      <button id="mobile-drawer-close" aria-label="Fechar Menu" class="p-2.5 rounded-xl bg-slate-100 text-slate-700 hover:bg-slate-200">
        <i class="fa-solid fa-xmark text-lg"></i>
      </button>
    </div>

    <div class="py-8 flex flex-col gap-6 text-xl font-bold text-slate-800">
      <a href="#projetos" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span>Projetos ⁰¹</span>
        <span class="text-xs font-mono text-emerald-600">01</span>
      </a>
      <a href="#servicos" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span>Serviços ⁰²</span>
        <span class="text-xs font-mono text-emerald-600">02</span>
      </a>
      <a href="#contato" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span>Contato ⁰³</span>
        <span class="text-xs font-mono text-emerald-600">03</span>
      </a>
      <a href="#transparencia" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span>Transparência Total</span>
        <span class="text-xs font-mono text-emerald-600">04</span>
      </a>
    </div>

    <div class="mt-auto pt-6 border-t border-slate-200 space-y-3">
      <div class="text-xs text-slate-500 font-mono text-center">WhatsApp Oficial: (32) 99929-2311</div>
      <a href="https://wa.me/5532999292311" target="_blank" class="w-full py-3.5 px-4 rounded-full bg-slate-950 text-white font-bold text-center flex items-center justify-center gap-2 text-sm shadow-md">
        <i class="fa-brands fa-whatsapp text-emerald-400 text-base"></i> Iniciar Projeto no WhatsApp
      </a>
    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- 2. HERO — POSICIONAMENTO E INTRODUÇÃO VISUAL                              -->
  <!-- ========================================================================= -->
  <section id="hero" class="relative py-16 sm:py-24 border-b border-slate-200/80 bg-gradient-to-b from-white to-[#f8fafc]">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
      
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider bg-slate-100 border border-slate-200 text-slate-700 shadow-sm">
        <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
        Engenharia Digital de Vendas
      </div>

      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-slate-900 tracking-tight max-w-4xl mx-auto leading-[1.12]">
        Seu site não precisa apenas receber visitas.
        <span class="block text-emerald-600">
          Ele precisa saber o que fazer com elas.
        </span>
      </h1>

      <p class="text-base sm:text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
        Construímos ecossistemas completos para transformar visitantes em clientes: Landing Pages de alta conversão, CRMs especializados por segmento e automação de WhatsApp.
      </p>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 3. BARRA DE REQUISIÇÃO POR NICHO & CATÁLOGO ESCONDIDO EM ABA               -->
  <!-- ========================================================================= -->
  <section id="projetos" class="py-16 sm:py-24 border-b border-slate-200/80 bg-white">
    <div class="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
      
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-800 bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
          <i class="fa-solid fa-magnifying-glass mr-1.5"></i> Barra de Requisição Inteligente
        </span>
        <h2 class="text-2xl sm:text-4xl font-extrabold text-slate-900">
          Qual é o seu nicho de atuação?
        </h2>
        <p class="text-sm text-slate-600 leading-relaxed">
          Digite abaixo o seu ramo de negócio para visualizar instantaneamente a arquitetura de vendas e o sistema sob medida já desenvolvido.
        </p>
      </div>

      <!-- The Smart Request Omnibar -->
      <div class="max-w-3xl mx-auto space-y-4">
        <div class="relative flex items-center shadow-lg rounded-2xl border-2 border-slate-200 hover:border-slate-400 focus-within:!border-slate-900 bg-white transition-all overflow-hidden p-2">
          <div class="pl-3 pr-2 text-slate-400">
            <i class="fa-solid fa-magnifying-glass text-lg"></i>
          </div>
          <input type="text" id="niche-omnibar-input" placeholder="Digite seu nicho (ex: energia solar, dentista, vendedor automotivo...)" oninput="handleNicheSearch(this.value)" class="w-full py-3 px-2 text-sm sm:text-base font-medium text-slate-900 placeholder-slate-400 focus:outline-none" />
          <button onclick="handleNicheSearch(document.getElementById('niche-omnibar-input').value)" class="px-5 py-3 rounded-xl bg-slate-950 hover:bg-slate-800 text-white font-bold text-xs sm:text-sm transition-all shrink-0">
            Buscar
          </button>
        </div>

        <!-- Suggestion Chips for Fast 1-Click Request -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-2 text-xs font-medium text-slate-600">
          <span class="text-slate-400 font-mono text-[11px] shrink-0">Sugestões rápidas:</span>
          <button onclick="requestNiche('energia solar')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">☀️ Energia Solar</button>
          <button onclick="requestNiche('dentista')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🦷 Dentista</button>
          <button onclick="requestNiche('vendedor automotivo')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🏎️ Automotivo / Motos</button>
          <button onclick="requestNiche('advogado')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">⚖️ Advocacia</button>
          <button onclick="requestNiche('pet')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🐾 Petshop</button>
          <button onclick="requestNiche('imobiliaria')" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🏠 Imóveis</button>
        </div>
      </div>

      <!-- Real-Time Request Results Container -->
      <div id="request-result-area" class="max-w-4xl mx-auto pt-4">
        <!-- Rendered dynamically by JavaScript -->
      </div>

      <!-- Toggle Button to Open Full Hidden Catalog Tab -->
      <div class="pt-8 border-t border-slate-200 text-center space-y-4">
        <button id="toggle-full-catalog-btn" onclick="toggleFullCatalog()" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs sm:text-sm border border-slate-300 transition-all shadow-sm">
          <i class="fa-solid fa-layer-group text-slate-900"></i>
          <span id="toggle-catalog-text">Abrir Aba com Catálogo Completo (32 Sistemas)</span>
          <i id="toggle-catalog-icon" class="fa-solid fa-chevron-down text-xs transition-transform"></i>
        </button>
      </div>

      <!-- Hidden Full Catalog Section (Toggled on click) -->
      <div id="hidden-full-catalog-container" class="hidden pt-6">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {cards_grid_html}
        </div>
      </div>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 4. TRANSPARÊNCIA TOTAL — NOVO LAYOUT COM ELEMENTOS VISUAIS E ANIMAÇÃO    -->
  <!-- ========================================================================= -->
  <section id="transparencia" class="py-20 sm:py-28 border-b border-slate-200/80 bg-[#f8fafc]">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <!-- Section Header -->
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-800 bg-slate-100 px-3.5 py-1.5 rounded-full border border-slate-200 inline-flex items-center gap-1.5 shadow-sm">
          <i class="fa-solid fa-circle-question text-slate-900"></i> TRANSPARÊNCIA TOTAL
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
          Talvez você esteja pensando...
        </h2>
        <p class="text-sm sm:text-base text-slate-600 leading-relaxed">
          Respostas honestas, visuais e diretas para as dúvidas mais comuns antes de implementar um sistema de vendas.
        </p>
      </div>

      <!-- Illustrated Visual Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Card 1: "Eu já tenho um site." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-800 font-mono font-bold text-xs flex items-center justify-center border border-slate-200">01</span>
              <span class="text-[11px] font-mono font-semibold text-slate-400">Comparativo Real</span>
            </div>
            <h3 class="text-lg font-bold text-slate-900 leading-snug">"Eu Já tenho um site."</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Ter um site comum muitas vezes é o mesmo que ter um folheto impresso parado na gaveta. Sem qualificação ativa e CRM, você perde a maioria dos contatos.
            </p>
          </div>

          <!-- Visual Graphic Diagram: Traditional vs Nexus Flow -->
          <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-2.5 font-mono text-xs">
            <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-center justify-between">
              <span class="text-slate-500 flex items-center gap-1.5"><i class="fa-solid fa-xmark text-rose-500"></i> Site Tradicional:</span>
              <span class="text-rose-600 font-bold">Folheto Parado</span>
            </div>
            <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-between">
              <span class="text-emerald-800 font-bold flex items-center gap-1.5"><i class="fa-solid fa-check text-emerald-600"></i> NEXUS FLOW:</span>
              <span class="text-emerald-700 font-bold">Captura & CRM Ativo</span>
            </div>
          </div>
        </div>

        <!-- Card 2: "Eu Já uso WhatsApp no dia a dia." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold text-xs flex items-center justify-center border border-emerald-200">02</span>
              <span class="text-[11px] font-mono font-semibold text-emerald-600"><i class="fa-brands fa-whatsapp mr-1"></i>Estruturado</span>
            </div>
            <h3 class="text-lg font-bold text-slate-900 leading-snug">"Eu Já uso WhatsApp no dia a dia."</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              O WhatsApp continua sendo o canal principal de fechamento, mas com o nosso sistema o lead já chega qualificado e registrado no Kanban, sem sumir em conversas perdidas.
            </p>
          </div>

          <!-- Visual WhatsApp Preview Bubble Graphic -->
          <div class="p-3.5 rounded-2xl bg-[#e7f7ef] border border-emerald-200 space-y-2 text-xs">
            <div class="flex items-center gap-2 pb-1.5 border-b border-emerald-200/60">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span class="text-[10px] font-mono text-emerald-800 font-bold">Lead Qualificado Recebido</span>
            </div>
            <div class="p-2 rounded-xl bg-white text-slate-800 text-[11px] shadow-sm leading-relaxed">
              "Olá! Fiz a simulação no site para <strong>Energia Solar</strong> e quero agendar a vistoria técnica."
            </div>
          </div>
        </div>

        <!-- Card 3: "Minha empresa é pequena demais para isso?" -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-800 font-mono font-bold text-xs flex items-center justify-center border border-slate-200">03</span>
              <span class="text-[11px] font-mono font-semibold text-slate-400">Escalabilidade</span>
            </div>
            <h3 class="text-lg font-bold text-slate-900 leading-snug">"Minha empresa é pequena demais para isso?"</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Pelo contrário: pequenas empresas têm equipes enxutas e não podem perder nenhum cliente por demora. O sistema economiza 2 horas diárias do dono em tarefas manuais.
            </p>
          </div>

          <!-- Visual Progressive Scale Diagram -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2 text-xs font-mono">
            <div class="flex items-center justify-between p-1.5 bg-white rounded-lg border border-slate-200">
              <span class="text-slate-600 text-[11px]">Nível 1: Comece com a Landing</span>
              <span class="text-slate-900 font-bold text-[10px]">Rápido</span>
            </div>
            <div class="flex items-center justify-between p-1.5 bg-white rounded-lg border border-slate-200">
              <span class="text-slate-600 text-[11px]">Nível 2: Adicione o CRM</span>
              <span class="text-emerald-700 font-bold text-[10px]">Ordem</span>
            </div>
          </div>
        </div>

        <!-- Card 4: "Não quero um sistema complicado de usar." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-800 font-mono font-bold text-xs flex items-center justify-center border border-slate-200">04</span>
              <span class="text-[11px] font-mono font-semibold text-slate-400">Fácil & Rápido</span>
            </div>
            <h3 class="text-lg font-bold text-slate-900 leading-snug">"Não quero um sistema complicado de usar."</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Nossos painéis foram pensados para quem tem pressa: botões grandes, contraste visual claro de lucro e custo, sem menus escondidos ou treinamentos intermináveis.
            </p>
          </div>

          <!-- Visual UI Mockup Snippet -->
          <div class="p-3.5 rounded-2xl bg-slate-900 text-white space-y-2 text-xs font-mono">
            <div class="flex items-center justify-between pb-1.5 border-b border-slate-800 text-[10px]">
              <span class="text-slate-400">PAINEL DO OPERADOR</span>
              <span class="text-emerald-400">1 CLIQUE</span>
            </div>
            <div class="grid grid-cols-2 gap-2 text-center text-[10px]">
              <div class="p-2 rounded-lg bg-slate-800 border border-slate-700">Ver Lucro Líquido</div>
              <div class="p-2 rounded-lg bg-emerald-950 text-emerald-300 border border-emerald-700">Chamar no Whats</div>
            </div>
          </div>
        </div>

        <!-- Card 5: "Eu já assino outro CRM de mercado." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-800 font-mono font-bold text-xs flex items-center justify-center border border-slate-200">05</span>
              <span class="text-[11px] font-mono font-semibold text-slate-400">Integração Total</span>
            </div>
            <h3 class="text-lg font-bold text-slate-900 leading-snug">"Eu já assino outro CRM de mercado."</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Podemos integrar nossas Landing Pages de alta conversão diretamente ao seu software existente, ou substituir ferramentas caras por uma solução definitiva.
            </p>
          </div>

          <!-- Visual Integration Connector Diagram -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-2 text-xs font-mono">
            <div class="flex items-center justify-center gap-2 text-[11px] font-bold text-slate-700">
              <span class="px-2 py-1 bg-white rounded border border-slate-200">Landing Page</span>
              <span>➔</span>
              <span class="px-2 py-1 bg-white rounded border border-slate-200 text-slate-900 font-bold">Seu CRM Atual</span>
            </div>
            <div class="text-[10px] text-slate-400">HubSpot • RD Station • Pipedrive • WhatsApp</div>
          </div>
        </div>

        <!-- Card 6: "Isso parece caro." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-amber-50 text-amber-700 font-mono font-bold text-xs flex items-center justify-center border border-amber-200">06</span>
              <span class="text-[11px] font-mono font-semibold text-amber-700">Retorno Rápido</span>
            </div>
            <h3 class="text-lg font-bold text-slate-900 leading-snug">"Isso parece caro."</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Caro é gastar R$ 1.500 em anúncios todo mês e perder contatos por falta de resposta rápida. Uma estrutura profissional se paga rapidamente no primeiro lote de vendas fechadas.
            </p>
          </div>

          <!-- Visual Financial Return Scale -->
          <div class="p-3.5 rounded-2xl bg-amber-50/60 border border-amber-200 space-y-2 text-xs font-mono">
            <div class="flex justify-between items-center text-[11px]">
              <span class="text-slate-600">Perda sem sistema:</span>
              <span class="text-rose-600 font-bold">-R$ 4.500/mês</span>
            </div>
            <div class="flex justify-between items-center text-[11px] pt-1 border-t border-amber-200/60">
              <span class="text-slate-800 font-bold">Com o ecossistema:</span>
              <span class="text-emerald-700 font-bold">+R$ 15.000 em vendas</span>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 5. SERVIÇOS & SOLUÇÕES (RESUMO CONCISO)                                   -->
  <!-- ========================================================================= -->
  <section id="servicos" class="py-20 sm:py-28 border-b border-slate-200/80 bg-white">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-700 bg-slate-100 px-3.5 py-1.5 rounded-full border border-slate-200">
          SERVIÇOS DE ENGENHARIA DIGITAL
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900">
          O que Desenvolvemos para sua Empresa
        </h2>
        <p class="text-sm sm:text-base text-slate-600">
          Soluções construídas para resolver o gargalo de vendas e trazer previsibilidade.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="p-8 rounded-3xl bg-slate-50 border border-slate-200 space-y-4 hover:shadow-lg transition-all">
          <div class="w-12 h-12 rounded-2xl bg-slate-950 text-white flex items-center justify-center text-xl shadow-md border border-slate-800">
            <i class="fa-solid fa-window-maximize text-emerald-400"></i>
          </div>
          <h3 class="text-xl font-bold text-slate-900">Landing Pages Estratégicas</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Páginas ultra-rápidas desenvolvidas para quebrar objeções específicas do seu nicho, com simuladores de orçamento e botão direto para o WhatsApp.
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-slate-50 border border-slate-200 space-y-4 hover:shadow-lg transition-all">
          <div class="w-12 h-12 rounded-2xl bg-emerald-600 text-white flex items-center justify-center text-xl shadow-md">
            <i class="fa-solid fa-diagram-project"></i>
          </div>
          <h3 class="text-xl font-bold text-slate-900">CRMs Adaptáveis (Serviço & Vendas)</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Painéis Kanban sob medida: modelo para Prestadores de Serviço (com cálculo fracionado de insumos g/kg/un) e modelo para Vendas (com CMV e margem líquida).
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-slate-50 border border-slate-200 space-y-4 hover:shadow-lg transition-all">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-white flex items-center justify-center text-xl shadow-md">
            <i class="fa-solid fa-robot text-emerald-400"></i>
          </div>
          <h3 class="text-xl font-bold text-slate-900">Automação de WhatsApp & IA</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Triagem imediata de leads, disparos automáticos de lembretes para evitar faltas e alertas no celular da equipe de vendas em tempo real.
          </p>
        </div>

      </div>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 6. CONTATO & CTA FINAL / FOOTER                                           -->
  <!-- ========================================================================= -->
  <footer id="contato" class="py-20 sm:py-28 bg-slate-950 text-white relative overflow-hidden">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8 relative z-10">
      
      <div class="max-w-2xl mx-auto space-y-4">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950/80 px-3.5 py-1.5 rounded-full border border-emerald-500/30 inline-flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span> Atendimento Imediato
        </span>
        <h2 class="text-3xl sm:text-5xl font-extrabold tracking-tight">
          Pronto para construir seu sistema de vendas?
        </h2>
        <p class="text-sm sm:text-base text-slate-400 leading-relaxed">
          Converse diretamente conosco pelo WhatsApp oficial e descubra qual modelo é o ideal para sua empresa.
        </p>
      </div>

      <!-- NOVO BOTÃO NO FOOTER (Sofisticado, Branco + Preto + Indicador Esmeralda) -->
      <div class="pt-4 flex flex-wrap items-center justify-center gap-4">
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Quero%20iniciar%20meu%20projeto%20com%20a%20NEXUS%20FLOW." target="_blank" class="inline-flex items-center justify-between gap-4 pl-3 pr-2.5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-950 transition-all font-bold text-sm shadow-xl group border border-slate-200">
          <div class="w-8 h-8 rounded-full bg-slate-950 flex items-center justify-center shrink-0">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-[0_0_8px_#34d399] animate-pulse"></span>
          </div>
          <span class="tracking-tight font-extrabold text-slate-950">Iniciar Projeto pelo WhatsApp</span>
          <div class="w-7 h-7 rounded-full bg-slate-950 text-white flex items-center justify-center text-xs group-hover:translate-x-1 transition-transform shrink-0">
            <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </div>
        </a>
      </div>

      <div class="pt-8 text-xs font-mono text-slate-500 flex items-center justify-center gap-4">
        <span><i class="fa-solid fa-phone mr-1"></i> (32) 99929-2311</span>
        <span>•</span>
        <span><i class="fa-solid fa-location-dot mr-1"></i> São Paulo / SP</span>
        <span>•</span>
        <span>© 2026 NEXUS FLOW</span>
      </div>

    </div>
  </footer>


  <!-- ========================================================================= -->
  <!-- CLIENT JAVASCRIPT: SMART OMNIBAR & MINIMAL INTERACTION                   -->
  <!-- ========================================================================= -->
  <script>
    // Embedded Database of all 32 niches
    const nicheDatabase = {niche_db_json};

    // Mobile drawer toggle
    const menuToggle = document.getElementById('mobile-menu-toggle');
    const drawerClose = document.getElementById('mobile-drawer-close');
    const drawer = document.getElementById('mobile-drawer');

    if (menuToggle && drawer) {{
      menuToggle.addEventListener('click', () => {{
        drawer.classList.remove('pointer-events-none', 'opacity-0');
        drawer.classList.add('pointer-events-auto', 'opacity-100');
      }});
    }}
    if (drawerClose && drawer) {{
      drawerClose.addEventListener('click', () => {{
        drawer.classList.add('pointer-events-none', 'opacity-0');
        drawer.classList.remove('pointer-events-auto', 'opacity-100');
      }});
    }}
    document.querySelectorAll('.mobile-nav-link').forEach(link => {{
      link.addEventListener('click', () => {{
        if (drawer) {{
          drawer.classList.add('pointer-events-none', 'opacity-0');
          drawer.classList.remove('pointer-events-auto', 'opacity-100');
        }}
      }});
    }});

    // Smart Request Omnibar Logic
    function handleNicheSearch(term) {{
      const query = (term || '').toLowerCase().trim();
      const resultArea = document.getElementById('request-result-area');
      if (!resultArea) return;

      if (query.length < 2) {{
        renderDefaultNicheCard();
        return;
      }}

      // Find best match in database
      const matched = nicheDatabase.filter(item => {{
        const titleMatch = item.title.toLowerCase().includes(query);
        const descMatch = item.desc.toLowerCase().includes(query);
        const kwMatch = item.keywords.some(k => k.toLowerCase().includes(query) || query.includes(k.toLowerCase()));
        return titleMatch || descMatch || kwMatch;
      }});

      if (matched.length > 0) {{
        renderMatchedCards(matched.slice(0, 3), query);
      }} else {{
        renderCustomRequestCard(query);
      }}
    }}

    function requestNiche(nicheName) {{
      const input = document.getElementById('niche-omnibar-input');
      if (input) {{
        input.value = nicheName;
        handleNicheSearch(nicheName);
        input.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      }}
    }}

    function renderDefaultNicheCard() {{
      const resultArea = document.getElementById('request-result-area');
      if (!resultArea) return;

      // Default featured niche: SunEco OS (Energia Solar)
      const solar = nicheDatabase.find(n => n.id === 'energia-solar') || nicheDatabase[0];
      if (!solar) return;

      resultArea.innerHTML = `
        <div class="rounded-3xl bg-slate-50 border-2 border-slate-900 p-6 sm:p-8 space-y-6 shadow-md transition-all">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-slate-800 uppercase">SISTEMA EM DESTAQUE (MODELO)</span>
            <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200">
              Disponível
            </span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
            <div class="md:col-span-6 h-56 rounded-2xl overflow-hidden bg-slate-200 border border-slate-200 shadow-inner">
              <img src="${{solar.image}}" alt="${{solar.title}}" class="w-full h-full object-cover object-top" />
            </div>
            <div class="md:col-span-6 space-y-4">
              <h3 class="text-2xl font-extrabold text-slate-900">${{solar.title}}</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">${{solar.desc}}</p>
              <div class="flex flex-wrap gap-2 pt-1">
                ${{solar.tags.slice(0, 3).map(t => `<span class="px-2.5 py-1 rounded-lg text-xs font-mono bg-white border border-slate-200 text-slate-700 font-semibold">${{t}}</span>`).join('')}}
              </div>
              <div class="flex flex-wrap items-center gap-3 pt-3">
                <a href="${{solar.url}}" target="_blank" class="px-5 py-2.5 rounded-xl bg-slate-950 hover:bg-slate-800 text-white font-bold text-xs flex items-center gap-2 transition-all">
                  <span>Acessar Site do Nicho</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
                ${{solar.has_crm ? `<a href="${{solar.admin_url}}" target="_blank" class="px-4 py-2.5 rounded-xl bg-white hover:bg-slate-100 text-slate-900 border border-slate-300 font-bold text-xs flex items-center gap-2 transition-all"><i class="fa-solid fa-lock text-emerald-600"></i> Painel CRM</a>` : ''}}
                <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostei%20do%20sistema%20para%20${{encodeURIComponent(solar.title)}}%20e%20quero%20um%20diagn%C3%B3stico." target="_blank" class="p-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition-all" title="Pedir no WhatsApp">
                  <i class="fa-brands fa-whatsapp text-sm"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    function renderMatchedCards(items, query) {{
      const resultArea = document.getElementById('request-result-area');
      if (!resultArea) return;

      const cardsHtml = items.map(item => `
        <div class="rounded-3xl bg-slate-50 border-2 border-slate-900 p-6 sm:p-8 space-y-6 shadow-md transition-all">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-slate-900 uppercase">Sistema Encontrado para: "${{query}}"</span>
            <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200">
              Disponível
            </span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
            <div class="md:col-span-6 h-56 rounded-2xl overflow-hidden bg-slate-200 border border-slate-200 shadow-inner">
              <img src="${{item.image}}" alt="${{item.title}}" class="w-full h-full object-cover object-top" />
            </div>
            <div class="md:col-span-6 space-y-4">
              <h3 class="text-2xl font-extrabold text-slate-900">${{item.title}}</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">${{item.desc}}</p>
              <div class="flex flex-wrap gap-2 pt-1">
                ${{item.tags.slice(0, 3).map(t => `<span class="px-2.5 py-1 rounded-lg text-xs font-mono bg-white border border-slate-200 text-slate-700 font-semibold">${{t}}</span>`).join('')}}
              </div>
              <div class="flex flex-wrap items-center gap-3 pt-3">
                <a href="${{item.url}}" target="_blank" class="px-5 py-2.5 rounded-xl bg-slate-950 hover:bg-slate-800 text-white font-bold text-xs flex items-center gap-2 transition-all">
                  <span>Acessar Site do Nicho</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
                ${{item.has_crm ? `<a href="${{item.admin_url}}" target="_blank" class="px-4 py-2.5 rounded-xl bg-white hover:bg-slate-100 text-slate-900 border border-slate-300 font-bold text-xs flex items-center gap-2 transition-all"><i class="fa-solid fa-lock text-emerald-600"></i> Painel CRM</a>` : ''}}
                <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostei%20do%20sistema%20para%20${{encodeURIComponent(item.title)}}%20e%20quero%20um%20diagn%C3%B3stico." target="_blank" class="p-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition-all" title="Pedir no WhatsApp">
                  <i class="fa-brands fa-whatsapp text-sm"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      `).join('');

      resultArea.innerHTML = cardsHtml;
    }}

    function renderCustomRequestCard(query) {{
      const resultArea = document.getElementById('request-result-area');
      if (!resultArea) return;

      resultArea.innerHTML = `
        <div class="rounded-3xl bg-slate-100 border-2 border-dashed border-slate-300 p-8 text-center space-y-4">
          <div class="w-12 h-12 rounded-2xl bg-slate-950 text-white flex items-center justify-center text-lg mx-auto">
            <i class="fa-solid fa-wand-magic-sparkles text-emerald-400"></i>
          </div>
          <h3 class="text-xl font-bold text-slate-900">Podemos construir a solução perfeita para "${{query}}"!</h3>
          <p class="text-xs sm:text-sm text-slate-600 max-w-md mx-auto leading-relaxed">
            Nossa engenharia adapta landing pages de alta velocidade e CRMs de serviços/vendas para qualquer segmento em poucos dias.
          </p>
          <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Meu%20nicho%20%C3%A9%20${{encodeURIComponent(query)}}%20e%20gostaria%20de%20um%20or%C3%A7amento%20sob%20medida." target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-slate-950 hover:bg-slate-800 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-md">
            <i class="fa-brands fa-whatsapp text-emerald-400"></i> Solicitar Sistema para ${{query}}
          </a>
        </div>
      `;
    }}

    // Toggle full catalog view
    function toggleFullCatalog() {{
      const container = document.getElementById('hidden-full-catalog-container');
      const text = document.getElementById('toggle-catalog-text');
      const icon = document.getElementById('toggle-catalog-icon');
      if (!container) return;

      if (container.classList.contains('hidden')) {{
        container.classList.remove('hidden');
        if (text) text.textContent = 'Fechar Catálogo de 32 Sistemas';
        if (icon) icon.className = 'fa-solid fa-chevron-up text-xs transition-transform';
      }} else {{
        container.classList.add('hidden');
        if (text) text.textContent = 'Abrir Aba com Catálogo Completo (32 Sistemas)';
        if (icon) icon.className = 'fa-solid fa-chevron-down text-xs transition-transform';
      }}
    }}

    // Init on load
    document.addEventListener('DOMContentLoaded', () => {{
      renderDefaultNicheCard();
    }});
  </script>

</body>
</html>
"""
    return html

if __name__ == '__main__':
    content = generate_light_portal()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Portal regenerated successfully, length:", len(content))
