const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const OUTPUT_FILE = path.join(ROOT_DIR, 'index.html');

// 1. Ecosystems with Full CRM & Public Site (WITH REAL SCREENSHOTS & HIGH-CONVERTING OBJECTION BREAKERS)
const CRM_NICHES = [
  {
    id: 'energia-solar',
    name: 'Energia Solar & Engenharia',
    shortName: 'Energia Solar',
    brand: 'SunEco OS',
    domain: 'suneco.com.br',
    tagline: 'Landing Page de Alta Conversão + CRM Fotovoltaico',
    desc: 'Dimensionamento solar automatizado, calculadora de economia para o cliente e CRM completo com controle de usinas, rastreio de inversores e módulos por lote.',
    objectionBreaker: 'Zero investimento inicial: a economia imediata na conta de luz cobre a parcela da usina solar, com 25 anos de garantia e homologação sem burocracia.',
    guarantee: 'Economia Garantida em Contrato',
    dir: 'energia-solar',
    icon: 'fa-solar-panel',
    badgeColor: 'emerald',
    accentColor: '#10B981',
    category: 'Engenharia & Solar',
    matchScore: '99% Relevante',
    previewImg: 'assets/previews/energia-solar.png',
    tags: ['Calculadora Solar 25 Anos', 'CRM Kanban', 'Estoque Inversores/Placas', 'Lembretes WhatsApp', 'Anti-Spam por IP'],
    publicUrl: 'energia-solar/index.html',
    adminUrl: 'energia-solar/admin/index.html'
  },
  {
    id: 'dentista',
    name: 'Odontologia & Estética Dental',
    shortName: 'Odontologia',
    brand: 'Lumina Dental OS',
    domain: 'luminadental.com.br',
    tagline: 'Consultório Digital + Gestão de Prontuários & Lotes',
    desc: 'Agendamento estético 3D, simulação de facetas e alinhadores, e painel CRM com histórico, faturamento e rastreio de resinas e anestésicos por lote.',
    objectionBreaker: 'Simulação 3D antes de começar: o paciente visualiza e aprova o sorriso perfeito no computador antes de qualquer procedimento, com anestesia de precisão sem dor.',
    guarantee: 'Previsibilidade Estética 3D',
    dir: 'dentista',
    icon: 'fa-tooth',
    badgeColor: 'amber',
    accentColor: '#C58B37',
    category: 'Saúde & Estética',
    matchScore: '98% Relevante',
    previewImg: 'assets/previews/dentista.png',
    tags: ['Avaliação 3D Sem Dor', 'CRM Clínico', 'Controle Resinas por Lote', 'Automação WhatsApp', 'Upload Docs'],
    publicUrl: 'dentista/index.html',
    adminUrl: 'dentista/admin/index.html'
  },
  {
    id: 'advogado',
    name: 'Advocacia & Direito de Alto Padrão',
    shortName: 'Advocacia',
    brand: 'Valente & Associados (LexPro OS)',
    domain: 'valenteassociados.adv.br',
    tagline: 'Escritório Digital + Diagnóstico de Risco & Prazos Fatais',
    desc: 'Captação confidencial com Diagnóstico de Risco Jurídico online e CRM com alerta vermelho de prazos prescricionais fatais e rateio de custas processuais.',
    objectionBreaker: 'Sigilo confidencial absoluto com honorários vinculados ao êxito: parecer de risco prévio e análise de viabilidade antes de protocolar qualquer ação judicial.',
    guarantee: 'Honorários no Êxito da Causa',
    dir: 'advogado',
    icon: 'fa-scale-balanced',
    badgeColor: 'blue',
    accentColor: '#3B82F6',
    category: 'Direito & Negócios',
    matchScore: '97% Relevante',
    previewImg: 'assets/previews/advogado.png',
    tags: ['Diagnóstico de Risco', 'Alerta Prazos Fatais', 'CRM Jurídico', 'Custas por Lote', 'WhatsApp VIP'],
    publicUrl: 'advogado/index.html',
    adminUrl: 'advogado/admin/index.html'
  },
  {
    id: 'concessionaria-honda',
    name: 'Concessionária & Automotivo',
    shortName: 'Honda Auto',
    brand: 'AutoDrive Honda OS',
    domain: 'autodrivehonda.com.br',
    tagline: 'Showroom de Veículos + CRM de Test-Drive & Peças',
    desc: 'Agendamento interativo de test-drive, catálogo digital de seminovos e novos, e CRM operacional com estoque de peças genuínas com preços variados por lote.',
    objectionBreaker: 'Taxa zero de fábrica com avaliação do seu usado em até 100% da Tabela FIPE na troca, além de aprovação de crédito simplificada em 15 minutos.',
    guarantee: 'Até 100% Tabela FIPE no Usado',
    dir: 'concessionaria-honda',
    icon: 'fa-car-side',
    badgeColor: 'red',
    accentColor: '#EF4444',
    category: 'Veículos & Motos',
    matchScore: '96% Relevante',
    previewImg: 'assets/previews/concessionaria-honda.png',
    tags: ['Test-Drive Online', 'CRM Automotivo', 'Estoque de Peças', 'Aviso WhatsApp', 'Lead por IP'],
    publicUrl: 'concessionaria-honda/index.html',
    adminUrl: 'concessionaria-honda/admin/index.html'
  },
  {
    id: 'arquiteto',
    name: 'Arquitetura & Design de Interiores',
    shortName: 'Arquitetura',
    brand: 'StudioDesign OS',
    domain: 'studiodesign.arq.br',
    tagline: 'Portfólio 3D + Simulador por m² & Cronograma de Obras',
    desc: 'Simulador paramétrico de custo por m² e cronograma de obra, briefing digital imersivo e CRM com acompanhamento de etapas de obra e acabamentos por lote.',
    objectionBreaker: 'Sem estouro de custos na obra: memorial descritivo com lista travada de materiais e cronograma de etapas antes de bater o primeiro prego.',
    guarantee: 'Custo & Prazo de Obra Travados',
    dir: 'arquiteto',
    icon: 'fa-compass-drafting',
    badgeColor: 'orange',
    accentColor: '#F97316',
    category: 'Arquitetura & Obra',
    matchScore: '98% Relevante',
    previewImg: 'assets/previews/arquiteto.png',
    tags: ['Simulador por m²', 'CRM de Obras', 'Materiais por Lote', 'Contratos & Plantas', 'WhatsApp'],
    publicUrl: 'arquiteto/index.html',
    adminUrl: 'arquiteto/admin/index.html'
  },
  {
    id: 'banho-e-tosa',
    name: 'Pet Shop, Banho & Tosa e Vet',
    shortName: 'Pet & Vet',
    brand: 'PetCare Deluxe OS',
    domain: 'petcaredeluxe.com.br',
    tagline: 'Agendamento Pet + Simulador Táxi Dog & Vacinas',
    desc: 'Simulador Pet Spa por porte (P/M/G/GG) e pelagem, agendamento de táxi dog climatizado e CRM com controle de vacinas e cosméticos por lote.',
    objectionBreaker: 'Cuidado afetuoso sem traumas: produtos 100% hipoalergênicos, banho monitorado com transmissão de fotos/vídeos para o tutor e táxi pet climatizado.',
    guarantee: 'Acompanhamento ao Vivo do Pet',
    dir: 'banho-e-tosa',
    icon: 'fa-paw',
    badgeColor: 'pink',
    accentColor: '#EC4899',
    category: 'Pet & Veterinária',
    matchScore: '97% Relevante',
    previewImg: 'assets/previews/banho-e-tosa.png',
    tags: ['Simulador Pet Spa & Táxi', 'CRM Pet Care', 'Vacinas & Insumos', 'Lembrete Banho', 'Anti-Spam'],
    publicUrl: 'banho-e-tosa/index.html',
    adminUrl: 'banho-e-tosa/admin/index.html'
  },
  {
    id: 'barbearia',
    name: 'Barbearia Premium & Club',
    shortName: 'Barbearia',
    brand: 'Barber Club OS',
    domain: 'barberclub.com.br',
    tagline: 'Agendamento com Seletor de Estilo & Barbeiro VIP',
    desc: 'Catálogo de cortes modernos/clássicos, seleção do barbeiro preferido e CRM de gestão com cálculo de comissões por profissional e estoque de pomadas.',
    objectionBreaker: 'Zero fila de espera: reserva pontual com cadeira garantida, toalha quente descartável e cerveja artesanal gelada de cortesia na recepção.',
    guarantee: 'Pontualidade Britânica Sem Fila',
    dir: 'barbearia',
    icon: 'fa-scissors',
    badgeColor: 'amber',
    accentColor: '#F59E0B',
    category: 'Estilo & Beleza',
    matchScore: '95% Relevante',
    previewImg: 'assets/previews/barbearia.png',
    tags: ['Seletor de Estilo VIP', 'CRM Barbearia', 'Estoque Pomadas', 'Confirmação 2h Antes', 'Faturamento'],
    publicUrl: 'barbearia/index.html',
    adminUrl: 'barbearia/admin/index.html'
  },
  {
    id: 'corretor-imoveis',
    name: 'Imóveis & Alto Padrão',
    shortName: 'Imobiliária',
    brand: 'ImobMax OS',
    domain: 'imobmax.com.br',
    tagline: 'Showroom de Imóveis + Simulador CAIXA SAC & CRM',
    desc: 'Simulador completo de financiamento imobiliário CAIXA SAC/Price, agendamento de visita VIP a coberturas e CRM de funil de vendas e comissões.',
    objectionBreaker: 'Segurança patrimonial jurídica: certidões negativas e laudo de vistoria técnica 100% gratuitos antes de qualquer sinal de pagamento.',
    guarantee: 'Due Diligence Jurídica Gratuita',
    dir: 'corretor-imoveis',
    icon: 'fa-building-columns',
    badgeColor: 'cyan',
    accentColor: '#06B6D4',
    category: 'Imóveis & VGV',
    matchScore: '99% Relevante',
    previewImg: 'assets/previews/corretor-imoveis.png',
    tags: ['Simulador Caixa SAC', 'CRM Imobiliário', 'VGV & Comissões', 'Upload Escrituras', 'Alerta Visitas'],
    publicUrl: 'corretor-imoveis/index.html',
    adminUrl: 'corretor-imoveis/admin/index.html'
  }
];

