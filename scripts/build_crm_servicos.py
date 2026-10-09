# -*- coding: utf-8 -*-
import os

content = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nexus CRM Serviços - Gestão de Atendimentos, Fichas Técnicas & Margem de Lucro</title>
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
          },
          colors: {
            brand: {
              50: '#ecfeff',
              100: '#cffafe',
              400: '#22d3ee',
              500: '#06b6d4',
              600: '#0891b2',
              700: '#0e7490',
            }
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
    .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(6, 182, 212, 0.6); }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-cyan-500 selection:text-black">

  <!-- TOP NOTIFICATION & TYPE SWITCHER BANNER -->
  <header class="bg-slate-900/90 border-b border-slate-800 sticky top-0 z-40 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        
        <!-- Left: Logo & Company Name (Editable) -->
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 to-emerald-500 flex items-center justify-center text-slate-950 font-black shadow-lg shadow-cyan-500/20">
            <i class="fa-solid fa-hand-holding-medical text-lg"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h1 id="header-company-name" class="font-extrabold text-base sm:text-lg text-white tracking-tight cursor-pointer hover:text-cyan-400 transition" onclick="openConfigModal()" title="Clique para editar o nome da sua empresa">
                Minha Empresa de Serviços
              </h1>
              <button onclick="openConfigModal()" class="text-xs text-slate-400 hover:text-cyan-400 p-1 rounded" title="Editar Nome e Configurações">
                <i class="fa-solid fa-pen-to-square"></i>
              </button>
            </div>
            <div class="flex items-center gap-2">
              <span class="inline-flex items-center gap-1 text-[11px] font-semibold text-cyan-400 bg-cyan-950/80 px-2 py-0.5 rounded-full border border-cyan-800/60">
                <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
                CRM de Serviços & Ficha de Insumos
              </span>
              <span class="text-[11px] text-slate-400 hidden sm:inline">• Custos por fração (g/kg/mg/L/un)</span>
            </div>
          </div>
        </div>

        <!-- Center/Right Switcher to CRM Vendas & Action Buttons -->
        <div class="flex items-center gap-2 sm:gap-3">
          
          <!-- Direct Switcher to CRM Vendas -->
          <a href="../crm-vendas/index.html" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-slate-700 hover:border-cyan-500/50 transition">
            <i class="fa-solid fa-cart-shopping text-emerald-400"></i>
            <span class="hidden md:inline">Alternar para</span> <strong>CRM Vendas</strong>
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

          <!-- Primary CTA: Novo Atendimento -->
          <button onclick="openNovoAtendimentoModal()" class="inline-flex items-center gap-2 px-3 sm:px-4 py-2 rounded-lg bg-gradient-to-r from-cyan-500 to-emerald-500 hover:from-cyan-400 hover:to-emerald-400 text-slate-950 font-bold text-xs sm:text-sm shadow-lg shadow-cyan-500/25 transition">
            <i class="fa-solid fa-plus"></i>
            <span>Novo Atendimento</span>
          </button>
        </div>

      </div>

      <!-- MAIN NAVIGATION TABS -->
      <nav class="flex items-center gap-1 sm:gap-2 overflow-x-auto py-2.5 border-t border-slate-800/80 custom-scrollbar text-xs sm:text-sm font-semibold">
        <button onclick="switchTab('funil')" id="tab-btn-funil" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-cyan-400 bg-cyan-950/60 border border-cyan-800/50">
          <i class="fa-solid fa-table-columns"></i>
          <span>Funil & Atendimentos</span>
          <span id="badge-total-atendimentos" class="px-1.5 py-0.2 bg-cyan-900/80 text-[10px] rounded-full text-cyan-200">0</span>
        </button>

        <button onclick="switchTab('historico')" id="tab-btn-historico" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-clock-rotate-left"></i>
          <span>Histórico de Movimentações</span>
        </button>

        <button onclick="switchTab('margens')" id="tab-btn-margens" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-chart-pie"></i>
          <span>Análise de Margens & Performance</span>
          <span class="px-1.5 py-0.2 bg-emerald-950 text-emerald-400 border border-emerald-800/40 text-[10px] rounded font-mono">Melhor Margem</span>
        </button>

        <button onclick="switchTab('servicos')" id="tab-btn-servicos" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-list-check"></i>
          <span>Catálogo de Serviços & Fichas</span>
        </button>

        <button onclick="switchTab('insumos')" id="tab-btn-insumos" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-boxes-stacked"></i>
          <span>Insumos & Estoque (g/kg/mg/L/un)</span>
        </button>

        <button onclick="switchTab('clientes')" id="tab-btn-clientes" class="tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
          <i class="fa-solid fa-users"></i>
          <span>Clientes</span>
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
        <button onclick="setDateFilter('tudo')" id="df-tudo" class="df-btn px-2.5 py-1 rounded bg-cyan-950 text-cyan-300 border border-cyan-800/80 font-medium">Todo Período</button>
        <button onclick="setDateFilter('hoje')" id="df-hoje" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Hoje</button>
        <button onclick="setDateFilter('7d')" id="df-7d" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Últimos 7 dias</button>
        <button onclick="setDateFilter('30d')" id="df-30d" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Últimos 30 dias</button>
        <button onclick="setDateFilter('mes')" id="df-mes" class="df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium">Este Mês</button>
      </div>

      <!-- Custom Date Range Picker -->
      <div class="flex items-center gap-2 text-xs flex-wrap">
        <span class="text-slate-400">De:</span>
        <input type="date" id="filter-date-start" onchange="applyCustomDateFilter()" class="bg-slate-950 border border-slate-700 rounded px-2 py-1 text-slate-200 text-xs focus:border-cyan-500 outline-none">
        <span class="text-slate-400">Até:</span>
        <input type="date" id="filter-date-end" onchange="applyCustomDateFilter()" class="bg-slate-950 border border-slate-700 rounded px-2 py-1 text-slate-200 text-xs focus:border-cyan-500 outline-none">
        <button onclick="clearDateFilter()" class="text-slate-400 hover:text-rose-400 p-1 text-xs" title="Limpar filtro de data">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

    </div>
  </section>

  <!-- METRIC KPI CARDS (Dinamically recalculated based on date filter) -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 w-full">
    <div class="grid grid-cols-2 lg:grid-cols-5 gap-3 sm:gap-4">
      
      <!-- Faturamento -->
      <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-cyan-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Faturamento</span>
          <div class="w-7 h-7 rounded-lg bg-cyan-950/80 text-cyan-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-money-bill-wave"></i>
          </div>
        </div>
        <div id="kpi-faturamento" class="text-lg sm:text-2xl font-black text-white font-mono tracking-tight">R$ 0,00</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span id="kpi-faturamento-desc">Total cobrado no período</span>
        </div>
      </div>

      <!-- Custo de Insumos -->
      <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-amber-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Custo Insumos</span>
          <div class="w-7 h-7 rounded-lg bg-amber-950/80 text-amber-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-flask"></i>
          </div>
        </div>
        <div id="kpi-custos" class="text-lg sm:text-2xl font-black text-amber-400 font-mono tracking-tight">R$ 0,00</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span>Gastos proporcionais</span>
        </div>
      </div>

      <!-- Lucro Líquido -->
      <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Lucro Líquido</span>
          <div class="w-7 h-7 rounded-lg bg-emerald-950/80 text-emerald-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-arrow-trend-up"></i>
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
          <span>Rentabilidade média</span>
        </div>
      </div>

      <!-- Atendimentos Concluídos -->
      <div class="col-span-2 lg:col-span-1 bg-slate-900/80 border border-slate-800/80 rounded-xl p-3.5 sm:p-4 shadow-sm relative overflow-hidden group hover:border-purple-500/40 transition">
        <div class="flex items-center justify-between text-slate-400 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider">Atendimentos</span>
          <div class="w-7 h-7 rounded-lg bg-purple-950/80 text-purple-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-check-double"></i>
          </div>
        </div>
        <div id="kpi-atendimentos" class="text-lg sm:text-2xl font-black text-purple-300 font-mono tracking-tight">0</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span>Ticket Médio: <strong id="kpi-ticket" class="text-slate-200">R$ 0,00</strong></span>
        </div>
      </div>

    </div>
  </section>

  <!-- TAB CONTENT CONTAINERS -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16 flex-1 w-full">

    <!-- ==================== TAB 1: FUNIL KANBAN ==================== -->
    <div id="tab-content-funil" class="tab-pane">
      <div class="flex items-center justify-between mb-4">
        <div>
          <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
            <span>Esteira de Atendimentos & Procedimentos</span>
            <span class="text-xs font-normal text-slate-400">(Arraste ou use as ações para avançar etapas)</span>
          </h2>
        </div>
        <div class="flex items-center gap-2">
          <input type="text" id="search-funil" oninput="renderKanban()" placeholder="Buscar cliente ou serviço..." class="bg-slate-900 border border-slate-800 rounded-lg px-3 py-1.5 text-xs text-slate-200 placeholder-slate-500 focus:border-cyan-500 outline-none w-44 sm:w-64">
          <button onclick="openNovoAtendimentoModal()" class="px-3 py-1.5 bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold text-xs rounded-lg transition flex items-center gap-1">
            <i class="fa-solid fa-plus"></i> <span class="hidden sm:inline">Atendimento</span>
          </button>
        </div>
      </div>

      <!-- KANBAN BOARD COLUMNS -->
      <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-3.5 overflow-x-auto pb-4 custom-scrollbar">
        
        <!-- Col 1: Novo Contato -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[250px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
              <span>1. Novo Contato</span>
            </div>
            <span id="col-count-novo" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="kanban-col-novo" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 2: Agendado / Avaliação -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[250px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-cyan-500"></span>
              <span>2. Agendado / Avaliação</span>
            </div>
            <span id="col-count-agendado" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="kanban-col-agendado" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 3: Em Execução -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[250px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-500 animate-pulse"></span>
              <span>3. Em Execução</span>
            </div>
            <span id="col-count-execucao" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="kanban-col-execucao" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 4: Concluído & Faturado -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[250px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
              <span>4. Concluído & Faturado</span>
            </div>
            <span id="col-count-concluido" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="kanban-col-concluido" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

        <!-- Col 5: Cancelado -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-xl p-3 flex flex-col min-w-[250px]">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-bold text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
              <span>5. Cancelado</span>
            </div>
            <span id="col-count-cancelado" class="px-2 py-0.5 rounded-full bg-slate-800 text-[11px] text-slate-400">0</span>
          </div>
          <div id="kanban-col-cancelado" class="flex-1 space-y-2.5 min-h-[300px]"></div>
        </div>

      </div>
    </div>


    <!-- ==================== TAB 2: HISTÓRICO DE MOVIMENTAÇÕES ==================== -->
    <div id="tab-content-historico" class="tab-pane hidden">
      <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-6">
        
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-5">
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <i class="fa-solid fa-clock-rotate-left text-cyan-400"></i>
              <span>Histórico Completo de Movimentações & Custos</span>
            </h2>
            <p class="text-xs text-slate-400">Auditoria detalhada de cada serviço executado, insumos consumidos e lucro líquido apurado.</p>
          </div>
          <div class="flex items-center gap-2">
            <input type="text" id="search-historico" oninput="renderHistorico()" placeholder="Filtrar histórico..." class="bg-slate-950 border border-slate-800 rounded-lg px-3 py-1.5 text-xs text-slate-200 placeholder-slate-500 focus:border-cyan-500 outline-none w-48">
            <button onclick="exportarHistoricoCSV()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-slate-700 transition flex items-center gap-1.5">
              <i class="fa-solid fa-file-csv text-emerald-400"></i>
              <span>Exportar CSV</span>
            </button>
          </div>
        </div>

        <!-- Table of movements -->
        <div class="overflow-x-auto rounded-lg border border-slate-800 custom-scrollbar">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-950 text-slate-400 font-semibold border-b border-slate-800">
              <tr>
                <th class="py-3 px-3">Data / Hora</th>
                <th class="py-3 px-3">Cliente</th>
                <th class="py-3 px-3">Serviço Realizado</th>
                <th class="py-3 px-3">Insumos Gastos na Operação</th>
                <th class="py-3 px-3 text-right">Valor Cobrado</th>
                <th class="py-3 px-3 text-right">Custo Insumos</th>
                <th class="py-3 px-3 text-right">Lucro Líquido</th>
                <th class="py-3 px-3 text-center">Margem (%)</th>
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
          <i class="fa-solid fa-box-open text-3xl mb-2 text-slate-600 block"></i>
          Nenhuma movimentação registrada no período selecionado.
        </div>

      </div>
    </div>


    <!-- ==================== TAB 3: ANÁLISE DE MARGENS & PERFORMANCE ==================== -->
    <div id="tab-content-margens" class="tab-pane hidden">
      <div class="space-y-6">
        
        <!-- Header summary for Margins -->
        <div class="bg-gradient-to-r from-slate-900 to-cyan-950/40 border border-slate-800 rounded-xl p-5">
          <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-cyan-400 bg-cyan-950 px-2 py-0.5 rounded border border-cyan-800/60">
                Inteligência Financeira de Serviços
              </span>
              <h2 class="text-lg sm:text-xl font-extrabold text-white mt-1">Ranking de Rentabilidade por Procedimento</h2>
              <p class="text-xs text-slate-400 mt-0.5">Descubra quais serviços deixam a maior margem percentual e quais geram mais lucro absoluto em reais no seu bolso.</p>
            </div>
            
            <div class="flex items-center gap-2 text-xs">
              <span class="text-slate-400">Ordenar por:</span>
              <select id="sort-margens" onchange="renderMargens()" class="bg-slate-950 border border-slate-700 text-slate-200 rounded px-2.5 py-1.5 outline-none focus:border-cyan-500 font-medium">
                <option value="melhor_margem">🏆 Melhor Margem (%)</option>
                <option value="maior_lucro">💰 Maior Lucro em R$</option>
                <option value="mais_realizados">🔥 Mais Realizados (Volume)</option>
                <option value="maior_faturamento">📈 Maior Faturamento</option>
                <option value="maior_custo">⚠️ Maior Custo de Insumos</option>
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


    <!-- ==================== TAB 4: CATÁLOGO DE SERVIÇOS & FICHAS TÉCNICAS ==================== -->
    <div id="tab-content-servicos" class="tab-pane hidden">
      <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-6">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-5">
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <i class="fa-solid fa-list-check text-cyan-400"></i>
              <span>Catálogo de Serviços & Fichas de Custo</span>
            </h2>
            <p class="text-xs text-slate-400">Cadastre seus procedimentos e vincule os insumos gastos para o sistema calcular o custo automático de cada operação.</p>
          </div>
          <button onclick="openNovoServicoModal()" class="px-3.5 py-2 bg-gradient-to-r from-cyan-500 to-emerald-500 text-slate-950 font-bold text-xs rounded-lg transition flex items-center gap-1.5 shadow-md shadow-cyan-500/20">
            <i class="fa-solid fa-plus"></i> <span>Adicionar Novo Serviço</span>
          </button>
        </div>

        <div id="servicos-list" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Rendered via JS -->
        </div>
      </div>
    </div>


    <!-- ==================== TAB 5: INSUMOS & ESTOQUE (PROPORCIONALIDADE g/kg/mg/L/un) ==================== -->
    <div id="tab-content-insumos" class="tab-pane hidden">
      <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-6">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-5">
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <i class="fa-solid fa-boxes-stacked text-cyan-400"></i>
              <span>Insumos, Materiais & Padronização de Custos</span>
            </h2>
            <p class="text-xs text-slate-400">
              Cadastre o pacote de compra (ex: 1 kg por R$ 100,00). O sistema calcula automaticamente frações como 100g (R$ 10,00) ou mg nos atendimentos!
            </p>
          </div>
          <button onclick="openNovoInsumoModal()" class="px-3.5 py-2 bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold text-xs rounded-lg transition flex items-center gap-1.5 shadow-md shadow-cyan-500/20">
            <i class="fa-solid fa-plus"></i> <span>Novo Insumo / Material</span>
          </button>
        </div>

        <!-- Table of Insumos -->
        <div class="overflow-x-auto rounded-lg border border-slate-800 custom-scrollbar">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-950 text-slate-400 font-semibold border-b border-slate-800">
              <tr>
                <th class="py-3 px-3">Nome do Insumo / Material</th>
                <th class="py-3 px-3">Unidade de Medida</th>
                <th class="py-3 px-3">Embalagem de Compra</th>
                <th class="py-3 px-3 text-right">Preço Pago</th>
                <th class="py-3 px-3 text-right">Custo Base Calculado</th>
                <th class="py-3 px-3 text-center">Exemplo de Fração</th>
                <th class="py-3 px-3 text-center">Estoque Atual</th>
                <th class="py-3 px-3 text-center">Ações</th>
              </tr>
            </thead>
            <tbody id="insumos-tbody" class="divide-y divide-slate-800/70 text-slate-200">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>


    <!-- ==================== TAB 6: CLIENTES ==================== -->
    <div id="tab-content-clientes" class="tab-pane hidden">
      <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-6">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-5">
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <i class="fa-solid fa-users text-cyan-400"></i>
              <span>Gestão de Clientes & Pacientes</span>
            </h2>
            <p class="text-xs text-slate-400">Histórico de atendimentos realizados, total investido e canal direto de WhatsApp.</p>
          </div>
          <button onclick="openNovoClienteModal()" class="px-3.5 py-2 bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold text-xs rounded-lg transition flex items-center gap-1.5 shadow-md shadow-cyan-500/20">
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

  <!-- MODAL: NOVO / EDITAR ATENDIMENTO -->
  <div id="modal-atendimento" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 id="modal-atendimento-title" class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-calendar-check text-cyan-400"></i>
          <span>Registrar Atendimento</span>
        </h3>
        <button onclick="closeModal('modal-atendimento')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-4 custom-scrollbar flex-1 text-xs">
        <input type="hidden" id="atend-id">

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Cliente *</label>
            <div class="flex gap-2">
              <select id="atend-cliente" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500"></select>
              <button type="button" onclick="openNovoClienteModal(true)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-cyan-400 border border-slate-700 rounded-lg" title="Cadastrar cliente rápido">
                <i class="fa-solid fa-user-plus"></i>
              </button>
            </div>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Data e Hora *</label>
            <input type="datetime-local" id="atend-data" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Serviço Principal *</label>
            <select id="atend-servico" onchange="onServicoSelecionadoNoAtendimento()" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500"></select>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Status na Esteira</label>
            <select id="atend-status" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
              <option value="novo">1. Novo Contato</option>
              <option value="agendado">2. Agendado / Avaliação</option>
              <option value="execucao">3. Em Execução</option>
              <option value="concluido" selected>4. Concluído & Faturado</option>
              <option value="cancelado">5. Cancelado</option>
            </select>
          </div>
        </div>

        <!-- Valores Financeiros -->
        <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 space-y-3">
          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-200 flex items-center gap-1.5">
              <i class="fa-solid fa-calculator text-cyan-400"></i> Composição Financeira da Operação
            </span>
            <span id="atend-resumo-margem" class="font-mono text-emerald-400 font-bold">Margem: 0%</span>
          </div>

          <div class="grid grid-cols-3 gap-3">
            <div>
              <label class="block text-slate-400 mb-1">Valor Cobrado (R$)</label>
              <input type="number" step="0.01" id="atend-valor" oninput="recalcularValoresAtendimento()" class="bg-slate-900 border border-slate-700 rounded-lg p-2 text-white font-mono font-bold w-full outline-none focus:border-cyan-500">
            </div>
            <div>
              <label class="block text-slate-400 mb-1">Custo Insumos (R$)</label>
              <input type="number" step="0.01" id="atend-custo" readonly class="bg-slate-900/50 border border-slate-800 rounded-lg p-2 text-amber-400 font-mono font-bold w-full cursor-not-allowed">
            </div>
            <div>
              <label class="block text-slate-400 mb-1">Lucro Líquido (R$)</label>
              <input type="number" step="0.01" id="atend-lucro" readonly class="bg-slate-900/50 border border-slate-800 rounded-lg p-2 text-emerald-400 font-mono font-bold w-full cursor-not-allowed">
            </div>
          </div>
        </div>

        <!-- Insumos específicos consumidos neste atendimento -->
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <label class="text-slate-300 font-semibold flex items-center gap-1">
              <i class="fa-solid fa-vial text-cyan-400"></i> Insumos gastos especificamente neste cliente:
            </label>
            <button type="button" onclick="adicionarLinhaInsumoAtendimento()" class="text-xs text-cyan-400 hover:text-cyan-300 font-semibold">
              + Adicionar Insumo Extra
            </button>
          </div>
          <div id="atend-insumos-container" class="space-y-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800 max-h-48 overflow-y-auto custom-scrollbar">
            <!-- Dynamic rows of consumables -->
          </div>
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Observações do Atendimento / Histórico Clínico ou Técnico</label>
          <textarea id="atend-obs" rows="2" placeholder="Ex: Paciente relatou sensibilidade, aplicado flúor extra sem custo adicional..." class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500"></textarea>
        </div>

      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-atendimento')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarAtendimento()" class="px-5 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs shadow-lg shadow-cyan-500/20 transition">Salvar Atendimento</button>
      </div>
    </div>
  </div>


  <!-- MODAL: NOVO / EDITAR SERVIÇO (FICHA TÉCNICA) -->
  <div id="modal-servico" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 id="modal-servico-title" class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-list-check text-cyan-400"></i>
          <span>Novo Serviço & Ficha Técnica</span>
        </h3>
        <button onclick="closeModal('modal-servico')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-4 custom-scrollbar flex-1 text-xs">
        <input type="hidden" id="serv-id">

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Nome do Serviço / Procedimento *</label>
          <input type="text" id="serv-nome" placeholder="Ex: Limpeza Dental Completa, Troca de Óleo, Consulta Especialista..." class="bg-slate-950 border border-slate-700 rounded-lg p-2.5 text-white w-full outline-none focus:border-cyan-500 text-sm">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Categoria</label>
            <input type="text" id="serv-categoria" placeholder="Ex: Odontologia, Estética, Mecânica..." class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
          </div>
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Preço Sugerido / Cobrado (R$) *</label>
            <input type="number" step="0.01" id="serv-preco" oninput="recalcularFichaTecnicaModal()" placeholder="0,00" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-emerald-400 font-mono font-bold w-full outline-none focus:border-cyan-500">
          </div>
        </div>

        <!-- Ficha Técnica de Insumos Padrão -->
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-3">
          <div class="flex items-center justify-between">
            <div>
              <span class="font-bold text-slate-200 flex items-center gap-1.5">
                <i class="fa-solid fa-flask text-cyan-400"></i> Ficha Técnica de Insumos Gastos por Operação
              </span>
              <p class="text-[11px] text-slate-400">Quais materiais são consumidos nesta operação por padrão?</p>
            </div>
            <button type="button" onclick="adicionarInsumoFichaTecnica()" class="px-2.5 py-1 bg-cyan-950 hover:bg-cyan-900 text-cyan-300 border border-cyan-800/80 rounded font-semibold text-[11px]">
              + Adicionar Insumo
            </button>
          </div>

          <div id="ficha-insumos-container" class="space-y-2 max-h-48 overflow-y-auto custom-scrollbar">
            <!-- Dynamic rows of standard consumables -->
          </div>

          <div class="flex items-center justify-between pt-2 border-t border-slate-800 font-mono text-xs">
            <span class="text-slate-400">Custo Total dos Insumos: <strong id="ficha-custo-total" class="text-amber-400">R$ 0,00</strong></span>
            <span class="text-slate-400">Lucro Estimado: <strong id="ficha-lucro-estimado" class="text-emerald-400">R$ 0,00</strong> (<span id="ficha-margem-estimada">0%</span>)</span>
          </div>
        </div>

      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-servico')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarServico()" class="px-5 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs shadow-lg shadow-cyan-500/20 transition">Salvar Serviço</button>
      </div>
    </div>
  </div>


  <!-- MODAL: NOVO / EDITAR INSUMO (PADRONIZAÇÃO g/kg/mg/L/ml/un) -->
  <div id="modal-insumo" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 id="modal-insumo-title" class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-boxes-stacked text-cyan-400"></i>
          <span>Novo Insumo & Cálculo Proporcional</span>
        </h3>
        <button onclick="closeModal('modal-insumo')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-4 custom-scrollbar flex-1 text-xs">
        <input type="hidden" id="ins-id">

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Nome do Insumo / Material *</label>
          <input type="text" id="ins-nome" placeholder="Ex: Bicarbonato de Sódio, Pasta Profilática, Resina, Óleo..." class="bg-slate-950 border border-slate-700 rounded-lg p-2.5 text-white w-full outline-none focus:border-cyan-500 text-sm">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Tipo de Medida *</label>
            <select id="ins-tipo-unidade" onchange="onTipoUnidadeChange()" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
              <option value="peso">Peso (kg / g / mg)</option>
              <option value="volume">Volume (L / ml)</option>
              <option value="unidade">Unidade / Peça / Caixa (un / cx / tubo)</option>
            </select>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Unidade da Embalagem Comprada *</label>
            <select id="ins-unidade-compra" onchange="recalcularCustoUnitarioInsumoModal()" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
              <!-- Dynamically populated based on tipo -->
            </select>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Quantidade no Pacote/Embalagem *</label>
            <input type="number" step="any" id="ins-qtd-compra" oninput="recalcularCustoUnitarioInsumoModal()" value="1" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white font-mono font-bold w-full outline-none focus:border-cyan-500">
            <span class="text-[10px] text-slate-400">Ex: 1 para 1kg, 500 para 500g, 50 para 50 un</span>
          </div>

          <div>
            <label class="block text-slate-300 font-semibold mb-1">Preço Total Pago na Embalagem (R$) *</label>
            <input type="number" step="0.01" id="ins-preco-compra" oninput="recalcularCustoUnitarioInsumoModal()" placeholder="0,00" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-emerald-400 font-mono font-bold w-full outline-none focus:border-cyan-500">
            <span class="text-[10px] text-slate-400">Valor na nota de compra</span>
          </div>
        </div>

        <!-- Proportional Cost Preview Box -->
        <div class="p-3 bg-cyan-950/40 rounded-xl border border-cyan-800/60 space-y-1.5 font-mono">
          <div class="flex items-center justify-between text-cyan-300 font-bold">
            <span>Custo Base por Fração:</span>
            <span id="ins-preview-base" class="text-white font-black">R$ 0,00</span>
          </div>
          <div id="ins-preview-conversoes" class="text-[11px] text-slate-300 space-y-0.5">
            <!-- Conversions dynamically shown: 100g = R$ 10,00, etc. -->
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Estoque Atual</label>
            <input type="number" step="any" id="ins-estoque-atual" value="10" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
          </div>
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Estoque Mínimo (Alerta)</label>
            <input type="number" step="any" id="ins-estoque-minimo" value="2" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
          </div>
        </div>

      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-insumo')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarInsumo()" class="px-5 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs shadow-lg shadow-cyan-500/20 transition">Salvar Insumo</button>
      </div>
    </div>
  </div>


  <!-- MODAL: NOVO / EDITAR CLIENTE -->
  <div id="modal-cliente" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-md max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 id="modal-cliente-title" class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-user-plus text-cyan-400"></i>
          <span>Novo Cliente</span>
        </h3>
        <button onclick="closeModal('modal-cliente')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-3 custom-scrollbar flex-1 text-xs">
        <input type="hidden" id="cli-id">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Nome Completo *</label>
          <input type="text" id="cli-nome" placeholder="Ex: Roberto Silva" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-white w-full outline-none focus:border-cyan-500">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">WhatsApp / Telefone *</label>
          <input type="text" id="cli-telefone" placeholder="(32) 99929-2311" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">E-mail</label>
          <input type="email" id="cli-email" placeholder="cliente@exemplo.com" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Cidade / Bairro</label>
          <input type="text" id="cli-cidade" placeholder="Ex: Juiz de Fora - MG" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
        </div>
      </div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-end gap-2">
        <button onclick="closeModal('modal-cliente')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Cancelar</button>
        <button onclick="salvarCliente()" class="px-5 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs shadow-lg shadow-cyan-500/20 transition">Salvar Cliente</button>
      </div>
    </div>
  </div>


  <!-- MODAL: CONFIGURAÇÕES & BACKUP -->
  <div id="modal-config" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg max-h-[92vh] flex flex-col overflow-hidden shadow-2xl">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <h3 class="font-bold text-white text-base flex items-center gap-2">
          <i class="fa-solid fa-sliders text-cyan-400"></i>
          <span>Configurações do CRM & Backup</span>
        </h3>
        <button onclick="closeModal('modal-config')" class="text-slate-400 hover:text-white p-1 text-sm"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="p-5 overflow-y-auto space-y-4 custom-scrollbar flex-1 text-xs">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Nome da Empresa / Profissional *</label>
          <input type="text" id="cfg-nome-empresa" class="bg-slate-950 border border-slate-700 rounded-lg p-2.5 text-white w-full outline-none focus:border-cyan-500 font-bold">
          <span class="text-[10px] text-slate-400">Altere para o nome da sua clínica, escritório, consultório ou empresa.</span>
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">WhatsApp Padrão para Contato dos Clientes</label>
          <input type="text" id="cfg-whatsapp" value="32999292311" class="bg-slate-950 border border-slate-700 rounded-lg p-2 text-slate-200 w-full outline-none focus:border-cyan-500">
        </div>

        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
          <span class="font-bold text-slate-300 block">Backup & Migração dos Dados</span>
          <p class="text-[11px] text-slate-400">Seus dados ficam 100% salvos no seu navegador. Você pode exportar para levar para outro computador ou importar a qualquer momento.</p>
          <div class="flex items-center gap-2 pt-1">
            <button onclick="exportarBackupJSON()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg font-semibold flex items-center gap-1.5">
              <i class="fa-solid fa-download text-cyan-400"></i> Exportar Dados (JSON)
            </button>
            <label class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg font-semibold flex items-center gap-1.5 cursor-pointer">
              <i class="fa-solid fa-upload text-emerald-400"></i> Importar Dados (JSON)
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
        <button onclick="salvarConfiguracoes()" class="px-5 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs shadow-lg shadow-cyan-500/20 transition">Salvar Configurações</button>
      </div>
    </div>
  </div>

  <!-- SCRIPT LOGIC -->
  <script src="crm_servicos.js"></script>
</body>
</html>
"""

with open("crm-servicos/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("crm-servicos/index.html generated successfully.")
