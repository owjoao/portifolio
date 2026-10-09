// ============================================================
// NEXUS CRM SERVIÇOS - CORE ENGINE & DYNAMIC ADAPTABLE STATE
// ============================================================

const STORAGE_KEY = 'NEXUS_CRM_SERVICOS_V1';

// Default initial state (Demonstrating proportional consumable costs)
const DEFAULT_STATE = {
  config: {
    nomeEmpresa: "Clínica & Serviços Especializados",
    whatsappPadrao: "32999292311"
  },
  clientes: [
    { id: "c1", nome: "Dra. Juliana Ribeiro", telefone: "(32) 99929-2311", email: "juliana@exemplo.com", cidade: "Juiz de Fora - MG" },
    { id: "c2", nome: "Carlos Eduardo Mendes", telefone: "(32) 99929-2311", email: "carlos@exemplo.com", cidade: "Belo Horizonte - MG" },
    { id: "c3", nome: "Mariana Souza Lima", telefone: "(32) 99929-2311", email: "mariana@exemplo.com", cidade: "Rio de Janeiro - RJ" },
    { id: "c4", nome: "Felipe Albuquerque", telefone: "(32) 99929-2311", email: "felipe@exemplo.com", cidade: "São Paulo - SP" }
  ],
  insumos: [
    {
      id: "ins1",
      nome: "Pó de Bicarbonato de Sódio",
      tipoUnidade: "peso",
      unidadeCompra: "kg",
      qtdCompra: 1,
      precoCompra: 100.00,
      estoqueAtual: 4.5,
      estoqueMinimo: 1.0,
      unidadeBase: "g",
      custoPorUnidadeBase: 0.10 // R$ 100 / 1000g = R$ 0,10 por grama
    },
    {
      id: "ins2",
      nome: "Tubo de Pasta Profilática",
      tipoUnidade: "unidade",
      unidadeCompra: "un",
      qtdCompra: 1,
      precoCompra: 15.00,
      estoqueAtual: 12,
      estoqueMinimo: 3,
      unidadeBase: "un",
      custoPorUnidadeBase: 15.00 // R$ 15,00 por tubo
    },
    {
      id: "ins3",
      nome: "Kit Resina Fotopolimerizável",
      tipoUnidade: "peso",
      unidadeCompra: "g",
      qtdCompra: 4,
      precoCompra: 120.00,
      estoqueAtual: 16,
      estoqueMinimo: 4,
      unidadeBase: "g",
      custoPorUnidadeBase: 30.00 // R$ 120 / 4g = R$ 30,00 por grama
    },
    {
      id: "ins4",
      nome: "Solução Antisséptica / Higienizante",
      tipoUnidade: "volume",
      unidadeCompra: "l",
      qtdCompra: 1,
      precoCompra: 50.00,
      estoqueAtual: 3.5,
      estoqueMinimo: 1.0,
      unidadeBase: "ml",
      custoPorUnidadeBase: 0.05 // R$ 50 / 1000ml = R$ 0,05 por ml
    },
    {
      id: "ins5",
      nome: "Luvas & Descartáveis Cirúrgicos",
      tipoUnidade: "unidade",
      unidadeCompra: "cx",
      qtdCompra: 50, // 50 pares
      precoCompra: 45.00,
      estoqueAtual: 35,
      estoqueMinimo: 10,
      unidadeBase: "par",
      custoPorUnidadeBase: 0.90 // R$ 45 / 50 pares = R$ 0,90 por par
    }
  ],
  servicos: [
    {
      id: "s1",
      nome: "Limpeza & Profilaxia Completa",
      categoria: "Odontologia / Higiene",
      precoSugerido: 220.00,
      insumos: [
        { insumoId: "ins1", quantidade: 100, unidade: "g" }, // 100g de bicarbonato (10% de 1kg = R$ 10,00)
        { insumoId: "ins2", quantidade: 1, unidade: "un" },   // 1 tubo pasta profilática = R$ 15,00
        { insumoId: "ins5", quantidade: 1, unidade: "par" }   // 1 par de luvas = R$ 0,90
      ]
      // Custo Total Insumos: R$ 25,90 | Lucro: R$ 194,10 | Margem: 88,2%
    },
    {
      id: "s2",
      nome: "Restauração em Resina Composta",
      categoria: "Procedimento Restaurador",
      precoSugerido: 350.00,
      insumos: [
        { insumoId: "ins3", quantidade: 1.2, unidade: "g" }, // 1.2g de resina = R$ 36,00
        { insumoId: "ins4", quantidade: 20, unidade: "ml" },  // 20ml antisséptico = R$ 1,00
        { insumoId: "ins5", quantidade: 2, unidade: "par" }   // 2 pares luvas = R$ 1,80
      ]
      // Custo Total Insumos: R$ 38,80 | Lucro: R$ 311,20 | Margem: 88,9%
    },
    {
      id: "s3",
      nome: "Avaliação & Diagnóstico Clínico",
      categoria: "Consulta Inicial",
      precoSugerido: 150.00,
      insumos: [
        { insumoId: "ins4", quantidade: 15, unidade: "ml" },  // 15ml = R$ 0,75
        { insumoId: "ins5", quantidade: 1, unidade: "par" }   // 1 par = R$ 0,90
      ]
      // Custo Total Insumos: R$ 1,65 | Lucro: R$ 148,35 | Margem: 98,9%
    }
  ],
  atendimentos: [
    {
      id: "at1",
      clienteId: "c1",
      data: new Date(Date.now() - 2 * 86400000).toISOString(),
      servicoId: "s1",
      nomeServico: "Limpeza & Profilaxia Completa",
      status: "concluido",
      valorCobrado: 220.00,
      custoInsumos: 25.90,
      lucroLiquido: 194.10,
      margem: 88.2,
      insumosUtilizados: [
        { insumoId: "ins1", nome: "Pó de Bicarbonato", quantidade: 100, unidade: "g", custoCalculado: 10.00 },
        { insumoId: "ins2", nome: "Tubo Pasta Profilática", quantidade: 1, unidade: "un", custoCalculado: 15.00 },
        { insumoId: "ins5", nome: "Luvas Descartáveis", quantidade: 1, unidade: "par", custoCalculado: 0.90 }
      ],
      obs: "Paciente com gengiva saudável, retorno semestral agendado."
    },
    {
      id: "at2",
      clienteId: "c2",
      data: new Date(Date.now() - 1 * 86400000).toISOString(),
      servicoId: "s2",
      nomeServico: "Restauração em Resina Composta",
      status: "concluido",
      valorCobrado: 350.00,
      custoInsumos: 38.80,
      lucroLiquido: 311.20,
      margem: 88.9,
      insumosUtilizados: [
        { insumoId: "ins3", nome: "Kit Resina", quantidade: 1.2, unidade: "g", custoCalculado: 36.00 },
        { insumoId: "ins4", nome: "Solução Antisséptica", quantidade: 20, unidade: "ml", custoCalculado: 1.00 },
        { insumoId: "ins5", nome: "Luvas Descartáveis", quantidade: 2, unidade: "par", custoCalculado: 1.80 }
      ],
      obs: "Dente 14 restaurado com resina estética."
    },
    {
      id: "at3",
      clienteId: "c3",
      data: new Date().toISOString(),
      servicoId: "s1",
      nomeServico: "Limpeza & Profilaxia Completa",
      status: "execucao",
      valorCobrado: 220.00,
      custoInsumos: 25.90,
      lucroLiquido: 194.10,
      margem: 88.2,
      insumosUtilizados: [
        { insumoId: "ins1", nome: "Pó de Bicarbonato", quantidade: 100, unidade: "g", custoCalculado: 10.00 },
        { insumoId: "ins2", nome: "Tubo Pasta Profilática", quantidade: 1, unidade: "un", custoCalculado: 15.00 },
        { insumoId: "ins5", nome: "Luvas Descartáveis", quantidade: 1, unidade: "par", custoCalculado: 0.90 }
      ],
      obs: "Em atendimento no momento."
    },
    {
      id: "at4",
      clienteId: "c4",
      data: new Date(Date.now() + 86400000).toISOString(),
      servicoId: "s3",
      nomeServico: "Avaliação & Diagnóstico Clínico",
      status: "agendado",
      valorCobrado: 150.00,
      custoInsumos: 1.65,
      lucroLiquido: 148.35,
      margem: 98.9,
      insumosUtilizados: [
        { insumoId: "ins4", nome: "Solução Antisséptica", quantidade: 15, unidade: "ml", custoCalculado: 0.75 },
        { insumoId: "ins5", nome: "Luvas Descartáveis", quantidade: 1, unidade: "par", custoCalculado: 0.90 }
      ],
      obs: "Primeira consulta para plano de tratamento."
    }
  ]
};

// Application State
let appState = loadState();
let currentDateFilter = 'tudo';
let customDateStart = null;
let customDateEnd = null;

// ============================================================
// STORAGE & INITIALIZATION
// ============================================================
function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw);
  } catch (e) {
    console.error("Erro ao carregar localStorage:", e);
  }
  return JSON.parse(JSON.stringify(DEFAULT_STATE));
}

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
  } catch (e) {
    console.error("Erro ao salvar localStorage:", e);
  }
  updateAllViews();
}

