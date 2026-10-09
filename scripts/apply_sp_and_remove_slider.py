import re

file_path = r'f:\Nova pasta\site\reforma-moveis\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Head title and meta to mention São Paulo - SP
html = html.replace(
    '<title>Renova Móveis | Reforma e Restauração de Móveis de Madeira e Estofados</title>',
    '<title>Renova Móveis | Reforma e Restauração de Móveis em São Paulo - SP</title>'
)
html = html.replace(
    'Seu móvel favorito pode ter uma nova história. Deixe seus móveis mais bonitos, resistentes e com cara de novo com a Renova Móveis. Solicite seu orçamento gratuito.',
    'Ateliê especializado em reforma e restauração de móveis em São Paulo - SP. Marcenaria fina, troca de tecidos e acabamentos nobres com coleta e entrega na Grande SP.'
)

# 2. Replace the Before/After Services section with an Artisanal Showcase Gallery
old_services_section_pattern = re.compile(
    r'<!-- ========================================================================= -->\s*'
    r'<!-- SEÇÃO NOSSOS SERVIÇOS & VITRINE ANTES/DEPOIS.*?<!-- ========================================================================= -->\s*'
    r'<!-- POR QUE ESCOLHER A RENOVA MÓVEIS',
    re.DOTALL
)

new_services_section = '''<!-- ========================================================================= -->
  <!-- SEÇÃO NOSSOS SERVIÇOS & VITRINE ARTESANAL (Sem antes/depois)               -->
  <!-- ========================================================================= -->
  <section id="servicos" class="reveal py-16 md:py-24 bg-renova-bgLight border-b border-renova-border">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Lado Esquerdo: Textos & Checklist -->
        <div class="lg:col-span-5 space-y-6">
          <span class="text-xs font-outfit font-extrabold uppercase tracking-widest text-renova-amber">
            NOSSOS SERVIÇOS & ATELIÊ
          </span>

          <h2 class="font-outfit font-black text-3xl sm:text-5xl text-slate-900 tracking-tight leading-[1.15]">
            Do simples ao sofisticado, transformamos seu móvel.
          </h2>

          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
            Realizamos reformas completas em móveis de madeira maciça, MDF e estofados. Seja para recuperar o aspecto original ou dar um novo estilo elegante, nós cuidamos de cada detalhe com marcenaria tradicional e tapeçaria de alto padrão em São Paulo.
          </p>

          <!-- Checklist dos Serviços -->
          <ul class="space-y-3.5 text-xs sm:text-sm text-slate-700 font-medium">
            <li class="flex items-center gap-3">
              <span class="w-5 h-5 rounded-full bg-renova-amber/20 text-renova-amber flex items-center justify-center text-xs flex-shrink-0">
                <i class="fa-solid fa-check"></i>
              </span>
              <span>Restauração estrutural de móveis clássicos e contemporâneos</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="w-5 h-5 rounded-full bg-renova-amber/20 text-renova-amber flex items-center justify-center text-xs flex-shrink-0">
                <i class="fa-solid fa-check"></i>
              </span>
              <span>Troca de estofados com tecidos nobres (linho, boucle e veludo)</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="w-5 h-5 rounded-full bg-renova-amber/20 text-renova-amber flex items-center justify-center text-xs flex-shrink-0">
                <i class="fa-solid fa-check"></i>
              </span>
              <span>Pintura especial, laqueamento acetinado e envernizamento marítimo</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="w-5 h-5 rounded-full bg-renova-amber/20 text-renova-amber flex items-center justify-center text-xs flex-shrink-0">
                <i class="fa-solid fa-check"></i>
              </span>
              <span>Tratamento anti-cupim, eliminação de folgas e polimento de ferragens</span>
            </li>
          </ul>

          <div class="pt-4 flex flex-wrap items-center gap-4">
            <a href="https://wa.me/5532999292311?text=gostei%20desse%20site%2C%20qual%20o%20valor%3F" target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3.5 rounded-full bg-renova-amber hover:bg-renova-amberHover text-renova-darkWood font-black text-xs uppercase tracking-wider shadow-md transition transform hover:scale-105" rel="noopener noreferrer">
              <i class="fa-brands fa-whatsapp text-sm"></i>
              <span>Solicitar Orçamento no WhatsApp</span>
            </a>
            <span class="text-xs text-slate-500 font-medium">Orçamento sem compromisso</span>
          </div>
        </div>

        <!-- Lado Direito: Vitrine da Peça Restaurada & Detalhes Artesanais -->
        <div class="lg:col-span-7">
          <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-stretch">
            
            <!-- Card Principal com Foto da Peça Restaurada -->
            <div class="md:col-span-7 bg-white p-4 rounded-3xl border border-renova-border shadow-xl flex flex-col justify-between relative overflow-hidden group">
              <div class="relative rounded-2xl overflow-hidden aspect-[4/5] bg-slate-100">
                <img 
                  src="assets/chair-after.jpg" 
                  alt="Móvel restaurado pelo ateliê Renova Móveis com madeira polida e estofamento em linho nobre" 
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" 
                  loading="lazy"
                />
                
                <!-- Badge de Excelência -->
                <div class="absolute top-3 left-3 bg-renova-darkWood/90 backdrop-blur-md text-white px-3 py-1.5 rounded-xl border border-white/10 shadow-lg text-[10px] font-bold flex items-center gap-1.5">
                  <i class="fa-solid fa-medal text-renova-amber"></i>
                  <span>Mobiliário Restaurado</span>
                </div>

                <!-- Tag flutuante inferior -->
                <div class="absolute bottom-3 left-3 right-3 bg-gradient-to-t from-black/85 via-black/50 to-transparent p-3.5 rounded-xl text-white">
                  <span class="text-[10px] font-mono uppercase tracking-widest text-renova-amber block font-bold">PADRÃO ATELIÊ RENOVA</span>
                  <span class="text-xs font-bold block mt-0.5">Madeira nobre tratada & estofamento anatômico D33</span>
                </div>
              </div>

              <div class="mt-3 flex items-center justify-between text-[11px] text-slate-500 px-1">
                <span class="flex items-center gap-1 font-semibold text-slate-700">
                  <i class="fa-solid fa-certificate text-renova-amber"></i> Garantia de 1 ano em estrutura
                </span>
                <span class="font-medium text-renova-amber font-bold">100% Artesanal</span>
              </div>
            </div>

            <!-- Coluna dos 3 Detalhes com Anotações Manuscritas -->
            <div class="md:col-span-5 flex flex-col justify-between gap-4">
              
              <!-- Detalhe 1: Madeira -->
              <div class="bg-white p-3.5 rounded-2xl border border-renova-border shadow-md hover:shadow-lg transition-all group">
                <div class="flex items-center gap-3">
                  <div class="w-16 h-16 rounded-xl overflow-hidden flex-shrink-0 border border-slate-100 shadow-inner">
                    <img src="assets/detail-wood.jpg" alt="Detalhe do encaixe da madeira" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                  </div>
                  <div>
                    <span class="font-script text-xl text-slate-800 font-bold block leading-none">Restauração da madeira</span>
                    <span class="text-[11px] text-slate-500 mt-1 block leading-tight">Encaixes reforçados e tratamento profilático anti-cupim</span>
                  </div>
                </div>
              </div>

              <!-- Detalhe 2: Tecido -->
              <div class="bg-white p-3.5 rounded-2xl border border-renova-border shadow-md hover:shadow-lg transition-all group">
                <div class="flex items-center gap-3">
                  <div class="w-16 h-16 rounded-xl overflow-hidden flex-shrink-0 border border-slate-100 shadow-inner">
                    <img src="assets/detail-fabric.jpg" alt="Detalhe da troca de tecido e estofado" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                  </div>
                  <div>
                    <span class="font-script text-xl text-slate-800 font-bold block leading-none">Troca de tecido e estofado</span>
                    <span class="text-[11px] text-slate-500 mt-1 block leading-tight">Espuma D33/D45 com tecidos impermeabilizados</span>
                  </div>
                </div>
              </div>

              <!-- Detalhe 3: Acabamento -->
              <div class="bg-white p-3.5 rounded-2xl border border-renova-border shadow-md hover:shadow-lg transition-all group">
                <div class="flex items-center gap-3">
                  <div class="w-16 h-16 rounded-xl overflow-hidden flex-shrink-0 border border-slate-100 shadow-inner">
                    <img src="assets/detail-finish.jpg" alt="Detalhe do acabamento premium" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                  </div>
                  <div>
                    <span class="font-script text-xl text-slate-800 font-bold block leading-none">Acabamento premium</span>
                    <span class="text-[11px] text-slate-500 mt-1 block leading-tight">Verniz PU marítimo fosco ou brilho com toque sedoso</span>
                  </div>
                </div>
              </div>

              <!-- Card Bônus: Atendimento em Domicílio em SP -->
              <div class="p-3.5 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-slate-800 flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-renova-amber text-renova-darkWood flex items-center justify-center text-sm font-bold flex-shrink-0 shadow-sm">
                  <i class="fa-solid fa-truck-ramp-box"></i>
                </div>
                <div class="text-xs">
                  <span class="font-bold text-slate-900 block leading-tight">Coleta & Entrega em SP Capital</span>
                  <span class="text-slate-600 text-[11px]">Transporte protegido em toda a região metropolitana</span>
                </div>
              </div>

            </div>

          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- POR QUE ESCOLHER A RENOVA MÓVEIS'''

