import json, os, re
from build_niche_db import build_new_portal

def generate_light_portal():
    niche_db_json = build_new_portal()
    projects = json.loads(niche_db_json)
    
    # Generate the portfolio cards for the hidden full catalog tab
    full_catalog_cards = []
    for p in projects:
        has_crm = p['has_crm']
        admin_btn = f'''
        <a href="{p['admin_url']}" target="_blank" class="py-2 px-3 rounded-xl bg-slate-900 text-emerald-400 hover:text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition-all">
          <i class="fa-solid fa-lock text-[10px]"></i> <span data-i18n="card_crm_btn">Painel CRM</span>
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
              <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i> <span data-i18n="card_view_btn">Ver Site</span>
            </a>
            {admin_btn}
          </div>
        </div>
        '''
        full_catalog_cards.append(card)

    cards_grid_html = "\n".join(full_catalog_cards)
    total_systems = len(projects)

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

  <!-- GSAP & ScrollTrigger Engine for Obsidian/Refero Motion -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

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
    /* Obsidian & Refero Motion Tokens */
    :root {{
      --duration-fast: 120ms;
      --duration-default: 200ms;
      --duration-slow: 320ms;
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
    }}
    * {{
      -webkit-font-smoothing: antialiased;
    }}
    /* Cult UI Shimmer CTA Button Animation */
    @keyframes shimmerMove {{
      0% {{ transform: translateX(-150%); }}
      100% {{ transform: translateX(150%); }}
    }}
    .shimmer-btn {{
      position: relative;
      overflow: hidden;
    }}
    .shimmer-btn::after {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.18), transparent);
      transform: translateX(-150%);
      animation: shimmerMove 3.5s infinite;
      pointer-events: none;
    }}

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

    /* ========================================================================= */
    /* ANIMAÇÃO DE ENTRADA CINEMATOGRÁFICA (< 3 SEGUNDOS): LOGO NÍTIDO + DESBORRAR */
    /* ========================================================================= */
    @keyframes introOverlayFlow {{
      0% {{
        backdrop-filter: blur(28px);
        -webkit-backdrop-filter: blur(28px);
        background-color: rgba(248, 250, 252, 0.88);
        opacity: 1;
        visibility: visible;
      }}
      40% {{
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        background-color: rgba(248, 250, 252, 0.82);
        opacity: 1;
      }}
      70% {{
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        background-color: rgba(248, 250, 252, 0.45);
        opacity: 0.9;
      }}
      88% {{
        backdrop-filter: blur(0px);
        -webkit-backdrop-filter: blur(0px);
        background-color: rgba(248, 250, 252, 0.05);
        opacity: 0.25;
      }}
      100% {{
        backdrop-filter: blur(0px);
        -webkit-backdrop-filter: blur(0px);
        background-color: rgba(248, 250, 252, 0);
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
      }}
    }}

    @keyframes introLogoCrispReveal {{
      0% {{
        transform: scale(0.88);
        opacity: 0;
        filter: blur(8px);
      }}
      22% {{
        transform: scale(1);
        opacity: 1;
        filter: blur(0px);
      }}
      65% {{
        transform: scale(1);
        opacity: 1;
        filter: blur(0px);
      }}
      88% {{
        transform: scale(1.05);
        opacity: 0.2;
        filter: blur(3px);
      }}
      100% {{
        transform: scale(1.08);
        opacity: 0;
        filter: blur(8px);
        visibility: hidden;
      }}
    }}

    #intro-cinematic-overlay {{
      animation: introOverlayFlow 2.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    #intro-logo-box {{
      animation: introLogoCrispReveal 2.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    @media (prefers-reduced-motion: reduce) {{
      #intro-cinematic-overlay {{
        display: none !important;
      }}
    }}
  </style>
</head>

