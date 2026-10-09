# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for extended preview scroll on hover
custom_css = '''
    /* Extended Screenshot Scroll on Hover */
    .extended-preview-img {
      object-fit: cover !important;
      object-position: top center !important;
      transition: object-position 5s cubic-bezier(0.25, 1, 0.35, 1), transform 0.5s ease !important;
    }
    .netflix-card:hover .extended-preview-img,
    .niche-grid-item:hover .extended-preview-img {
      object-position: bottom center !important;
      transform: scale(1.02) !important;
    }
    #modal-banner {
      transition: background-position 6s cubic-bezier(0.25, 1, 0.35, 1) !important;
    }
    #modal-banner:hover {
      background-position: bottom center !important;
    }
'''

if '/* Extended Screenshot Scroll on Hover */' not in html:
    html = html.replace('  </style>', custom_css + '  </style>')

# 2. Add extended-preview-img to all images with assets/previews/
import re
def add_class(match):
    full_tag = match.group(0)
    if 'extended-preview-img' not in full_tag:
        full_tag = full_tag.replace('class="', 'class="extended-preview-img ')
    return full_tag

html = re.sub(r'<img[^>]*src=[\'"]assets/previews/[^\'"]+[\'"][^>]*>', add_class, html)

# 3. Add 'Ver Imagem Completa' button to modal-banner if not present
if 'id="modal-full-print-btn"' not in html:
    modal_banner_addon = '''
          <div class="pt-2 flex items-center gap-2">
            <span class="text-[10px] text-slate-300 font-semibold flex items-center gap-1 bg-black/60 px-2.5 py-1 rounded-full border border-white/10 backdrop-blur-md">
              <i class="fa-solid fa-arrows-up-down text-cyan-400"></i> Passe o mouse no banner para rolar a página
            </span>
            <a id="modal-full-print-btn" href="#" target="_blank" class="text-[10px] text-white font-bold bg-white/15 hover:bg-white/25 px-2.5 py-1 rounded-full border border-white/20 backdrop-blur-md flex items-center gap-1 transition">
              <i class="fa-solid fa-expand text-cyan-400"></i> Abrir Print Completo (1280x2400)
            </a>
          </div>
'''
    html = html.replace('</p>\n        </div>\n      </div>', '</p>' + modal_banner_addon + '        </div>\n      </div>')

# 4. In openNetflixModal, set href for modal-full-print-btn
if "document.getElementById('modal-full-print-btn')" not in html:
    html = html.replace(
        "document.getElementById('modal-ep1-link').setAttribute('href', niche.publicUrl);",
        "document.getElementById('modal-ep1-link').setAttribute('href', niche.publicUrl);\n      const fullPrintBtn = document.getElementById('modal-full-print-btn'); if (fullPrintBtn) fullPrintBtn.setAttribute('href', niche.previewImg);"
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html with extended preview interactive scroll and modal zoom!')
