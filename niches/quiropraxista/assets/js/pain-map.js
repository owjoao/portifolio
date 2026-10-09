/**
 * QuiroLife - Pain Map & Regional Interaction Architecture
 * Modular: painData, painUI, spineScene, interactions
 * Follows responsible medical communication guidelines (no automatic diagnosis).
 */

const painData = {
  lombar: {
    key: 'lombar',
    region3D: 'lombar',
    title: 'Lombar & Região Ciática',
    tag: 'Região Inferior da Coluna (L1 a L5)',
    desc: 'Desconfortos no final das costas ou sensação de pressão que desce para o quadril podem ter diferentes causas biomecânicas — desde restrições articulares até sobrecarga por longas horas sentadas. A avaliação quiroprática presencial ajuda a entender a origem real das queixas.',
    method: 'Avaliação funcional da bacia + Descompressão manual precisa e liberação miofascial',
    sessions: 'Plano personalizado definido após os testes ortopédicos na 1ª consulta',
    ctaText: 'Entender a Região Lombar na Consulta',
    whatsappMsg: 'Olá QuiroLife! Sinto desconforto na região lombar/ciática e gostaria de agendar uma avaliação clínica.'
  },
  cervical: {
    key: 'cervical',
    region3D: 'cervical',
    title: 'Cervical & Região dos Ombros',
    tag: 'Região Superior da Coluna (C1 a C7)',
    desc: 'Pescoço rígido, peso sobre os ombros e cefaleias tensionais frequentemente estão associados à sobrecarga mecânica decorrente do uso contínuo de telas, má postura ao dormir ou acúmulo de estresse físico. A quiropraxia atua restaurando a amplitude de movimento.',
    method: 'Manobras articulares suaves de precisão + Relaxamento da musculatura suboccipital',
    sessions: 'Estratégia clínica individualizada com foco em mobilidade e ergonomia',
    ctaText: 'Entender a Região Cervical na Consulta',
    whatsappMsg: 'Olá QuiroLife! Tenho dores/tensão na região cervical e ombros e gostaria de agendar uma avaliação.'
  },
  toracica: {
    key: 'toracica',
    region3D: 'toracica',
    title: 'Torácica & Entre as Escápulas',
    tag: 'Região Média da Coluna (T1 a T12)',
    desc: 'Pontadas entre as escápulas, sensação de travamento ao respirar fundo e fadiga postural nas costas costumam indicar restrições de movimento nas vértebras torácicas e articulações costovertebrais causadas por postura mantida.',
    method: 'Ajustes torácicos específicos para abertura articular + Expansão da mobilidade respiratória',
    sessions: 'Orientação de mobilidade diária combinada ao protocolo de ajustes',
    ctaText: 'Entender a Região Torácica na Consulta',
    whatsappMsg: 'Olá QuiroLife! Gostaria de agendar uma avaliação para dor/tensão na região torácica (meio das costas).'
  },
  sacral: {
    key: 'sacral',
    region3D: 'sacral',
    title: 'Região Sacroilíaca & Pélvis',
    tag: 'Base da Coluna (Sacro e Cóccix)',
    desc: 'Desconforto ao se levantar da cama, dor assimétrica na bacia ou incômodo ao caminhar podem estar associados a desequilíbrios do eixo pélvico e restrições na articulação sacroilíaca, que funciona como alicerce de peso da coluna.',
    method: 'Harmonização dos eixos com mesa Drop Table + Testes funcionais de marcha e apoio',
    sessions: 'Cuidado estrutural para estabilização da base e prevenção de compensações',
    ctaText: 'Entender a Região Sacral na Consulta',
    whatsappMsg: 'Olá QuiroLife! Sinto incômodos na região do sacro e quadril e quero agendar uma avaliação.'
  },
  hernia: {
    key: 'hernia',
    region3D: 'lombar',
    title: 'Sobrecarga Discal & Hérnias',
    tag: 'Cuidado Discal & Descompressão',
    desc: 'Desconfortos com queimação ou formigamento podem estar relacionados à compressão de tecidos vizinhos aos discos intervertebrais. Nosso objetivo é avaliar sua condição com segurança, promovendo descompressão e alívio do estresse articular.',
    method: 'Protocolo cuidadoso de flexo-distração, tração axial suave e descompressão sem impacto',
    sessions: 'Acompanhamento progressivo e responsável respeitando os laudos de imagem do paciente',
    ctaText: 'Avaliar Meu Caso Discal',
    whatsappMsg: 'Olá QuiroLife! Possuo laudo de hérnia/protrusão discal e gostaria de agendar uma avaliação responsável.'
  },
  postura: {
    key: 'postura',
    region3D: 'toracica',
    title: 'Postura & Rotina Sedentária',
    tag: 'Ergonomia & Equilíbrio Postural',
    desc: 'Ficar sentado muitas horas na frente do computador impõe sobrecarga contínua às curvaturas naturais da coluna. Identificar desvios e compensações posturais previne o surgimento de dores crônicas e fadiga corporal ao final do dia.',
    method: 'Mapeamento postural completo + Restauração da biomecânica das articulações bloqueadas',
    sessions: 'Plano de reorganização postural e orientação para a sua rotina de trabalho',
    ctaText: 'Agendar Avaliação Postural',
    whatsappMsg: 'Olá QuiroLife! Trabalho muito tempo sentado e sinto a postura pesada. Quero agendar uma avaliação.'
  }
};

