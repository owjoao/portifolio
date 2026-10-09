# -*- coding: utf-8 -*-
import os
import re
from sites_configs import SITE_CONFIGS

def build_map_section(cfg):
    return f"""
  <!-- ========================================================================= -->
  <!-- LOCALIZAÇÃO / MAPA DA CAPITAL DE SÃO PAULO                                -->
  <!-- ========================================================================= -->
  <section id="localizacao" class="py-16 sm:py-20 bg-white border-t border-slate-100 text-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-slate-700 text-xs font-bold mb-3">
          <i class="fa-solid fa-location-dot text-rose-500"></i>
          <span>Fácil Acesso na Capital de São Paulo</span>
        </div>
        <h2 class="font-bold text-2xl sm:text-3xl lg:text-4xl text-slate-900 tracking-tight">
          Onde estamos localizados
        </h2>
        <p class="text-slate-500 text-xs sm:text-sm mt-2 leading-relaxed">
          {cfg['desc']}
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        
        <!-- Info Card -->
        <div class="lg:col-span-5 bg-slate-900 rounded-3xl p-6 sm:p-8 text-white shadow-xl flex flex-col justify-between space-y-6">
          <div class="space-y-4">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-2xl bg-white/10 text-white flex items-center justify-center text-lg shadow border border-white/10">
                <i class="fa-solid {cfg['icon']}"></i>
              </div>
              <div>
                <span class="font-bold text-lg text-white block">{cfg['name']}</span>
                <span class="text-[10px] font-semibold uppercase tracking-wider text-slate-300 block">{cfg['tag']}</span>
              </div>
            </div>

            <div class="space-y-3.5 pt-2 text-xs">
              <div class="flex items-start gap-3">
                <i class="fa-solid fa-map-pin text-rose-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Endereço Principal:</strong>
                  <span class="text-slate-300">Av. Paulista, 1000 - Bela Vista / Jardins, São Paulo - SP, CEP 01310-100</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-train-subway text-emerald-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Acesso por Metrô:</strong>
                  <span class="text-slate-300">Apenas 250 metros da Estação Trianon-Masp (Linha 2 - Verde).</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-square-parking text-blue-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Estacionamento Conveniado:</strong>
                  <span class="text-slate-300">Vaga coberta e manobrista no próprio edifício com comodidade.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-solid fa-wheelchair text-amber-400 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Acessibilidade Total:</strong>
                  <span class="text-slate-300">Rampas e elevadores modernos adaptados para idosos e mobilidade reduzida.</span>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <i class="fa-regular fa-clock text-slate-300 text-sm mt-0.5 shrink-0"></i>
                <div>
                  <strong class="text-white block font-bold">Horário de Funcionamento:</strong>
                  <span class="text-slate-300">Segunda a Sexta: 08h às 19h | Sábados: 08h às 14h</span>
                </div>
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-800 flex flex-col sm:flex-row gap-3">
            <a href="https://maps.google.com/?q=Av.+Paulista,+1000+-+Bela+Vista,+S%C3%A3o+Paulo+-+SP" target="_blank" rel="noopener noreferrer" class="flex-1 py-3 px-4 rounded-xl {cfg['btn_bg']} text-white text-center font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 transition shadow">
              <i class="fa-solid fa-route"></i>
              <span>Como Chegar</span>
            </a>
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20gostaria%20de%20informa%C3%A7%C3%B5es%20sobre%20a%20localiza%C3%A7%C3%A3o%20em%20S%C3%A3o%20Paulo%20({cfg['name']})." target="_blank" rel="noopener noreferrer" class="py-3 px-4 rounded-xl bg-white/10 hover:bg-white/20 text-white text-center font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 transition border border-white/15">
              <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
              <span>WhatsApp</span>
            </a>
          </div>

        </div>

        <!-- Google Maps Iframe -->
        <div class="lg:col-span-7 rounded-3xl overflow-hidden shadow-xl border-4 border-white bg-slate-100 min-h-[380px] lg:min-h-[440px] relative">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.098485293405!2d-46.6549887237894!3d-23.564903378796857!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce59c8da0aa315%3A0xd59f9431f2c9776a!2sAv.%20Paulista%2C%20S%C3%A3o%20Paulo%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" 
            width="100%" 
            height="100%" 
            style="border:0; min-height: 420px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade"
            title="Localização {cfg['name']} em São Paulo - SP"
            class="w-full h-full"
          ></iframe>
        </div>

      </div>

    </div>
  </section>
"""