<body class="bg-[#f8fafc] text-slate-800 font-sans antialiased overflow-x-hidden selection:bg-slate-900 selection:text-white pb-16 md:pb-0">

  <!-- ========================================================================= -->
  <!-- CINEMATIC INTRO: LOGO NÍTIDO EM DESTAQUE COM AMBIENTE EM VOLTA BORRADO    -->
  <!-- QUE VAI DESBORRANDO EM MENOS DE 3 SEGUNDOS (2.3s TOTAL COM SKIP NO CLIQUE)-->
  <!-- ========================================================================= -->
  <div id="intro-cinematic-overlay" onclick="skipIntroAnimation()" class="fixed inset-0 z-[9999] flex items-center justify-center cursor-pointer select-none">
    <div id="intro-logo-box" class="flex flex-col items-center gap-4 text-center px-6">
      
      <!-- Logo Tile com brilho esmeralda de alta tecnologia -->
      <div class="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-slate-950 p-[3px] shadow-[0_0_50px_rgba(16,185,129,0.35)] flex items-center justify-center border border-slate-800">
        <i class="fa-solid fa-layer-group text-emerald-400 text-2xl sm:text-3xl"></i>
      </div>

      <!-- Nome da Marca Nítido -->
      <div class="flex items-center gap-2">
        <span class="font-extrabold text-3xl sm:text-5xl tracking-tight text-slate-950">NEXUS</span>
        <span class="font-bold text-3xl sm:text-5xl tracking-tight text-emerald-600">FLOW</span>
      </div>

      <!-- Subtítulo e Indicador de Pulso -->
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/90 border border-slate-200/90 text-slate-800 text-xs font-mono font-bold shadow-sm">
        <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
        <span data-i18n="brand_subtitle">Sistemas & Vendas</span>
      </div>

    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- 1. HEADER MINIMALISTA & CENTRALIZADO (3 BOTÕES + IDIOMAS + NOVO BOTÃO)     -->
  <!-- ========================================================================= -->
  <header id="site-header" class="sticky top-0 z-50 transition-all duration-300 bg-white/92 backdrop-blur-md border-b border-slate-200/80">
    <!-- Subtle technical tick marks on header top -->
    <div class="h-1.5 w-full header-ruler border-b border-slate-100 opacity-60"></div>
    
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-3 sm:gap-4">
      
      <!-- Brand Logo (Adaptado: Obsidian + Emerald, sem azul) -->
      <a href="#hero" class="flex items-center gap-2.5 sm:gap-3 group focus:outline-none shrink-0" aria-label="NEXUS FLOW Início">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-slate-950 p-[2px] shadow-sm group-hover:scale-105 transition-transform duration-300 shrink-0 flex items-center justify-center border border-slate-800">
          <i class="fa-solid fa-layer-group text-emerald-400 text-sm sm:text-base"></i>
        </div>
        <div class="flex flex-col">
          <div class="flex items-center gap-1 sm:gap-1.5">
            <span class="font-extrabold text-base sm:text-lg tracking-tight text-slate-950">NEXUS</span>
            <span class="font-bold text-base sm:text-lg tracking-tight text-emerald-600">FLOW</span>
          </div>
          <span data-i18n="brand_subtitle" class="text-[8.5px] text-slate-400 font-semibold tracking-wider uppercase">Sistemas & Vendas</span>
        </div>
      </a>

      <!-- Exact 3 Buttons Navigation: Centralizada com precisão (Projetos ⁰¹, Serviços ⁰², Contato ⁰³) -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-700 mx-auto" aria-label="Navegação Principal">
        <a href="#projetos" class="hover:text-black transition-colors flex items-center gap-1 py-1 group">
          <span data-i18n="nav_projects" class="group-hover:translate-x-0.5 transition-transform">Projetos</span>
          <sup class="text-[10px] text-slate-400 font-mono">01</sup>
        </a>
        <a href="#comparativo-originkit" class="hover:text-black transition-colors flex items-center gap-1 py-1 group">
          <span data-i18n="nav_comparison" class="group-hover:translate-x-0.5 transition-transform">Diferenciais</span>
          <sup class="text-[10px] text-slate-400 font-mono">02</sup>
        </a>
        <a href="#servicos" class="hover:text-black transition-colors flex items-center gap-1 py-1 group">
          <span data-i18n="nav_services" class="group-hover:translate-x-0.5 transition-transform">Serviços</span>
          <sup class="text-[10px] text-slate-400 font-mono">03</sup>
        </a>
        <a href="#contato" class="hover:text-black transition-colors flex items-center gap-1 py-1 group">
          <span data-i18n="nav_contact" class="group-hover:translate-x-0.5 transition-transform">Contato</span>
          <sup class="text-[10px] text-slate-400 font-mono">04</sup>
        </a>
      </nav>

      <!-- Action Group: Seletor Interativo de Idiomas (ES / PT / EN) + Botão Tecnológico -->
      <div class="flex items-center gap-2.5 sm:gap-4 shrink-0">
        
        <!-- SELETOR DE IDIOMAS INTERATIVO (ESPAÑOL / PORTUGUÊS / ENGLISH) -->
        <div class="flex items-center gap-1 text-xs font-mono font-bold bg-slate-100/90 px-2 sm:px-2.5 py-1 rounded-full border border-slate-200 shadow-inner">
          <button onclick="setLanguage('es')" id="lang-btn-es" class="px-1.5 py-0.5 rounded transition-all text-slate-500 hover:text-slate-900" title="Español (España)">ES</button>
          <span class="text-slate-300 font-light select-none">/</span>
          <button onclick="setLanguage('pt')" id="lang-btn-pt" class="px-1.5 py-0.5 rounded transition-all text-slate-950 font-extrabold bg-white shadow-sm" title="Português (Brasil)">PT</button>
          <span class="text-slate-300 font-light select-none">/</span>
          <button onclick="setLanguage('en')" id="lang-btn-en" class="px-1.5 py-0.5 rounded transition-all text-slate-500 hover:text-slate-900" title="English (US)">EN</button>
        </div>

        <!-- NOVO BOTÃO RECONSTRUÍDO COM SHIMMER BUTTON (Branco + Preto + Indicador Esmeralda) -->
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostaria%20de%20iniciar%20um%20projeto%20com%20a%20NEXUS%20FLOW." target="_blank" class="shimmer-btn inline-flex items-center justify-between gap-2.5 sm:gap-3.5 pl-2 sm:pl-2.5 pr-2 sm:pr-2.5 py-1.5 rounded-full bg-slate-950 hover:bg-black text-white border border-slate-800 hover:border-emerald-500/50 shadow-[0_4px_16px_rgba(0,0,0,0.12)] hover:shadow-[0_6px_24px_rgba(16,185,129,0.2)] transition-all duration-300 group shrink-0">
          
          <!-- Ícone Tecnológico com Pulso Ativo de Sistema -->
          <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-900 border border-slate-700/80 flex items-center justify-center shrink-0">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-[0_0_8px_#34d399] animate-pulse"></span>
          </div>

          <!-- Nome Reconstruído do Botão -->
          <span data-i18n="btn_start_project" class="text-xs sm:text-sm font-bold tracking-tight text-white group-hover:text-emerald-300 transition-colors hidden sm:inline">
            Iniciar Projeto
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

    <!-- Idiomas no Mobile Drawer -->
    <div class="pt-4 pb-2 flex items-center justify-between border-b border-slate-100">
      <span class="text-xs font-mono text-slate-500 font-bold uppercase" data-i18n="lang_selector_label">Idioma / Language:</span>
      <div class="flex items-center gap-1.5 text-xs font-mono font-bold bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
        <button onclick="setLanguage('es')" id="mobile-lang-es" class="px-1.5 py-0.5 rounded text-slate-500">ES</button>
        <span class="text-slate-300">/</span>
        <button onclick="setLanguage('pt')" id="mobile-lang-pt" class="px-1.5 py-0.5 rounded text-slate-950 font-extrabold bg-white shadow-sm">PT</button>
        <span class="text-slate-300">/</span>
        <button onclick="setLanguage('en')" id="mobile-lang-en" class="px-1.5 py-0.5 rounded text-slate-500">EN</button>
      </div>
    </div>

    <div class="py-6 flex flex-col gap-5 text-xl font-bold text-slate-800">
      <a href="#projetos" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span data-i18n="nav_projects_full">Projetos ⁰¹</span>
        <span class="text-xs font-mono text-emerald-600">01</span>
      </a>
      <a href="#comparativo-originkit" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span data-i18n="nav_comparison_full">Diferenciais ⁰²</span>
        <span class="text-xs font-mono text-emerald-600">02</span>
      </a>
      <a href="#servicos" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span data-i18n="nav_services_full">Serviços ⁰³</span>
        <span class="text-xs font-mono text-emerald-600">03</span>
      </a>
      <a href="#contato" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span data-i18n="nav_contact_full">Contato ⁰⁴</span>
        <span class="text-xs font-mono text-emerald-600">04</span>
      </a>
      <a href="#transparencia" class="mobile-nav-link flex items-center justify-between py-2 border-b border-slate-100">
        <span data-i18n="transp_tag">Transparência Total</span>
        <span class="text-xs font-mono text-emerald-600">05</span>
      </a>
    </div>

    <div class="mt-auto pt-6 border-t border-slate-200 space-y-3">
      <div class="text-xs text-slate-500 font-mono text-center">WhatsApp Oficial: (32) 99929-2311</div>
      <a href="https://wa.me/5532999292311" target="_blank" class="w-full py-3.5 px-4 rounded-full bg-slate-950 text-white font-bold text-center flex items-center justify-center gap-2 text-sm shadow-md">
        <i class="fa-brands fa-whatsapp text-emerald-400 text-base"></i> <span data-i18n="btn_whatsapp_modal">Iniciar Projeto no WhatsApp</span>
      </a>
    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- 2. HERO — POSICIONAMENTO E INTRODUÇÃO VISUAL                              -->
  <!-- ========================================================================= -->
  <section id="hero" class="relative py-16 sm:py-24 border-b border-slate-200/80 bg-gradient-to-b from-white to-[#f8fafc] gsap-reveal">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
      
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider bg-slate-100 border border-slate-200 text-slate-700 shadow-sm">
        <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
        <span data-i18n="hero_badge">Engenharia Digital de Vendas</span>
      </div>

      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-slate-900 tracking-tight max-w-4xl mx-auto leading-[1.12]">
        <span data-i18n="hero_h1_part1">Seu site não precisa apenas receber visitas.</span>
        <span data-i18n="hero_h1_part2" class="block text-emerald-600">
          Ele precisa saber o que fazer com elas.
        </span>
      </h1>

      <p data-i18n="hero_desc" class="text-base sm:text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
        Construímos ecossistemas completos para transformar visitantes em clientes: Landing Pages de alta conversão, CRMs especializados por segmento e automação de WhatsApp.
      </p>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 3. BARRA DE REQUISIÇÃO POR NICHO & CATÁLOGO ESCONDIDO EM ABA               -->
  <!-- ========================================================================= -->
  <section id="projetos" class="py-16 sm:py-24 border-b border-slate-200/80 bg-white gsap-reveal">
    <div class="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
      
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-800 bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
          <i class="fa-solid fa-magnifying-glass mr-1.5"></i> <span data-i18n="omnibar_tag">Barra de Requisição Inteligente</span>
        </span>
        <h2 data-i18n="omnibar_title" class="text-2xl sm:text-4xl font-extrabold text-slate-900">
          Qual é o seu nicho de atuação?
        </h2>
        <p data-i18n="omnibar_desc" class="text-sm text-slate-600 leading-relaxed">
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
            <span data-i18n="omnibar_btn_search">Buscar</span>
          </button>
        </div>

        <!-- Suggestion Chips for Fast 1-Click Request -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-2 text-xs font-medium text-slate-600">
          <span data-i18n="omnibar_suggestions_label" class="text-slate-400 font-mono text-[11px] shrink-0">Sugestões rápidas:</span>
          <button onclick="requestNiche('energia solar')" data-i18n="chip_solar" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">☀️ Energia Solar</button>
          <button onclick="requestNiche('dentista')" data-i18n="chip_dentist" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🦷 Dentista</button>
          <button onclick="requestNiche('sorveteria')" data-i18n="chip_icecream" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🍦 Sorveteria / Gelato</button>
          <button onclick="requestNiche('vendedor automotivo')" data-i18n="chip_auto" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🏎️ Automotivo / Motos</button>
          <button onclick="requestNiche('advogado')" data-i18n="chip_lawyer" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">⚖️ Advocacia</button>
          <button onclick="requestNiche('pet')" data-i18n="chip_pet" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🐾 Petshop</button>
          <button onclick="requestNiche('imobiliaria')" data-i18n="chip_realestate" class="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 transition-colors shrink-0">🏠 Imóveis</button>
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
          <span id="toggle-catalog-text" data-i18n="catalog_btn_open">Abrir Aba com Catálogo Completo ({total_systems} Sistemas)</span>
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
  <!-- 4. COMPARATIVO ORIGINKIT — OBSIDIAN PATTERN CONTRASTE DE AUTORIDADE       -->
  <!-- ========================================================================= -->
  <section id="comparativo-originkit" class="py-20 sm:py-28 border-b border-slate-200/80 bg-zinc-50 gsap-reveal">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-16 space-y-3">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-800 bg-white px-3.5 py-1.5 rounded-full border border-slate-200 inline-flex items-center gap-1.5 shadow-sm">
          <i class="fa-solid fa-scale-balanced text-emerald-600"></i> <span data-i18n="originkit_tag">MATRIZ COMPARATIVA DE VALOR</span>
        </span>
        <h2 data-i18n="originkit_title" class="text-3xl sm:text-4xl font-extrabold text-zinc-900 tracking-tight">
          Por que a NEXUS FLOW é diferente do mercado comum?
        </h2>
        <p data-i18n="originkit_desc" class="text-sm sm:text-base text-zinc-600 leading-relaxed">
          Compare a previsibilidade e a garantia de um ecossistema de engenharia autoral contra as alternativas genéricas e amadoras.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-stretch">
        
        <!-- Opções Comuns do Mercado -->
        <div class="p-8 rounded-3xl bg-white border border-zinc-200/80 shadow-sm flex flex-col justify-between opacity-85">
          <div class="space-y-6">
            <h3 class="text-xl font-bold text-zinc-500 flex items-center gap-2">
              <span class="text-rose-500 font-bold">✕</span> <span data-i18n="originkit_bad_title">Agências & Freelancers Amadores</span>
            </h3>
            <ul class="space-y-4 text-zinc-600 text-sm">
              <li class="flex items-start gap-3">
                <span class="text-rose-500 font-bold shrink-0">✕</span>
                <span data-i18n="originkit_bad_1">Templates prontos de WordPress pesados que demoram mais de 4s para carregar</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-rose-500 font-bold shrink-0">✕</span>
                <span data-i18n="originkit_bad_2">Apenas entregam o site e somem, sem integração de CRM ou funil de vendas</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-rose-500 font-bold shrink-0">✕</span>
                <span data-i18n="originkit_bad_3">Custos mensais ocultos com plugins vulneráveis e manutenções surpresa</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-rose-500 font-bold shrink-0">✕</span>
                <span data-i18n="originkit_bad_4">Leads chegam desorganizados e se perdem no WhatsApp pessoal sem histórico</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-rose-500 font-bold shrink-0">✕</span>
                <span data-i18n="originkit_bad_5">Prazos vagos que atrasam semanas sem nenhuma garantia contratual de entrega</span>
              </li>
            </ul>
          </div>
          <div class="pt-6 border-t border-zinc-100 text-xs font-mono text-zinc-400">
            <span data-i18n="originkit_bad_footer">Resultado: Dinheiro de tráfego desperdiçado e conversão imprevisível.</span>
          </div>
        </div>

        <!-- Nosso Padrão de Engenharia NEXUS FLOW -->
        <div class="p-8 rounded-3xl bg-white border-2 border-emerald-600 shadow-xl relative ring-4 ring-emerald-600/10 flex flex-col justify-between">
          <div class="absolute -top-3.5 right-6 bg-emerald-600 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm">
            <span data-i18n="originkit_good_badge">Engenharia Autoral</span>
          </div>
          <div class="space-y-6">
            <h3 class="text-xl font-bold text-emerald-900 flex items-center gap-2">
              <span class="text-emerald-600 font-bold">✓</span> <span data-i18n="originkit_good_title">Ecossistemas NEXUS FLOW</span>
            </h3>
            <ul class="space-y-4 text-zinc-800 text-sm font-medium">
              <li class="flex items-start gap-3 text-emerald-800">
                <span class="text-emerald-600 font-bold shrink-0">✓</span>
                <span data-i18n="originkit_good_1">Código autoral ultra-rápido (< 1s) sem dependência de plataformas lentas</span>
              </li>
              <li class="flex items-start gap-3 text-emerald-800">
                <span class="text-emerald-600 font-bold shrink-0">✓</span>
                <span data-i18n="originkit_good_2">Ecossistema completo: Landing Page + Painel Kanban CRM + Automação de WhatsApp</span>
              </li>
              <li class="flex items-start gap-3 text-emerald-800">
                <span class="text-emerald-600 font-bold shrink-0">✓</span>
                <span data-i18n="originkit_good_3">Preço fixo transparente, sem mensalidades obrigatórias de licenças de terceiros</span>
              </li>
              <li class="flex items-start gap-3 text-emerald-800">
                <span class="text-emerald-600 font-bold shrink-0">✓</span>
                <span data-i18n="originkit_good_4">Leads pré-qualificados com cálculo de orçamento e direcionamento automático</span>
              </li>
              <li class="flex items-start gap-3 text-emerald-800">
                <span class="text-emerald-600 font-bold shrink-0">✓</span>
                <span data-i18n="originkit_good_5">Design editorial responsivo adaptado com precisão cirúrgica para o seu nicho</span>
              </li>
            </ul>
          </div>
          <div class="pt-6 border-t border-emerald-100 flex items-center justify-between">
            <span data-i18n="originkit_good_footer" class="text-xs font-mono font-bold text-emerald-700">Garantia total de entrega e conversão</span>
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Vi%20a%20matriz%20comparativa%20e%20quero%20o%20padr%C3%A3o%20NEXUS%20FLOW." target="_blank" class="text-xs font-bold text-emerald-800 hover:text-emerald-950 underline flex items-center gap-1">
              <span data-i18n="originkit_good_cta">Solicitar Padrão</span> <i class="fa-solid fa-arrow-right text-[10px]"></i>
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 5. TRANSPARÊNCIA TOTAL — RESPOSTAS DIRETAS E ANIMAÇÃO                     -->
  <!-- ========================================================================= -->
  <section id="transparencia" class="py-20 sm:py-28 border-b border-slate-200/80 bg-[#f8fafc] gsap-reveal">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <!-- Section Header -->
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-800 bg-slate-100 px-3.5 py-1.5 rounded-full border border-slate-200 inline-flex items-center gap-1.5 shadow-sm">
          <i class="fa-solid fa-circle-question text-slate-900"></i> <span data-i18n="transp_tag">TRANSPARÊNCIA TOTAL</span>
        </span>
        <h2 data-i18n="transp_title" class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
          Talvez você esteja pensando...
        </h2>
        <p data-i18n="transp_desc" class="text-sm sm:text-base text-slate-600 leading-relaxed">
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
              <span data-i18n="card1_badge" class="text-[11px] font-mono font-semibold text-slate-400">Comparativo Real</span>
            </div>
            <h3 data-i18n="card1_title" class="text-lg font-bold text-slate-900 leading-snug">"Eu Já tenho um site."</h3>
            <p data-i18n="card1_desc" class="text-xs text-slate-600 leading-relaxed">
              Ter um site comum muitas vezes é o mesmo que ter um folheto impresso parado na gaveta. Sem qualificação ativa e CRM, você perde a maioria dos contatos.
            </p>
          </div>

          <!-- Visual Graphic Diagram: Traditional vs Nexus Flow -->
          <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-2.5 font-mono text-xs">
            <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-center justify-between">
              <span class="text-slate-500 flex items-center gap-1.5"><i class="fa-solid fa-xmark text-rose-500"></i> <span data-i18n="card1_bad_label">Site Tradicional:</span></span>
              <span data-i18n="card1_bad_val" class="text-rose-600 font-bold">Folheto Parado</span>
            </div>
            <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-between">
              <span class="text-emerald-800 font-bold flex items-center gap-1.5"><i class="fa-solid fa-check text-emerald-600"></i> NEXUS FLOW:</span>
              <span data-i18n="card1_good_val" class="text-emerald-700 font-bold">Captura & CRM Ativo</span>
            </div>
          </div>
        </div>

        <!-- Card 2: "Eu Já uso WhatsApp no dia a dia." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-emerald-50 text-emerald-700 font-mono font-bold text-xs flex items-center justify-center border border-emerald-200">02</span>
              <span class="text-[11px] font-mono font-semibold text-emerald-600"><i class="fa-brands fa-whatsapp mr-1"></i><span data-i18n="card2_badge">Estruturado</span></span>
            </div>
            <h3 data-i18n="card2_title" class="text-lg font-bold text-slate-900 leading-snug">"Eu Já uso WhatsApp no dia a dia."</h3>
            <p data-i18n="card2_desc" class="text-xs text-slate-600 leading-relaxed">
              O WhatsApp continua sendo o canal principal de fechamento, mas com o nosso sistema o lead já chega qualificado e registrado no Kanban, sem sumir em conversas perdidas.
            </p>
          </div>

          <!-- Visual WhatsApp Preview Bubble Graphic -->
          <div class="p-3.5 rounded-2xl bg-[#e7f7ef] border border-emerald-200 space-y-2 text-xs">
            <div class="flex items-center gap-2 pb-1.5 border-b border-emerald-200/60">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span data-i18n="card2_bubble_tag" class="text-[10px] font-mono text-emerald-800 font-bold">Lead Qualificado Recebido</span>
            </div>
            <div data-i18n="card2_bubble_text" class="p-2 rounded-xl bg-white text-slate-800 text-[11px] shadow-sm leading-relaxed">
              "Olá! Fiz a simulação no site para <strong>Energia Solar</strong> e quero agendar a vistoria técnica."
            </div>
          </div>
        </div>

        <!-- Card 3: "Minha empresa é pequena demais para isso?" -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-800 font-mono font-bold text-xs flex items-center justify-center border border-slate-200">03</span>
              <span data-i18n="card3_badge" class="text-[11px] font-mono font-semibold text-slate-400">Escalabilidade</span>
            </div>
            <h3 data-i18n="card3_title" class="text-lg font-bold text-slate-900 leading-snug">"Minha empresa é pequena demais para isso?"</h3>
            <p data-i18n="card3_desc" class="text-xs text-slate-600 leading-relaxed">
              Pelo contrário: pequenas empresas têm equipes enxutas e não podem perder nenhum cliente por demora. O sistema economiza 2 horas diárias do dono em tarefas manuais.
            </p>
          </div>

          <!-- Visual Progressive Scale Diagram -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2 text-xs font-mono">
            <div class="flex items-center justify-between p-1.5 bg-white rounded-lg border border-slate-200">
              <span data-i18n="card3_level1" class="text-slate-600 text-[11px]">Nível 1: Comece com a Landing</span>
              <span data-i18n="card3_level1_tag" class="text-slate-900 font-bold text-[10px]">Rápido</span>
            </div>
            <div class="flex items-center justify-between p-1.5 bg-white rounded-lg border border-slate-200">
              <span data-i18n="card3_level2" class="text-slate-600 text-[11px]">Nível 2: Adicione o CRM</span>
              <span data-i18n="card3_level2_tag" class="text-emerald-700 font-bold text-[10px]">Ordem</span>
            </div>
          </div>
        </div>

        <!-- Card 4: "Não quero um sistema complicado de usar." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-800 font-mono font-bold text-xs flex items-center justify-center border border-slate-200">04</span>
              <span data-i18n="card4_badge" class="text-[11px] font-mono font-semibold text-slate-400">Fácil & Rápido</span>
            </div>
            <h3 data-i18n="card4_title" class="text-lg font-bold text-slate-900 leading-snug">"Não quero um sistema complicado de usar."</h3>
            <p data-i18n="card4_desc" class="text-xs text-slate-600 leading-relaxed">
              Nossos painéis foram pensados para quem tem pressa: botões grandes, contraste visual claro de lucro e custo, sem menus escondidos ou treinamentos intermináveis.
            </p>
          </div>

          <!-- Visual UI Mockup Snippet -->
          <div class="p-3.5 rounded-2xl bg-slate-900 text-white space-y-2 text-xs font-mono">
            <div class="flex items-center justify-between pb-1.5 border-b border-slate-800 text-[10px]">
              <span data-i18n="card4_panel_title" class="text-slate-400">PAINEL DO OPERADOR</span>
              <span data-i18n="card4_panel_badge" class="text-emerald-400">1 CLIQUE</span>
            </div>
            <div class="grid grid-cols-2 gap-2 text-center text-[10px]">
              <div data-i18n="card4_btn_profit" class="p-2 rounded-lg bg-slate-800 border border-slate-700">Ver Lucro Líquido</div>
              <div data-i18n="card4_btn_whats" class="p-2 rounded-lg bg-emerald-950 text-emerald-300 border border-emerald-700">Chamar no Whats</div>
            </div>
          </div>
        </div>

        <!-- Card 5: "Eu já assino outro CRM de mercado." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-800 font-mono font-bold text-xs flex items-center justify-center border border-slate-200">05</span>
              <span data-i18n="card5_badge" class="text-[11px] font-mono font-semibold text-slate-400">Integração Total</span>
            </div>
            <h3 data-i18n="card5_title" class="text-lg font-bold text-slate-900 leading-snug">"Eu já assino outro CRM de mercado."</h3>
            <p data-i18n="card5_desc" class="text-xs text-slate-600 leading-relaxed">
              Podemos integrar nossas Landing Pages de alta conversão diretamente ao seu software existente, ou substituir ferramentas caras por uma solução definitiva.
            </p>
          </div>

          <!-- Visual Integration Connector Diagram -->
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-2 text-xs font-mono">
            <div class="flex items-center justify-center gap-2 text-[11px] font-bold text-slate-700">
              <span data-i18n="card5_landing" class="px-2 py-1 bg-white rounded border border-slate-200">Landing Page</span>
              <span>➔</span>
              <span data-i18n="card5_target" class="px-2 py-1 bg-white rounded border border-slate-200 text-slate-900 font-bold">Seu CRM Atual</span>
            </div>
            <div class="text-[10px] text-slate-400">HubSpot • RD Station • Pipedrive • WhatsApp</div>
          </div>
        </div>

        <!-- Card 6: "Isso parece caro." -->
        <div class="rounded-3xl bg-white border border-slate-200 p-7 space-y-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-amber-50 text-amber-700 font-mono font-bold text-xs flex items-center justify-center border border-amber-200">06</span>
              <span data-i18n="card6_badge" class="text-[11px] font-mono font-semibold text-amber-700">Retorno Rápido</span>
            </div>
            <h3 data-i18n="card6_title" class="text-lg font-bold text-slate-900 leading-snug">"Isso parece caro."</h3>
            <p data-i18n="card6_desc" class="text-xs text-slate-600 leading-relaxed">
              Caro é gastar R$ 1.500 em anúncios todo mês e perder contatos por falta de resposta rápida. Uma estrutura profissional se paga rapidamente no primeiro lote de vendas fechadas.
            </p>
          </div>

          <!-- Visual Financial Return Scale -->
          <div class="p-3.5 rounded-2xl bg-amber-50/60 border border-amber-200 space-y-2 text-xs font-mono">
            <div class="flex justify-between items-center text-[11px]">
              <span data-i18n="card6_loss_label" class="text-slate-600">Perda sem sistema:</span>
              <span data-i18n="card6_loss_val" class="text-rose-600 font-bold">-R$ 4.500/mês</span>
            </div>
            <div class="flex justify-between items-center text-[11px] pt-1 border-t border-amber-200/60">
              <span data-i18n="card6_gain_label" class="text-slate-800 font-bold">Com o ecossistema:</span>
              <span data-i18n="card6_gain_val" class="text-emerald-700 font-bold">+R$ 15.000 em vendas</span>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 6. SERVIÇOS & SOLUÇÕES (RESUMO CONCISO)                                   -->
  <!-- ========================================================================= -->
  <section id="servicos" class="py-20 sm:py-28 border-b border-slate-200/80 bg-white gsap-reveal">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <span data-i18n="services_tag" class="text-xs font-mono font-bold uppercase tracking-wider text-slate-700 bg-slate-100 px-3.5 py-1.5 rounded-full border border-slate-200">
          SERVIÇOS DE ENGENHARIA DIGITAL
        </span>
        <h2 data-i18n="services_title" class="text-3xl sm:text-4xl font-extrabold text-slate-900">
          O que Desenvolvemos para sua Empresa
        </h2>
        <p data-i18n="services_desc" class="text-sm sm:text-base text-slate-600">
          Soluções construídas para resolver o gargalo de vendas e trazer previsibilidade.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="p-8 rounded-3xl bg-slate-50 border border-slate-200 space-y-4 hover:shadow-lg transition-all">
          <div class="w-12 h-12 rounded-2xl bg-slate-950 text-white flex items-center justify-center text-xl shadow-md border border-slate-800">
            <i class="fa-solid fa-window-maximize text-emerald-400"></i>
          </div>
          <h3 data-i18n="service1_title" class="text-xl font-bold text-slate-900">Landing Pages Estratégicas</h3>
          <p data-i18n="service1_desc" class="text-xs text-slate-600 leading-relaxed">
            Páginas ultra-rápidas desenvolvidas para quebrar objeções específicas do seu nicho, com simuladores de orçamento e botão direto para o WhatsApp.
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-slate-50 border border-slate-200 space-y-4 hover:shadow-lg transition-all">
          <div class="w-12 h-12 rounded-2xl bg-emerald-600 text-white flex items-center justify-center text-xl shadow-md">
            <i class="fa-solid fa-diagram-project"></i>
          </div>
          <h3 data-i18n="service2_title" class="text-xl font-bold text-slate-900">CRMs Adaptáveis (Serviço & Vendas)</h3>
          <p data-i18n="service2_desc" class="text-xs text-slate-600 leading-relaxed">
            Painéis Kanban sob medida: modelo para Prestadores de Serviço (com cálculo fracionado de insumos g/kg/un) e modelo para Vendas (com CMV e margem líquida).
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-slate-50 border border-slate-200 space-y-4 hover:shadow-lg transition-all">
          <div class="w-12 h-12 rounded-2xl bg-slate-950 text-white flex items-center justify-center text-xl shadow-md">
            <i class="fa-solid fa-robot text-emerald-400"></i>
          </div>
          <h3 data-i18n="service3_title" class="text-xl font-bold text-slate-900">Automação de WhatsApp & IA</h3>
          <p data-i18n="service3_desc" class="text-xs text-slate-600 leading-relaxed">
            Triagem imediata de leads, disparos automáticos de lembretes para evitar faltas e alertas no celular da equipe de vendas em tempo real.
          </p>
        </div>

      </div>

    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- 7. CONTATO & CTA FINAL / FOOTER                                           -->
  <!-- ========================================================================= -->
  <footer id="contato" class="py-20 sm:py-28 bg-slate-950 text-white relative overflow-hidden gsap-reveal">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8 relative z-10">
      
      <div class="max-w-2xl mx-auto space-y-4">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950/80 px-3.5 py-1.5 rounded-full border border-emerald-500/30 inline-flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span> <span data-i18n="footer_badge">Atendimento Imediato</span>
        </span>
        <h2 data-i18n="footer_title" class="text-3xl sm:text-5xl font-extrabold tracking-tight">
          Pronto para construir seu sistema de vendas?
        </h2>
        <p data-i18n="footer_desc" class="text-sm sm:text-base text-slate-400 leading-relaxed">
          Converse diretamente conosco pelo WhatsApp oficial e descubra qual modelo é o ideal para sua empresa.
        </p>
      </div>

      <!-- NOVO BOTÃO NO FOOTER COM SHIMMER -->
      <div class="pt-4 flex flex-wrap items-center justify-center gap-4">
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Quero%20iniciar%20meu%20projeto%20com%20a%20NEXUS%20FLOW." target="_blank" class="shimmer-btn inline-flex items-center justify-between gap-4 pl-3 pr-2.5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-950 transition-all font-bold text-sm shadow-xl group border border-slate-200">
          <div class="w-8 h-8 rounded-full bg-slate-950 flex items-center justify-center shrink-0">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-[0_0_8px_#34d399] animate-pulse"></span>
          </div>
          <span data-i18n="footer_btn" class="tracking-tight font-extrabold text-slate-950">Iniciar Projeto pelo WhatsApp</span>
          <div class="w-7 h-7 rounded-full bg-slate-950 text-white flex items-center justify-center text-xs group-hover:translate-x-1 transition-transform shrink-0">
            <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </div>
        </a>
      </div>

      <div class="pt-8 text-xs font-mono text-slate-500 flex items-center justify-center gap-4">
        <span><i class="fa-solid fa-phone mr-1"></i> (32) 99929-2311</span>
        <span>•</span>
        <span><i class="fa-solid fa-location-dot mr-1"></i> <span data-i18n="footer_location">São Paulo / SP</span></span>
        <span>•</span>
        <span>© 2026 NEXUS FLOW</span>
      </div>

    </div>
  </footer>


  <!-- ========================================================================= -->
  <!-- 8. ADR-002 MOBILE CONVERSION DOCK (STICKY BOTTOM EM SMARTPHONES)          -->
  <!-- ========================================================================= -->
  <aside class="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 p-3 shadow-[0_-4px_20px_rgba(0,0,0,0.25)]">
    <div class="flex items-center justify-between gap-3 max-w-md mx-auto">
      <div class="flex flex-col">
        <span class="text-xs font-bold text-white leading-tight" data-i18n="dock_title">Atendimento Direto</span>
        <span class="text-[11px] text-emerald-400 flex items-center gap-1 font-mono">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span> <span data-i18n="dock_online">Online agora</span>
        </span>
      </div>
      <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostaria%20de%20um%20diagn%C3%B3stico%20para%20minha%20empresa%20com%20a%20NEXUS%20FLOW." 
         class="shimmer-btn flex items-center gap-2 bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-extrabold text-xs px-4 py-2.5 rounded-full shadow-lg transition-transform active:scale-95">
        <i class="fa-brands fa-whatsapp text-sm"></i>
        <span data-i18n="dock_btn">Falar no WhatsApp</span>
      </a>
    </div>
  </aside>


  <!-- ========================================================================= -->
  <!-- CLIENT JAVASCRIPT: i18n ENGINE, INTRO ANIMATION & OMNIBAR                 -->
  <!-- ========================================================================= -->
  <script>
    // -------------------------------------------------------------------------
    // 1. Dicionário de Idiomas (PT: Português BR | EN: American | ES: España)
    // -------------------------------------------------------------------------
    const translations = {{
      pt: {{
        brand_subtitle: "Sistemas & Vendas",
        nav_projects: "Projetos",
        nav_comparison: "Diferenciais",
        nav_services: "Serviços",
        nav_contact: "Contato",
        nav_projects_full: "Projetos ⁰¹",
        nav_comparison_full: "Diferenciais ⁰²",
        nav_services_full: "Serviços ⁰³",
        nav_contact_full: "Contato ⁰⁴",
        btn_start_project: "Iniciar Projeto",
        btn_start_project_short: "Projeto",
        btn_whatsapp_modal: "Iniciar Projeto no WhatsApp",
        lang_selector_label: "Idioma / Language:",
        hero_badge: "Engenharia Digital de Vendas",
        hero_h1_part1: "Seu site não precisa apenas receber visitas.",
        hero_h1_part2: "Ele precisa saber o que fazer com elas.",
        hero_desc: "Construímos ecossistemas completos para transformar visitantes em clientes: Landing Pages de alta conversão, CRMs especializados por segmento e automação de WhatsApp.",
        omnibar_tag: "Barra de Requisição Inteligente",
        omnibar_title: "Qual é o seu nicho de atuação?",
        omnibar_desc: "Digite abaixo o seu ramo de negócio para visualizar instantaneamente a arquitetura de vendas e o sistema sob medida já desenvolvido.",
        omnibar_placeholder: "Digite seu nicho (ex: energia solar, dentista, vendedor automotivo...)",
        omnibar_btn_search: "Buscar",
        omnibar_suggestions_label: "Sugestões rápidas:",
        chip_solar: "☀️ Energia Solar",
        chip_dentist: "🦷 Dentista",
        chip_icecream: "🍦 Sorveteria / Gelato",
        chip_auto: "🏎️ Automotivo / Motos",
        chip_lawyer: "⚖️ Advocacia",
        chip_pet: "🐾 Petshop",
        chip_realestate: "🏠 Imóveis",
        catalog_btn_open: "Abrir Aba com Catálogo Completo ({total_systems} Sistemas)",
        catalog_btn_close: "Fechar Catálogo de {total_systems} Sistemas",
        card_view_btn: "Ver Site",
        card_crm_btn: "Painel CRM",
        originkit_tag: "MATRIZ COMPARATIVA DE VALOR",
        originkit_title: "Por que a NEXUS FLOW é diferente do mercado comum?",
        originkit_desc: "Compare a previsibilidade e a garantia de um ecossistema de engenharia autoral contra as alternativas genéricas e amadoras.",
        originkit_bad_title: "Agências & Freelancers Amadores",
        originkit_bad_1: "Templates prontos de WordPress pesados que demoram mais de 4s para carregar",
        originkit_bad_2: "Apenas entregam o site e somem, sem integração de CRM ou funil de vendas",
        originkit_bad_3: "Custos mensais ocultos com plugins vulneráveis e manutenções surpresa",
        originkit_bad_4: "Leads chegam desorganizados e se perdem no WhatsApp pessoal sem histórico",
        originkit_bad_5: "Prazos vagos que atrasam semanas sem nenhuma garantia contratual de entrega",
        originkit_bad_footer: "Resultado: Dinheiro de tráfego desperdiçado e conversão imprevisível.",
        originkit_good_badge: "Engenharia Autoral",
        originkit_good_title: "Ecossistemas NEXUS FLOW",
        originkit_good_1: "Código autoral ultra-rápido (< 1s) sem dependência de plataformas lentas",
        originkit_good_2: "Ecossistema completo: Landing Page + Painel Kanban CRM + Automação de WhatsApp",
        originkit_good_3: "Preço fixo transparente, sem mensalidades obrigatórias de licenças de terceiros",
        originkit_good_4: "Leads pré-qualificados com cálculo de orçamento e direcionamento automático",
        originkit_good_5: "Design editorial responsivo adaptado com precisão cirúrgica para o seu nicho",
        originkit_good_footer: "Garantia total de entrega e conversão",
        originkit_good_cta: "Solicitar Padrão",
        dock_title: "Atendimento Direto",
        dock_online: "Online agora",
        dock_btn: "Falar no WhatsApp",
        transp_tag: "TRANSPARÊNCIA TOTAL",
        transp_title: "Talvez você esteja pensando...",
        transp_desc: "Respostas honestas, visuais e diretas para as dúvidas mais comuns antes de implementar um sistema de vendas.",
        card1_badge: "Comparativo Real",
        card1_title: "\\"Eu Já tenho um site.\\"",
        card1_desc: "Ter um site comum muitas vezes é o mesmo que ter um folheto impresso parado na gaveta. Sem qualificação ativa e CRM, você perde a maioria dos contatos.",
        card1_bad_label: "Site Tradicional:",
        card1_bad_val: "Folheto Parado",
        card1_good_val: "Captura & CRM Ativo",
        card2_badge: "Estruturado",
        card2_title: "\\"Eu Já uso WhatsApp no dia a dia.\\"",
        card2_desc: "O WhatsApp continua sendo o canal principal de fechamento, mas com o nosso sistema o lead já chega qualificado e registrado no Kanban, sem sumir em conversas perdidas.",
        card2_bubble_tag: "Lead Qualificado Recebido",
        card2_bubble_text: "\\"Olá! Fiz a simulação no site para <strong>Energia Solar</strong> e quero agendar a vistoria técnica.\\"",
        card3_badge: "Escalabilidade",
        card3_title: "\\"Minha empresa é pequena demais para isso?\\"",
        card3_desc: "Pelo contrário: pequenas empresas têm equipes enxutas e não podem perder nenhum cliente por demora. O sistema economiza 2 horas diárias do dono em tarefas manuais.",
        card3_level1: "Nível 1: Comece com a Landing",
        card3_level1_tag: "Rápido",
        card3_level2: "Nível 2: Adicione o CRM",
        card3_level2_tag: "Ordem",
        card4_badge: "Fácil & Rápido",
        card4_title: "\\"Não quero um sistema complicado de usar.\\"",
        card4_desc: "Nossos painéis foram pensados para quem tem pressa: botões grandes, contraste visual claro de lucro e custo, sem menus escondidos ou treinamentos intermináveis.",
        card4_panel_title: "PAINEL DO OPERADOR",
        card4_panel_badge: "1 CLIQUE",
        card4_btn_profit: "Ver Lucro Líquido",
        card4_btn_whats: "Chamar no Whats",
        card5_badge: "Integração Total",
        card5_title: "\\"Eu já assino outro CRM de mercado.\\"",
        card5_desc: "Podemos integrar nossas Landing Pages de alta conversão diretamente ao seu software existente, ou substituir ferramentas caras por uma solução definitiva.",
        card5_landing: "Landing Page",
        card5_target: "Seu CRM Atual",
        card6_badge: "Retorno Rápido",
        card6_title: "\\"Isso parece caro.\\"",
        card6_desc: "Caro é gastar R$ 1.500 em anúncios todo mês e perder contatos por falta de resposta rápida. Uma estrutura profissional se paga rapidamente no primeiro lote de vendas fechadas.",
        card6_loss_label: "Perda sem sistema:",
        card6_loss_val: "-R$ 4.500/mês",
        card6_gain_label: "Com o ecossistema:",
        card6_gain_val: "+R$ 15.000 em vendas",
        services_tag: "SERVIÇOS DE ENGENHARIA DIGITAL",
        services_title: "O que Desenvolvemos para sua Empresa",
        services_desc: "Soluções construídas para resolver o gargalo de vendas e trazer previsibilidade.",
        service1_title: "Landing Pages Estratégicas",
        service1_desc: "Páginas ultra-rápidas desenvolvidas para quebrar objeções específicas do seu nicho, com simuladores de orçamento e botão direto para o WhatsApp.",
        service2_title: "CRMs Adaptáveis (Serviço & Vendas)",
        service2_desc: "Painéis Kanban sob medida: modelo para Prestadores de Serviço (com cálculo fracionado de insumos g/kg/un) e modelo para Vendas (com CMV e margem líquida).",
        service3_title: "Automação de WhatsApp & IA",
        service3_desc: "Triagem imediata de leads, disparos automáticos de lembretes para evitar faltas e alertas no celular da equipe de vendas em tempo real.",
        footer_badge: "Atendimento Imediato",
        footer_title: "Pronto para construir seu sistema de vendas?",
        footer_desc: "Converse diretamente conosco pelo WhatsApp oficial e descubra qual modelo é o ideal para sua empresa.",
        footer_btn: "Iniciar Projeto pelo WhatsApp",
        footer_location: "São Paulo / SP",
        niche_model_featured: "SISTEMA EM DESTAQUE (MODELO)",
        niche_available: "Disponível",
        niche_found: "Sistema Encontrado para:",
        niche_custom_title: "Podemos construir a solução perfeita para",
        niche_custom_desc: "Nossa engenharia adapta landing pages de alta velocidade e CRMs de serviços/vendas para qualquer segmento em poucos dias.",
        niche_custom_btn: "Solicitar Sistema para"
      }},
      en: {{
        brand_subtitle: "Systems & Sales",
        nav_projects: "Projects",
        nav_comparison: "Advantages",
        nav_services: "Services",
        nav_contact: "Contact",
        nav_projects_full: "Projects ⁰¹",
        nav_comparison_full: "Advantages ⁰²",
        nav_services_full: "Services ⁰³",
        nav_contact_full: "Contact ⁰⁴",
        btn_start_project: "Start Project",
        btn_start_project_short: "Project",
        btn_whatsapp_modal: "Start Project on WhatsApp",
        lang_selector_label: "Language / Idioma:",
        hero_badge: "Digital Sales Engineering",
        hero_h1_part1: "Your website shouldn't just receive visitors.",
        hero_h1_part2: "It needs to know what to do with them.",
        hero_desc: "We engineer end-to-end digital sales ecosystems: high-converting Landing Pages, industry-tailored CRMs, and intelligent WhatsApp automation.",
        omnibar_tag: "Smart Industry Request Bar",
        omnibar_title: "What is your business industry?",
        omnibar_desc: "Type your industry below to instantly inspect the custom sales architecture and systems already developed.",
        omnibar_placeholder: "Type your niche (e.g. solar energy, dentist, automotive dealer...)",
        omnibar_btn_search: "Search",
        omnibar_suggestions_label: "Quick suggestions:",
        chip_solar: "☀️ Solar Energy",
        chip_dentist: "🦷 Dentist",
        chip_icecream: "🍦 Ice Cream / Gelato",
        chip_auto: "🏎️ Automotive / Bikes",
        chip_lawyer: "⚖️ Law Firm",
        chip_pet: "🐾 Pet Shop",
        chip_realestate: "🏠 Real Estate",
        catalog_btn_open: "Open Full Catalog ({total_systems} Systems)",
        catalog_btn_close: "Close Full Catalog ({total_systems} Systems)",
        card_view_btn: "Live Demo",
        card_crm_btn: "CRM Panel",
        originkit_tag: "VALUE COMPARISON MATRIX",
        originkit_title: "Why NEXUS FLOW Outperforms Conventional Options",
        originkit_desc: "Compare the predictability and performance of tailored systems against generic and amateur market alternatives.",
        originkit_bad_title: "Agencies & Amateur Freelancers",
        originkit_bad_1: "Bloated generic WordPress themes taking over 4s to load on mobile",
        originkit_bad_2: "Hand off a static page and disappear—zero CRM or lead workflow",
        originkit_bad_3: "Hidden monthly maintenance fees with vulnerable, unstable plugins",
        originkit_bad_4: "Leads arrive scattered in personal chats with zero tracking or Kanban",
        originkit_bad_5: "Vague timelines delayed for weeks without contractual delivery guarantee",
        originkit_bad_footer: "Outcome: Wasted ad spend and zero predictable conversions.",
        originkit_good_badge: "Custom Engineering",
        originkit_good_title: "NEXUS FLOW Ecosystems",
        originkit_good_1: "Ultra-fast custom codebase (< 1s load) independent of heavy CMS bloat",
        originkit_good_2: "End-to-end ecosystem: Landing Page + Kanban CRM + WhatsApp automation",
        originkit_good_3: "Transparent fixed pricing—no mandatory third-party subscription locks",
        originkit_good_4: "Pre-qualified leads with quote simulation and intelligent routing",
        originkit_good_5: "High-end editorial design surgically tailored to your exact industry",
        originkit_good_footer: "Contractual delivery & conversion guarantee",
        originkit_good_cta: "Request Standard",
        dock_title: "Direct Support",
        dock_online: "Online now",
        dock_btn: "Chat on WhatsApp",
        transp_tag: "TOTAL TRANSPARENCY",
        transp_title: "You might be wondering...",
        transp_desc: "Direct, visual, and honest answers to the most common questions before implementing an automated sales system.",
        card1_badge: "Real Comparison",
        card1_title: "\\"I already have a website.\\"",
        card1_desc: "A conventional website is often like an unread brochure in a drawer. Without active qualification and an integrated CRM, most opportunities are lost.",
        card1_bad_label: "Traditional Site:",
        card1_bad_val: "Idle Brochure",
        card1_good_val: "Active Capture & CRM",
        card2_badge: "Structured",
        card2_title: "\\"I already use WhatsApp every day.\\"",
        card2_desc: "WhatsApp remains the primary deal-closing channel, but with our system leads arrive pre-qualified and synced to your Kanban—never buried in chats.",
        card2_bubble_tag: "Pre-Qualified Lead Received",
        card2_bubble_text: "\\"Hello! I completed the solar simulation on the website and want to schedule the technical inspection.\\"",
        card3_badge: "Scalability",
        card3_title: "\\"Is my business too small for this?\\"",
        card3_desc: "Quite the opposite: lean businesses have smaller teams and cannot afford slow response times. The system saves the owner 2 hours daily in manual chores.",
        card3_level1: "Stage 1: Launch the Landing Page",
        card3_level1_tag: "Fast",
        card3_level2: "Stage 2: Connect the CRM",
        card3_level2_tag: "Order",
        card4_badge: "Fast & Intuitive",
        card4_title: "\\"I don't want a complicated system.\\"",
        card4_desc: "Our panels are built for fast-paced founders: oversized controls, high-contrast net profit metrics, zero hidden menus or endless onboarding.",
        card4_panel_title: "OPERATOR CONSOLE",
        card4_panel_badge: "1-CLICK",
        card4_btn_profit: "View Net Profit",
        card4_btn_whats: "Open WhatsApp",
        card5_badge: "Seamless Sync",
        card5_title: "\\"I already subscribe to another CRM.\\"",
        card5_desc: "We can connect our high-converting Landing Pages directly into your existing CRM stack, or eliminate bloated subscriptions with a unified setup.",
        card5_landing: "Landing Page",
        card5_target: "Your Current CRM",
        card6_badge: "Fast Payback",
        card6_title: "\\"This sounds expensive.\\"",
        card6_desc: "Expensive is spending $1,500/month on ad campaigns and losing qualified prospects to delayed answers. A tailored setup pays for itself with the first batch of closed deals.",
        card6_loss_label: "Loss without system:",
        card6_loss_val: "-$4,500/mo",
        card6_gain_label: "With ecosystem:",
        card6_gain_val: "+$15,000 in sales",
        services_tag: "DIGITAL ENGINEERING SERVICES",
        services_title: "What We Engineer for Your Business",
        services_desc: "Bespoke digital architecture designed to eliminate sales friction and produce predictable revenue.",
        service1_title: "Strategic Landing Pages",
        service1_desc: "Ultra-fast web experiences engineered to disarm industry-specific buyer objections, featuring quote simulators and direct WhatsApp triggers.",
        service2_title: "Adaptive CRMs (Services & Sales)",
        service2_desc: "Bespoke Kanban workflows: Service Edition (fractional input cost accounting by g/kg/unit) and Sales Edition (COGS & net margin analytics).",
        service3_title: "WhatsApp Automation & AI",
        service3_desc: "Zero-latency lead triage, automated attendance reminders to eliminate no-shows, and instant sales team notification routing.",
        footer_badge: "Instant Support",
        footer_title: "Ready to engineer your sales system?",
        footer_desc: "Talk directly with our team on official WhatsApp to find the exact architecture for your business.",
        footer_btn: "Start Project on WhatsApp",
        footer_location: "São Paulo / Brazil",
        niche_model_featured: "FEATURED ARCHITECTURE (MODEL)",
        niche_available: "Available",
        niche_found: "System Found for:",
        niche_custom_title: "We can engineer the perfect system for",
        niche_custom_desc: "Our engineering team customizes high-speed landing engines and specialized CRMs for any niche in just a few days.",
        niche_custom_btn: "Request Custom System for"
      }},
      es: {{
        brand_subtitle: "Sistemas y Ventas",
        nav_projects: "Proyectos",
        nav_comparison: "Diferenciales",
        nav_services: "Servicios",
        nav_contact: "Contacto",
        nav_projects_full: "Proyectos ⁰¹",
        nav_comparison_full: "Diferenciales ⁰²",
        nav_services_full: "Servicios ⁰³",
        nav_contact_full: "Contacto ⁰⁴",
        btn_start_project: "Iniciar Proyecto",
        btn_start_project_short: "Proyecto",
        btn_whatsapp_modal: "Iniciar Proyecto por WhatsApp",
        lang_selector_label: "Idioma / Language:",
        hero_badge: "Ingeniería Digital de Ventas",
        hero_h1_part1: "Su sitio web no solo necesita recibir visitas.",
        hero_h1_part2: "Necesita saber qué hacer con ellas.",
        hero_desc: "Construimos ecosistemas integrales para convertir visitas en clientes: Landing Pages de alta conversión, CRMs especializados por sector y automatización de WhatsApp.",
        omnibar_tag: "Barra de Petición Inteligente",
        omnibar_title: "¿Cuál es su sector de actividad?",
        omnibar_desc: "Escriba su sector a continuación para ver al instante la arquitectura de ventas y el sistema a medida ya desarrollado.",
        omnibar_placeholder: "Escriba su sector (ej: energía solar, dentista, concesionario...)",
        omnibar_btn_search: "Buscar",
        omnibar_suggestions_label: "Sugerencias rápidas:",
        chip_solar: "☀️ Energía Solar",
        chip_dentist: "🦷 Dentista",
        chip_icecream: "🍦 Heladería / Gelato",
        chip_auto: "🏎️ Automoción / Motos",
        chip_lawyer: "⚖️ Abogacía",
        chip_pet: "🐾 Tienda de Mascotas",
        chip_realestate: "🏠 Inmobiliaria",
        catalog_btn_open: "Abrir Catálogo Completo ({total_systems} Sistemas)",
        catalog_btn_close: "Cerrar Catálogo de {total_systems} Sistemas",
        card_view_btn: "Ver Sitio",
        card_crm_btn: "Panel CRM",
        originkit_tag: "MATRIZ COMPARATIVA DE VALOR",
        originkit_title: "¿Por qué NEXUS FLOW es diferente de la oferta común?",
        originkit_desc: "Compare la certidumbre y garantía de un sistema de ingeniería propio frente a las soluciones estándar y aficionadas.",
        originkit_bad_title: "Agencias y Freelancers Novatos",
        originkit_bad_1: "Plantillas genéricas de WordPress que tardan más de 4s en cargar en móvil",
        originkit_bad_2: "Entregan una página web estática y desaparecen sin integración de CRM",
        originkit_bad_3: "Costes mensuales ocultos en plugins vulnerables y arreglos sorpresa",
        originkit_bad_4: "Los leads llegan desorganizados al chat personal y se pierden sin seguimiento",
        originkit_bad_5: "Plazos vagos que se retrasan semanas sin ninguna garantía por contrato",
        originkit_bad_footer: "Resultado: Presupuesto publicitario malgastado y cero previsibilidad.",
        originkit_good_badge: "Ingeniería Autoral",
        originkit_good_title: "Ecosistemas NEXUS FLOW",
        originkit_good_1: "Código exclusivo ultra rápido (< 1s) sin dependencia de plataformas lentas",
        originkit_good_2: "Ecosistema integral: Landing Page + Panel Kanban CRM + Automatización WhatsApp",
        originkit_good_3: "Precio fijo transparente sin suscripciones obligatorias a terceros",
        originkit_good_4: "Leads pre-cualificados con cálculo interactivo y enrutamiento ágil",
        originkit_good_5: "Diseño editorial adaptado con precisión milimétrica a su industria",
        originkit_good_footer: "Garantía contractual de entrega y conversión",
        originkit_good_cta: "Solicitar Estándar",
        dock_title: "Atención Inmediata",
        dock_online: "En línea ahora",
        dock_btn: "Hablar por WhatsApp",
        transp_tag: "TRANSPARENCIA TOTAL",
        transp_title: "Quizás esté pensando...",
        transp_desc: "Respuestas honestas, visuales y directas a las dudas más frecuentes antes de implementar un sistema de ventas.",
        card1_badge: "Comparativa Real",
        card1_title: "\\"Ya tengo una página web.\\"",
        card1_desc: "Tener una web convencional a menudo equivale a tener un folleto impreso en un cajón. Sin cualificación activa ni CRM, se pierde la mayoría de los contactos.",
        card1_bad_label: "Web Tradicional:",
        card1_bad_val: "Folleto Inactivo",
        card1_good_val: "Captación y CRM Activo",
        card2_badge: "Estructurado",
        card2_title: "\\"Ya uso WhatsApp a diario.\\"",
        card2_desc: "WhatsApp sigue siendo el canal principal de cierre, mas con nuestro sistema el lead llega cualificado y registrado en el Kanban, sin perderse en chats.",
        card2_bubble_tag: "Lead Cualificado Recibido",
        card2_bubble_text: "\\"¡Hola! Hice la simulación en la web para <strong>Energía Solar</strong> y quiero concertar la visita técnica.\\"",
        card3_badge: "Escalabilidad",
        card3_title: "\\"¿Mi empresa es demasiado pequeña para esto?\\"",
        card3_desc: "Al contrario: las pequeñas empresas tienen equipos reducidos y no pueden perder clientes por demoras. El sistema ahorra 2 horas diarias al propietario.",
        card3_level1: "Nivel 1: Empiece con la Landing Page",
        card3_level1_tag: "Rápido",
        card3_level2: "Nivel 2: Conecte el CRM",
        card3_level2_tag: "Orden",
        card4_badge: "Fácil y Rápido",
        card4_title: "\\"No quiero un sistema complicado de usar.\\"",
        card4_desc: "Nuestros paneles están diseñados para quien tiene prisa: botones grandes, contraste claro entre beneficio y coste, sin menús ocultos ni formaciones eternas.",
        card4_panel_title: "PANEL DEL OPERADOR",
        card4_panel_badge: "1 CLIC",
        card4_btn_profit: "Ver Beneficio Neto",
        card4_btn_whats: "Contactar por Whats",
        card5_badge: "Integración Total",
        card5_title: "\\"Ya pago otra suscripción de CRM.\\"",
        card5_desc: "Podemos conectar nuestras Landing Pages de alta conversión directamente a su software actual, o reemplazar herramientas caras por una solución definitiva.",
        card5_landing: "Landing Page",
        card5_target: "Su CRM Actual",
        card6_badge: "Retorno Rápido",
        card6_title: "\\"Esto parece caro.\\"",
        card6_desc: "Caro es invertir 1.500 € en anuncios cada mes y perder clientes por tardar en responder. Una estructura profesional se amortiza con el primer lote de ventas cerradas.",
        card6_loss_label: "Pérdida sin sistema:",
        card6_loss_val: "-4.500 €/mes",
        card6_gain_label: "Con el ecosistema:",
        card6_gain_val: "+15.000 € en ventas",
        services_tag: "SERVICIOS DE INGENIERÍA DIGITAL",
        services_title: "Lo que Desarrollamos para su Empresa",
        services_desc: "Soluciones diseñadas para resolver el embudo de ventas y aportar previsibilidad.",
        service1_title: "Landing Pages Estratégicas",
        service1_desc: "Páginas ultra rápidas diseñadas para derribar objeciones de su sector, con simuladores de presupuesto y botón directo a WhatsApp.",
        service2_title: "CRMs Adaptables (Servicios y Ventas)",
        service2_desc: "Paneles Kanban a medida: modelo para Servicios (con cálculo fraccionado de consumibles g/kg/ud) y modelo para Ventas (con coste de ventas y margen neto).",
        service3_title: "Automatización de WhatsApp e IA",
        service3_desc: "Cualificación instantánea de leads, recordatorios automáticos para evitar ausencias y alertas al equipo de ventas en tiempo real.",
        footer_badge: "Atención Inmediata",
        footer_title: "¿Listo para construir su sistema de ventas?",
        footer_desc: "Hable directamente con nosotros por el WhatsApp oficial y descubra qué modelo es ideal para su empresa.",
        footer_btn: "Iniciar Proyecto por WhatsApp",
        footer_location: "São Paulo / Brasil",
        niche_model_featured: "SISTEMA DESTACADO (MODELO)",
        niche_available: "Disponible",
        niche_found: "Sistema Encontrado para:",
        niche_custom_title: "Podemos construir la solución perfecta para",
        niche_custom_desc: "Nuestra ingeniería adapta landing pages de alta velocidad e CRMs de servicios/ventas para cualquier sector en pocos días.",
        niche_custom_btn: "Solicitar Sistema para"
      }}
    }};

    let currentLang = 'pt';

    function setLanguage(lang) {{
      if (!translations[lang]) return;
      currentLang = lang;
      try {{
        localStorage.setItem('nexus_lang', lang);
      }} catch (e) {{}}

      // Atualiza todos os elementos marcados com data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {{
          el.innerHTML = translations[lang][key];
        }}
      }});

      // Atualiza input placeholder do omnibar
      const omniInput = document.getElementById('niche-omnibar-input');
      if (omniInput && translations[lang]['omnibar_placeholder']) {{
        omniInput.placeholder = translations[lang]['omnibar_placeholder'];
      }}

      // Atualiza estilos dos botões de idioma no Header
      const langs = ['es', 'pt', 'en'];
      langs.forEach(l => {{
        const btn = document.getElementById('lang-btn-' + l);
        const mBtn = document.getElementById('mobile-lang-' + l);
        if (l === lang) {{
          if (btn) btn.className = 'px-1.5 py-0.5 rounded transition-all text-slate-950 font-extrabold bg-white shadow-sm';
          if (mBtn) mBtn.className = 'px-1.5 py-0.5 rounded transition-all text-slate-950 font-extrabold bg-white shadow-sm';
        }} else {{
          if (btn) btn.className = 'px-1.5 py-0.5 rounded transition-all text-slate-500 hover:text-slate-900';
          if (mBtn) mBtn.className = 'px-1.5 py-0.5 rounded transition-all text-slate-500 hover:text-slate-900';
        }}
      }});

      // Re-renderiza o card ativo do omnibar para aplicar o idioma
      const inputVal = omniInput ? omniInput.value.trim() : '';
      if (inputVal.length >= 2) {{
        handleNicheSearch(inputVal);
      }} else {{
        renderDefaultNicheCard();
      }}
    }}

    // -------------------------------------------------------------------------
    // 2. Animação de Entrada: Desborramento e Skip
    // -------------------------------------------------------------------------
    function skipIntroAnimation() {{
      const overlay = document.getElementById('intro-cinematic-overlay');
      if (overlay) {{
        overlay.style.transition = 'opacity 0.4s ease, backdrop-filter 0.4s ease';
        overlay.style.opacity = '0';
        overlay.style.backdropFilter = 'blur(0px)';
        overlay.style.webkitBackdropFilter = 'blur(0px)';
        setTimeout(() => {{
          overlay.remove();
        }}, 400);
      }}
    }}

    // Tecla ou clique fecha instantaneamente a animação
    window.addEventListener('keydown', skipIntroAnimation, {{ once: true }});

    // Remove do DOM após 2.4s para liberar 100% de memória e eventos
    setTimeout(() => {{
      const overlay = document.getElementById('intro-cinematic-overlay');
      if (overlay && overlay.parentNode) {{
        overlay.remove();
      }}
    }}, 2400);

    // -------------------------------------------------------------------------
    // 3. Base de Dados de Nichos & Lógica de Busca no Omnibar
    // -------------------------------------------------------------------------
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

      const t = translations[currentLang] || translations.pt;
      const solar = nicheDatabase.find(n => n.id === 'energia-solar') || nicheDatabase[0];
      if (!solar) return;

      resultArea.innerHTML = `
        <div class="rounded-3xl bg-slate-50 border-2 border-slate-900 p-6 sm:p-8 space-y-6 shadow-md transition-all">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-slate-800 uppercase">${{t.niche_model_featured}}</span>
            <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200">
              ${{t.niche_available}}
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
                  <span>${{t.card_view_btn}}</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
                ${{solar.has_crm ? `<a href="${{solar.admin_url}}" target="_blank" class="px-4 py-2.5 rounded-xl bg-white hover:bg-slate-100 text-slate-900 border border-slate-300 font-bold text-xs flex items-center gap-2 transition-all"><i class="fa-solid fa-lock text-emerald-600"></i> ${{t.card_crm_btn}}</a>` : ''}}
                <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostei%20do%20sistema%20para%20${{encodeURIComponent(solar.title)}}%20e%20quero%20um%20diagn%C3%B3stico." target="_blank" class="p-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition-all" title="WhatsApp">
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

      const t = translations[currentLang] || translations.pt;
      const cardsHtml = items.map(item => `
        <div class="rounded-3xl bg-slate-50 border-2 border-slate-900 p-6 sm:p-8 space-y-6 shadow-md transition-all">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-slate-900 uppercase">${{t.niche_found}} "${{query}}"</span>
            <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200">
              ${{t.niche_available}}
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
                ${{item.tags.slice(0, 3).map(tag => `<span class="px-2.5 py-1 rounded-lg text-xs font-mono bg-white border border-slate-200 text-slate-700 font-semibold">${{tag}}</span>`).join('')}}
              </div>
              <div class="flex flex-wrap items-center gap-3 pt-3">
                <a href="${{item.url}}" target="_blank" class="px-5 py-2.5 rounded-xl bg-slate-950 hover:bg-slate-800 text-white font-bold text-xs flex items-center gap-2 transition-all">
                  <span>${{t.card_view_btn}}</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
                ${{item.has_crm ? `<a href="${{item.admin_url}}" target="_blank" class="px-4 py-2.5 rounded-xl bg-white hover:bg-slate-100 text-slate-900 border border-slate-300 font-bold text-xs flex items-center gap-2 transition-all"><i class="fa-solid fa-lock text-emerald-600"></i> ${{t.card_crm_btn}}</a>` : ''}}
                <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostei%20do%20sistema%20para%20${{encodeURIComponent(item.title)}}%20e%20quero%20um%20diagn%C3%B3stico." target="_blank" class="p-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition-all" title="WhatsApp">
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

      const t = translations[currentLang] || translations.pt;
      resultArea.innerHTML = `
        <div class="rounded-3xl bg-slate-100 border-2 border-dashed border-slate-300 p-8 text-center space-y-4">
          <div class="w-12 h-12 rounded-2xl bg-slate-950 text-white flex items-center justify-center text-lg mx-auto">
            <i class="fa-solid fa-wand-magic-sparkles text-emerald-400"></i>
          </div>
          <h3 class="text-xl font-bold text-slate-900">${{t.niche_custom_title}} "${{query}}"!</h3>
          <p class="text-xs sm:text-sm text-slate-600 max-w-md mx-auto leading-relaxed">
            ${{t.niche_custom_desc}}
          </p>
          <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Meu%20nicho%20%C3%A9%20${{encodeURIComponent(query)}}%20e%20gostaria%20de%20um%20or%C3%A7amento%20sob%20medida." target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-slate-950 hover:bg-slate-800 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-md">
            <i class="fa-brands fa-whatsapp text-emerald-400"></i> ${{t.niche_custom_btn}} ${{query}}
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

      const t = translations[currentLang] || translations.pt;
      if (container.classList.contains('hidden')) {{
        container.classList.remove('hidden');
        if (text) text.textContent = t.catalog_btn_close;
        if (icon) icon.className = 'fa-solid fa-chevron-up text-xs transition-transform';
      }} else {{
        container.classList.add('hidden');
        if (text) text.textContent = t.catalog_btn_open;
        if (icon) icon.className = 'fa-solid fa-chevron-down text-xs transition-transform';
      }}
    }}

    // Obsidian/Refero GSAP ScrollTrigger Motion Initialization
    function initScrollAnimations() {{
      if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {{
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray('.gsap-reveal').forEach((elem) => {{
          gsap.fromTo(elem, 
            {{ opacity: 0, y: 30 }}, 
            {{ 
              opacity: 1, 
              y: 0, 
              duration: 0.8, 
              ease: "power2.out", 
              scrollTrigger: {{
                trigger: elem,
                start: "top 85%",
                toggleActions: "play none none none"
              }}
            }}
          );
        }});
      }}
    }}

    // Init on load
    document.addEventListener('DOMContentLoaded', () => {{
      try {{
        const savedLang = localStorage.getItem('nexus_lang');
        if (savedLang && translations[savedLang]) {{
          setLanguage(savedLang);
        }} else {{
          renderDefaultNicheCard();
        }}
      }} catch (e) {{
        renderDefaultNicheCard();
      }}
      initScrollAnimations();
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
    print("Portal regenerated successfully with Obsidian standards & 35 systems, length:", len(content))
