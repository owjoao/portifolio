const fs = require('fs');
const path = require('path');

console.log('--- Applying Image Upgrades to Energia Solar, Dentista, and Advogado ---');

// ==========================================
// 1. ENERGIA SOLAR
// ==========================================
let solarHtml = fs.readFileSync('energia-solar/index.html', 'utf8');

// Ensure residência & comercial images are updated
solarHtml = solarHtml.replace(/src="https:\/\/images\.unsplash\.com\/photo-1592833159155-c62df1b65634[^"]*"/g, 'src="assets/solar-modern-house.jpg"');
solarHtml = solarHtml.replace(/src="https:\/\/images\.unsplash\.com\/photo-1558449028-b53a39d100fc[^"]*"/g, 'src="assets/solar-inverter-tech.jpg"');

const solarTarget = '  <!-- ========================================================================= -->\r\n  <!-- SECTION: QUEBRA DE OBJEÇÕES (6 MITOS VS FATOS)                           -->';
const solarTargetLF = '  <!-- ========================================================================= -->\n  <!-- SECTION: QUEBRA DE OBJEÇÕES (6 MITOS VS FATOS)                           -->';

const engineeringSection = `  <!-- ========================================================================= -->
  <!-- SECTION: ENGENHARIA & VISTORIA TÉCNICA CERTIFICADA (PROMPT FLOW REAL ASSET) -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#051814] text-white relative overflow-hidden border-b border-emerald-900/40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="bg-gradient-to-r from-[#0A261F] to-[#061713] border border-emerald-500/30 rounded-3xl p-8 lg:p-12 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-green-500/20 border border-green-500/30 text-green-400 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-clipboard-check"></i> Corpo Técnico Próprio & Certificado
          </div>
          <h2 class="font-outfit font-black text-3xl sm:text-4xl text-white tracking-tight">
            Engenharia de Precisão e Vistoria com Tecnologia de Ponta
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Nada de instalações amadoras ou risco estrutural no seu telhado. Cada projeto SunEco é assinado por engenheiros eletricistas credenciados pelo CREA, com cálculo milimétrico de incidência solar, inclinação e telemetria remota.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2">
            <div class="p-4 rounded-2xl bg-black/30 border border-white/10">
              <div class="text-green-400 font-black text-2xl font-outfit">100%</div>
              <div class="text-xs text-slate-300 font-semibold mt-1">Homologação Garantida na Concessionária</div>
            </div>
            <div class="p-4 rounded-2xl bg-yellow-400/10 border border-yellow-500/30">
              <div class="text-yellow-400 font-black text-2xl font-outfit">25 Anos</div>
              <div class="text-xs text-slate-300 font-semibold mt-1">Garantia Linear de Eficiência</div>
            </div>
            <div class="p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/30">
              <div class="text-emerald-400 font-black text-2xl font-outfit">R$ 0</div>
              <div class="text-xs text-slate-300 font-semibold mt-1">Custo para Vistoria Prévia no Local</div>
            </div>
          </div>
          <div class="pt-2">
            <button onclick="openVistoriaModal()" class="inline-flex items-center gap-2.5 bg-gradient-to-r from-green-500 to-emerald-600 hover:from-green-600 hover:to-emerald-700 text-slate-950 font-outfit font-bold text-sm px-7 py-4 rounded-xl shadow-lg shadow-green-900/30 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Solicitar Vistoria Técnica no Meu Imóvel</span>
            </button>
          </div>
        </div>
        <div class="lg:col-span-5 relative">
          <div class="relative rounded-2xl overflow-hidden border border-emerald-500/40 shadow-2xl group">
            <img src="assets/solar-engineer-tablet.jpg" alt="Engenheiro Eletricista SunEco inspecionando usina solar com tablet" class="w-full h-[380px] object-cover transform group-hover:scale-105 transition-transform duration-700" loading="lazy" decoding="async">
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
            <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-emerald-200 text-slate-900 flex items-center justify-between">
              <div>
                <span class="text-[10px] uppercase font-bold text-emerald-700 block">Vistoria e Diagnóstico</span>
                <span class="text-xs font-bold font-outfit">Eng. Lucas Silveira • CREA 219.840-D</span>
              </div>
              <span class="px-2.5 py-1 rounded-md bg-emerald-100 text-emerald-800 text-[10px] font-bold">Certificado</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>\n\n`;