def build_video_modal(cfg):
    return f"""
  <!-- ========================================================================= -->
  <!-- MODAL: VÍDEO & QUALIDADE DE VIDA                                          -->
  <!-- ========================================================================= -->
  <div id="video-qv-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4 hidden">
    <div class="bg-white text-slate-900 rounded-3xl max-w-2xl w-full p-6 sm:p-8 shadow-2xl border border-slate-200 relative animate-fade-in max-h-[90vh] overflow-y-auto">
      <button onclick="closeVideoQvModal()" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center transition shadow-sm z-10" title="Fechar">
        <i class="fa-solid fa-xmark text-sm"></i>
      </button>

      <div class="flex items-center gap-2 mb-3">
        <span class="px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5">
          <i class="fa-solid fa-heart-pulse"></i> Qualidade de Vida & Bem-Estar
        </span>
        <span class="text-xs text-slate-400">• Vídeo Exclusivo</span>
      </div>

      <h3 class="text-xl sm:text-2xl font-extrabold text-slate-900 mb-2 leading-tight">
        {cfg['qv_title']}
      </h3>
      <p class="text-xs sm:text-sm text-slate-600 mb-4 leading-relaxed">
        {cfg['qv_desc']}
      </p>
      
      <!-- Video Player Preview -->
      <div class="aspect-video w-full rounded-2xl overflow-hidden relative bg-slate-950 shadow-inner group mb-5">
        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent flex flex-col justify-between p-5 z-10">
          <div class="self-end px-2.5 py-1 rounded-lg bg-black/60 backdrop-blur-md text-white text-[11px] font-mono font-semibold">
            <i class="fa-solid fa-clock mr-1 text-emerald-400"></i> 01:45 min • Full HD
          </div>
          <div class="flex items-center gap-4">
            <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20assisti%20ao%20v%C3%ADdeo%20sobre%20qualidade%20de%20vida%20e%20quero%20mais%20informa%C3%A7%C3%B5es%20({cfg['name']})." target="_blank" rel="noopener noreferrer" class="w-14 h-14 rounded-full bg-emerald-500 hover:bg-emerald-400 text-white flex items-center justify-center text-xl shadow-xl hover:scale-110 active:scale-95 transition-all shrink-0">
              <i class="fa-solid fa-play ml-1"></i>
            </a>
            <div>
              <p class="text-white font-bold text-sm sm:text-base leading-snug">Metodologia Focada no seu Bem-Estar</p>
              <p class="text-emerald-300 text-xs">{cfg['qv_sub']}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 3 Pilares de Qualidade de Vida -->
      <div class="grid grid-cols-3 gap-2 sm:gap-3 py-3 border-y border-slate-100 mb-5 text-center text-xs">
        <div class="p-2.5 rounded-xl bg-slate-50">
          <i class="fa-solid fa-clock-rotate-left text-emerald-600 block text-base mb-1"></i>
          <strong class="block text-slate-800 text-[11px] font-bold">Sem Fila e Sem Espera</strong>
          <span class="text-[10px] text-slate-500">Respeito ao seu tempo</span>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50">
          <i class="fa-solid fa-shield-halved text-emerald-600 block text-base mb-1"></i>
          <strong class="block text-slate-800 text-[11px] font-bold">Segurança & Conforto</strong>
          <span class="text-[10px] text-slate-500">Ambiente acolhedor</span>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50">
          <i class="fa-solid fa-bolt text-emerald-600 block text-base mb-1"></i>
          <strong class="block text-slate-800 text-[11px] font-bold">Fechamento em 1 Clique</strong>
          <span class="text-[10px] text-slate-500">Sem burocracia</span>
        </div>
      </div>

      <div class="flex flex-col sm:flex-row gap-3">
        <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20quero%20fechar%20meu%20atendimento%20com%20prioridade%20e%20foco%20em%20qualidade%20de%20vida%20({cfg['name']})." target="_blank" rel="noopener noreferrer" class="flex-1 py-3.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 shadow-lg transition">
          <i class="fa-brands fa-whatsapp text-base"></i> Fechar no WhatsApp com Prioridade
        </a>
        <button onclick="closeVideoQvModal(); scrollToFormFast();" class="py-3.5 px-5 rounded-xl bg-slate-900 hover:bg-black text-white font-bold text-xs uppercase tracking-wider text-center transition">
          Preencher Formulário Online
        </button>
      </div>
    </div>
  </div>
"""

def build_mobile_sticky(cfg):
    return f"""
  <!-- ========================================================================= -->
  <!-- MOBILE BOTTOM STICKY BAR (CONVERSÃO EM 1 CLIQUE)                          -->
  <!-- ========================================================================= -->
  <div class="fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 p-2.5 px-4 flex items-center justify-between gap-2.5 sm:hidden shadow-2xl">
    <a href="https://wa.me/5532999292311?text=Ol%C3%A1%2C%20gostaria%20de%20fechar%20meu%20atendimento%20com%20rapidez%20({cfg['name']})." target="_blank" rel="noopener noreferrer" class="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-1.5 shadow">
      <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Rápido
    </a>
    <button onclick="scrollToFormFast()" class="flex-1 py-2.5 rounded-xl bg-slate-900 hover:bg-black text-white font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-1.5 shadow">
      <i class="fa-regular fa-calendar-check text-emerald-400 text-sm"></i> Fechar Online
    </button>
  </div>
"""

def build_js_helpers(cfg):
    anchor = cfg.get('form_anchor', '#contato').replace('#', '')
    form_id = cfg.get('target_form_id', '')
    return f"""
  <!-- JS HELPERS: VÍDEO QUALIDADE DE VIDA & 1-CLICK CONVERSION -->
  <script>
    function openVideoQvModal() {{
      const m = document.getElementById('video-qv-modal');
      if (m) m.classList.remove('hidden');
    }}

    function closeVideoQvModal() {{
      const m = document.getElementById('video-qv-modal');
      if (m) m.classList.add('hidden');
    }}

    function scrollToFormFast(serviceName) {{
      let target = document.getElementById('{anchor}') || document.getElementById('agendamento') || document.getElementById('contato') || document.getElementById('simulador') || document.querySelector('form');
      if (target) {{
        target.scrollIntoView({{ behavior: 'smooth' }});
        target.classList.add('ring-4', 'ring-emerald-400/50');
        setTimeout(() => target.classList.remove('ring-4', 'ring-emerald-400/50'), 1500);

        setTimeout(() => {{
          const input = target.querySelector('input:not([type="hidden"])') || document.querySelector('input[type="text"], input[type="tel"]');
          if (input) input.focus();
        }}, 600);
      }} else {{
        window.location.href = "https://wa.me/5532999292311?text=Ol%C3%A1%2C%20gostaria%20de%20fechar%20com%20poucos%20cliques%20({cfg['name']}).";
      }}
    }}
  </script>
"""
