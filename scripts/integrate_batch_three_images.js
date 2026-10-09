const fs = require('fs');
const path = require('path');

console.log('=== Integrating Batch 3 Flow Images into Sites ===');

// ==========================================
// 1. RESTAURANTE EGEU
// ==========================================
let egeuHtml = fs.readFileSync('restaurante-egeu/index.html', 'utf8');

// Replace Unsplash food images with the real Michelin-level octopus tentacle
egeuHtml = egeuHtml.replace(
  'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1920&q=80',
  'assets/mediterranean-dish.jpg'
);
egeuHtml = egeuHtml.replace(
  'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
  'assets/mediterranean-dish.jpg'
);

fs.writeFileSync('restaurante-egeu/index.html', egeuHtml, 'utf8');
console.log('✅ Restaurante Egeu updated with mediterranean-dish.jpg');


// ==========================================
// 2. CORRETOR DE IMÓVEIS (IMOBMAX)
// ==========================================
let imobHtml = fs.readFileSync('corretor-imoveis/index.html', 'utf8');

const imobMansionShowcase = `
  <!-- ========================================================================= -->
  <!-- IMÓVEL EM DESTAQUE: MANSÃO ALPHAVILLE HORIZON (FLOW PHOTOREALISTIC ASSET) -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#050811] border-b border-re-border/60 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-gradient-to-r from-re-card to-[#0A1224] border border-re-cyan/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-re-border shadow-2xl group">
          <img 
            src="assets/luxury-mansion-pool.jpg" 
            alt="Mansão Contemporânea com Piscina de Borda Infinita e Área Gourmet Iluminada" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-re-cyan shadow-sm">
            <i class="fa-solid fa-gem text-cyan-400 mr-1.5"></i> Destaque do Mês • Alto Padrão
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-re-cyan/40 text-black flex items-center justify-between">
            <div>
              <span class="text-[10px] uppercase font-bold text-slate-500 block">Condomínio Residencial Horizon</span>
              <span class="text-sm font-black font-serif text-slate-900">Mansão Jardins do Lago • 580m²</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-cyan-950 text-cyan-300 font-serif font-black text-xs">R$ 3.850.000</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-re-cyan/10 border border-re-cyan/30 text-re-cyan text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-certificate"></i> Documentação 100% Auditada
          </div>
          <h2 class="font-serif font-black text-3xl sm:text-4xl text-white tracking-tight">
            Exclusividade, Vista Panorâmica e Segurança 24h
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Piscina aquecida de borda infinita com fogo de chão integrado, esquadrias do chão ao teto e automação residencial completa. Projeto assinado com habite-se e escritura imediata.
          </p>
          
          <div class="grid grid-cols-2 gap-3 text-xs text-slate-300 font-semibold">
            <div class="flex items-center gap-2"><i class="fa-solid fa-check text-re-cyan"></i> 4 Suítes Master</div>
            <div class="flex items-center gap-2"><i class="fa-solid fa-check text-re-cyan"></i> 4 Vagas Cobertas</div>
            <div class="flex items-center gap-2"><i class="fa-solid fa-check text-re-cyan"></i> Painéis Fotovoltaicos</div>
            <div class="flex items-center gap-2"><i class="fa-solid fa-check text-re-cyan"></i> Espaço Gourmet VIP</div>
          </div>

          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Henrique!%20Gostaria%20de%20agendar%20uma%20visita%20na%20Mans%C3%A3o%20Jardins%20do%20Lago." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-re-cyan to-blue-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-cyan-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Visita com Henrique</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!imobHtml.includes('luxury-mansion-pool.jpg')) {
  const targetSimulador = '<section id="simulador"';
  imobHtml = imobHtml.replace(targetSimulador, imobMansionShowcase + '\n  ' + targetSimulador);
  fs.writeFileSync('corretor-imoveis/index.html', imobHtml, 'utf8');
  console.log('✅ Corretor Imóveis updated with luxury-mansion-pool.jpg');
}


// ==========================================
// 3. PERSONAL TRAINER (RODRIGO SILVA)
// ==========================================
let fitHtml = fs.readFileSync('personal-trainer/index.html', 'utf8');

const fitBoutiqueShowcase = `
  <!-- ========================================================================= -->
  <!-- TREINAMENTO BOUTIQUE & METODOLOGIA VIP (FLOW PHOTOREALISTIC ASSET)         -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#0B0E17] border-b border-fit-border/60 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-fit-card border border-lime-400/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-lime-400/10 border border-lime-400/30 text-fit-lime text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-dumbbell"></i> Atendimento Presencial & Online
          </div>
          <h2 class="font-outfit font-black text-3xl sm:text-4xl text-white tracking-tight">
            Consultoria Presencial & Correção Técnica Individual
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Nada de treinos genéricos em folhas amassadas. Cada repetição é ajustada para sua biomecânica e nível de condicionamento, prevenindo lesões articulares e acelerando em até 3x a hipertrofia e definição muscular.
          </p>
          <div class="grid grid-cols-3 gap-3 pt-2 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-fit-lime font-black text-2xl font-outfit counter-up" data-target="90">90 Dias</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Protocolo Intensivo</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-cyan-400 font-black text-2xl font-outfit counter-up" data-target="0">Zero</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Lesões Registradas</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl font-outfit counter-up" data-target="100%">100%</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Foco no Seu Objetivo</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Rodrigo!%20Gostaria%20de%20agendar%20uma%20aula%20experimental%20presencial." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-fit-lime hover:bg-lime-400 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-lime-500/25 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Avaliação Física & Treino Teste</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-5 relative rounded-2xl overflow-hidden aspect-[16/10] border border-fit-border shadow-2xl group">
          <img 
            src="assets/personal-training.jpg" 
            alt="Personal Trainer Rodrigo Silva orientando aluna em treino de kettlebell em academia boutique" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs text-fit-lime font-bold">
            <i class="fa-solid fa-heart-pulse mr-1.5"></i> Biomecânica & Alta Performance
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!fitHtml.includes('personal-training.jpg')) {
  const targetMetodologia = '<section id="metodologia"';
  fitHtml = fitHtml.replace(targetMetodologia, fitBoutiqueShowcase + '\n  ' + targetMetodologia);
  fs.writeFileSync('personal-trainer/index.html', fitHtml, 'utf8');
  console.log('✅ Personal Trainer updated with personal-training.jpg');
}


