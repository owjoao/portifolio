# -*- coding: utf-8 -*-
import os

html_content = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nexus CRM Vendas - Gestão Comercial, Catálogo de Produtos & Lucro por Item</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Plus Jakarta Sans', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.6); }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(51, 65, 85, 0.8); border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(16, 185, 129, 0.6); }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-emerald-500 selection:text-black">

  <!-- TOP HEADER & TYPE SWITCHER BANNER -->
  <header class="bg-slate-900/90 border-b border-slate-800 sticky top-0 z-40 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        
        <!-- Left: Logo & Company Name (Editable) -->
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-cyan-500 flex items-center justify-center text-slate-950 font-black shadow-lg shadow-emerald-500/20">
            <i class="fa-solid fa-cart-shopping text-lg"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h1 id="header-company-name" class="font-extrabold text-base sm:text-lg text-white tracking-tight cursor-pointer hover:text-emerald-400 transition" onclick="openConfigModal()" title="Clique para editar o nome da sua empresa">
                Minha Loja & Distribuição Comercial
              </h1>
              <button onclick="openConfigModal()" class="text-xs text-slate-400 hover:text-emerald-400 p-1 rounded" title="Editar Nome e Configurações">
                <i class="fa-solid fa-pen-to-square"></i>
              </button>
            </div>
            <div class="flex items-center gap-2">
              <span class="inline-flex items-center gap-1 text-[11px] font-semibold text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded-full border border-emerald-800/60">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                CRM de Vendas, Produtos & Margens
              </span>
              <span class="text-[11px] text-slate-400 hidden sm:inline">• Custo unitário por item & CMV</span>
            </div>
          </div>
        </div>

        <!-- Center/Right Switcher to CRM Serviços & Action Buttons -->
        <div class="flex items-center gap-2 sm:gap-3">
          
          <!-- Direct Switcher to CRM Serviços -->
          <a href="../crm-servicos/index.html" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-slate-700 hover:border-cyan-500/50 transition">
            <i class="fa-solid fa-hand-holding-medical text-cyan-400"></i>
            <span class="hidden md:inline">Alternar para</span> <strong>CRM Serviços</strong>
            <i class="fa-solid fa-arrow-right text-[10px] text-slate-400"></i>
          </a>

          <!-- Reset / Demo Data Dropdown / Settings -->
          <button onclick="openConfigModal()" class="p-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700 border border-slate-700 transition" title="Configurações & Backup">
            <i class="fa-solid fa-sliders text-sm"></i>
          </button>

          <!-- Return to Portfolio -->
          <a href="../index.html" class="p-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700 border border-slate-700 transition" title="Voltar ao Portfólio Principal">
            <i class="fa-solid fa-house text-sm"></i>
          </a>

          <!-- Primary CTA: Nova Venda -->
          <button onclick="openNovaVendaModal()" class="inline-flex items-center gap-2 px-3 sm:px-4 py-2 rounded-lg bg-gradient-to-r from-emerald-500 to-cyan-500 hover:from-emerald-400 hover:to-cyan-400 text-slate-950 font-bold text-xs sm:text-sm shadow-lg shadow-emerald-500/25 transition">
            <i class="fa-solid fa-plus"></i>
            <span>Nova Venda</span>
          </button>
        </div>

      </div>

      <!-- MAIN NAVIGATION TABS -->
      <nav class="flex items-center gap-1 sm:gap-2 overflow-x-auto py-2.5 border-t border-slate-800/80 custom-scrollbar text-xs sm:text-sm font-semibold">
        <button onclick="switchTab('pipeline')" id="tab-btn-pipeline" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-emerald-400 bg-emerald-950/60 border border-emerald-800/50">
          <i class="fa-solid fa-filter-circle-dollar"></i>
          <span>Funil & Pipeline de Vendas</span>
          <span id="badge-total-vendas" class="px-1.5 py-0.2 bg-emerald-900/80 text-[10px] rounded-full text-emerald-200">0</span>
        </button>

        <button onclick="switchTab('historico')" id="tab-btn-historico" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-receipt"></i>
          <span>Histórico de Movimentações & Vendas</span>
        </button>

        <button onclick="switchTab('margens')" id="tab-btn-margens" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-chart-line"></i>
          <span>Análise de Margens & Performance</span>
          <span class="px-1.5 py-0.2 bg-cyan-950 text-cyan-400 border border-cyan-800/40 text-[10px] rounded font-mono">Melhor Margem</span>
        </button>

        <button onclick="switchTab('produtos')" id="tab-btn-produtos" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-boxes-packing"></i>
          <span>Catálogo de Produtos & Estoque</span>
        </button>

        <button onclick="switchTab('clientes')" id="tab-btn-clientes" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-users"></i>
          <span>Clientes & Compradores</span>
        </button>
      </nav>
    </div>
  </header>

  <!-- FILTER & ADAPTABLE DATE BAR -->
  <section class="bg-slate-900/60 border-b border-slate-800/80 px-4 sm:px-6 lg:px-8 py-3">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-3">
      
      <!-- Date quick filters -->
      <div class="flex items-center gap-1.5 flex-wrap text-xs">
        <span class="text-slate-400 font-semibold mr-1 flex items-center gap-1">
          <i class="fa-regular fa-calendar"></i> Período:
        </span>
        <button onclick="setDateFilter('tudo')" id="df-tudo" class="df-btn px-2.5 py-1 rounded bg-emerald-950 text-emerald-300 border border-emerald-800/80 font-medium">Todo Período</button>
        <button onclick="setDateFilter('hoje')" id="df-hoje" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Hoje</button>
        <button onclick="setDateFilter('7d')" id="df-7d" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Últimos 7 dias</button>
        <button onclick="setDateFilter('30d')" id="df-30d" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Últimos 30 dias</button>
        <button onclick="setDateFilter('mes')" id="df-mes" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Este Mês</button>
      </div>

      <!-- Custom Date Range Picker -->
      <div class="flex items-center gap-2 text-xs flex-wrap">
        <span class="text-slate-400">De:</span>
        <input type="date" id="filter-date-start" onchange="applyCustomDateFilter()" class="bg-slate-950 border border-slate-700 rounded px-2 py-1 text-slate-200 text-xs focus:border-emerald-500 outline-none">
        <span class="text-slate-400">Até:</span>
        <input type="date" id="filter-date-end" onchange="applyCustomDateFilter()" class="bg-slate-950 border border-slate-700 rounded px-2 py-1 text-slate-200 text-xs focus:border-emerald-500 outline-none">
        <button onclick="clearDateFilter()" class="text-slate-400 hover:text-rose-400 p-1 text-xs" title="Limpar filtro de data">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

    </div>
  </section>

  <!-- METRIC KPI CARDS (Dinamically recalculated based on date filter) -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 w-full">
    <div class="grid grid-cols-2 lg:grid-cols-5 gap-3 sm:gap-4">
      
      <!-- Faturamento de Vendas -->
      <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Faturamento Total</span>
          <div class="w-7 h-7 rounded-lg bg-emerald-950/80 text-emerald-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-cash-register"></i>
          </div>
        </div>
        <div id="kpi-faturamento" class="text-lg sm:text-2xl font-black text-white font-mono tracking-tight">R$ 0,00</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span>Receita bruta de vendas</span>
        </div>
      </div>

      <!-- Custo de Mercadorias (CMV) -->
      <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-amber-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Custo dos Itens (CMV)</span>
          <div class="w-7 h-7 rounded-lg bg-amber-950/80 text-amber-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-tag"></i>
          </div>
        </div>
        <div id="kpi-custos" class="text-lg sm:text-2xl font-black text-amber-400 font-mono tracking-tight">R$ 0,00</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span>Custo de aquisição unitário</span>
        </div>
      </div>

      <!-- Lucro Líquido -->
      <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Lucro Líquido</span>
          <div class="w-7 h-7 rounded-lg bg-emerald-950/80 text-emerald-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-chart-line"></i>
          </div>
        </div>
        <div id="kpi-lucro" class="text-lg sm:text-2xl font-black text-emerald-400 font-mono tracking-tight">R$ 0,00</div>
        <div class="text-[11px] text-emerald-400/90 mt-1 flex items-center gap-1">
          <i class="fa-solid fa-circle-check text-[9px]"></i>
          <span>Faturamento - Custos</span>
        </div>
      </div>

      <!-- Margem Média -->
      <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-cyan-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Margem Média</span>
          <div class="w-7 h-7 rounded-lg bg-cyan-950/80 text-cyan-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-percent"></i>
          </div>
        </div>
        <div id="kpi-margem" class="text-lg sm:text-2xl font-black text-cyan-300 font-mono tracking-tight">0.0%</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span>Rentabilidade comercial</span>
        </div>
      </div>

      <!-- Itens Vendidos & Ticket Médio -->
      <div class="col-span-2 lg:col-span-1 bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-purple-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Itens Vendidos</span>
          <div class="w-7 h-7 rounded-lg bg-purple-950/80 text-purple-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-box-open"></i>
          </div>
        </div>
        <div id="kpi-itens-vendidos" class="text-lg sm:text-2xl font-black text-purple-300 font-mono tracking-tight">0</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span>Ticket Médio: <strong id="kpi-ticket" class="text-slate-200">R$ 0,00</strong></span>
        </div>
      </div>

    </div>
  </section>

  <!-- TAB CONTENT CONTAINERS -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16 flex-1 w-full">

    <!-- ==================== TAB 1: PIPELINE / FUNIL KANBAN ==================== -->
    <div id="tab-content-pipeline" class="tab-pane">
      <div class="flex items-center justify-between mb-4">
        <div>
          <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
            <span>Pipeline & Funil Comercial de Vendas</span>
            <span class="text-xs font-normal text-slate-400">(Acompanhe negociações desde o lead até a entrega)</span>
          </h2>
        </div>
        <div class="flex items-center gap-2">
          <input type="text" id="search-pipeline" oninput="renderPipeline()" placeholder="Buscar cliente ou produto..." class="bg-slate-900 border border-slate-800 rounded-lg px-3 py-1.5 text-xs text-slate-200 placeholder-slate-500 focus:border-emerald-500 outline-none w-44 sm:w-64">
          <button onclick="openNovaVendaModal()" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs rounded-lg transition flex items-center gap-1">
            <i class="fa-solid fa-plus"></i> <span class="hidden sm:inline">Nova Venda</span>
          </button>
        </div>
      </div>

      <!-- KANBAN BOARD COLUMNS (6 Stages) -->
      <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-3 overflow-x-auto pb-4 custom-scrollbar">
        
        <!-- Col 1: Novo Lead -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[220px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
              <span>1. Novo Lead</span>
            </div>
            <span id="col-count-novo" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="pipeline-col-novo" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 2: Qualificação -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[220px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span>
              <span>2. Qualificação</span>
            </div>
            <span id="col-count-qualificacao" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="pipeline-col-qualificacao" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 3: Proposta -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[220px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-cyan-500"></span>
              <span>3. Proposta Enviada</span>
            </div>
            <span id="col-count-proposta" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="pipeline-col-proposta" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 4: Negociação -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[220px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-500 animate-pulse"></span>
              <span>4. Negociação</span>
            </div>
            <span id="col-count-negociacao" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="pipeline-col-negociacao" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 5: Venda Fechada -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[220px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
              <span>5. Venda Fechada</span>
            </div>
            <span id="col-count-fechada" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="pipeline-col-fechada" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 6: Perdida -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[220px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
              <span>6. Perdida</span>
            </div>
            <span id="col-count-perdida" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="pipeline-col-perdida" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

      </div>
    </div>


    <!-- ==================== TAB 2: HISTÓRICO DE VENDAS & MOVIMENTAÇÕES ==================== -->
    <div id="tab-content-historico" class="tab-pane hidden">
      <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-6">
        
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-5">
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <i class="fa-solid fa-receipt text-emerald-400"></i>
              <span>Histórico Completo de Vendas & Lucro por Item</span>
            </h2>
            <p class="text-xs text-slate-400">Auditoria detalhada de cada produto vendido, custo unitário (CMV), receita e margem apurada.</p>
          </div>
          <div class="flex items-center gap-2">
            <input type="text" id="search-historico" oninput="renderHistorico()" placeholder="Filtrar por produto ou cliente..." class="bg-slate-950 border border-slate-800 rounded-lg px-3 py-1.5 text-xs text-slate-200 placeholder-slate-500 focus:border-emerald-500 outline-none w-48">
            <button onclick="exportarHistoricoCSV()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-slate-700 transition flex items-center gap-1.5">
              <i class="fa-solid fa-file-csv text-emerald-400"></i>
              <span>Exportar CSV</span>
            </button>
          </div>
        </div>

        <!-- Table of sales movements -->
        <div class="overflow-x-auto rounded-lg border border-slate-800 custom-scrollbar">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-950 text-slate-400 font-semibold border-b border-slate-800">
              <tr>
                <th class="py-3 px-3">Data / Hora</th>
                <th class="py-3 px-3">Cliente</th>
                <th class="py-3 px-3">Produto(s) Vendido(s)</th>
                <th class="py-3 px-3 text-center">Qtd</th>
                <th class="py-3 px-3 text-right">Preço Venda</th>
                <th class="py-3 px-3 text-right">Custo dos Itens</th>
                <th class="py-3 px-3 text-right">Lucro da Venda</th>
                <th class="py-3 px-3 text-center">Margem (%)</th>
                <th class="py-3 px-3 text-center">Pagamento</th>
                <th class="py-3 px-3 text-center">Status</th>
                <th class="py-3 px-3 text-center">Ações</th>
              </tr>
            </thead>
            <tbody id="historico-tbody" class="divide-y divide-slate-800/70 text-slate-200">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>

        <div id="historico-empty" class="hidden py-12 text-center text-slate-400 text-xs">
          <i class="fa-solid fa-cart-arrow-down text-3xl mb-2 text-slate-600 block"></i>
          Nenhuma movimentação comercial registrada no período selecionado.
        </div>

      </div>
    </div>


    <!-- ==================== TAB 3: ANÁLISE DE MARGENS & PERFORMANCE ==================== -->
    <div id="tab-content-margens" class="tab-pane hidden">
      <div class="space-y-6">
        
        <!-- Header summary for Margins -->
        <div class="bg-gradient-to-r from-slate-900 to-emerald-950/40 border border-slate-800 rounded-xl p-5">
          <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950 px-2 py-0.5 rounded border border-emerald-800/60">
                Inteligência Comercial de Vendas
              </span>
              <h2 class="text-lg sm:text-xl font-extrabold text-white mt-1">Ranking de Rentabilidade por Produto</h2>
              <p class="text-xs text-slate-400 mt-0.5">Identifique quais produtos deixam a maior margem percentual e quais mais colocam lucro em reais no seu bolso.</p>
            </div>
            
            <div class="flex items-center gap-2 text-xs">
              <span class="text-slate-400">Ordenar por:</span>
              <select id="sort-margens" onchange="renderMargens()" class="bg-slate-950 border border-slate-700 text-slate-200 rounded px-2.5 py-1.5 outline-none focus:border-emerald-500 font-medium">
                <option value="melhor_margem">🏆 Melhor Margem (%)</option>
                <option value="maior_lucro">💰 Maior Lucro em R$</option>
                <option value="mais_vendidos">🔥 Mais Vendidos (Giro)</option>
                <option value="maior_faturamento">📈 Maior Faturamento</option>
                <option value="maior_cmv">⚠️ Maior Custo de Compra</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Margin Cards Grid & Visual Comparisons -->
        <div id="margens-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Rendered via JS -->
        </div>

      </div>
    </div>


    <!-- ==================== TAB 4: CATÁLOGO DE PRODUTOS & ESTOQUE ==================== -->
    <div id="tab-content-produtos" class="tab-pane hidden">
      <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-6">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-5">
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <i class="fa-solid fa-boxes-packing text-emerald-400"></i>
              <span>Catálogo de Produtos & Controle de Estoque</span>
            </h2>
            <p class="text-xs text-slate-400">Cadastre seus produtos com custo de compra (CMV) e preço de venda para cálculo automático de margem unitária.</p>
          </div>
          <button onclick="openNovoProdutoModal()" class="px-3.5 py-2 bg-gradient-to-r from-emerald-500 to-cyan-500 text-slate-950 font-bold text-xs rounded-lg transition flex items-center gap-1.5 shadow-md shadow-emerald-500/20">
            <i class="fa-solid fa-plus"></i> <span>Adicionar Novo Produto</span>
          </button>
        </div>

        <!-- Products table -->
        <div class="overflow-x-auto rounded-lg border border-slate-800 custom-scrollbar">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-950 text-slate-400 font-semibold border-b border-slate-800">
              <tr>
                <th class="py-3 px-3">Código / SKU</th>
                <th class="py-3 px-3">Nome do Produto</th>
                <th class="py-3 px-3">Categoria</th>
                <th class="py-3 px-3 text-right">Custo de Compra</th>
                <th class="py-3 px-3 text-right">Preço de Venda</th>
                <th class="py-3 px-3 text-right">Lucro Unitário</th>
                <th class="py-3 px-3 text-center">Margem Unitária</th>
                <th class="py-3 px-3 text-center">Estoque Atual</th>
                <th class="py-3 px-3 text-center">Ações</th>
              </tr>
            </thead>
            <tbody id="produtos-tbody" class="divide-y divide-slate-800/70 text-slate-200">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>


    <!-- ==================== TAB 5: CLIENTES ==================== -->
    <div id="tab-content-clientes" class="tab-pane hidden">
      <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-6">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-5">
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <i class="fa-solid fa-users text-emerald-400"></i>
              <span>Clientes & Compradores</span>
            </h2>
            <p class="text-xs text-slate-400">Histórico de compras realizadas, LTV (total investido) e canal direto de WhatsApp.</p>
          </div>
          <button onclick="openNovoClienteModal()" class="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs rounded-lg transition flex items-center gap-1.5 shadow-md shadow-emerald-500/20">
            <i class="fa-solid fa-plus"></i> <span>Novo Cliente</span>
          </button>
        </div>

        <div id="clientes-list" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Rendered via JS -->
        </div>
      </div>
    </div>

  </main>

  <!-- ==================== MODALS ==================== -->

  <!-- MODAL: NOVA / EDITAR VENDA -->
  <div id="modal-venda" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 id="modal-venda-title" class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-cart-plus text-emerald-400"></i>
          <span>Registrar Venda / Proposta</span>
        </h3>
        <button onclick="closeModal('modal-venda')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-4 custom-scrollbar flex-1 text-xs">
        <input type="hidden" id="venda-id">

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Cliente *</label>
            <div class="flex gap-2">
              <select id="venda-cliente" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500"></select>
              <button type="button" onclick="openNovoClienteModal(true)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700 rounded-lg" title="Cadastrar cliente rápido">
                <i class="fa-solid fa-user-plus"></i>
              </button>
            </div>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Data e Hora *</label>
            <input type="datetime-local" id="venda-data" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="sm:col-span-2">
            <label class="block text-slate-300 font-semibold mb-1">Produto *</label>
            <select id="venda-produto" onchange="onProdutoSelecionadoNaVenda()" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500"></select>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Quantidade *</label>
            <input type="number" min="1" id="venda-qtd" oninput="recalcularValoresVenda()" value="1" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white font-mono font-bold w-full outline-none focus:border-emerald-500 text-center">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Etapa no Pipeline</label>
            <select id="venda-etapa" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
              <option value="novo">1. Novo Lead</option>
              <option value="qualificacao">2. Qualificação / Interesse</option>
              <option value="proposta">3. Proposta Enviada</option>
              <option value="negociacao">4. Negociação & Pagamento</option>
              <option value="fechada" selected>5. Venda Fechada & Entregue</option>
              <option value="perdida">6. Perdida</option>
            </select>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Forma de Pagamento</label>
            <select id="venda-pagamento" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
              <option value="PIX">PIX à vista</option>
              <option value="Cartão de Crédito">Cartão de Crédito</option>
              <option value="Boleto Bancário">Boleto Bancário</option>
              <option value="Financiamento">Financiamento</option>
              <option value="Dinheiro">Dinheiro</option>
            </select>
          </div>
        </div>

        <!-- Composição Financeira da Venda -->
        <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 space-y-3">
          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-200 flex items-center gap-1.5">
              <i class="fa-solid fa-calculator text-emerald-400"></i> Composição Financeira da Venda
            </span>
            <span id="venda-resumo-margem" class="font-mono text-emerald-400 font-bold">Margem: 0%</span>
          </div>

          <div class="grid grid-cols-3 gap-3">
            <div>
              <label class="block text-slate-400 mb-1">Valor Total Venda (R$)</label>
              <input type="number" step="0.01" id="venda-total" oninput="recalcularValoresVenda(true)" class="bg-slate-900 border border-slate-700 rounded-lg p-2 text-white font-mono font-bold w-full outline-none focus:border-emerald-500">
            </div>
            <div>
              <label class="block text-slate-400 mb-1">Custo Total Itens (R$)</label>
              <input type="number" step="0.01" id="venda-custo-total" readonly class="bg-slate-900/50 border border-slate-800 rounded-lg p-2 text-amber-400 font-mono font-bold w-full cursor-not-allowed">
            </div>
            <div>
              <label class="block text-slate-400 mb-1">Lucro Líquido (R$)</label>
              <input type="number" step="0.01" id="venda-lucro" readonly class="bg-slate-900/50 border border-slate-800 rounded-lg p-2 text-emerald-400 font-mono font-bold w-full cursor-not-allowed">
            </div>
          </div>
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Observações da Venda / Dados de Entrega</label>
          <textarea id="venda-obs" rows="2" placeholder="Ex: Cliente solicitou entrega para sexta-feira, negociado desconto de 5% à vista no PIX..." class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500"></textarea>
        </div>

      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-venda')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarVenda()" class="px-5 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs shadow-lg shadow-emerald-500/20 transition">Salvar Venda</button>
      </div>
    </div>
  </div>


  <!-- MODAL: NOVO / EDITAR PRODUTO -->
  <div id="modal-produto" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-md max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 id="modal-produto-title" class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-box text-emerald-400"></i>
          <span>Novo Produto</span>
        </h3>
        <button onclick="closeModal('modal-produto')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-3.5 custom-scrollbar flex-1 text-xs">
        <input type="hidden" id="prod-id">

        <div class="grid grid-cols-3 gap-2">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">SKU / Código</label>
            <input type="text" id="prod-sku" placeholder="PROD-01" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white w-full outline-none focus:border-emerald-500 uppercase font-mono">
          </div>
          <div class="col-span-2">
            <label class="block text-slate-300 font-semibold mb-1">Nome do Produto *</label>
            <input type="text" id="prod-nome" placeholder="Ex: Inversor Solar 5kW, Kit Peças..." class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white w-full outline-none focus:border-emerald-500 font-bold">
          </div>
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Categoria</label>
          <input type="text" id="prod-categoria" placeholder="Ex: Equipamentos, Acessórios, Autopeças..." class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Custo de Compra (R$) *</label>
            <input type="number" step="0.01" id="prod-custo" oninput="recalcularMargemProdutoModal()" placeholder="0,00" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-amber-400 font-mono font-bold w-full outline-none focus:border-emerald-500">
            <span class="text-[10px] text-slate-400">Quanto você paga pelo item</span>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Preço de Venda (R$) *</label>
            <input type="number" step="0.01" id="prod-preco" oninput="recalcularMargemProdutoModal()" placeholder="0,00" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-emerald-400 font-mono font-bold w-full outline-none focus:border-emerald-500">
            <span class="text-[10px] text-slate-400">Preço cobrado do cliente</span>
          </div>
        </div>

        <!-- Profit & Margin Preview -->
        <div class="p-3 bg-emerald-950/40 rounded-xl border border-emerald-800/60 font-mono space-y-1">
          <div class="flex items-center justify-between text-xs">
            <span class="text-slate-300">Lucro Unitário:</span>
            <strong id="prod-preview-lucro" class="text-emerald-400 text-sm">R$ 0,00</strong>
          </div>
          <div class="flex items-center justify-between text-xs">
            <span class="text-slate-300">Margem Comercial:</span>
            <strong id="prod-preview-margem" class="text-cyan-300 text-sm">0.0%</strong>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Estoque Atual</label>
            <input type="number" id="prod-estoque" value="10" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white w-full outline-none focus:border-emerald-500 font-mono">
          </div>
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Estoque Mínimo</label>
            <input type="number" id="prod-estoque-min" value="2" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white w-full outline-none focus:border-emerald-500 font-mono">
          </div>
        </div>

      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-produto')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarProduto()" class="px-5 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs shadow-lg shadow-emerald-500/20 transition">Salvar Produto</button>
      </div>
    </div>
  </div>


  <!-- MODAL: NOVO / EDITAR CLIENTE -->
  <div id="modal-cliente" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-md max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 id="modal-cliente-title" class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-user-plus text-emerald-400"></i>
          <span>Novo Cliente Comprador</span>
        </h3>
        <button onclick="closeModal('modal-cliente')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-3 custom-scrollbar flex-1 text-xs">
        <input type="hidden" id="cli-id">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Nome Completo / Razão Social *</label>
          <input type="text" id="cli-nome" placeholder="Ex: Gabriel Rezende" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white w-full outline-none focus:border-emerald-500">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">WhatsApp / Telefone *</label>
          <input type="text" id="cli-telefone" placeholder="(32) 99929-2311" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">E-mail</label>
          <input type="email" id="cli-email" placeholder="cliente@empresa.com" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Cidade / Estado</label>
          <input type="text" id="cli-cidade" placeholder="Ex: São Paulo - SP" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
        </div>
      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-cliente')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarCliente()" class="px-5 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs shadow-lg shadow-emerald-500/20 transition">Salvar Cliente</button>
      </div>
    </div>
  </div>


  <!-- MODAL: CONFIGURAÇÕES & BACKUP -->
  <div id="modal-config" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-sliders text-emerald-400"></i>
          <span>Configurações Comerciais & Backup</span>
        </h3>
        <button onclick="closeModal('modal-config')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-4 custom-scrollbar flex-1 text-xs">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Nome da Empresa / Loja *</label>
          <input type="text" id="cfg-nome-empresa" class="bg-slate-950 border border-slate-700 rounded-lg p-2.5 text-white w-full outline-none focus:border-emerald-500 font-bold">
          <span class="text-[10px] text-slate-400">Altere para a identidade comercial da sua loja ou distribuidora.</span>
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">WhatsApp Padrão para Atendimento</label>
          <input type="text" id="cfg-whatsapp" value="32999292311" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-emerald-500">
        </div>

        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
          <span class="font-bold text-slate-300 block">Backup & Migração dos Dados</span>
          <p class="text-[11px] text-slate-400">Seus dados ficam 100% salvos no seu navegador. Exporte para JSON e importe quando desejar.</p>
          <div class="flex items-center gap-2 pt-1">
            <button onclick="exportarBackupJSON()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg font-semibold flex items-center gap-1.5">
              <i class="fa-solid fa-download text-emerald-400"></i> Exportar Dados (JSON)
            </button>
            <label class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg font-semibold flex items-center gap-1.5 cursor-pointer">
              <i class="fa-solid fa-upload text-cyan-400"></i> Importar Dados (JSON)
              <input type="file" id="cfg-import-file" onchange="importarBackupJSON(event)" accept=".json" class="hidden">
            </label>
          </div>
        </div>

        <div class="p-3 bg-rose-950/30 rounded-xl border border-rose-900/40 space-y-2">
          <span class="font-bold text-rose-300 block">Área de Redefinição</span>
          <div class="flex items-center gap-2">
            <button onclick="resetarDadosExemplo()" class="px-3 py-1.5 bg-amber-900/60 hover:bg-amber-800 text-amber-200 border border-amber-700/60 rounded-lg font-semibold">
              <i class="fa-solid fa-rotate-left"></i> Carregar Dados de Exemplo
            </button>
            <button onclick="limparTodosDados()" class="px-3 py-1.5 bg-rose-900/60 hover:bg-rose-800 text-rose-200 border border-rose-700/60 rounded-lg font-semibold">
              <i class="fa-solid fa-trash-can"></i> Limpar Tudo do Zero
            </button>
          </div>
        </div>
      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-config')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarConfiguracoes()" class="px-5 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs shadow-lg shadow-emerald-500/20 transition">Salvar Configurações</button>
      </div>
    </div>
  </div>

  <!-- SCRIPT LOGIC -->
  <script src="crm_vendas.js"></script>
</body>
</html>
"""

with open("crm-vendas/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("crm-vendas/index.html generated successfully.")
