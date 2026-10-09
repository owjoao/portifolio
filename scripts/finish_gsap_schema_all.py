"""
Inject GSAP and Schema.org into the remaining niches to reach 100% compliance across all 33 niches.
"""
import os, json

REMAINING_NICHES = {
    'energia-solar': {
        'schema_type': 'HomeAndConstructionBusiness',
        'business_name': 'SunEco OS • Energia Solar & Fotovoltaica',
        'desc': 'Sistemas de energia solar fotovoltaica residencial e industrial com até 95% de economia na conta de luz.'
    },
    'arquiteto': {
        'schema_type': 'ProfessionalService',
        'business_name': 'ArtVista Arquitetura & Design',
        'desc': 'Projetos arquitetônicos residenciais e comerciais de alto padrão com acompanhamento completo de obra.'
    },
    'banho-e-tosa': {
        'schema_type': 'VeterinaryCare',
        'business_name': 'Pawly Petshop & Centro de Estética Animal',
        'desc': 'Banho, tosa na tesoura, hidratação com ozonioterapia e cuidados veterinários carinhosos para cães e gatos.'
    },
    'psicologia': {
        'schema_type': 'MedicalClinic',
        'business_name': 'Mente Serena • Clínica de Psicologia & Bem-Estar',
        'desc': 'Atendimento psicológico clínico presencial e online baseado na Terapia Cognitivo-Comportamental.'
    },
    'nutricionista': {
        'schema_type': 'MedicalBusiness',
        'business_name': 'NutriViva • Nutrição Clínica & Esportiva',
        'desc': 'Consultoria nutricional individualizada com bioimpedância e planejamento alimentar sustentável.'
    },
    'podologo': {
        'schema_type': 'MedicalClinic',
        'business_name': 'Podologia Especializada & Saúde dos Pés',
        'desc': 'Tratamento de unhas encravadas, calosidades, pés diabéticos e laserterapia podológica indolor.'
    },
    'shineray-uba': {
        'schema_type': 'AutoDealer',
        'business_name': 'Shineray Ubá • Scooters & Motos Elétricas',
        'desc': 'Concessionária oficial Shineray com linha completa de motos elétricas, ciclomotores e peças genuínas.'
    },
    'topmotos032': {
        'schema_type': 'AutoDealer',
        'business_name': 'TOP MOTOS 032 • Multimarcas & Seminovos',
        'desc': 'Venda, troca e financiamento de motos seminovas revisadas com garantia e procedência.'
    },
    'vrum-motos': {
        'schema_type': 'AutoDealer',
        'business_name': 'Vrum Motos • Concessionária & Peças',
        'desc': 'Compre sua moto zero km e seminova com as melhores taxas de financiamento da região.'
    },
    'fumaca-motos': {
        'schema_type': 'AutoRepair',
        'business_name': 'Fumaça Motos • Oficina Especializada & Multimarcas',
        'desc': 'Manutenção preventiva, preparação de motores, injeção eletrônica e socorro para motocicletas.'
    },
    'rampabike': {
        'schema_type': 'BikeStore',
        'business_name': 'Rampa Bike Especializada & Oficina Shimano',
        'desc': 'Bicicletas de performance MTB e Speed, componentes Shimano e oficina técnica certificada.'
    },
    'caxixi': {
        'schema_type': 'Restaurant',
        'business_name': 'Bar & Restaurante Caxixi',
        'desc': 'Culinária tradicional brasileira com pratos caseiros, carnes na brasa e drinks autorais.'
    },
    'reconcavo': {
        'schema_type': 'Restaurant',
        'business_name': 'Recôncavo Culinária & Sabores da Bahia',
        'desc': 'Moquecas tradicionais de pescada e camarão, acarajé artesanal e sobremesas baianas.'
    },
    'reforma-moveis': {
        'schema_type': 'HomeAndConstructionBusiness',
        'business_name': 'Ateliê Renova Móveis & Restauração',
        'desc': 'Restauração artesanal de móveis clássicos e contemporâneos, marcenaria fina e estofaria.'
    },
    'sorveteria': {
        'schema_type': 'IceCreamShop',
        'business_name': 'SCOOPÉRA Gelateria & Sorvetes Artesanais',
        'desc': 'Sorvetes artesanais cremosos, picolés gourmet de frutas e taças especiais sem conservantes artificiais.'
    }
}

GSAP_CDN = '''
  <!-- GSAP & ScrollTrigger -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
'''

for niche, data in REMAINING_NICHES.items():
    path = os.path.join(niche, 'index.html')
    if not os.path.exists(path):
        continue
    content = open(path, encoding='utf-8', errors='ignore').read()
    changed = False

    # GSAP
    if 'gsap.min.js' not in content:
        content = content.replace('</head>', f'{GSAP_CDN}\n</head>')
        changed = True

    # Schema.org
    if 'application/ld+json' not in content:
        schema_dict = {
            '@context': 'https://schema.org',
            '@type': data['schema_type'],
            'name': data['business_name'],
            'description': data['desc'],
            'telephone': '+55-32-99929-2311',
            'url': f'https://nexusflow.digital/{niche}/',
            'address': {
                '@type': 'PostalAddress',
                'streetAddress': 'Av. Paulista, 1000',
                'addressLocality': 'São Paulo',
                'addressRegion': 'SP',
                'postalCode': '01310-100',
                'addressCountry': 'BR'
            }
        }
        schema_html = f'''
  <!-- Schema.org SEO & GEO Data -->
  <script type="application/ld+json">
  {json.dumps(schema_dict, indent=2, ensure_ascii=False)}
  </script>
'''
        content = content.replace('</head>', f'{schema_html}\n</head>')
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[+] Updated GSAP/Schema for {niche}')

print('All remaining niches processed.')