// ==========================================
// 4. BANHO E TOSA (PETCARE)
// ==========================================
let petHtml = fs.readFileSync('banho-e-tosa/index.html', 'utf8');

const petSpaShowcase = `
  <!-- ========================================================================= -->
  <!-- EXPERIÊNCIA PET SPA & BANHO RELAXANTE (FLOW PHOTOREALISTIC ASSET)         -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#0E0916] border-b border-pet-border/60 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-pet-card border border-pet-pink/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-5 relative rounded-2xl overflow-hidden aspect-[16/10] border border-pet-border shadow-2xl group">
          <img 
            src="assets/pet-spa-dog.jpg" 
            alt="Golden Retriever feliz em banheira inox de pet spa com espuma e água morna" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-white/95 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-slate-200 text-xs font-bold text-pet-purple shadow-sm">
            <i class="fa-solid fa-shower text-pet-pink mr-1.5"></i> Banheira Inox Aquecida
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-black/85 backdrop-blur-md p-3 rounded-xl border border-white/10 text-white flex items-center justify-between text-xs">
            <span class="font-bold flex items-center gap-1.5"><i class="fa-solid fa-heart text-pet-pink"></i> Zero Ansiedade</span>
            <span class="text-slate-300">Shampoo Hipoalergênico</span>
          </div>
        </div>

        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-pet-pink/10 border border-pet-pink/30 text-pet-pink text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-spa"></i> Cuidado Afetuoso & Cromoterapia
          </div>
          <h2 class="font-outfit font-black text-3xl sm:text-4xl text-white tracking-tight">
            Banho sem Gaiolas, com Água na Temperatura Certa e Muito Carinho
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Nada de secadores barulhentos assustando seu filho de 4 patas. Nosso ambiente conta com acústica isolada, hidratação de pelagem com óleos naturais e envio de vídeos no seu WhatsApp durante o banho.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3 rounded-2xl bg-[#140E20] border border-white/10">
              <div class="text-pet-pink font-black text-2xl font-outfit counter-up" data-target="+4.200">+4.200</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Pets Felizes</div>
            </div>
            <div class="p-3 rounded-2xl bg-[#140E20] border border-white/10">
              <div class="text-emerald-400 font-black text-2xl font-outfit">100%</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Toalhas Esterilizadas</div>
            </div>
            <div class="p-3 rounded-2xl bg-[#140E20] border border-white/10">
              <div class="text-amber-400 font-black text-2xl font-outfit">Vídeos</div>
              <div class="text-[11px] text-slate-300 mt-0.5">No WhatsApp</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20PetCare!%20Gostaria%20de%20agendar%20um%20banho%20relaxante%20para%20o%20meu%20pet." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-pet-purple to-pet-pink hover:opacity-95 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-purple-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-paw"></i>
              <span>Agendar Banho Relaxante</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!petHtml.includes('pet-spa-dog.jpg')) {
  const targetServicos = '<section id="servicos"';
  petHtml = petHtml.replace(targetServicos, petSpaShowcase + '\n  ' + targetServicos);
  fs.writeFileSync('banho-e-tosa/index.html', petHtml, 'utf8');
  console.log('✅ Banho e Tosa updated with pet-spa-dog.jpg');
}


// ==========================================
// 5. CONCESSIONÁRIA HONDA & MOTOS
// ==========================================
let hondaHtml = fs.readFileSync('concessionaria-honda/index.html', 'utf8');

const adventureShowcase = `
  <!-- ========================================================================= -->
  <!-- ESPÍRITO DE AVENTURA & TEST RIDE (FLOW PHOTOREALISTIC ASSET)               -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#07090F] border-b border-red-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#0D111A] border border-red-600/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-red-600/20 border border-red-500/40 text-red-400 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-compass"></i> Linha Adventure & Touring
          </div>
          <h2 class="font-sans font-black text-3xl sm:text-4xl text-white tracking-tight">
            Liberdade na Estrada com a Confiabilidade Lendária Honda
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Suspensaõ eletrônica adaptativa, freios ABS de duplo canal e motor com torque instantâneo para viagens sem limites. Agende seu Test Ride e sinta a pilotagem antes de fechar negócio.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-red-400 font-black text-2xl">3 Anos</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Garantia Total</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-yellow-400 font-black text-2xl">7 Trocas</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Óleo Grátis</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl">R$ 0</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Para Fazer Test Ride</div>
            </div>
          </div>
          <div class="pt-2">
            <button onclick="openLeadModal('Agendar Test Ride Adventure')" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-red-600 hover:bg-red-700 text-white font-black text-xs uppercase tracking-wider shadow-lg shadow-red-900/40 transition transform hover:scale-105">
              <i class="fa-solid fa-motorcycle"></i>
              <span>Agendar Meu Test Ride Gratuito</span>
            </button>
          </div>
        </div>

        <div class="lg:col-span-5 relative rounded-2xl overflow-hidden aspect-[16/10] border border-red-900/50 shadow-2xl group">
          <img 
            src="assets/rider-sunset.jpg" 
            alt="Piloto em motocicleta adventure touring na rodovia costeira ao pôr do sol" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs text-red-400 font-bold">
            <i class="fa-solid fa-road mr-1.5"></i> Viva a Aventura
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!hondaHtml.includes('rider-sunset.jpg')) {
  const targetCompare = '<section id="comparador"';
  hondaHtml = hondaHtml.replace(targetCompare, adventureShowcase + '\n  ' + targetCompare);
  fs.writeFileSync('concessionaria-honda/index.html', hondaHtml, 'utf8');
  console.log('✅ Concessionária Honda updated with rider-sunset.jpg');
}
