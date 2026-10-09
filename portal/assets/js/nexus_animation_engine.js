/**
 * ============================================================================
 * NEXUS FLOW — MASTER ANIMATION ENGINE
 * Orchestrates: Three.js (3D Space) + GSAP (Cinematic & ScrollTrigger)
 *              + Motion (Spring Physics & Progress) + Anime.js (SVG Circuit)
 * ============================================================================
 */

(function () {
  'use strict';

  // --- 1. Top Reading Scroll Progress Bar via Motion (motion.dev) ---
  function initScrollProgressBar() {
    try {
      const bar = document.createElement('div');
      bar.id = 'nexus-scroll-bar';
      bar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        width: 100%;
        background: linear-gradient(90deg, #06b6d4, #10b981);
        transform-origin: 0 50%;
        transform: scaleX(0);
        z-index: 9999;
        pointer-events: none;
      `;
      document.body.appendChild(bar);

      if (window.Motion && typeof window.Motion.scroll === 'function') {
        window.Motion.scroll(window.Motion.animate(bar, { scaleX: [0, 1] }, { ease: 'linear' }));
      } else {
        window.addEventListener('scroll', () => {
          const max = document.documentElement.scrollHeight - window.innerHeight;
          const progress = max > 0 ? window.scrollY / max : 0;
          bar.style.transform = `scaleX(${progress})`;
        }, { passive: true });
      }
    } catch (e) {
      console.warn('Scroll bar init fallback:', e);
    }
  }

  // --- 2. Three.js: 3D Spatial Constellation in Hero Banner ---
  function initThreeJsHero() {
    const container = document.getElementById('hero-threejs-container');
    if (!container || typeof THREE === 'undefined') return;

    try {
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
      camera.position.z = 80;

      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'high-performance' });
      renderer.setSize(container.clientWidth, container.clientHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      container.appendChild(renderer.domElement);

      // Create Particle Constellation
      const particleCount = window.innerWidth < 768 ? 200 : 550;
      const geometry = new THREE.BufferGeometry();
      const positions = new Float32Array(particleCount * 3);
      const colors = new Float32Array(particleCount * 3);

      const colorCyan = new THREE.Color(0x06b6d4);
      const colorEmerald = new THREE.Color(0x10b981);
      const colorWhite = new THREE.Color(0xffffff);

      for (let i = 0; i < particleCount; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 160;
        positions[i * 3 + 1] = (Math.random() - 0.5) * 120;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 100;

        const rand = Math.random();
        const chosen = rand > 0.6 ? colorCyan : (rand > 0.25 ? colorEmerald : colorWhite);
        colors[i * 3] = chosen.r;
        colors[i * 3 + 1] = chosen.g;
        colors[i * 3 + 2] = chosen.b;
      }

      geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      // Circular particle texture generator
      const canvas = document.createElement('canvas');
      canvas.width = 16;
      canvas.height = 16;
      const ctx = canvas.getContext('2d');
      const grad = ctx.createRadialGradient(8, 8, 0, 8, 8, 8);
      grad.addColorStop(0, 'rgba(255,255,255,1)');
      grad.addColorStop(0.5, 'rgba(6,182,212,0.6)');
      grad.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 16, 16);
      const texture = new THREE.CanvasTexture(canvas);

      const material = new THREE.PointsMaterial({
        size: 2.2,
        map: texture,
        transparent: true,
        vertexColors: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      const points = new THREE.Points(geometry, material);
      scene.add(points);

      // Subtle mouse interaction
      let mouseX = 0, mouseY = 0;
      let targetX = 0, targetY = 0;
      window.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX - window.innerWidth / 2) * 0.0008;
        mouseY = (e.clientY - window.innerHeight / 2) * 0.0008;
      }, { passive: true });

      // Viewport culling with IntersectionObserver (0% GPU when out of view)
      let isVisible = true;
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          isVisible = entry.isIntersecting;
        });
      }, { threshold: 0.1 });
      observer.observe(container);

      let animId;
      function animate() {
        if (isVisible) {
          targetX += (mouseX - targetX) * 0.05;
          targetY += (mouseY - targetY) * 0.05;

          points.rotation.y += 0.001;
          points.rotation.x += 0.0005;
          points.rotation.y += targetX * 0.2;
          points.rotation.x += targetY * 0.2;

          renderer.render(scene, camera);
        }
        animId = requestAnimationFrame(animate);
      }
      animate();

      window.addEventListener('resize', () => {
        if (!container) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
      }, { passive: true });

    } catch (e) {
      console.warn('Three.js hero setup skipped or errored:', e);
    }
  }

  // --- 3. GSAP & ScrollTrigger: Timelines & Magnetic Buttons ---
  function initGsapCinematics() {
    if (typeof gsap === 'undefined') return;

    try {
      if (typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
      }

      // Hero Entrance Timeline
      const heroTl = gsap.timeline({ defaults: { ease: 'power3.out' } });
      heroTl.from('#hero .display-title', { opacity: 0, y: 30, duration: 0.8, delay: 0.1 })
            .from('#hero p.text-body-lead', { opacity: 0, y: 20, duration: 0.6 }, '-=0.5')
            .from('#hero .btn-nexus-primary, #hero .btn-nexus-secondary', { opacity: 0, scale: 0.95, stagger: 0.1, duration: 0.5 }, '-=0.3');

      // Magnetic Buttons
      document.querySelectorAll('.magnetic-btn').forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
          const rect = btn.getBoundingClientRect();
          const x = e.clientX - rect.left - rect.width / 2;
          const y = e.clientY - rect.top - rect.height / 2;
          gsap.to(btn, { x: x * 0.25, y: y * 0.25, duration: 0.3, ease: 'power2.out' });
        });
        btn.addEventListener('mouseleave', () => {
          gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.4)' });
        });
      });

      // Staggered Reveals for Problem & Process
      if (typeof ScrollTrigger !== 'undefined') {
        gsap.utils.toArray('.flow-step-card').forEach((card, idx) => {
          gsap.from(card, {
            scrollTrigger: {
              trigger: card,
              start: 'top 88%',
              toggleActions: 'play none none none'
            },
            opacity: 0,
            y: 35,
            duration: 0.6,
            delay: idx * 0.1,
            ease: 'power2.out'
          });
        });
      }

    } catch (e) {
      console.warn('GSAP initialization fallback:', e);
    }
  }

  // --- 4. Motion (motion.dev): Real Spring Physics on Cards ---
  function initMotionSprings() {
    try {
      const cards = document.querySelectorAll('.portfolio-item-card');
      cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
          if (window.Motion && typeof window.Motion.animate === 'function') {
            window.Motion.animate(card, { y: -6, scale: 1.01 }, {
              easing: [0.34, 1.56, 0.64, 1], // Spring curve
              duration: 0.35
            });
          }
        });
        card.addEventListener('mouseleave', () => {
          if (window.Motion && typeof window.Motion.animate === 'function') {
            window.Motion.animate(card, { y: 0, scale: 1 }, {
              easing: [0.16, 1, 0.3, 1],
              duration: 0.3
            });
          }
        });
      });
    } catch (e) {
      console.warn('Motion spring physics fallback:', e);
    }
  }

  // --- 5. Anime.js: SVG Circuit Electricity & Radial Ripples ---
  function initAnimeCircuits() {
    if (typeof anime === 'undefined') return;

    try {
      const pulsePath = document.getElementById('circuit-wire-pulse');
      if (pulsePath) {
        anime({
          targets: pulsePath,
          strokeDashoffset: [anime.setDashoffset, 0],
          easing: 'easeInOutSine',
          duration: 3500,
          direction: 'alternate',
          loop: true
        });
      }

      // Radial ripples on filter buttons
      document.querySelectorAll('.portfolio-filter-pill').forEach(btn => {
        btn.addEventListener('click', (e) => {
          anime({
            targets: btn,
            scale: [0.94, 1],
            duration: 250,
            easing: 'easeOutElastic(1, .8)'
          });
        });
      });

    } catch (e) {
      console.warn('Anime.js circuit line setup fallback:', e);
    }
  }

  // --- Initialization on DOM Ready ---
  document.addEventListener('DOMContentLoaded', () => {
    initScrollProgressBar();
    initThreeJsHero();
    initGsapCinematics();
    initMotionSprings();
    initAnimeCircuits();
    console.log('⚡ NEXUS FLOW Master Animation Suite Initialized (Three.js + GSAP + Motion + Anime.js)');
  });

})();

