/**
 * BUILDER SCRIPT FOR NETFLIX-STYLE SHOWCASE (MASTER INDEX.HTML)
 * Creates a high-end, responsive Netflix-inspired showroom for all niche websites and CRMs.
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const OUTPUT_FILE = path.join(ROOT_DIR, 'index.html');

// 1. Ecosystems with Full CRM & Public Site
const CRM_NICHES = [
  {
    id: 'energia-solar',
    name: 'Energia Solar & Engenharia',
    brand: 'SunEco OS',
    tagline: 'Landing Page de Alta Conversão + CRM Fotovoltaico',
    desc: 'Dimensionamento solar automatizado, calculadora de economia para o cliente e CRM completo com controle de usinas, rastreio de inversores e módulos por lote.',
    dir: 'energia-solar',
    icon: 'fa-solar-panel',
    badgeColor: 'emerald',
    accentColor: '#10B981',
    gradient: 'from-emerald-950 via-slate-900 to-emerald-900',
    matchScore: '99% Relevante',
    ticket: 'R$ 18.900',
    tags: ['Site de Vendas', 'CRM Kanban', 'Estoque Inversores/Placas', 'Lembretes WhatsApp', 'Anti-Spam'],
    previewBg: 'linear-gradient(135deg, #064E3B 0%, #022C22 100%)',
    previewIcon: 'fa-solar-panel',
    publicUrl: 'energia-solar/index.html',
    adminUrl: 'energia-solar/admin/index.html'
  },
  {
    id: 'dentista',
    name: 'Odontologia & Estética Dental',
    brand: 'Lumina Dental OS',
    tagline: 'Consultório Digital + Gestão de Prontuários & Lotes',
    desc: 'Agendamento estético 3D, quebra de objeções para implantes e facetas E-Max, e painel CRM com histórico, faturamento e rastreio de resinas e anestésicos por lote.',
    dir: 'dentista',
    icon: 'fa-tooth',
    badgeColor: 'amber',
    accentColor: '#C58B37',
    gradient: 'from-amber-950 via-slate-900 to-amber-900',
    matchScore: '98% Relevante',
    ticket: 'R$ 16.000',
    tags: ['Avaliação 3D', 'CRM Clínico', 'Controle Resinas por Lote', 'Automação WhatsApp', 'Upload Docs'],
    previewBg: 'linear-gradient(135deg, #78350F 0%, #451A03 100%)',
    previewIcon: 'fa-tooth',
    publicUrl: 'dentista/index.html',
    adminUrl: 'dentista/admin/index.html'
  },
  {
    id: 'advogado',
    name: 'Direito & Alta Complexidade',
    brand: 'LexPro OS',
    tagline: 'Escritório Digital + Controle de Prazos Fatais & Custas',
    desc: 'Captação confidencial de clientes jurídicos, agendamento seguro e painel CRM com alerta vermelho de prazos prescricionais fatais e rateio de custas processuais.',
    dir: 'advogado',
    icon: 'fa-scale-balanced',
    badgeColor: 'blue',
    accentColor: '#3B82F6',
    gradient: 'from-blue-950 via-slate-900 to-indigo-900',
    matchScore: '97% Relevante',
    ticket: 'R$ 12.500',
    tags: ['Consulta Confidencial', 'Alerta Prazos Fatais', 'CRM Jurídico', 'Custas por Lote', 'WhatsApp VIP'],
    previewBg: 'linear-gradient(135deg, #1E3A8A 0%, #0F172A 100%)',
    previewIcon: 'fa-scale-balanced',
    publicUrl: 'advogado/index.html',
    adminUrl: 'advogado/admin/index.html'
  },
  {
    id: 'concessionaria-honda',
    name: 'Concessionária & Automotivo',
    brand: 'AutoDrive OS',
    tagline: 'Showroom de Veículos + CRM de Test-Drive & Peças',
    desc: 'Agendamento interativo de test-drive, catálogo digital de seminovos e novos, e CRM operacional com estoque de peças genuínas com preços variados por lote.',
    dir: 'concessionaria-honda',
    icon: 'fa-car-side',
    badgeColor: 'red',
    accentColor: '#EF4444',
    gradient: 'from-red-950 via-slate-900 to-rose-900',
    matchScore: '96% Relevante',
    ticket: 'R$ 89.000',
    tags: ['Test-Drive Online', 'CRM Automotivo', 'Estoque de Peças', 'Aviso WhatsApp', 'Lead por IP'],
    previewBg: 'linear-gradient(135deg, #7F1D1D 0%, #18181B 100%)',
    previewIcon: 'fa-car-side',
    publicUrl: 'concessionaria-honda/index.html',
    adminUrl: 'concessionaria-honda/admin/index.html'
  },
  {
    id: 'arquiteto',
    name: 'Arquitetura & Design de Interiores',
    brand: 'StudioDesign OS',
    tagline: 'Portfólio 3D + CRM de Cronograma de Obras & Compras',
    desc: 'Briefing interativo de arquitetura residencial e comercial, portfólio visual imersivo e CRM com acompanhamento de etapas de obra e acabamentos por lote.',
    dir: 'arquiteto',
    icon: 'fa-compass-drafting',
    badgeColor: 'orange',
    accentColor: '#F97316',
    gradient: 'from-orange-950 via-slate-900 to-amber-900',
    matchScore: '98% Relevante',
    ticket: 'R$ 22.000',
    tags: ['Briefing Online', 'CRM de Obras', 'Materiais por Lote', 'Contratos & Plantas', 'WhatsApp'],
    previewBg: 'linear-gradient(135deg, #7C2D12 0%, #1C1917 100%)',
    previewIcon: 'fa-compass-drafting',
    publicUrl: 'arquiteto/index.html',
    adminUrl: 'arquiteto/admin/index.html'
  },
  {
    id: 'banho-e-tosa',
    name: 'Pet Shop, Banho & Tosa e Vet',
    brand: 'PetCare OS',
    tagline: 'Agendamento Pet + CRM com Táxi Dog & Vacinas',
    desc: 'Reserva online de banho, tosa e consultas veterinárias, solicitação de leva e traz (táxi pet) e CRM com controle de vacinas e cosméticos por lote.',
    dir: 'banho-e-tosa',
    icon: 'fa-paw',
    badgeColor: 'pink',
    accentColor: '#EC4899',
    gradient: 'from-pink-950 via-slate-900 to-purple-900',
    matchScore: '97% Relevante',
    ticket: 'R$ 140',
    tags: ['Agendamento Táxi Dog', 'CRM Pet Care', 'Vacinas & Insumos', 'Lembrete Banho', 'Anti-Spam'],
    previewBg: 'linear-gradient(135deg, #831843 0%, #1E1B4B 100%)',
    previewIcon: 'fa-paw',
    publicUrl: 'banho-e-tosa/index.html',
    adminUrl: 'banho-e-tosa/admin/index.html'
  },
  {
    id: 'barbearia',
    name: 'Barbearia Premium & Club',
    brand: 'BarberOS',
    tagline: 'Agendamento de Horário + CRM com Comissões & Pomadas',
    desc: 'Seleção do barbeiro favorito, reserva de barba terapia e corte, e CRM de gestão com cálculo de comissões por profissional e estoque de pomadas e lâminas.',
    dir: 'barbearia',
    icon: 'fa-scissors',
    badgeColor: 'amber',
    accentColor: '#F59E0B',
    gradient: 'from-amber-950 via-slate-900 to-yellow-900',
    matchScore: '95% Relevante',
    ticket: 'R$ 95',
    tags: ['Escolha de Barbeiro', 'CRM Barbearia', 'Estoque Pomadas', 'Confirmação 2h Antes', 'Faturamento'],
    previewBg: 'linear-gradient(135deg, #451A03 0%, #18181B 100%)',
    previewIcon: 'fa-scissors',
    publicUrl: 'barbearia/index.html',
    adminUrl: 'barbearia/admin/index.html'
  },
  {
    id: 'corretor-imoveis',
    name: 'Imóveis & Alto Padrão',
    brand: 'ImobMax OS',
    tagline: 'Showroom de Imóveis + CRM de Funil de Vendas & VGV',
    desc: 'Agendamento de visita VIP a mansões e coberturas, quebra de objeções de financiamento e CRM com funil de negociação de contratos e cálculo de comissões.',
    dir: 'corretor-imoveis',
    icon: 'fa-building-columns',
    badgeColor: 'cyan',
    accentColor: '#06B6D4',
    gradient: 'from-cyan-950 via-slate-900 to-sky-900',
    matchScore: '99% Relevante',
    ticket: 'R$ 850.000',
    tags: ['Visita VIP', 'CRM Imobiliário', 'VGV & Comissões', 'Upload Escrituras', 'Alerta Visitas'],
    previewBg: 'linear-gradient(135deg, #164E63 0%, #0F172A 100%)',
    previewIcon: 'fa-building-columns',
    publicUrl: 'corretor-imoveis/index.html',
    adminUrl: 'corretor-imoveis/admin/index.html'
  }
];

// 2. Additional Specialized Landing Pages in Workspace
const LANDING_PAGES = [
  { id: 'contador', name: 'Contabilidade Consultiva', brand: 'Exata Contábil', dir: 'contador', icon: 'fa-calculator', category: 'Financeiro', color: '#10B981' },
  { id: 'nutricionista', name: 'Nutrição & Performance', brand: 'NutriViva', dir: 'nutricionista', icon: 'fa-apple-whole', category: 'Saúde', color: '#84CC16' },
  { id: 'personal-trainer', name: 'Personal Trainer & Fitness', brand: 'ProFit Performance', dir: 'personal-trainer', icon: 'fa-dumbbell', category: 'Saúde', color: '#E11D48' },
  { id: 'fotografo-casamento', name: 'Fotografia de Casamentos', brand: 'Lumière Photo Studio', dir: 'fotografo-casamento', icon: 'fa-camera', category: 'Eventos', color: '#A855F7' },
  { id: 'psicologia', name: 'Psicologia & Psicoterapia', brand: 'Mente Serena', dir: 'psicologia', icon: 'fa-brain', category: 'Saúde', color: '#06B6D4' },
  { id: 'oftalmologista', name: 'Oftalmologia & Cirurgia', brand: 'Visão Prime Clínica', dir: 'oftalmologista', icon: 'fa-eye', category: 'Saúde', color: '#3B82F6' },
  { id: 'quiropraxista', name: 'Quiropraxia & Coluna', brand: 'Coluna Viva', dir: 'quiropraxista', icon: 'fa-bone', category: 'Saúde', color: '#14B8A6' },
  { id: 'podologo', name: 'Podologia Clínica', brand: 'Podologia Especializada', dir: 'podologo', icon: 'fa-shoe-prints', category: 'Saúde', color: '#6366F1' },
  { id: 'acupunturista', name: 'Acupuntura & Medicina Tradicional', brand: 'Equilíbrio Oriental', dir: 'acupunturista', icon: 'fa-spa', category: 'Bem-Estar', color: '#EC4899' },
  { id: 'lavanderia', name: 'Lavanderia Express & Têxtil', brand: 'LavaClean Express', dir: 'lavanderia', icon: 'fa-shirt', category: 'Serviços', color: '#0EA5E9' },
  { id: 'professor-idiomas', name: 'Aulas de Inglês & Idiomas', brand: 'Polyglot Academy', dir: 'professor-idiomas', icon: 'fa-language', category: 'Educação', color: '#F59E0B' },
  { id: 'professor-musica', name: 'Escola & Professor de Música', brand: 'Harmonia Instituto', dir: 'professor-musica', icon: 'fa-music', category: 'Educação', color: '#8B5CF6' },
  { id: 'professor-particular', name: 'Aulas Particulares & Reforço', brand: 'Nota 10 Aulas', dir: 'professor-particular', icon: 'fa-graduation-cap', category: 'Educação', color: '#10B981' },
  { id: 'fumaca-motos', name: 'Concessionária de Motos', brand: 'Fumaça Motos Multimarcas', dir: 'fumaca-motos', icon: 'fa-motorcycle', category: 'Veículos', color: '#DC2626' },
  { id: 'restaurante-egeu', name: 'Gastronomia & Restaurante Egeu', brand: 'Restaurante Egeu Mediterrâneo', dir: 'restaurante-egeu', icon: 'fa-utensils', category: 'Gastronomia', color: '#D97706' },
  { id: 'boteco-portugues', name: 'Boteco Português & Tapas', brand: 'O Tasco Boteco Lusitano', dir: 'boteco-portugues', icon: 'fa-beer-mug-empty', category: 'Gastronomia', color: '#EF4444' }
];

console.log('Building Netflix Showcase with', CRM_NICHES.length, 'flagship ecosystems and', LANDING_PAGES.length, 'landing pages...');
