const fs = require('fs');
const path = require('path');

console.log('=== Integrating Final Batch Images (Idiomas, Particular & Caxixi) ===');

// ==========================================
// 1. PROFESSOR DE IDIOMAS (POLYGLOT ACADEMY)
// ==========================================
let idiomasHtml = fs.readFileSync('professor-idiomas/index.html', 'utf8');

const idiomasShowcase = `
  <!-- ========================================================================= -->
  <!-- AULAS DE CONVERSAÇÃO DINÂMICAS & CAFÉ (FLOW PHOTOREALISTIC ASSET)         -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#080E17] border-b border-cyan-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#0D1624] border border-cyan-500/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
          <img 
            src="assets/aulas-conversacao.jpg" 
            alt="Sessão dinâmica de conversação em inglês com professora e aluna sorridentes em cafeteria aconchegante com laptop e aplicativo" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-cyan-300">
            <i class="fa-solid fa-comments mr-1.5"></i> Método Direct Speech 100% Prático
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-cyan-200 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-cyan-800 block">Inglês para Viagens, Carreira & Entrevistas</span>
              <span class="font-bold font-montserrat text-sm text-slate-900">Fale com Confiança Desde a 1ª Semana</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-cyan-950 text-cyan-200 font-bold text-xs">Zero Bloqueio</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-earth-americas"></i> Destrave Sua Fala Definitivamente
          </div>
          <h2 class="font-montserrat font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Fluência Real Sem Regras Gramaticais Enfadonhas
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Esqueça anos de cursinho tradicional repetindo frases sem sentido. Criamos simulações reais do seu dia a dia profissional e de viagens para você pensar em inglês espontaneamente.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-cyan-400 font-black text-2xl counter-up" data-target="+680">+680</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Alunos Fluentes</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl counter-up" data-target="90">90 Dias</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Primeira Conversa</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl">Grátis</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Nivelamento</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1!%20Gostaria%20de%20fazer%20meu%20teste%20de%20nivelamento%20de%20ingl%C3%AAs%20gratuito." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:opacity-95 text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-cyan-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Nivelamento & Aula Teste</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!idiomasHtml.includes('aulas-conversacao.jpg')) {
  const targetDiag = '<section id="diagnostico"';
  idiomasHtml = idiomasHtml.replace(targetDiag, idiomasShowcase + '\n  ' + targetDiag);
  fs.writeFileSync('professor-idiomas/index.html', idiomasHtml, 'utf8');
  console.log('✅ Professor de Idiomas updated with aulas-conversacao.jpg');
}


// ==========================================
// 2. PROFESSOR PARTICULAR (PROF. GABRIEL MENDES)
// ==========================================
let partHtml = fs.readFileSync('professor-particular/index.html', 'utf8');

const particularShowcase = `
  <!-- ========================================================================= -->
  <!-- MESA DE ESTUDOS, IPAD & EQUAÇÕES RESOLVIDAS (FLOW PHOTOREALISTIC ASSET)    -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#0B0D14] border-b border-indigo-900/40 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#121624] border border-indigo-500/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-white/10 shadow-2xl group">
          <img 
            src="assets/estudos-mentor.jpg" 
            alt="Estudante focada resolvendo equações de física e cálculo com Apple Pencil no iPad Pro em mesa de estudos organizada" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-indigo-300">
            <i class="fa-solid fa-graduation-cap mr-1.5"></i> Metodologia Ativa & Resolução Guiada
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-indigo-200 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-indigo-800 block">Matemática, Física, Química & ENEM</span>
              <span class="font-bold font-outfit text-sm text-slate-900">Salto Médio de 3.5 Pontos nas Notas Escolares</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-indigo-950 text-indigo-200 font-bold text-xs">Aprovação</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-brain"></i> Recuperação & Alta Performance
          </div>
          <h2 class="font-outfit font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Transforme o Medo de Exatas em Segurança e Excelência
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Identificamos a lacuna de aprendizado exata dos anos anteriores que está travando o aluno hoje. Com explicações visuais e listas inteligentes de exercícios, o entendimento acontece de verdade.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-indigo-400 font-black text-2xl counter-up" data-target="+820">+820</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Alunos Salvos</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl counter-up" data-target="98%">98%</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Taxa Aprovação</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl">+3.5</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Salto na Média</div>
            </div>
          </div>
          <div class="pt-2">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%20Prof.%20Gabriel!%20Gostaria%20de%20agendar%20uma%20aula%20particular%20de%20refor%C3%A7o." target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 hover:opacity-95 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-indigo-950/40 transition transform hover:scale-105">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Agendar Aula de Diagnóstico</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!partHtml.includes('estudos-mentor.jpg')) {
  const targetSimulador = '<section id="simulador"';
  partHtml = partHtml.replace(targetSimulador, particularShowcase + '\n  ' + targetSimulador);
  fs.writeFileSync('professor-particular/index.html', partHtml, 'utf8');
  console.log('✅ Professor Particular updated with estudos-mentor.jpg');
}


