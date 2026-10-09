const fs = require('fs');
const path = require('path');

const targetFile = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(targetFile, 'utf8');

const targetSnippet = `          <div class="p-6 pt-0 space-y-2">
            <a href="dentista/admin/index.html" target="_blank" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-black font-extrabold text-xs uppercase tracking-wider transition shadow-lg flex items-center justify-center gap-2" rel="noopener noreferrer">
              <span>Acessar Painel CRM Ao Vivo</span>
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </a>
          </div>
        </div>`;

const newCards = `          <div class="p-6 pt-0 space-y-2">
            <a href="dentista/admin/index.html" target="_blank" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-black font-extrabold text-xs uppercase tracking-wider transition shadow-lg flex items-center justify-center gap-2" rel="noopener noreferrer">
              <span>Acessar Painel CRM Ao Vivo</span>
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </a>
          </div>
        </div>

        <!-- Card: SunEco OS - CRM Solar, Estoque por Lote & Prazos (NOVO) -->
        <div data-category="crm" class="port-card glass-card rounded-3xl overflow-hidden border border-emerald-500/30 hover:border-emerald-500/70 shadow-xl hover:shadow-[0_0_35px_rgba(16,185,129,0.25)] transition-all duration-500 flex flex-col justify-between group">
          <div>
            <!-- Browser Mockup Window Header -->
            <div class="px-4 py-3 bg-[#111622] border-b border-white/10 flex items-center justify-between select-none">
              <div class="flex items-center gap-1.5">
                <span class="w-3 h-3 rounded-full bg-rose-500/80 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-amber-500/80 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-emerald-500/80 inline-block"></span>
              </div>
              <div class="px-3 py-0.5 rounded-md bg-nexus-black/60 border border-white/5 text-[10px] font-mono text-slate-400 flex items-center gap-1.5">
                <i class="fa-solid fa-lock text-[8px] text-emerald-400"></i>
                <span>suneco.eng.br/admin</span>
              </div>
              <span class="text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                CRM Solar Pro
              </span>
            </div>

            <!-- Preview Interactive Mockup Container -->
            <div class="relative bg-gradient-to-br from-emerald-950/40 via-[#0B131E] to-slate-950 p-6 border-b border-white/5 overflow-hidden">
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-2">
                  <div class="w-7 h-7 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 text-xs">
                    <i class="fa-solid fa-solar-panel"></i>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-white tracking-wide">SunEco OS • Painel Solar</div>
                    <div class="text-[9px] text-slate-400">Estoque por Lote & Lucro Real</div>
                  </div>
                </div>
                <span class="px-2 py-0.5 rounded-full text-[9px] font-mono font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                  Lucro Real: 42.8%
                </span>
              </div>

              <!-- Mini Pipeline Kanban Preview -->
              <div class="grid grid-cols-4 gap-2 mb-3">
                <div class="p-2 rounded-xl bg-white/5 border border-white/10 text-center">
                  <div class="text-[8px] uppercase font-bold text-sky-400 truncate">1. Leads Site</div>
                  <div class="text-xs font-mono font-bold text-white mt-1">4 novos</div>
                </div>
                <div class="p-2 rounded-xl bg-white/5 border border-white/10 text-center">
                  <div class="text-[8px] uppercase font-bold text-amber-400 truncate">2. Vistoria</div>
                  <div class="text-xs font-mono font-bold text-white mt-1">Amanhã</div>
                </div>
                <div class="p-2 rounded-xl bg-white/5 border border-white/10 text-center">
                  <div class="text-[8px] uppercase font-bold text-purple-400 truncate">3. CEMIG</div>
                  <div class="text-xs font-mono font-bold text-white mt-1">Parecer</div>
                </div>
                <div class="p-2 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-center">
                  <div class="text-[8px] uppercase font-bold text-emerald-400 truncate">4. Concluído</div>
                  <div class="text-xs font-mono font-bold text-emerald-300 mt-1">R$ 147k</div>
                </div>
              </div>

              <div class="flex items-center justify-between text-[10px] text-slate-400 font-mono pt-2 border-t border-white/5">
                <span>📦 Lotes c/ Preço Distinto</span>
                <span>🛡️ Anti-Spam por IP</span>
              </div>
            </div>

            <!-- Card Body Info -->
            <div class="p-6">
              <div class="flex items-center justify-between mb-2">
                <h3 class="font-outfit font-black text-2xl text-white group-hover:text-emerald-400 transition-colors">
                  SunEco OS • CRM Solar & Engenharia
                </h3>
                <span class="w-8 h-8 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center text-sm">
                  <i class="fa-solid fa-chart-pie"></i>
                </span>
              </div>
              <p class="text-slate-400 text-xs sm:text-sm leading-relaxed mb-4">
                CRM solar com estoque por lote de compra (custo real ponderado), gráfico de pizza de insumos, cálculo de margem líquida, tarefas, central de lembretes WhatsApp e integração anti-spam com a página pública.
              </p>
              <div class="flex flex-wrap gap-1.5">
                <span class="text-[10px] font-mono bg-emerald-500/10 text-emerald-300 px-2.5 py-1 rounded-md border border-emerald-500/20 font-bold">Estoque por Lote</span>
                <span class="text-[10px] font-mono bg-white/5 text-slate-300 px-2.5 py-1 rounded-md border border-white/5">Gráfico de Pizza</span>
                <span class="text-[10px] font-mono bg-white/5 text-slate-300 px-2.5 py-1 rounded-md border border-white/5">Prazos Fatais</span>
                <span class="text-[10px] font-mono bg-white/5 text-slate-300 px-2.5 py-1 rounded-md border border-white/5">Troca de Tema</span>
              </div>
            </div>
          </div>
          
          <div class="p-6 pt-0 space-y-2">
            <a href="energia-solar/admin/index.html" target="_blank" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 hover:to-emerald-500 text-white font-extrabold text-xs uppercase tracking-wider transition shadow-lg flex items-center justify-center gap-2" rel="noopener noreferrer">
              <span>Acessar SunEco OS (CRM)</span>
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </a>
            <a href="energia-solar/index.html" target="_blank" class="w-full py-2.5 rounded-xl bg-white/5 hover:bg-white/10 text-slate-300 font-bold text-xs uppercase tracking-wider transition border border-white/10 flex items-center justify-center gap-2" rel="noopener noreferrer">
              <span>Ver Site Público com Anti-Spam</span>
              <i class="fa-solid fa-solar-panel"></i>
            </a>
          </div>
        </div>

        <!-- Card: LexPro OS - CRM Jurídico & Prazos OAB (NOVO) -->
        <div data-category="crm" class="port-card glass-card rounded-3xl overflow-hidden border border-blue-500/30 hover:border-blue-500/70 shadow-xl hover:shadow-[0_0_35px_rgba(59,130,246,0.25)] transition-all duration-500 flex flex-col justify-between group">
          <div>
            <div class="px-4 py-3 bg-[#111622] border-b border-white/10 flex items-center justify-between select-none">
              <div class="flex items-center gap-1.5">
                <span class="w-3 h-3 rounded-full bg-rose-500/80 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-amber-500/80 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-emerald-500/80 inline-block"></span>
              </div>
              <div class="px-3 py-0.5 rounded-md bg-nexus-black/60 border border-white/5 text-[10px] font-mono text-slate-400 flex items-center gap-1.5">
                <i class="fa-solid fa-lock text-[8px] text-blue-400"></i>
                <span>lexpro.adv.br/admin</span>
              </div>
              <span class="text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded bg-blue-500/20 text-blue-400 border border-blue-500/30">
                CRM Jurídico
              </span>
            </div>

            <div class="relative bg-gradient-to-br from-blue-950/40 via-[#0B131E] to-slate-950 p-6 border-b border-white/5 overflow-hidden">
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-2">
                  <div class="w-7 h-7 rounded-lg bg-blue-500/20 border border-blue-500/40 flex items-center justify-center text-blue-400 text-xs">
                    <i class="fa-solid fa-scale-balanced"></i>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-white tracking-wide">LexPro OS • Painel Jurídico</div>
                    <div class="text-[9px] text-slate-400">Prazos Fatais & Custas Processuais</div>
                  </div>
                </div>
                <span class="px-2 py-0.5 rounded-full text-[9px] font-mono font-bold bg-blue-500/10 text-blue-400 border border-blue-500/30">
                  Prazos OAB Ativos
                </span>
              </div>

              <div class="grid grid-cols-4 gap-2 mb-3">
                <div class="p-2 rounded-xl bg-white/5 border border-white/10 text-center">
                  <div class="text-[8px] uppercase font-bold text-sky-400 truncate">1. Triagem</div>
                  <div class="text-xs font-mono font-bold text-white mt-1">3 novos</div>
                </div>
                <div class="p-2 rounded-xl bg-white/5 border border-white/10 text-center">
                  <div class="text-[8px] uppercase font-bold text-amber-400 truncate">2. Consulta</div>
                  <div class="text-xs font-mono font-bold text-white mt-1">Hoje</div>
                </div>
                <div class="p-2 rounded-xl bg-white/5 border border-white/10 text-center">
                  <div class="text-[8px] uppercase font-bold text-purple-400 truncate">3. Protocolo</div>
                  <div class="text-xs font-mono font-bold text-white mt-1">TJMG</div>
                </div>
                <div class="p-2 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-center">
                  <div class="text-[8px] uppercase font-bold text-emerald-400 truncate">4. Honorários</div>
                  <div class="text-xs font-mono font-bold text-emerald-300 mt-1">R$ 47.5k</div>
                </div>
              </div>

              <div class="flex items-center justify-between text-[10px] text-slate-400 font-mono pt-2 border-t border-white/5">
                <span>📂 Repositório de Petições</span>
                <span>💬 Lembrete de Audiência</span>
              </div>
            </div>

            <div class="p-6">
              <div class="flex items-center justify-between mb-2">
                <h3 class="font-outfit font-black text-2xl text-white group-hover:text-blue-400 transition-colors">
                  LexPro OS • CRM & Prazos OAB
                </h3>
                <span class="w-8 h-8 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center text-sm">
                  <i class="fa-solid fa-gavel"></i>
                </span>
              </div>
              <p class="text-slate-400 text-xs sm:text-sm leading-relaxed mb-4">
                Painel para escritórios de advocacia. Monitoramento de prazos fatais recursais, controle de custas e diligências por lote, funil de clientes e envio de notificações automáticas via WhatsApp.
              </p>
              <div class="flex flex-wrap gap-1.5">
                <span class="text-[10px] font-mono bg-blue-500/10 text-blue-300 px-2.5 py-1 rounded-md border border-blue-500/20 font-bold">Prazos Fatais</span>
                <span class="text-[10px] font-mono bg-white/5 text-slate-300 px-2.5 py-1 rounded-md border border-white/5">Diligências por Lote</span>
                <span class="text-[10px] font-mono bg-white/5 text-slate-300 px-2.5 py-1 rounded-md border border-white/5">WhatsApp Jurídico</span>
              </div>
            </div>
          </div>
          
          <div class="p-6 pt-0 space-y-2">
            <a href="advogado/admin/index.html" target="_blank" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-400 hover:to-blue-500 text-white font-extrabold text-xs uppercase tracking-wider transition shadow-lg flex items-center justify-center gap-2" rel="noopener noreferrer">
              <span>Acessar LexPro OS (CRM)</span>
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </a>
          </div>
        </div>`;

if (content.includes(targetSnippet)) {
  content = content.replace(targetSnippet, newCards);
  fs.writeFileSync(targetFile, content, 'utf8');
  console.log('✅ Novos cards de CRM (SunEco OS e LexPro OS) inseridos com sucesso no portfólio principal!');
} else {
  console.error('❌ Não foi possível encontrar o snippet de destino em index.html');
}