function resetarDadosExemplo() {
  if (confirm("Tem certeza que deseja recarregar os dados de exemplo profissionais?")) {
    appState = JSON.parse(JSON.stringify(DEFAULT_STATE));
    saveState();
    closeModal('modal-config');
  }
}

function limparTodosDados() {
  if (confirm("ATENÇÃO: Deseja apagar todos os dados para começar do zero?")) {
    appState = {
      config: { nomeEmpresa: "Meu Negócio de Serviços", whatsappPadrao: "32999292311" },
      clientes: [],
      insumos: [],
      servicos: [],
      atendimentos: []
    };
    saveState();
    closeModal('modal-config');
  }
}

// ============================================================
// UNIT CONVERSION & PROPORTIONAL COST ENGINE
// ============================================================
// Calculates the base unit and cost per base unit (e.g. per gram, per ml, per single item)
function calcularCustoUnitarioBase(tipoUnidade, unidadeCompra, qtdCompra, precoCompra) {
  qtdCompra = parseFloat(qtdCompra) || 1;
  precoCompra = parseFloat(precoCompra) || 0;
  if (qtdCompra <= 0) qtdCompra = 1;

  let unidadeBase = 'un';
  let custoPorUnidadeBase = 0;

  if (tipoUnidade === 'peso') {
    // Base unit: gramas (g)
    unidadeBase = 'g';
    let qtdEmGramas = qtdCompra;
    if (unidadeCompra === 'kg') qtdEmGramas = qtdCompra * 1000;
    else if (unidadeCompra === 'mg') qtdEmGramas = qtdCompra / 1000;
    else qtdEmGramas = qtdCompra; // já em g

    custoPorUnidadeBase = precoCompra / (qtdEmGramas || 1);
  } 
  else if (tipoUnidade === 'volume') {
    // Base unit: mililitros (ml)
    unidadeBase = 'ml';
    let qtdEmMl = qtdCompra;
    if (unidadeCompra === 'l') qtdEmMl = qtdCompra * 1000;
    else qtdEmMl = qtdCompra; // já em ml

    custoPorUnidadeBase = precoCompra / (qtdEmMl || 1);
  } 
  else {
    // Base unit: unidades / peças
    unidadeBase = unidadeCompra || 'un';
    custoPorUnidadeBase = precoCompra / qtdCompra;
  }

  return { unidadeBase, custoPorUnidadeBase };
}

// Converts a consumed quantity to cost in R$
function calcularCustoConsumo(insumo, quantidadeConsumida, unidadeConsumida) {
  if (!insumo) return 0;
  quantidadeConsumida = parseFloat(quantidadeConsumida) || 0;
  const baseCost = insumo.custoPorUnidadeBase || 0;

  if (insumo.tipoUnidade === 'peso') {
    let emGramas = quantidadeConsumida;
    if (unidadeConsumida === 'kg') emGramas = quantidadeConsumida * 1000;
    else if (unidadeConsumida === 'mg') emGramas = quantidadeConsumida / 1000;
    return emGramas * baseCost;
  } 
  else if (insumo.tipoUnidade === 'volume') {
    let emMl = quantidadeConsumida;
    if (unidadeConsumida === 'l') emMl = quantidadeConsumida * 1000;
    return emMl * baseCost;
  } 
  else {
    return quantidadeConsumida * baseCost;
  }
}

// ============================================================
// FORMATTERS
// ============================================================
function formatMoney(val) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(val || 0);
}

function formatDate(isoStr) {
  if (!isoStr) return '-';
  const d = new Date(isoStr);
  return d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' });
}

function formatPercent(val) {
  return (val || 0).toFixed(1) + '%';
}

// ============================================================
// DATE FILTERING LOGIC
// ============================================================
function setDateFilter(filterType) {
  currentDateFilter = filterType;
  customDateStart = null;
  customDateEnd = null;
  document.getElementById('filter-date-start').value = '';
  document.getElementById('filter-date-end').value = '';

  document.querySelectorAll('.df-btn').forEach(btn => {
    btn.className = 'df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium';
  });
  const activeBtn = document.getElementById(`df-${filterType}`);
  if (activeBtn) {
    activeBtn.className = 'df-btn px-2.5 py-1 rounded bg-cyan-950 text-cyan-300 border border-cyan-800/80 font-medium';
  }

  updateAllViews();
}

function applyCustomDateFilter() {
  const s = document.getElementById('filter-date-start').value;
  const e = document.getElementById('filter-date-end').value;
  if (s || e) {
    currentDateFilter = 'custom';
    customDateStart = s ? new Date(s + 'T00:00:00') : null;
    customDateEnd = e ? new Date(e + 'T23:59:59') : null;

    document.querySelectorAll('.df-btn').forEach(btn => {
      btn.className = 'df-btn px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 font-medium';
    });
    updateAllViews();
  }
}

function clearDateFilter() {
  setDateFilter('tudo');
}

function isDateInFilter(dateStr) {
  if (currentDateFilter === 'tudo') return true;
  if (!dateStr) return false;
  const d = new Date(dateStr);
  const now = new Date();

  if (currentDateFilter === 'hoje') {
    return d.toDateString() === now.toDateString();
  }
  if (currentDateFilter === '7d') {
    const limit = new Date(now.getTime() - 7 * 86400000);
    return d >= limit && d <= now;
  }
  if (currentDateFilter === '30d') {
    const limit = new Date(now.getTime() - 30 * 86400000);
    return d >= limit && d <= now;
  }
  if (currentDateFilter === 'mes') {
    return d.getMonth() === now.getMonth() && d.getFullYear() === now.getFullYear();
  }
  if (currentDateFilter === 'custom') {
    if (customDateStart && d < customDateStart) return false;
    if (customDateEnd && d > customDateEnd) return false;
    return true;
  }
  return true;
}

function getFilteredAtendimentos() {
  return appState.atendimentos.filter(a => isDateInFilter(a.data));
}

// ============================================================
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
}

// ============================================================
// THEME SWITCHING (Dark / Light)
// ============================================================
const THEME_STORAGE_KEY = 'NEXUS_CRM_THEME';

function initTheme() {
  const saved = localStorage.getItem(THEME_STORAGE_KEY) || 'dark';
  applyTheme(saved);
}

function applyTheme(theme) {
  const html = document.documentElement;
  const icon = document.getElementById('theme-icon');
  const label = document.getElementById('theme-label');

  if (theme === 'light') {
    html.classList.remove('dark');
    if (icon) icon.className = 'fa-solid fa-moon text-amber-500';
    if (label) label.textContent = 'Modo Claro Ativo';
    localStorage.setItem(THEME_STORAGE_KEY, 'light');
  } else {
    html.classList.add('dark');
    if (icon) icon.className = 'fa-solid fa-sun text-amber-400';
    if (label) label.textContent = 'Modo Escuro Ativo';
    localStorage.setItem(THEME_STORAGE_KEY, 'dark');
  }
}

function toggleTheme() {
  const isDark = document.documentElement.classList.contains('dark');
  applyTheme(isDark ? 'light' : 'dark');
}

// ============================================================
// TAB NAVIGATION
// ============================================================
const TAB_DESCRIPTIONS_SERVICOS = {
  funil: { title: "Pipeline de Atendimentos", desc: "Arraste os cards para atualizar o status do procedimento" },
  historico: { title: "Histórico de Movimentações & Caixa", desc: "Auditoria detalhada com receitas, custos e lucros apurados" },
  margens: { title: "Comparativo de Margens de Lucro", desc: "Ranking de rentabilidade dos procedimentos cadastrados" },
  servicos: { title: "Catálogo de Serviços & Procedimentos", desc: "Gerencie procedimentos e composição técnica de consumo" },
  insumos: { title: "Estoque de Insumos & Custos Unitários", desc: "Controle de materiais com conversão proporcional por kg, g, mg, L ou ml" },
  clientes: { title: "Base de Clientes & Contatos", desc: "Cadastre e edite clientes com canal direto via WhatsApp" }
};

function switchTab(tabId) {
  document.querySelectorAll('.tab-pane').forEach(el => el.classList.add('hidden'));
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.className = 'tab-btn w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800/70 hover:text-slate-900 dark:hover:text-slate-200 border border-transparent';
  });

  const content = document.getElementById(`tab-content-${tabId}`);
  const btn = document.getElementById(`tab-btn-${tabId}`);
  if (content) content.classList.remove('hidden');
  if (btn) {
    btn.className = 'tab-btn w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl font-bold transition text-cyan-700 dark:text-cyan-400 bg-cyan-50 dark:bg-cyan-950/70 border border-cyan-200 dark:border-cyan-800/60 shadow-sm';
  }

  const meta = TAB_DESCRIPTIONS_SERVICOS[tabId];
  if (meta) {
    const titleEl = document.getElementById('topbar-view-title');
    const descEl = document.getElementById('topbar-view-desc');
    if (titleEl) titleEl.textContent = meta.title;
    if (descEl) descEl.textContent = meta.desc;
  }
}