// ==========================================
// 3. CAXIXI (TRADIÇÃO CERÂMICA DO RECÔNCAVO)
// ==========================================
let caxixiHtml = fs.readFileSync('caxixi/index.html', 'utf8');

const caxixiClayShowcase = `
  <!-- ========================================================================= -->
  <!-- FEITURA DO BARRO & OLARIA TRADICIONAL (FLOW PHOTOREALISTIC ASSET)         -->
  <!-- ========================================================================= -->
  <section class="py-16 bg-[#160E08] border-b border-amber-900/40 relative overflow-hidden text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
      <div class="card-lift bg-[#22160E] border border-amber-600/30 rounded-3xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-2xl">
        <div class="lg:col-span-7 relative rounded-2xl overflow-hidden aspect-[16/10] border border-amber-900/40 shadow-2xl group">
          <img 
            src="assets/ceramica-artesanal.jpg" 
            alt="Oficina de olaria artesanal na Bahia com prateleiras de vasos de barro secando e artesã moldando cerâmica na roda de oleiro" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
            loading="lazy" 
            decoding="async"
          />
          <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-amber-400">
            <i class="fa-solid fa-shapes mr-1.5"></i> Tradição Tricentenária de Maragojipe & Nazaré
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-3.5 rounded-xl border border-amber-200 text-black flex items-center justify-between text-xs">
            <div>
              <span class="text-[10px] uppercase font-bold text-amber-900 block">Argila Pura do Recôncavo Moldada à Mão</span>
              <span class="font-bold font-serif text-sm text-slate-900">A Alma da Cerâmica e Culinária Baiana</span>
            </div>
            <span class="px-3 py-1 rounded-lg bg-amber-950 text-amber-200 font-bold text-xs">Herança Viva</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-amber-600/20 border border-amber-600/40 text-amber-300 text-xs font-bold uppercase tracking-wider">
            <i class="fa-solid fa-fire-flame-curved"></i> Queima em Fornos Tradicionais
          </div>
          <h2 class="font-serif font-black text-3xl sm:text-4xl text-white tracking-tight leading-snug">
            Panelas de Barro, Moquecas e a Sabedoria dos Nossos Mestres
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            O sabor inigualável da nossa comida nasce no barro do Recôncavo. Cada panela, cumbuca e pote decorativo guarda a energia ancestral das mãos que moldam a nossa cultura há mais de três séculos.
          </p>
          <div class="grid grid-cols-3 gap-3 text-center">
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-amber-400 font-black text-2xl font-serif counter-up" data-target="300">300+ Anos</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Tradição Viva</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-emerald-400 font-black text-2xl font-serif">100%</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Feito à Mão</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-black/40 border border-white/10">
              <div class="text-white font-black text-2xl font-serif">Nazaré</div>
              <div class="text-[11px] text-slate-300 mt-0.5">Berço do Barro</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
`;

if (!caxixiHtml.includes('ceramica-artesanal.jpg')) {
  // Insert before the footer or before the first section
  const targetSignature = '<div class="signature-section"';
  if (caxixiHtml.includes(targetSignature)) {
    caxixiHtml = caxixiHtml.replace(targetSignature, caxixiClayShowcase + '\n  ' + targetSignature);
  } else {
    caxixiHtml = caxixiHtml.replace('<main>', '<main>\n' + caxixiClayShowcase);
  }
  fs.writeFileSync('caxixi/index.html', caxixiHtml, 'utf8');
  console.log('✅ Caxixi updated with ceramica-artesanal.jpg');
}
