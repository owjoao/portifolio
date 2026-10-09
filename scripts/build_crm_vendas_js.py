# -*- coding: utf-8 -*-
import os

js_content = r"""// ============================================================
// NEXUS CRM VENDAS - CORE ENGINE & DYNAMIC ADAPTABLE STATE
// ============================================================

const STORAGE_KEY = 'NEXUS_CRM_VENDAS_V1';

// Default initial state (Demonstrating commercial sales & profit per item)
const DEFAULT_STATE = {
  config: {
    nomeEmpresa: "Nexus Distribuição & Comércio",
    whatsappPadrao: "32999292311"
  },
  clientes: [
    { id: "c1", nome: "Dr. Marcelo Vieira", telefone: "(32) 99929-2311", email: "marcelo@agro.com", cidade: "Ribeirão Preto - SP" },
    { id: "c2", nome: "Beatriz Vasconcelos", telefone: "(32) 99929-2311", email: "beatriz@lojas.com", cidade: "Campinas - SP" },
    { id: "c3", nome: "Eng. Lucas Meirelles", telefone: "(32) 99929-2311", email: "lucas@solartech.com", cidade: "Belo Horizonte - MG" },
    { id: "c4", nome: "Renata Fagundes", telefone: "(32) 99929-2311", email: "renata@empresa.com", cidade: "Curitiba - PR" }
  ],
  produtos: [
    {
      id: "p1",
      sku: "INV-5K",
      nome: "Inversor Solar Híbrido 5kW WiFi",
      categoria: "Equipamentos de Energia",
      custoCompra: 2400.00,
      precoVenda: 4200.00,
      estoqueAtual: 14,
      estoqueMinimo: 3
      // Lucro Unit: R$ 1.800,00 | Margem: 42.9%
    },
    {
      id: "p2",
      sku: "MOD-550W",
      nome: "Painel Solar Monocristalino 550W Tier 1",
      categoria: "Módulos Fotovoltaicos",
      custoCompra: 320.00,
      precoVenda: 580.00,
      estoqueAtual: 180,
      estoqueMinimo: 20
      // Lucro Unit: R$ 260,00 | Margem: 44.8%
    },
    {
      id: "p3",
      sku: "CABO-SOLAR",
      nome: "Rolo Cabo Solar 6mm² Dupla Isolação (100m)",
      categoria: "Cabos & Condutores",
      custoCompra: 380.00,
      precoVenda: 590.00,
      estoqueAtual: 30,
      estoqueMinimo: 5
      // Lucro Unit: R$ 210,00 | Margem: 35.6%
    },
    {
      id: "p4",
      sku: "KIT-ESTRUT",
      nome: "Kit Estrutura Fixação Telhado Cerâmico (4 Placas)",
      categoria: "Estruturas Metálicas",
      custoCompra: 210.00,
      precoVenda: 450.00,
      estoqueAtual: 22,
      estoqueMinimo: 6
      // Lucro Unit: R$ 240,00 | Margem: 53.3%
    },
    {
      id: "p5",
      sku: "DISJ-QUADRO",
      nome: "Quadro de Proteção String Box 2 Entradas / 2 Saídas",
      categoria: "Proteção Elétrica",
      custoCompra: 450.00,
      precoVenda: 890.00,
      estoqueAtual: 18,
      estoqueMinimo: 4
      // Lucro Unit: R$ 440,00 | Margem: 49.4%
    }
  ],
  vendas: [
    {
      id: "v1",
      clienteId: "c1",
      data: new Date(Date.now() - 3 * 86400000).toISOString(),
      produtoId: "p1",
      nomeProduto: "Inversor Solar Híbrido 5kW WiFi",
      quantidade: 1,
      precoVendaUnitario: 4200.00,
      custoCompraUnitario: 2400.00,
      valorTotalVenda: 4200.00,
      custoTotal: 2400.00,
      lucroLiquido: 1800.00,
      margem: 42.9,
      etapa: "fechada",
      formaPagamento: "PIX",
      obs: "Entrega expressa realizada com sucesso."
    },
    {
      id: "v2",
      clienteId: "c2",
      data: new Date(Date.now() - 2 * 86400000).toISOString(),
      produtoId: "p2",
      nomeProduto: "Painel Solar Monocristalino 550W Tier 1",
      quantidade: 10,
      precoVendaUnitario: 580.00,
      custoCompraUnitario: 320.00,
      valorTotalVenda: 5800.00,
      custoTotal: 3200.00,
      lucroLiquido: 2600.00,
      margem: 44.8,
      etapa: "fechada",
      formaPagamento: "Boleto Bancário",
      obs: "Lote de 10 placas entregue no centro de distribuição."
    },
    {
      id: "v3",
      clienteId: "c3",
      data: new Date(Date.now() - 1 * 86400000).toISOString(),
      produtoId: "p4",
      nomeProduto: "Kit Estrutura Fixação Telhado Cerâmico (4 Placas)",
      quantidade: 3,
      precoVendaUnitario: 450.00,
      custoCompraUnitario: 210.00,
      valorTotalVenda: 1350.00,
      custoTotal: 630.00,
      lucroLiquido: 720.00,
      margem: 53.3,
      etapa: "negociacao",
      formaPagamento: "Cartão de Crédito",
      obs: "Cliente negociando frete compartilhado."
    },
    {
      id: "v4",
      clienteId: "c4",
      data: new Date().toISOString(),
      produtoId: "p5",
      nomeProduto: "Quadro de Proteção String Box 2 Entradas / 2 Saídas",
      quantidade: 2,
      precoVendaUnitario: 890.00,
      custoCompraUnitario: 450.00,
      valorTotalVenda: 1780.00,
      custoTotal: 900.00,
      lucroLiquido: 880.00,
      margem: 49.4,
      etapa: "proposta",
      formaPagamento: "PIX",
      obs: "Proposta técnica enviada por PDF e WhatsApp."
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
  if (confirm("Tem certeza que deseja recarregar os dados de exemplo comerciais?")) {
    appState = JSON.parse(JSON.stringify(DEFAULT_STATE));
    saveState();
    closeModal('modal-config');
  }
}

function limparTodosDados() {
  if (confirm("ATENÇÃO: Deseja apagar todos os dados de vendas para começar do zero?")) {
    appState = {
      config: { nomeEmpresa: "Minha Loja Comercial", whatsappPadrao: "32999292311" },
      clientes: [],
      produtos: [],
      vendas: []
    };
    saveState();
    closeModal('modal-config');
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
    activeBtn.className = 'df-btn px-2.5 py-1 rounded bg-emerald-950 text-emerald-300 border border-emerald-800/80 font-medium';
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

function getFilteredVendas() {
  return appState.vendas.filter(v => isDateInFilter(v.data));
}

// ============================================================
// CORE VIEW REFRESH & KPIS
// ============================================================
function updateAllViews() {
  // Update header company name
  const nameEl = document.getElementById('header-company-name');
  if (nameEl) nameEl.textContent = appState.config.nomeEmpresa || 'Minha Loja Comercial';

  const filtered = getFilteredVendas();
  const fechadas = filtered.filter(v => v.etapa === 'fechada');

  // Recalculate Totals
  const totalFaturamento = fechadas.reduce((acc, v) => acc + (v.valorTotalVenda || 0), 0);
  const totalCustos = fechadas.reduce((acc, v) => acc + (v.custoTotal || 0), 0);
  const totalLucro = totalFaturamento - totalCustos;
  const margemMedia = totalFaturamento > 0 ? (totalLucro / totalFaturamento) * 100 : 0;
  const totalItens = fechadas.reduce((acc, v) => acc + (v.quantidade || 0), 0);
  const totalVendasCount = fechadas.length;
  const ticketMedio = totalVendasCount > 0 ? totalFaturamento / totalVendasCount : 0;

  // KPI UI
  document.getElementById('kpi-faturamento').textContent = formatMoney(totalFaturamento);
  document.getElementById('kpi-custos').textContent = formatMoney(totalCustos);
  document.getElementById('kpi-lucro').textContent = formatMoney(totalLucro);
  document.getElementById('kpi-margem').textContent = formatPercent(margemMedia);
  document.getElementById('kpi-itens-vendidos').textContent = totalItens;
  document.getElementById('kpi-ticket').textContent = formatMoney(ticketMedio);
  document.getElementById('badge-total-vendas').textContent = appState.vendas.length;

  // Update tabs
  renderPipeline();
  renderHistorico();
  renderMargens();
  renderProdutos();
  renderClientes();
}

// ============================================================
// TAB NAVIGATION
// ============================================================
function switchTab(tabId) {
  document.querySelectorAll('.tab-pane').forEach(el => el.classList.add('hidden'));
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.className = 'tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent';
  });

  const content = document.getElementById(`tab-content-${tabId}`);
  const btn = document.getElementById(`tab-btn-${tabId}`);
  if (content) content.classList.remove('hidden');
  if (btn) {
    btn.className = 'tab-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-emerald-400 bg-emerald-950/60 border border-emerald-800/50';
  }
}

// ============================================================
// TAB 1: PIPELINE / FUNIL KANBAN (6 COLUMNS)
// ============================================================
function renderPipeline() {
  const searchTerm = (document.getElementById('search-pipeline')?.value || '').toLowerCase();
  const cols = {
    novo: document.getElementById('pipeline-col-novo'),
    qualificacao: document.getElementById('pipeline-col-qualificacao'),
    proposta: document.getElementById('pipeline-col-proposta'),
    negociacao: document.getElementById('pipeline-col-negociacao'),
    fechada: document.getElementById('pipeline-col-fechada'),
    perdida: document.getElementById('pipeline-col-perdida'),
  };

  // Clear columns
  Object.values(cols).forEach(col => { if (col) col.innerHTML = ''; });
  const counts = { novo: 0, qualificacao: 0, proposta: 0, negociacao: 0, fechada: 0, perdida: 0 };

  const filtered = getFilteredVendas();

  filtered.forEach(venda => {
    const cliente = appState.clientes.find(c => c.id === venda.clienteId) || { nome: 'Cliente não informado', telefone: '' };
    const produto = appState.produtos.find(p => p.id === venda.produtoId) || { nome: venda.nomeProduto || 'Produto' };

    // Search filter
    if (searchTerm) {
      const matchClient = cliente.nome.toLowerCase().includes(searchTerm);
      const matchProd = produto.nome.toLowerCase().includes(searchTerm);
      if (!matchClient && !matchProd) return;
    }

    const etapa = venda.etapa || 'novo';
    if (counts[etapa] !== undefined) counts[etapa]++;

    const col = cols[etapa];
    if (!col) return;

    // WhatsApp direct message
    const cleanPhone = cliente.telefone.replace(/\D/g, '');
    const waUrl = `https://wa.me/${cleanPhone || appState.config.whatsappPadrao || '5532999292311'}?text=${encodeURIComponent(`Olá ${cliente.nome}, referente ao produto ${produto.nome} (${venda.quantidade}x)...`)}`;

    const card = document.createElement('div');
    card.className = "bg-slate-950/90 border border-slate-800 hover:border-emerald-500/50 rounded-xl p-3 shadow-md space-y-2.5 transition group";
    card.innerHTML = `
      <div class="flex items-start justify-between gap-2">
        <div>
          <span class="font-bold text-white text-xs block">${cliente.nome}</span>
          <span class="text-[11px] text-emerald-400 font-medium truncate block max-w-[150px]">${produto.nome}</span>
          <span class="text-[10px] text-slate-400 font-mono">Qtd: <strong>${venda.quantidade} un</strong></span>
        </div>
        <div class="flex items-center gap-1">
          <a href="${waUrl}" target="_blank" class="w-6 h-6 rounded bg-emerald-950/80 text-emerald-400 hover:bg-emerald-800 flex items-center justify-center text-[11px]" title="Chamar no WhatsApp">
            <i class="fa-brands fa-whatsapp"></i>
          </a>
          <button onclick="editarVenda('${venda.id}')" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:text-emerald-400 flex items-center justify-center text-[10px]" title="Editar venda">
            <i class="fa-solid fa-pen"></i>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-1 py-1.5 px-2 bg-slate-900/60 rounded-lg border border-slate-800/80 text-[10px] font-mono">
        <div>
          <span class="text-slate-400 block">Venda Total:</span>
          <span class="text-white font-bold">${formatMoney(venda.valorTotalVenda)}</span>
        </div>
        <div>
          <span class="text-slate-400 block">Custo (CMV):</span>
          <span class="text-amber-400 font-bold">${formatMoney(venda.custoTotal)}</span>
        </div>
        <div class="col-span-2 pt-1 border-t border-slate-800/60 flex items-center justify-between">
          <span class="text-slate-400">Lucro: <strong class="text-emerald-400">${formatMoney(venda.lucroLiquido)}</strong></span>
          <span class="text-cyan-300 font-bold">${formatPercent(venda.margem)}</span>
        </div>
      </div>

      <div class="flex items-center justify-between text-[10px] text-slate-400 pt-1">
        <span><i class="fa-regular fa-clock mr-1"></i>${formatDate(venda.data).split(' ')[0]}</span>
        
        <!-- Status quick changer -->
        <select onchange="mudarEtapaVenda('${venda.id}', this.value)" class="bg-slate-900 border border-slate-700 text-slate-300 rounded px-1.5 py-0.5 text-[10px] outline-none">
          <option value="novo" ${etapa === 'novo' ? 'selected' : ''}>1. Lead</option>
          <option value="qualificacao" ${etapa === 'qualificacao' ? 'selected' : ''}>2. Qualif.</option>
          <option value="proposta" ${etapa === 'proposta' ? 'selected' : ''}>3. Proposta</option>
          <option value="negociacao" ${etapa === 'negociacao' ? 'selected' : ''}>4. Negoc.</option>
          <option value="fechada" ${etapa === 'fechada' ? 'selected' : ''}>5. Fechada</option>
          <option value="perdida" ${etapa === 'perdida' ? 'selected' : ''}>6. Perdida</option>
        </select>
      </div>
    `;

    col.appendChild(card);
  });

  // Update counts
  document.getElementById('col-count-novo').textContent = counts.novo;
  document.getElementById('col-count-qualificacao').textContent = counts.qualificacao;
  document.getElementById('col-count-proposta').textContent = counts.proposta;
  document.getElementById('col-count-negociacao').textContent = counts.negociacao;
  document.getElementById('col-count-fechada').textContent = counts.fechada;
  document.getElementById('col-count-perdida').textContent = counts.perdida;
}

function mudarEtapaVenda(id, novaEtapa) {
  const venda = appState.vendas.find(v => v.id === id);
  if (venda) {
    venda.etapa = novaEtapa;
    saveState();
  }
}

// ============================================================
// TAB 2: HISTÓRICO DE VENDAS (LEDGER)
// ============================================================
function renderHistorico() {
  const tbody = document.getElementById('historico-tbody');
  const empty = document.getElementById('historico-empty');
  const searchTerm = (document.getElementById('search-historico')?.value || '').toLowerCase();
  if (!tbody) return;

  tbody.innerHTML = '';
  const filtered = getFilteredVendas();
  const sorted = [...filtered].sort((a, b) => new Date(b.data) - new Date(a.data));

  let visibleCount = 0;
  sorted.forEach(venda => {
    const cliente = appState.clientes.find(c => c.id === venda.clienteId) || { nome: 'Cliente não informado', telefone: '' };
    const produto = appState.produtos.find(p => p.id === venda.produtoId) || { nome: venda.nomeProduto || 'Produto' };

    if (searchTerm) {
      const match = cliente.nome.toLowerCase().includes(searchTerm) || produto.nome.toLowerCase().includes(searchTerm);
      if (!match) return;
    }

    visibleCount++;
    const tr = document.createElement('tr');
    tr.className = "hover:bg-slate-900/60 transition";

    const etapaBadges = {
      novo: '<span class="px-2 py-0.5 bg-blue-950 text-blue-400 border border-blue-800/40 rounded text-[10px]">Novo Lead</span>',
      qualificacao: '<span class="px-2 py-0.5 bg-purple-950 text-purple-400 border border-purple-800/40 rounded text-[10px]">Qualificação</span>',
      proposta: '<span class="px-2 py-0.5 bg-cyan-950 text-cyan-400 border border-cyan-800/40 rounded text-[10px]">Proposta</span>',
      negociacao: '<span class="px-2 py-0.5 bg-amber-950 text-amber-400 border border-amber-800/40 rounded text-[10px]">Negociação</span>',
      fechada: '<span class="px-2 py-0.5 bg-emerald-950 text-emerald-400 border border-emerald-800/40 rounded text-[10px]">Venda Fechada</span>',
      perdida: '<span class="px-2 py-0.5 bg-rose-950 text-rose-400 border border-rose-800/40 rounded text-[10px]">Perdida</span>'
    };

    tr.innerHTML = `
      <td class="py-3 px-3 font-mono text-[11px] text-slate-400">${formatDate(venda.data)}</td>
      <td class="py-3 px-3 font-bold text-white">${cliente.nome}</td>
      <td class="py-3 px-3 font-semibold text-emerald-400">${produto.nome}</td>
      <td class="py-3 px-3 text-center font-mono font-bold">${venda.quantidade}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-white">${formatMoney(venda.valorTotalVenda)}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-amber-400">${formatMoney(venda.custoTotal)}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-emerald-400">${formatMoney(venda.lucroLiquido)}</td>
      <td class="py-3 px-3 text-center font-mono font-bold text-cyan-300">${formatPercent(venda.margem)}</td>
      <td class="py-3 px-3 text-center text-slate-300 text-[11px]">${venda.formaPagamento || 'PIX'}</td>
      <td class="py-3 px-3 text-center">${etapaBadges[venda.etapa] || venda.etapa}</td>
      <td class="py-3 px-3 text-center">
        <div class="flex items-center justify-center gap-1.5">
          <button onclick="editarVenda('${venda.id}')" class="p-1 rounded text-slate-400 hover:text-emerald-400" title="Editar">
            <i class="fa-solid fa-pen-to-square"></i>
          </button>
          <button onclick="excluirVenda('${venda.id}')" class="p-1 rounded text-slate-400 hover:text-rose-400" title="Excluir">
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
  const filtered = getFilteredVendas();
  if (filtered.length === 0) {
    alert("Nenhuma movimentação comercial para exportar.");
    return;
  }

  let csv = "Data;Cliente;Telefone;Produto;Quantidade;Valor Venda Total;Custo Total;Lucro Liquido;Margem %;Pagamento;Etapa;Observacoes\n";
  filtered.forEach(v => {
    const c = appState.clientes.find(cli => cli.id === v.clienteId) || { nome: '-', telefone: '-' };
    const p = appState.produtos.find(pro => pro.id === v.produtoId) || { nome: v.nomeProduto || '-' };
    csv += `"${formatDate(v.data)}";"${c.nome}";"${c.telefone}";"${p.nome}";"${v.quantidade}";"${v.valorTotalVenda}";"${v.custoTotal}";"${v.lucroLiquido}";"${v.margem}";"${v.formaPagamento || 'PIX'}";"${v.etapa}";"${(v.obs || '').replace(/"/g, '""')}"\n`;
  });

  const blob = new Blob(["\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", `historico_vendas_produtos_${new Date().toISOString().split('T')[0]}.csv`);
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
  const filtered = getFilteredVendas();
  const fechadas = filtered.filter(v => v.etapa === 'fechada');

  // Compute metrics for each product in catalog
  const performance = appState.produtos.map(prod => {
    const vendasDoProd = fechadas.filter(v => v.produtoId === prod.id);
    const volumeItens = vendasDoProd.reduce((acc, v) => acc + (v.quantidade || 0), 0);
    const faturamentoTotal = vendasDoProd.reduce((acc, v) => acc + (v.valorTotalVenda || 0), 0);
    const custoTotal = vendasDoProd.reduce((acc, v) => acc + (v.custoTotal || 0), 0);
    const lucroTotal = faturamentoTotal - custoTotal;
    const margemMedia = faturamentoTotal > 0 ? (lucroTotal / faturamentoTotal) * 100 : 0;

    // Unit baseline
    const lucroUnitario = prod.precoVenda - prod.custoCompra;
    const margemUnitaria = prod.precoVenda > 0 ? (lucroUnitario / prod.precoVenda) * 100 : 0;

    return {
      produto: prod,
      volumeItens,
      faturamentoTotal,
      custoTotal,
      lucroTotal,
      margemMedia: volumeItens > 0 ? margemMedia : margemUnitaria,
      lucroUnitario,
      margemUnitaria
    };
  });

  // Sort
  if (sortType === 'melhor_margem') {
    performance.sort((a, b) => b.margemMedia - a.margemMedia);
  } else if (sortType === 'maior_lucro') {
    performance.sort((a, b) => b.lucroTotal - a.lucroTotal);
  } else if (sortType === 'mais_vendidos') {
    performance.sort((a, b) => b.volumeItens - a.volumeItens);
  } else if (sortType === 'maior_faturamento') {
    performance.sort((a, b) => b.faturamentoTotal - a.faturamentoTotal);
  } else if (sortType === 'maior_cmv') {
    performance.sort((a, b) => b.produto.custoCompra - a.produto.custoCompra);
  }

  performance.forEach((p, idx) => {
    const isTop1 = idx === 0 && p.margemMedia > 0;
    const isLowMargin = p.margemMedia < 20 && p.produto.precoVenda > 0;

    const card = document.createElement('div');
    card.className = `bg-slate-900/80 border ${isTop1 ? 'border-emerald-500/80 shadow-lg shadow-emerald-500/10' : 'border-slate-800'} rounded-2xl p-5 space-y-4 relative overflow-hidden transition group hover:border-emerald-500/60`;
    
    // Top highlight badge
    let topBadge = '';
    if (isTop1) {
      topBadge = '<span class="absolute top-3 right-3 px-2 py-0.5 bg-emerald-950 text-emerald-400 border border-emerald-800 text-[10px] font-bold rounded-full flex items-center gap-1"><i class="fa-solid fa-crown text-[9px]"></i> Melhor Margem</span>';
    } else if (isLowMargin) {
      topBadge = '<span class="absolute top-3 right-3 px-2 py-0.5 bg-amber-950 text-amber-400 border border-amber-800 text-[10px] font-bold rounded-full">⚠️ Margem Baixa</span>';
    }

    card.innerHTML = `
      ${topBadge}
      <div>
        <span class="text-[10px] font-mono text-emerald-400 uppercase tracking-wider">${p.produto.sku || 'SKU'} • ${p.produto.categoria || 'Geral'}</span>
        <h3 class="text-base font-extrabold text-white group-hover:text-emerald-400 transition">${p.produto.nome}</h3>
      </div>

      <!-- Margin Meter -->
      <div>
        <div class="flex items-center justify-between text-xs font-mono mb-1">
          <span class="text-slate-400">Margem Comercial:</span>
          <strong class="text-base ${p.margemMedia >= 40 ? 'text-emerald-400' : p.margemMedia >= 25 ? 'text-cyan-400' : 'text-amber-400'}">${formatPercent(p.margemMedia)}</strong>
        </div>
        <div class="w-full bg-slate-950 h-2.5 rounded-full overflow-hidden border border-slate-800">
          <div class="h-full rounded-full transition-all duration-500 ${p.margemMedia >= 40 ? 'bg-gradient-to-r from-emerald-500 to-cyan-500' : p.margemMedia >= 25 ? 'bg-cyan-500' : 'bg-amber-500'}" style="width: ${Math.min(100, Math.max(0, p.margemMedia))}%"></div>
        </div>
      </div>

      <!-- Unit breakdown -->
      <div class="grid grid-cols-2 gap-2 p-3 bg-slate-950/80 rounded-xl border border-slate-800 text-xs font-mono">
        <div>
          <span class="text-[10px] text-slate-400 block">Preço de Venda:</span>
          <span class="text-white font-bold">${formatMoney(p.produto.precoVenda)}</span>
        </div>
        <div>
          <span class="text-[10px] text-slate-400 block">Custo Compra (CMV):</span>
          <span class="text-amber-400 font-bold">${formatMoney(p.produto.custoCompra)}</span>
        </div>
        <div class="pt-2 border-t border-slate-800">
          <span class="text-[10px] text-slate-400 block">Lucro por Item:</span>
          <span class="text-emerald-400 font-bold">${formatMoney(p.lucroUnitario)}</span>
        </div>
        <div class="pt-2 border-t border-slate-800">
          <span class="text-[10px] text-slate-400 block">Vendido no Período:</span>
          <span class="text-slate-200 font-bold">${p.volumeItens} unidades</span>
        </div>
      </div>

      <div class="flex items-center justify-between text-xs pt-1">
        <span class="text-slate-400">Lucro Total no Caixa: <strong class="text-emerald-400 font-mono">${formatMoney(p.lucroTotal)}</strong></span>
        <button onclick="editarProduto('${p.produto.id}')" class="text-xs text-emerald-400 hover:underline">Editar Produto →</button>
      </div>
    `;

    grid.appendChild(card);
  });
}

// ============================================================
// TAB 4: CATÁLOGO DE PRODUTOS & ESTOQUE
// ============================================================
function renderProdutos() {
  const tbody = document.getElementById('produtos-tbody');
  if (!tbody) return;
  tbody.innerHTML = '';

  appState.produtos.forEach(prod => {
    const lucroUnit = prod.precoVenda - prod.custoCompra;
    const margemUnit = prod.precoVenda > 0 ? (lucroUnit / prod.precoVenda) * 100 : 0;
    const alertaEstoque = prod.estoqueAtual <= prod.estoqueMinimo;

    const tr = document.createElement('tr');
    tr.className = "hover:bg-slate-900/60 transition";
    tr.innerHTML = `
      <td class="py-3 px-3 font-mono text-[11px] text-emerald-400 font-bold">${prod.sku || '-'}</td>
      <td class="py-3 px-3 font-bold text-white">${prod.nome}</td>
      <td class="py-3 px-3 text-slate-400 text-xs">${prod.categoria || 'Geral'}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-amber-400">${formatMoney(prod.custoCompra)}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-white">${formatMoney(prod.precoVenda)}</td>
      <td class="py-3 px-3 text-right font-mono font-bold text-emerald-400">${formatMoney(lucroUnit)}</td>
      <td class="py-3 px-3 text-center font-mono font-bold text-cyan-300">${formatPercent(margemUnit)}</td>
      <td class="py-3 px-3 text-center">
        <span class="px-2 py-0.5 rounded font-mono font-bold text-xs ${alertaEstoque ? 'bg-rose-950 text-rose-400 border border-rose-800' : 'bg-slate-800 text-slate-200'}">
          ${prod.estoqueAtual} un
        </span>
      </td>
      <td class="py-3 px-3 text-center">
        <div class="flex items-center justify-center gap-1.5">
          <button onclick="editarProduto('${prod.id}')" class="p-1 rounded text-slate-400 hover:text-emerald-400" title="Editar Produto">
            <i class="fa-solid fa-pen-to-square"></i>
          </button>
          <button onclick="excluirProduto('${prod.id}')" class="p-1 rounded text-slate-400 hover:text-rose-400" title="Excluir Produto">
            <i class="fa-solid fa-trash-can"></i>
          </button>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

// ============================================================
// TAB 5: CLIENTES & COMPRADORES
// ============================================================
function renderClientes() {
  const container = document.getElementById('clientes-list');
  if (!container) return;
  container.innerHTML = '';

  appState.clientes.forEach(cli => {
    const vendasDoCliente = appState.vendas.filter(v => v.clienteId === cli.id);
    const totalGasto = vendasDoCliente.filter(v => v.etapa === 'fechada').reduce((acc, v) => acc + (v.valorTotalVenda || 0), 0);
    const totalLucro = vendasDoCliente.filter(v => v.etapa === 'fechada').reduce((acc, v) => acc + (v.lucroLiquido || 0), 0);

    const cleanPhone = (cli.telefone || '').replace(/\D/g, '');
    const waUrl = `https://wa.me/${cleanPhone || appState.config.whatsappPadrao || '5532999292311'}?text=${encodeURIComponent(`Olá ${cli.nome}, tudo bem?`)}`;

    const card = document.createElement('div');
    card.className = "bg-slate-950/90 border border-slate-800 rounded-xl p-4 space-y-3 hover:border-emerald-500/50 transition";
    card.innerHTML = `
      <div class="flex items-start justify-between">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-full bg-emerald-950 text-emerald-400 flex items-center justify-center font-bold text-xs border border-emerald-800/60">
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
          <button onclick="editarCliente('${cli.id}')" class="w-7 h-7 rounded bg-slate-800 text-slate-300 hover:text-emerald-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-pen"></i>
          </button>
          <button onclick="excluirCliente('${cli.id}')" class="w-7 h-7 rounded bg-slate-800 text-slate-300 hover:text-rose-400 flex items-center justify-center text-xs">
            <i class="fa-solid fa-trash"></i>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-2 p-2 bg-slate-900 rounded-lg text-[11px] font-mono">
        <div>
          <span class="text-slate-400 block">Total Comprado (LTV):</span>
          <span class="text-white font-bold">${formatMoney(totalGasto)}</span>
        </div>
        <div>
          <span class="text-slate-400 block">Lucro Gerado:</span>
          <span class="text-emerald-400 font-bold">${formatMoney(totalLucro)}</span>
        </div>
      </div>

      <div class="text-[11px] text-slate-400 flex items-center justify-between">
        <span>${cli.cidade || 'Localização não informada'}</span>
        <span>${vendasDoCliente.length} vendas registradas</span>
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

// --- VENDA MODAL ---
function openNovaVendaModal() {
  document.getElementById('modal-venda-title').innerHTML = '<i class="fa-solid fa-cart-plus text-emerald-400"></i> Registrar Venda / Proposta';
  document.getElementById('venda-id').value = '';
  document.getElementById('venda-data').value = new Date().toISOString().slice(0, 16);
  document.getElementById('venda-qtd').value = 1;
  document.getElementById('venda-obs').value = '';

  popularSelectClientesVenda();
  popularSelectProdutosVenda();

  onProdutoSelecionadoNaVenda();
  openModal('modal-venda');
}

function popularSelectClientesVenda(selectedId) {
  const sel = document.getElementById('venda-cliente');
  if (!sel) return;
  sel.innerHTML = appState.clientes.map(c => `<option value="${c.id}" ${c.id === selectedId ? 'selected' : ''}>${c.nome} (${c.telefone})</option>`).join('');
}

function popularSelectProdutosVenda(selectedId) {
  const sel = document.getElementById('venda-produto');
  if (!sel) return;
  sel.innerHTML = appState.produtos.map(p => `<option value="${p.id}" ${p.id === selectedId ? 'selected' : ''}>${p.nome} - ${formatMoney(p.precoVenda)}</option>`).join('');
}

function onProdutoSelecionadoNaVenda() {
  const prodId = document.getElementById('venda-produto')?.value;
  const prod = appState.produtos.find(p => p.id === prodId);
  if (!prod) return;

  const qtd = parseFloat(document.getElementById('venda-qtd').value) || 1;
  document.getElementById('venda-total').value = (prod.precoVenda * qtd).toFixed(2);
  recalcularValoresVenda();
}

function recalcularValoresVenda(manualTotalEdit = false) {
  const prodId = document.getElementById('venda-produto')?.value;
  const prod = appState.produtos.find(p => p.id === prodId);
  const qtd = parseFloat(document.getElementById('venda-qtd').value) || 1;

  let valorTotal = parseFloat(document.getElementById('venda-total').value) || 0;
  if (!manualTotalEdit && prod) {
    valorTotal = prod.precoVenda * qtd;
    document.getElementById('venda-total').value = valorTotal.toFixed(2);
  }

  const custoUnit = prod ? prod.custoCompra : 0;
  const custoTotal = custoUnit * qtd;
  const lucro = valorTotal - custoTotal;
  const margem = valorTotal > 0 ? (lucro / valorTotal) * 100 : 0;

  document.getElementById('venda-custo-total').value = custoTotal.toFixed(2);
  document.getElementById('venda-lucro').value = lucro.toFixed(2);
  document.getElementById('venda-resumo-margem').textContent = `Margem: ${formatPercent(margem)}`;
  document.getElementById('venda-resumo-margem').className = `font-mono font-bold ${margem >= 40 ? 'text-emerald-400' : margem >= 20 ? 'text-cyan-400' : 'text-amber-400'}`;
}

function salvarVenda() {
  const id = document.getElementById('venda-id').value;
  const clienteId = document.getElementById('venda-cliente').value;
  const produtoId = document.getElementById('venda-produto').value;
  const prod = appState.produtos.find(p => p.id === produtoId);
  const data = document.getElementById('venda-data').value;
  const quantidade = parseFloat(document.getElementById('venda-qtd').value) || 1;
  const etapa = document.getElementById('venda-etapa').value;
  const formaPagamento = document.getElementById('venda-pagamento').value;
  const valorTotalVenda = parseFloat(document.getElementById('venda-total').value) || 0;
  const obs = document.getElementById('venda-obs').value;

  if (!clienteId || !produtoId) {
    alert("Por favor, selecione o cliente e o produto.");
    return;
  }

  const precoVendaUnitario = valorTotalVenda / (quantidade || 1);
  const custoCompraUnitario = prod ? prod.custoCompra : 0;
  const custoTotal = custoCompraUnitario * quantidade;
  const lucroLiquido = valorTotalVenda - custoTotal;
  const margem = valorTotalVenda > 0 ? (lucroLiquido / valorTotalVenda) * 100 : 0;

  if (id) {
    const idx = appState.vendas.findIndex(v => v.id === id);
    if (idx !== -1) {
      appState.vendas[idx] = {
        ...appState.vendas[idx],
        clienteId,
        produtoId,
        nomeProduto: prod ? prod.nome : '',
        data: new Date(data).toISOString(),
        quantidade,
        precoVendaUnitario,
        custoCompraUnitario,
        valorTotalVenda,
        custoTotal,
        lucroLiquido,
        margem,
        etapa,
        formaPagamento,
        obs
      };
    }
  } else {
    appState.vendas.unshift({
      id: 'v_' + Date.now(),
      clienteId,
      produtoId,
      nomeProduto: prod ? prod.nome : '',
      data: new Date(data).toISOString(),
      quantidade,
      precoVendaUnitario,
      custoCompraUnitario,
      valorTotalVenda,
      custoTotal,
      lucroLiquido,
      margem,
      etapa,
      formaPagamento,
      obs
    });
  }

  saveState();
  closeModal('modal-venda');
}

function editarVenda(id) {
  const venda = appState.vendas.find(v => v.id === id);
  if (!venda) return;

  document.getElementById('modal-venda-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-emerald-400"></i> Editar Venda';
  document.getElementById('venda-id').value = venda.id;
  document.getElementById('venda-data').value = new Date(venda.data).toISOString().slice(0, 16);
  document.getElementById('venda-qtd').value = venda.quantidade || 1;
  document.getElementById('venda-etapa').value = venda.etapa;
  document.getElementById('venda-pagamento').value = venda.formaPagamento || 'PIX';
  document.getElementById('venda-total').value = venda.valorTotalVenda;
  document.getElementById('venda-obs').value = venda.obs || '';

  popularSelectClientesVenda(venda.clienteId);
  popularSelectProdutosVenda(venda.produtoId);

  recalcularValoresVenda(true);
  openModal('modal-venda');
}

function excluirVenda(id) {
  if (confirm("Excluir este registro de venda?")) {
    appState.vendas = appState.vendas.filter(v => v.id !== id);
    saveState();
  }
}


// --- PRODUTO MODAL ---
function openNovoProdutoModal() {
  document.getElementById('modal-produto-title').innerHTML = '<i class="fa-solid fa-box text-emerald-400"></i> Novo Produto';
  document.getElementById('prod-id').value = '';
  document.getElementById('prod-sku').value = 'PRD-' + Math.floor(100 + Math.random() * 900);
  document.getElementById('prod-nome').value = '';
  document.getElementById('prod-categoria').value = '';
  document.getElementById('prod-custo').value = '';
  document.getElementById('prod-preco').value = '';
  document.getElementById('prod-estoque').value = 10;
  document.getElementById('prod-estoque-min').value = 2;

  recalcularMargemProdutoModal();
  openModal('modal-produto');
}

function recalcularMargemProdutoModal() {
  const custo = parseFloat(document.getElementById('prod-custo').value) || 0;
  const preco = parseFloat(document.getElementById('prod-preco').value) || 0;
  const lucro = preco - custo;
  const margem = preco > 0 ? (lucro / preco) * 100 : 0;

  document.getElementById('prod-preview-lucro').textContent = formatMoney(lucro);
  document.getElementById('prod-preview-margem').textContent = formatPercent(margem);
  document.getElementById('prod-preview-margem').className = `text-sm font-bold ${margem >= 40 ? 'text-emerald-400' : margem >= 20 ? 'text-cyan-400' : 'text-amber-400'}`;
}

function salvarProduto() {
  const id = document.getElementById('prod-id').value;
  const sku = document.getElementById('prod-sku').value.trim();
  const nome = document.getElementById('prod-nome').value.trim();
  const categoria = document.getElementById('prod-categoria').value.trim();
  const custoCompra = parseFloat(document.getElementById('prod-custo').value) || 0;
  const precoVenda = parseFloat(document.getElementById('prod-preco').value) || 0;
  const estoqueAtual = parseInt(document.getElementById('prod-estoque').value) || 0;
  const estoqueMinimo = parseInt(document.getElementById('prod-estoque-min').value) || 0;

  if (!nome) {
    alert("Informe o nome do produto.");
    return;
  }

  if (id) {
    const idx = appState.produtos.findIndex(p => p.id === id);
    if (idx !== -1) {
      appState.produtos[idx] = { ...appState.produtos[idx], sku, nome, categoria, custoCompra, precoVenda, estoqueAtual, estoqueMinimo };
    }
  } else {
    appState.produtos.push({
      id: 'prod_' + Date.now(),
      sku,
      nome,
      categoria,
      custoCompra,
      precoVenda,
      estoqueAtual,
      estoqueMinimo
    });
  }

  saveState();
  closeModal('modal-produto');
}

function editarProduto(id) {
  const p = appState.produtos.find(prod => prod.id === id);
  if (!p) return;

  document.getElementById('modal-produto-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-emerald-400"></i> Editar Produto';
  document.getElementById('prod-id').value = p.id;
  document.getElementById('prod-sku').value = p.sku || '';
  document.getElementById('prod-nome').value = p.nome;
  document.getElementById('prod-categoria').value = p.categoria || '';
  document.getElementById('prod-custo').value = p.custoCompra;
  document.getElementById('prod-preco').value = p.precoVenda;
  document.getElementById('prod-estoque').value = p.estoqueAtual;
  document.getElementById('prod-estoque-min').value = p.estoqueMinimo;

  recalcularMargemProdutoModal();
  openModal('modal-produto');
}

function excluirProduto(id) {
  if (confirm("Excluir este produto do catálogo?")) {
    appState.produtos = appState.produtos.filter(p => p.id !== id);
    saveState();
  }
}


// --- CLIENTE MODAL ---
function openNovoClienteModal(fromVenda = false) {
  document.getElementById('modal-cliente-title').innerHTML = '<i class="fa-solid fa-user-plus text-emerald-400"></i> Novo Cliente Comprador';
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

  // If venda modal was open, refresh client select
  popularSelectClientesVenda(newClientId);
}

function editarCliente(id) {
  const cli = appState.clientes.find(c => c.id === id);
  if (!cli) return;

  document.getElementById('modal-cliente-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-emerald-400"></i> Editar Cliente';
  document.getElementById('cli-id').value = cli.id;
  document.getElementById('cli-nome').value = cli.nome;
  document.getElementById('cli-telefone').value = cli.telefone;
  document.getElementById('cli-email').value = cli.email || '';
  document.getElementById('cli-cidade').value = cli.cidade || '';
  openModal('modal-cliente');
}

function excluirCliente(id) {
  if (confirm("Excluir este cliente e todas as suas vendas?")) {
    appState.clientes = appState.clientes.filter(c => c.id !== id);
    appState.vendas = appState.vendas.filter(v => v.clienteId !== id);
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
  downloadAnchor.setAttribute("download", `nexus_crm_vendas_backup_${new Date().toISOString().split('T')[0]}.json`);
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
      if (imported.produtos && imported.vendas) {
        appState = imported;
        saveState();
        alert("Backup importado com sucesso!");
        closeModal('modal-config');
      } else {
        alert("Arquivo JSON inválido para o CRM Vendas.");
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
  updateAllViews();
});
"""

with open("crm-vendas/crm_vendas.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("crm-vendas/crm_vendas.js written successfully.")
