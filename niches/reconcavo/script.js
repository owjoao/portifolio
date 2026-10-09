document.documentElement.classList.add("js");

const header = document.querySelector("[data-header]");
const menuToggle = document.querySelector("[data-menu-toggle]");
const navigation = document.querySelector("[data-navigation]");

if (menuToggle && navigation) {
  const closeMenu = () => {
    menuToggle.setAttribute("aria-expanded", "false");
    navigation.classList.remove("is-open");
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    navigation.classList.toggle("is-open", !isOpen);
  });

  navigation.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuToggle.getAttribute("aria-expanded") === "true") {
      closeMenu();
      menuToggle.focus();
    }
  });
}

const progress = document.querySelector("[data-progress]");

const updateScrollEffects = () => {
  const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
  const percentage = scrollableHeight > 0 ? Math.min(window.scrollY / scrollableHeight, 1) : 0;

  if (progress) {
    progress.style.transform = `scaleX(${percentage})`;
  }

  if (header) {
    header.classList.toggle("is-scrolled", window.scrollY > 12);
  }
};

updateScrollEffects();
window.addEventListener("scroll", updateScrollEffects, { passive: true });
window.addEventListener("resize", updateScrollEffects, { passive: true });

const revealItems = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -32px" },
  );

  revealItems.forEach((item) => revealObserver.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

const parallaxItems = [...document.querySelectorAll("[data-parallax]")];
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

if (parallaxItems.length && window.matchMedia("(pointer: fine)").matches && !reducedMotion.matches) {
  let ticking = false;

  const updateParallax = () => {
    parallaxItems.forEach((item) => {
      const bounds = item.getBoundingClientRect();
      const centerOffset = window.innerHeight / 2 - (bounds.top + bounds.height / 2);
      const factor = Number(item.dataset.parallax || 0);
      item.style.setProperty("--parallax-y", `${(centerOffset * factor).toFixed(1)}px`);
    });
    ticking = false;
  };

  const requestParallax = () => {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(updateParallax);
  };

  window.addEventListener("scroll", requestParallax, { passive: true });
  window.addEventListener("resize", requestParallax, { passive: true });
  updateParallax();
}

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});

const mapVisual = document.querySelector("[data-map-visual]");
const mapFrame = document.querySelector("[data-map-frame]");

if (mapVisual && mapFrame) {
  const showMap = () => mapVisual.classList.add("is-loaded");
  mapFrame.addEventListener("load", showMap, { once: true });
  window.setTimeout(showMap, 3500);
}