// 2. All 24 Additional Specialized Landing Pages in the Workspace (WITH DEDICATED PREVIEWS)
const LANDING_PAGES = [
  // Saúde & Bem-Estar
  { id: 'psicologia', name: 'Psicologia & Psicoterapia', brand: 'Mente Serena', dir: 'psicologia', icon: 'fa-brain', category: 'Saúde', color: '#06B6D4', desc: 'Atendimentos clínicos online e presenciais com acolhimento terapêutico, TCC e sigilo absoluto.' },
  { id: 'oftalmologista', name: 'Oftalmologia & Cirurgia', brand: 'Visão Prime Clínica', dir: 'oftalmologista', icon: 'fa-eye', category: 'Saúde', color: '#3B82F6', desc: 'Exames completos de acuidade visual com equipamentos a laser de última geração sem desconforto.' },
  { id: 'nutricionista', name: 'Nutrição & Performance', brand: 'NutriViva', dir: 'nutricionista', icon: 'fa-apple-whole', category: 'Saúde', color: '#84CC16', desc: 'Planos alimentares sem dietas restritivas extremas, com foco em longevidade, hipertrofia e energia.' },
  { id: 'quiropraxista', name: 'Quiropraxia & Coluna', brand: 'Coluna Viva', dir: 'quiropraxista', icon: 'fa-bone', category: 'Saúde', color: '#14B8A6', desc: 'Alívio de dores nas costas e alinhamento postural já na primeira sessão sem uso de remédios.' },
  { id: 'podologo', name: 'Podologia Clínica', brand: 'Podologia Especializada', dir: 'podologo', icon: 'fa-shoe-prints', category: 'Saúde', color: '#6366F1', desc: 'Tratamento de unhas encravadas e calosidades com esterilização cirúrgica e alívio imediato.' },
  { id: 'acupunturista', name: 'Acupuntura & Medicina Tradicional', brand: 'Equilíbrio Oriental', dir: 'acupunturista', icon: 'fa-spa', category: 'Saúde', color: '#EC4899', desc: 'Equilíbrio energético corporal, alívio da ansiedade e controle de dores com agulhas indolores.' },
  { id: 'personal-trainer', name: 'Personal Trainer & Fitness', brand: 'ProFit Performance', dir: 'personal-trainer', icon: 'fa-dumbbell', category: 'Saúde', color: '#E11D48', desc: 'Consultoria fitness individualizada com metodologia anti-lesão e evolução física comprovada.' },

  // Veículos, Supercarros & Motociclismo
  { id: 'gtmotors', name: 'Supercarros & Esportivos', brand: 'GT Motors Brasil', dir: 'gtmotors', icon: 'fa-gauge-high', category: 'Veículos', color: '#EF4444', desc: 'Showroom exclusivo de carros esportivos, importados e supercarros com laudo cautelar 100% aprovado.' },
  { id: 'shineray-uba', name: 'Motos Shineray & Consórcio', brand: 'Shineray Ubá', dir: 'shineray-uba', icon: 'fa-motorcycle', category: 'Veículos', color: '#DC2626', desc: 'Concessionária autorizada com toda a linha de motos zero km, consórcio facilitado e oficina mecânica.' },
  { id: 'topmotos032', name: 'Motos Seminovas & Oficina', brand: 'TOP MOTOS 032', dir: 'topmotos032', icon: 'fa-motorcycle', category: 'Veículos', color: '#EA580C', desc: 'Motos seminovas revisadas com garantia total, avaliação justa do seu usado e oficina especializada.' },
  { id: 'vrum-motos', name: 'Loja de Motos em Ubá', brand: 'Vrum Motos', dir: 'vrum-motos', icon: 'fa-motorcycle', category: 'Veículos', color: '#F59E0B', desc: 'Estoque completo de motocicletas novas e seminovas com aprovação de financiamento rápida.' },
  { id: 'fumaca-motos', name: 'Concessionária de Motos', brand: 'Fumaça Motos Multimarcas', dir: 'fumaca-motos', icon: 'fa-motorcycle', category: 'Veículos', color: '#B91C1C', desc: 'Motos revisadas com procedência atestada, garantia e primeira parcela com prazo estendido.' },
  { id: 'rampabike', name: 'Bicicletas, Peças & Oficina', brand: 'Rampa Bike Especializada', dir: 'rampabike', icon: 'fa-bicycle', category: 'Veículos', color: '#10B981', desc: 'Desde 1994 oferecendo as melhores marcas de bikes, acessórios profissionais e oficina especializada.' },

  // Gastronomia, Bares & Eventos
  { id: 'boteco-portugues', name: 'Boteco Português & Tapas', brand: 'O Tasco Boteco Lusitano', dir: 'boteco-portugues', icon: 'fa-beer-mug-empty', category: 'Gastronomia', color: '#EF4444', desc: 'Bolinhos de bacalhau artesanais premiados, chopp hiper gelado e ambiente tradicional acolhedor.' },
  { id: 'restaurante-egeu', name: 'Gastronomia & Restaurante Egeu', brand: 'Restaurante Egeu Mediterrâneo', dir: 'restaurante-egeu', icon: 'fa-utensils', category: 'Gastronomia', color: '#D97706', desc: 'Culinária mediterrânea autêntica com peixes e frutos do mar frescos e reserva de mesa VIP sem espera.' },
  { id: 'caxixi', name: 'Caxixi Bar e Restaurante', brand: 'Bar & Restaurante Caxixi', dir: 'caxixi', icon: 'fa-utensils', category: 'Gastronomia', color: '#F97316', desc: 'Sabores tradicionais da culinária baiana em Salvador com porções generosas, cerveja trincando e aconchego.' },
  { id: 'reconcavo', name: 'Recôncavo Culinária Baiana', brand: 'Recôncavo Culinária', dir: 'reconcavo', icon: 'fa-bowl-rice', category: 'Gastronomia', color: '#EAB308', desc: 'Gastronomia afro-baiana na Barra em Salvador: moquecas de dendê puro, acarajé e tempero ancestral.' },
  { id: 'fotografo-casamento', name: 'Fotografia de Casamentos', brand: 'Lumière Photo Studio', dir: 'fotografo-casamento', icon: 'fa-camera', category: 'Eventos', color: '#A855F7', desc: 'Cobertura fotográfica cinematográfica de casamentos com entrega do pré-wedding em 48 horas.' },

  // Serviços, Reformas, Educação & Negócios
  { id: 'reforma-moveis', name: 'Tapeçaria & Reforma de Sofás', brand: 'Ateliê Renova Móveis', dir: 'reforma-moveis', icon: 'fa-couch', category: 'Serviços', color: '#8B5CF6', desc: 'Restauração de estofados finos, troca de tecidos impermeáveis e reforma completa de sofás e poltronas.' },
  { id: 'contador', name: 'Contabilidade Consultiva', brand: 'Exata Contábil', dir: 'contador', icon: 'fa-calculator', category: 'Financeiro', color: '#10B981', desc: 'Planejamento tributário, abertura ágil de empresas e BPO financeiro com redução legal de impostos.' },
  { id: 'lavanderia', name: 'Lavanderia Express & Têxtil', brand: 'LavaClean Express', dir: 'lavanderia', icon: 'fa-shirt', category: 'Serviços', color: '#0EA5E9', desc: 'Higienização profissional com coleta e entrega expressa em domicílio sem danificar tecidos.' },
  { id: 'professor-idiomas', name: 'Aulas de Inglês & Idiomas', brand: 'Polyglot Academy', dir: 'professor-idiomas', icon: 'fa-language', category: 'Educação', color: '#F59E0B', desc: 'Fluência conversacional para viagens e negócios sem foco excessivo em gramática maçante.' },
  { id: 'professor-musica', name: 'Escola & Professor de Música', brand: 'Harmonia Instituto', dir: 'professor-musica', icon: 'fa-music', category: 'Educação', color: '#8B5CF6', desc: 'Aulas práticas no seu instrumento preferido desde a 1ª aula, tocando suas músicas favoritas.' },
  { id: 'professor-particular', name: 'Aulas Particulares & Reforço', brand: 'Nota 10 Aulas', dir: 'professor-particular', icon: 'fa-graduation-cap', category: 'Educação', color: '#10B981', desc: 'Reforço escolar personalizado com garantia de entendimento da matéria e notas altas.' }
];