html = old_services_section_pattern.sub(new_services_section, html)

# 3. Update the Contact / Map section for São Paulo Capital
old_contact_section_pattern = re.compile(
    r'<!-- ========================================================================= -->\s*'
    r'<!-- SEÇÃO ONDE ESTAMOS & FORMULÁRIO DE ORÇAMENTO.*?<!-- ========================================================================= -->\s*'
    r'<!-- FOOTER',
    re.DOTALL
)

new_contact_section = '''<!-- ========================================================================= -->
  <!-- SEÇÃO ONDE ESTAMOS & FORMULÁRIO DE ORÇAMENTO (Capital de SP)               -->
  <!-- ========================================================================= -->
  <section id="contato" class="reveal py-16 md:py-24 bg-renova-bgLight relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        
        <!-- Card Esquerda: Onde Estamos & Mapa (São Paulo - SP Capital) -->
        <div class="lg:col-span-7 rounded-3xl p-8 sm:p-10 text-white flex flex-col justify-between shadow-2xl relative overflow-hidden bg-cover bg-center border border-renova-borderDark/40" style="background-image: linear-gradient(to right, rgba(22, 19, 16, 0.95) 0%, rgba(22, 19, 16, 0.88) 55%, rgba(22, 19, 16, 0.75) 100%), url('assets/hero-full-mockup.jpg');">
          
          <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center h-full relative z-10">
            <!-- Textos e Botão WhatsApp -->
            <div class="md:col-span-6 space-y-4">
              <span class="text-[11px] font-outfit font-extrabold uppercase tracking-widest text-renova-amber block">
                ONDE ESTAMOS • SÃO PAULO - SP
              </span>
              <h2 class="font-outfit font-black text-2xl sm:text-3xl text-white tracking-tight leading-tight">
                Atendemos toda a Capital de SP!
              </h2>
              <p class="text-white/80 text-xs sm:text-sm leading-relaxed">
                Nosso ateliê próprio atende toda a capital de <strong>São Paulo - SP</strong> e região metropolitana (Pinheiros, Jardins, Moema, Perdizes, Tatuapé, Santana, Morumbi e Grande SP). Oferecemos coleta e entrega com transporte acolchoado e seguro.
              </p>

              <div class="pt-2">
                <a href="https://wa.me/5532999292311?text=gostei%20desse%20site%2C%20qual%20o%20valor%3F" target="_blank" class="shimmer-btn inline-flex items-center gap-2.5 px-6 py-3 rounded-full bg-renova-amber hover:bg-renova-amberHover text-renova-darkWood font-black text-xs uppercase tracking-wider transition transform hover:scale-105 shadow-lg" rel="noopener noreferrer">
                  <i class="fa-brands fa-whatsapp text-base"></i>
                  <span>Falar no WhatsApp: (32) 99929-2311</span>
                </a>
              </div>
            </div>

            <!-- Mapa Integrado Flutuante com Cartão de Endereço em SP Capital -->
            <div class="md:col-span-6">
              <div class="relative rounded-2xl overflow-hidden shadow-2xl border border-white/20 bg-white group">
                <div class="absolute top-3 left-3 bg-white/95 backdrop-blur-sm p-3 rounded-xl shadow-md z-10 border border-slate-100 max-w-[210px]">
                  <span class="font-outfit font-black text-slate-900 text-[11px] block leading-tight">São Paulo - SP (Capital)</span>
                  <span class="text-[9px] text-slate-500 block leading-tight mt-0.5">Ateliê Central & Coleta Agendada</span>
                  <span class="text-[10px] font-bold text-renova-amber block mt-0.5">(32) 99929-2311</span>
                </div>
                <img src="assets/map-sp-capital.jpg" alt="Mapa de atendimento da Renova Móveis em São Paulo Capital" class="w-full h-52 sm:h-56 object-cover transform group-hover:scale-105 transition-transform duration-500">
              </div>
            </div>
          </div>

        </div>

        <!-- Card Direita: Solicite Seu Orçamento (Formulário) -->
        <div class="lg:col-span-5 bg-white rounded-3xl p-8 sm:p-10 border border-renova-border shadow-2xl flex flex-col justify-between">
          
          <div>
            <h3 class="font-outfit font-black text-2xl sm:text-3xl text-slate-900 tracking-tight mb-1">
              Solicite seu orçamento
            </h3>
            <p class="text-xs text-slate-500 mb-6">
              Preencha os dados abaixo e retornaremos rapidamente com a estimativa do seu projeto em São Paulo.
            </p>

            <!-- Form -->
            <form id="form-orcamento" onsubmit="enviarOrcamento(event)" class="space-y-4">
              <div>
                <input 
                  type="text" 
                  id="form-nome" 
                  required 
                  placeholder="Nome completo" 
                  class="w-full px-4 py-3.5 rounded-xl bg-slate-50 border border-renova-border text-slate-800 text-sm focus:border-renova-amber outline-none transition"
                />
              </div>

              <div>
                <input 
                  type="tel" 
                  id="form-whatsapp" 
                  required 
                  placeholder="WhatsApp com DDD" 
                  class="w-full px-4 py-3.5 rounded-xl bg-slate-50 border border-renova-border text-slate-800 text-sm focus:border-renova-amber outline-none transition"
                />
              </div>

              <div>
                <input 
                  type="text" 
                  id="form-bairro" 
                  placeholder="Bairro em São Paulo ou Região" 
                  class="w-full px-4 py-3.5 rounded-xl bg-slate-50 border border-renova-border text-slate-800 text-sm focus:border-renova-amber outline-none transition"
                />
              </div>

              <div>
                <select 
                  id="form-servico" 
                  class="w-full px-4 py-3.5 rounded-xl bg-slate-50 border border-renova-border text-slate-700 text-sm focus:border-renova-amber outline-none transition"
                >
                  <option value="Reforma Completa">Reforma Completa de Móvel</option>
                  <option value="Troca de Estofado e Tecido">Troca de Tecido / Estofamento</option>
                  <option value="Restauração de Madeira Clássica">Restauração de Madeira Maciça</option>
                  <option value="Laqueamento ou Envernizamento">Laqueamento / Pintura / Verniz</option>
                  <option value="Outros Serviços de Marcenaria">Outros reparos / Avaliação</option>
                </select>
              </div>

              <div class="pt-2">
                <button 
                  type="submit" 
                  class="shimmer-btn w-full py-4 rounded-xl bg-renova-amber hover:bg-renova-amberHover text-renova-darkWood font-black text-sm uppercase tracking-wider shadow-lg transition transform hover:scale-[1.02] flex items-center justify-center gap-2"
                >
                  <i class="fa-brands fa-whatsapp text-lg"></i>
                  <span>Enviar solicitação no WhatsApp</span>
                </button>
              </div>

              <div class="text-center pt-2">
                <span class="text-[10px] text-slate-400 flex items-center justify-center gap-1.5">
                  <i class="fa-solid fa-lock text-slate-400"></i> Seus dados estão seguros conosco.
                </span>
              </div>
            </form>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- FOOTER'''

