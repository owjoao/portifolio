# -*- coding: utf-8 -*-
import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update titles and texts for arquiteto
html = html.replace('StudioDesign OS</div>\n              <h3 class="text-base font-bold text-white leading-tight font-serif">Arquitetura & Design de Interiores</h3>', 'ArtVista Wall Art</div>\n              <h3 class="text-base font-bold text-white leading-tight font-serif">ArtVista • Arte em Parede & Decoração 3D</h3>')

html = html.replace('Simulador paramétrico de custo por m² e cronograma de obra, briefing digital imersivo e CRM com acompanhamento de etapas de obra e acabamentos por lote.', 'Esculturas tridimensionais exclusivas e quadros com iluminação em LED quente dimerizável, loja virtual com carrinho interativo e simulação na parede via WhatsApp.')

# Update NICHES_DATA entry for arquiteto
niches_match = re.search(r'const NICHES_DATA = (\[[\s\S]*?\]);', html)
if niches_match:
    try:
        niches_data = json.loads(niches_match.group(1))
        for item in niches_data:
            if item.get('id') == 'arquiteto':
                item['name'] = 'ArtVista • Arte em Parede & Decoração 3D'
                item['shortName'] = 'ArtVista Decor'
                item['brand'] = 'ArtVista Wall Art'
                item['domain'] = 'artvista.com.br'
                item['tagline'] = 'Esculturas de Parede 3D + Iluminação LED & Loja Virtual'
                item['desc'] = 'Quadros e esculturas de parede 3D exclusivas com LED dimerizável, loja virtual com carrinho interativo, cálculo de frete e simulação 3D no WhatsApp.'
                item['objectionBreaker'] = 'Simulação 3D gratuita na sua parede antes de comprar, envio seguro para todo o Brasil em caixa de madeira e 5 anos de garantia.'
                item['guarantee'] = 'Garantia de 5 Anos ArtVista'
                item['category'] = 'Arte & Decoração'
                item['tags'] = ['Esculturas 3D LED', 'Carrinho Interativo', 'Frete Grátis', 'Obras Autorais', 'Simulador de Parede']
                print('Updated NICHES_DATA for arquiteto')
                break
        new_json_str = json.dumps(niches_data, ensure_ascii=False)
        html = html[:niches_match.start(1)] + new_json_str + html[niches_match.end(1):]
    except Exception as e:
        print('Error updating NICHES_DATA:', e)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated portfolio index.html for ArtVista successfully!')