function buildHtml() {
  const totalCount = CRM_NICHES.length + LANDING_PAGES.length;

  // Generate Filter Pills (Pills com Ícones e Contadores)
  const pillsHtml = `
    <button onclick="filterByNiche('all')" class="niche-pill active shrink-0 px-4 py-2 rounded-full text-xs font-bold bg-white text-black hover:bg-slate-200 transition-all flex items-center gap-2 border border-white/20 shadow-md">
      <i class="fa-solid fa-layer-group text-sm"></i>
      <span>Todos os Sistemas (${totalCount})</span>
    </button>
    <button onclick="filterByNiche('crm')" class="niche-pill shrink-0 px-4 py-2 rounded-full text-xs font-bold bg-neutral-900/80 text-white hover:bg-neutral-800 transition-all flex items-center gap-2 border border-neutral-700">
      <i class="fa-solid fa-cubes text-cyan-400 text-sm"></i>
      <span>Com CRM Integrado (${CRM_NICHES.length})</span>
    </button>
    <button onclick="filterByNiche('saúde')" class="niche-pill shrink-0 px-4 py-2 rounded-full text-xs font-bold bg-neutral-900/80 text-slate-300 hover:text-white hover:bg-neutral-800 transition-all flex items-center gap-2 border border-neutral-800">
      <i class="fa-solid fa-stethoscope text-emerald-400 text-sm"></i>
      <span>Saúde & Clínica</span>
    </button>
    <button onclick="filterByNiche('veículos')" class="niche-pill shrink-0 px-4 py-2 rounded-full text-xs font-bold bg-neutral-900/80 text-slate-300 hover:text-white hover:bg-neutral-800 transition-all flex items-center gap-2 border border-neutral-800">
      <i class="fa-solid fa-motorcycle text-red-400 text-sm"></i>
      <span>Veículos & Motos</span>
    </button>
    <button onclick="filterByNiche('gastronomia')" class="niche-pill shrink-0 px-4 py-2 rounded-full text-xs font-bold bg-neutral-900/80 text-slate-300 hover:text-white hover:bg-neutral-800 transition-all flex items-center gap-2 border border-neutral-800">
      <i class="fa-solid fa-utensils text-amber-400 text-sm"></i>
      <span>Gastronomia</span>
    </button>
    <button onclick="filterByNiche('educação')" class="niche-pill shrink-0 px-4 py-2 rounded-full text-xs font-bold bg-neutral-900/80 text-slate-300 hover:text-white hover:bg-neutral-800 transition-all flex items-center gap-2 border border-neutral-800">
      <i class="fa-solid fa-graduation-cap text-indigo-400 text-sm"></i>
      <span>Educação</span>
    </button>
    ${CRM_NICHES.map(n => `
      <button onclick="filterByNiche('${n.id}')" data-niche-id="${n.id}" class="niche-pill shrink-0 px-4 py-2 rounded-full text-xs font-bold bg-neutral-900/80 text-slate-300 hover:text-white hover:bg-neutral-800 transition-all flex items-center gap-2 border border-neutral-800">
        <i class="fa-solid ${n.icon} text-sm" style="color: ${n.accentColor}"></i>
        <span>${n.shortName}</span>
      </button>
    `).join('')}
  `;

  // UNIFIED CARD RENDERER: EVERY CARD HAS A REAL HEADER SCREENSHOT IMAGE!
  function renderCard(item) {
    const isCrm = Boolean(item.adminUrl);
    const preview = isCrm 
      ? item.previewImg 
      : `assets/previews/preview_${item.id.replace(/-/g, '_')}.jpg`;
    
    const categoryLabel = item.category || (isCrm ? 'Ecossistema CRM' : 'Landing Page');
    const accentColor = item.accentColor || item.color || '#06B6D4';
    const matchTag = isCrm ? item.matchScore : '98% Conversão';
    const guaranteeTag = isCrm ? item.guarantee : 'Pronto para Rodar';

    const objectionOrHighlight = item.objectionBreaker 
      ? item.objectionBreaker 
      : item.desc;

    const clickAction = isCrm 
      ? `openNetflixModal('${item.id}')` 
      : `window.open('${item.dir}/index.html', '_blank')`;

    return `
      <div class="netflix-card group relative w-[310px] sm:w-[340px] shrink-0 rounded-2xl bg-neutral-900/90 border border-neutral-800/80 overflow-hidden shadow-xl hover:border-neutral-600 hover:shadow-2xl transition-all duration-300 cursor-pointer flex flex-col justify-between" onclick="${clickAction}">
        <div>
          <!-- Card Top Visual Banner with REAL SITE HEADER SCREENSHOT -->
          <div class="h-48 w-full relative overflow-hidden bg-neutral-950">
            <img src="${preview}" alt="${item.name}" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 via-neutral-900/25 to-transparent pointer-events-none"></div>
            
            <!-- Top Tag / Match -->
            <div class="absolute top-3 left-3 right-3 flex items-center justify-between z-10 pointer-events-none">
              <span class="px-2.5 py-1 rounded-full text-[10px] font-extrabold uppercase tracking-wider bg-black/80 text-white border border-white/20 backdrop-blur-md flex items-center gap-1.5 shadow-md">
                <i class="fa-solid ${item.icon}" style="color: ${accentColor}"></i>
                ${categoryLabel}
              </span>
              <span class="text-[11px] font-black text-emerald-400 font-mono tracking-tight bg-black/80 px-2 py-0.5 rounded border border-emerald-500/40 backdrop-blur-md">
                ${matchTag}
              </span>
            </div>

            <!-- Bottom Badges: Guarantee Tag (NO BUDGET/PRICE) -->
            <div class="absolute bottom-2 left-3 right-3 flex items-center justify-between text-[11px] text-white/95 z-10 pointer-events-none">
              <span class="font-bold flex items-center gap-1 drop-shadow-md text-white">
                ${isCrm ? '<i class="fa-solid fa-shield-halved text-amber-400"></i> Lumina OS CRM' : '<i class="fa-solid fa-bolt text-cyan-400"></i> Landing Page'}
              </span>
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-950/90 text-emerald-300 border border-emerald-500/40 flex items-center gap-1 shadow-sm backdrop-blur-sm">
                <i class="fa-solid fa-check text-[9px]"></i> ${guaranteeTag}
              </span>
            </div>
          </div>

          <!-- Card Body -->
          <div class="p-4 space-y-3 bg-neutral-900">
            <div>
              <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">${item.brand}</div>
              <h3 class="text-base font-bold text-white leading-tight font-serif">${item.name}</h3>
            </div>

            <p class="text-xs text-slate-400 line-clamp-2 leading-relaxed">
              ${item.desc}
            </p>

            <!-- HIGHLIGHT / OBJECTION BOX -->
            <div class="p-2.5 rounded-xl bg-neutral-950 border border-neutral-800 text-[11px] leading-snug">
              <span class="text-[10px] font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1 mb-0.5">
                <i class="fa-solid ${isCrm ? 'fa-shield-check text-emerald-400' : 'fa-award text-amber-400'}"></i> ${isCrm ? 'Quebra de Objeção Principal' : 'Destaque de Conversão'}
              </span>
              <p class="text-slate-300 font-medium line-clamp-2">${objectionOrHighlight}</p>
            </div>

            <!-- Feature Pills -->
            <div class="flex flex-wrap gap-1.5 pt-1">
              ${(item.tags || [categoryLabel, 'Alta Conversão', 'WhatsApp Integrado']).slice(0, 3).map(tag => `
                <span class="text-[10px] font-semibold bg-neutral-800 text-slate-300 px-2 py-0.5 rounded border border-neutral-700/60">${tag}</span>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- Quick Action Buttons -->
        <div class="p-4 pt-2 border-t border-neutral-800 flex items-center justify-between gap-2 bg-neutral-900" onclick="event.stopPropagation()">
          ${isCrm ? `
            <a href="${item.publicUrl}" target="_blank" class="flex-1 py-2 px-3 rounded-xl bg-white text-black hover:bg-slate-200 text-center font-bold text-xs flex items-center justify-center gap-1.5 transition-all shadow-sm">
              <i class="fa-solid fa-play text-[10px]"></i> Ver Site
            </a>
            <a href="${item.adminUrl}" target="_blank" class="flex-1 py-2 px-3 rounded-xl bg-neutral-800 hover:bg-neutral-700 text-white text-center font-bold text-xs flex items-center justify-center gap-1.5 transition-all border border-neutral-700">
              <i class="fa-solid fa-lock text-[10px] text-amber-400"></i> Painel CRM
            </a>
            <button onclick="copyNicheLink('${item.id}')" title="Copiar Link para Enviar ao Cliente" class="p-2 rounded-xl bg-neutral-800 hover:bg-neutral-700 text-slate-300 hover:text-white transition-all border border-neutral-700 text-xs">
              <i class="fa-solid fa-share-nodes"></i>
            </button>
          ` : `
            <a href="${item.dir}/index.html" target="_blank" class="flex-1 py-2 px-3 rounded-xl bg-white text-black hover:bg-slate-200 text-center font-bold text-xs flex items-center justify-center gap-1.5 transition-all shadow-sm">
              <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i> Ver Landing Page
            </a>
            <button onclick="copyDirectUrl('${item.dir}/index.html', '${item.name}')" title="Copiar Link" class="p-2 px-3 rounded-xl bg-neutral-800 hover:bg-neutral-700 text-slate-300 hover:text-white transition-all border border-neutral-700 text-xs flex items-center gap-1.5">
              <i class="fa-solid fa-copy"></i> Copiar Link
            </button>
          `}
        </div>
      </div>
    `;
  }

  // Double array to create seamless loop for slow sliding marquee
  const loopedFlagships = [...CRM_NICHES, ...CRM_NICHES];
  const flagshipsTrackHtml = loopedFlagships.map(renderCard).join('');

  // 1. Professional & Health Track (Saúde, Odonto, Direito, Arquitetura)
  const healthProcs = [
    CRM_NICHES.find(n => n.id === 'dentista'),
    CRM_NICHES.find(n => n.id === 'advogado'),
    CRM_NICHES.find(n => n.id === 'arquiteto'),
    LANDING_PAGES.find(n => n.id === 'psicologia'),
    LANDING_PAGES.find(n => n.id === 'oftalmologista'),
    LANDING_PAGES.find(n => n.id === 'nutricionista'),
    LANDING_PAGES.find(n => n.id === 'quiropraxista'),
    LANDING_PAGES.find(n => n.id === 'acupunturista'),
    LANDING_PAGES.find(n => n.id === 'podologo')
  ].filter(Boolean);

  const loopedHealth = [...healthProcs, ...healthProcs];

  // 2. Automotive, Motos & Speed Track
  const autoProcs = [
    CRM_NICHES.find(n => n.id === 'concessionaria-honda'),
    LANDING_PAGES.find(n => n.id === 'gtmotors'),
    LANDING_PAGES.find(n => n.id === 'shineray-uba'),
    LANDING_PAGES.find(n => n.id === 'topmotos032'),
    LANDING_PAGES.find(n => n.id === 'vrum-motos'),
    LANDING_PAGES.find(n => n.id === 'fumaca-motos'),
    LANDING_PAGES.find(n => n.id === 'rampabike')
  ].filter(Boolean);

  const loopedAuto = [...autoProcs, ...autoProcs];

  // 3. Gastronomy, Lifestyle & Services Track
  const lifestyleProcs = [
    CRM_NICHES.find(n => n.id === 'energia-solar'),
    CRM_NICHES.find(n => n.id === 'barbearia'),
    CRM_NICHES.find(n => n.id === 'banho-e-tosa'),
    CRM_NICHES.find(n => n.id === 'corretor-imoveis'),
    LANDING_PAGES.find(n => n.id === 'restaurante-egeu'),
    LANDING_PAGES.find(n => n.id === 'boteco-portugues'),
    LANDING_PAGES.find(n => n.id === 'caxixi'),
    LANDING_PAGES.find(n => n.id === 'reconcavo'),
    LANDING_PAGES.find(n => n.id === 'fotografo-casamento'),
    LANDING_PAGES.find(n => n.id === 'reforma-moveis'),
    LANDING_PAGES.find(n => n.id === 'lavanderia'),
    LANDING_PAGES.find(n => n.id === 'personal-trainer'),
    LANDING_PAGES.find(n => n.id === 'contador')
  ].filter(Boolean);

  const loopedLifestyle = [...lifestyleProcs, ...lifestyleProcs];

  // Grid for all items
  const allGridCardsHtml = [
    ...CRM_NICHES.map(item => `
      <div class="niche-grid-item" data-niche="${item.id}" data-category="crm ${item.category.toLowerCase()} ${item.id} ${item.name.toLowerCase()}">
        ${renderCard(item)}
      </div>
    `),
    ...LANDING_PAGES.map(item => `
      <div class="niche-grid-item" data-niche="${item.id}" data-category="landing ${item.category.toLowerCase()} ${item.id} ${item.name.toLowerCase()}">
        ${renderCard(item)}
      </div>
    `)
  ].join('');

  return `<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth bg-[#07090E] text-white">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NEXUS FLOW • Portfólio de Soluções Digitais & CRM por Nicho</title>
  <meta name="description" content="Ecossistema completo de captação e conversão por nicho: Landing Pages de alta conversão, Quebra de Objeções e CRM especializado." />
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>" />

  <!-- Google Fonts: Outfit, Plus Jakarta Sans & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet" />

  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            outfit: ['Outfit', 'sans-serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
          colors: {
            nexus: {
              black: '#07090E',
              dark: '#0D111A',
              card: '#131926',
              border: '#1E293B',
              indigo: '#6366F1',
              cyan: '#06B6D4',
              emerald: '#10B981',
              orange: '#F59E0B'
            }
          }
        }
      }
    };
  </script>

  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      height: 8px;
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #07090E;
    }
    ::-webkit-scrollbar-thumb {
      background: #1E293B;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #334155;
    }

    /* Hide scrollbar for clean horizontal scrolls */
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }

    /* Cinematic Glow & Gradients */
    .cinema-hero-bg {
      background: radial-gradient(circle at 50% 10%, rgba(99, 102, 241, 0.15) 0%, rgba(6, 182, 212, 0.08) 35%, rgba(7, 9, 14, 0.95) 75%), #07090E;
    }

    /* Slow Sliding Carousel Track Animation (Continuous horizontal flow) */
    @keyframes slowMarquee {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    @keyframes slowMarqueeReverse {
      0% { transform: translateX(-50%); }
      100% { transform: translateX(0); }
    }

    .slider-track {
      display: flex;
      gap: 1.25rem;
      width: max-content;
      animation: slowMarquee 75s linear infinite;
    }

    .slider-track-reverse {
      display: flex;
      gap: 1.25rem;
      width: max-content;
      animation: slowMarqueeReverse 85s linear infinite;
    }

    /* Pause sliding when hovering over carousel or card */
    .slider-wrapper:hover .slider-track,
    .slider-wrapper:hover .slider-track-reverse {
      animation-play-state: paused;
    }

    /* Glass Header */
    .glass-header {
      background: rgba(7, 9, 14, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }
  </style>
</head>
<body class="bg-[#07090E] text-slate-100 font-sans antialiased selection:bg-cyan-500 selection:text-black">

  <!-- ========================================================================= -->
  <!-- 1. HEADER REAL DO SITE (NEXUS FLOW BRANDING & QUICK NAVIGATION)           -->
  <!-- ========================================================================= -->
  <header class="sticky top-0 z-50 glass-header border-b border-white/10 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
      
      <!-- Brand Logo Oficial NEXUS FLOW -->
      <a href="index.html" class="flex items-center gap-3.5 group shrink-0">
        <div class="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500 via-indigo-600 to-cyan-400 flex items-center justify-center text-white text-xl shadow-lg shadow-indigo-500/25 group-hover:scale-105 transition-transform duration-300">
          <i class="fa-solid fa-layer-group"></i>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="font-outfit font-black text-2xl tracking-tight text-white">NEXUS</span>
            <span class="font-outfit font-black text-2xl tracking-tight text-cyan-400">FLOW</span>
          </div>
          <span class="block text-[9px] font-mono tracking-widest uppercase text-slate-400 font-semibold -mt-1">
            Sales Engineering & AI Systems
          </span>
        </div>
      </a>

      <!-- Desktop Nav Links Reais do Site -->
      <nav class="hidden md:flex items-center gap-8 text-xs lg:text-sm font-semibold text-slate-300">
        <a href="#hero-banner" class="hover:text-cyan-400 transition-colors">Início</a>
        <a href="#row-crm" class="hover:text-cyan-400 transition-colors flex items-center gap-2">
          <span>Sistemas com CRM</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">${CRM_NICHES.length} Nichos</span>
        </a>
        <a href="#row-todos" class="hover:text-cyan-400 transition-colors">Portfólio Completo (${totalCount})</a>
      </nav>

      <!-- Search & WhatsApp CTA Button Oficial -->
      <div class="flex items-center gap-3">
        <!-- Live Instant Search -->
        <div class="relative hidden sm:block w-44 lg:w-56">
          <input 
            type="text" 
            id="live-search-input" 
            oninput="handleSearch(this.value)" 
            placeholder="Buscar nicho (solar, odonto...)" 
            class="w-full pl-8 pr-7 py-2 rounded-full bg-neutral-900/90 border border-neutral-700 text-xs text-white placeholder-slate-400 focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 transition-all"
          />
          <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-xs text-slate-400"></i>
          <button id="clear-search-btn" onclick="clearSearch()" class="hidden absolute right-2.5 top-2.5 text-xs text-slate-400 hover:text-white">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- WhatsApp CTA Oficial -->
        <a href="https://wa.me/5532999292311?text=Olá!%20Gostaria%20de%20um%20diagnóstico%20gratuito%20para%20estruturar%20o%20fluxo%20de%20vendas%20e%20CRM%20da%20minha%20empresa." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-gradient-to-r from-indigo-500 to-cyan-500 hover:from-indigo-600 hover:to-cyan-400 text-white font-bold text-xs uppercase tracking-wider shadow-lg shadow-indigo-500/20 transition-all transform hover:scale-105 active:scale-95 shrink-0">
          <i class="fa-brands fa-whatsapp text-sm"></i>
          <span class="hidden sm:inline">Solicitar Diagnóstico</span>
          <span class="sm:hidden">WhatsApp</span>
        </a>
      </div>
    </div>

    <!-- Niche Filter Pills Bar (Subheader com Ícones de Cada Nicho) -->
    <div class="border-t border-white/10 bg-[#07090E]/95 py-2.5 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto flex items-center gap-2 overflow-x-auto no-scrollbar">
        ${pillsHtml}
      </div>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- 2. BILLBOARD HERO SECTION (FEATURED TITLE COM PRINT REAL DO HEADER)       -->
  <!-- ========================================================================= -->
  <section id="hero-banner" class="relative cinema-hero-bg border-b border-neutral-800 py-12 lg:py-18 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Top Badges -->
      <div class="flex flex-wrap items-center gap-2 mb-4">
        <span class="px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest bg-gradient-to-r from-indigo-500 to-cyan-500 text-white shadow-md flex items-center gap-1.5">
          <i class="fa-solid fa-bolt"></i> Destaque em Conversão 2026
        </span>
        <span class="px-3 py-1 rounded-full text-[10px] font-extrabold uppercase tracking-wider bg-neutral-900/90 text-slate-300 border border-neutral-700">
          Ecossistema 100% Integrado (Site + CRM)
        </span>
        <span class="text-xs font-black text-emerald-400 font-mono tracking-tight bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">
          Garantia Comprovada em Contrato
        </span>
      </div>

      <!-- Hero Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-7 space-y-5">
          <h1 id="hero-title" class="font-outfit font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-[1.1]">
            SunEco OS • <span class="text-emerald-400">Energia Solar</span>
          </h1>

          <p id="hero-tagline" class="text-sm sm:text-base font-semibold text-slate-300">
            Landing Page de Alta Conversão com Calculadora Solar 25 Anos + CRM Lumina OS
          </p>

          <p id="hero-desc" class="text-xs sm:text-sm text-slate-400 max-w-2xl leading-relaxed">
            O cliente acessa a página pública, simula a economia na conta de luz e agenda a vistoria técnica. Imediatamente o lead cai no Kanban do painel Lumina OS com gestão de inversores, rastreio de placas por lote e envio automático de lembretes no WhatsApp.
          </p>

          <!-- DESTAQUE CENTRAL: QUEBRA DE OBJEÇÃO (NO LUGAR DE ORÇAMENTO/PREÇO) -->
          <div id="hero-objection-box" class="p-4 rounded-2xl bg-gradient-to-r from-neutral-900 to-neutral-950 border border-cyan-500/30 shadow-lg max-w-2xl">
            <div class="flex items-center gap-2 mb-1">
              <span class="w-6 h-6 rounded-lg bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-xs">
                <i class="fa-solid fa-shield-check"></i>
              </span>
              <span class="text-xs font-bold uppercase tracking-wider text-cyan-300">
                Quebra de Objeção Principal do Nicho
              </span>
            </div>
            <p id="hero-objection-text" class="text-xs sm:text-sm text-slate-200 font-medium leading-relaxed">
              Zero investimento inicial: a economia imediata na conta de luz cobre a parcela da usina solar, com 25 anos de garantia e homologação sem burocracia.
            </p>
          </div>

          <!-- Action Buttons -->
          <div class="flex flex-wrap items-center gap-3 pt-2">
            <a id="hero-public-btn" href="energia-solar/index.html" target="_blank" class="px-6 py-3.5 rounded-xl bg-white text-black hover:bg-slate-200 font-bold text-sm flex items-center gap-2.5 transition-all shadow-xl shadow-white/10 transform hover:scale-105">
              <i class="fa-solid fa-play text-xs text-black"></i>
              <span>Ver Site Público</span>
            </a>
            <a id="hero-admin-btn" href="energia-solar/admin/index.html" target="_blank" class="px-6 py-3.5 rounded-xl bg-neutral-900/90 hover:bg-neutral-800 text-white font-bold text-sm flex items-center gap-2.5 transition-all border border-neutral-700 shadow-lg">
              <i class="fa-solid fa-lock text-xs text-amber-400"></i>
              <span>Abrir Painel CRM</span>
            </a>
            <button onclick="openNetflixModal('energia-solar')" class="px-4 py-3.5 rounded-xl bg-neutral-900/80 hover:bg-neutral-800 text-slate-300 hover:text-white text-sm font-semibold transition border border-neutral-800 flex items-center gap-2">
              <i class="fa-solid fa-circle-info"></i>
              <span>Detalhes & Proposta</span>
            </button>
          </div>

          <!-- Micro Metadados de Garantia -->
          <div class="flex items-center gap-6 pt-3 text-xs text-slate-400">
            <div class="flex items-center gap-2">
              <i class="fa-solid fa-circle-check text-emerald-400"></i>
              <span id="hero-kpi-1">Economia Garantida em Contrato</span>
            </div>
            <div class="flex items-center gap-2">
              <i class="fa-solid fa-shield-halved text-cyan-400"></i>
              <span>Lumina OS Kanban Integrado</span>
            </div>
            <div class="flex items-center gap-2">
              <i class="fa-solid fa-bolt text-amber-400"></i>
              <span>Anti-Spam por IP Ativo</span>
            </div>
          </div>
        </div>

        <!-- Hero Mockup Window com Screenshot Real -->
        <div class="lg:col-span-5">
          <div class="relative group rounded-3xl bg-neutral-900 border border-neutral-700/80 p-2 shadow-2xl overflow-hidden">
            <!-- Browser Header Bar -->
            <div class="px-4 py-3 bg-neutral-950/90 border-b border-neutral-800 flex items-center justify-between text-xs">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-rose-500/80"></span>
                <span class="w-3 h-3 rounded-full bg-amber-500/80"></span>
                <span class="w-3 h-3 rounded-full bg-emerald-500/80"></span>
                <span id="hero-preview-domain" class="ml-2 font-mono text-[11px] text-slate-400 bg-neutral-900 px-3 py-0.5 rounded-full border border-neutral-800">
                  suneco.com.br
                </span>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 flex items-center gap-1">
                <i class="fa-solid fa-lock text-[9px]"></i> SSL Seguro
              </span>
            </div>

            <!-- Actual Site Header Screenshot Image -->
            <div class="h-64 sm:h-72 w-full relative overflow-hidden bg-neutral-950">
              <img id="hero-preview-img" src="assets/previews/energia-solar.png" alt="Preview Real do Site" class="w-full h-full object-cover object-top transition-all duration-500 group-hover:scale-102" />
              <div class="absolute inset-0 bg-gradient-to-t from-neutral-900/70 via-transparent to-transparent pointer-events-none"></div>
            </div>

            <!-- Quick Footer with Switcher -->
            <div class="p-3 bg-neutral-950 border-t border-neutral-800 flex items-center justify-between text-xs">
              <span class="text-[11px] text-slate-400 font-medium flex items-center gap-1.5">
                <i class="fa-solid fa-camera text-cyan-400"></i> Print Real do Site
              </span>
              <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
                ${CRM_NICHES.map(n => `
                  <button onclick="setHeroFeature('${n.id}')" title="${n.name}" class="w-7 h-7 rounded-lg bg-neutral-900 hover:bg-neutral-800 border border-neutral-800 hover:border-cyan-500/50 flex items-center justify-center text-xs transition shrink-0" style="color: ${n.accentColor}">
                    <i class="fa-solid ${n.icon}"></i>
                  </button>
                `).join('')}
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 3. ROW 1: EM ALTA (SISTEMAS COMPLETOS COM CRM - ANIMAÇÃO LENTA)           -->
  <!-- ========================================================================= -->
  <section id="row-crm" class="pt-10 pb-8 overflow-hidden relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-4 flex items-center justify-between">
      <div>
        <h2 class="text-xl sm:text-2xl font-black text-white font-outfit flex items-center gap-2.5">
          <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
          🔥 Em Alta: Ecossistemas Completos (Site Público + Painel CRM)
        </h2>
        <p class="text-xs text-slate-400 mt-1">
          Deslize suavemente ou passe o cursor sobre qualquer card para pausar e abrir o sistema.
        </p>
      </div>

      <!-- Row Navigation Arrows -->
      <div class="flex items-center gap-2">
        <button onclick="scrollRow('track-flagships', -340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-left"></i>
        </button>
        <button onclick="scrollRow('track-flagships', 340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-right"></i>
        </button>
      </div>
    </div>

    <!-- Infinite Slow Sliding Carousel Track (Pause on Hover) -->
    <div class="slider-wrapper w-full overflow-x-auto no-scrollbar py-4 px-4 sm:px-6 lg:px-8">
      <div id="track-flagships" class="slider-track">
        ${flagshipsTrackHtml}
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 4. ROW 2: PROFISSIONAIS LIBERAIS, SAÚDE & DIREITO                         -->
  <!-- ========================================================================= -->
  <section class="py-6 overflow-hidden relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-4 flex items-center justify-between">
      <div>
        <h2 class="text-lg sm:text-xl font-black text-white font-outfit flex items-center gap-2.5">
          <i class="fa-solid fa-stethoscope text-cyan-400"></i>
          💼 Consultórios, Saúde Especializada & Advocacia de Alto Padrão
        </h2>
        <p class="text-xs text-slate-400 mt-1">Odontologia, Direito, Arquitetura, Psicologia, Oftalmologia, Nutrição, Quiropraxia e Acupuntura.</p>
      </div>

      <div class="flex items-center gap-2">
        <button onclick="scrollRow('track-health', -340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-left"></i>
        </button>
        <button onclick="scrollRow('track-health', 340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-right"></i>
        </button>
      </div>
    </div>

    <div class="slider-wrapper w-full overflow-x-auto no-scrollbar py-4 px-4 sm:px-6 lg:px-8">
      <div id="track-health" class="slider-track-reverse">
        ${loopedHealth.map(renderCard).join('')}
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 5. ROW 3: AUTOMOTIVO, SUPERCARROS & MOTOCICLISMO                          -->
  <!-- ========================================================================= -->
  <section class="py-6 overflow-hidden relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-4 flex items-center justify-between">
      <div>
        <h2 class="text-lg sm:text-xl font-black text-white font-outfit flex items-center gap-2.5">
          <i class="fa-solid fa-motorcycle text-red-400"></i>
          🏎️ Concessionárias, Supercarros, Motos & Mobilidade
        </h2>
        <p class="text-xs text-slate-400 mt-1">Honda Automotivo, GT Motors Supercarros, Shineray Ubá, Top Motos 032, Vrum Motos, Fumaça Motos e Rampa Bike.</p>
      </div>

      <div class="flex items-center gap-2">
        <button onclick="scrollRow('track-auto', -340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-left"></i>
        </button>
        <button onclick="scrollRow('track-auto', 340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-right"></i>
        </button>
      </div>
    </div>

    <div class="slider-wrapper w-full overflow-x-auto no-scrollbar py-4 px-4 sm:px-6 lg:px-8">
      <div id="track-auto" class="slider-track">
        ${loopedAuto.map(renderCard).join('')}
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 6. ROW 4: GASTRONOMIA, ESTILO DE VIDA, SERVIÇOS & NEGÓCIOS                -->
  <!-- ========================================================================= -->
  <section class="py-6 overflow-hidden relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-4 flex items-center justify-between">
      <div>
        <h2 class="text-lg sm:text-xl font-black text-white font-outfit flex items-center gap-2.5">
          <i class="fa-solid fa-utensils text-amber-400"></i>
          🍷 Gastronomia, Estilo de Vida, Serviços & Negócios
        </h2>
        <p class="text-xs text-slate-400 mt-1">Bares e Restaurantes, Barbearias, Pet Shops, Fotografia de Casamento, Reforma de Móveis e Serviços.</p>
      </div>

      <div class="flex items-center gap-2">
        <button onclick="scrollRow('track-lifestyle', -340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-left"></i>
        </button>
        <button onclick="scrollRow('track-lifestyle', 340)" class="w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center transition border border-neutral-700 text-xs">
          <i class="fa-solid fa-chevron-right"></i>
        </button>
      </div>
    </div>

    <div class="slider-wrapper w-full overflow-x-auto no-scrollbar py-4 px-4 sm:px-6 lg:px-8">
      <div id="track-lifestyle" class="slider-track-reverse">
        ${loopedLifestyle.map(renderCard).join('')}
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 7. COMPLETE GRID VIEW & FILTERED SEARCH RESULTS                           -->
  <!-- ========================================================================= -->
  <section id="row-todos" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-24">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8 border-b border-neutral-800 pb-5">
      <div>
        <h2 id="grid-section-title" class="text-2xl font-black text-white font-outfit flex items-center gap-2.5">
          <i class="fa-solid fa-border-all text-cyan-400"></i>
          Catálogo Geral de Soluções
        </h2>
        <p id="grid-section-subtitle" class="text-xs text-slate-400 mt-1">
          Exibindo todos os ${totalCount} projetos e CRMs disponíveis no ecossistema com prints reais e identidade autoral.
        </p>
      </div>

      <!-- Counter Badge -->
      <div id="results-count-badge" class="text-xs font-bold text-slate-400 bg-neutral-900 border border-neutral-800 px-3.5 py-1.5 rounded-full">
        ${totalCount} Soluções Cadastradas
      </div>
    </div>

    <!-- Responsive Grid -->
    <div id="niche-grid-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      ${allGridCardsHtml}
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 8. QUICK LOOK / DETAIL MODAL WITH PRINT REAL & EPISODES                   -->
  <!-- ========================================================================= -->
  <div id="netflix-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden items-center justify-center p-4 sm:p-6 overflow-y-auto">
    <div class="relative w-full max-w-4xl rounded-3xl bg-neutral-900 border border-neutral-800 shadow-2xl overflow-hidden my-8" onclick="event.stopPropagation()">
      
      <!-- Close Button -->
      <button onclick="closeNetflixModal()" class="absolute top-4 right-4 z-20 w-10 h-10 rounded-full bg-black/80 hover:bg-neutral-800 text-white flex items-center justify-center transition border border-white/20">
        <i class="fa-solid fa-xmark text-lg"></i>
      </button>

      <!-- Modal Banner with Real Screenshot Image -->
      <div id="modal-banner" class="h-64 sm:h-80 w-full relative bg-neutral-950 flex flex-col justify-end p-6 sm:p-8">
        <div class="relative z-10 space-y-2">
          <div class="flex items-center gap-2">
            <span id="modal-badge" class="px-2.5 py-1 rounded-full text-[10px] font-extrabold uppercase tracking-wider bg-white text-black font-mono">
              ENERGIA SOLAR
            </span>
            <span id="modal-match" class="text-xs font-bold text-emerald-400 font-mono bg-black/70 px-2 py-0.5 rounded border border-emerald-500/30">
              99% Relevante
            </span>
          </div>
          <h2 id="modal-title" class="text-2xl sm:text-4xl font-black text-white font-outfit">
            SunEco OS • Energia Solar
          </h2>
          <p id="modal-tagline" class="text-xs sm:text-sm font-medium text-slate-300 max-w-xl">
            Landing Page de Alta Conversão + CRM Fotovoltaico
          </p>
        </div>
      </div>

      <!-- Modal Body -->
      <div class="p-6 sm:p-8 space-y-6">
        
        <!-- QUEBRA DE OBJEÇÃO (NO LUGAR DE PREÇO/ORÇAMENTO) -->
        <div class="p-4 rounded-2xl bg-neutral-950 border border-neutral-800">
          <div class="text-[11px] font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5 mb-1">
            <i class="fa-solid fa-shield-check text-emerald-400 text-sm"></i> Quebra de Objeção Comercial (Alta Conversão)
          </div>
          <p id="modal-objection" class="text-sm text-slate-200 leading-relaxed font-medium">
            Zero investimento inicial: a economia imediata na conta de luz cobre a parcela da usina solar.
          </p>
        </div>

        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Visão Geral da Solução</h4>
          <p id="modal-desc" class="text-sm text-slate-300 leading-relaxed">
            Descrição do sistema e automações.
          </p>
        </div>

        <!-- Links Rápidos e Acesso aos Ambientes -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Ambientes do Ecossistema</h4>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            
            <!-- Link Site Público -->
            <a id="modal-ep1-link" href="#" target="_blank" class="p-4 rounded-2xl bg-neutral-950 hover:bg-neutral-800 border border-neutral-800 hover:border-neutral-600 transition flex items-center gap-4 group">
              <div class="w-12 h-12 rounded-xl bg-white text-black flex items-center justify-center text-xl shrink-0 group-hover:scale-105 transition-transform shadow-md">
                <i class="fa-solid fa-play"></i>
              </div>
              <div class="overflow-hidden">
                <div class="text-[10px] font-bold uppercase tracking-wider text-emerald-400">Ambiente do Cliente</div>
                <div class="text-sm font-bold text-white truncate">Site / Landing Page</div>
                <div class="text-xs text-slate-400 truncate">Calculadoras, Prova Social & WhatsApp</div>
              </div>
            </a>

            <!-- Link CRM Admin -->
            <a id="modal-ep2-link" href="#" target="_blank" class="p-4 rounded-2xl bg-neutral-950 hover:bg-neutral-800 border border-neutral-800 hover:border-neutral-600 transition flex items-center gap-4 group">
              <div class="w-12 h-12 rounded-xl bg-neutral-800 text-amber-400 flex items-center justify-center text-xl shrink-0 border border-neutral-700 group-hover:scale-105 transition-transform shadow-md">
                <i class="fa-solid fa-lock"></i>
              </div>
              <div class="overflow-hidden">
                <div class="text-[10px] font-bold uppercase tracking-wider text-amber-400">Ambiente de Gestão</div>
                <div class="text-sm font-bold text-white truncate">Painel CRM Operacional</div>
                <div class="text-xs text-slate-400 truncate">Kanban, Lotes, Faturamento & Disparos</div>
              </div>
            </a>
          </div>
        </div>

        <!-- Link Direto para Enviar ao Cliente -->
        <div class="p-4 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2">
          <div class="text-xs font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-share-nodes text-cyan-400"></i>
            <span>Link Direto deste Nicho para Apresentar ao Cliente:</span>
          </div>
          <div class="flex items-center gap-2">
            <input id="modal-share-input" type="text" readonly class="w-full bg-neutral-900 border border-neutral-700 rounded-xl px-3 py-2 text-xs font-mono text-slate-300 focus:outline-none" />
            <button onclick="copyModalLink()" class="px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-black font-bold text-xs shrink-0 flex items-center gap-1.5 transition">
              <i class="fa-solid fa-copy"></i> Copiar Link
            </button>
          </div>
          <p class="text-[11px] text-slate-400">
            💡 Envie este link diretamente no WhatsApp do seu cliente para que o portfólio já abra diretamente na solução dele!
          </p>
        </div>

      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 9. FOOTER REAL DO SITE                                                    -->
  <!-- ========================================================================= -->
  <footer class="border-t border-neutral-800 bg-[#05070B] py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-slate-400">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-bold text-sm">
          <i class="fa-solid fa-layer-group"></i>
        </div>
        <div>
          <span class="font-outfit font-black text-sm text-white tracking-wider">NEXUS FLOW</span>
          <p class="text-[11px] text-slate-400">Ecossistema de Soluções Digitais & CRM por Nicho</p>
        </div>
      </div>

      <div class="flex items-center gap-6">
        <a href="#hero-banner" class="hover:text-white transition">Voltar ao Topo</a>
        <a href="#row-crm" class="hover:text-white transition">Sistemas CRM</a>
        <a href="#row-todos" class="hover:text-white transition">Catálogo Geral</a>
        <a href="https://wa.me/5532999292311" target="_blank" class="hover:text-white transition text-cyan-400">Falar com Consultor</a>
      </div>

      <div class="text-right">
        <span>© 2026 NEXUS FLOW. Todos os direitos reservados.</span>
      </div>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- TOAST NOTIFICATION CONTAINER                                              -->
  <!-- ========================================================================= -->
  <div id="toast-container" class="fixed bottom-6 right-6 z-50 flex flex-col gap-2 pointer-events-none"></div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT LOGIC (SEARCH, FILTERING, SLIDERS & URL ROUTING)              -->
  <!-- ========================================================================= -->
  <script>
    // All Niches Data
    const NICHES_DATA = ${JSON.stringify(CRM_NICHES)};
    const ALL_ITEMS_COUNT = ${totalCount};

    // Smooth horizontal scroll for carousel buttons
    function scrollRow(trackId, offset) {
      const track = document.getElementById(trackId);
      if (track) {
        track.scrollBy({ left: offset, behavior: 'smooth' });
      }
    }

    // Set Hero Billboard
    function setHeroFeature(nicheId) {
      const niche = NICHES_DATA.find(n => n.id === nicheId);
      if (!niche) return;

      document.getElementById('hero-title').innerHTML = niche.name + ' • <span style="color: ' + niche.accentColor + '">' + niche.brand + '</span>';
      document.getElementById('hero-tagline').textContent = niche.tagline;
      document.getElementById('hero-desc').textContent = niche.desc;
      document.getElementById('hero-objection-text').textContent = niche.objectionBreaker;
      document.getElementById('hero-kpi-1').textContent = niche.guarantee;
      document.getElementById('hero-public-btn').setAttribute('href', niche.publicUrl);
      document.getElementById('hero-admin-btn').setAttribute('href', niche.adminUrl);

      // Update real screenshot in the browser mockup
      const heroImg = document.getElementById('hero-preview-img');
      if (heroImg) heroImg.src = niche.previewImg;
      
      const domainEl = document.getElementById('hero-preview-domain');
      if (domainEl) domainEl.textContent = niche.domain;

      // Smooth scroll to hero
      const hero = document.getElementById('hero-banner');
      if (hero) hero.scrollIntoView({ behavior: 'smooth' });

      showToast('Destaque alterado para ' + niche.name, 'info');
    }

    // Filter by Niche Pill
    function filterByNiche(nicheKey) {
      // Update active pill button state
      document.querySelectorAll('.niche-pill').forEach(btn => {
        btn.classList.remove('active', 'bg-white', 'text-black');
        btn.classList.add('bg-neutral-900/80', 'text-slate-300');
      });

      const clickedBtn = event ? event.currentTarget : null;
      if (clickedBtn) {
        clickedBtn.classList.remove('bg-neutral-900/80', 'text-slate-300');
        clickedBtn.classList.add('active', 'bg-white', 'text-black');
      }

      const gridItems = document.querySelectorAll('.niche-grid-item');
      let visibleCount = 0;
      const targetLower = (nicheKey || '').toLowerCase();

      gridItems.forEach(item => {
        const itemNiche = (item.getAttribute('data-niche') || '').toLowerCase();
        const itemCategory = (item.getAttribute('data-category') || '').toLowerCase();

        if (nicheKey === 'all') {
          item.classList.remove('hidden');
          visibleCount++;
        } else if (nicheKey === 'crm') {
          if (itemCategory.includes('crm')) {
            item.classList.remove('hidden');
            visibleCount++;
          } else {
            item.classList.add('hidden');
          }
        } else {
          if (itemNiche === targetLower || itemCategory.includes(targetLower)) {
            item.classList.remove('hidden');
            visibleCount++;
          } else {
            item.classList.add('hidden');
          }
        }
      });

      // Update badge
      const badge = document.getElementById('results-count-badge');
      if (badge) {
        badge.textContent = visibleCount + ' Soluções Encontradas';
      }

      // Smooth scroll to catalog grid if filtering a specific niche
      if (nicheKey !== 'all') {
        const gridSection = document.getElementById('row-todos');
        if (gridSection) gridSection.scrollIntoView({ behavior: 'smooth' });
      }
    }

    // Live Instant Search
    function handleSearch(term) {
      const cleanTerm = (term || '').trim().toLowerCase();
      const clearBtn = document.getElementById('clear-search-btn');
      if (clearBtn) {
        if (cleanTerm) clearBtn.classList.remove('hidden');
        else clearBtn.classList.add('hidden');
      }

      const gridItems = document.querySelectorAll('.niche-grid-item');
      let count = 0;

      gridItems.forEach(item => {
        const text = (item.textContent || '').toLowerCase();
        const niche = (item.getAttribute('data-niche') || '').toLowerCase();
        const category = (item.getAttribute('data-category') || '').toLowerCase();

        if (!cleanTerm || text.includes(cleanTerm) || niche.includes(cleanTerm) || category.includes(cleanTerm)) {
          item.classList.remove('hidden');
          count++;
        } else {
          item.classList.add('hidden');
        }
      });

      const badge = document.getElementById('results-count-badge');
      if (badge) {
        badge.textContent = cleanTerm ? count + ' resultados para "' + cleanTerm + '"' : ALL_ITEMS_COUNT + ' Soluções Cadastradas';
      }

      if (cleanTerm && count > 0) {
        const gridSection = document.getElementById('row-todos');
        if (gridSection) gridSection.scrollIntoView({ behavior: 'smooth' });
      }
    }

    function clearSearch() {
      const input = document.getElementById('live-search-input');
      if (input) input.value = '';
      handleSearch('');
    }

    // Modal Logic
    let currentModalNiche = null;

    function openNetflixModal(nicheId) {
      const niche = NICHES_DATA.find(n => n.id === nicheId);
      if (!niche) return;

      currentModalNiche = niche;

      document.getElementById('modal-title').textContent = niche.brand + ' • ' + niche.name;
      document.getElementById('modal-tagline').textContent = niche.tagline;
      document.getElementById('modal-desc').textContent = niche.desc;
      document.getElementById('modal-objection').textContent = niche.objectionBreaker;
      document.getElementById('modal-badge').textContent = niche.name.toUpperCase();
      document.getElementById('modal-match').textContent = niche.matchScore;
      
      // Real screenshot background in modal header
      document.getElementById('modal-banner').style.backgroundImage = "linear-gradient(to top, #171717 15%, rgba(23, 23, 23, 0.4) 65%, rgba(0, 0, 0, 0.2) 100%), url('" + niche.previewImg + "')";
      document.getElementById('modal-banner').style.backgroundSize = 'cover';
      document.getElementById('modal-banner').style.backgroundPosition = 'top center';

      document.getElementById('modal-ep1-link').setAttribute('href', niche.publicUrl);
      document.getElementById('modal-ep2-link').setAttribute('href', niche.adminUrl);

      // Direct Client Share URL
      const shareUrl = window.location.origin + window.location.pathname.replace('index.html', '') + '?nicho=' + niche.id;
      document.getElementById('modal-share-input').value = shareUrl;

      const modal = document.getElementById('netflix-modal');
      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
      }
    }

    function closeNetflixModal() {
      const modal = document.getElementById('netflix-modal');
      if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
    }

    // Close on Escape or click outside
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeNetflixModal();
    });

    document.getElementById('netflix-modal').addEventListener('click', (e) => {
      if (e.target.id === 'netflix-modal') closeNetflixModal();
    });

    // Copy Links & Toasts
    function copyNicheLink(nicheId) {
      const shareUrl = window.location.origin + window.location.pathname.replace('index.html', '') + '?nicho=' + nicheId;
      navigator.clipboard.writeText(shareUrl).then(() => {
        showToast('Link exclusivo do nicho ' + nicheId + ' copiado com sucesso!', 'success');
      }).catch(() => {
        prompt('Copie o link:', shareUrl);
      });
    }

    function copyModalLink() {
      const input = document.getElementById('modal-share-input');
      if (input) {
        navigator.clipboard.writeText(input.value).then(() => {
          showToast('Link do cliente copiado! Pode enviar no WhatsApp.', 'success');
        });
      }
    }

    function copyDirectUrl(relUrl, title) {
      const fullUrl = window.location.origin + window.location.pathname.replace('index.html', '') + relUrl;
      navigator.clipboard.writeText(fullUrl).then(() => {
        showToast('Link de ' + title + ' copiado!', 'success');
      }).catch(() => {
        prompt('Copie o link:', fullUrl);
      });
    }

    function showToast(message, type = 'info') {
      const container = document.getElementById('toast-container');
      if (!container) return;

      const toast = document.createElement('div');
      toast.className = 'px-4 py-3 rounded-2xl bg-neutral-900 border border-neutral-700 text-white shadow-2xl text-xs font-bold flex items-center gap-2.5 transition-all transform translate-y-4 opacity-0 pointer-events-auto';
      
      const icon = type === 'success' 
        ? '<i class="fa-solid fa-circle-check text-emerald-400 text-sm"></i>' 
        : '<i class="fa-solid fa-circle-info text-cyan-400 text-sm"></i>';

      toast.innerHTML = icon + '<span>' + message + '</span>';
      container.appendChild(toast);

      // Animate in
      requestAnimationFrame(() => {
        toast.classList.remove('translate-y-4', 'opacity-0');
      });

      // Remove after 3.5s
      setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-y-4');
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }

    // =========================================================================
    // URL ROUTING & NICHE AUTOFILTER (?nicho=energia-solar)
    // =========================================================================
    window.addEventListener('DOMContentLoaded', () => {
      const params = new URLSearchParams(window.location.search);
      const targetNiche = params.get('nicho');
      const searchTerm = params.get('q') || params.get('busca');

      if (targetNiche) {
        // If client opened with ?nicho=energia-solar
        setHeroFeature(targetNiche);
        filterByNiche(targetNiche);
        openNetflixModal(targetNiche);
        showToast('Exibindo projeto especializado em ' + targetNiche, 'success');
      } else if (searchTerm) {
        const input = document.getElementById('live-search-input');
        if (input) input.value = searchTerm;
        handleSearch(searchTerm);
      }
    });
  </script>
</body>
</html>`;
}

function run() {
  console.log('Generating Enhanced Showcase with Real Screenshots for EVERY SINGLE CARD in all rows & grid...');
  const html = buildHtml();
  fs.writeFileSync(OUTPUT_FILE, html, 'utf8');
  console.log('✅ Master index.html built successfully at:', OUTPUT_FILE);
  console.log('   - File size:', (html.length / 1024).toFixed(1), 'KB');
  console.log('   - Total Sites Included:', CRM_NICHES.length + LANDING_PAGES.length);
  console.log('   - Real Header Screenshots: Used in 100% of cards in every carousel row and grid');
  console.log('   - Objection Breakers: 100% active, zero budget quotes');
}

run();
