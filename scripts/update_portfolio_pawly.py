# -*- coding: utf-8 -*-
import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero pill or title if present
html = html.replace('title="Pet Shop, Banho & Tosa e Vet"', 'title="Pawly • Pet Shop & E-commerce Premium"')

# 2. Update card descriptions & badges in banho-e-tosa card
# Look for Lumina OS CRM in banho-e-tosa section and replace with Pawly E-commerce
old_card_pattern = r'(onclick="openNetflixModal\(\'banho-e-tosa\'\)"[\s\S]*?)(<h3[^>]*>)(.*?)(</h3>[\s\S]*?<p[^>]*>)(.*?)(</p>)'

def replace_card_info(match):
    prefix = match.group(1)
    h3_open = match.group(2)
    # title
    h3_close_and_p_open = match.group(4)
    # desc
    p_close = match.group(6)
    new_title = "Pawly • Pet Shop & E-commerce Premium"
    new_desc = "Landing page completa com carrinho interativo, frete dinâmico, adoção de pets, quiz personalizado, agendamento de serviços e captura de leads."
    return f"{prefix}{h3_open}{new_title}{h3_close_and_p_open}{new_desc}{p_close}"

html = re.sub(old_card_pattern, replace_card_info, html)

# 3. Update NICHES_DATA in JS
# Find JSON object for banho-e-tosa
niches_match = re.search(r'const NICHES_DATA = (\[[\s\S]*?\]);', html)
if niches_match:
    try:
        niches_data = json.loads(niches_match.group(1))
        for item in niches_data:
            if item.get('id') == 'banho-e-tosa':
                item['name'] = 'Pawly • Pet Shop & E-commerce Premium'
                item['shortName'] = 'Pawly Pet'
                item['brand'] = 'Pawly Petshop'
                item['domain'] = 'pawly.com.br'
                item['tagline'] = 'E-commerce Petshop + Adoção & Agendamento'
                item['desc'] = 'Landing page completa com carrinho interativo, frete dinâmico, adoção de pets, quiz personalizado e agendamento.'
                item['objectionBreaker'] = 'Cuidado afetuoso com entrega rápida para todo o Brasil, produtos premium e atendimento humanizado via WhatsApp.'
                item['guarantee'] = 'Garantia Pawly & Entrega Segura'
                item['category'] = 'Pet & E-commerce'
                item['tags'] = ['Carrinho Interativo', 'Frete Dinâmico', 'Adoção de Pets', 'Quiz Personalizado', 'WhatsApp VIP']
                print('Updated NICHES_DATA entry for banho-e-tosa')
                break
        new_json_str = json.dumps(niches_data, ensure_ascii=False)
        html = html[:niches_match.start(1)] + new_json_str + html[niches_match.end(1):]
    except Exception as e:
        print('Error parsing NICHES_DATA:', e)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Portfolio index.html updated successfully!')
