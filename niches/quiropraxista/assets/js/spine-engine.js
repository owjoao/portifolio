/**
 * QuiroLife - 3D Interactive Spine Engine
 * Built with Three.js with complete fallback, smooth damping, raycasting,
 * and regional focus (Cervical, Torácica, Lombar, Sacral).
 */

class SpineViewer {
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      console.warn(`SpineViewer: container #${containerId} not found.`);
      return;
    }

    this.options = Object.assign({
      interactive: true,
      autoRotate: true,
      autoRotateSpeed: 0.003,
      allowDrag: true,
      fov: 42,
      onRegionSelect: null,
      onRegionHover: null,
      fallbackId: 'spine-fallback'
    }, options);

    this.regions = {
      cervical: { name: 'Cervical', range: [0, 6], cameraY: 2.2, cameraZ: 5.5, targetY: 2.1, desc: 'C1 a C7: Suporte craniano, flexibilidade e rotação do pescoço.' },
      toracica: { name: 'Torácica', range: [7, 18], cameraY: 0.6, cameraZ: 6.2, targetY: 0.5, desc: 'T1 a T12: Proteção torácica, estabilidade e ancoragem das costelas.' },
      lombar: { name: 'Lombar', range: [19, 23], cameraY: -1.2, cameraZ: 5.8, targetY: -1.3, desc: 'L1 a L5: Suporte da carga corporal, distribuição de peso e mobilidade do tronco.' },
      sacral: { name: 'Sacral', range: [24, 25], cameraY: -2.7, cameraZ: 5.2, targetY: -2.8, desc: 'Sacro e Cóccix: Conexão com a bacia, centro de gravidade e base estrutural.' }
    };

    this.activeRegion = null;
    this.hoveredRegion = null;
    this.isDragging = false;
    this.previousMousePosition = { x: 0, y: 0 };
    this.targetRotation = { x: 0, y: 0 };
    this.currentRotation = { x: 0, y: 0 };
    this.targetCamera = { y: 0, z: 8.5 };
    this.currentCamera = { y: 0, z: 8.5 };
    this.targetLookAtY = -0.2;
    this.currentLookAtY = -0.2;
    this.mouse = { x: 0, y: 0 };
    this.vertebraeMeshes = [];
    this.discMeshes = [];
    this.hotspotObjects = [];
    this.isVisible = true;
    this.hasInteracted = false;

    this.init();
  }

  isWebGLSupported() {
    try {
      const canvas = document.createElement('canvas');
      return !!(window.WebGLRenderingContext && (canvas.getContext('webgl') || canvas.getContext('experimental-webgl')));
    } catch (e) {
      return false;
    }
  }

  init() {
    if (!this.isWebGLSupported() || typeof THREE === 'undefined') {
      this.showFallback();
      return;
    }

    try {
      this.setupScene();
      this.createSpineGeometry();
      this.createHotspots();
      this.setupLights();
      this.setupEvents();
      this.setupObserver();
      this.animate();
    } catch (err) {
      console.error('Error initializing 3D spine:', err);
      this.showFallback();
    }
  }

  showFallback() {
    const fallback = document.getElementById(this.options.fallbackId);
    if (fallback) {
      fallback.classList.remove('hidden');
    }
    if (this.container) {
      const canvas = this.container.querySelector('canvas');
      if (canvas) canvas.style.display = 'none';
    }
  }

  setupScene() {
    const width = this.container.clientWidth || 400;
    const height = this.container.clientHeight || 550;

    this.scene = new THREE.Scene();
    this.scene.fog = new THREE.FogExp2(0x07111E, 0.05);

    this.camera = new THREE.PerspectiveCamera(this.options.fov, width / height, 0.1, 100);
    this.camera.position.set(0, 0, 8.5);

    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.25;

    this.container.innerHTML = '';
    this.container.appendChild(this.renderer.domElement);

    this.mainGroup = new THREE.Group();
    this.scene.add(this.mainGroup);

    this.raycaster = new THREE.Raycaster();
  }

  setupLights() {
    // Ambient light - Deep cool blue
    const ambientLight = new THREE.AmbientLight(0x0E1E33, 1.4);
    this.scene.add(ambientLight);

    // Main key light - Crisp cool white
    const keyLight = new THREE.DirectionalLight(0xF8FAFC, 1.8);
    keyLight.position.set(4, 6, 6);
    this.scene.add(keyLight);

    // Rim light 1 - Signature Cyan Glow
    const cyanRim = new THREE.DirectionalLight(0x41C9E2, 2.4);
    cyanRim.position.set(-5, 2, -4);
    this.scene.add(cyanRim);

    // Rim light 2 - Tech Blue Glow
    const blueRim = new THREE.DirectionalLight(0x008DDA, 1.8);
    blueRim.position.set(5, -3, -3);
    this.scene.add(blueRim);

    // Soft point light along spine core
    this.coreLight = new THREE.PointLight(0x41C9E2, 1.2, 8);
    this.coreLight.position.set(0, 0, 1.2);
    this.mainGroup.add(this.coreLight);
  }

  createSpineGeometry() {
    // Shared materials
    this.materials = {
      cervical: new THREE.MeshStandardMaterial({
        color: 0xE2E8F0,
        roughness: 0.35,
        metalness: 0.15,
        emissive: 0x07111E,
        emissiveIntensity: 0.2
      }),
      toracica: new THREE.MeshStandardMaterial({
        color: 0xE2E8F0,
        roughness: 0.35,
        metalness: 0.15,
        emissive: 0x07111E,
        emissiveIntensity: 0.2
      }),
      lombar: new THREE.MeshStandardMaterial({
        color: 0xE2E8F0,
        roughness: 0.35,
        metalness: 0.15,
        emissive: 0x07111E,
        emissiveIntensity: 0.2
      }),
      sacral: new THREE.MeshStandardMaterial({
        color: 0xE2E8F0,
        roughness: 0.4,
        metalness: 0.12,
        emissive: 0x07111E,
        emissiveIntensity: 0.2
      }),
      disc: new THREE.MeshStandardMaterial({
        color: 0x008DDA,
        roughness: 0.2,
        metalness: 0.4,
        emissive: 0x0077B6,
        emissiveIntensity: 0.4,
        transparent: true,
        opacity: 0.88
      }),
      cord: new THREE.MeshStandardMaterial({
        color: 0x41C9E2,
        emissive: 0x41C9E2,
        emissiveIntensity: 0.6,
        roughness: 0.1,
        transparent: true,
        opacity: 0.7
      }),
      nerve: new THREE.LineBasicMaterial({
        color: 0xACE2E1,
        transparent: true,
        opacity: 0.6,
        linewidth: 1.5
      })
    };

    // Vertebrae positions and natural anatomic curve
    // Total 24 vertebrae + Sacrum/Coccyx
    const totalVertebrae = 24;
    const spineStartY = 3.2;
    const spineEndY = -2.3;
    const totalHeight = spineStartY - spineEndY;
    const stepY = totalHeight / totalVertebrae;

    const cordPoints = [];

    for (let i = 0; i < totalVertebrae; i++) {
      const t = i / (totalVertebrae - 1);
      const y = spineStartY - i * stepY;

      // Natural anatomical S-curve (lordosis/kyphosis)
      // Cervical (0-6): lordosis forward (-z)
      // Thoracic (7-18): kyphosis backward (+z)
      // Lumbar (19-23): lordosis forward (-z)
      let zOffset = 0;
      let scale = 1;
      let regionKey = 'cervical';

      if (i <= 6) {
        // Cervical
        regionKey = 'cervical';
        const ct = i / 6;
        zOffset = -Math.sin(ct * Math.PI) * 0.22;
        scale = 0.55 + ct * 0.15;
      } else if (i <= 18) {
        // Thoracic
        regionKey = 'toracica';
        const tt = (i - 7) / 11;
        zOffset = Math.sin(tt * Math.PI) * 0.32;
        scale = 0.72 + tt * 0.28;
      } else {
        // Lumbar
        regionKey = 'lombar';
        const lt = (i - 19) / 4;
        zOffset = -Math.sin(lt * Math.PI) * 0.28;
        scale = 1.05 + lt * 0.25;
      }

      cordPoints.push(new THREE.Vector3(0, y, zOffset));

      // Build stylized anatomical vertebra
      const vertebraGroup = new THREE.Group();
      vertebraGroup.position.set(0, y, zOffset);
      vertebraGroup.userData = {
        index: i,
        region: regionKey,
        isVertebra: true,
        baseScale: scale
      };

      // 1. Vertebral Body (Anterior)
      const bodyGeo = new THREE.CylinderGeometry(0.38 * scale, 0.42 * scale, 0.14 * scale, 24);
      bodyGeo.scale(1.2, 1, 0.9); // Kidney-bean anatomical proportion
      const bodyMesh = new THREE.Mesh(bodyGeo, this.materials[regionKey].clone());
      bodyMesh.position.set(0, 0, -0.05 * scale);
      bodyMesh.castShadow = true;
      bodyMesh.receiveShadow = true;
      vertebraGroup.add(bodyMesh);

      // 2. Spinous Process (Posterior spine protrusion)
      const spinousAngle = regionKey === 'toracica' ? -0.35 : (regionKey === 'cervical' ? -0.15 : -0.1);
      const spinousLength = (regionKey === 'toracica' ? 0.7 : 0.5) * scale;
      const spinousGeo = new THREE.ConeGeometry(0.12 * scale, spinousLength, 12);
      spinousGeo.rotateX(Math.PI / 2 + spinousAngle);
      const spinousMesh = new THREE.Mesh(spinousGeo, this.materials[regionKey].clone());
      spinousMesh.position.set(0, -0.02 * scale, (0.35 + spinousLength * 0.4) * scale);
      vertebraGroup.add(spinousMesh);

      // 3. Transverse Processes (Lateral wings)
      const wingLength = 0.45 * scale;
      const wingGeo = new THREE.ConeGeometry(0.09 * scale, wingLength, 10);
      wingGeo.rotateZ(Math.PI / 2);

      const leftWing = new THREE.Mesh(wingGeo, this.materials[regionKey].clone());
      leftWing.position.set(-0.35 * scale - wingLength * 0.4, 0, 0.1 * scale);
      vertebraGroup.add(leftWing);

      const rightWing = new THREE.Mesh(wingGeo, this.materials[regionKey].clone());
      rightWing.position.set(0.35 * scale + wingLength * 0.4, 0, 0.1 * scale);
      rightWing.rotation.y = Math.PI;
      vertebraGroup.add(rightWing);

      // Store references
      vertebraGroup.traverse(child => {
        if (child.isMesh) {
          child.userData = { parentGroup: vertebraGroup, region: regionKey };
          this.vertebraeMeshes.push(child);
        }
      });

      this.mainGroup.add(vertebraGroup);

      // 4. Intervertebral Disc (between bodies, except at bottom)
      if (i < totalVertebrae - 1) {
        const discY = y - stepY * 0.5;
        const discZ = zOffset;
        const discGeo = new THREE.CylinderGeometry(0.36 * scale, 0.38 * scale, 0.05 * scale, 20);
        discGeo.scale(1.22, 1, 0.92);
        const discMesh = new THREE.Mesh(discGeo, this.materials.disc.clone());
        discMesh.position.set(0, discY, discZ - 0.05 * scale);
        discMesh.userData = { isDisc: true, region: regionKey };
        this.discMeshes.push(discMesh);
        this.mainGroup.add(discMesh);
      }

      // 5. Stylized Nerve Root Branches (lateral pulse lines)
      const nerveLeftCurve = new THREE.CatmullRomCurve3([
        new THREE.Vector3(-0.15 * scale, y, zOffset),
        new THREE.Vector3(-0.55 * scale, y - 0.08, zOffset - 0.05),
        new THREE.Vector3(-0.95 * scale, y - 0.16, zOffset - 0.12)
      ]);
      const nerveRightCurve = new THREE.CatmullRomCurve3([
        new THREE.Vector3(0.15 * scale, y, zOffset),
        new THREE.Vector3(0.55 * scale, y - 0.08, zOffset - 0.05),
        new THREE.Vector3(0.95 * scale, y - 0.16, zOffset - 0.12)
      ]);

      const nervePointsLeft = nerveLeftCurve.getPoints(12);
      const nervePointsRight = nerveRightCurve.getPoints(12);

      const nerveGeoL = new THREE.BufferGeometry().setFromPoints(nervePointsLeft);
      const nerveGeoR = new THREE.BufferGeometry().setFromPoints(nervePointsRight);

      const nerveLineL = new THREE.Line(nerveGeoL, this.materials.nerve);
      const nerveLineR = new THREE.Line(nerveGeoR, this.materials.nerve);
      this.mainGroup.add(nerveLineL);
      this.mainGroup.add(nerveLineR);
    }

    // 6. Sacrum & Coccyx (Fused shield at base)
    const sacrumGroup = new THREE.Group();
    sacrumGroup.position.set(0, -2.7, -0.05);
    sacrumGroup.userData = { region: 'sacral', isVertebra: true };

    const sacrumGeo = new THREE.ConeGeometry(0.78, 1.15, 16);
    sacrumGeo.scale(1.25, 1, 0.65);
    sacrumGeo.rotateX(Math.PI); // Point down
    const sacrumMesh = new THREE.Mesh(sacrumGeo, this.materials.sacral.clone());
    sacrumMesh.userData = { parentGroup: sacrumGroup, region: 'sacral' };
    this.vertebraeMeshes.push(sacrumMesh);
    sacrumGroup.add(sacrumMesh);

    // Coccyx tip
    const coccyxGeo = new THREE.ConeGeometry(0.24, 0.45, 10);
    coccyxGeo.rotateX(Math.PI);
    const coccyxMesh = new THREE.Mesh(coccyxGeo, this.materials.sacral.clone());
    coccyxMesh.position.set(0, -0.75, 0.05);
    coccyxMesh.userData = { parentGroup: sacrumGroup, region: 'sacral' };
    this.vertebraeMeshes.push(coccyxMesh);
    sacrumGroup.add(coccyxMesh);

    this.mainGroup.add(sacrumGroup);

    // 7. Glowing Spinal Canal Core
    const cordCurve = new THREE.CatmullRomCurve3(cordPoints);
    const cordGeo = new THREE.TubeGeometry(cordCurve, 40, 0.07, 10, false);
    const cordMesh = new THREE.Mesh(cordGeo, this.materials.cord);
    this.mainGroup.add(cordMesh);
  }

  createHotspots() {
    this.hotspotDefinitions = [
      { key: 'cervical', y: 2.3, z: 0.1, label: 'Cervical' },
      { key: 'toracica', y: 0.6, z: 0.4, label: 'Torácica' },
      { key: 'lombar', y: -1.3, z: -0.1, label: 'Lombar' },
      { key: 'sacral', y: -2.7, z: 0.2, label: 'Sacral' }
    ];

    this.hotspotDefinitions.forEach(def => {
      const group = new THREE.Group();
      group.position.set(1.4, def.y, def.z);
      group.userData = { isHotspot: true, region: def.key, label: def.label };

      // Inner glowing core
      const coreGeo = new THREE.SphereGeometry(0.09, 16, 16);
      const coreMat = new THREE.MeshBasicMaterial({ color: 0x41C9E2 });
      const coreMesh = new THREE.Mesh(coreGeo, coreMat);
      group.add(coreMesh);

      // Pulsing outer halo ring
      const ringGeo = new THREE.RingGeometry(0.12, 0.17, 24);
      const ringMat = new THREE.MeshBasicMaterial({
        color: 0xACE2E1,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.75
      });
      const ringMesh = new THREE.Mesh(ringGeo, ringMat);
      group.add(ringMesh);

      // Connecting dashline to spine
      const linePoints = [
        new THREE.Vector3(0, 0, 0),
        new THREE.Vector3(-0.9, 0, 0)
      ];
      const lineGeo = new THREE.BufferGeometry().setFromPoints(linePoints);
      const lineMat = new THREE.LineDashedMaterial({
        color: 0x41C9E2,
        dashSize: 0.08,
        gapSize: 0.05,
        transparent: true,
        opacity: 0.5
      });
      const line = new THREE.Line(lineGeo, lineMat);
      line.computeLineDistances();
      group.add(line);

      this.hotspotObjects.push({
        group,
        ringMesh,
        def,
        pulseOffset: Math.random() * Math.PI
      });

      this.mainGroup.add(group);
    });
  }

  setupEvents() {
    const el = this.renderer.domElement;

    // Pointer move (hover & parallax)
    const onPointerMove = (e) => {
      const rect = el.getBoundingClientRect();
      this.mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      this.mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

      if (!this.hasInteracted) {
        this.notifyInteraction();
      }

      if (this.isDragging && this.options.allowDrag) {
        const deltaX = e.clientX - this.previousMousePosition.x;
        const deltaY = e.clientY - this.previousMousePosition.y;

        this.targetRotation.y += deltaX * 0.008;
        this.targetRotation.x += deltaY * 0.005;

        // Clamp x rotation to avoid upside-down flip
        this.targetRotation.x = Math.max(-0.6, Math.min(0.6, this.targetRotation.x));

        this.previousMousePosition = { x: e.clientX, y: e.clientY };
      } else {
        // Gentle parallax when not dragging
        this.targetRotation.y = this.mouse.x * 0.35;
        this.targetRotation.x = -this.mouse.y * 0.2;
      }

      this.checkRaycast();
    };

    const onPointerDown = (e) => {
      this.isDragging = true;
      this.previousMousePosition = { x: e.clientX, y: e.clientY };
      el.style.cursor = 'grabbing';
      this.notifyInteraction();
    };

    const onPointerUp = () => {
      this.isDragging = false;
      el.style.cursor = 'grab';
    };

    const onClick = () => {
      this.checkRaycast(true);
    };

    // Touch support
    const onTouchStart = (e) => {
      if (e.touches.length === 1) {
        this.isDragging = true;
        this.previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        this.notifyInteraction();
      }
    };

    const onTouchMove = (e) => {
      if (e.touches.length === 1 && this.isDragging) {
        const deltaX = e.touches[0].clientX - this.previousMousePosition.x;
        const deltaY = e.touches[0].clientY - this.previousMousePosition.y;

        this.targetRotation.y += deltaX * 0.008;
        this.targetRotation.x += deltaY * 0.005;
        this.targetRotation.x = Math.max(-0.6, Math.min(0.6, this.targetRotation.x));

        this.previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      }
    };

    const onTouchEnd = () => {
      this.isDragging = false;
    };

    el.style.cursor = 'grab';
    el.addEventListener('pointermove', onPointerMove, { passive: true });
    el.addEventListener('pointerdown', onPointerDown);
    window.addEventListener('pointerup', onPointerUp);
    el.addEventListener('click', onClick);

    el.addEventListener('touchstart', onTouchStart, { passive: true });
    el.addEventListener('touchmove', onTouchMove, { passive: true });
    window.addEventListener('touchend', onTouchEnd);

    // Responsive resize
    this.resizeObserver = new ResizeObserver(() => {
      this.handleResize();
    });
    this.resizeObserver.observe(this.container);
  }

  notifyInteraction() {
    this.hasInteracted = true;
    const badge = document.getElementById('spine-microcopy');
    if (badge) {
      badge.style.opacity = '0';
      badge.style.pointerEvents = 'none';
      setTimeout(() => badge.remove(), 600);
    }
  }

  handleResize() {
    if (!this.container || !this.renderer || !this.camera) return;
    const width = this.container.clientWidth || 360;
    const height = this.container.clientHeight || 520;
    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(width, height);
  }

  setupObserver() {
    // Only render when visible to maximize performance and save battery
    this.intersectionObserver = new IntersectionObserver(([entry]) => {
      this.isVisible = entry.isIntersecting;
    }, { threshold: 0.1 });

    this.intersectionObserver.observe(this.container);
  }

  checkRaycast(isClick = false) {
    if (!this.camera || !this.scene) return;

    this.raycaster.setFromCamera(this.mouse, this.camera);
    const intersects = this.raycaster.intersectObjects(this.mainGroup.children, true);

    let foundRegion = null;

    for (let i = 0; i < intersects.length; i++) {
      const obj = intersects[i].object;
      const region = obj.userData?.region || obj.parent?.userData?.region;
      if (region) {
        foundRegion = region;
        break;
      }
    }

    if (foundRegion !== this.hoveredRegion) {
      this.hoveredRegion = foundRegion;
      this.updateHighlight();
      if (this.options.onRegionHover) {
        this.options.onRegionHover(foundRegion);
      }
    }

    if (isClick && foundRegion) {
      this.focusRegion(foundRegion);
      if (this.options.onRegionSelect) {
        this.options.onRegionSelect(foundRegion);
      }
    }
  }

  updateHighlight() {
    const targetRegion = this.activeRegion || this.hoveredRegion;

    this.vertebraeMeshes.forEach(mesh => {
      const reg = mesh.userData.region;
      if (targetRegion && reg === targetRegion) {
        mesh.material.emissive.setHex(0x008DDA);
        mesh.material.emissiveIntensity = 0.9;
        mesh.material.color.setHex(0xACE2E1);
      } else {
        mesh.material.emissive.setHex(0x07111E);
        mesh.material.emissiveIntensity = 0.2;
        mesh.material.color.setHex(0xE2E8F0);
      }
    });

    this.discMeshes.forEach(mesh => {
      const reg = mesh.userData.region;
      if (targetRegion && reg === targetRegion) {
        mesh.material.emissive.setHex(0x41C9E2);
        mesh.material.emissiveIntensity = 1.0;
      } else {
        mesh.material.emissive.setHex(0x0077B6);
        mesh.material.emissiveIntensity = 0.4;
      }
    });
  }

  focusRegion(regionKey, triggerCallback = true) {
    if (!this.regions[regionKey]) return;

    const data = this.regions[regionKey];
    this.activeRegion = regionKey;

    // Smooth camera transition
    this.targetCamera.y = data.cameraY;
    this.targetCamera.z = data.cameraZ;
    this.targetLookAtY = data.targetY;

    // Subtle rotation to highlight anatomical profile
    this.targetRotation.y = 0.45;
    this.targetRotation.x = 0.05;

    this.updateHighlight();

    if (triggerCallback && this.options.onRegionSelect) {
      this.options.onRegionSelect(regionKey);
    }
  }

  resetView() {
    this.activeRegion = null;
    this.hoveredRegion = null;
    this.targetCamera.y = 0;
    this.targetCamera.z = 8.5;
    this.targetLookAtY = -0.2;
    this.targetRotation.x = 0;
    this.targetRotation.y = 0;
    this.updateHighlight();
  }

  animate() {
    requestAnimationFrame(() => this.animate());

    if (!this.isVisible) return;

    // Auto rotate very slowly if not dragging and not focused
    if (this.options.autoRotate && !this.isDragging && !this.activeRegion) {
      this.targetRotation.y += this.options.autoRotateSpeed;
    }

    // Damping (lerp) for buttery smooth physical feel
    const damp = 0.065;
    this.currentRotation.x += (this.targetRotation.x - this.currentRotation.x) * damp;
    this.currentRotation.y += (this.targetRotation.y - this.currentRotation.y) * damp;

    this.mainGroup.rotation.x = this.currentRotation.x;
    this.mainGroup.rotation.y = this.currentRotation.y;

    // Camera lerp
    this.currentCamera.y += (this.targetCamera.y - this.currentCamera.y) * damp;
    this.currentCamera.z += (this.targetCamera.z - this.currentCamera.z) * damp;
    this.currentLookAtY += (this.targetLookAtY - this.currentLookAtY) * damp;

    this.camera.position.y = this.currentCamera.y;
    this.camera.position.z = this.currentCamera.z;
    this.camera.lookAt(0, this.currentLookAtY, 0);

    // Pulse hotspots and face camera (billboarding)
    const time = performance.now() * 0.003;
    this.hotspotObjects.forEach(hp => {
      const scale = 1 + Math.sin(time + hp.pulseOffset) * 0.22;
      hp.ringMesh.scale.set(scale, scale, 1);
      hp.ringMesh.material.opacity = 0.4 + Math.cos(time + hp.pulseOffset) * 0.35;
      hp.group.lookAt(this.camera.position);
    });

    this.renderer.render(this.scene, this.camera);
  }
}

// Export to global scope
window.SpineViewer = SpineViewer;
