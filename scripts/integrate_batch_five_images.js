const fs = require('fs');
const path = require('path');

console.log('=== Integrating Batch 5 Flow Images into Sites ===');

// ==========================================
// 1. RAMPA BIKE (OFICINA CERTIFICADA)
// ==========================================
let rampaHtml = fs.readFileSync('rampabike/index.html', 'utf8');

const rampaWorkshopShowcase = `
  <!-- ========================================================================= -->
  <!-- OFICINA ESPECIALIZADA & PARK TOOL CERTIFIED (FLOW PHOTOREALISTIC ASSET)   -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#161616] border-t border-white/10 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#1F1F1F] border border-orange-500/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
          <img 
            src="assets/bike-workshop.jpg" 
            alt="Mecânico especializado em oficina de ciclismo de alta performance ajustando mountain bike de carbono S-Works" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-orange-400 shadow-sm">
            <i class="fa-solid fa-wrench mr-1.5"></i> Park Tool Certified Service
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-black/85 backdrop-blur-md p-3.5 rounded-xl border border-white/10 text-white flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-orange-400 block">Oficina Especializada MTB, Speed & E-Bike</span>
              <span class="font-bold text-sm">Sangria de Freios, Suspensão & Transmissão Eletrônica</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-orange-600 text-white font-bold text-xs">Revisão Geral</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-orange-500/10 border border-orange-500/30 text-orange-400 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-gear"></i> Mecânica de Alta Performance
          </div>
          <h2 class="font-display font-black text-3xl sm:text-4xl text-white tracking-tight uppercase leading-snug">
            Cuidado Cirúrgico com Sua Bike de Estrada ou Trilha
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Ferramental 100% calibrado, torquímetros de precisão para quadros de carbono e lavagem ultrassônica de peças. Sua bike sai pronta para vencer qualquer subida ou competição.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-orange-400 font-black text-2xl counter-up" data-target="+3.500">+3.500</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Bikes Revisadas</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl counter-up" data-target="24h">24h</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Prazo Padrão</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-white font-black text-2xl">Leva & Traz</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Disponível</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Rampa%20Bike!%20Gostaria%20de%20agendar%20uma%20revis%C3%A3o%20para%20minha%20bike." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-orange-600 hover:bg-orange-700 text-white font-black text-xs uppercase tracking-wider shadow-lg shadow-orange-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Revisão da Minha Bike</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!rampaHtml.includes('bike-workshop.jpg')) {
  const targetOficina = '<section id="oficina"';
  rampaHtml = rampaHtml.replace(targetOficina, rampaWorkshopShowcase + '\n  ' + targetOficina);
  fs.writeFileSync('rampabike/index.html', rampaHtml, 'utf8');
  console.log('✅ Rampa Bike updated with bike-workshop.jpg');
}


// ==========================================
// 2. PROFESSOR DE MÚSICA (STUDIO HARMONIA)
// ==========================================
let musicaHtml = fs.readFileSync('professor-musica/index.html', 'utf8');

const musicaStudioShowcase = `
  <!-- ========================================================================= -->
  <!-- ESTÚDIO ACÚSTICO & AMBIENTE DE ENSAIO (FLOW PHOTOREALISTIC ASSET)         -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#0E0B14] border-b border-purple-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#161220] border border-purple-500/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
          <img 
            src="assets/estudio-musica.jpg" 
            alt="Estúdio musical acústico com piano Steinway, violão clássico vintage e iluminação quente de lâmpadas Edison" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-amber-300">
            <i class="fa-solid fa-music mr-1.5"></i> Estúdio Harmonia Conceito
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-purple-300 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-purple-700 block">Piano Steinway & Violões Acústicos</span>
              <span class="font-bold font-serif text-sm text-slate-900">Isolamento Acústico Profissional</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-purple-950 text-purple-200 font-bold text-xs">Aulas VIP</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-purple-500/10 border border-purple-500/30 text-purple-300 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-guitar"></i> Prática Real desde a 1ª Aula
          </div>
          <h2 class="font-playfair font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Aprenda Seu Instrumento dos Sonhos no Ambiente Perfeito
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Nada de métodos chatos e anos só de teoria sem tocar nada. Aqui você toca suas músicas preferidas nas primeiras 4 semanas, com postura correta e ouvido musical refinado.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl counter-up" data-target="60">60 Dias</div>
              <div class="text-[11px] text-slate-300 mt-0.5">1ª Apresentação</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-purple-400 font-black text-2xl counter-up" data-target="+450">+450</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Alunos Ativos</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl">Grátis</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Aula Experimental</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostaria%20de%20agendar%20uma%20aula%20experimental%20no%20Est%C3%BAdio%20Harmonia." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-purple-600 to-amber-600 hover:opacity-95 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-purple-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Aula Experimental Gratuita</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!musicaHtml.includes('estudio-musica.jpg')) {
  const targetSimulador = '<section id="simulador"';
  musicaHtml = musicaHtml.replace(targetSimulador, musicaStudioShowcase + '\n  ' + targetSimulador);
  fs.writeFileSync('professor-musica/index.html', musicaHtml, 'utf8');
  console.log('✅ Professor de Música updated with estudio-musica.jpg');
}


