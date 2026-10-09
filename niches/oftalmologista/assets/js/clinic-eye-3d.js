/**
 * CLINIC EYE 3D - Instrumento Óptico Interativo em Three.js
 * 
 * Renderiza um olho anatômico/óptico estilizado com:
 * - Córnea translúcida com reflexo especular
 * - Íris com relevo óptico, gradiente de cores institucionais (Deep Navy, Cyan, Aqua)
 * - Pupila reativa com microcontração
 * - Anéis de aberrometria / topografia corneana concêntricos
 * - Retículo de diagnóstico médico sutil
 * - Parallax suave respondendo ao cursor do usuário
 * - Pausa automática de renderização fora do viewport (IntersectionObserver)
 * - Fallback elegante para dispositivos sem WebGL
 */

(function () {
  const container = document.getElementById("hero-eye-canvas-container");
  if (!container) return;

  // Verificação de suporte a WebGL
  function hasWebGL() {
    try {
      const canvas = document.createElement("canvas");
      return !!(window.WebGLRenderingContext && (canvas.getContext("webgl") || canvas.getContext("experimental-webgl")));
    } catch (e) {
      return false;
    }
  }

  if (!hasWebGL() || typeof THREE === "undefined") {
    renderFallbackSVG(container);
    return;
  }

  let scene, camera, renderer, eyeGroup, corneaMesh, irisMesh, pupilMesh, ringsGroup, reticleGroup;
  let targetRotation = { x: 0, y: 0 };
  let currentRotation = { x: 0, y: 0 };
  let isVisible = true;
  let animationFrameId = null;

  function init() {
    const width = container.clientWidth || 500;
    const height = container.clientHeight || 500;

    // Cena
    scene = new THREE.Scene();

    // Câmera
    camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 100);
    camera.position.set(0, 0, 7.5);

    // Renderer com dpr controlado para máxima performance a 60 FPS
    renderer = new THREE.WebGLRenderer({
      alpha: true,
      antialias: true,
      powerPreference: "high-performance"
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.15;
    container.appendChild(renderer.domElement);

    // Grupo principal do Olho
    eyeGroup = new THREE.Group();
    scene.add(eyeGroup);

    // 1. Esclera (Globo Ocular Externo)
    const scleraGeo = new THREE.SphereGeometry(2.2, 48, 48);
    const scleraMat = new THREE.MeshPhysicalMaterial({
      color: 0x071521,
      emissive: 0x040D14,
      roughness: 0.25,
      metalness: 0.1,
      clearcoat: 0.8,
      clearcoatRoughness: 0.2
    });
    const scleraMesh = new THREE.Mesh(scleraGeo, scleraMat);
    eyeGroup.add(scleraMesh);

    // 2. Íris Anatômica Texturizada Proceduralmente
    const irisCanvas = document.createElement("canvas");
    irisCanvas.width = 1024;
    irisCanvas.height = 1024;
    const ctx = irisCanvas.getContext("2d");
    
    // Desenhar textura da íris com fibras radiais
    const cx = 512, cy = 512;
    const grad = ctx.createRadialGradient(cx, cy, 50, cx, cy, 512);
    grad.addColorStop(0, "#030A12");
    grad.addColorStop(0.2, "#0B2230");
    grad.addColorStop(0.5, "#1C8F9C");
    grad.addColorStop(0.78, "#35C7D8");
    grad.addColorStop(0.92, "#79E3E8");
    grad.addColorStop(1, "#071521");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 1024, 1024);

    // Fibras radiais ópticas
    ctx.lineWidth = 1.5;
    for (let i = 0; i < 360; i += 0.8) {
      const angle = (i * Math.PI) / 180;
      const length = 200 + Math.sin(i * 12) * 60 + Math.random() * 80;
      const alpha = 0.15 + Math.random() * 0.35;
      ctx.strokeStyle = `rgba(121, 227, 232, ${alpha})`;
      ctx.beginPath();
      ctx.moveTo(cx + Math.cos(angle) * 120, cy + Math.sin(angle) * 120);
      ctx.lineTo(cx + Math.cos(angle) * (120 + length), cy + Math.sin(angle) * (120 + length));
      ctx.stroke();
    }

    // Anéis da íris
    ctx.strokeStyle = "rgba(53, 199, 216, 0.4)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(cx, cy, 280, 0, Math.PI * 2);
    ctx.stroke();

    const irisTexture = new THREE.CanvasTexture(irisCanvas);
    irisTexture.needsUpdate = true;

    // Geometria da Íris (disco ligeiramente curvado para trás)
    const irisGeo = new THREE.CircleGeometry(1.28, 48);
    const irisMat = new THREE.MeshStandardMaterial({
      map: irisTexture,
      roughness: 0.3,
      metalness: 0.15,
      bumpScale: 0.05
    });
    irisMesh = new THREE.Mesh(irisGeo, irisMat);
    irisMesh.position.set(0, 0, 1.82);
    eyeGroup.add(irisMesh);

    // 3. Pupila Reativa
    const pupilGeo = new THREE.CircleGeometry(0.42, 36);
    const pupilMat = new THREE.MeshBasicMaterial({ color: 0x02060B });
    pupilMesh = new THREE.Mesh(pupilGeo, pupilMat);
    pupilMesh.position.set(0, 0, 1.84);
    eyeGroup.add(pupilMesh);

    // 4. Córnea Translúcida com Domo de Luz
    const corneaGeo = new THREE.SphereGeometry(1.42, 48, 32, 0, Math.PI * 2, 0, Math.PI / 2.3);
    const corneaMat = new THREE.MeshPhysicalMaterial({
      color: 0xEEF5F5,
      transparent: true,
      opacity: 0.28,
      roughness: 0.05,
      metalness: 0.05,
      transmission: 0.9,
      ior: 1.376, // Índice de refração real da córnea humana
      clearcoat: 1.0,
      clearcoatRoughness: 0.05,
      depthWrite: false
    });
    corneaMesh = new THREE.Mesh(corneaGeo, corneaMat);
    corneaMesh.position.set(0, 0, 1.25);
    eyeGroup.add(corneaMesh);

    // 5. Anéis Concêntricos de Topografia / Aberrometria Corneana
    ringsGroup = new THREE.Group();
    const ringRadii = [1.55, 1.85, 2.15, 2.45];
    ringRadii.forEach((r, idx) => {
      const ringGeo = new THREE.RingGeometry(r, r + 0.015, 64);
      const ringMat = new THREE.MeshBasicMaterial({
        color: idx % 2 === 0 ? 0x35C7D8 : 0x1C8F9C,
        transparent: true,
        opacity: 0.22 - idx * 0.04,
        side: THREE.DoubleSide
      });
      const ringMesh = new THREE.Mesh(ringGeo, ringMat);
      ringMesh.position.set(0, 0, 1.5 - idx * 0.1);
      ringsGroup.add(ringMesh);
    });
    eyeGroup.add(ringsGroup);

    // 6. Retículo Médico & Eixo Visual de Precisão
    reticleGroup = new THREE.Group();
    
    // Linhas de retículo sutil
    const lineMat = new THREE.LineBasicMaterial({
      color: 0x35C7D8,
      transparent: true,
      opacity: 0.35
    });

    const crossGeoX = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(-1.8, 0, 1.86),
      new THREE.Vector3(1.8, 0, 1.86)
    ]);
    const crossLineX = new THREE.Line(crossGeoX, lineMat);
    reticleGroup.add(crossLineX);

    const crossGeoY = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(0, -1.8, 1.86),
      new THREE.Vector3(0, 1.8, 1.86)
    ]);
    const crossLineY = new THREE.Line(crossGeoY, lineMat);
    reticleGroup.add(crossLineY);

    // Pequenos marcadores de coordenada nos 4 polos
    const markerGeo = new THREE.RingGeometry(0.04, 0.07, 16);
    const markerMat = new THREE.MeshBasicMaterial({ color: 0x79E3E8, side: THREE.DoubleSide });
    
    [
      { x: 1.3, y: 0 },
      { x: -1.3, y: 0 },
      { x: 0, y: 1.3 },
      { x: 0, y: -1.3 }
    ].forEach(pos => {
      const marker = new THREE.Mesh(markerGeo, markerMat);
      marker.position.set(pos.x, pos.y, 1.86);
      reticleGroup.add(marker);
    });

    eyeGroup.add(reticleGroup);

    // 7. Iluminação Clínica Refinada
    const ambientLight = new THREE.AmbientLight(0x0B2230, 1.8);
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0x79E3E8, 2.4);
    keyLight.position.set(3, 4, 5);
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0x1C8F9C, 1.2);
    fillLight.position.set(-4, -2, 3);
    scene.add(fillLight);

    const rimLight = new THREE.PointLight(0x35C7D8, 1.5, 12);
    rimLight.position.set(0, 0, 3.8);
    scene.add(rimLight);

    // Eventos de Cursor e Redimensionamento
    setupInteractivity();
    setupResize();
    setupVisibilityObserver();

    // Loop
    animate();
  }

  function setupInteractivity() {
    const heroSection = document.querySelector("#hero-section") || container;

    window.addEventListener("mousemove", (e) => {
      if (!isVisible) return;
      const rect = container.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;

      // Movimento angular suave baseado no cursor (limitado a ângulos médicos elegantes)
      const mouseX = (e.clientX - centerX) / (window.innerWidth / 2);
      const mouseY = (e.clientY - centerY) / (window.innerHeight / 2);

      targetRotation.y = THREE.MathUtils.clamp(mouseX * 0.45, -0.4, 0.4);
      targetRotation.x = THREE.MathUtils.clamp(mouseY * 0.35, -0.3, 0.3);

      // Microcontração da pupila em resposta ao foco do mouse
      const distFromCenter = Math.hypot(mouseX, mouseY);
      if (pupilMesh) {
        const pupilScale = THREE.MathUtils.lerp(0.85, 1.15, THREE.MathUtils.clamp(distFromCenter, 0, 1));
        pupilMesh.scale.set(pupilScale, pupilScale, 1);
      }
    });

    // Touch suave para mobile / tablets
    window.addEventListener("touchmove", (e) => {
      if (!isVisible || !e.touches[0]) return;
      const touch = e.touches[0];
      const rect = container.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;

      const mouseX = (touch.clientX - centerX) / (window.innerWidth / 2);
      const mouseY = (touch.clientY - centerY) / (window.innerHeight / 2);

      targetRotation.y = THREE.MathUtils.clamp(mouseX * 0.3, -0.25, 0.25);
      targetRotation.x = THREE.MathUtils.clamp(mouseY * 0.25, -0.2, 0.2);
    }, { passive: true });
  }

  function setupResize() {
    window.addEventListener("resize", () => {
      if (!container || !renderer || !camera) return;
      const width = container.clientWidth;
      const height = container.clientHeight;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    });
  }

  function setupVisibilityObserver() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        isVisible = entry.isIntersecting;
        if (isVisible && !animationFrameId) {
          animate();
        }
      });
    }, { threshold: 0.05 });

    observer.observe(container);
  }

  function animate() {
    if (!isVisible) {
      animationFrameId = null;
      return;
    }

    animationFrameId = requestAnimationFrame(animate);

    // Interpolação amortecida tipo gimbal de precisão óptica
    currentRotation.x += (targetRotation.x - currentRotation.x) * 0.06;
    currentRotation.y += (targetRotation.y - currentRotation.y) * 0.06;

    if (eyeGroup) {
      // Flutuação microscópica natural
      const time = performance.now() * 0.001;
      const microDriftX = Math.sin(time * 0.7) * 0.02;
      const microDriftY = Math.cos(time * 0.9) * 0.02;

      eyeGroup.rotation.x = currentRotation.x + microDriftX;
      eyeGroup.rotation.y = currentRotation.y + microDriftY;
    }

    // Rotação sutil dos anéis de aberrometria
    if (ringsGroup) {
      ringsGroup.rotation.z += 0.0015;
    }

    if (reticleGroup) {
      reticleGroup.rotation.z -= 0.0008;
    }

    renderer.render(scene, camera);
  }

  function renderFallbackSVG(target) {
    target.innerHTML = `
      <div class="relative w-full h-full flex items-center justify-center p-8">
        <svg class="w-72 h-72 animate-pulse" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="100" cy="100" r="90" stroke="#1C8F9C" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.4"/>
          <circle cx="100" cy="100" r="70" stroke="#35C7D8" stroke-width="2" opacity="0.6"/>
          <circle cx="100" cy="100" r="50" fill="#0B2230" stroke="#79E3E8" stroke-width="2"/>
          <circle cx="100" cy="100" r="24" fill="#071521"/>
          <circle cx="110" cy="90" r="6" fill="#F7FAFA" opacity="0.8"/>
          <line x1="10" y1="100" x2="190" y2="100" stroke="#35C7D8" stroke-width="0.75" opacity="0.4"/>
          <line x1="100" y1="10" x2="100" y2="190" stroke="#35C7D8" stroke-width="0.75" opacity="0.4"/>
        </svg>
      </div>
    `;
  }

  // Inicializar quando o DOM estiver pronto
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
