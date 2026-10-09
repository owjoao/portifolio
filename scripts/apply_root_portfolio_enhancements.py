# -*- coding: utf-8 -*-
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

root_map_section = """
  <!-- ========================================================================= -->
  <!-- LOCALIZAÇÃO / HUB DE TECNOLOGIA NA CAPITAL DE SÃO PAULO                  -->
  <!-- ========================================================================= -->
  <section id="localizacao" class="py-16 sm:py-24 bg-neutral-950 border-t border-neutral-800/80 text-white relative overflow-hidden">
    <!-- Glow de fundo -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-indigo-600/10 rounded-full blur-[120px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-bold mb-3">
          <i class="fa-solid fa-location-dot text-rose-500"></i>
          <span>Hub de Atendimento na Capital de São Paulo</span>
        </div>
        <h2 class="font-heading font-extrabold text-2xl sm:text-3xl lg:text-4xl text-white tracking-tight">
          Onde estamos localizados
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2 leading-relaxed">
          Nosso escritório executivo de atendimento e desenvolvimento digital fica localizado no coração financeiro de São Paulo (Av. Paulista), a 250m do Metrô Trianon-Masp, com total acessibilidade e conforto.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        
        <!-- Info Card -->
        <div class="lg:col-span-5 bg-[#0C1019] border border-neutral-800 rounded-3xl p-6 sm:p-8 text-white shadow-2xl flex flex-col justify-between space-y-6">
          <div class="space-y-4">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-2xl bg-indigo-600 text-white flex items-center justify-center text-lg shadow-lg shadow-indigo-600/30">
                <i class="fa-solid fa-laptop-code"></i>
              </div>
              <div>
                <span class="font-heading font-extrabold text-lg text-white block">NEXUS FLOW</span>
                <span class="text-[10px] font-semibold uppercase tracking-wider text-cyan-400 block">Soluções Digitais & CRM por Nicho</span>
              </div>
            </div>

            <div class="space-y-3.5 pt-2 text-xs">
              <div class="flex items-start gap-3">
                <i class="fa-solid fa-map-pin text-rose-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Endereço Principal:</strong>
                  <span class="text-slate-400">Av. Paulista, 1000 - Bela Vista / Jardins, São Paulo - SP, CEP 01310-100</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-train-subway text-emerald-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Acesso por Metrô:</strong>
                  <span class="text-slate-400">Apenas 250 metros da Estação Trianon-Masp (Linha 2 - Verde).</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-square-parking text-blue-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Estacionamento Conveniado:</strong>
                  <span class="text-slate-400">Vagas cobertas e manobrista no próprio edifício.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-wheelchair text-amber-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Acessibilidade Total:</strong>
                  <span class="text-slate-400">Rampas e elevadores modernos adaptados para mobilidade reduzida.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-regular fa-clock text-slate-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Horário de Atendimento Executivo:</strong>
                  <span class="text-slate-400">Segunda a Sexta: 08h às 19h | Sábados: 08h às 14h</span>
                </div>
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-neutral-800 flex flex-col sm:flex-row gap-3">
            <a href="https://maps.google.com/?q=Av.+Paulista,+1000+-+Bela+Vista,+S%C3%A3o+Paulo+-+SP" target="_blank" rel="noopener noreferrer" class="flex-1 py-3 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-center font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 transition shadow">
              <i class="fa-solid fa-route"></i>
              <span>Como Chegar</span>
            </a>
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20reuni%C3%A3o%20ou%20visita%20em%20S%C3%A3o%20Paulo." target="_blank" rel="noopener noreferrer" class="py-3 px-4 rounded-xl bg-white/10 hover:bg-white/20 text-white text-center font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 transition border border-white/10">
              <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
              <span>Falar no WhatsApp</span>
            </a>
          </div>

        </div>

        <!-- Google Maps Iframe -->
        <div class="lg:col-span-7 rounded-3xl overflow-hidden shadow-2xl border-2 border-neutral-800 bg-neutral-900 min-h-[380px] lg:min-h-[440px] relative">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.098485293405!2d-46.6549887237894!3d-23.564903378796857!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce59c8da0aa315%3A0xd59f9431f2c9776a!2sAv.%20Paulista%2C%20S%C3%A3o%20Paulo%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" 
            width="100%" 
            height="100%" 
            style="border:0; min-height: 420px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade"
            title="Localização NEXUS FLOW em São Paulo - SP"
            class="w-full h-full"
          ></iframe>
        </div>

      </div>

    </div>
  </section>
"""