if (!solarHtml.includes('solar-engineer-tablet.jpg')) {
  if (solarHtml.includes(solarTarget)) {
    solarHtml = solarHtml.replace(solarTarget, engineeringSection + solarTarget);
    console.log('Inserted engineering section into energia-solar (CRLF)');
  } else if (solarHtml.includes(solarTargetLF)) {
    solarHtml = solarHtml.replace(solarTargetLF, engineeringSection + solarTargetLF);
    console.log('Inserted engineering section into energia-solar (LF)');
  }
}
fs.writeFileSync('energia-solar/index.html', solarHtml, 'utf8');
console.log('Updated energia-solar/index.html successfully');


// ==========================================
// 2. DENTISTA
// ==========================================
let dentistaHtml = fs.readFileSync('dentista/index.html', 'utf8');

// A. Update "depois.jpg" in Before & After with the ultra-crisp radiant smile
dentistaHtml = dentistaHtml.replace('assets/depois.jpg', 'assets/natural-radiant-smile.jpg');

// B. Add clinic luxury interior & 3D scanner showcase block
// Let's add an interactive section: "Infraestrutura & Tecnologia 3D de Ponta" before #planos or #contato
const clinicTechSection = `
  <!-- ========================================================================= -->
  <!-- INFRAESTRUTURA VIP & TECNOLOGIA 3D (FLOW PHOTOREALISTIC ASSETS)           -->
  <!-- ========================================================================= -->
  <section class="py-20 md:py-28 bg-slate-50 border-t border-dental-borderLight relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold tracking-widest uppercase bg-dental-mintLight text-dental-teal px-4 py-1.5 rounded-full border border-teal-200/60 inline-block mb-3">
          Experiência High-End & Conforto Absoluto
        </span>
        <h2 class="font-serif font-black text-3xl sm:text-5xl text-dental-dark tracking-tight">
          Ambiente Conceito & Escaneamento Digital 3D
        </h2>
        <p class="text-slate-600 text-sm sm:text-base mt-4 leading-relaxed">
          Unimos a mais avançada tecnologia odontológica a uma arquitetura desenhada para seu relaxamento. Diga adeus às moldagens com massa desconfortável e à ansiedade da cadeira odontológica.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Card 1: Clínica Luxo -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-dental-borderLight shadow-sm hover:shadow-xl transition-all duration-500 group">
          <div class="relative rounded-2xl overflow-hidden aspect-[16/10] mb-6">
            <img 
              src="assets/clinic-luxury-interior.jpg" 
              alt="Ambiente Clínico de Luxo com Cadeira em Couro Champagne e Iluminação Natural" 
              class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
              loading="lazy" 
              decoding="async"
            />
            <div class="absolute top-4 left-4 bg-white/95 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-slate-200 text-xs font-bold text-dental-dark shadow-sm">
              <i class="fa-solid fa-gem text-amber-500 mr-1.5"></i> Suíte Clínica VIP
            </div>
          </div>
          <h3 class="font-serif font-bold text-2xl text-dental-dark mb-2">Conforto e Biossegurança Máxima</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed mb-4">
            Cadeiras ergonômicas estofadas em couro italiano, aromaterapia personalizada, fones anti-ruído e iluminação circadiana que reduzem o estresse e proporcionam um tratamento tranquilo.
          </p>
          <div class="flex items-center gap-3 text-xs text-teal-800 font-semibold">
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-check text-emerald-500"></i> Fones Noise-Cancelling</span>
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-check text-emerald-500"></i> Menu de Cafés Especiais</span>
          </div>
        </div>

        <!-- Card 2: Escaneamento 3D Digital -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-dental-borderLight shadow-sm hover:shadow-xl transition-all duration-500 group">
          <div class="relative rounded-2xl overflow-hidden aspect-[16/10] mb-6">
            <img 
              src="assets/dental-scanner-tech.jpg" 
              alt="Cirurgiã-Dentista realizando escaneamento intraoral 3D com câmera digital de alta precisão" 
              class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
              loading="lazy" 
              decoding="async"
            />
            <div class="absolute top-4 left-4 bg-white/95 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-teal-200 text-xs font-bold text-teal-800 shadow-sm">
              <i class="fa-solid fa-camera-viewfinder text-teal-600 mr-1.5"></i> Escâner Intraoral 3D
            </div>
          </div>
          <h3 class="font-serif font-bold text-2xl text-dental-dark mb-2">Previsibilidade Digital Milimétrica</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed mb-4">
            Em menos de 3 minutos, nossa câmera 3D captura toda a sua arcada dentária em altíssima resolução. Você visualiza o resultado final do seu novo sorriso na tela antes mesmo de iniciar o procedimento.
          </p>
          <div class="flex items-center gap-3 text-xs text-teal-800 font-semibold">
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-check text-emerald-500"></i> Zero Massas de Moldagem</span>
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-check text-emerald-500"></i> Simulação 3D em Tempo Real</span>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!dentistaHtml.includes('clinic-luxury-interior.jpg')) {
  const targetDepoimentos = '<section id="depoimentos"';
  dentistaHtml = dentistaHtml.replace(targetDepoimentos, clinicTechSection + '\n  ' + targetDepoimentos);
}
fs.writeFileSync('dentista/index.html', dentistaHtml, 'utf8');
console.log('Updated dentista/index.html successfully');


// ==========================================
// 3. ADVOGADO
// ==========================================
let advogadoHtml = fs.readFileSync('advogado/index.html', 'utf8');

// Replace the placeholder MV initials badge with the real high-res partner portrait!
const mvInitialsSearch = `<div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-law-gold to-amber-800 text-black flex items-center justify-center text-2xl font-serif font-bold shadow-lg">
                MV
              </div>`;

const mvPhotoReplacement = `<div class="w-20 h-20 rounded-2xl overflow-hidden border-2 border-law-gold shadow-lg shrink-0">
                <img src="assets/law-senior-partner.jpg" alt="Dr. Marcos Valente - Sócio Fundador" class="w-full h-full object-cover object-top" />
              </div>`;

if (advogadoHtml.includes('MV') && !advogadoHtml.includes('law-senior-partner.jpg')) {
  advogadoHtml = advogadoHtml.replace(mvInitialsSearch, mvPhotoReplacement);
  console.log('Replaced MV avatar with law-senior-partner.jpg in advogado');
}

// Add the Boardroom & Legal Contract Macro section
const lawFirmShowcase = `
  <!-- ========================================================================= -->
  <!-- INFRAESTRUTURA CORPORATIVA & ALTO PADRÃO DE ATENDIMENTO                   -->
  <!-- ========================================================================= -->
  <section class="py-20 bg-[#070A12] border-y border-law-border/60 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left: Sala de Reuniões Executiva -->
        <div class="lg:col-span-6 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-law-gold/10 border border-law-gold/30 text-law-gold text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-building-columns"></i> Sede Corporativa & Sigilo Absoluto
          </div>
          <h2 class="font-serif font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Ambiente Estruturado para Negociações de Alto Impacto
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Nossa sede foi projetada com acústica isolada e infraestrutura completa para reuniões presenciais e teleconferências seguras com clientes no Brasil e no exterior. Conduzimos mediações patrimoniais em ambiente neutro e elegante, minimizando desgastes e acelerando desfechos favoráveis.
          </p>
          <div class="rounded-2xl overflow-hidden border border-law-border shadow-2xl relative group aspect-[16/10]">
            <img src="assets/law-firm-boardroom.jpg" alt="Sala de Reuniões Executiva Valente e Associados" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" loading="lazy" decoding="async">
            <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs text-law-gold font-bold">
              <i class="fa-solid fa-lock mr-1.5 text-xs"></i> Sala de Negociações Confidenciais
            </div>
          </div>
        </div>

        <!-- Right: Contratos & Rigor Técnico com Foto Macro da Caneta -->
        <div class="lg:col-span-6 space-y-6">
          <div class="rounded-2xl overflow-hidden border border-law-border shadow-2xl relative group aspect-[16/10]">
            <img src="assets/law-contract-pen.jpg" alt="Instrumento Contratual com Selo Notarial e Caneta Tinteiro de Luxo" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" loading="lazy" decoding="async">
            <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs text-white font-bold">
              <i class="fa-solid fa-stamp text-law-gold mr-1.5 text-xs"></i> Due Diligence & Segurança Registral
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-law-card border border-law-gold/30 shadow-xl space-y-3">
            <h3 class="font-serif font-bold text-xl text-white">Minutas Blindadas Contra Nulidades</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Cada cláusula de inventário, testamento ou partilha societária é confeccionada com base na mais recente jurisprudência dos Tribunais Superiores (STJ e STF), assegurando eficácia plena e prevenindo litígios futuros entre sucessores.
            </p>
            <div class="flex items-center gap-4 pt-2 text-xs font-semibold text-law-gold">
              <span><i class="fa-solid fa-check text-emerald-400 mr-1"></i> Compliance Notarial</span>
              <span><i class="fa-solid fa-check text-emerald-400 mr-1"></i> Assinatura Digital ICP-Brasil</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
`;

if (!advogadoHtml.includes('law-firm-boardroom.jpg')) {
  const targetAreas = '<section id="areas"';
  advogadoHtml = advogadoHtml.replace(targetAreas, lawFirmShowcase + '\n  ' + targetAreas);
}
fs.writeFileSync('advogado/index.html', advogadoHtml, 'utf8');
console.log('Updated advogado/index.html successfully');