// ============================================================
// TAB 1: KANBAN BOARD
// ============================================================
function renderKanban() {
  const searchTerm = (document.getElementById('search-funil')?.value || '').toLowerCase();
  const cols = {
    novo: document.getElementById('kanban-col-novo'),
    agendado: document.getElementById('kanban-col-agendado'),
    execucao: document.getElementById('kanban-col-execucao'),
    concluido: document.getElementById('kanban-col-concluido'),
    cancelado: document.getElementById('kanban-col-cancelado'),
  };

  // Clear columns
  Object.values(cols).forEach(col => { if (col) col.innerHTML = ''; });
  const counts = { novo: 0, agendado: 0, execucao: 0, concluido: 0, cancelado: 0 };

  const filtered = getFilteredAtendimentos();

  filtered.forEach(atend => {
    const cliente = appState.clientes.find(c => c.id === atend.clienteId) || { nome: 'Cliente não informado', telefone: '' };
    const servico = appState.servicos.find(s => s.id === atend.servicoId) || { nome: atend.nomeServico || 'Serviço Personalizado' };

    // Search filter
    if (searchTerm) {
      const matchClient = cliente.nome.toLowerCase().includes(searchTerm);
      const matchServ = servico.nome.toLowerCase().includes(searchTerm);
      if (!matchClient && !matchServ) return;
    }

    const st = atend.status || 'novo';
    if (counts[st] !== undefined) counts[st]++;

    const col = cols[st];
    if (!col) return;

    // Direct WhatsApp message link
    const cleanPhone = cliente.telefone.replace(/\D/g, '');
    const waUrl = `https://wa.me/${cleanPhone || appState.config.whatsappPadrao || '5532999292311'}?text=${encodeURIComponent(`Olá ${cliente.nome}, referente ao seu atendimento de ${servico.nome}...`)}`;

    const card = document.createElement('div');
    card.className = "bg-white dark:bg-slate-900/90 border border-slate-200/90 dark:border-slate-800 hover:border-cyan-500/50 rounded-xl p-3 shadow-sm dark:shadow-md space-y-2.5 transition group";
    card.innerHTML = `
      <div class="flex items-start justify-between gap-2">
        <div>
          <span class="font-bold text-slate-800 dark:text-white text-xs block">${cliente.nome}</span>
          <span class="text-[11px] text-cyan-600 dark:text-cyan-400 font-semibold">${servico.nome}</span>
        </div>
        <div class="flex items-center gap-1">
          <a href="${waUrl}" target="_blank" class="w-6 h-6 rounded bg-emerald-100 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-400 hover:bg-emerald-200 dark:hover:bg-emerald-800 flex items-center justify-center text-[11px] transition" title="Chamar no WhatsApp">
            <i class="fa-brands fa-whatsapp"></i>
          </a>
          <button onclick="editarAtendimento('${atend.id}')" class="w-6 h-6 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-cyan-600 dark:hover:text-cyan-400 flex items-center justify-center text-[10px] transition" title="Editar atendimento">
            <i class="fa-solid fa-pen"></i>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-1 py-1.5 px-2 bg-slate-50 dark:bg-slate-950/60 rounded-lg border border-slate-200/80 dark:border-slate-800/80 text-[10px] font-mono">
        <div>
          <span class="text-slate-500 dark:text-slate-400 block">Cobrado:</span>
          <span class="text-slate-900 dark:text-white font-bold">${formatMoney(atend.valorCobrado)}</span>
        </div>
        <div>
          <span class="text-slate-500 dark:text-slate-400 block">Insumos:</span>
          <span class="text-amber-600 dark:text-amber-400 font-bold">${formatMoney(atend.custoInsumos)}</span>
        </div>
        <div class="col-span-2 pt-1 border-t border-slate-200 dark:border-slate-800/60 flex items-center justify-between">
          <span class="text-slate-600 dark:text-slate-400">
            ${atend.lucroLiquido >= 0 ? 'Lucro:' : 'Prejuízo:'}
            <strong class="${atend.lucroLiquido >= 0 ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'} font-bold">
              ${atend.lucroLiquido >= 0 ? '▲ +' : '▼ -'}${formatMoney(Math.abs(atend.lucroLiquido))}
            </strong>
          </span>
          <span class="${atend.lucroLiquido >= 0 ? (atend.margem >= 50 ? 'text-emerald-600 dark:text-emerald-400' : 'text-cyan-600 dark:text-cyan-300') : 'text-rose-600 dark:text-rose-400 font-black'} font-bold">
            ${formatPercent(atend.margem)}
          </span>
        </div>
      </div>

      <div class="flex items-center justify-between text-[10px] text-slate-500 dark:text-slate-400 pt-1">
        <span><i class="fa-regular fa-clock mr-1"></i>${formatDate(atend.data).split(' ')[0]}</span>
        
        <!-- Status quick changer -->
        <select onchange="mudarStatusAtendimento('${atend.id}', this.value)" class="bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 rounded px-1.5 py-0.5 text-[10px] outline-none">
          <option value="novo" ${st === 'novo' ? 'selected' : ''}>1. Novo</option>
          <option value="agendado" ${st === 'agendado' ? 'selected' : ''}>2. Agendado</option>
          <option value="execucao" ${st === 'execucao' ? 'selected' : ''}>3. Execução</option>
          <option value="concluido" ${st === 'concluido' ? 'selected' : ''}>4. Concluído</option>
          <option value="cancelado" ${st === 'cancelado' ? 'selected' : ''}>5. Cancelado</option>
        </select>
      </div>
    `;

    col.appendChild(card);
  });

  // Update counts
  document.getElementById('col-count-novo').textContent = counts.novo;
  document.getElementById('col-count-agendado').textContent = counts.agendado;
  document.getElementById('col-count-execucao').textContent = counts.execucao;
  document.getElementById('col-count-concluido').textContent = counts.concluido;
  document.getElementById('col-count-cancelado').textContent = counts.cancelado;
}

function mudarStatusAtendimento(id, novoStatus) {
  const atend = appState.atendimentos.find(a => a.id === id);
  if (atend) {
    atend.status = novoStatus;
    saveState();
  }
}