// ==========================================
// 3. LAVANDERIA (LAVAMAX EXPRESS)
// ==========================================
let lavaHtml = fs.readFileSync('lavanderia/index.html', 'utf8');

const lavaShowcase = `
  <!-- ========================================================================= -->
  <!-- MÁQUINAS MIELE INOX & ROUPAS DOBRADAS (FLOW PHOTOREALISTIC ASSET)         -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#080E17] border-b border-cyan-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#0D1624] border border-cyan-500/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
          <img 
            src="assets/lavanderia-moderna.jpg" 
            alt="Lavanderia moderna com fileira de lavadoras industriais inox Miele e toalhas brancas dobradas em cestos de vime" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-cyan-300">
            <i class="fa-solid fa-shirt mr-1.5"></i> Tecnologia Industrial Miele Inox
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-cyan-200 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-cyan-700 block">Lavagem com Ozônio & Toalhas Macias</span>
              <span class="font-bold text-sm text-slate-900">Roupas Lavadas, Secas & Passadas em 24h</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-cyan-950 text-cyan-300 font-bold text-xs">Delivery Grátis</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-water"></i> Economize 12 Horas por Semana
          </div>
          <h2 class="font-outfit font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Suas Roupas Perfumadas, Macias e Prontas para o Armário
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Adeus varal na sala e montanhas de roupas para passar no domingo. Coletamos na sua casa, higienizamos com produtos ecológicos e entregamos tudo dobrado e perfumado.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-cyan-400 font-black text-2xl counter-up" data-target="24h">24h</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Entrega Rápida</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl counter-up" data-target="100%">100%</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Hipoalergênico</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl">R$ 0</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Taxa de Coleta</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Lavamax!%20Gostaria%20de%20agendar%20uma%20coleta%20de%20roupas." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-cyan-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-truck"></i>
              <span>Solicitar Coleta no Meu Endereço</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!lavaHtml.includes('lavanderia-moderna.jpg')) {
  const targetCalc = '<section id="calculadora"';
  lavaHtml = lavaHtml.replace(targetCalc, lavaShowcase + '\n  ' + targetCalc);
  fs.writeFileSync('lavanderia/index.html', lavaHtml, 'utf8');
  console.log('✅ Lavanderia updated with lavanderia-moderna.jpg');
}


// ==========================================
// 4. OFTALMOLOGISTA (CLÍNICA OPTIVISION)
// ==========================================
let oftalHtml = fs.readFileSync('oftalmologista/index.html', 'utf8');

const oftalShowcase = `
  <!-- ========================================================================= -->
  <!-- LÂMPADA DE FENDA & DIAGNÓSTICO RETINIANO (FLOW PHOTOREALISTIC ASSET)      -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#060A10] border-b border-cyan-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#0B121E] border border-cyan-500/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
          <img 
            src="assets/oftalmo-tech.jpg" 
            alt="Médica oftalmologista realizando exame microscópico de lâmpada de fenda digital com tela de mapeamento retiniano" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-cyan-300">
            <i class="fa-solid fa-eye mr-1.5"></i> Mapeamento de Retina em Alta Resolução
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-cyan-200 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-cyan-800 block">Diagnóstico de Glaucoma, Catarata & Refração</span>
              <span class="font-bold text-sm text-slate-900">Precisão Milimétrica sem Desconforto</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-cyan-950 text-cyan-200 font-bold text-xs">Exame 100% Digital</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-shield-halved"></i> Saúde Ocular Preventiva
          </div>
          <h2 class="font-outfit font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Enxergue o Mundo com Clareza e Máxima Nitidez
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Detecção precoce de alterações na córnea, cristalino e retina com equipamentos de tecnologia alemã. Grau perfeito na primeira consulta e laudo completo para óculos e lentes de contato.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-cyan-400 font-black text-2xl counter-up" data-target="+8.900">+8.900</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Exames Feitos</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl counter-up" data-target="99.7%">99.7%</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Satisfação</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl">Zero Dor</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Procedimento Suave</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20OptiVision!%20Gostaria%20de%20agendar%20uma%20consulta%20oftalmol%C3%B3gica." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-cyan-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Consulta Oftalmológica</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!oftalHtml.includes('oftalmo-tech.jpg')) {
  const targetTeste = '<section id="teste-visao"';
  oftalHtml = oftalHtml.replace(targetTeste, oftalShowcase + '\n  ' + targetTeste);
  fs.writeFileSync('oftalmologista/index.html', oftalHtml, 'utf8');
  console.log('✅ Oftalmologista updated with oftalmo-tech.jpg');
}


