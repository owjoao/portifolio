const fs = require('fs');
const path = require('path');

console.log('=== Integrating Batch 4 Flow Images into Sites ===');

// ==========================================
// 1. ARQUITETO (ARQUITETURA & DESIGN)
// ==========================================
let archHtml = fs.readFileSync('arquiteto/index.html', 'utf8');

const archStudioShowcase = `
  <!-- ========================================================================= -->
  <!-- ESTÚDIO AUTORAL & MAQUETES 3D (FLOW PHOTOREALISTIC ASSET)                  -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#080B10] border-b border-arch-border/60 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-arch-card border border-arch-gold/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-arch-border shadow-2xl group">
          <img 
            src="assets/architect-studio.jpg" 
            alt="Arquiteta desenvolvendo projeto executivo em prancheta de carvalho com maquete 3D física" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-arch-gold shadow-sm">
            <i class="fa-solid fa-compass-drafting mr-1.5"></i> Estúdio de Criação & Prototipagem
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-arch-gold/40 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-slate-500 block">Metodologia BIM + Maquete Volumétrica</span>
              <span class="font-serif font-black text-slate-900 text-sm">Visualização Espacial Antes da Obra</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-arch-gold text-black font-serif font-black text-xs">Zero Erros</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-arch-gold/10 border border-arch-gold/30 text-arch-gold text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-ruler-combined"></i> Compatibilização Milimétrica
          </div>
          <h2 class="font-serif font-black text-3xl sm:text-4xl text-white tracking-tight">
            Projetos Autorais Desenhados para Sua Vida e Orçamento
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Nada de plantas genéricas de gaveta. Desenvolvemos estudos de iluminação natural, ventilação cruzada e maquetes 3D que eliminam até 25% do desperdício de materiais na construção civil.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-[#090C12] border border-white/10">
              <div class="text-arch-gold font-serif font-black text-2xl counter-up" data-target="+180">+180</div>
              <div class="text-[11px] text-slate-400 mt-0.5">Obras Entregues</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-[#090C12] border border-white/10">
              <div class="text-emerald-400 font-serif font-black text-2xl counter-up" data-target="100%">100%</div>
              <div class="text-[11px] text-slate-400 mt-0.5">Aprovação Prefeitura</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-[#090C12] border border-white/10">
              <div class="text-white font-serif font-black text-2xl">R$ 0</div>
              <div class="text-[11px] text-slate-400 mt-0.5">Consulta Inicial</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Beatriz!%20Gostaria%20de%20conversar%20sobre%20meu%20projeto%20arquitet%C3%B4nico." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-arch-gold to-amber-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-amber-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Briefing de Arquitetura</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!archHtml.includes('architect-studio.jpg')) {
  const targetCalc = '<section id="calculadora"';
  archHtml = archHtml.replace(targetCalc, archStudioShowcase + '\n  ' + targetCalc);
  fs.writeFileSync('arquiteto/index.html', archHtml, 'utf8');
  console.log('✅ Arquiteto updated with architect-studio.jpg');
}


// ==========================================
// 2. BARBEARIA (VALHALLA BARBER CLUB)
// ==========================================
let barberHtml = fs.readFileSync('barbearia/index.html', 'utf8');

const barberShowcase = `
  <!-- ========================================================================= -->
  <!-- AMBIENTE VINTAGE & EXPERIÊNCIA DO CORTE (FLOW PHOTOREALISTIC ASSETS)      -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#0E0B09] border-b border-barber-border/60 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <span class="text-xs font-bold uppercase tracking-widest text-barber-gold bg-barber-gold/10 px-3.5 py-1.5 rounded-full border border-barber-gold/30">
          Experiência Gentleman
        </span>
        <h2 class="font-serif font-black text-3xl sm:text-4xl text-white mt-4">
          Navalha Afiada, Toalha Quente & Café Moído na Hora
        </h2>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Card 1: Cadeira Belmont & Espelho Iluminado -->
        <div class="card-lift bg-barber-card border border-barber-gold/30 rounded-3xl p-6 sm:p-8 space-y-4">
          <div class="relative rounded-2xl overflow-hidden aspect-[16/10] border border-barber-border shadow-2xl group">
            <img 
              src="assets/barber-chair-luxury.jpg" 
              alt="Cadeira hidráulica Belmont em couro conhaque com bancada em nogueira e espelho circular halo" 
              class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
              loading="lazy" 
              decoding="async"
            />
            <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-barber-gold">
              <i class="fa-solid fa-chair mr-1.5"></i> Cadeira Belmont Vintage
            </div>
          </div>
          <h3 class="font-serif font-bold text-2xl text-white">Conforto Ergonômico Máximo</h3>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Reclinação suave com massagem lombar para o momento da toalha quente e barba tradicional com espuma morna batida na hora.
          </p>
        </div>

        <!-- Card 2: Barbeiro com Navalhete & Fumaça de Toalha -->
        <div class="card-lift bg-barber-card border border-barber-gold/30 rounded-3xl p-6 sm:p-8 space-y-4">
          <div class="relative rounded-2xl overflow-hidden aspect-[16/10] border border-barber-border shadow-2xl group">
            <img 
              src="assets/barber-craftsman.jpg" 
              alt="Mestre barbeiro alinhando barba com navalhete clássico e toalha quente fumegante" 
              class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
              loading="lazy" 
              decoding="async"
            />
            <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-emerald-400">
              <i class="fa-solid fa-scissors mr-1.5"></i> Alinhamento Milimétrico
            </div>
          </div>
          <h3 class="font-serif font-bold text-2xl text-white">Visagismo & Precisão de Lâmina</h3>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Análise das linhas da mandíbula e do formato do rosto para criar a proporção ideal para sua barba e cabelo, sem falhas e sem irritação.
          </p>
        </div>
      </div>

    </div>
  </section>
