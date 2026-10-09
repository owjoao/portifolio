/**
 * UNIVERSAL NICHE CRM ENGINE FACTORY
 * Generates and installs specialized, secure, lot-based CRMs
 * for each website niche in the portfolio.
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

const NICHE_CONFIGS = [
  {
    dir: 'advogado',
    title: 'LexPro OS • Gestão Jurídica, Prazos OAB & CRM',
    shortName: 'LexPro OS',
    badge: 'Advocacia & Jurídico',
    icon: 'fa-scale-balanced',
    themeColor: '#1E293B',
    accentClass: 'theme-solar-blue',
    serviceType: 'Consultoria & Processos',
    defaultClients: [
      { id: 'c1', name: 'Dr. Marcos Valente', phone: '(32) 99111-2233', date: '2026-10-01', service: 'Direito Tributário', value: 15000, stage: 'vistoria' },
      { id: 'c2', name: 'Juliana Pires', phone: '(32) 98822-3344', date: '2026-10-05', service: 'Inventário & Família', value: 8500, stage: 'homologacao' },
      { id: 'c3', name: 'Construtora Horizonte', phone: '(32) 99444-5566', date: '2026-09-27', service: 'Assessoria Trabalhista', value: 24000, stage: 'concluido' }
    ],
    defaultBatches: [
      { id: 'b1', item: 'Perícia Técnica Contábil', code: 'PER-2026-01', supplier: 'Instituto Pericial MG', date: '2026-08-15', qty: 5, unitCost: 1200.00 },
      { id: 'b2', item: 'Certidões Negativas Cartoriais', code: 'CERT-LOTE-2', supplier: 'Cartório Central', date: '2026-09-10', qty: 20, unitCost: 95.00 },
      { id: 'b3', item: 'Diligências Correspondente Externa', code: 'DIL-LOTE-3', supplier: 'Rede Correspondentes', date: '2026-09-02', qty: 10, unitCost: 250.00 }
    ],
    defaultTasks: [
      { id: 't1', title: 'Protocolar Apelação Cível no TJMG - Prazo Fatal', due: '2026-10-01', priority: 'alta', done: false },
      { id: 't2', title: 'Audiência de Conciliação Virtual - Juliana Pires', due: '2026-10-03', priority: 'alta', done: false }
    ],
    defaultDocs: [
      { id: 'd1', title: 'Procuração Ad Judicia com Poderes Específicos', client: 'Dr. Marcos Valente', cat: 'Procuração', date: '2026-09-28', status: 'Assinada' },
      { id: 'd2', title: 'Petição Inicial & Guia de Custas Judiciais', client: 'Juliana Pires', cat: 'Petição', date: '2026-09-25', status: 'Protocolada' }
    ],
    waTemplates: {
      t1Name: 'Lembrete de Audiência / Consulta',
      t1Msg: 'Olá {NAME}, tudo bem? Confirmamos sua consulta jurídica agendada para {DATE}. Qualquer documento novo pode nos enviar por aqui!',
      t2Name: 'Andamento Processual',
      t2Msg: 'Olá {NAME}! Temos novidades no seu processo ({SERVICE}). Uma nova movimentação favorável foi registrada pelo tribunal.',
      t3Name: 'Assinatura de Documento',
      t3Msg: 'Olá {NAME}! Enviamos a procuração para assinatura digital. Por favor confira e nos avise assim que rubricar.'
    },
    deadlines: [
      { title: 'Prazo Fatal Recurso Ordinário (Processo 00412-2026)', days: '1 dia restante', icon: 'fa-gavel' },
      { title: 'Audiência de Instrução e Julgamento - Vara Cível', days: '3 dias restantes', icon: 'fa-calendar-check' }
    ]
  },
  {
    dir: 'concessionaria-honda',
    title: 'AutoDrive OS • Gestão de Veículos, Lotes & Financiamentos',
    shortName: 'AutoDrive OS',
    badge: 'Concessionária & Veículos',
    icon: 'fa-car-side',
    themeColor: '#DC2626',
    accentClass: 'theme-solar-amber',
    serviceType: 'Venda & Financiamento',
    defaultClients: [
      { id: 'c1', name: 'Rodrigo Mendonça', phone: '(32) 99822-1144', date: '2026-10-01', service: 'Honda Civic Touring', value: 165000, stage: 'vistoria' },
      { id: 'c2', name: 'Dra. Camila Toledo', phone: '(32) 99933-4455', date: '2026-10-03', service: 'Honda HR-V EXL', value: 148000, stage: 'homologacao' },
      { id: 'c3', name: 'Lucas Bertoli', phone: '(32) 98844-7788', date: '2026-09-28', service: 'Honda City Hatch', value: 115000, stage: 'concluido' }
    ],
    defaultBatches: [
      { id: 'b1', item: 'Lote Veículos Novos Faturamento Direto', code: 'LOTE-FAT-01', supplier: 'Montadora Honda Brasil', date: '2026-08-10', qty: 8, unitCost: 108000.00 },
      { id: 'b2', item: 'Lote Seminovos Selecionados Revisados', code: 'LOTE-SEMI-02', supplier: 'Repasse Frotistas', date: '2026-09-01', qty: 12, unitCost: 74000.00 },
      { id: 'b3', item: 'Kit Acessórios Originais & Película Solar', code: 'KIT-ACES-03', supplier: 'Acessórios Autorizados', date: '2026-09-12', qty: 25, unitCost: 650.00 }
    ],
    defaultTasks: [
      { id: 't1', title: 'Vistoria Cautelar Dekra - Honda Civic', due: '2026-10-01', priority: 'alta', done: false },
      { id: 't2', title: 'Aprovação de Crédito Bancário - Camila Toledo', due: '2026-10-02', priority: 'alta', done: false }
    ],
    defaultDocs: [
      { id: 'd1', title: 'Laudo de Vistoria Cautelar 100% Aprovado', client: 'Rodrigo Mendonça', cat: 'Laudo Pericial', date: '2026-09-28', status: 'Aprovado' },
      { id: 'd2', title: 'Contrato de Compra e Venda com Reserva', client: 'Dra. Camila Toledo', cat: 'Contrato', date: '2026-09-26', status: 'Assinado' }
    ],
    waTemplates: {
      t1Name: 'Confirmação de Test-Drive',
      t1Msg: 'Olá {NAME}! Tudo pronto para seu Test-Drive do {SERVICE} na data de {DATE}! O carro já está higienizado e abastecido esperando você.',
      t2Name: 'Aprovação de Financiamento',
      t2Msg: 'Parabéns {NAME}! Sua proposta de financiamento para o {SERVICE} foi APROVADA com taxa especial! Quando podemos assinar?',
      t3Name: 'Entrega das Chaves',
      t3Msg: 'Grande dia {NAME}! O seu veículo está pronto para entrega na nossa concessionária com polimento e tanque cheio!'
    },
    deadlines: [
      { title: 'Vencimento de Reserva de Taxa Promocional Bancária', days: '2 dias restantes', icon: 'fa-percent' },
      { title: 'Transferência de Propriedade DETRAN (Prazo 30 dias)', days: '4 dias restantes', icon: 'fa-id-card' }
    ]
  },
  {
    dir: 'arquiteto',
    title: 'StudioDesign OS • Gestão de Obras, Lotes & Projetos 3D',
    shortName: 'StudioDesign OS',
    badge: 'Arquitetura & Engenharia',
    icon: 'fa-compass-drafting',
    themeColor: '#0F172A',
    accentClass: 'theme-solar-violet',
    serviceType: 'Projeto & Interiores',
    defaultClients: [
      { id: 'c1', name: 'Marcelo Faria', phone: '(32) 99122-3344', date: '2026-10-02', service: 'Projeto Arquitetônico Completo', value: 28000, stage: 'vistoria' },
      { id: 'c2', name: 'Dra. Larissa Ramos', phone: '(32) 98855-6677', date: '2026-10-04', service: 'Design de Interiores Clínica', value: 19500, stage: 'homologacao' }
    ],
    defaultBatches: [
      { id: 'b1', item: 'Lote Madeira Maciça Cumaru para Deck', code: 'MAD-CUM-01', supplier: 'Madereira Tropical', date: '2026-08-20', qty: 50, unitCost: 180.00 },
      { id: 'b2', item: 'Porcelanato Calacata 120x120 Lote A', code: 'POR-CAL-02', supplier: 'Portobello Shop', date: '2026-09-05', qty: 80, unitCost: 145.00 },
      { id: 'b3', item: 'Luminárias Embutidas LED No-Glare', code: 'LUM-LED-03', supplier: 'Iluminação & Conceito', date: '2026-09-12', qty: 35, unitCost: 85.00 }
    ],
    defaultTasks: [
      { id: 't1', title: 'Aprovação de Alvará de Construção na Prefeitura', due: '2026-10-02', priority: 'alta', done: false },
      { id: 't2', title: 'Medição a Laser no Imóvel - Marcelo Faria', due: '2026-10-03', priority: 'media', done: false }
    ],
    defaultDocs: [
      { id: 'd1', title: 'Planta Baixa Executiva & Cortes DWG', client: 'Marcelo Faria', cat: 'Projetos DWG', date: '2026-09-28', status: 'Concluído' },
      { id: 'd2', title: 'Memorial Descritivo de Acabamentos', client: 'Dra. Larissa Ramos', cat: 'Memorial', date: '2026-09-25', status: 'Revisado' }
    ],
    waTemplates: {
      t1Name: 'Apresentação Render 3D',
      t1Msg: 'Olá {NAME}! Finalizamos os renders foto-realistas do seu projeto ({SERVICE})! Vamos agendar a apresentação?',
      t2Name: 'Vistoria de Obra',
      t2Msg: 'Olá {NAME}! Passando para avisar que estivemos na obra para a vistoria técnica e a concretagem foi aprovada com sucesso!',
      t3Name: 'Lista de Compras / Especificação',
      t3Msg: 'Olá {NAME}! Segue a lista detalhada de pisos e acabamentos aprovados para aquisição com o desconto dos nossos parceiros.'
    },
    deadlines: [
      { title: 'Prazo Limite Resposta de Comunigado Prefeitura', days: '2 dias restantes', icon: 'fa-building-columns' },
      { title: 'Fechamento de Pedido de Porcelanato Lote Especial', days: '4 dias restantes', icon: 'fa-ruler-combined' }
    ]
  },
  {
    dir: 'banho-e-tosa',
    title: 'PetCare OS • Gestão Pet, Banho & Tosa, Lotes & CRM',
    shortName: 'PetCare OS',
    badge: 'Pet Shop & Estética Pet',
    icon: 'fa-paw',
    themeColor: '#059669',
    accentClass: 'theme-solar-emerald',
    serviceType: 'Estética & Saúde Pet',
    defaultClients: [
      { id: 'c1', name: 'Luna (Golden Retriever) - Tutor: André', phone: '(32) 99877-1122', date: '2026-09-30', service: 'Banho Terapêutico + Tosa Higiênica', value: 160, stage: 'vistoria' },
      { id: 'c2', name: 'Thor (Spitz Alemão) - Tutora: Fernanda', phone: '(32) 99122-8899', date: '2026-10-01', service: 'Tosa na Tesoura + Hidratação Argan', value: 190, stage: 'homologacao' },
      { id: 'c3', name: 'Pipoca (Poodle) - Tutora: Beatriz', phone: '(32) 98844-3322', date: '2026-09-29', service: 'Banho Completo + Corte de Unhas', value: 110, stage: 'concluido' }
    ],
    defaultBatches: [
      { id: 'b1', item: 'Shampoo Hipoalergênico Dermacare 5L', code: 'SHP-DER-01', supplier: 'Petbrilho Distribuidora', date: '2026-08-10', qty: 10, unitCost: 140.00 },
      { id: 'b2', item: 'Condicionador Hidratação Ouro 5L', code: 'COND-OUR-02', supplier: 'Petbrilho Distribuidora', date: '2026-09-01', qty: 8, unitCost: 165.00 },
      { id: 'b3', item: 'Lâminas de Tosa Profissionais Cerâmica 10', code: 'LAM-CER-03', supplier: 'Oster Import', date: '2026-09-10', qty: 12, unitCost: 110.00 }
    ],
    defaultTasks: [
      { id: 't1', title: 'Esterilização em Autoclave das Tesouras e Lâminas', due: '2026-09-30', priority: 'alta', done: false },
      { id: 't2', title: 'Reposição de Laços e Bandanas Temáticas', due: '2026-10-02', priority: 'media', done: false }
    ],
    defaultDocs: [
      { id: 'd1', title: 'Ficha de Anamnese & Alergias Pet - Luna', client: 'Luna (André)', cat: 'Ficha Clínica', date: '2026-09-28', status: 'Ativa' },
      { id: 'd2', title: 'Carteira de Vacinação & Controle Antipulgas', client: 'Thor (Fernanda)', cat: 'Vacinas', date: '2026-09-25', status: 'Em Dia' }
    ],
    waTemplates: {
      t1Name: 'Pet Pronto para Buscar',
      t1Msg: 'Olá! O banho e tosa do seu pet ({SERVICE}) foi finalizado com muito carinho! Ele(a) já está cheiroso(a) e pronto(a) para voltar para casa! 🐾',
      t2Name: 'Lembrete de Horário',
      t2Msg: 'Olá! Passando para lembrar do horário agendado de banho/tosa para {DATE}! O transporte busca se precisar!',
      t3Name: 'Retorno Periódico (15 dias)',
      t3Msg: 'Olá! Já faz 15 dias do último banho do seu pet! Que tal mantermos a pelagem macia e sem nós? Temos horários livres esta semana!'
    },
    deadlines: [
      { title: 'Vencimento Vacina Polivalente V10 - Luna', days: '3 dias restantes', icon: 'fa-syringe' },
      { title: 'Retorno para Higiene Bucal - Thor', days: '5 dias restantes', icon: 'fa-tooth' }
    ]
  },
  {
    dir: 'barbearia',
    title: 'BarberOS • Gestão de Barbearia, Lotes de Cosméticos & CRM',
    shortName: 'BarberOS',
    badge: 'Barbearia & Grooming',
    icon: 'fa-scissors',
    themeColor: '#78350F',
    accentClass: 'theme-solar-amber',
    serviceType: 'Corte & Estilo',
    defaultClients: [
      { id: 'c1', name: 'Gabriel Queiroz', phone: '(32) 99844-5511', date: '2026-09-30', service: 'Corte Degradê + Barboterapia', value: 90, stage: 'vistoria' },
      { id: 'c2', name: 'Thiago Nogueira', phone: '(32) 99133-2288', date: '2026-10-01', service: 'Corte Clássico na Tesoura', value: 65, stage: 'homologacao' }
    ],
    defaultBatches: [
      { id: 'b1', item: 'Pomada Modeladora Efeito Matte Lote 1', code: 'POM-MAT-01', supplier: 'BarberClub Distribuidora', date: '2026-08-10', qty: 30, unitCost: 22.00 },
      { id: 'b2', item: 'Pomada Modeladora Efeito Matte Lote 2', code: 'POM-MAT-02', supplier: 'BarberClub Distribuidora', date: '2026-09-15', qty: 25, unitCost: 26.50 },
      { id: 'b3', item: 'Óleo para Barba Amêndoas & Cedro 30ml', code: 'OLEO-CED-03', supplier: 'Nobre Beard', date: '2026-09-05', qty: 20, unitCost: 28.00 }
    ],
    defaultTasks: [
      { id: 't1', title: 'Afiação das Navalhas e Lâminas Japonesas', due: '2026-09-30', priority: 'alta', done: false },
      { id: 't2', title: 'Reabastecer Cervejas Artesanais e Café', due: '2026-10-01', priority: 'media', done: false }
    ],
    defaultDocs: [
      { id: 'd1', title: 'Ficha de Preferência de Estilo & Barboterapia', client: 'Gabriel Queiroz', cat: 'Estilo', date: '2026-09-28', status: 'Ativo' }
    ],
    waTemplates: {
      t1Name: 'Lembrete de Horário',
      t1Msg: 'Fala {NAME}! Seu corte ({SERVICE}) está confirmado para {DATE}. Cerveja gelada te esperando!',
      t2Name: 'Retorno 15 Dias (Fade)',
      t2Msg: 'E aí {NAME}! Já faz 15 dias do seu último degradê. Bora dar aquele talento no visual para o fim de semana?'
    },
    deadlines: [
      { title: 'Pedido de Lote Especial de Pomadas com Fornecedor', days: '2 dias restantes', icon: 'fa-box' }
    ]
  },
  {
    dir: 'corretor-imoveis',
    title: 'ImobMax OS • Gestão de Imóveis, Lotes de Captação & CRM',
    shortName: 'ImobMax OS',
    badge: 'Imóveis & Vendas',
    icon: 'fa-house-chimney',
    themeColor: '#0369A1',
    accentClass: 'theme-solar-blue',
    serviceType: 'Intermediação & Locação',
    defaultClients: [
      { id: 'c1', name: 'Henrique Vasconcelos', phone: '(32) 99811-7788', date: '2026-10-01', service: 'Apartamento 3 Quartos Centro', value: 450000, stage: 'vistoria' },
      { id: 'c2', name: 'Juliana e Renato', phone: '(32) 99144-6633', date: '2026-10-03', service: 'Casa em Condomínio Fechado', value: 890000, stage: 'homologacao' }
    ],
    defaultBatches: [
      { id: 'b1', item: 'Lote Fotografia Profissional & Tour 360', code: 'FOTO-360-01', supplier: 'Studio Imob Fotos', date: '2026-08-15', qty: 10, unitCost: 350.00 },
      { id: 'b2', item: 'Lote Impulsionamento Portais Zap/VivaReal', code: 'ADS-ZAP-02', supplier: 'Grupo OLX', date: '2026-09-01', qty: 15, unitCost: 180.00 }
    ],
    defaultTasks: [
      { id: 't1', title: 'Vistoria de Entrega de Chaves - Henrique Vasconcelos', due: '2026-10-01', priority: 'alta', done: false },
      { id: 't2', title: 'Emissão de Certidões de Ônus Reais no RGI', due: '2026-10-04', priority: 'alta', done: false }
    ],
    defaultDocs: [
      { id: 'd1', title: 'Matrícula Atualizada com Negativa de Ônus', client: 'Henrique Vasconcelos', cat: 'RGI', date: '2026-09-28', status: 'Emitido' },
      { id: 'd2', title: 'Proposta Comercial de Compra Vinculante', client: 'Juliana e Renato', cat: 'Proposta', date: '2026-09-26', status: 'Aceita' }
    ],
    waTemplates: {
      t1Name: 'Agendamento de Visita',
      t1Msg: 'Olá {NAME}! Sua visita ao imóvel ({SERVICE}) está agendada para {DATE}. Estarei te esperando na portaria!',
      t2Name: 'Proposta Aprovada',
      t2Msg: 'Excelente notícia {NAME}! O proprietário aceitou sua proposta pelo imóvel! Vamos para a fase documental!'
    },
    deadlines: [
      { title: 'Validade da Opção de Venda com Exclusividade (60 dias)', days: '4 dias restantes', icon: 'fa-handshake' }
    ]
  }
];

function buildCrmHtml(cfg) {
  // Read SunEco template and replace niche specifics
  const baseTemplatePath = path.resolve(__dirname, '../energia-solar/admin/index.html');
  let html = fs.readFileSync(baseTemplatePath, 'utf8');

  // Replace Title & Branding
  html = html.replace(/<title>.*?<\/title>/, `<title>${cfg.title}</title>`);
  html = html.replace(/SunEco OS/g, cfg.shortName);
  html = html.replace(/Solar CRM Pro/g, cfg.badge);
  html = html.replace(/fa-solar-panel/g, cfg.icon);
  html = html.replace(/Gestão Solar, Estoque por Lote & CRM/g, cfg.title);
  html = html.replace(/Engenharia, Estoque por Lote & Clientes/g, `Gestão por Lote, Clientes & Prazos • ${cfg.badge}`);

  // Replace default data arrays in script
  const jsonClients = JSON.stringify(cfg.defaultClients, null, 2);
  const jsonBatches = JSON.stringify(cfg.defaultBatches, null, 2);
  const jsonTasks = JSON.stringify(cfg.defaultTasks, null, 2);
  const jsonDocs = JSON.stringify(cfg.defaultDocs, null, 2);

  html = html.replace(/const DEFAULT_CLIENTS = \[[\s\S]*?\];/, `const DEFAULT_CLIENTS = ${jsonClients};`);
  html = html.replace(/const DEFAULT_BATCHES = \[[\s\S]*?\];/, `const DEFAULT_BATCHES = ${jsonBatches};`);
  html = html.replace(/const DEFAULT_TASKS = \[[\s\S]*?\];/, `const DEFAULT_TASKS = ${jsonTasks};`);
  html = html.replace(/const DEFAULT_DOCS = \[[\s\S]*?\];/, `const DEFAULT_DOCS = ${jsonDocs};`);

  // Replace storage keys so each CRM has its own independent database
  const storagePrefix = cfg.dir.replace(/[^a-zA-Z0-9]/g, '_');
  html = html.replace(/suneco_admin_auth/g, `${storagePrefix}_admin_auth`);
  html = html.replace(/suneco_crm_clients/g, `${storagePrefix}_crm_clients`);
  html = html.replace(/suneco_crm_batches/g, `${storagePrefix}_crm_batches`);
  html = html.replace(/suneco_crm_tasks/g, `${storagePrefix}_crm_tasks`);
  html = html.replace(/suneco_crm_docs/g, `${storagePrefix}_crm_docs`);
  html = html.replace(/suneco_theme_accent/g, `${storagePrefix}_theme_accent`);
  html = html.replace(/suneco_dark_mode/g, `${storagePrefix}_dark_mode`);

  // Inject default theme class if specified
  if (cfg.accentClass) {
    html = html.replace(/<html lang="pt-BR" class="h-full">/, `<html lang="pt-BR" class="h-full ${cfg.accentClass}">`);
  }

  return html;
}

function generateNicheCrms() {
  console.log('🏭 Iniciando Fábrica Universal de CRMs Personalizados por Nicho...');

  for (const cfg of NICHE_CONFIGS) {
    const targetDir = path.join(ROOT_DIR, cfg.dir);
    if (!fs.existsSync(targetDir)) {
      console.log(`[SKIP] Pasta ${cfg.dir} não existe.`);
      continue;
    }

    const adminDir = path.join(targetDir, 'admin');
    if (!fs.existsSync(adminDir)) {
      fs.mkdirSync(adminDir, { recursive: true });
    }

    const crmHtml = buildCrmHtml(cfg);
    const targetFile = path.join(adminDir, 'index.html');
    fs.writeFileSync(targetFile, crmHtml, 'utf8');

    console.log(`✅ CRM Gerado com Sucesso: ${cfg.shortName} -> ${path.relative(ROOT_DIR, targetFile)}`);
  }

  console.log('\n🎉 Todos os CRMs dos nichos foram gerados e instalados com sucesso!');
}

generateNicheCrms();
