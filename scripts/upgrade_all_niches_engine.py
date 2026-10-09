"""
Script to comprehensively upgrade all 17 niche landing pages to Master Plan standard:
- Add GSAP + ScrollTrigger scripts
- Add Schema.org JSON-LD LocalBusiness / Service data
- Insert rich photo galleries / showcase sections using newly downloaded assets
- Insert interactive FAQ accordions
- Add customer testimonials / social proof
- Ensure 100% pt-BR and correct WhatsApp (32) 99929-2311
- Ensure responsive layout, smooth hover effects, no 3D elements
"""

import os, re, json
from bs4 import BeautifulSoup

GSAP_CDN = '''
  <!-- GSAP & ScrollTrigger -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
'''

GSAP_INIT_SCRIPT = '''
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray('.reveal, .card-lift').forEach((elem) => {
          gsap.from(elem, {
            scrollTrigger: {
              trigger: elem,
              start: 'top 85%',
              toggleActions: 'play none none none'
            },
            opacity: 0,
            y: 30,
            duration: 0.8,
            ease: 'power2.out'
          });
        });
      }
    });

    function toggleFaqItem(btn) {
      const content = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      if (content.classList.contains('hidden')) {
        content.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
      } else {
        content.classList.add('hidden');
        if (icon) icon.classList.remove('rotate-180');
      }
    }
  </script>
'''

print("Engine base script initialized.")