`;

if (!barberHtml.includes('barber-chair-luxury.jpg')) {
  const targetSeletor = '<section id="seletor"';
  barberHtml = barberHtml.replace(targetSeletor, barberShowcase + '\n  ' + targetSeletor);
  fs.writeFileSync('barbearia/index.html', barberHtml, 'utf8');
  console.log('✅ Barbearia updated with barber-chair-luxury.jpg and barber-craftsman.jpg');
}


// ==========================================
// 3. CONCESSIONÁRIA HONDA (SHOWROOM & OFICINA)
// ==========================================
let hondaHtml = fs.readFileSync('concessionaria-honda/index.html', 'utf8');

const showroomServiceSection = `
  <!-- ========================================================================= -->
  <!-- SHOWROOM MODERNO & OFICINA MASTER HONDA (FLOW PHOTOREALISTIC ASSETS)      -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#080B10] border-b border-red-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <span class="text-xs font-bold uppercase tracking-widest text-red-500 bg-red-600/10 px-3.5 py-1.5 rounded-full border border-red-600/30">
          Infraestrutura Oficial Honda
        </span>
        <h2 class="font-sans font-black text-3xl sm:text-4xl text-white mt-4">
          Concessionária Conceito & Box Técnico Certificado
        </h2>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Card 1: Showroom Iluminado -->
        <div class="card-lift bg-[#0D111A] border border-red-600/30 rounded-3xl p-6 sm:p-8 space-y-4">
          <div class="relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
            <img 
              src="assets/showroom-hero.jpg" 
              alt="Showroom de motocicletas Honda com piso de microcimento polido e iluminação halo no teto" 
              class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
              loading="lazy" 
              decoding="async"
            />
            <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-red-400">
              <i class="fa-solid fa-store mr-1.5"></i> Showroom Climatizado
            </div>
          </div>
          <h3 class="font-sans font-black text-2xl text-white">Linha Completa 0km Pronta Entrega</h3>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Modelos Street, Trail, Scooter e Big Trail disponíveis para você montar, testar o conforto e sair pilotando no mesmo dia.
          </p>
        </div>

        <!-- Card 2: Oficina Master Service com Scanner -->
        <div class="card-lift bg-[#0D111A] border border-red-600/30 rounded-3xl p-6 sm:p-8 space-y-4">
          <div class="relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
            <img 
              src="assets/workshop-service.jpg" 
              alt="Mecânico mestre certificado Honda utilizando scanner digital em motocicleta touring no elevador hidráulico" 
              class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
              loading="lazy" 
              decoding="async"
            />
            <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-emerald-400">
              <i class="fa-solid fa-wrench mr-1.5"></i> Honda Master Service
            </div>
          </div>
          <h3 class="font-sans font-black text-2xl text-white">Diagnóstico Computadorizado Oficial</h3>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Elevadores pneumáticos, peças 100% genuínas Honda HAMP e telemetria eletrônica direta com a fábrica para revisões transparentes.
          </p>
        </div>
      </div>

    </div>
  </section>
`;

if (!hondaHtml.includes('showroom-hero.jpg')) {
  const targetComoFunciona = '<section id="como-funciona"';
  hondaHtml = hondaHtml.replace(targetComoFunciona, showroomServiceSection + '\n  ' + targetComoFunciona);
  fs.writeFileSync('concessionaria-honda/index.html', hondaHtml, 'utf8');
  console.log('✅ Concessionária Honda updated with showroom-hero.jpg and workshop-service.jpg');
}