// ==========================================
// 5. REFORMA DE MÓVEIS (ATELIÊ DO RESTAURO)
// ==========================================
let refHtml = fs.readFileSync('reforma-moveis/index.html', 'utf8');

const refShowcase = `
  <!-- ========================================================================= -->
  <!-- MESTRE MARCENEIRO & RESTAURAÇÃO ARTESANAL (FLOW PHOTOREALISTIC ASSET)     -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#0E0B08] border-b border-amber-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#16120E] border border-amber-500/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
          <img 
            src="assets/artesao-madeira.jpg" 
            alt="Mestre marceneiro em bancada rústica restaurando poltrona clássica de madeira maciça e palhinha vienense com plaina manual" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-amber-300">
            <i class="fa-solid fa-hammer mr-1.5"></i> Restauro Nobre de Madeira Maciça
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-amber-200 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-amber-800 block">Palhinha Indiana, Verniz PU & Espumas D-33</span>
              <span class="font-bold font-playfair text-sm text-slate-900">Seu Móvel Herdado Renascido Como Novo</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-amber-950 text-amber-200 font-bold text-xs">5 Anos Garantia</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-tree"></i> 40 Anos de Tradição Familiar
          </div>
          <h2 class="font-playfair font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Preserve a Memória Afetiva e a Qualidade dos Seus Móveis
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Móveis antigos têm madeira nobre (jacarandá, peroba, imbúia) que não existe mais no mercado. Restauramos a estrutura, trocamos o tecido por veludos impermeáveis ou couro e entregamos uma obra de arte na sua sala.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl font-playfair counter-up" data-target="+2.100">+2.100</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Móveis Salvos</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl font-playfair">5 Anos</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Garantia Estrutural</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-white font-black text-2xl font-playfair">Em Domicílio</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Orçamento sem Custo</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostaria%20de%20enviar%20fotos%20do%20meu%20m%C3%B3vel%20para%20or%C3%A7amento%20de%20restaura%C3%A7%C3%A3o." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-amber-600 to-amber-700 hover:opacity-95 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-amber-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-camera"></i>
              <span>Enviar Foto do Meu Móvel no WhatsApp</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!refHtml.includes('artesao-madeira.jpg')) {
  const targetOrcamento = '<section id="orcamento"';
  refHtml = refHtml.replace(targetOrcamento, refShowcase + '\n  ' + targetOrcamento);
  fs.writeFileSync('reforma-moveis/index.html', refHtml, 'utf8');
  console.log('✅ Reforma de Móveis updated with artesao-madeira.jpg');
}