// ============================================================
// TAB 2: HISTÓRICO DE MOVIMENTAÇÕES (LEDGER)
// ============================================================
function renderHistorico() {
  const tbody = document.getElementById('historico-tbody');
  const empty = document.getElementById('historico-empty');
  const searchTerm = (document.getElementById('search-historico')?.value || '').toLowerCase();
  if (!tbody) return;

  tbody.innerHTML = '';
  const filtered = getFilteredAtendimentos();

  const sorted = [...filtered].sort((a, b) => new Date(b.data) - new Date(a.data));

  let visibleCount = 0;
  sorted.forEach(atend => {
    const cliente = appState.clientes.find(c => c.id === atend.clienteId) || { nome: 'Cliente não informado', telefone: '' };
    const servico = appState.servicos.find(s => s.id === atend.servicoId) || { nome: atend.nomeServico || 'Serviço' };

    if (searchTerm) {
      const match = cliente.nome.toLowerCase().includes(searchTerm) || servico.nome.toLowerCase().includes(searchTerm);
      if (!match) return;
    }

    visibleCount++;
    const tr = document.createElement('tr');
    tr.className = "hover:bg-slate-50 dark:hover:bg-slate-900/60 transition";

    const insumosResumo = (atend.insumosUtilizados || []).map(i => `${i.nome}: ${i.quantidade}${i.unidade} (${formatMoney(i.custoCalculado)})`).join(', ') || 'Nenhum insumo registrado';

    const statusBadges = {
      novo: '<span class="px-2 py-0.5 bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-400 border border-blue-300 dark:border-blue-800/40 rounded text-[10px] whitespace-nowrap">Novo Contato</span>',
      agendado: '<span class="px-2 py-0.5 bg-cyan-100 dark:bg-cyan-950 text-cyan-700 dark:text-cyan-400 border border-cyan-300 dark:border-cyan-800/40 rounded text-[10px] whitespace-nowrap">Agendado</span>',
      execucao: '<span class="px-2 py-0.5 bg-amber-100 dark:bg-amber-950 text-amber-700 dark:text-amber-400 border border-amber-300 dark:border-amber-800/40 rounded text-[10px] whitespace-nowrap">Em Execução</span>',
      concluido: '<span class="px-2 py-0.5 bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800/40 rounded text-[10px] whitespace-nowrap">Concluído</span>',
      cancelado: '<span class="px-2 py-0.5 bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-400 border border-rose-300 dark:border-rose-800/40 rounded text-[10px] whitespace-nowrap">Cancelado</span>'
    };

    tr.innerHTML = `
      <td class="py-3 px-3 font-mono text-[11px] text-slate-500 dark:text-slate-400 whitespace-nowrap">${formatDate(atend.data)}</td>
      <td class="py-3 px-3 font-bold text-slate-900 dark:text-white">${cliente.nome}</td>
      <td class="py-3 px-3 font-semibold text-cyan-600 dark:text-cyan-400">${servico.nome}</td>
      <td class="py-3 px-3 text-slate-600 dark:text-slate-300 text-[11px] max-w-xs truncate" title="${insumosResumo}">
        ${insumosResumo}
      </td>
      <td class="py-3 px-3 text-right font-mono font-bold text-slate-900 dark:text-white whitespace-nowrap">${formatMoney(atend.valorCobrado)}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-amber-600 dark:text-amber-400 whitespace-nowrap">${formatMoney(atend.custoInsumos)}</td>
      <td class="py-3 px-3 text-right font-mono font-bold ${atend.lucroLiquido >= 0 ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400 font-black'} whitespace-nowrap">${atend.lucroLiquido >= 0 ? '+' : '-'}${formatMoney(Math.abs(atend.lucroLiquido))}</td>
      <td class="py-3 px-3 text-center font-mono font-bold ${atend.lucroLiquido >= 0 ? 'text-cyan-600 dark:text-cyan-300' : 'text-rose-600 dark:text-rose-400 font-black'} whitespace-nowrap">${formatPercent(atend.margem)}</td>
      <td class="py-3 px-3 text-center whitespace-nowrap">${statusBadges[atend.status] || atend.status}</td>
      <td class="py-3 px-3 text-center whitespace-nowrap">
        <div class="flex items-center justify-center gap-1.5">
          <button onclick="editarAtendimento('${atend.id}')" class="p-1 rounded text-slate-400 hover:text-cyan-500" title="Editar">
            <i class="fa-solid fa-pen-to-square"></i>
          </button>
          <button onclick="excluirAtendimento('${atend.id}')" class="p-1 rounded text-slate-400 hover:text-rose-500" title="Excluir">
            <i class="fa-solid fa-trash-can"></i>
          </button>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  });

  if (empty) empty.classList.toggle('hidden', visibleCount > 0);
}

function exportarHistoricoCSV() {
  const filtered = getFilteredAtendimentos();
  if (filtered.length === 0) {
    alert("Nenhuma movimentação para exportar.");
    return;
  }

  let csv = "Data;Cliente;Telefone;Servico;Valor Cobrado;Custo Insumos;Lucro Liquido;Margem %;Status;Observacoes\n";
  filtered.forEach(a => {
    const c = appState.clientes.find(cli => cli.id === a.clienteId) || { nome: '-', telefone: '-' };
    const s = appState.servicos.find(ser => ser.id === a.servicoId) || { nome: a.nomeServico || '-' };
    csv += `"${formatDate(a.data)}";"${c.nome}";"${c.telefone}";"${s.nome}";"${a.valorCobrado}";"${a.custoInsumos}";"${a.lucroLiquido}";"${a.margem}";"${a.status}";"${(a.obs || '').replace(/"/g, '""')}"\n`;
  });

  const blob = new Blob(["\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", `historico_movimentacoes_servicos_${new Date().toISOString().split('T')[0]}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// ============================================================
// TAB 3: ANÁLISE DE MARGENS & PERFORMANCE
// ============================================================
function renderMargens() {
  const grid = document.getElementById('margens-grid');
  const sortType = document.getElementById('sort-margens')?.value || 'melhor_margem';
  if (!grid) return;

  grid.innerHTML = '';
  const filtered = getFilteredAtendimentos();
  const faturados = filtered.filter(a => a.status === 'concluido');

  // Compute metrics for each service in the catalog
  const performance = appState.servicos.map(serv => {
    const atendimentosDoServico = faturados.filter(a => a.servicoId === serv.id);
    const volume = atendimentosDoServico.length;
    const faturamentoTotal = atendimentosDoServico.reduce((acc, a) => acc + (a.valorCobrado || 0), 0);
    const custoInsumosTotal = atendimentosDoServico.reduce((acc, a) => acc + (a.custoInsumos || 0), 0);
    const lucroTotal = faturamentoTotal - custoInsumosTotal;
    const margemMedia = faturamentoTotal > 0 ? (lucroTotal / faturamentoTotal) * 100 : 0;

    // Ficha técnica baseline
    const custoBaseFicha = (serv.insumos || []).reduce((acc, item) => {
      const ins = appState.insumos.find(i => i.id === item.insumoId);
      return acc + calcularCustoConsumo(ins, item.quantidade, item.unidade);
    }, 0);
    const lucroBaseFicha = serv.precoSugerido - custoBaseFicha;
    const margemBaseFicha = serv.precoSugerido > 0 ? (lucroBaseFicha / serv.precoSugerido) * 100 : 0;

    return {
      servico: serv,
      volume,
      faturamentoTotal,
      custoInsumosTotal,
      lucroTotal,
      margemMedia: volume > 0 ? margemMedia : margemBaseFicha,
      custoBaseFicha,
      lucroBaseFicha,
      margemBaseFicha
    };
  });

  // Sort
  if (sortType === 'melhor_margem') {
    performance.sort((a, b) => b.margemMedia - a.margemMedia);
  } else if (sortType === 'maior_lucro') {
    performance.sort((a, b) => b.lucroTotal - a.lucroTotal);
  } else if (sortType === 'mais_realizados') {
    performance.sort((a, b) => b.volume - a.volume);
  } else if (sortType === 'maior_faturamento') {
    performance.sort((a, b) => b.faturamentoTotal - a.faturamentoTotal);
  } else if (sortType === 'maior_custo') {
    performance.sort((a, b) => b.custoBaseFicha - a.custoBaseFicha);
  }

  performance.forEach((p, idx) => {
    const isTop1 = idx === 0 && p.margemMedia > 0;
    const isLowMargin = p.margemMedia < 40 && p.servico.precoSugerido > 0;

    const card = document.createElement('div');
    card.className = `bg-white dark:bg-slate-900/80 border ${isTop1 ? 'border-emerald-500 shadow-md shadow-emerald-500/10' : 'border-slate-200 dark:border-slate-800'} rounded-2xl p-5 space-y-4 relative overflow-hidden transition group hover:border-cyan-500`;
    
    // Top highlight badge
    let topBadge = '';
    if (isTop1) {
      topBadge = '<span class="absolute top-3 right-3 px-2 py-0.5 bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800 text-[10px] font-bold rounded-full flex items-center gap-1"><i class="fa-solid fa-crown text-[9px]"></i> Líder em Margem</span>';
    } else if (isLowMargin) {
      topBadge = '<span class="absolute top-3 right-3 px-2 py-0.5 bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-400 border border-rose-300 dark:border-rose-800 text-[10px] font-bold rounded-full">⚠️ Margem Baixa</span>';
    }

    card.innerHTML = `
      ${topBadge}
      <div>
        <span class="text-[10px] font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">${p.servico.categoria || 'Geral'}</span>
        <h3 class="text-base font-extrabold text-slate-900 dark:text-white group-hover:text-cyan-600 dark:group-hover:text-cyan-400 transition">${p.servico.nome}</h3>
      </div>

      <!-- Margin Meter -->
      <div>
        <div class="flex items-center justify-between text-xs font-mono mb-1">
          <span class="text-slate-600 dark:text-slate-400 font-sans font-medium">Margem Líquida:</span>
          <strong class="text-base ${p.margemMedia >= 70 ? 'text-emerald-600 dark:text-emerald-400' : p.margemMedia >= 40 ? 'text-cyan-600 dark:text-cyan-400' : 'text-amber-600 dark:text-amber-400'}">${formatPercent(p.margemMedia)}</strong>
        </div>
        <div class="w-full bg-slate-100 dark:bg-slate-950 h-2.5 rounded-full overflow-hidden border border-slate-200 dark:border-slate-800">
          <div class="h-full rounded-full transition-all duration-500 ${p.margemMedia >= 70 ? 'bg-gradient-to-r from-cyan-500 to-emerald-500' : p.margemMedia >= 40 ? 'bg-cyan-500' : 'bg-amber-500'}" style="width: ${Math.min(100, Math.max(0, p.margemMedia))}%"></div>
        </div>
      </div>

      <!-- Unit breakdown -->
      <div class="grid grid-cols-2 gap-2 p-3 bg-slate-50 dark:bg-slate-950/80 rounded-xl border border-slate-200/80 dark:border-slate-800 text-xs font-mono">
        <div>
          <span class="text-[10px] text-slate-500 dark:text-slate-400 block font-sans">Preço Cobrado:</span>
          <span class="text-slate-900 dark:text-white font-bold">${formatMoney(p.servico.precoSugerido)}</span>
        </div>
        <div>
          <span class="text-[10px] text-slate-500 dark:text-slate-400 block font-sans">Custo de Insumos:</span>
          <span class="text-amber-600 dark:text-amber-400 font-bold">${formatMoney(p.custoBaseFicha)}</span>
        </div>
        <div class="pt-2 border-t border-slate-200 dark:border-slate-800">
          <span class="text-[10px] text-slate-500 dark:text-slate-400 block font-sans">Lucro por Atend.:</span>
          <span class="text-emerald-600 dark:text-emerald-400 font-bold">${formatMoney(p.lucroBaseFicha)}</span>
        </div>
        <div class="pt-2 border-t border-slate-200 dark:border-slate-800">
          <span class="text-[10px] text-slate-500 dark:text-slate-400 block font-sans">Volume no Período:</span>
          <span class="text-slate-800 dark:text-slate-200 font-bold">${p.volume} realizados</span>
        </div>
      </div>

      <div class="flex items-center justify-between text-xs pt-1">
        <span class="text-slate-600 dark:text-slate-400">Lucro Total Gerado: <strong class="text-emerald-600 dark:text-emerald-400 font-mono">${formatMoney(p.lucroTotal)}</strong></span>
        <button onclick="editarServico('${p.servico.id}')" class="text-xs font-semibold text-cyan-600 dark:text-cyan-400 hover:underline">Ver Ficha Técnica →</button>
      </div>
    `;

    grid.appendChild(card);
  });
}

// ============================================================
// TAB 4: CATÁLOGO DE SERVIÇOS & FICHAS TÉCNICAS
// ============================================================
function renderServicos() {
  const container = document.getElementById('servicos-list');
  if (!container) return;
  container.innerHTML = '';

  appState.servicos.forEach(serv => {
    const card = document.createElement('div');
    card.className = "bg-slate-950/90 border border-slate-800 rounded-xl p-4 space-y-3 hover:border-cyan-500/50 transition";

    let insumosHtml = '';
    let totalCustoInsumos = 0;

    (serv.insumos || []).forEach(item => {
      const ins = appState.insumos.find(i => i.id === item.insumoId);
      const custo = calcularCustoConsumo(ins, item.quantidade, item.unidade);
      totalCustoInsumos += custo;
      insumosHtml += `
        <li class="flex items-center justify-between text-[11px] py-1 border-b border-slate-800/60 last:border-0">
          <span class="text-slate-300">• ${ins ? ins.nome : 'Insumo'}: <strong>${item.quantidade} ${item.unidade}</strong></span>
          <span class="text-amber-400 font-mono">${formatMoney(custo)}</span>
        </li>
      `;
    });

    const lucroEstimado = serv.precoSugerido - totalCustoInsumos;
    const margem = serv.precoSugerido > 0 ? (lucroEstimado / serv.precoSugerido) * 100 : 0;

    card.innerHTML = `
      <div class="flex items-start justify-between">
        <div>
          <span class="text-[10px] text-cyan-400 font-semibold uppercase">${serv.categoria || 'Serviço'}</span>
          <h3 class="font-extrabold text-white text-sm">${serv.nome}</h3>
        </div>
        <div class="flex items-center gap-1">
          <button onclick="editarServico('${serv.id}')" class="p-1 text-slate-400 hover:text-cyan-400 text-xs"><i class="fa-solid fa-pen"></i></button>
          <button onclick="excluirServico('${serv.id}')" class="p-1 text-slate-400 hover:text-rose-400 text-xs"><i class="fa-solid fa-trash-can"></i></button>
        </div>
      </div>

      <div class="p-2.5 bg-slate-900/80 rounded-lg border border-slate-800/80 space-y-1">
        <span class="text-[10px] text-slate-400 font-bold uppercase block">Ficha Técnica de Insumos:</span>
        <ul class="space-y-0.5">
          ${insumosHtml || '<li class="text-[11px] text-slate-500 italic">Nenhum insumo vinculado a esta ficha</li>'}
        </ul>
      </div>

      <div class="grid grid-cols-3 gap-1 text-center font-mono text-[11px] pt-1">
        <div class="p-1.5 bg-slate-900 rounded border border-slate-800">
          <span class="text-[9px] text-slate-400 block">Cobrado</span>
          <span class="font-bold text-white">${formatMoney(serv.precoSugerido)}</span>
        </div>
        <div class="p-1.5 bg-slate-900 rounded border border-slate-800">
          <span class="text-[9px] text-slate-400 block">Custos</span>
          <span class="font-bold text-amber-400">${formatMoney(totalCustoInsumos)}</span>
        </div>
        <div class="p-1.5 bg-slate-900 rounded border border-slate-800">
          <span class="text-[9px] text-slate-400 block">Margem</span>
          <span class="font-bold text-emerald-400">${formatPercent(margem)}</span>
        </div>
      </div>
    `;

    container.appendChild(card);
  });
}

// ============================================================
// TAB 5: INSUMOS & ESTOQUE (PROPORCIONALIDADE)
// ============================================================
function renderInsumos() {
  const tbody = document.getElementById('insumos-tbody');
  if (!tbody) return;
  tbody.innerHTML = '';

  appState.insumos.forEach(ins => {
    const tr = document.createElement('tr');
    tr.className = "hover:bg-slate-900/60 transition";

    let exemploFracao = '';
    if (ins.tipoUnidade === 'peso') {
      exemploFracao = `100g = <strong class="text-amber-400">${formatMoney(calcularCustoConsumo(ins, 100, 'g'))}</strong>`;
    } else if (ins.tipoUnidade === 'volume') {
      exemploFracao = `100ml = <strong class="text-amber-400">${formatMoney(calcularCustoConsumo(ins, 100, 'ml'))}</strong>`;
    } else {
      exemploFracao = `1 ${ins.unidadeBase} = <strong class="text-amber-400">${formatMoney(ins.custoPorUnidadeBase)}</strong>`;
    }

    const alertaEstoque = ins.estoqueAtual <= ins.estoqueMinimo;

    tr.innerHTML = `
      <td class="py-3 px-3 font-bold text-white flex items-center gap-2">
        <i class="fa-solid fa-box text-cyan-500/70"></i>
        <span>${ins.nome}</span>
      </td>
      <td class="py-3 px-3 text-slate-300 font-semibold uppercase text-[11px]">${ins.tipoUnidade}</td>
      <td class="py-3 px-3 font-mono">${ins.qtdCompra} ${ins.unidadeCompra}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-white">${formatMoney(ins.precoCompra)}</td>
      <td class="py-3 px-3 text-right font-mono text-cyan-300">
        ${formatMoney(ins.custoPorUnidadeBase)} / ${ins.unidadeBase}
      </td>
      <td class="py-3 px-3 text-center font-mono text-[11px]">${exemploFracao}</td>
      <td class="py-3 px-3 text-center">
        <span class="px-2 py-0.5 rounded font-mono font-bold text-xs ${alertaEstoque ? 'bg-rose-950 text-rose-400 border border-rose-800' : 'bg-slate-800 text-slate-200'}">
          ${ins.estoqueAtual} ${ins.unidadeCompra}
        </span>
      </td>
      <td class="py-3 px-3 text-center">
        <div class="flex items-center justify-center gap-1.5">
          <button onclick="editarInsumo('${ins.id}')" class="p-1 rounded text-slate-400 hover:text-cyan-400" title="Editar Insumo">
            <i class="fa-solid fa-pen-to-square"></i>
          </button>
          <button onclick="excluirInsumo('${ins.id}')" class="p-1 rounded text-slate-400 hover:text-rose-400" title="Excluir Insumo">
            <i class="fa-solid fa-trash-can"></i>
          </button>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

// ============================================================
// TAB 6: CLIENTES
// ============================================================
function renderClientes() {
  const container = document.getElementById('clientes-list');
  if (!container) return;
  container.innerHTML = '';

  appState.clientes.forEach(cli => {
    const atendimentosDoCliente = appState.atendimentos.filter(a => a.clienteId === cli.id);
    const totalGasto = atendimentosDoCliente.filter(a => a.status === 'concluido').reduce((acc, a) => acc + (a.valorCobrado || 0), 0);
    const totalLucro = atendimentosDoCliente.filter(a => a.status === 'concluido').reduce((acc, a) => acc + (a.lucroLiquido || 0), 0);

    const cleanPhone = (cli.telefone || '').replace(/\D/g, '');
    const waUrl = `https://wa.me/${cleanPhone || appState.config.whatsappPadrao || '5532999292311'}?text=${encodeURIComponent(`Olá ${cli.nome}, tudo bem?`)}`;

    const card = document.createElement('div');
    card.className = "bg-slate-950/90 border border-slate-800 rounded-xl p-4 space-y-3 hover:border-cyan-500/50 transition";
    card.innerHTML = `
      <div class="flex items-start justify-between">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-full bg-cyan-950 text-cyan-400 flex items-center justify-center font-bold text-xs border border-cyan-800/60">
            ${cli.nome.charAt(0).toUpperCase()}
          </div>
          <div>
            <h3 class="font-extrabold text-white text-sm">${cli.nome}</h3>
            <span class="text-xs text-slate-400 font-mono">${cli.telefone}</span>
          </div>
        </div>
        <div class="flex items-center gap-1">
          <a href="${waUrl}" target="_blank" class="w-7 h-7 rounded bg-emerald-950/80 text-emerald-400 hover:bg-emerald-800 flex items-center justify-center text-xs" title="Conversar no WhatsApp">
            <i class="fa-brands fa-whatsapp"></i>
          </a>
          <button onclick="editarCliente('${cli.id}')" class="w-7 h-7 rounded bg-slate-800 text-slate-300 hover:text-cyan-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-pen"></i>
          </button>
          <button onclick="excluirCliente('${cli.id}')" class="w-7 h-7 rounded bg-slate-800 text-slate-300 hover:text-rose-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-trash"></i>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-2 p-2 bg-slate-900 rounded-lg text-[11px] font-mono">
        <div>
          <span class="text-slate-400 block">Total Investido:</span>
          <span class="text-white font-bold">${formatMoney(totalGasto)}</span>
        </div>
        <div>
          <span class="text-slate-400 block">Lucro Gerado:</span>
          <span class="text-emerald-400 font-bold">${formatMoney(totalLucro)}</span>
        </div>
      </div>

      <div class="text-[11px] text-slate-400 flex items-center justify-between">
        <span>${cli.cidade || 'Localização não informada'}</span>
        <span>${atendimentosDoCliente.length} atendimentos</span>
      </div>
    `;
    container.appendChild(card);
  });
}

// ============================================================
// MODAL CONTROLLERS & CRUD ACTIONS
// ============================================================
function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove('hidden');
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('hidden');
}

// --- ATENDIMENTO MODAL ---
function openNovoAtendimentoModal() {
  document.getElementById('modal-atendimento-title').innerHTML = '<i class="fa-solid fa-calendar-check text-cyan-400"></i> Registrar Atendimento';
  document.getElementById('atend-id').value = '';
  document.getElementById('atend-data').value = new Date().toISOString().slice(0, 16);
  document.getElementById('atend-obs').value = '';

  popularSelectClientesAtendimento();
  popularSelectServicosAtendimento();

  onServicoSelecionadoNoAtendimento();
  openModal('modal-atendimento');
}

function popularSelectClientesAtendimento(selectedId) {
  const sel = document.getElementById('atend-cliente');
  if (!sel) return;
  sel.innerHTML = appState.clientes.map(c => `<option value="${c.id}" ${c.id === selectedId ? 'selected' : ''}>${c.nome} (${c.telefone})</option>`).join('');
}

function popularSelectServicosAtendimento(selectedId) {
  const sel = document.getElementById('atend-servico');
  if (!sel) return;
  sel.innerHTML = appState.servicos.map(s => `<option value="${s.id}" ${s.id === selectedId ? 'selected' : ''}>${s.nome} - ${formatMoney(s.precoSugerido)}</option>`).join('');
}

function onServicoSelecionadoNoAtendimento() {
  const servId = document.getElementById('atend-servico')?.value;
  const serv = appState.servicos.find(s => s.id === servId);
  if (!serv) return;

  document.getElementById('atend-valor').value = serv.precoSugerido || 0;

  // Build consumable list from service recipe
  const container = document.getElementById('atend-insumos-container');
  container.innerHTML = '';

  (serv.insumos || []).forEach(item => {
    adicionarLinhaInsumoAtendimento(item.insumoId, item.quantidade, item.unidade);
  });

  recalcularValoresAtendimento();
}

function adicionarLinhaInsumoAtendimento(insumoId, qtd, unidade) {
  const container = document.getElementById('atend-insumos-container');
  if (!container) return;

  const row = document.createElement('div');
  row.className = "flex items-center gap-2 text-xs bg-slate-900 p-2 rounded-lg border border-slate-800";

  const optionsInsumos = appState.insumos.map(i => `<option value="${i.id}" ${i.id === insumoId ? 'selected' : ''}>${i.nome} (${i.tipoUnidade})</option>`).join('');

  row.innerHTML = `
    <select class="atend-ins-id bg-slate-950 border border-slate-700 rounded p-1.5 text-slate-200 flex-1 outline-none" onchange="onInsumoLinhaChanged(this)">
      ${optionsInsumos}
    </select>
    <input type="number" step="any" value="${qtd || 1}" class="atend-ins-qtd bg-slate-950 border border-slate-700 rounded p-1.5 text-white font-mono w-20 outline-none text-center" oninput="recalcularValoresAtendimento()">
    <select class="atend-ins-unidade bg-slate-950 border border-slate-700 rounded p-1.5 text-slate-200 w-16 outline-none" onchange="recalcularValoresAtendimento()">
      <option value="g" ${unidade === 'g' ? 'selected' : ''}>g</option>
      <option value="kg" ${unidade === 'kg' ? 'selected' : ''}>kg</option>
      <option value="mg" ${unidade === 'mg' ? 'selected' : ''}>mg</option>
      <option value="ml" ${unidade === 'ml' ? 'selected' : ''}>ml</option>
      <option value="l" ${unidade === 'l' ? 'selected' : ''}>L</option>
      <option value="un" ${unidade === 'un' ? 'selected' : ''}>un</option>
      <option value="par" ${unidade === 'par' ? 'selected' : ''}>par</option>
      <option value="cx" ${unidade === 'cx' ? 'selected' : ''}>cx</option>
    </select>
    <span class="atend-ins-subtotal font-mono text-amber-400 w-20 text-right font-bold">R$ 0,00</span>
    <button type="button" onclick="this.parentElement.remove(); recalcularValoresAtendimento();" class="text-slate-500 hover:text-rose-400 p-1"><i class="fa-solid fa-xmark"></i></button>
  `;

  container.appendChild(row);
  recalcularValoresAtendimento();
}

function onInsumoLinhaChanged(selectEl) {
  const row = selectEl.parentElement;
  const insId = selectEl.value;
  const ins = appState.insumos.find(i => i.id === insId);
  if (!ins) return;

  const unitSelect = row.querySelector('.atend-ins-unidade');
  if (ins.tipoUnidade === 'peso') unitSelect.value = 'g';
  else if (ins.tipoUnidade === 'volume') unitSelect.value = 'ml';
  else unitSelect.value = ins.unidadeBase || 'un';

  recalcularValoresAtendimento();
}

function recalcularValoresAtendimento() {
  const valorCobrado = parseFloat(document.getElementById('atend-valor').value) || 0;
  let totalCustos = 0;

  const rows = document.querySelectorAll('#atend-insumos-container > div');
  rows.forEach(r => {
    const insId = r.querySelector('.atend-ins-id')?.value;
    const qtd = parseFloat(r.querySelector('.atend-ins-qtd')?.value) || 0;
    const un = r.querySelector('.atend-ins-unidade')?.value || 'un';
    const ins = appState.insumos.find(i => i.id === insId);

    const subtotal = calcularCustoConsumo(ins, qtd, un);
    totalCustos += subtotal;

    const subtotalEl = r.querySelector('.atend-ins-subtotal');
    if (subtotalEl) subtotalEl.textContent = formatMoney(subtotal);
  });

  const lucro = valorCobrado - totalCustos;
  const margem = valorCobrado > 0 ? (lucro / valorCobrado) * 100 : 0;

  document.getElementById('atend-custo').value = totalCustos.toFixed(2);
  document.getElementById('atend-lucro').value = lucro.toFixed(2);
  document.getElementById('atend-resumo-margem').textContent = `Margem: ${formatPercent(margem)}`;
  document.getElementById('atend-resumo-margem').className = `font-mono font-bold ${margem >= 60 ? 'text-emerald-400' : margem >= 30 ? 'text-cyan-400' : 'text-amber-400'}`;
}

function salvarAtendimento() {
  const id = document.getElementById('atend-id').value;
  const clienteId = document.getElementById('atend-cliente').value;
  const servicoId = document.getElementById('atend-servico').value;
  const serv = appState.servicos.find(s => s.id === servicoId);
  const data = document.getElementById('atend-data').value;
  const status = document.getElementById('atend-status').value;
  const valorCobrado = parseFloat(document.getElementById('atend-valor').value) || 0;
  const obs = document.getElementById('atend-obs').value;

  if (!clienteId || !servicoId) {
    alert("Por favor, selecione o cliente e o serviço.");
    return;
  }

  // Build consumables list
  const insumosUtilizados = [];
  let custoInsumos = 0;

  document.querySelectorAll('#atend-insumos-container > div').forEach(r => {
    const insId = r.querySelector('.atend-ins-id')?.value;
    const qtd = parseFloat(r.querySelector('.atend-ins-qtd')?.value) || 0;
    const un = r.querySelector('.atend-ins-unidade')?.value || 'un';
    const ins = appState.insumos.find(i => i.id === insId);
    const custo = calcularCustoConsumo(ins, qtd, un);
    custoInsumos += custo;

    insumosUtilizados.push({
      insumoId: insId,
      nome: ins ? ins.nome : 'Insumo',
      quantidade: qtd,
      unidade: un,
      custoCalculado: custo
    });
  });

  const lucroLiquido = valorCobrado - custoInsumos;
  const margem = valorCobrado > 0 ? (lucroLiquido / valorCobrado) * 100 : 0;

  if (id) {
    const idx = appState.atendimentos.findIndex(a => a.id === id);
    if (idx !== -1) {
      appState.atendimentos[idx] = {
        ...appState.atendimentos[idx],
        clienteId,
        servicoId,
        nomeServico: serv ? serv.nome : '',
        data: new Date(data).toISOString(),
        status,
        valorCobrado,
        custoInsumos,
        lucroLiquido,
        margem,
        insumosUtilizados,
        obs
      };
    }
  } else {
    appState.atendimentos.unshift({
      id: 'at_' + Date.now(),
      clienteId,
      servicoId,
      nomeServico: serv ? serv.nome : '',
      data: new Date(data).toISOString(),
      status,
      valorCobrado,
      custoInsumos,
      lucroLiquido,
      margem,
      insumosUtilizados,
      obs
    });
  }

  saveState();
  closeModal('modal-atendimento');
}

function editarAtendimento(id) {
  const atend = appState.atendimentos.find(a => a.id === id);
  if (!atend) return;

  document.getElementById('modal-atendimento-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-cyan-400"></i> Editar Atendimento';
  document.getElementById('atend-id').value = atend.id;
  document.getElementById('atend-data').value = new Date(atend.data).toISOString().slice(0, 16);
  document.getElementById('atend-status').value = atend.status;
  document.getElementById('atend-valor').value = atend.valorCobrado;
  document.getElementById('atend-obs').value = atend.obs || '';

  popularSelectClientesAtendimento(atend.clienteId);
  popularSelectServicosAtendimento(atend.servicoId);

  const container = document.getElementById('atend-insumos-container');
  container.innerHTML = '';
  (atend.insumosUtilizados || []).forEach(item => {
    adicionarLinhaInsumoAtendimento(item.insumoId, item.quantidade, item.unidade);
  });

  recalcularValoresAtendimento();
  openModal('modal-atendimento');
}

function excluirAtendimento(id) {
  if (confirm("Excluir este atendimento do histórico?")) {
    appState.atendimentos = appState.atendimentos.filter(a => a.id !== id);
    saveState();
  }
}


// --- SERVICO & FICHA TÉCNICA MODAL ---
function openNovoServicoModal() {
  document.getElementById('modal-servico-title').innerHTML = '<i class="fa-solid fa-plus text-cyan-400"></i> Novo Serviço & Ficha Técnica';
  document.getElementById('serv-id').value = '';
  document.getElementById('serv-nome').value = '';
  document.getElementById('serv-categoria').value = '';
  document.getElementById('serv-preco').value = '';

  const container = document.getElementById('ficha-insumos-container');
  container.innerHTML = '';
  recalcularFichaTecnicaModal();
  openModal('modal-servico');
}

function adicionarInsumoFichaTecnica(insumoId, qtd, unidade) {
  const container = document.getElementById('ficha-insumos-container');
  if (!container) return;

  const row = document.createElement('div');
  row.className = "flex items-center gap-2 text-xs bg-slate-900 p-2 rounded-lg border border-slate-800";

  const options = appState.insumos.map(i => `<option value="${i.id}" ${i.id === insumoId ? 'selected' : ''}>${i.nome}</option>`).join('');

  row.innerHTML = `
    <select class="ficha-ins-id bg-slate-950 border border-slate-700 rounded p-1.5 text-slate-200 flex-1 outline-none" onchange="recalcularFichaTecnicaModal()">
      ${options}
    </select>
    <input type="number" step="any" value="${qtd || 1}" class="ficha-ins-qtd bg-slate-950 border border-slate-700 rounded p-1.5 text-white font-mono w-20 outline-none text-center" oninput="recalcularFichaTecnicaModal()">
    <select class="ficha-ins-unidade bg-slate-950 border border-slate-700 rounded p-1.5 text-slate-200 w-16 outline-none" onchange="recalcularFichaTecnicaModal()">
      <option value="g" ${unidade === 'g' ? 'selected' : ''}>g</option>
      <option value="kg" ${unidade === 'kg' ? 'selected' : ''}>kg</option>
      <option value="mg" ${unidade === 'mg' ? 'selected' : ''}>mg</option>
      <option value="ml" ${unidade === 'ml' ? 'selected' : ''}>ml</option>
      <option value="l" ${unidade === 'l' ? 'selected' : ''}>L</option>
      <option value="un" ${unidade === 'un' ? 'selected' : ''}>un</option>
      <option value="par" ${unidade === 'par' ? 'selected' : ''}>par</option>
      <option value="cx" ${unidade === 'cx' ? 'selected' : ''}>cx</option>
    </select>
    <span class="ficha-ins-subtotal font-mono text-amber-400 w-20 text-right font-bold">R$ 0,00</span>
    <button type="button" onclick="this.parentElement.remove(); recalcularFichaTecnicaModal();" class="text-slate-500 hover:text-rose-400 p-1"><i class="fa-solid fa-xmark"></i></button>
  `;
  container.appendChild(row);
  recalcularFichaTecnicaModal();
}

function recalcularFichaTecnicaModal() {
  const preco = parseFloat(document.getElementById('serv-preco').value) || 0;
  let totalCustos = 0;

  document.querySelectorAll('#ficha-insumos-container > div').forEach(r => {
    const insId = r.querySelector('.ficha-ins-id')?.value;
    const qtd = parseFloat(r.querySelector('.ficha-ins-qtd')?.value) || 0;
    const un = r.querySelector('.ficha-ins-unidade')?.value || 'un';
    const ins = appState.insumos.find(i => i.id === insId);
    const custo = calcularCustoConsumo(ins, qtd, un);
    totalCustos += custo;

    const sub = r.querySelector('.ficha-ins-subtotal');
    if (sub) sub.textContent = formatMoney(custo);
  });

  const lucro = preco - totalCustos;
  const margem = preco > 0 ? (lucro / preco) * 100 : 0;

  document.getElementById('ficha-custo-total').textContent = formatMoney(totalCustos);
  document.getElementById('ficha-lucro-estimado').textContent = formatMoney(lucro);
  document.getElementById('ficha-margem-estimada').textContent = formatPercent(margem);
}

function salvarServico() {
  const id = document.getElementById('serv-id').value;
  const nome = document.getElementById('serv-nome').value.trim();
  const categoria = document.getElementById('serv-categoria').value.trim();
  const precoSugerido = parseFloat(document.getElementById('serv-preco').value) || 0;

  if (!nome) {
    alert("Informe o nome do serviço.");
    return;
  }

  const insumos = [];
  document.querySelectorAll('#ficha-insumos-container > div').forEach(r => {
    const insId = r.querySelector('.ficha-ins-id')?.value;
    const qtd = parseFloat(r.querySelector('.ficha-ins-qtd')?.value) || 0;
    const un = r.querySelector('.ficha-ins-unidade')?.value || 'un';
    if (insId) insumos.push({ insumoId: insId, quantidade: qtd, unidade: un });
  });

  if (id) {
    const idx = appState.servicos.findIndex(s => s.id === id);
    if (idx !== -1) {
      appState.servicos[idx] = { ...appState.servicos[idx], nome, categoria, precoSugerido, insumos };
    }
  } else {
    appState.servicos.push({
      id: 'serv_' + Date.now(),
      nome,
      categoria,
      precoSugerido,
      insumos
    });
  }

  saveState();
  closeModal('modal-servico');
}

function editarServico(id) {
  const s = appState.servicos.find(serv => serv.id === id);
  if (!s) return;

  document.getElementById('modal-servico-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-cyan-400"></i> Editar Serviço & Ficha Técnica';
  document.getElementById('serv-id').value = s.id;
  document.getElementById('serv-nome').value = s.nome;
  document.getElementById('serv-categoria').value = s.categoria || '';
  document.getElementById('serv-preco').value = s.precoSugerido;

  const container = document.getElementById('ficha-insumos-container');
  container.innerHTML = '';
  (s.insumos || []).forEach(item => {
    adicionarInsumoFichaTecnica(item.insumoId, item.quantidade, item.unidade);
  });

  recalcularFichaTecnicaModal();
  openModal('modal-servico');
}

function excluirServico(id) {
  if (confirm("Excluir este serviço do catálogo?")) {
    appState.servicos = appState.servicos.filter(s => s.id !== id);
    saveState();
  }
}


// --- INSUMO & ESTOQUE MODAL ---
function openNovoInsumoModal() {
  document.getElementById('modal-insumo-title').innerHTML = '<i class="fa-solid fa-plus text-cyan-400"></i> Novo Insumo & Cálculo Proporcional';
  document.getElementById('ins-id').value = '';
  document.getElementById('ins-nome').value = '';
  document.getElementById('ins-tipo-unidade').value = 'peso';
  document.getElementById('ins-qtd-compra').value = 1;
  document.getElementById('ins-preco-compra').value = '';
  document.getElementById('ins-estoque-atual').value = 10;
  document.getElementById('ins-estoque-minimo').value = 2;

  onTipoUnidadeChange();
  openModal('modal-insumo');
}

function onTipoUnidadeChange() {
  const tipo = document.getElementById('ins-tipo-unidade').value;
  const selUn = document.getElementById('ins-unidade-compra');
  selUn.innerHTML = '';

  if (tipo === 'peso') {
    selUn.innerHTML = `
      <option value="kg" selected>Quilograma (kg)</option>
      <option value="g">Grama (g)</option>
      <option value="mg">Miligrama (mg)</option>
    `;
  } else if (tipo === 'volume') {
    selUn.innerHTML = `
      <option value="l" selected>Litro (L)</option>
      <option value="ml">Mililitro (ml)</option>
    `;
  } else {
    selUn.innerHTML = `
      <option value="un" selected>Unidade (un)</option>
      <option value="cx">Caixa (cx)</option>
      <option value="tubo">Tubo / Bisnaga</option>
      <option value="frasco">Frasco</option>
      <option value="par">Par</option>
      <option value="kit">Kit</option>
    `;
  }
  recalcularCustoUnitarioInsumoModal();
}

function recalcularCustoUnitarioInsumoModal() {
  const tipo = document.getElementById('ins-tipo-unidade').value;
  const unidadeCompra = document.getElementById('ins-unidade-compra').value;
  const qtdCompra = parseFloat(document.getElementById('ins-qtd-compra').value) || 1;
  const precoCompra = parseFloat(document.getElementById('ins-preco-compra').value) || 0;

  const { unidadeBase, custoPorUnidadeBase } = calcularCustoUnitarioBase(tipo, unidadeCompra, qtdCompra, precoCompra);

  document.getElementById('ins-preview-base').textContent = `${formatMoney(custoPorUnidadeBase)} / ${unidadeBase}`;

  const convBox = document.getElementById('ins-preview-conversoes');
  convBox.innerHTML = '';

  if (tipo === 'peso') {
    // Show 100g, 10g, 1g, 500mg
    const mockInsumo = { tipoUnidade: 'peso', custoPorUnidadeBase };
    convBox.innerHTML = `
      <div>• 100g = <strong class="text-amber-300">${formatMoney(calcularCustoConsumo(mockInsumo, 100, 'g'))}</strong></div>
      <div>• 10g = <strong class="text-amber-300">${formatMoney(calcularCustoConsumo(mockInsumo, 10, 'g'))}</strong></div>
      <div>• 1g = <strong class="text-amber-300">${formatMoney(calcularCustoConsumo(mockInsumo, 1, 'g'))}</strong></div>
    `;
  } else if (tipo === 'volume') {
    const mockInsumo = { tipoUnidade: 'volume', custoPorUnidadeBase };
    convBox.innerHTML = `
      <div>• 100ml = <strong class="text-amber-300">${formatMoney(calcularCustoConsumo(mockInsumo, 100, 'ml'))}</strong></div>
      <div>• 20ml = <strong class="text-amber-300">${formatMoney(calcularCustoConsumo(mockInsumo, 20, 'ml'))}</strong></div>
      <div>• 1ml = <strong class="text-amber-300">${formatMoney(calcularCustoConsumo(mockInsumo, 1, 'ml'))}</strong></div>
    `;
  } else {
    convBox.innerHTML = `
      <div>• 1 ${unidadeBase} = <strong class="text-amber-300">${formatMoney(custoPorUnidadeBase)}</strong></div>
      <div>• 0.5 ${unidadeBase} (metade) = <strong class="text-amber-300">${formatMoney(custoPorUnidadeBase * 0.5)}</strong></div>
    `;
  }
}

function salvarInsumo() {
  const id = document.getElementById('ins-id').value;
  const nome = document.getElementById('ins-nome').value.trim();
  const tipoUnidade = document.getElementById('ins-tipo-unidade').value;
  const unidadeCompra = document.getElementById('ins-unidade-compra').value;
  const qtdCompra = parseFloat(document.getElementById('ins-qtd-compra').value) || 1;
  const precoCompra = parseFloat(document.getElementById('ins-preco-compra').value) || 0;
  const estoqueAtual = parseFloat(document.getElementById('ins-estoque-atual').value) || 0;
  const estoqueMinimo = parseFloat(document.getElementById('ins-estoque-minimo').value) || 0;

  if (!nome) {
    alert("Informe o nome do insumo.");
    return;
  }

  const { unidadeBase, custoPorUnidadeBase } = calcularCustoUnitarioBase(tipoUnidade, unidadeCompra, qtdCompra, precoCompra);

  if (id) {
    const idx = appState.insumos.findIndex(i => i.id === id);
    if (idx !== -1) {
      appState.insumos[idx] = {
        ...appState.insumos[idx],
        nome,
        tipoUnidade,
        unidadeCompra,
        qtdCompra,
        precoCompra,
        estoqueAtual,
        estoqueMinimo,
        unidadeBase,
        custoPorUnidadeBase
      };
    }
  } else {
    appState.insumos.push({
      id: 'ins_' + Date.now(),
      nome,
      tipoUnidade,
      unidadeCompra,
      qtdCompra,
      precoCompra,
      estoqueAtual,
      estoqueMinimo,
      unidadeBase,
      custoPorUnidadeBase
    });
  }

  saveState();
  closeModal('modal-insumo');
}

function editarInsumo(id) {
  const ins = appState.insumos.find(i => i.id === id);
  if (!ins) return;

  document.getElementById('modal-insumo-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-cyan-400"></i> Editar Insumo';
  document.getElementById('ins-id').value = ins.id;
  document.getElementById('ins-nome').value = ins.nome;
  document.getElementById('ins-tipo-unidade').value = ins.tipoUnidade;
  onTipoUnidadeChange();
  document.getElementById('ins-unidade-compra').value = ins.unidadeCompra;
  document.getElementById('ins-qtd-compra').value = ins.qtdCompra;
  document.getElementById('ins-preco-compra').value = ins.precoCompra;
  document.getElementById('ins-estoque-atual').value = ins.estoqueAtual;
  document.getElementById('ins-estoque-minimo').value = ins.estoqueMinimo;

  recalcularCustoUnitarioInsumoModal();
  openModal('modal-insumo');
}

function excluirInsumo(id) {
  if (confirm("Excluir este insumo? Procedimentos vinculados poderão ter custos recalculados.")) {
    appState.insumos = appState.insumos.filter(i => i.id !== id);
    saveState();
  }
}


// --- CLIENTE MODAL ---
function openNovoClienteModal(fromAtendimento = false) {
  document.getElementById('modal-cliente-title').innerHTML = '<i class="fa-solid fa-user-plus text-cyan-400"></i> Novo Cliente';
  document.getElementById('cli-id').value = '';
  document.getElementById('cli-nome').value = '';
  document.getElementById('cli-telefone').value = '(32) 99929-2311';
  document.getElementById('cli-email').value = '';
  document.getElementById('cli-cidade').value = '';
  openModal('modal-cliente');
}

function salvarCliente() {
  const id = document.getElementById('cli-id').value;
  const nome = document.getElementById('cli-nome').value.trim();
  const telefone = document.getElementById('cli-telefone').value.trim();
  const email = document.getElementById('cli-email').value.trim();
  const cidade = document.getElementById('cli-cidade').value.trim();

  if (!nome || !telefone) {
    alert("Informe pelo menos o nome e o telefone do cliente.");
    return;
  }

  let newClientId = id;
  if (id) {
    const idx = appState.clientes.findIndex(c => c.id === id);
    if (idx !== -1) {
      appState.clientes[idx] = { ...appState.clientes[idx], nome, telefone, email, cidade };
    }
  } else {
    newClientId = 'c_' + Date.now();
    appState.clientes.push({ id: newClientId, nome, telefone, email, cidade });
  }

  saveState();
  closeModal('modal-cliente');

  // If atendimento modal was open, refresh client select
  popularSelectClientesAtendimento(newClientId);
}

function editarCliente(id) {
  const cli = appState.clientes.find(c => c.id === id);
  if (!cli) return;

  document.getElementById('modal-cliente-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-cyan-400"></i> Editar Cliente';
  document.getElementById('cli-id').value = cli.id;
  document.getElementById('cli-nome').value = cli.nome;
  document.getElementById('cli-telefone').value = cli.telefone;
  document.getElementById('cli-email').value = cli.email || '';
  document.getElementById('cli-cidade').value = cli.cidade || '';
  openModal('modal-cliente');
}

function excluirCliente(id) {
  if (confirm("Excluir este cliente e seus atendimentos?")) {
    appState.clientes = appState.clientes.filter(c => c.id !== id);
    appState.atendimentos = appState.atendimentos.filter(a => a.clienteId !== id);
    saveState();
  }
}


// --- CONFIGURAÇÕES & BACKUP MODAL ---
function openConfigModal() {
  document.getElementById('cfg-nome-empresa').value = appState.config.nomeEmpresa || '';
  document.getElementById('cfg-whatsapp').value = appState.config.whatsappPadrao || '32999292311';
  openModal('modal-config');
}

function salvarConfiguracoes() {
  const nomeEmpresa = document.getElementById('cfg-nome-empresa').value.trim();
  const whatsappPadrao = document.getElementById('cfg-whatsapp').value.trim();

  if (nomeEmpresa) appState.config.nomeEmpresa = nomeEmpresa;
  if (whatsappPadrao) appState.config.whatsappPadrao = whatsappPadrao;

  saveState();
  closeModal('modal-config');
}

function exportarBackupJSON() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(appState, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", `nexus_crm_servicos_backup_${new Date().toISOString().split('T')[0]}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
}

function importarBackupJSON(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function(e) {
    try {
      const imported = JSON.parse(e.target.result);
      if (imported.servicos && imported.insumos) {
        appState = imported;
        saveState();
        alert("Backup importado com sucesso!");
        closeModal('modal-config');
      } else {
        alert("Arquivo JSON inválido para o CRM Serviços.");
      }
    } catch (err) {
      alert("Erro ao ler o arquivo JSON: " + err.message);
    }
  };
  reader.readAsText(file);
}

// ============================================================
// INITIAL START
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  updateAllViews();
  if (window.location.hash) {
    const hashTab = window.location.hash.replace('#', '');
    if (document.getElementById(`tab-content-${hashTab}`)) {
      switchTab(hashTab);
    }
  }
});
