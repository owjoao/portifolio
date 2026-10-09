import json, os, re

def load_projects():
    with open('scripts/projects_catalog.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def build_new_portal():
    projects = load_projects()
    
    # Pre-generate projects JSON for client-side search in the Smart Request Bar
    niche_database = []
    
    keywords_map = {
        'energia-solar/index.html': ['solar', 'energia solar', 'placas', 'fotovoltaica', 'inversor', 'engenharia'],
        'dentista/index.html': ['dentista', 'odontologia', 'odonto', 'dente', 'implante', 'ortodontia', 'sorriso', 'clinica'],
        'advogado/index.html': ['advogado', 'advocacia', 'juridico', 'direito', 'lexpro', 'processo', 'causa'],
        'concessionaria-honda/index.html': ['honda', 'concessionaria', 'carro', 'automotivo', 'vendedor automotivo', 'veiculos', 'test drive', 'seminovos'],
        'arquiteto/index.html': ['arquiteto', 'arquitetura', 'projeto', 'decoracao', 'artvista', 'quadros', 'design interiores'],
        'banho-e-tosa/index.html': ['pet', 'petshop', 'banho e tosa', 'veterinario', 'cachorro', 'gato', 'pawly'],
        'barbearia/index.html': ['barbearia', 'barbeiro', 'cabelo', 'barba', 'corte', 'barber club'],
        'corretor-imoveis/index.html': ['imoveis', 'imobiliaria', 'corretor', 'casa', 'apartamento', 'financiamento', 'imobmax'],
        'psicologia/index.html': ['psicologia', 'psicologo', 'terapia', 'saude mental', 'mente serena', 'ansiedade'],
        'oftalmologista/index.html': ['oftalmologista', 'olhos', 'visao', 'clinica de olhos', 'oftalmo', 'otica'],
        'nutricionista/index.html': ['nutricionista', 'dieta', 'nutricao', 'emagrecimento', 'alimentacao', 'nutriviva'],
        'quiropraxista/index.html': ['quiropraxista', 'quiropraxia', 'coluna', 'postura', 'dor nas costas', 'ajuste'],
        'acupunturista/index.html': ['acupunturista', 'acupuntura', 'medicina chinesa', 'equilibrio', 'agulhas'],
        'podologo/index.html': ['podologo', 'podologia', 'pes', 'unha', 'saude dos pes'],
        'gtmotors/index.html': ['gt motors', 'supercarros', 'carros esportivos', 'vendedor automotivo', 'porsche', 'ferrari'],
        'shineray-uba/index.html': ['shineray', 'motos', 'moto', 'scooter', 'ciclomotor', 'consorcio moto'],
        'topmotos032/index.html': ['top motos', 'motos', 'moto eletrica', 'consorcio', 'motos 032'],
        'vrum-motos/index.html': ['vrum motos', 'motos multimarcas', 'venda de motos', 'duas rodas'],
        'fumaca-motos/index.html': ['fumaca motos', 'oficina de motos', 'revisao moto', 'pecas de moto'],
        'rampabike/index.html': ['bike', 'bicicleta', 'ciclismo', 'mtb', 'speed', 'oficina bike'],
        'restaurante-egeu/index.html': ['restaurante', 'egeu', 'gastronomia', 'mediterraneo', 'jantar', 'reserva mesa'],
        'boteco-portugues/index.html': ['boteco', 'bar', 'portugues', 'tasco', 'petiscos', 'cerveja'],
        'caxixi/index.html': ['caxixi', 'bar e restaurante', 'drinks', 'almoco', 'gastronomia'],
        'reconcavo/index.html': ['reconcavo', 'culinaria baiana', 'dende', 'acaraje', 'moqueca', 'comida'],
        'fotografo-casamento/index.html': ['fotografo', 'fotografia', 'casamento', 'ensaio', 'fotos', 'lumiere'],
        'reforma-moveis/index.html': ['reforma', 'moveis', 'marcenaria', 'estofados', 'tapeçaria', 'restauracao'],
        'lavanderia/index.html': ['lavanderia', 'lavagem de roupas', 'lavaclean', 'lavanderia express'],
        'personal-trainer/index.html': ['personal', 'personal trainer', 'treino', 'musculacao', 'fitness', 'academia'],
        'contador/index.html': ['contador', 'contabilidade', 'fiscal', 'imposto', 'abertura de empresa', 'exata contabil'],
        'professor-idiomas/index.html': ['ingles', 'idiomas', 'professor de ingles', 'espanhol', 'polyglot', 'aulas particulares'],
        'professor-musica/index.html': ['musica', 'aulas de musica', 'violao', 'piano', 'canto', 'harmonia'],
        'professor-particular/index.html': ['reforco escolar', 'professor particular', 'aulas', 'matematica', 'enem', 'nota 10'],
        'sorveteria/index.html': ['sorvete', 'sorveteria', 'gelato', 'gelateria', 'acai', 'açai', 'sobremesa', 'picole', 'doce', 'scoopera'],
        'pizzaria_landingpage/index.html': ['pizzaria', 'pizza', 'forno a lenha', 'calzone', 'restaurante', 'massa', 'bella napoli'],
        'lanchonete/index.html': ['lanchonete', 'hamburguer', 'lanche', 'fast food', 'kfc', 'frango frito', 'delivery', 'porcao']
    }

    for url, proj in projects.items():
        keys = keywords_map.get(url, [proj['title'].lower()])
        has_crm = '/admin/index.html' in [u for u in [url.replace('/index.html', '/admin/index.html')]] and ('energia' in url or 'dentista' in url or 'advogado' in url or 'concessionaria' in url or 'arquiteto' in url or 'banho' in url or 'barbearia' in url or 'corretor' in url)
        admin_url = url.replace('/index.html', '/admin/index.html') if has_crm else ''
        
        niche_database.append({
            'url': url,
            'title': proj['title'],
            'image': proj['image'],
            'desc': proj['desc'],
            'tags': proj['tags'],
            'keywords': keys,
            'has_crm': has_crm,
            'admin_url': admin_url
        })

    db_json = json.dumps(niche_database, ensure_ascii=False)
    return db_json

if __name__ == '__main__':
    db = build_new_portal()
    print("Database built with length:", len(db))
