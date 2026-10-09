# -*- coding: utf-8 -*-
"""
Script to apply typography, fast-scan visual hierarchy,
distinct Lucro/Prejuízo colors, and chart animations to both CRMs.
"""

def update_crm_servicos_html():
    path = "crm-servicos/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update font and style declarations
    old_style = """  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(51, 65, 85, 0.7); border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(203, 213, 225, 0.9); border-radius: 9999px; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(6, 182, 212, 0.6); }
  </style>"""

    new_style = """  <style>
    body {
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
      font-feature-settings: "tnum" 1;
      font-variant-numeric: tabular-nums;
    }
    .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(51, 65, 85, 0.7); border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(203, 213, 225, 0.9); border-radius: 9999px; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(6, 182, 212, 0.6); }

    /* Fast-scan KPI Cards & Smooth Animations */
    .kpi-card-transition {
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, border-color 0.25s ease;
    }
    .kpi-card-transition:hover {
      transform: translateY(-2px);
    }
    .progress-bar-fill {
      transition: width 1s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @keyframes pulseAlert {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.85; transform: scale(1.01); }
    }
    .animate-pulse-alert {
      animation: pulseAlert 2s infinite ease-in-out;
    }
  </style>"""

    if old_style in html:
        html = html.replace(old_style, new_style)
    else:
        print("Warning: old_style not found directly in crm-servicos/index.html")

    # 2. Add id="kpi-card-lucro" and id="kpi-lucro-desc" and id="kpi-lucro-badge"
    old_lucro_kpi = """        <!-- Lucro Líquido (Emerald) -->
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/50 transition">
          <div class="flex items-center justify-between text-slate-500 dark:text-slate-400 mb-1.5">
            <span class="text-[11px] font-bold uppercase tracking-wider">Lucro Líquido</span>
            <div class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-arrow-trend-up"></i>
            </div>
          </div>
          <div id="kpi-lucro" class="text-xl sm:text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono tracking-tight">R$ 0,00</div>
          <span class="text-[11px] text-emerald-600 dark:text-emerald-400 mt-1 block font-semibold flex items-center gap-1">
            <i class="fa-solid fa-circle-check text-[9px]"></i> Faturamento - Custos
          </span>
        </div>"""

    new_lucro_kpi = """        <!-- Lucro Líquido / Prejuízo (Dinâmico) -->
        <div id="kpi-card-lucro" class="kpi-card-transition bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/50 transition">
          <div class="flex items-center justify-between text-slate-500 dark:text-slate-400 mb-1.5">
            <span id="kpi-lucro-title" class="text-[11px] font-bold uppercase tracking-wider">Lucro Líquido Real</span>
            <div id="kpi-lucro-icon-box" class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-xs">
              <i id="kpi-lucro-icon" class="fa-solid fa-arrow-trend-up"></i>
            </div>
          </div>
          <div id="kpi-lucro" class="text-xl sm:text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono tracking-tight">R$ 0,00</div>
          <span id="kpi-lucro-desc" class="text-[11px] text-emerald-600 dark:text-emerald-400 mt-1 block font-semibold flex items-center gap-1">
            <i class="fa-solid fa-circle-check text-[9px]"></i> Faturamento - Custos
          </span>
        </div>"""

    if old_lucro_kpi in html:
        html = html.replace(old_lucro_kpi, new_lucro_kpi)

    # 3. Add Fast Visual Analytics Strip (Termômetro de Rentabilidade)
    analytics_strip = """      </div>

      <!-- TERMÔMETRO VISUAL DE RENTABILIDADE (GRÁFICO ANIMADO PARA VISUALIZAÇÃO RÁPIDA) -->
      <div class="mt-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 shadow-sm">
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3 pb-3 mb-3 border-b border-slate-100 dark:border-slate-800/80">
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 flex items-center justify-center text-base font-bold shrink-0">
              <i class="fa-solid fa-chart-column"></i>
            </div>
            <div>
              <div class="flex items-center gap-2 flex-wrap">
                <h3 class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">
                  Termômetro de Rentabilidade em Tempo Real
                </h3>
                <span id="health-semaphore-badge" class="px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800 flex items-center gap-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping"></span> Operação Altamente Lucrativa
                </span>
              </div>
              <p class="text-[11px] text-slate-500 dark:text-slate-400">Visão executiva imediata: proporção entre o dinheiro que fica no caixa (Lucro) vs custos operacionais</p>
            </div>
          </div>
          
          <!-- Quick Legend with dynamic values -->
          <div class="flex items-center gap-4 text-xs font-mono shrink-0">
            <div class="flex items-center gap-1.5">
              <span class="w-3 h-3 rounded-md bg-emerald-500 shrink-0"></span>
              <span class="text-slate-500 dark:text-slate-400 font-sans text-[11px]">Lucro Líquido:</span>
              <strong id="bar-legend-lucro" class="text-emerald-600 dark:text-emerald-400 font-bold">R$ 0,00 (0%)</strong>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="w-3 h-3 rounded-md bg-amber-500 shrink-0"></span>
              <span class="text-slate-500 dark:text-slate-400 font-sans text-[11px]">Custo Insumos:</span>
              <strong id="bar-legend-custo" class="text-amber-600 dark:text-amber-400 font-bold">R$ 0,00 (0%)</strong>
            </div>
          </div>
        </div>

        <!-- Animated Proportion Bar -->
        <div class="space-y-1.5">
          <div class="w-full bg-slate-100 dark:bg-slate-950 h-5 sm:h-6 rounded-xl overflow-hidden p-0.5 border border-slate-200 dark:border-slate-800 flex gap-0.5">
            <div id="chart-bar-lucro" class="h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm" style="width: 0%;" title="Lucro Líquido"></div>
            <div id="chart-bar-custo" class="h-full bg-gradient-to-r from-amber-500 to-amber-600 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm" style="width: 0%;" title="Custos"></div>
          </div>
          <div class="flex justify-between items-center text-[10px] text-slate-400 font-mono px-1">
            <span>0% (Custo Zero)</span>
            <span id="chart-bar-hint" class="font-sans font-semibold text-slate-600 dark:text-slate-300">Retenção de caixa: 88.6%</span>
            <span>100% (Faturamento Total)</span>
          </div>
        </div>
      </div>
    </section>"""

    # Replace end of section
    old_end = """        </div>

      </div>
    </section>"""

    if old_end in html:
        html = html.replace(old_end, analytics_strip)
    else:
        print("Warning: old_end not found in crm-servicos/index.html")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("crm-servicos/index.html successfully updated.")

