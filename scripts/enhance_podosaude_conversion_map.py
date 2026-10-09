# -*- coding: utf-8 -*-
with open('podologo/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the 7 Treatment Cards to include direct click-to-book buttons with service pre-fill
old_treatment_cards = """      <!-- 7 Cards Row -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-7 gap-3.5 sm:gap-4">
        
        <!-- 1. Unhas Encravadas -->
        <div class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card transition flex flex-col group">
          <div class="h-28 w-full overflow-hidden bg-slate-200">
            <img src="assets/tratamento_unha_encravada.jpg" alt="Unhas Encravadas" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-3 text-center">
            <span class="font-heading font-bold text-xs text-navy-850 block">Unhas Encravadas</span>
          </div>
        </div>

        <!-- 2. Calos e Calosidades -->
        <div class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card transition flex flex-col group">
          <div class="h-28 w-full overflow-hidden bg-slate-200">
            <img src="assets/tratamento_calos_calosidades.jpg" alt="Calos e Calosidades" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-3 text-center">
            <span class="font-heading font-bold text-xs text-navy-850 block">Calos e Calosidades</span>
          </div>
        </div>

        <!-- 3. Alterações nas Unhas -->
        <div class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card transition flex flex-col group">
          <div class="h-28 w-full overflow-hidden bg-slate-200">
            <img src="assets/tratamento_alteracoes_unhas.jpg" alt="Alterações nas Unhas" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-3 text-center">
            <span class="font-heading font-bold text-xs text-navy-850 block">Alterações nas Unhas</span>
          </div>
        </div>

        <!-- 4. Micose de Unhas -->
        <div class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card transition flex flex-col group">
          <div class="h-28 w-full overflow-hidden bg-slate-200">
            <img src="assets/tratamento_micose_unhas.jpg" alt="Micose de Unhas" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-3 text-center">
            <span class="font-heading font-bold text-xs text-navy-850 block">Micose de Unhas</span>
          </div>
        </div>

        <!-- 5. Verrugas Plantares -->
        <div class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card transition flex flex-col group">
          <div class="h-28 w-full overflow-hidden bg-slate-200">
            <img src="assets/tratamento_verrugas_plantares.jpg" alt="Verrugas Plantares" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-3 text-center">
            <span class="font-heading font-bold text-xs text-navy-850 block">Verrugas Plantares</span>
          </div>
        </div>

        <!-- 6. Cuidados Preventivos -->
        <div class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card transition flex flex-col group">
          <div class="h-28 w-full overflow-hidden bg-slate-200">
            <img src="assets/tratamento_cuidados_preventivos.jpg" alt="Cuidados Preventivos" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-3 text-center">
            <span class="font-heading font-bold text-xs text-navy-850 block">Cuidados Preventivos</span>
          </div>
        </div>

        <!-- 7. Pé Diabético -->
        <div class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card transition flex flex-col group">
          <div class="h-28 w-full overflow-hidden bg-slate-200">
            <img src="assets/tratamento_pe_diabetico.jpg" alt="Pé Diabético" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-3 text-center">
            <span class="font-heading font-bold text-xs text-navy-850 block">Pé Diabético</span>
          </div>
        </div>

      </div>"""

new_treatment_cards = """      <!-- 7 Cards Row with 1-Click Direct Form Booking Buttons -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-7 gap-3.5 sm:gap-4">
        
        <!-- 1. Unhas Encravadas -->
        <div onclick="selectServiceAndScroll('Unha Encravada')" class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card hover:border-teal/60 transition flex flex-col justify-between group cursor-pointer">
          <div>
            <div class="h-28 w-full overflow-hidden bg-slate-200 relative">
              <img src="assets/tratamento_unha_encravada.jpg" alt="Unhas Encravadas" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <span class="absolute top-2 right-2 bg-navy-900/80 backdrop-blur-md text-white text-[9px] font-bold px-2 py-0.5 rounded-full">
                Alívio Rápido
              </span>
            </div>
            <div class="p-2.5 pb-1 text-center">
              <span class="font-heading font-bold text-xs text-navy-850 block leading-tight">Unhas Encravadas</span>
            </div>
          </div>
          <div class="p-2.5 pt-0">
            <button type="button" class="w-full py-1.5 px-2 rounded-xl bg-teal-50 group-hover:bg-teal text-teal-800 group-hover:text-white text-[11px] font-heading font-bold transition-colors flex items-center justify-center gap-1 shadow-sm">
              <i class="fa-regular fa-calendar-check text-[10px]"></i> Agendar
            </button>
          </div>
        </div>

        <!-- 2. Calos e Calosidades -->
        <div onclick="selectServiceAndScroll('Calos e Calosidades')" class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card hover:border-teal/60 transition flex flex-col justify-between group cursor-pointer">
          <div>
            <div class="h-28 w-full overflow-hidden bg-slate-200 relative">
              <img src="assets/tratamento_calos_calosidades.jpg" alt="Calos e Calosidades" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <span class="absolute top-2 right-2 bg-navy-900/80 backdrop-blur-md text-white text-[9px] font-bold px-2 py-0.5 rounded-full">
                Conforto
              </span>
            </div>
            <div class="p-2.5 pb-1 text-center">
              <span class="font-heading font-bold text-xs text-navy-850 block leading-tight">Calos e Calosidades</span>
            </div>
          </div>
          <div class="p-2.5 pt-0">
            <button type="button" class="w-full py-1.5 px-2 rounded-xl bg-teal-50 group-hover:bg-teal text-teal-800 group-hover:text-white text-[11px] font-heading font-bold transition-colors flex items-center justify-center gap-1 shadow-sm">
              <i class="fa-regular fa-calendar-check text-[10px]"></i> Agendar
            </button>
          </div>
        </div>

        <!-- 3. Alterações nas Unhas -->
        <div onclick="selectServiceAndScroll('Outros Cuidados')" class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card hover:border-teal/60 transition flex flex-col justify-between group cursor-pointer">
          <div>
            <div class="h-28 w-full overflow-hidden bg-slate-200 relative">
              <img src="assets/tratamento_alteracoes_unhas.jpg" alt="Alterações nas Unhas" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <span class="absolute top-2 right-2 bg-navy-900/80 backdrop-blur-md text-white text-[9px] font-bold px-2 py-0.5 rounded-full">
                Órteses
              </span>
            </div>
            <div class="p-2.5 pb-1 text-center">
              <span class="font-heading font-bold text-xs text-navy-850 block leading-tight">Alterações nas Unhas</span>
            </div>
          </div>
          <div class="p-2.5 pt-0">
            <button type="button" class="w-full py-1.5 px-2 rounded-xl bg-teal-50 group-hover:bg-teal text-teal-800 group-hover:text-white text-[11px] font-heading font-bold transition-colors flex items-center justify-center gap-1 shadow-sm">
              <i class="fa-regular fa-calendar-check text-[10px]"></i> Agendar
            </button>
          </div>
        </div>

        <!-- 4. Micose de Unhas -->
        <div onclick="selectServiceAndScroll('Micose e Laser')" class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card hover:border-teal/60 transition flex flex-col justify-between group cursor-pointer">
          <div>
            <div class="h-28 w-full overflow-hidden bg-slate-200 relative">
              <img src="assets/tratamento_micose_unhas.jpg" alt="Micose de Unhas" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <span class="absolute top-2 right-2 bg-navy-900/80 backdrop-blur-md text-white text-[9px] font-bold px-2 py-0.5 rounded-full">
                Laserterapia
              </span>
            </div>
            <div class="p-2.5 pb-1 text-center">
              <span class="font-heading font-bold text-xs text-navy-850 block leading-tight">Micose de Unhas</span>
            </div>
          </div>
          <div class="p-2.5 pt-0">
            <button type="button" class="w-full py-1.5 px-2 rounded-xl bg-teal-50 group-hover:bg-teal text-teal-800 group-hover:text-white text-[11px] font-heading font-bold transition-colors flex items-center justify-center gap-1 shadow-sm">
              <i class="fa-regular fa-calendar-check text-[10px]"></i> Agendar
            </button>
          </div>
        </div>

        <!-- 5. Verrugas Plantares -->
        <div onclick="selectServiceAndScroll('Outros Cuidados')" class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card hover:border-teal/60 transition flex flex-col justify-between group cursor-pointer">
          <div>
            <div class="h-28 w-full overflow-hidden bg-slate-200 relative">
              <img src="assets/tratamento_verrugas_plantares.jpg" alt="Verrugas Plantares" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <span class="absolute top-2 right-2 bg-navy-900/80 backdrop-blur-md text-white text-[9px] font-bold px-2 py-0.5 rounded-full">
                Inspeção
              </span>
            </div>
            <div class="p-2.5 pb-1 text-center">
              <span class="font-heading font-bold text-xs text-navy-850 block leading-tight">Verrugas Plantares</span>
            </div>
          </div>
          <div class="p-2.5 pt-0">
            <button type="button" class="w-full py-1.5 px-2 rounded-xl bg-teal-50 group-hover:bg-teal text-teal-800 group-hover:text-white text-[11px] font-heading font-bold transition-colors flex items-center justify-center gap-1 shadow-sm">
              <i class="fa-regular fa-calendar-check text-[10px]"></i> Agendar
            </button>
          </div>
        </div>

        <!-- 6. Cuidados Preventivos -->
        <div onclick="selectServiceAndScroll('Avaliação Geral')" class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card hover:border-teal/60 transition flex flex-col justify-between group cursor-pointer">
          <div>
            <div class="h-28 w-full overflow-hidden bg-slate-200 relative">
              <img src="assets/tratamento_cuidados_preventivos.jpg" alt="Cuidados Preventivos" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <span class="absolute top-2 right-2 bg-navy-900/80 backdrop-blur-md text-white text-[9px] font-bold px-2 py-0.5 rounded-full">
                Hidratação
              </span>
            </div>
            <div class="p-2.5 pb-1 text-center">
              <span class="font-heading font-bold text-xs text-navy-850 block leading-tight">Cuidados Preventivos</span>
            </div>
          </div>
          <div class="p-2.5 pt-0">
            <button type="button" class="w-full py-1.5 px-2 rounded-xl bg-teal-50 group-hover:bg-teal text-teal-800 group-hover:text-white text-[11px] font-heading font-bold transition-colors flex items-center justify-center gap-1 shadow-sm">
              <i class="fa-regular fa-calendar-check text-[10px]"></i> Agendar
            </button>
          </div>
        </div>

        <!-- 7. Pé Diabético -->
        <div onclick="selectServiceAndScroll('Pé Diabético')" class="bg-slate-50 rounded-2xl overflow-hidden border border-slate-200/80 shadow-soft hover:shadow-card hover:border-teal/60 transition flex flex-col justify-between group cursor-pointer">
          <div>
            <div class="h-28 w-full overflow-hidden bg-slate-200 relative">
              <img src="assets/tratamento_pe_diabetico.jpg" alt="Pé Diabético" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <span class="absolute top-2 right-2 bg-navy-900/80 backdrop-blur-md text-white text-[9px] font-bold px-2 py-0.5 rounded-full">
                Especializado
              </span>
            </div>
            <div class="p-2.5 pb-1 text-center">
              <span class="font-heading font-bold text-xs text-navy-850 block leading-tight">Pé Diabético</span>
            </div>
          </div>
          <div class="p-2.5 pt-0">
            <button type="button" class="w-full py-1.5 px-2 rounded-xl bg-teal-50 group-hover:bg-teal text-teal-800 group-hover:text-white text-[11px] font-heading font-bold transition-colors flex items-center justify-center gap-1 shadow-sm">
              <i class="fa-regular fa-calendar-check text-[10px]"></i> Agendar
            </button>
          </div>
        </div>

      </div>"""

if old_treatment_cards in html:
    html = html.replace(old_treatment_cards, new_treatment_cards)
    print("Replaced treatment cards with direct 1-click booking buttons!")
else:
    print("Old treatment cards not exact match, checking pattern...")

# 2. Add Quick Period Selector Pills to the Form to reduce typing and close in few clicks
old_date_field = """            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Data preferencial</label>
              <input type="date" id="form-date" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 focus:border-teal focus:ring-1 focus:ring-teal text-xs outline-none bg-slate-50 text-slate-700" />
            </div>"""

new_date_field = """            <div>
              <div class="flex items-center justify-between mb-1">
                <label class="block text-xs font-semibold text-slate-700">Data e Turno Preferencial</label>
                <span class="text-[10px] text-teal-700 font-bold"><i class="fa-solid fa-bolt text-amber-500"></i> Seleção rápida</span>
              </div>
              <input type="date" id="form-date" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 focus:border-teal focus:ring-1 focus:ring-teal text-xs outline-none bg-slate-50 text-slate-700 mb-2" />
              
              <!-- Atalhos de 1 clique para agendamento ágil -->
              <div class="flex flex-wrap gap-1.5">
                <button type="button" onclick="setQuickPeriod('Urgente / Hoje')" class="period-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-slate-100 hover:bg-teal-50 hover:text-teal border border-slate-200 transition flex items-center gap-1">
                  ⚡ Hoje / Urgente
                </button>
                <button type="button" onclick="setQuickPeriod('Manhã (09h às 12h)')" class="period-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-slate-100 hover:bg-teal-50 hover:text-teal border border-slate-200 transition flex items-center gap-1">
                  ☀️ Manhã
                </button>
                <button type="button" onclick="setQuickPeriod('Tarde (13h às 18h)')" class="period-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-slate-100 hover:bg-teal-50 hover:text-teal border border-slate-200 transition flex items-center gap-1">
                  🌤️ Tarde
                </button>
                <button type="button" onclick="setQuickPeriod('Sábado (09h às 13h)')" class="period-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-slate-100 hover:bg-teal-50 hover:text-teal border border-slate-200 transition flex items-center gap-1">
                  📅 Sábado
                </button>
              </div>
            </div>"""

if old_date_field in html:
    html = html.replace(old_date_field, new_date_field)
    print("Added quick period selection pills to form!")

# 3. Add Google Maps Location Section for São Paulo - SP Capital
maps_section = """
  <!-- ========================================================================= -->
  <!-- LOCALIZAÇÃO / MAPA DA CAPITAL DE SÃO PAULO                                -->
  <!-- ========================================================================= -->
  <section id="localizacao" class="py-16 sm:py-20 bg-white border-t border-slate-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-teal-100/70 border border-teal-200 text-teal-800 text-xs font-heading font-bold mb-3">
          <i class="fa-solid fa-location-dot text-teal-600"></i>
          <span>Fácil Acesso na Capital de São Paulo</span>
        </div>
        <h2 class="font-heading font-extrabold text-2xl sm:text-3xl lg:text-4xl text-navy-850 tracking-tight">
          Onde estamos localizados
        </h2>
        <p class="text-slate-500 text-xs sm:text-sm mt-2 leading-relaxed">
          Consultório moderno, seguro e de fácil acesso na região nobre de São Paulo (Av. Paulista), a 250m do Metrô Trianon-Masp e com estacionamento conveniado.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        
        <!-- Info Card -->
        <div class="lg:col-span-5 bg-navy-900 rounded-3xl p-6 sm:p-8 text-white shadow-card flex flex-col justify-between space-y-6">
          <div class="space-y-4">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-2xl bg-teal text-white flex items-center justify-center text-lg shadow">
                <i class="fa-solid fa-heart-pulse"></i>
              </div>
              <div>
                <span class="font-heading font-extrabold text-lg text-white block">PODOSAÚDE</span>
                <span class="text-[10px] font-semibold uppercase tracking-wider text-teal-400 block">Podologia Clínica & Laser</span>
              </div>
            </div>

            <div class="space-y-3.5 pt-2 text-xs">
              <div class="flex items-start gap-3">
                <i class="fa-solid fa-map-pin text-teal-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-heading font-bold">Endereço Principal:</strong>
                  <span class="text-slate-300">Av. Paulista, 1000 - Bela Vista / Jardins, São Paulo - SP, CEP 01310-100</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-train-subway text-teal-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-heading font-bold">Acesso por Metrô:</strong>
                  <span class="text-slate-300">Apenas 250 metros da Estação Trianon-Masp (Linha 2 - Verde).</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-square-parking text-teal-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-heading font-bold">Estacionamento Conveniado:</strong>
                  <span class="text-slate-300">Vaga coberta e manobrista no próprio edifício clínico.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-wheelchair text-teal-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-heading font-bold">Acessibilidade Total:</strong>
                  <span class="text-slate-300">Rampas e elevadores modernos adaptados para idosos e mobilidade reduzida.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-regular fa-clock text-teal-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-heading font-bold">Horário de Funcionamento:</strong>
                  <span class="text-slate-300">Segunda a Sexta: 09h às 18h | Sábados: 09h às 13h</span>
                </div>
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-navy-800 flex flex-col sm:flex-row gap-3">
            <a href="https://maps.google.com/?q=Av.+Paulista,+1000+-+Bela+Vista,+S%C3%A3o+Paulo+-+SP" target="_blank" class="flex-1 py-3 px-4 rounded-xl bg-teal hover:bg-clinical text-white text-center font-heading font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 transition shadow">
              <i class="fa-solid fa-route"></i>
              <span>Como Chegar</span>
            </a>
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20gostaria%20de%20tirar%20d%C3%BAvidas%20sobre%20como%20chegar%20%C3%A0%20cl%C3%ADnica%20PODOSA%C3%9ADE%20em%20S%C3%A3o%20Paulo." target="_blank" class="py-3 px-4 rounded-xl bg-white/10 hover:bg-white/20 text-white text-center font-heading font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 transition border border-white/15">
              <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
              <span>Falar no WhatsApp</span>
            </a>
          </div>

        </div>

        <!-- Google Maps Iframe -->
        <div class="lg:col-span-7 rounded-3xl overflow-hidden shadow-card border-4 border-white bg-slate-100 min-h-[380px] lg:min-h-[460px] relative">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.098485293405!2d-46.6549887237894!3d-23.564903378796857!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce59c8da0aa315%3A0xd59f9431f2c9776a!2sAv.%20Paulista%2C%20S%C3%A3o%20Paulo%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" 
            width="100%" 
            height="100%" 
            style="border:0; min-height: 420px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade"
            title="Localização da Clínica PODOSAÚDE em São Paulo - SP"
            class="w-full h-full"
          ></iframe>
        </div>

      </div>

    </div>
  </section>
"""

# Insert Maps Section right before Section 14 (CTA FINAL)
if '<!-- ========================================================================= -->' in html and '14. CTA FINAL' in html:
    html = html.replace(
        '  <!-- ========================================================================= -->\n  <!-- 14. CTA FINAL',
        maps_section + '\n  <!-- ========================================================================= -->\n  <!-- 14. CTA FINAL'
    )
    print("Added Google Maps section for São Paulo Capital!")

# 4. Add Mobile Floating Bottom Sticky Bar for Ultra Fast 1-Click Conversion
mobile_sticky_bar = """
  <!-- ========================================================================= -->
  <!-- MOBILE BOTTOM STICKY BAR (CONVERSÃO EM 1 CLIQUE)                          -->
  <!-- ========================================================================= -->
  <div class="fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 p-2.5 px-4 flex items-center justify-between gap-2.5 sm:hidden shadow-2xl">
    <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o%20na%20PODOSA%C3%9ADE." target="_blank" class="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-heading font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-1.5 shadow">
      <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Rápido
    </a>
    <button onclick="scrollToAppointment()" class="flex-1 py-2.5 rounded-xl bg-navy-850 hover:bg-navy-900 text-white font-heading font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-1.5 shadow">
      <i class="fa-regular fa-calendar-check text-teal-400 text-sm"></i> Agendar Online
    </button>
  </div>
"""

if '<!-- MOBILE BOTTOM STICKY BAR' not in html:
    html = html.replace('  <!-- TOAST NOTIFICATION CONTAINER', mobile_sticky_bar + '\n  <!-- TOAST NOTIFICATION CONTAINER')
    print("Added mobile sticky conversion bar!")

# 5. Add JavaScript helpers: selectServiceAndScroll and setQuickPeriod
js_functions = """
    // Pre-fill Service and Smooth Scroll to Form
    function selectServiceAndScroll(serviceName) {
      const select = document.getElementById('form-service');
      if (select) {
        // Map friendly names to select values
        if (serviceName.includes('Unha')) select.value = 'Unha Encravada';
        else if (serviceName.includes('Calo')) select.value = 'Calos e Calosidades';
        else if (serviceName.includes('Micose') || serviceName.includes('Laser')) select.value = 'Micose e Laser';
        else if (serviceName.includes('Diab')) select.value = 'Pé Diabético';
        else if (serviceName.includes('Avalia')) select.value = 'Avaliação Geral';
        else select.value = 'Outros Cuidados';
      }

      scrollToAppointment();
      showToast('Serviço "' + serviceName + '" selecionado! Preencha seu nome e WhatsApp.');
    }

    function scrollToAppointment() {
      const section = document.getElementById('agendamento');
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
        
        // Highlight form with subtle pulse
        const formBox = section.querySelector('.lg\\\\:col-span-7') || section.querySelector('form');
        if (formBox) {
          formBox.classList.add('ring-4', 'ring-teal/30');
          setTimeout(() => formBox.classList.remove('ring-4', 'ring-teal/30'), 1500);
        }

        // Focus on name input after scroll
        setTimeout(() => {
          const nameInput = document.getElementById('form-name');
          if (nameInput) nameInput.focus();
        }, 600);
      }
    }

    // Set Quick Period in Message/Date
    function setQuickPeriod(periodText) {
      const msgArea = document.getElementById('form-message');
      if (msgArea) {
        const currentMsg = msgArea.value.trim();
        msgArea.value = currentMsg ? currentMsg + ' • Preferência: ' + periodText : 'Preferência de horário: ' + periodText;
      }
      showToast('Período ' + periodText + ' adicionado ao agendamento!');
    }
"""

if 'function selectServiceAndScroll' not in html:
    html = html.replace('    // Appointment Form Submit', js_functions + '\n    // Appointment Form Submit')
    print("Added JavaScript conversion helpers!")

with open('podologo/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("podologo/index.html enhanced with 1-click booking and São Paulo map!")