html = old_contact_section_pattern.sub(new_contact_section, html)

# 4. Clean up scripts (remove slider listeners, keep form submission)
old_script_pattern = re.compile(
    r'<script>\s*// Slider Antes / Depois Interativo.*?function enviarOrcamento\(e\)',
    re.DOTALL
)

new_script_prefix = '''<script>
    // Envio do Formulário para WhatsApp
    function enviarOrcamento(e)'''

html = old_script_pattern.sub(new_script_prefix, html)

# 5. Update footer address text
html = html.replace('Salvador - BA', 'São Paulo - SP')

# 6. Update form handler message to include bairro
old_form_fn = '''      let msg = `gostei desse site, qual o valor?`;
      if (nome || whatsapp) {
        msg += `\\n(Lead: ${nome} - ${whatsapp} - Serviço: ${servico})`;
      }'''

new_form_fn = '''      const bairro = (document.getElementById('form-bairro') ? document.getElementById('form-bairro').value.trim() : '') || 'São Paulo - SP';
      let msg = `gostei desse site, qual o valor?`;
      if (nome || whatsapp) {
        msg += `\\n(Lead: ${nome} - ${whatsapp} - Local: ${bairro} - Serviço: ${servico})`;
      }'''

html = html.replace(old_form_fn, new_form_fn)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Update successfully completed in index.html!')