def update_crm_vendas_html():
    path = "crm-vendas/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update font and style declarations
    old_style = """  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(51, 65, 85, 0.7); border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(203, 213, 225, 0.9); border-radius: 9999px; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(16, 185, 129, 0.6); }
  </style>"""

    new_style = """  <style>
    body {
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
      font-feature-settings: "tnum" 1;
      font-variant-numeric: tabular-nums;
    }
    .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(51, 65, 85, 0.7); border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(203, 213, 225, 0.9); border-radius: 9999px; }
    .dark .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(16, 185, 129, 0.6); }

    /* Fast-scan KPI Cards & Smooth Animations */
    .kpi-card-transition {
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, border-color 0.25s ease;
    }
    .kpi-card-transition:hover {
      transform: translateY(-2px);
    }
    .progress-bar-fill {
      transition: width 1s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @keyframes pulseAlert {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.85; transform: scale(1.01); }
    }
    .animate-pulse-alert {
      animation: pulseAlert 2s infinite ease-in-out;
    }
  </style>"""

    if old_style in html:
        html = html.replace(old_style, new_style)

    # 2. Add id="kpi-card-lucro" and id="kpi-lucro-desc" and id="kpi-lucro-badge"
    old_lucro_kpi = """        <!-- Lucro Líquido (Emerald) -->
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/50 transition">
          <div class="flex items-center justify-between text-slate-500 dark:text-slate-400 mb-1.5">
            <span class="text-[11px] font-bold uppercase tracking-wider">Lucro Líquido</span>
            <div class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-arrow-trend-up"></i>
            </div>
          </div>
          <div id="kpi-lucro" class="text-xl sm:text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono tracking-tight">R$ 0,00</div>
          <span class="text-[11px] text-emerald-600 dark:text-emerald-400 mt-1 block font-semibold flex items-center gap-1">
            <i class="fa-solid fa-circle-check text-[9px]"></i> Faturamento - Custos
          </span>
        </div>"""

    new_lucro_kpi = """        <!-- Lucro Líquido / Prejuízo (Dinâmico) -->
        <div id="kpi-card-lucro" class="kpi-card-transition bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/50 transition">
          <div class="flex items-center justify-between text-slate-500 dark:text-slate-400 mb-1.5">
            <span id="kpi-lucro-title" class="text-[11px] font-bold uppercase tracking-wider">Lucro Líquido Real</span>
            <div id="kpi-lucro-icon-box" class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-xs">
              <i id="kpi-lucro-icon" class="fa-solid fa-arrow-trend-up"></i>
            </div>
          </div>
          <div id="kpi-lucro" class="text-xl sm:text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono tracking-tight">R$ 0,00</div>
          <span id="kpi-lucro-desc" class="text-[11px] text-emerald-600 dark:text-emerald-400 mt-1 block font-semibold flex items-center gap-1">
            <i class="fa-solid fa-circle-check text-[9px]"></i> Faturamento - Custos (CMV)
          </span>
        </div>"""

    if old_lucro_kpi in html:
        html = html.replace(old_lucro_kpi, new_lucro_kpi)

    # 3. Add Fast Visual Analytics Strip
    analytics_strip = """      </div>

      <!-- TERMÔMETRO VISUAL DE RENTABILIDADE (GRÁFICO ANIMADO PARA VISUALIZAÇÃO RÁPIDA) -->
      <div class="mt-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 shadow-sm">
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3 pb-3 mb-3 border-b border-slate-100 dark:border-slate-800/80">
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-base font-bold shrink-0">
              <i class="fa-solid fa-chart-column"></i>
            </div>
            <div>
              <div class="flex items-center gap-2 flex-wrap">
                <h3 class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">
                  Termômetro Comercial em Tempo Real
                </h3>
                <span id="health-semaphore-badge" class="px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800 flex items-center gap-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping"></span> Operação Altamente Lucrativa
                </span>
              </div>
              <p class="text-[11px] text-slate-500 dark:text-slate-400">Visão executiva imediata: retenção líquida de caixa vs Custo de Mercadorias Vendidas (CMV)</p>
            </div>
          </div>
          
          <!-- Quick Legend with dynamic values -->
          <div class="flex items-center gap-4 text-xs font-mono shrink-0">
            <div class="flex items-center gap-1.5">
              <span class="w-3 h-3 rounded-md bg-emerald-500 shrink-0"></span>
              <span class="text-slate-500 dark:text-slate-400 font-sans text-[11px]">Lucro Líquido:</span>
              <strong id="bar-legend-lucro" class="text-emerald-600 dark:text-emerald-400 font-bold">R$ 0,00 (0%)</strong>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="w-3 h-3 rounded-md bg-amber-500 shrink-0"></span>
              <span class="text-slate-500 dark:text-slate-400 font-sans text-[11px]">Custo CMV:</span>
              <strong id="bar-legend-custo" class="text-amber-600 dark:text-amber-400 font-bold">R$ 0,00 (0%)</strong>
            </div>
          </div>
        </div>

        <!-- Animated Proportion Bar -->
        <div class="space-y-1.5">
          <div class="w-full bg-slate-100 dark:bg-slate-950 h-5 sm:h-6 rounded-xl overflow-hidden p-0.5 border border-slate-200 dark:border-slate-800 flex gap-0.5">
            <div id="chart-bar-lucro" class="h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm" style="width: 0%;" title="Lucro Líquido"></div>
            <div id="chart-bar-custo" class="h-full bg-gradient-to-r from-amber-500 to-amber-600 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm" style="width: 0%;" title="CMV"></div>
          </div>
          <div class="flex justify-between items-center text-[10px] text-slate-400 font-mono px-1">
            <span>0% (Custo Zero)</span>
            <span id="chart-bar-hint" class="font-sans font-semibold text-slate-600 dark:text-slate-300">Retenção de caixa: 44.0%</span>
            <span>100% (Receita Total)</span>
          </div>
        </div>
      </div>
    </section>"""

    old_end = """        </div>

      </div>
    </section>"""

    if old_end in html:
        html = html.replace(old_end, analytics_strip)
    else:
        print("Warning: old_end not found in crm-vendas/index.html")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("crm-vendas/index.html successfully updated.")

if __name__ == "__main__":
    update_crm_servicos_html()
    update_crm_vendas_html()
