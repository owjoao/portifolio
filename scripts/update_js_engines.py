# -*- coding: utf-8 -*-
"""
Update crm_servicos.js and crm_vendas.js with:
1. animateNumber() count-up transitions
2. renderVisualAnalytics() real-time animated proportion bar & health indicators
3. Dynamic Lucro vs Prejuízo card & badge styling
4. Kanban card profit/loss semantic differentiation
"""

def update_crm_servicos_js():
    path = "crm-servicos/crm_servicos.js"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # Replacement for updateAllViews and adding animation functions
    target_start = "// ============================================================\n// CORE VIEW REFRESH & KPIS\n// ============================================================"
    target_end = "  renderClientes();\n}"

    new_engine = """// ============================================================
// ANIMATED NUMERICAL COUNTER (FOR FAST SCANNING & DELIGHTFUL UX)
// ============================================================
function animateNumber(elementId, endValue, options = {}) {
  const el = document.getElementById(elementId);
  if (!el) return;
  const { isCurrency = false, isPercent = false, duration = 450 } = options;

  const startValue = el._currentVal !== undefined ? el._currentVal : 0;
  el._currentVal = endValue;

  const startTime = performance.now();

  function step(now) {
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    // Smooth easeOutExpo
    const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
    const current = startValue + (endValue - startValue) * ease;

    if (isCurrency) {
      el.textContent = formatMoney(current);
    } else if (isPercent) {
      el.textContent = current.toFixed(1) + '%';
    } else {
      el.textContent = Math.round(current);
    }

    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      if (isCurrency) el.textContent = formatMoney(endValue);
      else if (isPercent) el.textContent = endValue.toFixed(1) + '%';
      else el.textContent = endValue;
    }
  }

  requestAnimationFrame(step);
}

// ============================================================
// ANIMATED VISUAL ANALYTICS (REAL-TIME FINANCIAL THERMOMETER)
// ============================================================
function renderVisualAnalytics(totalFaturamento, totalCustos, totalLucro, margemMedia) {
  const barLucro = document.getElementById('chart-bar-lucro');
  const barCusto = document.getElementById('chart-bar-custo');
  const legLucro = document.getElementById('bar-legend-lucro');
  const legCusto = document.getElementById('bar-legend-custo');
  const badgeHealth = document.getElementById('health-semaphore-badge');
  const hintEl = document.getElementById('chart-bar-hint');

  if (!barLucro || !barCusto) return;

  const pctLucro = totalFaturamento > 0 && totalLucro > 0 ? (totalLucro / totalFaturamento) * 100 : 0;
  const pctCusto = totalFaturamento > 0 ? (totalCustos / totalFaturamento) * 100 : (totalCustos > 0 ? 100 : 0);

  if (totalLucro >= 0) {
    barLucro.style.width = `${Math.min(100, Math.max(0, pctLucro))}%`;
    barLucro.textContent = pctLucro > 12 ? `${pctLucro.toFixed(0)}% Lucro` : '';
    barLucro.className = "h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm";

    barCusto.style.width = `${Math.min(100, Math.max(0, pctCusto))}%`;
    barCusto.textContent = pctCusto > 12 ? `${pctCusto.toFixed(0)}% Custo` : '';
    barCusto.className = "h-full bg-gradient-to-r from-amber-500 to-amber-600 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm";

    if (legLucro) legLucro.innerHTML = `<span class="text-emerald-500 font-bold">+${formatMoney(totalLucro)} (${pctLucro.toFixed(1)}%)</span>`;
    if (legCusto) legCusto.innerHTML = `<span class="text-amber-500 font-bold">${formatMoney(totalCustos)} (${pctCusto.toFixed(1)}%)</span>`;

    if (badgeHealth) {
      if (margemMedia >= 60) {
        badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800 flex items-center gap-1";
        badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping"></span> Operação Altamente Lucrativa';
      } else if (margemMedia >= 30) {
        badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-cyan-100 text-cyan-700 dark:bg-cyan-950 dark:text-cyan-400 border border-cyan-300 dark:border-cyan-800 flex items-center gap-1";
        badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-cyan-500"></span> Margem Estável & Saudável';
      } else {
        badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-400 border border-amber-300 dark:border-amber-800 flex items-center gap-1";
        badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span> Margem Apertada / Atenção';
      }
    }

    if (hintEl) {
      hintEl.textContent = `Retenção de Caixa: ${pctLucro.toFixed(1)}% do faturamento líquido disponível`;
    }
  } else {
    // PREJUÍZO DETECTADO
    barLucro.style.width = `0%`;
    barLucro.textContent = '';
    barCusto.style.width = `100%`;
    barCusto.textContent = '100% Custos Superaram Faturamento';
    barCusto.className = "h-full bg-gradient-to-r from-rose-600 to-rose-500 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-white font-mono shadow-sm animate-pulse";

    if (legLucro) legLucro.innerHTML = `<span class="text-rose-500 font-black">Prejuízo: -${formatMoney(Math.abs(totalLucro))}</span>`;
    if (legCusto) legCusto.innerHTML = `<span class="text-amber-500 font-bold">${formatMoney(totalCustos)}</span>`;

    if (badgeHealth) {
      badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300 border border-rose-300 dark:border-rose-800 flex items-center gap-1 animate-pulse";
      badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span> ALERTA: PREJUÍZO OPERACIONAL';
    }

    if (hintEl) {
      hintEl.textContent = `Atenção: Os insumos superaram o total cobrado em ${formatMoney(Math.abs(totalLucro))}`;
    }
  }
}

// ============================================================
// CORE VIEW REFRESH & KPIS
// ============================================================
function updateAllViews() {
  const filtered = getFilteredAtendimentos();
  const faturados = filtered.filter(a => a.status === 'concluido');

  // Recalculate Totals
  const totalFaturamento = faturados.reduce((acc, a) => acc + (a.valorCobrado || 0), 0);
  const totalCustos = faturados.reduce((acc, a) => acc + (a.custoInsumos || 0), 0);
  const totalLucro = totalFaturamento - totalCustos;
  const margemMedia = totalFaturamento > 0 ? (totalLucro / totalFaturamento) * 100 : 0;
  const totalCount = faturados.length;
  const ticketMedio = totalCount > 0 ? totalFaturamento / totalCount : 0;

  // Animated KPI Numbers (Fast scan & pleasant motion)
  animateNumber('kpi-faturamento', totalFaturamento, { isCurrency: true });
  animateNumber('kpi-custos', totalCustos, { isCurrency: true });
  animateNumber('kpi-lucro', totalLucro, { isCurrency: true });
  animateNumber('kpi-margem', margemMedia, { isPercent: true });
  animateNumber('kpi-atendimentos', totalCount);
  animateNumber('kpi-ticket', ticketMedio, { isCurrency: true });
  const badgeTotal = document.getElementById('badge-total-atendimentos');
  if (badgeTotal) badgeTotal.textContent = appState.atendimentos.length;

  // Dynamic Lucro vs Prejuízo Card Styler
  const cardLucro = document.getElementById('kpi-card-lucro');
  const lucroEl = document.getElementById('kpi-lucro');
  const lucroTitle = document.getElementById('kpi-lucro-title');
  const lucroIconBox = document.getElementById('kpi-lucro-icon-box');
  const lucroIcon = document.getElementById('kpi-lucro-icon');
  const lucroDesc = document.getElementById('kpi-lucro-desc');

  if (totalLucro >= 0) {
    if (cardLucro) {
      cardLucro.className = "kpi-card-transition bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/50 transition";
    }
    if (lucroTitle) lucroTitle.textContent = "Lucro Líquido Real";
    if (lucroIconBox) {
      lucroIconBox.className = "w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-xs";
    }
    if (lucroIcon) lucroIcon.className = "fa-solid fa-arrow-trend-up";
    if (lucroEl) {
      lucroEl.className = "text-xl sm:text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono tracking-tight";
    }
    if (lucroDesc) {
      lucroDesc.innerHTML = `<i class="fa-solid fa-circle-check text-[9px] text-emerald-500"></i> Faturamento excede custos em <strong class="text-emerald-600 dark:text-emerald-400">${formatMoney(totalLucro)}</strong>`;
      lucroDesc.className = "text-[11px] text-emerald-600 dark:text-emerald-400 mt-1 block font-semibold";
    }
  } else {
    // PREJUÍZO OPERACIONAL!
    if (cardLucro) {
      cardLucro.className = "kpi-card-transition bg-rose-50/80 dark:bg-rose-950/40 border-2 border-rose-500/80 rounded-2xl p-4 shadow-md shadow-rose-500/10 relative overflow-hidden group hover:border-rose-500 transition animate-pulse-alert";
    }
    if (lucroTitle) lucroTitle.textContent = "Prejuízo Operacional";
    if (lucroIconBox) {
      lucroIconBox.className = "w-8 h-8 rounded-xl bg-rose-200 dark:bg-rose-900 text-rose-700 dark:text-rose-200 flex items-center justify-center text-xs animate-bounce";
    }
    if (lucroIcon) lucroIcon.className = "fa-solid fa-triangle-exclamation";
    if (lucroEl) {
      lucroEl.className = "text-xl sm:text-2xl font-black text-rose-600 dark:text-rose-400 font-mono tracking-tight";
    }
    if (lucroDesc) {
      lucroDesc.innerHTML = `<i class="fa-solid fa-triangle-exclamation text-[9px] text-rose-500"></i> Insumos excedem receita em <strong class="text-rose-600 dark:text-rose-400">${formatMoney(Math.abs(totalLucro))}</strong>`;
      lucroDesc.className = "text-[11px] text-rose-600 dark:text-rose-400 mt-1 block font-bold";
    }
  }

  // Render Visual Charts
  renderVisualAnalytics(totalFaturamento, totalCustos, totalLucro, margemMedia);

  // Update tabs
  renderKanban();
  renderHistorico();
  renderMargens();
  renderServicos();
  renderInsumos();
  renderClientes();
}"""

    # Locate region to replace
    idx_start = code.find(target_start)
    idx_end = code.find(target_end, idx_start)
    if idx_start != -1 and idx_end != -1:
        code = code[:idx_start] + new_engine + code[idx_end + len(target_end):]
    else:
        print("Error locating target region in crm-servicos/crm_servicos.js")

    # Also update kanban card profit/loss display
    old_card_profit = """        <div class="col-span-2 pt-1 border-t border-slate-200 dark:border-slate-800/60 flex items-center justify-between">
          <span class="text-slate-600 dark:text-slate-400">Lucro: <strong class="text-emerald-600 dark:text-emerald-400 font-bold">${formatMoney(atend.lucroLiquido)}</strong></span>
          <span class="text-cyan-600 dark:text-cyan-300 font-bold">${formatPercent(atend.margem)}</span>
        </div>"""

    new_card_profit = """        <div class="col-span-2 pt-1 border-t border-slate-200 dark:border-slate-800/60 flex items-center justify-between">
          <span class="text-slate-600 dark:text-slate-400">
            ${atend.lucroLiquido >= 0 ? 'Lucro:' : 'Prejuízo:'}
            <strong class="${atend.lucroLiquido >= 0 ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'} font-bold">
              ${atend.lucroLiquido >= 0 ? '▲ +' : '▼ -'}${formatMoney(Math.abs(atend.lucroLiquido))}
            </strong>
          </span>
          <span class="${atend.lucroLiquido >= 0 ? (atend.margem >= 50 ? 'text-emerald-600 dark:text-emerald-400' : 'text-cyan-600 dark:text-cyan-300') : 'text-rose-600 dark:text-rose-400 font-black'} font-bold">
            ${formatPercent(atend.margem)}
          </span>
        </div>"""

    if old_card_profit in code:
        code = code.replace(old_card_profit, new_card_profit)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print("crm-servicos/crm_servicos.js updated successfully.")