const painUI = {
  currentKey: 'lombar',
  phoneWhatsApp: '5532999292311',

  init() {
    this.renderRegionButtons();
    this.select(this.currentKey, false);
    this.setupEventListeners();
  },

  renderRegionButtons() {
    const container = document.getElementById('pain-buttons-list');
    if (!container) return;

    // Buttons already in HTML or dynamically updated
  },

  select(key, update3D = true) {
    const data = painData[key];
    if (!data) return;

    this.currentKey = key;

    // Update Text Elements
    const titleEl = document.getElementById('pain-title');
    const tagEl = document.getElementById('pain-tag');
    const descEl = document.getElementById('pain-desc');
    const methodEl = document.getElementById('pain-method');
    const sessionsEl = document.getElementById('pain-sessions');
    const whatsappBtn = document.getElementById('btn-pain-whatsapp');

    if (titleEl) titleEl.textContent = data.title;
    if (tagEl) tagEl.textContent = data.tag;
    if (descEl) descEl.textContent = data.desc;
    if (methodEl) methodEl.textContent = data.method;
    if (sessionsEl) sessionsEl.textContent = data.sessions;

    if (whatsappBtn) {
      whatsappBtn.href = `https://wa.me/${this.phoneWhatsApp}?text=${encodeURIComponent(data.whatsappMsg)}`;
      const btnText = whatsappBtn.querySelector('.btn-cta-label');
      if (btnText) btnText.textContent = data.ctaText || 'Agendar Avaliação para Esta Região';
    }

    // Update Buttons State
    const allButtons = document.querySelectorAll('[data-pain-key]');
    allButtons.forEach(btn => {
      const btnKey = btn.getAttribute('data-pain-key');
      const isSelected = btnKey === key;
      const indicator = btn.querySelector('.pain-btn-indicator');
      const arrow = btn.querySelector('.pain-btn-arrow');

      if (isSelected) {
        btn.classList.add('bg-quiro-dark', 'border-quiro-cyan', 'shadow-lg', 'shadow-cyan-950/40');
        btn.classList.remove('bg-quiro-dark/50', 'border-quiro-border');
        if (indicator) {
          indicator.classList.add('bg-quiro-cyan', 'scale-125');
          indicator.classList.remove('bg-slate-500');
        }
        if (arrow) {
          arrow.classList.add('text-quiro-cyan', 'translate-x-1');
          arrow.classList.remove('text-slate-500');
        }
      } else {
        btn.classList.remove('bg-quiro-dark', 'border-quiro-cyan', 'shadow-lg', 'shadow-cyan-950/40');
        btn.classList.add('bg-quiro-dark/50', 'border-quiro-border');
        if (indicator) {
          indicator.classList.remove('bg-quiro-cyan', 'scale-125');
          indicator.classList.add('bg-slate-500');
        }
        if (arrow) {
          arrow.classList.remove('text-quiro-cyan', 'translate-x-1');
          arrow.classList.add('text-slate-500');
        }
      }
    });

    // Notify 3D Spine scene if available
    if (update3D && window.heroSpineViewer) {
      window.heroSpineViewer.focusRegion(data.region3D, false);
    }
  },

  setupEventListeners() {
    const buttons = document.querySelectorAll('[data-pain-key]');
    buttons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const key = btn.getAttribute('data-pain-key');
        this.select(key, true);
      });
    });
  }
};

// Global interactions coordinator
const interactions = {
  init() {
    painUI.init();
  }
};

document.addEventListener('DOMContentLoaded', () => {
  interactions.init();
});
