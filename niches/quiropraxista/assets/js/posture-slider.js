/**
 * QuiroLife - Posture & Mobility Educational Interactive Comparison
 * Drag slider revealing difference between daily habitual overload posture
 * and biomechanically aligned functional posture.
 */

class PostureSlider {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;

    this.sliderHandle = this.container.querySelector('.slider-handle');
    this.beforeLayer = this.container.querySelector('.layer-observed');
    this.afterLayer = this.container.querySelector('.layer-aligned');
    this.sliderRange = this.container.querySelector('.slider-input');
    this.metricsHeadWeight = document.getElementById('posture-metric-head');
    this.metricsCurvature = document.getElementById('posture-metric-curve');
    this.metricsDiscs = document.getElementById('posture-metric-discs');
    this.statusLabel = document.getElementById('posture-status-label');

    this.isDragging = false;
    this.currentPosition = 50; // percentage 0 to 100

    this.init();
  }

  init() {
    this.updatePosition(50);
    this.setupEvents();
  }

  updatePosition(percent) {
    percent = Math.max(0, Math.min(100, percent));
    this.currentPosition = percent;

    if (this.beforeLayer) {
      this.beforeLayer.style.clipPath = `polygon(0 0, ${percent}% 0, ${percent}% 100%, 0 100%)`;
    }

    if (this.sliderHandle) {
      this.sliderHandle.style.left = `${percent}%`;
    }

    if (this.sliderRange) {
      this.sliderRange.value = percent;
    }

    // Dynamic educational metrics
    if (percent < 35) {
      // Overload state
      if (this.metricsHeadWeight) this.metricsHeadWeight.innerHTML = '<span class="text-rose-400 font-black">+22 kg</span> <span class="text-slate-400 text-xs">(cabeça projetada a 45°)</span>';
      if (this.metricsCurvature) this.metricsCurvature.innerHTML = '<span class="text-rose-400 font-bold">Hipercifose & Ombros Fechados</span>';
      if (this.metricsDiscs) this.metricsDiscs.innerHTML = '<span class="text-rose-400 font-bold">Sobrecarga discal lombar acentuada</span>';
      if (this.statusLabel) this.statusLabel.textContent = 'Postura Habitual com Sobrecarga Diária';
    } else if (percent > 65) {
      // Aligned state
      if (this.metricsHeadWeight) this.metricsHeadWeight.innerHTML = '<span class="text-emerald-400 font-black">~5 kg</span> <span class="text-slate-400 text-xs">(eixo neutro equilibrado)</span>';
      if (this.metricsCurvature) this.metricsCurvature.innerHTML = '<span class="text-emerald-400 font-bold">Curvaturas fisiológicas livres</span>';
      if (this.metricsDiscs) this.metricsDiscs.innerHTML = '<span class="text-emerald-400 font-bold">Distribuição harmônica de peso</span>';
      if (this.statusLabel) this.statusLabel.textContent = 'Alinhamento Funcional e Mobilidade';
    } else {
      // Transition state
      if (this.metricsHeadWeight) this.metricsHeadWeight.innerHTML = '<span class="text-amber-400 font-black">~12 kg</span> <span class="text-slate-400 text-xs">(inclinação média)</span>';
      if (this.metricsCurvature) this.metricsCurvature.innerHTML = '<span class="text-amber-400 font-bold">Transição de apoio postural</span>';
      if (this.metricsDiscs) this.metricsDiscs.innerHTML = '<span class="text-amber-400 font-bold">Recrutamento postural consciente</span>';
      if (this.statusLabel) this.statusLabel.textContent = 'Arraste para comparar os eixos';
    }
  }

  setupEvents() {
    const onMove = (clientX) => {
      const rect = this.container.getBoundingClientRect();
      const x = clientX - rect.left;
      const percent = (x / rect.width) * 100;
      this.updatePosition(percent);
    };

    if (this.sliderHandle) {
      this.sliderHandle.addEventListener('mousedown', (e) => {
        this.isDragging = true;
        e.preventDefault();
      });

      this.sliderHandle.addEventListener('touchstart', (e) => {
        this.isDragging = true;
      }, { passive: true });
    }

    this.container.addEventListener('mousemove', (e) => {
      if (!this.isDragging) return;
      onMove(e.clientX);
    });

    this.container.addEventListener('touchmove', (e) => {
      if (!this.isDragging || !e.touches.length) return;
      onMove(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('mouseup', () => {
      this.isDragging = false;
    });

    window.addEventListener('touchend', () => {
      this.isDragging = false;
    });

    if (this.sliderRange) {
      this.sliderRange.addEventListener('input', (e) => {
        this.updatePosition(parseFloat(e.target.value));
      });
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.postureSlider = new PostureSlider('posture-comparison-widget');
});