def update_crm_vendas_js():
    path = "crm-vendas/crm_vendas.js"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    target_start = "// ============================================================\n// CORE VIEW REFRESH & KPIS\n// ============================================================"
    target_end = "  renderClientes();\n}"

    new_engine = """// ============================================================
// ANIMATED NUMERICAL COUNTER (FOR FAST SCANNING & DELIGHTFUL UX)
// ============================================================
function animateNumber(elementId, endValue, options = {}) {
  const el = document.getElementById(elementId);
  if (!el) return;
  const { isCurrency = false, isPercent = false, duration = 450 } = options;

  const startValue = el._currentVal !== undefined ? el._currentVal : 0;
  el._currentVal = endValue;

  const startTime = performance.now();

  function step(now) {
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
    const current = startValue + (endValue - startValue) * ease;

    if (isCurrency) {
      el.textContent = formatMoney(current);
    } else if (isPercent) {
      el.textContent = current.toFixed(1) + '%';
    } else {
      el.textContent = Math.round(current);
    }

    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      if (isCurrency) el.textContent = formatMoney(endValue);
      else if (isPercent) el.textContent = endValue.toFixed(1) + '%';
      else el.textContent = endValue;
    }
  }

  requestAnimationFrame(step);
}

// ============================================================
// ANIMATED VISUAL ANALYTICS (REAL-TIME FINANCIAL THERMOMETER)
// ============================================================
function renderVisualAnalytics(totalFaturamento, totalCustos, totalLucro, margemMedia) {
  const barLucro = document.getElementById('chart-bar-lucro');
  const barCusto = document.getElementById('chart-bar-custo');
  const legLucro = document.getElementById('bar-legend-lucro');
  const legCusto = document.getElementById('bar-legend-custo');
  const badgeHealth = document.getElementById('health-semaphore-badge');
  const hintEl = document.getElementById('chart-bar-hint');

  if (!barLucro || !barCusto) return;

  const pctLucro = totalFaturamento > 0 && totalLucro > 0 ? (totalLucro / totalFaturamento) * 100 : 0;
  const pctCusto = totalFaturamento > 0 ? (totalCustos / totalFaturamento) * 100 : (totalCustos > 0 ? 100 : 0);

  if (totalLucro >= 0) {
    barLucro.style.width = `${Math.min(100, Math.max(0, pctLucro))}%`;
    barLucro.textContent = pctLucro > 12 ? `${pctLucro.toFixed(0)}% Lucro` : '';
    barLucro.className = "h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm";

    barCusto.style.width = `${Math.min(100, Math.max(0, pctCusto))}%`;
    barCusto.textContent = pctCusto > 12 ? `${pctCusto.toFixed(0)}% CMV` : '';
    barCusto.className = "h-full bg-gradient-to-r from-amber-500 to-amber-600 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-slate-950 font-mono shadow-sm";

    if (legLucro) legLucro.innerHTML = `<span class="text-emerald-500 font-bold">+${formatMoney(totalLucro)} (${pctLucro.toFixed(1)}%)</span>`;
    if (legCusto) legCusto.innerHTML = `<span class="text-amber-500 font-bold">${formatMoney(totalCustos)} (${pctCusto.toFixed(1)}%)</span>`;

    if (badgeHealth) {
      if (margemMedia >= 40) {
        badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800 flex items-center gap-1";
        badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping"></span> Operação Comercial Altamente Lucrativa';
      } else if (margemMedia >= 20) {
        badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-cyan-100 text-cyan-700 dark:bg-cyan-950 dark:text-cyan-400 border border-cyan-300 dark:border-cyan-800 flex items-center gap-1";
        badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-cyan-500"></span> Margem Comercial Estável';
      } else {
        badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-400 border border-amber-300 dark:border-amber-800 flex items-center gap-1";
        badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span> Margem Estreita / Atenção';
      }
    }

    if (hintEl) {
      hintEl.textContent = `Retenção Líquida: ${pctLucro.toFixed(1)}% das vendas convertidas em lucro no caixa`;
    }
  } else {
    // PREJUÍZO DETECTADO
    barLucro.style.width = `0%`;
    barLucro.textContent = '';
    barCusto.style.width = `100%`;
    barCusto.textContent = '100% Custos Superaram Vendas';
    barCusto.className = "h-full bg-gradient-to-r from-rose-600 to-rose-500 rounded-lg transition-all duration-1000 ease-out flex items-center justify-center px-2 text-[10px] font-bold text-white font-mono shadow-sm animate-pulse";

    if (legLucro) legLucro.innerHTML = `<span class="text-rose-500 font-black">Prejuízo: -${formatMoney(Math.abs(totalLucro))}</span>`;
    if (legCusto) legCusto.innerHTML = `<span class="text-amber-500 font-bold">${formatMoney(totalCustos)}</span>`;

    if (badgeHealth) {
      badgeHealth.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black tracking-normal uppercase bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300 border border-rose-300 dark:border-rose-800 flex items-center gap-1 animate-pulse";
      badgeHealth.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span> ALERTA: PREJUÍZO COMERCIAL';
    }

    if (hintEl) {
      hintEl.textContent = `Atenção: O CMV superou as vendas em ${formatMoney(Math.abs(totalLucro))}`;
    }
  }
}

// ============================================================
// CORE VIEW REFRESH & KPIS
// ============================================================
function updateAllViews() {
  const filtered = getFilteredVendas();
  const faturadas = filtered.filter(v => v.etapa === 'fechada');

  // Recalculate Totals
  const totalFaturamento = faturadas.reduce((acc, v) => acc + (v.valorTotalVenda || 0), 0);
  const totalCustos = faturadas.reduce((acc, v) => acc + (v.custoTotal || 0), 0);
  const totalLucro = totalFaturamento - totalCustos;
  const margemMedia = totalFaturamento > 0 ? (totalLucro / totalFaturamento) * 100 : 0;
  const totalItens = faturadas.reduce((acc, v) => acc + (v.quantidade || 0), 0);
  const totalCount = faturadas.length;
  const ticketMedio = totalCount > 0 ? totalFaturamento / totalCount : 0;

  // Animated KPI Numbers
  animateNumber('kpi-faturamento', totalFaturamento, { isCurrency: true });
  animateNumber('kpi-custos', totalCustos, { isCurrency: true });
  animateNumber('kpi-lucro', totalLucro, { isCurrency: true });
  animateNumber('kpi-margem', margemMedia, { isPercent: true });
  animateNumber('kpi-itens-vendidos', totalItens);
  animateNumber('kpi-ticket', ticketMedio, { isCurrency: true });
  const badgeTotal = document.getElementById('badge-total-vendas');
  if (badgeTotal) badgeTotal.textContent = appState.vendas.length;

  // Dynamic Lucro vs Prejuízo Card Styler
  const cardLucro = document.getElementById('kpi-card-lucro');
  const lucroEl = document.getElementById('kpi-lucro');
  const lucroTitle = document.getElementById('kpi-lucro-title');
  const lucroIconBox = document.getElementById('kpi-lucro-icon-box');
  const lucroIcon = document.getElementById('kpi-lucro-icon');
  const lucroDesc = document.getElementById('kpi-lucro-desc');

  if (totalLucro >= 0) {
    if (cardLucro) {
      cardLucro.className = "kpi-card-transition bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm relative overflow-hidden group hover:border-emerald-500/50 transition";
    }
    if (lucroTitle) lucroTitle.textContent = "Lucro Líquido Real";
    if (lucroIconBox) {
      lucroIconBox.className = "w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-400 flex items-center justify-center text-xs";
    }
    if (lucroIcon) lucroIcon.className = "fa-solid fa-arrow-trend-up";
    if (lucroEl) {
      lucroEl.className = "text-xl sm:text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono tracking-tight";
    }
    if (lucroDesc) {
      lucroDesc.innerHTML = `<i class="fa-solid fa-circle-check text-[9px] text-emerald-500"></i> Faturamento excede custos em <strong class="text-emerald-600 dark:text-emerald-400">${formatMoney(totalLucro)}</strong>`;
      lucroDesc.className = "text-[11px] text-emerald-600 dark:text-emerald-400 mt-1 block font-semibold";
    }
  } else {
    // PREJUÍZO OPERACIONAL!
    if (cardLucro) {
      cardLucro.className = "kpi-card-transition bg-rose-50/80 dark:bg-rose-950/40 border-2 border-rose-500/80 rounded-2xl p-4 shadow-md shadow-rose-500/10 relative overflow-hidden group hover:border-rose-500 transition animate-pulse-alert";
    }
    if (lucroTitle) lucroTitle.textContent = "Prejuízo Comercial";
    if (lucroIconBox) {
      lucroIconBox.className = "w-8 h-8 rounded-xl bg-rose-200 dark:bg-rose-900 text-rose-700 dark:text-rose-200 flex items-center justify-center text-xs animate-bounce";
    }
    if (lucroIcon) lucroIcon.className = "fa-solid fa-triangle-exclamation";
    if (lucroEl) {
      lucroEl.className = "text-xl sm:text-2xl font-black text-rose-600 dark:text-rose-400 font-mono tracking-tight";
    }
    if (lucroDesc) {
      lucroDesc.innerHTML = `<i class="fa-solid fa-triangle-exclamation text-[9px] text-rose-500"></i> CMV excede receita em <strong class="text-rose-600 dark:text-rose-400">${formatMoney(Math.abs(totalLucro))}</strong>`;
      lucroDesc.className = "text-[11px] text-rose-600 dark:text-rose-400 mt-1 block font-bold";
    }
  }

  // Render Visual Charts
  renderVisualAnalytics(totalFaturamento, totalCustos, totalLucro, margemMedia);

  // Update tabs
  renderPipeline();
  renderHistorico();
  renderMargens();
  renderProdutos();
  renderClientes();
}"""

    idx_start = code.find(target_start)
    idx_end = code.find(target_end, idx_start)
    if idx_start != -1 and idx_end != -1:
        code = code[:idx_start] + new_engine + code[idx_end + len(target_end):]
    else:
        print("Error locating target region in crm-vendas/crm_vendas.js")

    # Update pipeline card profit/loss line
    old_card_profit = """        <div class="col-span-2 pt-1 border-t border-slate-200 dark:border-slate-800/60 flex items-center justify-between">
          <span class="text-slate-600 dark:text-slate-400">Lucro: <strong class="text-emerald-600 dark:text-emerald-400 font-bold">${formatMoney(venda.lucroLiquido)}</strong></span>
          <span class="text-cyan-600 dark:text-cyan-300 font-bold">${formatPercent(venda.margem)}</span>
        </div>"""

    new_card_profit = """        <div class="col-span-2 pt-1 border-t border-slate-200 dark:border-slate-800/60 flex items-center justify-between">
          <span class="text-slate-600 dark:text-slate-400">
            ${venda.lucroLiquido >= 0 ? 'Lucro:' : 'Prejuízo:'}
            <strong class="${venda.lucroLiquido >= 0 ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'} font-bold">
              ${venda.lucroLiquido >= 0 ? '▲ +' : '▼ -'}${formatMoney(Math.abs(venda.lucroLiquido))}
            </strong>
          </span>
          <span class="${venda.lucroLiquido >= 0 ? (venda.margem >= 40 ? 'text-emerald-600 dark:text-emerald-400' : 'text-cyan-600 dark:text-cyan-300') : 'text-rose-600 dark:text-rose-400 font-black'} font-bold">
            ${formatPercent(venda.margem)}
          </span>
        </div>"""

    if old_card_profit in code:
        code = code.replace(old_card_profit, new_card_profit)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print("crm-vendas/crm_vendas.js updated successfully.")

if __name__ == "__main__":
    update_crm_servicos_js()
    update_crm_vendas_js()