root_video_modal = """
  <!-- ========================================================================= -->
  <!-- MODAL: VÍDEO & QUALIDADE DE VIDA (NEXUS FLOW)                             -->
  <!-- ========================================================================= -->
  <div id="video-qv-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4 hidden">
    <div class="bg-neutral-900 text-white rounded-3xl max-w-2xl w-full p-6 sm:p-8 shadow-2xl border border-neutral-800 relative animate-fade-in max-h-[90vh] overflow-y-auto">
      <button onclick="closeVideoQvModal()" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-neutral-800 hover:bg-neutral-700 text-slate-300 flex items-center justify-center transition shadow-sm z-10" title="Fechar">
        <i class="fa-solid fa-xmark text-sm"></i>
      </button>

      <div class="flex items-center gap-2 mb-3">
        <span class="px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5">
          <i class="fa-solid fa-heart-pulse"></i> Qualidade de Vida & Produtividade
        </span>
        <span class="text-xs text-slate-400">• Vídeo Exclusivo</span>
      </div>

      <h3 class="text-xl sm:text-2xl font-extrabold text-white mb-2 leading-tight">
        Mais Tempo Livre e Menos Estresse: Como Nossas Soluções Devolvem sua Qualidade de Vida
      </h3>
      <p class="text-xs sm:text-sm text-slate-300 mb-4 leading-relaxed">
        Descubra no vídeo como landing pages que convertem em poucos cliques e sistemas automatizados eliminam o trabalho braçal e permitem que você foque no que realmente importa: viver melhor.
      </p>
      
      <!-- Video Player Preview -->
      <div class="aspect-video w-full rounded-2xl overflow-hidden relative bg-black shadow-inner group mb-5 border border-neutral-800">
        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent flex flex-col justify-between p-5 z-10">
          <div class="self-end px-2.5 py-1 rounded-lg bg-black/60 backdrop-blur-md text-white text-[11px] font-mono font-semibold">
            <i class="fa-solid fa-clock mr-1 text-emerald-400"></i> 02:10 min • Full HD
          </div>
          <div class="flex items-center gap-4">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20assisti%20ao%20v%C3%ADdeo%20do%20portf%C3%B3lio%20sobre%20qualidade%20de%20vida%20e%20gostaria%20de%20um%20projeto." target="_blank" rel="noopener noreferrer" class="w-14 h-14 rounded-full bg-indigo-600 hover:bg-indigo-500 text-white flex items-center justify-center text-xl shadow-xl hover:scale-110 active:scale-95 transition-all shrink-0">
              <i class="fa-solid fa-play ml-1"></i>
            </a>
            <div>
              <p class="text-white font-bold text-sm sm:text-base leading-snug">Metodologia Flow: Conversão em Poucos Cliques</p>
              <p class="text-emerald-300 text-xs">Menos atrito para o cliente, mais agendamentos e vendas fechadas para você</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 3 Pilares de Qualidade de Vida -->
      <div class="grid grid-cols-3 gap-2 sm:gap-3 py-3 border-y border-neutral-800 mb-5 text-center text-xs">
        <div class="p-2.5 rounded-xl bg-neutral-950/60 border border-neutral-800">
          <i class="fa-solid fa-bolt text-indigo-400 block text-base mb-1"></i>
          <strong class="block text-white text-[11px] font-bold">Fechamento em 2 Cliques</strong>
          <span class="text-[10px] text-slate-400">Sem burocracia</span>
        </div>
        <div class="p-2.5 rounded-xl bg-neutral-950/60 border border-neutral-800">
          <i class="fa-solid fa-mobile-screen-button text-cyan-400 block text-base mb-1"></i>
          <strong class="block text-white text-[11px] font-bold">Mobile First Impecável</strong>
          <span class="text-[10px] text-slate-400">Conversão de palma</span>
        </div>
        <div class="p-2.5 rounded-xl bg-neutral-950/60 border border-neutral-800">
          <i class="fa-solid fa-heart-pulse text-emerald-400 block text-base mb-1"></i>
          <strong class="block text-white text-[11px] font-bold">Mais Tempo Livre</strong>
          <span class="text-[10px] text-slate-400">Paz e previsibilidade</span>
        </div>
      </div>

      <div class="flex flex-col sm:flex-row gap-3">
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20quero%20um%20site%20com%20alta%20convers%C3%A3o%20e%20foco%20em%20qualidade%20de%20vida." target="_blank" rel="noopener noreferrer" class="flex-1 py-3.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition">
          <i class="fa-brands fa-whatsapp text-base"></i> Contratar via WhatsApp Rápido
        </a>
        <button onclick="closeVideoQvModal()" class="py-3.5 px-5 rounded-xl bg-neutral-800 hover:bg-neutral-700 text-white font-bold text-xs uppercase tracking-wider text-center transition">
          Explorar Portfólio
        </button>
      </div>
    </div>
  </div>
"""

root_sticky_bar = """
  <!-- ========================================================================= -->
  <!-- MOBILE BOTTOM STICKY BAR (CONVERSÃO EM 1 CLIQUE)                          -->
  <!-- ========================================================================= -->
  <div class="fixed bottom-0 left-0 right-0 z-40 bg-neutral-950/95 backdrop-blur-md border-t border-neutral-800 p-2.5 px-4 flex items-center justify-between gap-2.5 sm:hidden shadow-2xl">
    <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20quero%20solicitar%20um%20or%C3%A7amento%20para%20o%20meu%20nicho." target="_blank" rel="noopener noreferrer" class="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-1.5 shadow">
      <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Rápido
    </a>
    <button onclick="openVideoQvModal()" class="flex-1 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-1.5 shadow">
      <i class="fa-solid fa-play text-xs"></i> Vídeo Solução
    </button>
  </div>
"""

root_js = """
  <script>
    function openVideoQvModal() {
      const m = document.getElementById('video-qv-modal');
      if (m) m.classList.remove('hidden');
    }
    function closeVideoQvModal() {
      const m = document.getElementById('video-qv-modal');
      if (m) m.classList.add('hidden');
    }
  </script>
"""

# Inject into root index.html
if 'id="localizacao"' not in html:
    html = html.replace('<footer class="border-t border-neutral-800 bg-[#05070B] py-12">', root_map_section + '\n  <footer class="border-t border-neutral-800 bg-[#05070B] py-12">')
    print("Added São Paulo Map Section to root index.html!")

if 'id="video-qv-modal"' not in html:
    html = html.replace('</body>', root_video_modal + '\n' + root_sticky_bar + '\n' + root_js + '\n</body>')
    print("Added Video Qualidade de Vida modal and sticky bar to root index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Root index.html successfully updated!")
