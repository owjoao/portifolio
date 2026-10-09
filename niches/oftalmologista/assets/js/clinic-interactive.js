/**
 * CLINIC INTERACTIVE - Controladores Interativos da Experiência Oftalmológica
 * 
 * - Header inteligente (scroll reveal, blur, height reduction)
 * - Cursor minimalista de alta precisão (desktop only, sem prejudicar usabilidade)
 * - Mapa anatômico interativo do olho humano (hotspots educativos)
 * - Explorador de condições / sintomas visuais com modal/drawer informativo
 * - Tabs e accordions de serviços por especialidade
 * - Simulador educativo de claridade do cristalino (Catarata)
 * - Guia didático de cirurgia refrativa (LASIK vs PRK)
 * - Mini teste "Check-up Rápido da sua Visão" (sem diagnóstico, reflexivo e ético)
 * - FAQ com animação suave de altura
 * - Mobile drawer e bottom navigation
 */

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", () => {
    initHeaderScroll();
    initMobileNav();
    initCustomCursor();
    initEyeAnatomyMap();
    initSymptomsExplorer();
    initServicesTabs();
    initCataractSlider();
    initRefractiveViewer();
    initVisualCheckup();
    initFaqAccordion();
    initGsapAnimations();
  });

  /* =========================================================================
     1. HEADER SCROLL EFFECT
     ========================================================================= */
  function initHeaderScroll() {
    const header = document.getElementById("main-header");
    if (!header) return;

    const handleScroll = () => {
      if (window.scrollY > 40) {
        header.classList.add("bg-[#071521]/95", "backdrop-blur-md", "shadow-lg", "shadow-cyan-950/20", "py-2.5");
        header.classList.remove("bg-transparent", "py-4");
      } else {
        header.classList.remove("bg-[#071521]/95", "backdrop-blur-md", "shadow-lg", "shadow-cyan-950/20", "py-2.5");
        header.classList.add("bg-transparent", "py-4");
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();
  }

  /* =========================================================================
     2. MOBILE NAVIGATION DRAWER
     ========================================================================= */
  function initMobileNav() {
    const toggleBtn = document.getElementById("mobile-menu-toggle");
    const closeBtn = document.getElementById("mobile-menu-close");
    const drawer = document.getElementById("mobile-menu-drawer");
    const backdrop = document.getElementById("mobile-menu-backdrop");
    const menuLinks = document.querySelectorAll(".mobile-nav-link");

    if (!toggleBtn || !drawer) return;

    const openMenu = () => {
      drawer.classList.remove("translate-x-full");
      if (backdrop) backdrop.classList.remove("hidden");
      document.body.classList.add("overflow-hidden");
    };

    const closeMenu = () => {
      drawer.classList.add("translate-x-full");
      if (backdrop) backdrop.classList.add("hidden");
      document.body.classList.remove("overflow-hidden");
    };

    toggleBtn.addEventListener("click", openMenu);
    if (closeBtn) closeBtn.addEventListener("click", closeMenu);
    if (backdrop) backdrop.addEventListener("click", closeMenu);
    menuLinks.forEach(link => link.addEventListener("click", closeMenu));
  }

  /* =========================================================================
     3. CUSTOM MINIMALIST CURSOR (Desktop Only)
     ========================================================================= */
  function initCustomCursor() {
    const isTouch = "ontouchstart" in window || navigator.maxTouchPoints > 0;
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (isTouch || prefersReducedMotion || window.innerWidth < 1024) return;

    const dot = document.createElement("div");
    dot.className = "custom-cursor-dot";
    const ring = document.createElement("div");
    ring.className = "custom-cursor-ring";

    document.body.appendChild(dot);
    document.body.appendChild(ring);

    let mouseX = -100, mouseY = -100;
    let ringX = -100, ringY = -100;

    window.addEventListener("mousemove", (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      dot.style.transform = `translate(${mouseX}px, ${mouseY}px)`;
    }, { passive: true });

    function renderRing() {
      ringX += (mouseX - ringX) * 0.18;
      ringY += (mouseY - ringY) * 0.18;
      ring.style.transform = `translate(${ringX}px, ${ringY}px)`;
      requestAnimationFrame(renderRing);
    }
    requestAnimationFrame(renderRing);

    // Hover states para links e botões interativos
    const interactiveElements = document.querySelectorAll("a, button, input, [role='button'], .cursor-pointer, .interactive-card");
    interactiveElements.forEach(el => {
      el.addEventListener("mouseenter", () => document.body.classList.add("cursor-hover"));
      el.addEventListener("mouseleave", () => document.body.classList.remove("cursor-hover"));
    });

    const threeContainer = document.getElementById("hero-eye-canvas-container");
    if (threeContainer) {
      threeContainer.addEventListener("mouseenter", () => document.body.classList.add("cursor-3d"));
      threeContainer.addEventListener("mouseleave", () => document.body.classList.remove("cursor-3d"));
    }
  }

  /* =========================================================================
     4. MAPA ANATÔMICO INTERATIVO DO OLHO
     ========================================================================= */
  const ANATOMY_DATA = {
    cornea: {
      name: "Córnea",
      role: "Superfície refrativa externa",
      description: "A superfície transparente anterior do olho. É responsável por cerca de dois terços do poder refrativo total, focalizando os feixes de luz que entram no olho. Alterações na sua curvatura ou regularidade estão associadas a miopia, astigmatismo, hipermetropia e ceratocone.",
      relevance: "Área de atuação da cirurgia refrativa a laser (LASIK / PRK) e crosslinking.",
      tag: "Óptica e Superfície"
    },
    cristalino: {
      name: "Cristalino",
      role: "Lente de foco dinâmico natural",
      description: "Lente biconvexa natural localizada atrás da íris. Sua função é ajustar o foco para diferentes distâncias (acomodação visual). Com o tempo, perde a flexibilidade (presbiopia) e pode sofrer opacificação progressiva, condição conhecida como catarata.",
      relevance: "Na cirurgia de catarata, é substituído por uma lente intraocular (LIO) de alta tecnologia.",
      tag: "Foco & Acomodação"
    },
    retina: {
      name: "Retina",
      role: "Camada fotorreceptora neurológica",
      description: "Membrana delgada que reveste o fundo do olho, repleta de fotorreceptores que convertem a luz em sinais elétricos. É irrigada por microvasos sensíveis a condições como diabetes, hipertensão e descolamento de retina.",
      relevance: "Investigada detalhadamente pelo Mapeamento de Retina e Tomografia de Coerência Óptica (OCT).",
      tag: "Sensibilidade & Luz"
    },
    macula: {
      name: "Mácula e Fóvea",
      role: "Centro da visão de alta resolução",
      description: "Pequena área no centro da retina responsável pela visão detalhada e central, necessária para ler, reconhecer rostos e enxergar cores. Pode sofrer degeneração macular relacionada à idade (DMRI) ou edema.",
      relevance: "Avaliada com precisão micrométrica através do OCT de alta resolução.",
      tag: "Visão Central Fina"
    },
    nervo: {
      name: "Nervo Óptico",
      role: "Condutor dos impulsos visuais ao cérebro",
      description: "Cabo formado por mais de um milhão de fibras nervosas que conecta o olho ao córtex visual cerebral. O aumento da pressão intraocular é um dos principais fatores de risco para lesão crônica dessas fibras no glaucoma.",
      relevance: "Aferido rotineiramente pela tonometria de precisão, retinografia e campo visual.",
      tag: "Conexão Neural"
    }
  };

  function initEyeAnatomyMap() {
    const hotspots = document.querySelectorAll("[data-anatomy-target]");
    const titleEl = document.getElementById("anatomy-title");
    const roleEl = document.getElementById("anatomy-role");
    const descEl = document.getElementById("anatomy-desc");
    const relevanceEl = document.getElementById("anatomy-relevance");
    const tagEl = document.getElementById("anatomy-tag");

    if (!hotspots.length || !titleEl) return;

    function selectStructure(key) {
      const data = ANATOMY_DATA[key];
      if (!data) return;

      hotspots.forEach(btn => {
        if (btn.getAttribute("data-anatomy-target") === key) {
          btn.classList.add("bg-cyan-400", "text-black", "ring-4", "ring-cyan-400/30");
          btn.classList.remove("bg-[#0B2230]", "text-white");
        } else {
          btn.classList.remove("bg-cyan-400", "text-black", "ring-4", "ring-cyan-400/30");
          btn.classList.add("bg-[#0B2230]", "text-white");
        }
      });

      titleEl.textContent = data.name;
      roleEl.textContent = data.role;
      descEl.textContent = data.description;
      relevanceEl.textContent = data.relevance;
      if (tagEl) tagEl.textContent = data.tag;
    }

    hotspots.forEach(btn => {
      btn.addEventListener("click", () => {
        const target = btn.getAttribute("data-anatomy-target");
        selectStructure(target);
      });
      btn.addEventListener("mouseenter", () => {
        const target = btn.getAttribute("data-anatomy-target");
        selectStructure(target);
      });
    });

    // Padrão inicial: Córnea
    selectStructure("cornea");
  }

  /* =========================================================================
     5. EXPLORADOR DE SINTOMAS E CONDIÇÕES ("O QUE MUDOU NA SUA VISÃO?")
     ========================================================================= */
  const CONDITIONS_DATA = {
    miopia: {
      name: "Miopia",
      category: "Erro Refrativo",
      whatIs: "Condição óptica em que os raios de luz focam antes da retina, geralmente porque o globo ocular é mais longo que o normal ou a curvatura da córnea é excessiva.",
      perception: "Dificuldade para enxergar objetos e placas de longe com clareza, enquanto a visão para perto costuma permanecer nítida. Pode causar cansaço visual e franzir frequente dos olhos.",
      evaluation: "Exame de refração computadorizada em lâmpada de fenda, topografia corneana e ceratometria.",
      whatsappContext: "refrativa"
    },
    astigmatismo: {
      name: "Astigmatismo",
      category: "Erro Refrativo",
      whatIs: "Imperfeição na curvatura da córnea ou do cristalino, que adquire um formato ovalado semelhante a uma bola de futebol americano, gerando múltiplos pontos focais.",
      perception: "Visão distorcida ou com sombras tanto para longe quanto para perto. Linhas retas podem parecer onduladas e luzes à noite costumam apresentar raios espalhados.",
      evaluation: "Refração estática e dinâmica, aberrometria com mapa de frentes de onda e topografia de córnea.",
      whatsappContext: "refrativa"
    },
    hipermetropia: {
      name: "Hipermetropia",
      category: "Erro Refrativo",
      whatIs: "Ocorre quando o olho é mais curto que o padrão ou o poder refrativo da córnea é insuficiente, fazendo com que a imagem se forme teoricamente atrás da retina.",
      perception: "Esforço constante e fadiga ocular ao ler, trabalhar em computadores ou focar objetos próximos. Pode provocar dores de cabeça frontais ao final do dia.",
      evaluation: "Refração com cicloplegia (colírio dilatador para relaxar a acomodação) e biometria óptica.",
      whatsappContext: "refrativa"
    },
    catarata: {
      name: "Catarata",
      category: "Opacificação do Cristalino",
      whatIs: "Processo natural em que o cristalino perde sua transparência gradual, tornando-se amarelado ou turvo com a idade ou fatores metabólicos.",
      perception: "Sensação persistente de estar olhando através de um vidro embaçado, nevoeiro constante, cores menos vivas, maior sensibilidade ao brilho de faróis e perda de contraste.",
      evaluation: "Biomicroscopia detalhada em lâmpada de fenda, biometria óptica IOLMaster e mapeamento de retina.",
      whatsappContext: "catarata"
    },
    olhoseco: {
      name: "Síndrome do Olho Seco",
      category: "Superfície Ocular",
      whatIs: "Disfunção na quantidade ou na qualidade do filme lacrimal, frequentemente associada à disfunção das glândulas de Meibomius ou ao uso prolongado de telas.",
      perception: "Ardência, sensação de areia ou corpo estranho nos olhos, vermelhidão recorrente, fotofobia e oscilação transitória na nitidez da visão.",
      evaluation: "Teste de tempo de ruptura lacrimal (BUT), coloração com fluoresceína e meibografia digital.",
      whatsappContext: "olhoseco"
    },
    ceratocone: {
      name: "Ceratocone",
      category: "Ectasia Corneana",
      whatIs: "Doença não inflamatória e progressiva em que a córnea sofre afinamento central ou paracentral, assumindo formato cônico.",
      perception: "Piora progressiva do astigmatismo, troca frequente de grau dos óculos sem melhora satisfatória, halos noturnos e hábito crônico de coçar os olhos.",
      evaluation: "Topografia computadorizada de córnea, paquimetria ultrassônica e tomografia Pentacam.",
      whatsappContext: "ceratocone"
    },
    retina: {
      name: "Alterações da Retina e Mácula",
      category: "Doenças Retinianas",
      whatIs: "Comprometimentos na camada neural posterior do olho, como descolamento de vítreo, retinopatia diabética, oclusões vasculares ou DMRI.",
      perception: "Aparecimento súbito de manchas escuras móveis ('moscas volantes'), flashes de luz no campo periférico ou mancha fixa escura no centro do campo visual.",
      evaluation: "Mapeamento minucioso de fundo de olho com dilatação e Tomografia de Coerência Óptica (OCT).",
      whatsappContext: "retina"
    }
  };

  function initSymptomsExplorer() {
    const modal = document.getElementById("condition-modal");
    const closeBtn = document.getElementById("condition-modal-close");
    const backdrop = document.getElementById("condition-modal-backdrop");
    const cards = document.querySelectorAll("[data-condition-key]");

    if (!modal) return;

    const titleEl = document.getElementById("modal-cond-title");
    const categoryEl = document.getElementById("modal-cond-category");
    const whatEl = document.getElementById("modal-cond-what");
    const perceptionEl = document.getElementById("modal-cond-perception");
    const evalEl = document.getElementById("modal-cond-eval");
    const ctaBtn = document.getElementById("modal-cond-cta");

    function openModal(key) {
      const data = CONDITIONS_DATA[key];
      if (!data) return;

      if (titleEl) titleEl.textContent = data.name;
      if (categoryEl) categoryEl.textContent = data.category;
      if (whatEl) whatEl.textContent = data.whatIs;
      if (perceptionEl) perceptionEl.textContent = data.perception;
      if (evalEl) evalEl.textContent = data.evaluation;
      if (ctaBtn && window.CLINIC_CONFIG) {
        ctaBtn.href = window.CLINIC_CONFIG.getWhatsAppUrl(data.whatsappContext);
      }

      modal.classList.remove("hidden");
      document.body.classList.add("overflow-hidden");
    }

    function closeModal() {
      modal.classList.add("hidden");
      document.body.classList.remove("overflow-hidden");
    }

    cards.forEach(card => {
      card.addEventListener("click", () => {
        const key = card.getAttribute("data-condition-key");
        openModal(key);
      });
    });

    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    if (backdrop) backdrop.addEventListener("click", closeModal);
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !modal.classList.contains("hidden")) {
        closeModal();
      }
    });
  }

  /* =========================================================================
     6. SERVIÇOS & ESPECIALIDADES (TABS)
     ========================================================================= */
  function initServicesTabs() {
    const tabBtns = document.querySelectorAll("[data-service-tab]");
    const panels = document.querySelectorAll("[data-service-panel]");

    if (!tabBtns.length || !panels.length) return;

    tabBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const targetGroup = btn.getAttribute("data-service-tab");

        tabBtns.forEach(b => {
          b.classList.remove("bg-gradient-to-r", "from-[#1C8F9C]", "to-[#35C7D8]", "text-[#071521]", "font-bold", "shadow-lg");
          b.classList.add("bg-[#0B2230]/60", "text-slate-300", "border-white/10");
        });

        btn.classList.add("bg-gradient-to-r", "from-[#1C8F9C]", "to-[#35C7D8]", "text-[#071521]", "font-bold", "shadow-lg");
        btn.classList.remove("bg-[#0B2230]/60", "text-slate-300", "border-white/10");

        panels.forEach(panel => {
          if (panel.getAttribute("data-service-panel") === targetGroup) {
            panel.classList.remove("hidden");
            panel.classList.add("animate-fadeIn");
          } else {
            panel.classList.add("hidden");
            panel.classList.remove("animate-fadeIn");
          }
        });
      });
    });
  }

  /* =========================================================================
     7. SIMULADOR DE CLARIDADE DA CATARATA
     ========================================================================= */
  function initCataractSlider() {
    const slider = document.getElementById("cataract-range-input");
    const overlay = document.getElementById("cataract-clarity-overlay");
    const labelEl = document.getElementById("cataract-clarity-label");

    if (!slider || !overlay) return;

    slider.addEventListener("input", (e) => {
      const val = parseInt(e.target.value, 10); // 0 (sem catarata/pós LIO) até 100 (catarata densa)
      // Ajusta opacidade do blur/nevoeiro
      const blurAmount = (val / 100) * 8;
      const opacity = (val / 100) * 0.85;
      overlay.style.backdropFilter = `blur(${blurAmount}px)`;
      overlay.style.webkitBackdropFilter = `blur(${blurAmount}px)`;
      overlay.style.backgroundColor = `rgba(180, 160, 120, ${opacity * 0.35})`;

      if (labelEl) {
        if (val < 25) {
          labelEl.textContent = "Visão Clara & Cristalina (Pós Implante de Lente Intraocular)";
          labelEl.className = "text-xs font-bold text-emerald-400";
        } else if (val < 70) {
          labelEl.textContent = "Opacificação Moderada (Perda de Contraste e Luz Amarelada)";
          labelEl.className = "text-xs font-bold text-amber-300";
        } else {
          labelEl.textContent = "Catarata Densa (Visão Embaçada Semelhante a Vidro Fosco)";
          labelEl.className = "text-xs font-bold text-rose-400";
        }
      }
    });
  }

  /* =========================================================================
     8. VISUALIZADOR REFRATIVA (LASIK vs PRK)
     ========================================================================= */
  function initRefractiveViewer() {
    const btnLasik = document.getElementById("btn-method-lasik");
    const btnPrk = document.getElementById("btn-method-prk");
    const panelLasik = document.getElementById("panel-method-lasik");
    const panelPrk = document.getElementById("panel-method-prk");

    if (!btnLasik || !btnPrk || !panelLasik || !panelPrk) return;

    btnLasik.addEventListener("click", () => {
      btnLasik.classList.add("bg-[#35C7D8]", "text-[#071521]", "font-bold");
      btnLasik.classList.remove("text-slate-300", "bg-transparent");
      btnPrk.classList.remove("bg-[#35C7D8]", "text-[#071521]", "font-bold");
      btnPrk.classList.add("text-slate-300", "bg-transparent");

      panelLasik.classList.remove("hidden");
      panelPrk.classList.add("hidden");
    });

    btnPrk.addEventListener("click", () => {
      btnPrk.classList.add("bg-[#35C7D8]", "text-[#071521]", "font-bold");
      btnPrk.classList.remove("text-slate-300", "bg-transparent");
      btnLasik.classList.remove("bg-[#35C7D8]", "text-[#071521]", "font-bold");
      btnLasik.classList.add("text-slate-300", "bg-transparent");

      panelPrk.classList.remove("hidden");
      panelLasik.classList.add("hidden");
    });
  }

  /* =========================================================================
     9. MINI TESTE "CHECK-UP RÁPIDO DA SUA VISÃO" (Reflexivo, Sem Diagnóstico)
     ========================================================================= */
  const answers = { q1: null, q2: null, q3: null };

  window.answerCheckup = function (qIndex, isYes) {
    answers[`q${qIndex}`] = isYes;

    const btnYes = document.getElementById(`checkup-q${qIndex}-yes`);
    const btnNo = document.getElementById(`checkup-q${qIndex}-no`);

    if (btnYes && btnNo) {
      if (isYes) {
        btnYes.className = "flex-1 py-2.5 px-4 rounded-xl bg-[#35C7D8] text-[#071521] font-bold text-xs shadow-md transition";
        btnNo.className = "flex-1 py-2.5 px-4 rounded-xl border border-white/10 text-slate-400 font-medium text-xs hover:border-white/30 transition";
      } else {
        btnNo.className = "flex-1 py-2.5 px-4 rounded-xl bg-slate-700 text-white font-bold text-xs shadow-md transition";
        btnYes.className = "flex-1 py-2.5 px-4 rounded-xl border border-white/10 text-slate-400 font-medium text-xs hover:border-white/30 transition";
      }
    }

    // Se todas as 3 perguntas foram respondidas, exibir resultado reflexivo
    if (answers.q1 !== null && answers.q2 !== null && answers.q3 !== null) {
      const resultBox = document.getElementById("checkup-result-box");
      const summaryText = document.getElementById("checkup-summary-text");
      const resultCta = document.getElementById("checkup-result-cta");

      if (resultBox) {
        resultBox.classList.remove("hidden");
        resultBox.scrollIntoView({ behavior: "smooth", block: "nearest" });

        const positiveCount = (answers.q1 ? 1 : 0) + (answers.q2 ? 1 : 0) + (answers.q3 ? 1 : 0);
        let feedback = "";
        let context = "checkup";

        if (positiveCount >= 2) {
          feedback = "Suas respostas apontam que você tem notado oscilações na nitidez visual ou desconforto durante o dia a dia. Uma avaliação presencial com exames de refração e lâmpada de fenda é o caminho mais seguro para investigar sua visão.";
          context = "checkup";
        } else if (positiveCount === 1) {
          feedback = "Você apontou algum ponto pontual de desconforto ou hábito visual. Mesmo quando os sintomas parecem sutis, a medicina oftalmológica preventiva ajuda a preservar a saúde dos seus olhos.";
          context = "checkup";
        } else {
          feedback = "Excelente percepção visual! Lembre-se de que a aferição anual da pressão ocular (tonometria) e o fundo de olho são essenciais para manter sua saúde ocular sempre protegida.";
          context = "checkup";
        }

        if (summaryText) summaryText.textContent = feedback;
        if (resultCta && window.CLINIC_CONFIG) {
          resultCta.href = window.CLINIC_CONFIG.getWhatsAppUrl(context, `Olá! Fiz o Check-up Rápido no site e gostaria de agendar uma avaliação oftalmológica.`);
        }
      }
    }
  };

  function initVisualCheckup() {
    // Reset inicial garantido
    answers.q1 = null;
    answers.q2 = null;
    answers.q3 = null;
  }

  /* =========================================================================
     10. FAQ ACCORDION INTERATIVO
     ========================================================================= */
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll(".faq-item");
    if (!faqItems.length) return;

    faqItems.forEach(item => {
      const trigger = item.querySelector(".faq-trigger");
      const content = item.querySelector(".accordion-content");
      const icon = item.querySelector(".faq-icon");

      if (!trigger || !content) return;

      trigger.addEventListener("click", () => {
        const isOpen = content.classList.contains("open");

        // Fechar outros itens abertos
        faqItems.forEach(other => {
          const otherContent = other.querySelector(".accordion-content");
          const otherIcon = other.querySelector(".faq-icon");
          if (otherContent && otherContent !== content) {
            otherContent.classList.remove("open");
            if (otherIcon) otherIcon.style.transform = "rotate(0deg)";
          }
        });

        if (isOpen) {
          content.classList.remove("open");
          if (icon) icon.style.transform = "rotate(0deg)";
          trigger.setAttribute("aria-expanded", "false");
        } else {
          content.classList.add("open");
          if (icon) icon.style.transform = "rotate(180deg)";
          trigger.setAttribute("aria-expanded", "true");
        }
      });
    });
  }

  /* =========================================================================
     11. ANIMAÇÕES GSAP SCROLLTRIGGER (Progressive Enhancement Seguro)
     ========================================================================= */
  function initGsapAnimations() {
    if (typeof gsap === "undefined" || typeof ScrollTrigger === "undefined") return;

    gsap.registerPlugin(ScrollTrigger);

    // Timeline da Avaliação (4 Etapas) - Movimento suave sem ocultar permanentemente
    const timelineCards = document.querySelectorAll(".evaluation-step-card");
    if (timelineCards.length) {
      timelineCards.forEach(card => {
        gsap.fromTo(card, 
          { y: 24 }, 
          {
            y: 0,
            duration: 0.7,
            ease: "power2.out",
            scrollTrigger: {
              trigger: card,
              start: "top 90%",
              toggleActions: "play none none none"
            }
          }
        );
      });
    }

    // Revelações suaves de títulos de seção
    const sectionHeadings = document.querySelectorAll(".reveal-heading");
    sectionHeadings.forEach(heading => {
      gsap.fromTo(heading,
        { y: 15 },
        {
          y: 0,
          duration: 0.6,
          ease: "power2.out",
          scrollTrigger: {
            trigger: heading,
            start: "top 90%",
            toggleActions: "play none none none"
          }
        }
      );
    });
  }

})();
