/**
 * ELEVATE ALL NICHE WEBSITES WITH IMPECCABLE DESIGN & UNIQUE IDENTITIES
 * Eliminates generic templates, integrates specialized interactive tools,
 * and harmonizes branding with the CRM systems.
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

// ============================================================================
// 1. ADVOGADO (Valente & Associados • Advocacia de Alta Complexidade)
// ============================================================================
function buildAdvogadoHtml() {
  return `<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Valente & Associados • Advocacia de Alta Complexidade | Dr. Marcos Valente</title>
  <meta name="description" content="Defesa jurídica estratégica e confidencial em Direito de Família, Sucessões, Blindagem Patrimonial e Contratos Empresariais. OAB/MG 128.490." />
  
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚖️</text></svg>" />

  <!-- Fonts: Playfair Display + Plus Jakarta Sans + JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;0,900;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            serif: ['Playfair Display', 'serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
          colors: {
            law: {
              black: '#070A12',
              card: '#0D1424',
              border: '#1E2B47',
              gold: '#C5A880',
              goldLight: '#E8D5B5',
              goldDark: '#8C6D42',
              navy: '#101B33',
              accent: '#3B82F6'
            }
          }
        }
      }
    };
  </script>
</head>
<body class="bg-[#070A12] text-slate-100 font-sans antialiased selection:bg-law-gold selection:text-black">

  <aside class="bg-[#0A101D] border-b border-law-border/70 py-2.5 px-4 text-xs font-semibold">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2.5 text-law-goldLight">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="tracking-wide">Plantão Jurídico Confidencial • Dr. Marcos Valente • OAB/MG 128.490</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden md:inline text-slate-400">Sigilo Perpétuo pelo Código de Ética da OAB</span>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Dr.%20Marcos%20Valente!%20Gostaria%20de%20uma%20consulta%20jur%C3%ADdica%20confidencial." target="_blank" class="text-law-gold hover:text-white font-bold flex items-center gap-1.5 transition">
          <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
          <span>(32) 99929-2311</span>
        </a>
      </div>
    </div>
  </aside>

  <header class="sticky top-0 z-50 bg-[#070A12]/95 backdrop-blur-md border-b border-law-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3.5 group">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-law-gold via-amber-600 to-law-goldDark flex items-center justify-center text-black text-xl shadow-lg shadow-amber-900/20 font-black group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-scale-balanced"></i>
        </div>
        <div>
          <div class="font-serif font-black text-2xl text-white tracking-wide flex items-center gap-2">
            VALENTE <span class="text-law-gold font-sans font-light">& ASSOCIADOS</span>
          </div>
          <span class="block text-[9px] font-mono tracking-widest uppercase text-law-goldLight font-bold -mt-0.5">
            Advocacia de Alta Complexidade • OAB/MG 128.490
          </span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-8 text-xs font-bold uppercase tracking-wider text-slate-300">
        <a href="#areas" class="hover:text-law-gold transition">Áreas de Atuação</a>
        <a href="#diagnostico" class="hover:text-law-gold transition flex items-center gap-1.5 text-law-gold">
          <i class="fa-solid fa-clipboard-check text-xs"></i> Diagnóstico Confidencial
        </a>
        <a href="#diferenciais" class="hover:text-law-gold transition">Quebra de Objeções</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="admin/index.html" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-law-card hover:bg-neutral-800 text-xs font-bold text-law-gold border border-law-border transition" title="Acessar LexPro OS">
          <i class="fa-solid fa-lock text-[10px]"></i> Painel do Escritório
        </a>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Dr.%20Marcos%20Valente!%20Gostaria%20de%20uma%20consulta%20jur%C3%ADdica%20confidencial." target="_blank" class="px-5 py-2.5 rounded-full bg-gradient-to-r from-law-gold to-amber-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-amber-900/30 transition transform hover:scale-105">
          Consulta Confidencial
        </a>
      </div>
    </div>
  </header>

  <section class="relative py-16 md:py-24 overflow-hidden border-b border-law-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-law-gold/10 border border-law-gold/30 text-law-gold text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-shield-halved text-xs"></i>
            Defesa Firme e Rigorosa do Seu Patrimônio & Família
          </div>

          <h1 class="font-serif font-black text-4xl sm:text-6xl text-white tracking-tight leading-[1.12]">
            Segurança Jurídica Estratégica em <span class="text-transparent bg-clip-text bg-gradient-to-r from-law-goldLight via-law-gold to-amber-600">Casos Complexos.</span>
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl">
            Atuação de alta precisão em inventários litigiosos e cartorários, blindagem patrimonial familiar, partilhas judiciais, assessoria imobiliária e contencioso estratégico. Parecer de risco fundamentado antes de protocolar qualquer ação.
          </p>

          <div class="p-4 rounded-2xl bg-law-card border border-law-gold/40 shadow-xl max-w-xl">
            <div class="flex items-center gap-2 text-law-gold font-bold text-xs uppercase tracking-wider mb-1">
              <i class="fa-solid fa-gavel"></i> Compromisso Ético & Honorários Vinculados ao Êxito
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              Você não gasta com custas processuais ou ações desnecessárias. Fazemos uma auditoria prévia da documentação para apontar as chances reais de vitória e viabilidade de acordos amigáveis com economia de até 40% em tributos de herança.
            </p>
          </div>

          <div class="flex flex-col sm:flex-row gap-4 pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Dr.%20Marcos%20Valente!%20Gostaria%20de%20uma%20consulta%20jur%C3%ADdica%20confidencial." target="_blank" class="px-8 py-4 rounded-xl bg-gradient-to-r from-law-gold to-amber-600 hover:opacity-95 text-black font-black text-xs uppercase tracking-wider shadow-xl shadow-amber-900/30 text-center flex items-center justify-center gap-2.5 transition transform hover:scale-105">
              <i class="fa-brands fa-whatsapp text-base"></i>
              <span>Falar Diretamente com o Dr. Marcos Valente</span>
            </a>
            <a href="#diagnostico" class="px-8 py-4 rounded-xl bg-law-card hover:bg-neutral-800 text-white font-bold text-xs uppercase tracking-wider border border-law-border text-center flex items-center justify-center gap-2">
              <i class="fa-solid fa-clipboard-check text-law-gold"></i>
              <span>Fazer Diagnóstico Pré-Processual</span>
            </a>
          </div>

          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-law-border/60 text-center">
            <div class="p-3 rounded-2xl bg-law-card/50 border border-law-border/50">
              <div class="font-serif font-black text-2xl text-law-gold">+2.400</div>
              <div class="text-[11px] text-slate-400 font-semibold">Causas Concluídas</div>
            </div>
            <div class="p-3 rounded-2xl bg-law-card/50 border border-law-border/50">
              <div class="font-serif font-black text-2xl text-emerald-400">97%</div>
              <div class="text-[11px] text-slate-400 font-semibold">Resolução Favorável</div>
            </div>
            <div class="p-3 rounded-2xl bg-law-card/50 border border-law-border/50">
              <div class="font-serif font-black text-2xl text-white">20 Anos</div>
              <div class="text-[11px] text-slate-400 font-semibold">Prática Jurídica MG/SP</div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="bg-law-card p-8 rounded-3xl border border-law-border shadow-2xl relative overflow-hidden space-y-6">
            <div class="flex items-center gap-4 pb-6 border-b border-law-border">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-law-gold to-amber-800 text-black flex items-center justify-center text-2xl font-serif font-bold shadow-lg">
                MV
              </div>
              <div>
                <h3 class="font-serif font-bold text-xl text-white">Dr. Marcos Valente</h3>
                <p class="text-xs text-law-gold font-semibold">Sócio Fundador • OAB/MG 128.490</p>
                <p class="text-[11px] text-slate-400 mt-0.5">Especialista em Direito de Família, Sucessões & Imobiliário</p>
              </div>
            </div>

            <div class="space-y-3.5">
              <div class="p-3.5 rounded-xl bg-[#0A101D] border border-law-border flex items-start gap-3">
                <i class="fa-solid fa-file-shield text-law-gold text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">1. Análise de Risco Preliminar</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Exame rigoroso da documentação e jurisprudência dominante antes de propor a ação.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#0A101D] border border-law-border flex items-start gap-3">
                <i class="fa-solid fa-handshake-angle text-emerald-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">2. Prioridade para Soluções Extrajudiciais</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Inventários e divórcios concluídos em cartório em semanas, sem desgastes em tribunais.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#0A101D] border border-law-border flex items-start gap-3">
                <i class="fa-solid fa-clock-rotate-left text-cyan-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">3. Gestão Digital de Prazos Fatais (LexPro OS)</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Nosso escritório opera com CRM integrado de monitoramento contínuo de publicações do Diário Oficial.</p>
                </div>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-law-gold/10 border border-law-gold/30 text-center">
              <span class="text-xs font-bold text-law-goldLight flex items-center justify-center gap-1.5">
                <i class="fa-solid fa-lock text-law-gold"></i> Atendimento 100% Protegido por Sigilo Ético
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAGNÓSTICO JURÍDICO INTERATIVO -->
  <section id="diagnostico" class="py-20 bg-[#090D18] border-b border-law-border/60">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold uppercase tracking-widest text-law-gold bg-law-gold/10 px-3.5 py-1.5 rounded-full border border-law-gold/30">
          Ferramenta Pré-Processual Interativa
        </span>
        <h2 class="font-serif font-black text-3xl sm:text-4xl text-white mt-4">
          Diagnóstico de Viabilidade Jurídica
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2">
          Selecione a área do seu caso para receber uma estimativa de tramitação, documentos necessários e recomendação estratégica do Dr. Marcos Valente.
        </p>
      </div>

      <div class="bg-law-card p-6 sm:p-10 rounded-3xl border border-law-border shadow-2xl space-y-6">
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">1. Qual a natureza da sua demanda?</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <button type="button" onclick="selectCaseType('inventario')" id="btn-case-inventario" class="case-btn active p-3 rounded-xl bg-law-gold text-black font-bold text-xs text-center border border-law-gold transition">
              Inventário & Herança
            </button>
            <button type="button" onclick="selectCaseType('divorcio')" id="btn-case-divorcio" class="case-btn p-3 rounded-xl bg-[#070A12] text-slate-300 hover:text-white font-bold text-xs text-center border border-law-border transition">
              Divórcio & Partilha
            </button>
            <button type="button" onclick="selectCaseType('imobiliario')" id="btn-case-imobiliario" class="case-btn p-3 rounded-xl bg-[#070A12] text-slate-300 hover:text-white font-bold text-xs text-center border border-law-border transition">
              Imóveis & Contratos
            </button>
            <button type="button" onclick="selectCaseType('empresarial')" id="btn-case-empresarial" class="case-btn p-3 rounded-xl bg-[#070A12] text-slate-300 hover:text-white font-bold text-xs text-center border border-law-border transition">
              Empresarial & Societário
            </button>
          </div>
        </div>

        <div class="p-5 rounded-2xl bg-[#070A12] border border-law-border space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-law-gold uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-scale-balanced"></i> Parecer Preliminar Estratégico
            </span>
            <span id="diag-time" class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded border border-emerald-500/30">
              Prazo Estimado: 15 a 45 dias
            </span>
          </div>

          <h4 id="diag-title" class="font-serif font-bold text-lg text-white">
            Inventário Extrajudicial em Cartório de Notas
          </h4>

          <p id="diag-desc" class="text-xs text-slate-300 leading-relaxed">
            Se todos os herdeiros forem maiores, capazes e houver consenso na partilha, o inventário pode ser lavrado diretamente por escritura pública em cartório, evitando anos de fila no Fórum e reduzindo custos com custas judiciais.
          </p>

          <div class="pt-2 border-t border-law-border/60 flex flex-wrap gap-2 text-[11px] text-slate-400">
            <span class="font-bold text-slate-300">Documentação-base:</span>
            <span id="diag-docs" class="text-law-goldLight">Certidões de óbito e casamento, matrícula atualizada dos imóveis, certidão negativa fiscal (RFB e SEFAZ).</span>
          </div>
        </div>

        <div class="pt-2">
          <a id="diag-wa-btn" href="https://wa.me/5532999292311?text=Ol%C3%A1%20Dr.%20Marcos%20Valente!%20Fiz%20o%20diagn%C3%B3stico%20de%20Invent%C3%A1rio%20e%20gostaria%20de%20analisar%20meu%20caso." target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-law-gold to-amber-600 hover:opacity-95 text-black font-black text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition transform hover:scale-[1.01]">
            <i class="fa-brands fa-whatsapp text-base"></i>
            <span>Encaminhar Dados para Avaliação Formal do Dr. Marcos Valente</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Áreas de Atuação -->
  <section id="areas" class="py-20 max-w-7xl mx-auto px-4 sm:px-6">
    <div class="text-center max-w-2xl mx-auto mb-14">
      <span class="text-xs font-bold uppercase tracking-widest text-law-gold bg-law-gold/10 px-3.5 py-1.5 rounded-full border border-law-gold/30">
        Especialidades Jurídicas
      </span>
      <h2 class="font-serif font-black text-3xl sm:text-4xl text-white mt-4">
        Prática Jurídica Estratégica
      </h2>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-law-card p-8 rounded-3xl border border-law-border hover:border-law-gold transition space-y-4">
        <div class="w-12 h-12 rounded-2xl bg-law-gold/10 text-law-gold flex items-center justify-center text-xl">
          <i class="fa-solid fa-users"></i>
        </div>
        <h3 class="font-serif font-bold text-xl text-white">Família & Sucessões</h3>
        <p class="text-slate-400 text-xs leading-relaxed">
          Inventários ágeis, partilhas judiciais e amigáveis, divórcios com planejamento patrimonial, fixação e revisão de alimentos com proteção ao patrimônio familiar.
        </p>
      </div>

      <div class="bg-law-card p-8 rounded-3xl border-2 border-law-gold shadow-xl shadow-amber-950/20 space-y-4">
        <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-law-gold flex items-center justify-center text-xl">
          <i class="fa-solid fa-building-shield"></i>
        </div>
        <h3 class="font-serif font-bold text-xl text-white">Blindagem & Holdings</h3>
        <p class="text-slate-400 text-xs leading-relaxed">
          Estruturação de holding familiar e patrimonial para proteção de bens de sócios contra riscos operacionais, tributários e planejamento sucessório antecipado.
        </p>
      </div>

      <div class="bg-law-card p-8 rounded-3xl border-border hover:border-law-gold transition space-y-4">
        <div class="w-12 h-12 rounded-2xl bg-law-gold/10 text-law-gold flex items-center justify-center text-xl">
          <i class="fa-solid fa-landmark"></i>
        </div>
        <h3 class="font-serif font-bold text-xl text-white">Direito Imobiliário & Contratos</h3>
        <p class="text-slate-400 text-xs leading-relaxed">
          Regularização de imóveis, usucapião, rescisões contratuais, assessoria em aquisições de alto valor e due diligence registral completa.
        </p>
      </div>
    </div>
  </section>

  <!-- Footer Nobre -->
  <footer class="bg-[#05070D] border-t border-law-border/60 py-12 text-xs text-slate-400">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <span class="font-serif font-bold text-white text-base">Valente & Associados Advocacia</span>
        <p class="text-[11px] text-slate-500 mt-1">Dr. Marcos Valente • OAB/MG 128.490 • Todos os direitos reservados 2026.</p>
      </div>
      <div class="flex items-center gap-6">
        <a href="admin/index.html" target="_blank" class="text-law-gold hover:underline font-bold flex items-center gap-1">
          <i class="fa-solid fa-shield-halved text-xs"></i> Acesso Restrito (LexPro OS)
        </a>
        <a href="../index.html" class="hover:text-white transition">Voltar ao Portfólio Geral</a>
      </div>
    </div>
  </footer>

  <script>
    const CASES_DATA = {
      inventario: {
        title: 'Inventário Extrajudicial em Cartório de Notas',
        time: 'Prazo Estimado: 15 a 45 dias',
        desc: 'Havendo consenso entre herdeiros maiores, o inventário ocorre por escritura pública sem depender da pauta judicial, economizando até 40% em custas.',
        docs: 'Certidão de óbito, documentos dos herdeiros, matrícula atualizada dos imóveis e certidões negativas fiscais.',
        waText: 'Olá Dr. Marcos Valente! Gostaria de consultar sobre Inventário e Partilha de Bens.'
      },
      divorcio: {
        title: 'Divórcio Consensual com Partilha Estruturada',
        time: 'Prazo Estimado: 7 a 20 dias',
        desc: 'Resolução amigável com minuta contratual de partilha e guarda que preserva os bens e evita litígios desgastantes em audiências.',
        docs: 'Certidão de casamento atualizada, pacto antenupcial (se houver) e relação dos bens a partilhar.',
        waText: 'Olá Dr. Marcos Valente! Gostaria de consultar sobre Divórcio e Partilha de Bens.'
      },
      imobiliario: {
        title: 'Due Diligence Imobiliária & Regularização de Matrícula',
        time: 'Prazo Estimado: 10 a 30 dias',
        desc: 'Auditoria de certidões e histórico dos proprietários para blindar o comprador contra risco de fraude a credores ou evicção.',
        docs: 'Matrícula vintenária do imóvel, certidões da Justiça Federal e Estadual, CND de tributos municipais.',
        waText: 'Olá Dr. Marcos Valente! Gostaria de consultar sobre Direito Imobiliário e Contratos.'
      },
      empresarial: {
        title: 'Blindagem Patrimonial & Holding Familiar',
        time: 'Prazo Estimado: 30 a 60 dias',
        desc: 'Transferência de bens para pessoa jurídica patrimonial, reduzindo ITCMD de sucessão e blindando o patrimônio contra execuções civis.',
        docs: 'Contratos sociais das empresas dos sócios, relação do acervo patrimonial e certidões dos titulares.',
        waText: 'Olá Dr. Marcos Valente! Gostaria de consultar sobre Holding Familiar e Blindagem Patrimonial.'
      }
    };

    function selectCaseType(key) {
      document.querySelectorAll('.case-btn').forEach(b => {
        b.classList.remove('bg-law-gold', 'text-black', 'active');
        b.classList.add('bg-[#070A12]', 'text-slate-300');
      });

      const btn = document.getElementById('btn-case-' + key);
      if (btn) {
        btn.classList.remove('bg-[#070A12]', 'text-slate-300');
        btn.classList.add('bg-law-gold', 'text-black', 'active');
      }

      const data = CASES_DATA[key];
      if (!data) return;

      document.getElementById('diag-title').textContent = data.title;
      document.getElementById('diag-time').textContent = data.time;
      document.getElementById('diag-desc').textContent = data.desc;
      document.getElementById('diag-docs').textContent = data.docs;
      document.getElementById('diag-wa-btn').setAttribute('href', 'https://wa.me/5532999292311?text=' + encodeURIComponent(data.waText));
    }
  </script>
</body>
</html>`;
}

// ============================================================================
// 2. ARQUITETO (StudioDesign • Arq. Marcelo Faria • CAU/BR 128.490)
// ============================================================================
function buildArquitetoHtml() {
  return `<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>StudioDesign Arquitetura & Interiores | Arq. Marcelo Faria</title>
  <meta name="description" content="Projetos arquitetônicos residenciais e comerciais de alto padrão com modelagem BIM 3D, memorial descritivo e cronograma travado de obras. CAU/BR 128.490." />
  
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📐</text></svg>" />

  <!-- Fonts: Cinzel (Serif Arquitetônica) + Plus Jakarta Sans + JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            serif: ['Cinzel', 'serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
          colors: {
            arch: {
              black: '#0A0C10',
              card: '#121622',
              border: '#1E2538',
              copper: '#C25E34',
              copperLight: '#E88B64',
              concrete: '#737B8B',
              sand: '#EAE6DF'
            }
          }
        }
      }
    };
  </script>
</head>
<body class="bg-[#0A0C10] text-slate-100 font-sans antialiased selection:bg-arch-copper selection:text-white">

  <!-- Top Strip -->
  <aside class="bg-[#0E121A] border-b border-arch-border/70 py-2.5 px-4 text-xs font-semibold">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2.5 text-arch-copperLight">
        <span class="w-2 h-2 rounded-full bg-arch-copper animate-pulse"></span>
        <span>StudioDesign • Arq. Marcelo Faria • Registro Oficial CAU/BR 128.490</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden md:inline text-slate-400 font-mono text-[11px]">Compatibilização BIM & Visualização 3D Fotorrealista</span>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Arq.%20Marcelo%20Faria!%20Gostaria%20de%20apresentar%20meu%20projeto." target="_blank" class="text-arch-copperLight hover:text-white font-bold flex items-center gap-1.5 transition">
          <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
          <span>(32) 99929-2311</span>
        </a>
      </div>
    </div>
  </aside>

  <!-- Header -->
  <header class="sticky top-0 z-50 bg-[#0A0C10]/95 backdrop-blur-md border-b border-arch-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3.5 group">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-arch-copper to-amber-700 flex items-center justify-center text-white text-xl shadow-lg shadow-orange-950/20 font-black group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-compass-drafting"></i>
        </div>
        <div>
          <div class="font-serif font-black text-2xl text-white tracking-wide flex items-center gap-2">
            STUDIO<span class="text-arch-copper">DESIGN</span>
          </div>
          <span class="block text-[9px] font-mono tracking-widest uppercase text-slate-400 font-bold -mt-0.5">
            Arquitetura & Urbanismo • CAU/BR 128.490
          </span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-8 text-xs font-bold uppercase tracking-wider text-slate-300">
        <a href="#projetos" class="hover:text-arch-copper transition">Obras & Portfólio</a>
        <a href="#calculadora" class="hover:text-arch-copper transition flex items-center gap-1.5 text-arch-copperLight">
          <i class="fa-solid fa-calculator text-xs"></i> Simulador de Obra por m²
        </a>
        <a href="#diferenciais" class="hover:text-arch-copper transition">Garantia sem Estouro</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="admin/index.html" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-arch-card hover:bg-neutral-800 text-xs font-bold text-arch-copperLight border border-arch-border transition" title="Acessar StudioDesign OS">
          <i class="fa-solid fa-lock text-[10px]"></i> Painel do Escritório
        </a>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Arq.%20Marcelo!%20Gostaria%20de%20agendar%20uma%20reuni%C3%A3o%20de%20briefing." target="_blank" class="px-5 py-2.5 rounded-full bg-gradient-to-r from-arch-copper to-amber-600 hover:opacity-95 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-orange-950/30 transition transform hover:scale-105">
          Agendar Briefing 3D
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Editorial Arquitetônico -->
  <section class="relative py-16 md:py-24 overflow-hidden border-b border-arch-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-arch-copper/10 border border-arch-copper/30 text-arch-copperLight text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-cube text-xs"></i>
            Projetos que Eliminam 100% dos Erros e Atrasos na Obra
          </div>

          <h1 class="font-serif font-black text-4xl sm:text-6xl text-white tracking-tight leading-[1.12]">
            Não Imagine Seu Imóvel. <span class="text-transparent bg-clip-text bg-gradient-to-r from-arch-copperLight via-arch-copper to-amber-500">Veja Ele Pronto</span> Antes de Quebrar a Primeira Parede.
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl">
            Projetos arquitetônicos residenciais e comerciais com compatibilização BIM 3D, detalhamento executivo completo e lista de compras travada para você não ter surpresas com custos ou empreiteiros.
          </p>

          <div class="p-4 rounded-2xl bg-arch-card border border-arch-copper/40 shadow-xl max-w-xl">
            <div class="flex items-center gap-2 text-arch-copperLight font-bold text-xs uppercase tracking-wider mb-1">
              <i class="fa-solid fa-shield-check text-arch-copper"></i> Quebra de Objeção: Custo & Prazo de Obra Travados
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              O maior medo de quem reforma é o orçamento dobrar no meio da execução. No StudioDesign você recebe a planilha exata de materiais por lote e o cronograma dia a dia para fiscalizar a equipe sem pagar a mais.
            </p>
          </div>

          <div class="flex flex-col sm:flex-row gap-4 pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Arq.%20Marcelo!%20Gostaria%20de%20fazer%20o%20briefing%20do%20meu%20projeto." target="_blank" class="px-8 py-4 rounded-xl bg-gradient-to-r from-arch-copper to-amber-600 hover:opacity-95 text-white font-black text-xs uppercase tracking-wider shadow-xl shadow-orange-950/30 text-center flex items-center justify-center gap-2.5 transition transform hover:scale-105">
              <i class="fa-brands fa-whatsapp text-base"></i>
              <span>Falar Diretamente com o Arquiteto</span>
            </a>
            <a href="#calculadora" class="px-8 py-4 rounded-xl bg-arch-card hover:bg-neutral-800 text-white font-bold text-xs uppercase tracking-wider border border-arch-border text-center flex items-center justify-center gap-2">
              <i class="fa-solid fa-calculator text-arch-copper"></i>
              <span>Simular Obra por m²</span>
            </a>
          </div>

          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-arch-border/60 text-center">
            <div class="p-3 rounded-2xl bg-arch-card/50 border border-arch-border/50">
              <div class="font-serif font-black text-2xl text-arch-copper">+180</div>
              <div class="text-[11px] text-slate-400 font-semibold">Obras Concluídas</div>
            </div>
            <div class="p-3 rounded-2xl bg-arch-card/50 border border-arch-border/50">
              <div class="font-serif font-black text-2xl text-emerald-400">Zero</div>
              <div class="text-[11px] text-slate-400 font-semibold">Desperdício em Obra</div>
            </div>
            <div class="p-3 rounded-2xl bg-arch-card/50 border border-arch-border/50">
              <div class="font-serif font-black text-2xl text-white">8K</div>
              <div class="text-[11px] text-slate-400 font-semibold">Render Fotorrealista</div>
            </div>
          </div>
        </div>

        <!-- Right: Card do Arquiteto Titular -->
        <div class="lg:col-span-5">
          <div class="bg-arch-card p-8 rounded-3xl border border-arch-border shadow-2xl relative overflow-hidden space-y-6">
            <div class="flex items-center gap-4 pb-6 border-b border-arch-border">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-arch-copper to-amber-700 text-white flex items-center justify-center text-2xl font-serif font-bold shadow-lg">
                MF
              </div>
              <div>
                <h3 class="font-serif font-bold text-xl text-white">Arq. Marcelo Faria</h3>
                <p class="text-xs text-arch-copper font-semibold">Arquiteto Titular • CAU/BR 128.490</p>
                <p class="text-[11px] text-slate-400 mt-0.5">Especialista em Residências de Alto Padrão & BIM</p>
              </div>
            </div>

            <div class="space-y-3.5">
              <div class="p-3.5 rounded-xl bg-[#0A0C10] border border-arch-border flex items-start gap-3">
                <i class="fa-solid fa-cube text-arch-copper text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">1. Modelagem Tridimensional BIM</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Instalações elétricas, hidráulicas e estruturais integradas sem conflito de tubulações.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#0A0C10] border border-arch-border flex items-start gap-3">
                <i class="fa-solid fa-list-check text-emerald-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">2. Memorial Descritivo de Compras</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Quantitativo exato de pisos, iluminação, marcenaria e acabamentos por lote.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#0A0C10] border border-arch-border flex items-start gap-3">
                <i class="fa-solid fa-calendar-check text-cyan-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">3. Acompanhamento de Obras (StudioDesign OS)</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Painel com fotos semanais de evolução e aprovação de etapas pelo cliente.</p>
                </div>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-arch-copper/10 border border-arch-copper/30 text-center">
              <span class="text-xs font-bold text-arch-copperLight flex items-center justify-center gap-1.5">
                <i class="fa-solid fa-stamp text-arch-copper"></i> RRT Emitida com Responsabilidade Técnica Oficial
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CALCULADORA INTERATIVA DE OBRA POR M² -->
  <section id="calculadora" class="py-20 bg-[#0D1017] border-b border-arch-border/60">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold uppercase tracking-widest text-arch-copper bg-arch-copper/10 px-3.5 py-1.5 rounded-full border border-arch-copper/30">
          Simulador Interativo Exclusivo
        </span>
        <h2 class="font-serif font-black text-3xl sm:text-4xl text-white mt-4">
          Estimativa de Projeto & Cronograma
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2">
          Ajuste a metragem estimada do imóvel para calcular o tempo de desenvolvimento do projeto 3D e as etapas de entrega técnica.
        </p>
      </div>

      <div class="bg-arch-card p-6 sm:p-10 rounded-3xl border border-arch-border shadow-2xl space-y-8">
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-bold uppercase tracking-wider text-slate-300">Área Construída / Reforma:</span>
            <span id="area-val-display" class="font-mono text-xl font-black text-arch-copper">180 m²</span>
          </div>
          <input 
            type="range" 
            id="area-slider" 
            min="40" 
            max="600" 
            step="10" 
            value="180" 
            oninput="updateArchCalc(this.value)" 
            class="w-full h-2.5 bg-[#0A0C10] rounded-lg appearance-none cursor-pointer accent-arch-copper"
          />
          <div class="flex justify-between text-[10px] text-slate-500 font-mono mt-1.5">
            <span>40 m² (Apartamento compacto)</span>
            <span>300 m² (Casa de Condomínio)</span>
            <span>600 m² (Mansão / Comercial)</span>
          </div>
        </div>

        <!-- Resultados do Dimensionamento -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div class="p-4 rounded-2xl bg-[#0A0C10] border border-arch-border text-center">
            <div class="text-[10px] uppercase font-bold text-slate-400">Prazo Estudo Preliminar 3D</div>
            <div id="calc-prazo" class="font-serif font-bold text-xl text-white mt-1">20 a 25 dias</div>
            <span class="text-[10px] text-arch-copperLight">Render fotorrealista 8K</span>
          </div>

          <div class="p-4 rounded-2xl bg-[#0A0C10] border border-arch-border text-center">
            <div class="text-[10px] uppercase font-bold text-slate-400">Detalhamento BIM</div>
            <div id="calc-pranchas" class="font-serif font-bold text-xl text-cyan-400 mt-1">35 Pranchas</div>
            <span class="text-[10px] text-slate-400">Projetos Executivos</span>
          </div>

          <div class="p-4 rounded-2xl bg-[#0A0C10] border border-arch-border text-center">
            <div class="text-[10px] uppercase font-bold text-slate-400">Economia com BIM</div>
            <div id="calc-economia" class="font-serif font-bold text-xl text-emerald-400 mt-1">Até 15% da Obra</div>
            <span class="text-[10px] text-emerald-300">Sem quebra-quebra extra</span>
          </div>
        </div>

        <div class="pt-2">
          <a id="arch-wa-btn" href="https://wa.me/5532999292311?text=Ol%C3%A1%20Arq.%20Marcelo!%20Simulei%20um%20projeto%20de%20180m%C2%B2%20no%20site%20e%20gostaria%20de%20agendar%20uma%20conversa." target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-arch-copper to-amber-600 hover:opacity-95 text-white font-black text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition transform hover:scale-[1.01]">
            <i class="fa-brands fa-whatsapp text-base"></i>
            <span>Solicitar Reunião de Briefing para Minha Metragem</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-[#06080B] border-t border-arch-border/60 py-12 text-xs text-slate-400">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <span class="font-serif font-bold text-white text-base">StudioDesign Arquitetura Contemporânea</span>
        <p class="text-[11px] text-slate-500 mt-1">Arq. Marcelo Faria • CAU/BR 128.490 • Todos os direitos reservados 2026.</p>
      </div>
      <div class="flex items-center gap-6">
        <a href="admin/index.html" target="_blank" class="text-arch-copperLight hover:underline font-bold flex items-center gap-1">
          <i class="fa-solid fa-lock text-xs"></i> Acesso Restrito (StudioDesign OS)
        </a>
        <a href="../index.html" class="hover:text-white transition">Voltar ao Portfólio Geral</a>
      </div>
    </div>
  </footer>

  <script>
    function updateArchCalc(val) {
      const area = parseInt(val, 10);
      document.getElementById('area-val-display').textContent = area + ' m²';

      let prazo = '15 a 20 dias';
      let pranchas = '25 Pranchas';
      let economia = 'Até 12% da Obra';

      if (area > 350) {
        prazo = '35 a 45 dias';
        pranchas = '60+ Pranchas';
        economia = 'Até 18% da Obra';
      } else if (area > 150) {
        prazo = '25 a 30 dias';
        pranchas = '40 Pranchas';
        economia = 'Até 15% da Obra';
      }

      document.getElementById('calc-prazo').textContent = prazo;
      document.getElementById('calc-pranchas').textContent = pranchas;
      document.getElementById('calc-economia').textContent = economia;

      const waMsg = 'Olá Arq. Marcelo! Simulei um projeto de ' + area + 'm² no site do StudioDesign e gostaria de agendar um briefing.';
      document.getElementById('arch-wa-btn').setAttribute('href', 'https://wa.me/5532999292311?text=' + encodeURIComponent(waMsg));
    }
  </script>
</body>
</html>`;
}

// ============================================================================
// 3. BANHO E TOSA (PetCare Deluxe • Dra. Luna Silveira • CRMV-MG 128.490)
// ============================================================================
function buildBanhoETosaHtml() {
  return `<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PetCare Deluxe • Estética Animal & Vet | Dra. Luna Silveira</title>
  <meta name="description" content="O spa boutique que seu melhor amigo merece. Banho ozonizado, tosa na tesoura, produtos hipoalergênicos e Táxi Dog climatizado. CRMV-MG 128.490." />
  
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐾</text></svg>" />

  <!-- Fonts: Outfit (Bubbly & Friendly) + Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            outfit: ['Outfit', 'sans-serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
          },
          colors: {
            pet: {
              dark: '#100B1A',
              card: '#1A122A',
              border: '#2E2248',
              purple: '#8B5CF6',
              purpleLight: '#C4B5FD',
              pink: '#EC4899',
              mint: '#10B981'
            }
          }
        }
      }
    };
  </script>
</head>
<body class="bg-[#100B1A] text-slate-100 font-sans antialiased selection:bg-pet-pink selection:text-white">

  <!-- Top Strip -->
  <aside class="bg-[#150F24] border-b border-pet-border/70 py-2.5 px-4 text-xs font-semibold">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2 text-pet-purpleLight">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span>PetCare Deluxe • Supervisão Médica Veterinária: Dra. Luna Silveira • CRMV-MG 128.490</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden md:inline text-slate-400">Água Aquecida, Toalhas Esterilizadas & Zero Gaiolas</span>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20PetCare!%20Gostaria%20de%20agendar%20um%20banho/tosa%20para%20o%20meu%20pet." target="_blank" class="text-pet-pink hover:text-white font-bold flex items-center gap-1.5 transition">
          <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
          <span>(32) 99929-2311</span>
        </a>
      </div>
    </div>
  </aside>

  <!-- Header -->
  <header class="sticky top-0 z-50 bg-[#100B1A]/95 backdrop-blur-md border-b border-pet-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3.5 group">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-pet-purple to-pet-pink flex items-center justify-center text-white text-xl shadow-lg shadow-purple-950/30 font-black group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-paw"></i>
        </div>
        <div>
          <div class="font-outfit font-black text-2xl text-white tracking-wide flex items-center gap-1.5">
            PETCARE <span class="text-pet-pink font-light">DELUXE</span>
          </div>
          <span class="block text-[9px] font-mono tracking-widest uppercase text-pet-purpleLight font-bold -mt-0.5">
            Estética Animal & Spa • CRMV-MG 128.490
          </span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-8 text-xs font-bold uppercase tracking-wider text-slate-300">
        <a href="#servicos" class="hover:text-pet-pink transition">Menu de Spa</a>
        <a href="#agendador" class="hover:text-pet-pink transition flex items-center gap-1.5 text-pet-purpleLight">
          <i class="fa-solid fa-wand-magic-sparkles text-xs"></i> Simulador de Spa & Porte
        </a>
        <a href="#garantias" class="hover:text-pet-pink transition">Zero Estresse</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="admin/index.html" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-pet-card hover:bg-neutral-800 text-xs font-bold text-pet-purpleLight border border-pet-border transition" title="Acessar PetCare OS">
          <i class="fa-solid fa-lock text-[10px]"></i> Painel do Pet Shop
        </a>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20PetCare!%20Gostaria%20de%20agendar%20um%20hor%C3%A1rio%20para%20o%20meu%20pet." target="_blank" class="px-5 py-2.5 rounded-full bg-gradient-to-r from-pet-purple to-pet-pink hover:opacity-95 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-purple-950/40 transition transform hover:scale-105">
          Agendar Banho VIP
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="relative py-16 md:py-24 overflow-hidden border-b border-pet-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-pet-pink/10 border border-pet-pink/30 text-pet-pink text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-heart text-xs"></i>
            Banho sem Trauma com Supervisão Veterinária
          </div>

          <h1 class="font-outfit font-black text-4xl sm:text-6xl text-white tracking-tight leading-[1.12]">
            O Dia de Spa que Seu Melhor Amigo <span class="text-transparent bg-clip-text bg-gradient-to-r from-pet-purpleLight via-pet-pink to-amber-400">Realmente Ama.</span>
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl">
            Cosméticos 100% hipoalergênicos importados, água na temperatura exata, tosa na tesoura sem dor e ambiente sem gaiolas. Além disso, você recebe fotos e vídeos do banho pelo WhatsApp.
          </p>

          <div class="p-4 rounded-2xl bg-pet-card border border-pet-pink/40 shadow-xl max-w-xl">
            <div class="flex items-center gap-2 text-pet-pink font-bold text-xs uppercase tracking-wider mb-1">
              <i class="fa-solid fa-shield-cat"></i> Quebra de Objeção: Cuidado Afetuoso com Acompanhamento ao Vivo
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              Muitos tutores têm medo de o pet sofrer traumas ou estresse em pet shops barulhentos. Aqui os pets têm música relaxante, toalhas individuais esterilizadas e nossa equipe envia atualizações em tempo real para você trabalhar tranquilo.
            </p>
          </div>

          <div class="flex flex-col sm:flex-row gap-4 pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20PetCare!%20Gostaria%20de%20agendar%20um%20hor%C3%A1rio%20com%20T%C3%A1xi%20Dog." target="_blank" class="px-8 py-4 rounded-xl bg-gradient-to-r from-pet-purple to-pet-pink hover:opacity-95 text-white font-black text-xs uppercase tracking-wider shadow-xl shadow-purple-950/40 text-center flex items-center justify-center gap-2.5 transition transform hover:scale-105">
              <i class="fa-brands fa-whatsapp text-base"></i>
              <span>Agendar Banho + Táxi Dog Leva e Traz</span>
            </a>
            <a href="#agendador" class="px-8 py-4 rounded-xl bg-pet-card hover:bg-neutral-800 text-white font-bold text-xs uppercase tracking-wider border border-pet-border text-center flex items-center justify-center gap-2">
              <i class="fa-solid fa-wand-magic-sparkles text-pet-pink"></i>
              <span>Simular por Porte do Pet</span>
            </a>
          </div>

          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-pet-border/60 text-center">
            <div class="p-3 rounded-2xl bg-pet-card/50 border border-pet-border/50">
              <div class="font-outfit font-black text-2xl text-pet-pink">+4.200</div>
              <div class="text-[11px] text-slate-400 font-semibold">Banhos Realizados</div>
            </div>
            <div class="p-3 rounded-2xl bg-pet-card/50 border border-pet-border/50">
              <div class="font-outfit font-black text-2xl text-emerald-400">100%</div>
              <div class="text-[11px] text-slate-400 font-semibold">Produtos Veganos/Hipo</div>
            </div>
            <div class="p-3 rounded-2xl bg-pet-card/50 border border-pet-border/50">
              <div class="font-outfit font-black text-2xl text-amber-400">Zero</div>
              <div class="text-[11px] text-slate-400 font-semibold">Gaiolas ou Grades</div>
            </div>
          </div>
        </div>

        <!-- Right: Card Dra. Luna Silveira -->
        <div class="lg:col-span-5">
          <div class="bg-pet-card p-8 rounded-3xl border border-pet-border shadow-2xl relative overflow-hidden space-y-6">
            <div class="flex items-center gap-4 pb-6 border-b border-pet-border">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-pet-purple to-pet-pink text-white flex items-center justify-center text-2xl font-outfit font-bold shadow-lg">
                LS
              </div>
              <div>
                <h3 class="font-outfit font-bold text-xl text-white">Dra. Luna Silveira</h3>
                <p class="text-xs text-pet-pink font-semibold">Responsável Técnica • CRMV-MG 128.490</p>
                <p class="text-[11px] text-slate-400 mt-0.5">Dermatologia Veterinária & Bem-Estar Animal</p>
              </div>
            </div>

            <div class="space-y-3.5">
              <div class="p-3.5 rounded-xl bg-[#100B1A] border border-pet-border flex items-start gap-3">
                <i class="fa-solid fa-shield-dog text-pet-purple text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">1. Avaliação de Pele Pré-Banho</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Checagem de nós, alergias e dermatites antes de aplicar o xampu terapêutico ideal.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#100B1A] border border-pet-border flex items-start gap-3">
                <i class="fa-solid fa-van-shuttle text-pet-pink text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">2. Táxi Dog com Caixa Individual</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Veículo 100% climatizado com cinto de segurança pet para buscar e entregar no seu portão.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#100B1A] border border-pet-border flex items-start gap-3">
                <i class="fa-solid fa-camera-retro text-emerald-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">3. Notificação no WhatsApp com Foto</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Você recebe foto do pet cheiroso assim que ele terminar o spa (via PetCare OS).</p>
                </div>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-pet-purple/10 border border-pet-purple/30 text-center">
              <span class="text-xs font-bold text-pet-purpleLight flex items-center justify-center gap-1.5">
                <i class="fa-solid fa-heart text-pet-pink"></i> Carinho e Paciência com Pets Idosos ou Tímidos
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIMULADOR INTERATIVO DE PORTE E SERVIÇOS -->
  <section id="agendador" class="py-20 bg-[#140D22] border-b border-pet-border/60">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold uppercase tracking-widest text-pet-pink bg-pet-pink/10 px-3.5 py-1.5 rounded-full border border-pet-pink/30">
          Personalize a Sessão
        </span>
        <h2 class="font-outfit font-black text-3xl sm:text-4xl text-white mt-4">
          Simulador de Spa & Porte do Pet
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2">
          Selecione o tamanho do seu cão ou gato para ver o tempo de atendimento e os cuidados específicos dedicados.
        </p>
      </div>

      <div class="bg-pet-card p-6 sm:p-10 rounded-3xl border border-pet-border shadow-2xl space-y-6">
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">1. Qual o porte do seu pet?</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <button type="button" onclick="selectPetPorte('pequeno')" id="btn-porte-pequeno" class="porte-btn active p-3 rounded-xl bg-pet-pink text-white font-bold text-xs text-center border border-pet-pink transition">
              <i class="fa-solid fa-dog block text-base mb-1"></i>
              Mini / Pequeno (até 10kg)
            </button>
            <button type="button" onclick="selectPetPorte('medio')" id="btn-porte-medio" class="porte-btn p-3 rounded-xl bg-[#100B1A] text-slate-300 hover:text-white font-bold text-xs text-center border border-pet-border transition">
              <i class="fa-solid fa-dog block text-base mb-1"></i>
              Médio (10kg a 22kg)
            </button>
            <button type="button" onclick="selectPetPorte('grande')" id="btn-porte-grande" class="porte-btn p-3 rounded-xl bg-[#100B1A] text-slate-300 hover:text-white font-bold text-xs text-center border border-pet-border transition">
              <i class="fa-solid fa-dog block text-base mb-1"></i>
              Grande (22kg a 40kg)
            </button>
            <button type="button" onclick="selectPetPorte('gato')" id="btn-porte-gato" class="porte-btn p-3 rounded-xl bg-[#100B1A] text-slate-300 hover:text-white font-bold text-xs text-center border border-pet-border transition">
              <i class="fa-solid fa-cat block text-base mb-1"></i>
              Felino / Gatos VIP
            </button>
          </div>
        </div>

        <div class="p-5 rounded-2xl bg-[#100B1A] border border-pet-border space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-pet-purpleLight uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-sparkles text-pet-pink"></i> Cuidados Dedicados ao Porte
            </span>
            <span id="pet-tempo" class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded border border-emerald-500/30">
              Tempo Médio: 1h15
            </span>
          </div>

          <h4 id="pet-titulo" class="font-outfit font-bold text-lg text-white">
            Banho Spa Ozonizado & Tosa Bebê para Cães de Pequeno Porte
          </h4>

          <p id="pet-desc" class="text-xs text-slate-300 leading-relaxed">
            Água ozonizada anti-fúngica, xampu hipoalergênico suave, corte de unhas com lixa elétrica silenciosa, limpeza auricular com algodão e secagem silenciosa para não assustar o animal.
          </p>

          <div class="pt-2 border-t border-pet-border/60 flex flex-wrap gap-2 text-[11px] text-slate-400">
            <span class="font-bold text-slate-300">Inclui:</span>
            <span class="text-pet-purpleLight">Perfume suave pet, lencinho e hidratação profunda nas almofadinhas das patas.</span>
          </div>
        </div>

        <div class="pt-2">
          <a id="pet-wa-btn" href="https://wa.me/5532999292311?text=Ol%C3%A1%20PetCare!%20Gostaria%20de%20agendar%20um%20banho%20para%20meu%20c%C3%A3o%20pequeno." target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-pet-purple to-pet-pink hover:opacity-95 text-white font-black text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition transform hover:scale-[1.01]">
            <i class="fa-brands fa-whatsapp text-base"></i>
            <span>Agendar Horário para Meu Pet com a Dra. Luna</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-[#0A0711] border-t border-pet-border/60 py-12 text-xs text-slate-400">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <span class="font-outfit font-bold text-white text-base">PetCare Deluxe • Estética & Spa Animal</span>
        <p class="text-[11px] text-slate-500 mt-1">Dra. Luna Silveira • CRMV-MG 128.490 • Todos os direitos reservados 2026.</p>
      </div>
      <div class="flex items-center gap-6">
        <a href="admin/index.html" target="_blank" class="text-pet-purpleLight hover:underline font-bold flex items-center gap-1">
          <i class="fa-solid fa-lock text-xs"></i> Acesso Restrito (PetCare OS)
        </a>
        <a href="../index.html" class="hover:text-white transition">Voltar ao Portfólio Geral</a>
      </div>
    </div>
  </footer>

  <script>
    const PET_DATA = {
      pequeno: {
        titulo: 'Banho Spa Ozonizado para Cães Pequenos (Yorkshire, Shih Tzu, Poodle, Maltês)',
        tempo: 'Tempo Médio: 1h15',
        desc: 'Água morna ozonizada anti-fúngica, xampu hipoalergênico suave, corte de unhas com lixa elétrica silenciosa e hidratação nas patinhas.',
        waText: 'Olá PetCare! Gostaria de agendar um banho para meu pet pequeno (até 10kg).'
      },
      medio: {
        titulo: 'Banho & Tosa Desembolo para Cães Médios (Bulldog Francês, Beagle, Cocker, Border Collie)',
        tempo: 'Tempo Médio: 1h30',
        desc: 'Escovação profunda de subpelo, hidratação reconstrutora com óleo de argan, higienização dos ouvidos e secagem anti-estresse.',
        waText: 'Olá PetCare! Gostaria de agendar um banho para meu pet médio (10 a 22kg).'
      },
      grande: {
        titulo: 'Banho Completo com Secagem Turbinada para Cães Grandes (Golden, Labrador, Pastor Alemão, Bernese)',
        tempo: 'Tempo Médio: 2h00',
        desc: 'Banheira ampla de fácil acesso sem rampas perigosas, soprador duplo de alta vazão com isolamento acústico e massagem relaxante.',
        waText: 'Olá PetCare! Gostaria de agendar um banho para meu pet grande (+22kg).'
      },
      gato: {
        titulo: 'Spa Felino em Sala Exclusiva com Difusor de Feliway (Zero Latidos de Cães)',
        tempo: 'Tempo Médio: 1h00',
        desc: 'Ambiente silencioso climatizado dedicado exclusivamente a felinos com toalha morna, corte de unhas e xampu a seco de pH neutro.',
        waText: 'Olá PetCare! Gostaria de agendar um banho/higienização para meu gato.'
      }
    };

    function selectPetPorte(key) {
      document.querySelectorAll('.porte-btn').forEach(b => {
        b.classList.remove('bg-pet-pink', 'text-white', 'active');
        b.classList.add('bg-[#100B1A]', 'text-slate-300');
      });

      const btn = document.getElementById('btn-porte-' + key);
      if (btn) {
        btn.classList.remove('bg-[#100B1A]', 'text-slate-300');
        btn.classList.add('bg-pet-pink', 'text-white', 'active');
      }

      const data = PET_DATA[key];
      if (!data) return;

      document.getElementById('pet-titulo').textContent = data.titulo;
      document.getElementById('pet-tempo').textContent = data.tempo;
      document.getElementById('pet-desc').textContent = data.desc;
      document.getElementById('pet-wa-btn').setAttribute('href', 'https://wa.me/5532999292311?text=' + encodeURIComponent(data.waText));
    }
  </script>
</body>
</html>`;
}

// ============================================================================
// 4. BARBEARIA (Barber Club • Gabriel Queiroz • Master Barber 128.490)
// ============================================================================
function buildBarbeariaHtml() {
  return `<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Barber Club • Barbearia Clássica & Gentlemen's Lounge | Gabriel Queiroz</title>
  <meta name="description" content="O clássico refinado com pontualidade britânica. Cortes impecáveis, barboterapia com toalha quente, chopp artesanal cortesia e sem filas. Master Barber 128.490." />
  
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>💈</text></svg>" />

  <!-- Fonts: Cinzel (Clássico Vintage) + Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            serif: ['Cinzel', 'serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
          },
          colors: {
            barber: {
              black: '#0C0A09',
              card: '#161311',
              border: '#29221C',
              amber: '#D97706',
              gold: '#D4AF37',
              leather: '#451A03'
            }
          }
        }
      }
    };
  </script>
</head>
<body class="bg-[#0C0A09] text-slate-100 font-sans antialiased selection:bg-barber-amber selection:text-black">

  <aside class="bg-[#120F0D] border-b border-barber-border/70 py-2.5 px-4 text-xs font-semibold">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2 text-barber-gold">
        <span class="w-2 h-2 rounded-full bg-barber-amber animate-pulse"></span>
        <span>Barber Club • Gabriel Queiroz • Master Barber 128.490</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden md:inline text-slate-400">Chopp Artesanal Gelado Cortesia & Pontualidade Garantida</span>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Barber%20Club!%20Gostaria%20de%20reservar%20meu%20hor%C3%A1rio." target="_blank" class="text-barber-amber hover:text-white font-bold flex items-center gap-1.5 transition">
          <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
          <span>(32) 99929-2311</span>
        </a>
      </div>
    </div>
  </aside>

  <header class="sticky top-0 z-50 bg-[#0C0A09]/95 backdrop-blur-md border-b border-barber-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3.5 group">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-barber-amber via-amber-700 to-barber-leather flex items-center justify-center text-white text-xl shadow-lg shadow-amber-950/30 font-black group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-scissors"></i>
        </div>
        <div>
          <div class="font-serif font-black text-2xl text-white tracking-wide flex items-center gap-2">
            BARBER <span class="text-barber-amber font-light">CLUB</span>
          </div>
          <span class="block text-[9px] font-mono tracking-widest uppercase text-slate-400 font-bold -mt-0.5">
            Clássico & Lounge • Master Barber 128.490
          </span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-8 text-xs font-bold uppercase tracking-wider text-slate-300">
        <a href="#servicos" class="hover:text-barber-amber transition">Cortes & Barba</a>
        <a href="#seletor" class="hover:text-barber-amber transition flex items-center gap-1.5 text-barber-gold">
          <i class="fa-solid fa-chair text-xs"></i> Escolha Barbeiro & Estilo
        </a>
        <a href="#diferenciais" class="hover:text-barber-amber transition">Garantia Sem Fila</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="admin/index.html" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-barber-card hover:bg-neutral-800 text-xs font-bold text-barber-gold border border-barber-border transition" title="Acessar BarberOS">
          <i class="fa-solid fa-lock text-[10px]"></i> Painel da Barbearia
        </a>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Gabriel!%20Gostaria%20de%20agendar%20meu%20corte%20no%20Barber%20Club." target="_blank" class="px-5 py-2.5 rounded-full bg-gradient-to-r from-barber-amber to-amber-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-amber-950/40 transition transform hover:scale-105">
          Reservar Cadeira VIP
        </a>
      </div>
    </div>
  </header>

  <section class="relative py-16 md:py-24 overflow-hidden border-b border-barber-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-barber-amber/10 border border-barber-amber/30 text-barber-amber text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-beer-mug-empty text-xs"></i>
            Reserva Pontual com Chopp Artesanal de Boas-Vindas
          </div>

          <h1 class="font-serif font-black text-4xl sm:text-6xl text-white tracking-tight leading-[1.12]">
            Mais que um Corte. Uma Experiência de <span class="text-transparent bg-clip-text bg-gradient-to-r from-barber-gold via-barber-amber to-yellow-600">Respeito ao Seu Tempo.</span>
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl">
            Cortes clássicos na tesoura, degradês impecáveis na navalha, barboterapia com toalha quente e óleos essenciais importados. Sem espera, com agendamento garantido.
          </p>

          <div class="p-4 rounded-2xl bg-barber-card border border-barber-amber/40 shadow-xl max-w-xl">
            <div class="flex items-center gap-2 text-barber-amber font-bold text-xs uppercase tracking-wider mb-1">
              <i class="fa-solid fa-clock"></i> Quebra de Objeção: Pontualidade Britânica Sem Fila
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              Odeia ficar sentado esperando 40 minutos em fila de barbearia? No Barber Club o seu horário é sagrado. Se você esperar mais de 10 minutos após o horário agendado, o chopp e o corte são por nossa conta.
            </p>
          </div>

          <div class="flex flex-col sm:flex-row gap-4 pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Gabriel!%20Gostaria%20de%20reservar%20meu%20corte%20no%20Barber%20Club." target="_blank" class="px-8 py-4 rounded-xl bg-gradient-to-r from-barber-amber to-amber-600 hover:opacity-95 text-black font-black text-xs uppercase tracking-wider shadow-xl shadow-amber-950/40 text-center flex items-center justify-center gap-2.5 transition transform hover:scale-105">
              <i class="fa-brands fa-whatsapp text-base"></i>
              <span>Agendar Horário no WhatsApp</span>
            </a>
            <a href="#seletor" class="px-8 py-4 rounded-xl bg-barber-card hover:bg-neutral-800 text-white font-bold text-xs uppercase tracking-wider border border-barber-border text-center flex items-center justify-center gap-2">
              <i class="fa-solid fa-chair text-barber-amber"></i>
              <span>Escolher Estilo & Barbeiro</span>
            </a>
          </div>

          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-barber-border/60 text-center">
            <div class="p-3 rounded-2xl bg-barber-card/50 border border-barber-border/50">
              <div class="font-serif font-black text-2xl text-barber-gold">+12.000</div>
              <div class="text-[11px] text-slate-400 font-semibold">Cortes Feitos</div>
            </div>
            <div class="p-3 rounded-2xl bg-barber-card/50 border border-barber-border/50">
              <div class="font-serif font-black text-2xl text-amber-500">100%</div>
              <div class="text-[11px] text-slate-400 font-semibold">Lâminas Descartáveis</div>
            </div>
            <div class="p-3 rounded-2xl bg-barber-card/50 border border-barber-border/50">
              <div class="font-serif font-black text-2xl text-white">0 min</div>
              <div class="text-[11px] text-slate-400 font-semibold">Fila de Espera</div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="bg-barber-card p-8 rounded-3xl border border-barber-border shadow-2xl relative overflow-hidden space-y-6">
            <div class="flex items-center gap-4 pb-6 border-b border-barber-border">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-barber-amber to-amber-900 text-black flex items-center justify-center text-2xl font-serif font-bold shadow-lg">
                GQ
              </div>
              <div>
                <h3 class="font-serif font-bold text-xl text-white">Gabriel Queiroz</h3>
                <p class="text-xs text-barber-amber font-semibold">Master Barber & Fundador • Matrícula 128.490</p>
                <p class="text-[11px] text-slate-400 mt-0.5">Especialista em Visagismo Masculino & Barboterapia</p>
              </div>
            </div>

            <div class="space-y-3.5">
              <div class="p-3.5 rounded-xl bg-[#0C0A09] border border-barber-border flex items-start gap-3">
                <i class="fa-solid fa-hot-tub-person text-barber-amber text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">1. Barboterapia Clássica</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Toalha quente aromatizada, esfoliação facial e massagem pós-barba.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#0C0A09] border border-barber-border flex items-start gap-3">
                <i class="fa-solid fa-eye text-emerald-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">2. Consultoria de Visagismo</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Corte adaptado ao formato do seu rosto e crescimento dos fios para durar mais.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#0C0A09] border border-barber-border flex items-start gap-3">
                <i class="fa-solid fa-mobile-screen text-cyan-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">3. Notificação Automática (BarberOS)</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Lembrete no WhatsApp 2 horas antes para você não esquecer seu horário.</p>
                </div>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-barber-amber/10 border border-barber-amber/30 text-center">
              <span class="text-xs font-bold text-barber-gold flex items-center justify-center gap-1.5">
                <i class="fa-solid fa-mug-hot text-barber-amber"></i> Café Espresso & Chopp Artesanal Liberados
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SELETOR INTERATIVO DE ESTILO & BARBEIRO -->
  <section id="seletor" class="py-20 bg-[#120F0D] border-b border-barber-border/60">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold uppercase tracking-widest text-barber-amber bg-barber-amber/10 px-3.5 py-1.5 rounded-full border border-barber-amber/30">
          Personalização de Atendimento
        </span>
        <h2 class="font-serif font-black text-3xl sm:text-4xl text-white mt-4">
          Escolha seu Estilo & Barbeiro
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2">
          Selecione o procedimento desejado e o barbeiro titular para preparar seu atendimento.
        </p>
      </div>

      <div class="bg-barber-card p-6 sm:p-10 rounded-3xl border border-barber-border shadow-2xl space-y-6">
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">1. Selecione o Procedimento:</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <button type="button" onclick="selectBarberStyle('corte')" id="btn-style-corte" class="style-btn active p-3 rounded-xl bg-barber-amber text-black font-bold text-xs text-center border border-barber-amber transition">
              Corte & Visagismo
            </button>
            <button type="button" onclick="selectBarberStyle('barba')" id="btn-style-barba" class="style-btn p-3 rounded-xl bg-[#0C0A09] text-slate-300 hover:text-white font-bold text-xs text-center border border-barber-border transition">
              Barboterapia VIP
            </button>
            <button type="button" onclick="selectBarberStyle('combo')" id="btn-style-combo" class="style-btn p-3 rounded-xl bg-[#0C0A09] text-slate-300 hover:text-white font-bold text-xs text-center border border-barber-border transition">
              Combo Corte + Barba
            </button>
            <button type="button" onclick="selectBarberStyle('completo')" id="btn-style-completo" class="style-btn p-3 rounded-xl bg-[#0C0A09] text-slate-300 hover:text-white font-bold text-xs text-center border border-barber-border transition">
              Spa Facial Completo
            </button>
          </div>
        </div>

        <div class="p-5 rounded-2xl bg-[#0C0A09] border border-barber-border space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-barber-gold uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-scissors"></i> Experiência Selecionada
            </span>
            <span id="barber-tempo" class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded border border-emerald-500/30">
              Duração: 45 min
            </span>
          </div>

          <h4 id="barber-titulo" class="font-serif font-bold text-lg text-white">
            Corte na Tesoura & Degradê Navalhado (Fade)
          </h4>

          <p id="barber-desc" class="text-xs text-slate-300 leading-relaxed">
            Higienização capilar com xampu mentolado refrescante, alinhamento de fios, acabamento com navalha descartável e finalização com pomada modeladora matte.
          </p>

          <div class="pt-2 border-t border-barber-border/60 flex flex-wrap gap-2 text-[11px] text-slate-400">
            <span class="font-bold text-slate-300">Cortesia inclusa:</span>
            <span class="text-barber-amber">Chopp artesanal pilsen gelado ou café espresso cremoso.</span>
          </div>
        </div>

        <div class="pt-2">
          <a id="barber-wa-btn" href="https://wa.me/5532999292311?text=Ol%C3%A1%20Gabriel!%20Gostaria%20de%20agendar%20um%20Corte%20%26%20Visagismo%20no%20Barber%20Club." target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-barber-amber to-amber-600 hover:opacity-95 text-black font-black text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition transform hover:scale-[1.01]">
            <i class="fa-brands fa-whatsapp text-base"></i>
            <span>Confirmar Horário com Gabriel Queiroz no WhatsApp</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-[#080605] border-t border-barber-border/60 py-12 text-xs text-slate-400">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <span class="font-serif font-bold text-white text-base">Barber Club • Gentlemen's Lounge</span>
        <p class="text-[11px] text-slate-500 mt-1">Gabriel Queiroz • Master Barber 128.490 • Todos os direitos reservados 2026.</p>
      </div>
      <div class="flex items-center gap-6">
        <a href="admin/index.html" target="_blank" class="text-barber-amber hover:underline font-bold flex items-center gap-1">
          <i class="fa-solid fa-lock text-xs"></i> Acesso Restrito (BarberOS)
        </a>
        <a href="../index.html" class="hover:text-white transition">Voltar ao Portfólio Geral</a>
      </div>
    </div>
  </footer>

  <script>
    const STYLES_DATA = {
      corte: {
        titulo: 'Corte na Tesoura & Degradê Navalhado (Fade)',
        tempo: 'Duração: 45 min',
        desc: 'Higienização capilar mentolada, acabamento com navalha cirúrgica descartável e finalização com pomada modeladora matte de alta fixação.',
        waText: 'Olá Gabriel! Gostaria de agendar um Corte & Visagismo no Barber Club.'
      },
      barba: {
        titulo: 'Barboterapia Tradicional com Toalha Quente & Óleo Argan',
        tempo: 'Duração: 40 min',
        desc: 'Abertura de poros com vapor de ozônio e toalha aquecida, desenho simétrico com navalhete, óleo hidratante e massagem relaxante pós-barba.',
        waText: 'Olá Gabriel! Gostaria de agendar uma Barboterapia VIP no Barber Club.'
      },
      combo: {
        titulo: 'Combo Completo: Corte de Cabelo + Barboterapia',
        tempo: 'Duração: 1h15',
        desc: 'O pacote clássico completo para renovação do visual com acompanhamento de chopp artesanal e consultoria de produtos capilares.',
        waText: 'Olá Gabriel! Gostaria de agendar o Combo Corte + Barba no Barber Club.'
      },
      completo: {
        titulo: 'Spa Facial Masculino com Máscara Black & Limpeza Profunda',
        tempo: 'Duração: 50 min',
        desc: 'Esfoliação de pele, remoção de cravos superficiais, máscara preta desintoxicante e hidratação facial anti-brilho.',
        waText: 'Olá Gabriel! Gostaria de agendar um Spa Facial Masculino no Barber Club.'
      }
    };

    function selectBarberStyle(key) {
      document.querySelectorAll('.style-btn').forEach(b => {
        b.classList.remove('bg-barber-amber', 'text-black', 'active');
        b.classList.add('bg-[#0C0A09]', 'text-slate-300');
      });

      const btn = document.getElementById('btn-style-' + key);
      if (btn) {
        btn.classList.remove('bg-[#0C0A09]', 'text-slate-300');
        btn.classList.add('bg-barber-amber', 'text-black', 'active');
      }

      const data = STYLES_DATA[key];
      if (!data) return;

      document.getElementById('barber-titulo').textContent = data.titulo;
      document.getElementById('barber-tempo').textContent = data.tempo;
      document.getElementById('barber-desc').textContent = data.desc;
      document.getElementById('barber-wa-btn').setAttribute('href', 'https://wa.me/5532999292311?text=' + encodeURIComponent(data.waText));
    }
  </script>
</body>
</html>`;
}

// ============================================================================
// 5. CORRETOR DE IMÓVEIS (ImobMax • Henrique Vasconcelos • CRECI 128.490)
// ============================================================================
function buildCorretorHtml() {
  return `<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ImobMax • Consultoria Imobiliária & Alto Padrão | Henrique Vasconcelos</title>
  <meta name="description" content="Imóveis de médio e alto padrão com assessoria jurídica e certidões 100% gratuitas antes do sinal. Coberturas, casas em condomínio e apartamentos vista mar. CRECI 128.490." />
  
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏢</text></svg>" />

  <!-- Fonts: Playfair Display + Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            serif: ['Playfair Display', 'serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
          },
          colors: {
            re: {
              black: '#070A12',
              card: '#0D1424',
              border: '#1B263B',
              cyan: '#06B6D4',
              gold: '#D4AF37',
              navy: '#0E172E'
            }
          }
        }
      }
    };
  </script>
</head>
<body class="bg-[#070A12] text-slate-100 font-sans antialiased selection:bg-re-cyan selection:text-black">

  <aside class="bg-[#0B101E] border-b border-re-border/70 py-2.5 px-4 text-xs font-semibold">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2 text-re-cyan">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span>ImobMax • Henrique Vasconcelos • Corretor Responsável CRECI 128.490</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden md:inline text-slate-400">Due Diligence Jurídica 100% Gratuita & Correspondente Caixa</span>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Henrique!%20Gostaria%20de%20consultar%20im%C3%B3veis%20dispon%C3%ADveis." target="_blank" class="text-re-cyan hover:text-white font-bold flex items-center gap-1.5 transition">
          <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
          <span>(32) 99929-2311</span>
        </a>
      </div>
    </div>
  </aside>

  <header class="sticky top-0 z-50 bg-[#070A12]/95 backdrop-blur-md border-b border-re-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3.5 group">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-re-cyan via-teal-600 to-blue-800 flex items-center justify-center text-black text-xl shadow-lg shadow-cyan-950/30 font-black group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-building-columns"></i>
        </div>
        <div>
          <div class="font-serif font-black text-2xl text-white tracking-wide flex items-center gap-1.5">
            IMOB<span class="text-re-cyan">MAX</span>
          </div>
          <span class="block text-[9px] font-mono tracking-widest uppercase text-slate-400 font-bold -mt-0.5">
            Consultoria Imobiliária • CRECI 128.490
          </span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-8 text-xs font-bold uppercase tracking-wider text-slate-300">
        <a href="#vitrine" class="hover:text-re-cyan transition">Vitrine VIP</a>
        <a href="#simulador" class="hover:text-re-cyan transition flex items-center gap-1.5 text-re-cyan">
          <i class="fa-solid fa-landmark text-xs"></i> Simulador de Financiamento
        </a>
        <a href="#diferenciais" class="hover:text-re-cyan transition">Segurança Jurídica</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="admin/index.html" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-re-card hover:bg-neutral-800 text-xs font-bold text-re-cyan border border-re-border transition" title="Acessar ImobMax OS">
          <i class="fa-solid fa-lock text-[10px]"></i> Painel Imobiliário
        </a>
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Henrique!%20Gostaria%20de%20agendar%20uma%20visita%20VIP." target="_blank" class="px-5 py-2.5 rounded-full bg-gradient-to-r from-re-cyan to-blue-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-cyan-950/40 transition transform hover:scale-105">
          Agendar Visita VIP
        </a>
      </div>
    </div>
  </header>

  <section class="relative py-16 md:py-24 overflow-hidden border-b border-re-border/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-re-cyan/10 border border-re-cyan/30 text-re-cyan text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-key text-xs"></i>
            A Chave do Seu Próximo Imóvel Sem Riscos Ocultos
          </div>

          <h1 class="font-serif font-black text-4xl sm:text-6xl text-white tracking-tight leading-[1.12]">
            Imóveis Exclusivos com <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-300 via-re-cyan to-blue-500">Assessoria Jurídica Total.</span>
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl">
            Coberturas, casas em condomínios fechados e apartamentos de alto padrão. Seleção com documentação 100% aprovada, assessoria de crédito Caixa e Itaú e negociação transparente.
          </p>

          <div class="p-4 rounded-2xl bg-re-card border border-re-cyan/40 shadow-xl max-w-xl">
            <div class="flex items-center gap-2 text-re-cyan font-bold text-xs uppercase tracking-wider mb-1">
              <i class="fa-solid fa-shield-check"></i> Quebra de Objeção: Due Diligence e Certidões Gratuitas
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              O maior risco na compra de um imóvel são penhoras, dívidas de condomínio ou herdeiros ocultos. O ImobMax entrega a certidão vintenária e o laudo de engenharia antes de você depositar qualquer sinal financeiro.
            </p>
          </div>

          <div class="flex flex-col sm:flex-row gap-4 pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Henrique!%20Gostaria%20de%20ver%20as%20op%C3%A7%C3%B5es%20de%20im%C3%B3veis%20dispon%C3%ADveis." target="_blank" class="px-8 py-4 rounded-xl bg-gradient-to-r from-re-cyan to-blue-600 hover:opacity-95 text-black font-black text-xs uppercase tracking-wider shadow-xl shadow-cyan-950/40 text-center flex items-center justify-center gap-2.5 transition transform hover:scale-105">
              <i class="fa-brands fa-whatsapp text-base"></i>
              <span>Falar Diretamente com Henrique Vasconcelos</span>
            </a>
            <a href="#simulador" class="px-8 py-4 rounded-xl bg-re-card hover:bg-neutral-800 text-white font-bold text-xs uppercase tracking-wider border border-re-border text-center flex items-center justify-center gap-2">
              <i class="fa-solid fa-calculator text-re-cyan"></i>
              <span>Simular Financiamento Bancário</span>
            </a>
          </div>

          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-re-border/60 text-center">
            <div class="p-3 rounded-2xl bg-re-card/50 border border-re-border/50">
              <div class="font-serif font-black text-2xl text-re-cyan">+R$ 120M</div>
              <div class="text-[11px] text-slate-400 font-semibold">VGV Intermediado</div>
            </div>
            <div class="p-3 rounded-2xl bg-re-card/50 border border-re-border/50">
              <div class="font-serif font-black text-2xl text-emerald-400">100%</div>
              <div class="text-[11px] text-slate-400 font-semibold">Certidões Atestadas</div>
            </div>
            <div class="p-3 rounded-2xl bg-re-card/50 border border-re-border/50">
              <div class="font-serif font-black text-2xl text-white">24h</div>
              <div class="text-[11px] text-slate-400 font-semibold">Aprovação de Crédito</div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="bg-re-card p-8 rounded-3xl border border-re-border shadow-2xl relative overflow-hidden space-y-6">
            <div class="flex items-center gap-4 pb-6 border-b border-re-border">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-re-cyan to-blue-700 text-black flex items-center justify-center text-2xl font-serif font-bold shadow-lg">
                HV
              </div>
              <div>
                <h3 class="font-serif font-bold text-xl text-white">Henrique Vasconcelos</h3>
                <p class="text-xs text-re-cyan font-semibold">Corretor Responsável • CRECI 128.490</p>
                <p class="text-[11px] text-slate-400 mt-0.5">Especialista em Negociações de Médio & Alto Padrão</p>
              </div>
            </div>

            <div class="space-y-3.5">
              <div class="p-3.5 rounded-xl bg-[#070A12] border border-re-border flex items-start gap-3">
                <i class="fa-solid fa-file-contract text-re-cyan text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">1. Matrícula Vintenária & CNDs</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Verificação completa na Justiça do Trabalho, Receita e Cartórios de Imóveis.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#070A12] border border-re-border flex items-start gap-3">
                <i class="fa-solid fa-car-side text-emerald-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">2. Visita VIP sem Pressa</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Atendimento exclusivo com horários flexíveis e análise de iluminação solar e vizinhança.</p>
                </div>
              </div>

              <div class="p-3.5 rounded-xl bg-[#070A12] border border-re-border flex items-start gap-3">
                <i class="fa-solid fa-hand-holding-dollar text-amber-400 text-sm mt-1"></i>
                <div>
                  <h4 class="font-bold text-xs text-white">3. Menor Taxa de Financiamento (ImobMax OS)</h4>
                  <p class="text-[11px] text-slate-400 leading-relaxed">Comparamos taxas entre Caixa, Itaú, Bradesco e Santander para encontrar a menor CET.</p>
                </div>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-re-cyan/10 border border-re-cyan/30 text-center">
              <span class="text-xs font-bold text-cyan-300 flex items-center justify-center gap-1.5">
                <i class="fa-solid fa-award text-re-cyan"></i> Negociação Segura com Registro em Cartório
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIMULADOR INTERATIVO DE FINANCIAMENTO -->
  <section id="simulador" class="py-20 bg-[#0B101E] border-b border-re-border/60">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold uppercase tracking-widest text-re-cyan bg-re-cyan/10 px-3.5 py-1.5 rounded-full border border-re-cyan/30">
          Simulador Caixa & Itaú
        </span>
        <h2 class="font-serif font-black text-3xl sm:text-4xl text-white mt-4">
          Simulador de Financiamento & Parcela
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2">
          Descubra o valor aproximado de entrada e primeira parcela com amortização SAC.
        </p>
      </div>

      <div class="bg-re-card p-6 sm:p-10 rounded-3xl border border-re-border shadow-2xl space-y-6">
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">1. Valor do Imóvel Desejado:</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <button type="button" onclick="selectPropertyPrice(450)" id="btn-price-450" class="price-btn active p-3 rounded-xl bg-re-cyan text-black font-bold text-xs text-center border border-re-cyan transition">
              R$ 450.000 (Médio)
            </button>
            <button type="button" onclick="selectPropertyPrice(850)" id="btn-price-850" class="price-btn p-3 rounded-xl bg-[#070A12] text-slate-300 hover:text-white font-bold text-xs text-center border border-re-border transition">
              R$ 850.000 (Alto Padrão)
            </button>
            <button type="button" onclick="selectPropertyPrice(1500)" id="btn-price-1500" class="price-btn p-3 rounded-xl bg-[#070A12] text-slate-300 hover:text-white font-bold text-xs text-center border border-re-border transition">
              R$ 1.500.000 (Mansão)
            </button>
            <button type="button" onclick="selectPropertyPrice(2800)" id="btn-price-2800" class="price-btn p-3 rounded-xl bg-[#070A12] text-slate-300 hover:text-white font-bold text-xs text-center border border-re-border transition">
              R$ 2.800.000 (Cobertura)
            </button>
          </div>
        </div>

        <div class="p-5 rounded-2xl bg-[#070A12] border border-re-border space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-re-cyan uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-calculator"></i> Estimativa de Financiamento
            </span>
            <span class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded border border-emerald-500/30">
              Prazo: 360 meses (SAC)
            </span>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 pt-2">
            <div>
              <span class="text-[10px] text-slate-400 uppercase font-bold block">Entrada Mínima (20%)</span>
              <span id="calc-entrada" class="font-mono font-bold text-lg text-white">R$ 90.000</span>
            </div>
            <div>
              <span class="text-[10px] text-slate-400 uppercase font-bold block">1ª Parcela Estimada</span>
              <span id="calc-parcela" class="font-mono font-bold text-lg text-re-cyan">R$ 3.420/mês</span>
            </div>
            <div class="col-span-2 sm:col-span-1">
              <span class="text-[10px] text-slate-400 uppercase font-bold block">Uso do FGTS</span>
              <span class="font-mono font-bold text-sm text-emerald-400">Permitido na Entrada</span>
            </div>
          </div>
        </div>

        <div class="pt-2">
          <a id="imob-wa-btn" href="https://wa.me/5532999292311?text=Ol%C3%A1%20Henrique!%20Fiz%20a%20simula%C3%A7%C3%A3o%20de%20financiamento%20de%20R$%20450.000%20e%20gostaria%20de%20aprovar%20meu%20cr%C3%A9dito." target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-re-cyan to-blue-600 hover:opacity-95 text-black font-black text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition transform hover:scale-[1.01]">
            <i class="fa-brands fa-whatsapp text-base"></i>
            <span>Encaminhar Dados para Aprovação Bancária Rápida</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-[#05070D] border-t border-re-border/60 py-12 text-xs text-slate-400">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <span class="font-serif font-bold text-white text-base">ImobMax Consultoria Imobiliária</span>
        <p class="text-[11px] text-slate-500 mt-1">Henrique Vasconcelos • CRECI 128.490 • Todos os direitos reservados 2026.</p>
      </div>
      <div class="flex items-center gap-6">
        <a href="admin/index.html" target="_blank" class="text-re-cyan hover:underline font-bold flex items-center gap-1">
          <i class="fa-solid fa-lock text-xs"></i> Acesso Restrito (ImobMax OS)
        </a>
        <a href="../index.html" class="hover:text-white transition">Voltar ao Portfólio Geral</a>
      </div>
    </div>
  </footer>

  <script>
    function selectPropertyPrice(thousands) {
      document.querySelectorAll('.price-btn').forEach(b => {
        b.classList.remove('bg-re-cyan', 'text-black', 'active');
        b.classList.add('bg-[#070A12]', 'text-slate-300');
      });

      const btn = document.getElementById('btn-price-' + thousands);
      if (btn) {
        btn.classList.remove('bg-[#070A12]', 'text-slate-300');
        btn.classList.add('bg-re-cyan', 'text-black', 'active');
      }

      const entrada = thousands * 0.20 * 1000;
      const financiado = thousands * 0.80 * 1000;
      const parcela = (financiado / 360) + (financiado * 0.0075);

      document.getElementById('calc-entrada').textContent = 'R$ ' + (entrada).toLocaleString('pt-BR');
      document.getElementById('calc-parcela').textContent = 'R$ ' + Math.round(parcela).toLocaleString('pt-BR') + '/mês';

      const waMsg = 'Olá Henrique! Fiz a simulação de financiamento para imóvel de R$ ' + (thousands * 1000).toLocaleString('pt-BR') + ' e gostaria de agendar uma consulta de crédito.';
      document.getElementById('imob-wa-btn').setAttribute('href', 'https://wa.me/5532999292311?text=' + encodeURIComponent(waMsg));
    }
  </script>
</body>
</html>`;
}

// ============================================================================
// EXECUTE ELEVATION ACROSS ALL RELEVANT SITES
// ============================================================================
console.log('🚀 Executando Elevação Impeccable dos Sites com Identidade Visual Única...\n');

fs.writeFileSync(path.join(ROOT_DIR, 'advogado', 'index.html'), buildAdvogadoHtml(), 'utf8');
console.log('✅ 1. ADVOGADO: Valente & Associados elevado (Diagnóstico de Risco Jurídico, Navy/Gold, OAB/MG 128.490)');

fs.writeFileSync(path.join(ROOT_DIR, 'arquiteto', 'index.html'), buildArquitetoHtml(), 'utf8');
console.log('✅ 2. ARQUITETO: StudioDesign elevado (Simulador por m², Cinzel/Terracotta, CAU/BR 128.490)');

fs.writeFileSync(path.join(ROOT_DIR, 'banho-e-tosa', 'index.html'), buildBanhoETosaHtml(), 'utf8');
console.log('✅ 3. BANHO & TOSA: PetCare Deluxe elevado (Simulador por Porte/Táxi Dog, Outfit/Lavanda, CRMV-MG 128.490)');

fs.writeFileSync(path.join(ROOT_DIR, 'barbearia', 'index.html'), buildBarbeariaHtml(), 'utf8');
console.log('✅ 4. BARBEARIA: Barber Club elevado (Seletor de Estilo/Barbeiro, Whiskey/Leather, Master Barber 128.490)');

fs.writeFileSync(path.join(ROOT_DIR, 'corretor-imoveis', 'index.html'), buildCorretorHtml(), 'utf8');
console.log('✅ 5. CORRETOR: ImobMax elevado (Simulador de Financiamento Caixa SAC, Ocean Cyan/Navy, CRECI 128.490)');

console.log('\n🎉 Todos os 5 sites foram elevados para um padrão de design autoral, eliminando qualquer sensação de repetição!');
