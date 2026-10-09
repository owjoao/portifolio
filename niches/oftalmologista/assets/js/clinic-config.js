/**
 * CLINIC_CONFIG - Arquitetura Central de Configuração da Clínica Oftalmológica
 * 
 * Permite adaptar 100% da landing page para qualquer clínica/instituto oftalmológico
 * sem necessidade de reescrever o código HTML.
 * Dados não verificados estão claramente marcados para confirmação pelo cliente.
 */

const CLINIC_CONFIG = {
  // Identidade Institucional
  name: "Instituto de Oftalmologia Especializada",
  shortName: "Instituto de Olhos",
  unitName: "Unidade Central",
  tagline: "Tecnologia diagnóstica para enxergar com máxima nitidez e segurança.",
  
  // Informações de Contato
  phone: "(32) 99929-2311",
  phoneFormatted: "+55 (32) 99929-2311",
  whatsappNumber: "5532999292311",
  email: "contato@institutodeolhos.med.br",
  
  // Localização & Endereço (Editável / Placeholder seguro)
  location: {
    title: "Unidade de Diagnóstico e Centro Cirúrgico",
    address: "Av. Paulista, 1000 - Bela Vista / Jardins",
    addressNote: "[CONFIRMAR ENDEREÇO COM O CLIENTE]",
    city: "São Paulo",
    state: "SP",
    cep: "01310-100",
    metroReference: "A 250m da Estação Trianon-Masp (Linha 2 - Verde)",
    parking: "Estacionamento conveniado no local com manobrista",
    accessibility: "Acessibilidade plena: rampas e elevadores para mobilidade reduzida",
    hoursWeekday: "Segunda a Sexta: 08h às 19h",
    hoursSaturday: "Sábados: 08h às 13h",
    mapsEmbedUrl: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.098485293405!2d-46.6549887237894!3d-23.564903378796857!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce59c8da0aa315%3A0xd59f9431f2c9776a!2sAv.%20Paulista%2C%20S%C3%A3o%20Paulo%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr",
    mapsDirectionsUrl: "https://maps.google.com/?q=Av.+Paulista,+1000+-+Bela+Vista,+S%C3%A3o+Paulo+-+SP"
  },

  // Corpo Clínico (Responsável Técnico & Especialistas)
  // IMPORTANTE: Não inventar CRM/RQE. Se não confirmado, sinalizar transparentemente.
  doctor: {
    title: "Direção Técnica & Oftalmologia Especializada",
    name: "Corpo Clínico Especializado",
    crm: "CRM [CONFIRMAR COM O CLIENTE]",
    rqe: "RQE [CONFIRMAR COM O CLIENTE]",
    specializations: [
      "Cirurgia Refrativa a Laser (LASIK / PRK)",
      "Cirurgia de Catarata & Lentes Intraoculares",
      "Diagnóstico Avançado de Córnea e Retina"
    ],
    confirmed: false
  },

  // Indicadores de Prática Clínica e Estrutura
  // Se verified for false, o componente exibe atributos qualitativos seguros e certificados.
  stats: [
    {
      value: "100%",
      label: "Exames com Tecnologia Digital",
      highlight: "Precisão óptica computadorizada",
      verified: true
    },
    {
      value: "4 Etapas",
      label: "Protocolo de Avaliação Individual",
      highlight: "Conversa, exames, laudo e conduta",
      verified: true
    },
    {
      value: "Padrão Ouro",
      label: "Biometria e Tomografia Ocular",
      highlight: "Equipamentos calibrados e certificados",
      verified: true
    },
    {
      value: "Ambiente",
      label: "Centro Cirúrgico e Salas Climatizadas",
      highlight: "Controle estrito de assepsia",
      verified: true
    }
  ],

  // Política de Preços & Condições
  pricingPolicy: {
    showExactPrices: false, // Alterar para true se o cliente autorizar divulgação de tabela
    consultationNote: "Consulte as condições da consulta e a cobertura pelo seu plano de saúde.",
    surgeryNote: "A indicação cirúrgica e os valores dependem de exames pré-operatórios individualizados.",
    insuranceAccepted: true,
    insuranceNotice: "Atendimento particular e cobertura de exames por diversos convênios médicos."
  },

  // Mensagens Contextuais de WhatsApp
  whatsappMessages: {
    geral: "Olá! Gostaria de agendar uma avaliação oftalmológica.",
    refrativa: "Olá! Gostaria de informações sobre a avaliação pré-operatória para Cirurgia Refrativa a Laser (LASIK / PRK).",
    catarata: "Olá! Gostaria de informações sobre a avaliação especializada para Cirurgia de Catarata e Lentes Intraoculares.",
    checkup: "Olá! Gostaria de agendar um Check-up Ocular completo (refração, pressão ocular e fundo de olho).",
    retina: "Olá! Gostaria de agendar uma avaliação de retina e exames diagnósticos (OCT / Mapeamento).",
    olhoseco: "Olá! Gostaria de agendar uma consulta para avaliação e tratamento de Olho Seco.",
    ceratocone: "Olá! Gostaria de agendar uma avaliação especializada para Córnea e Ceratocone.",
    localizacao: "Olá! Gostaria de receber orientações sobre como chegar à clínica e agendar uma consulta."
  },

  // Gerador de links seguros para o WhatsApp
  getWhatsAppUrl(context = "geral", customText = null) {
    const text = customText || this.whatsappMessages[context] || this.whatsappMessages.geral;
    return `https://wa.me/${this.whatsappNumber}?text=${encodeURIComponent(text)}`;
  }
};

// Auto-inicialização para vincular links e campos dinâmicos
document.addEventListener("DOMContentLoaded", () => {
  // Atualiza todos os links com data-whatsapp-context
  const whatsappButtons = document.querySelectorAll("[data-whatsapp-context]");
  whatsappButtons.forEach(btn => {
    const context = btn.getAttribute("data-whatsapp-context");
    btn.setAttribute("href", CLINIC_CONFIG.getWhatsAppUrl(context));
    btn.setAttribute("target", "_blank");
    btn.setAttribute("rel", "noopener noreferrer");
  });

  // Atualiza links com data-maps-direction
  const mapsButtons = document.querySelectorAll("[data-maps-direction]");
  mapsButtons.forEach(btn => {
    btn.setAttribute("href", CLINIC_CONFIG.location.mapsDirectionsUrl);
    btn.setAttribute("target", "_blank");
    btn.setAttribute("rel", "noopener noreferrer");
  });

  // Atualiza elementos de texto marcados com data-clinic-var
  const clinicVars = document.querySelectorAll("[data-clinic-var]");
  clinicVars.forEach(el => {
    const path = el.getAttribute("data-clinic-var").split(".");
    let val = CLINIC_CONFIG;
    for (const key of path) {
      if (val && val[key] !== undefined) {
        val = val[key];
      } else {
        val = null;
        break;
      }
    }
    if (val !== null && typeof val === "string") {
      el.textContent = val;
    }
  });
});
