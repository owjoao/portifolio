"""
Complete Niche Upgrade Engine to apply Plano Mestre across all remaining niches.
For each niche, this script:
1. Injects GSAP 3.12.5 and ScrollTrigger in <head>
2. Injects Schema.org JSON-LD (LocalBusiness / MedicalClinic / LegalService / RealEstateAgent, etc.)
3. Injects custom visual showcase using the newly downloaded assets
4. Injects interactive FAQ accordion component
5. Injects client testimonials / social proof grid
6. Injects GSAP scroll animations & FAQ toggle scripts
7. Guarantees 100% pt-BR language and official WhatsApp (32) 99929-2311
"""

import os, re
from bs4 import BeautifulSoup

GSAP_CDN = '''
  <!-- GSAP & ScrollTrigger -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
'''

GSAP_SCRIPT = '''
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray('.reveal, .card-lift, .stagger-card').forEach((elem) => {
          gsap.from(elem, {
            scrollTrigger: {
              trigger: elem,
              start: 'top 88%',
              toggleActions: 'play none none none'
            },
            opacity: 0,
            y: 28,
            duration: 0.75,
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

NICHES_DATA = {
    'corretor-imoveis': {
        'schema_type': 'RealEstateAgent',
        'business_name': 'ImobMax Consultoria Imobiliária',
        'desc': 'Consultoria imobiliária de alto padrão em São Paulo com assessoria jurídica completa.',
        'accent_color': 'cyan',
        'gallery_title': 'Portfólio de Imóveis Exclusivos',
        'gallery_subtitle': 'Casas em condomínio, coberturas lineares e apartamentos com acabamento refinado.',
        'gallery': [
            {'img': 'assets/hero-mansion.jpg', 'title': 'Mansão Contemporânea Alphaville', 'desc': '580m² privativos, 4 suítes, piscina com borda infinita e automação.'},
            {'img': 'assets/penthouse-view.jpg', 'title': 'Cobertura Duplex Jardins', 'desc': '420m², vista panorâmica 360°, espaço gourmet e 5 vagas de garagem.'},
            {'img': 'assets/apartment-living.jpg', 'title': 'Living Integrado Vila Nova Conceição', 'desc': 'Living com pé-direito duplo, lareira ecológica e acabamentos em mármore.'},
            {'img': 'assets/condominio-fachada.jpg', 'title': 'Residencial Boutique Itaim Bibi', 'desc': 'Torre exclusiva com 1 apartamento por andar, gerador full e lazer privativo.'}
        ],
        'faqs': [
            ('Como funciona a assessoria jurídica gratuita?', 'Realizamos o levantamento minucioso de certidões vintenárias, CNDs trabalhistas, fiscais e tributárias do vendedor antes de qualquer sinal financeiro.'),
            ('Vocês aprovam financiamento bancário?', 'Sim! Somos correspondentes credenciados Caixa, Itaú, Bradesco e Santander. Negociamos as menores taxas de juros (CET) para seu perfil.'),
            ('Como é agendada a visita VIP?', 'Você escolhe o melhor dia e horário via WhatsApp e realizamos a visita com carro privativo e análise detalhada de documentação.')
        ],
        'reviews': [
            ('Dr. Renato Mendonça', 'Comprei uma cobertura nos Jardins com total segurança. A certidão vintenária prévia me deu total tranquilidade.', '⭐⭐⭐⭐⭐'),
            ('Fernanda Guimarães', 'Atendimento impecável do Henrique. Conseguiu taxa reduzida na Caixa e fechamos em tempo recorde.', '⭐⭐⭐⭐⭐')
        ]
    },
    'advogado': {
        'schema_type': 'LegalService',
        'business_name': 'Valente & Associados Advocacia',
        'desc': 'Escritório de advocacia estratégica especializado em Sucessões, Direito de Família e Blindagem Patrimonial.',
        'accent_color': 'amber',
        'gallery_title': 'Infraestrutura & Atuação Estratégica',
        'gallery_subtitle': 'Rigor técnico, sigilo perpétuo e ambiente projetado para decisões de alto impacto.',
        'gallery': [
            {'img': 'assets/law-hero.jpg', 'title': 'Sede Corporativa & Biblioteca Jurídica', 'desc': 'Ambiente exclusivo com isolamento acústico e biblioteca com acervo doutrinário completo.'},
            {'img': 'assets/law-library.jpg', 'title': 'Pesquisa Jurisprudencial Aprofundada', 'desc': 'Teses customizadas com base nos precedentes mais recentes do STJ e STF.'},
            {'img': 'assets/law-courtroom.jpg', 'title': 'Atuação em Tribunais Superiores', 'desc': 'Sustentações orais perante Tribunais de Justiça e Tribunais Superiores em Brasília.'},
            {'img': 'assets/law-meeting.jpg', 'title': 'Mediação & Negociação Extrajudicial', 'desc': 'Resolução célere de inventários e partilhas consensuais diretamente em Cartório de Notas.'}
        ],
        'faqs': [
            ('Como funciona o sigilo profissional?', 'Todas as comunicações e documentos compartilhados são rigorosamente protegidos pelo Código de Ética e Estatuto da OAB.'),
            ('Quanto tempo demora um inventário em cartório?', 'Quando há consenso entre herdeiros capazes, o processo é concluído em média entre 15 e 45 dias úteis.'),
            ('É possível parcelar os honorários e custas?', 'Sim, oferecemos condições facilitadas de honorários inclusive atrelados ao êxito em causas patrimoniais.')
        ],
        'reviews': [
            ('Carlos Eduardo Salles', 'Dr. Marcos resolveu nosso inventário familiar em apenas 30 dias em cartório. Economizamos tempo e desgaste emocional.', '⭐⭐⭐⭐⭐'),
            ('Patrícia Alvarenga', 'Assessoria impecável na reestruturação societária e proteção patrimonial da nossa holding.', '⭐⭐⭐⭐⭐')
        ]
    },
    'barbearia': {
        'schema_type': 'BarberShop',
        'business_name': 'Barber Club OS • Barbearia Clássica',
        'desc': 'Barbearia artesanal com toalha quente, navalha tradicional e ambiente lounge exclusivo.',
        'accent_color': 'amber',
        'gallery_title': 'A Experiência Barber Club',
        'gallery_subtitle': 'Cortes clássicos, toalha quente, navalhetes esterilizados e chopp artesanal gelado.',
        'gallery': [
            {'img': 'assets/barber-hero.jpg', 'title': 'Cortes Clássicos & Modernos', 'desc': 'Degradê perfeito, tesoura artesanal e alinhamento milimétrico do perfil facial.'},
            {'img': 'assets/barber-shave.jpg', 'title': 'Barboterapia com Toalha Quente', 'desc': 'Espuma densa aquecida, óleos essenciais pós-barba e lâmina descartável de alta precisão.'},
            {'img': 'assets/barber-cut.jpg', 'title': 'Design de Barba & Bigode', 'desc': 'Visagismo masculino adaptado à anatomia do seu rosto e estilo de vida.'},
            {'img': 'assets/barber-tools.jpg', 'title': 'Produtos Premium de Cuidados', 'desc': 'Pomadas de alta fixação efeito matte, óleos hidratantes e balms aromáticos.'}
        ],
        'faqs': [
            ('Preciso agendar horário com antecedência?', 'Recomendamos o agendamento prévio via WhatsApp para garantir zero fila e atendimento VIP pontual.'),
            ('O que está incluso no serviço de Barboterapia?', 'Massagem facial relaxante, vapor de ozônio, esfoliação leve, toalha aquecida e loção pós-barba importada.'),
            ('Quais produtos vocês utilizam?', 'Utilizamos apenas pomadas e tônicos testados dermatologicamente com fixação matte e hidratação profunda.')
        ],
        'reviews': [
            ('Guilherme Antunes', 'Melhor barbearia de São Paulo. A toalha quente e o atendimento com chopp gelado são imbatíveis.', '⭐⭐⭐⭐⭐'),
            ('Thiago Meireles', 'Pontualidade britânica e degradê na régua. Não troco por nada.', '⭐⭐⭐⭐⭐')
        ]
    },
    'restaurante-egeu': {
        'schema_type': 'Restaurant',
        'business_name': 'Restaurante Egeu Mediterrâneo',
        'desc': 'Gastronomia mediterrânea contemporânea com peixes frescos, frutos do mar e carta de vinhos selecionada.',
        'accent_color': 'sky',
        'gallery_title': 'Sabores Autênticos do Mar Egeu',
        'gallery_subtitle': 'Ingredientes frescos grelhados no azeite extravirgem grego com especiarias autênticas.',
        'gallery': [
            {'img': 'assets/egeu-hero.jpg', 'title': 'Polvo Grelhado com Azeite de Oliva', 'desc': 'Tentáculos de polvo crocantes por fora e macios por dentro com purê de fava e orégano selvagem.'},
            {'img': 'assets/egeu-seafood.jpg', 'title': 'Seleção de Frutos do Mar Frescos', 'desc': 'Camarões tigre grelhados, lulas recheadas e mariscos com toque de limão siciliano.'},
            {'img': 'assets/egeu-wine.jpg', 'title': 'Adega com Rótulos Mediterrâneos', 'desc': 'Vinhos brancos minerais da Grécia e tintos encorpados para harmonização sublime.'},
            {'img': 'assets/egeu-dessert.jpg', 'title': 'Baklava Tradicional com Sorvete', 'desc': 'Massa folhada crocante recheada com pistache caramelizado e mel artesanal.'}
        ],
        'faqs': [
            ('É necessário fazer reserva prévia?', 'Para jantares e finais de semana, a reserva antecipada garante as melhores mesas do lounge ou varanda.'),
            ('Possuem opções vegetarianas e veganas?', 'Sim! Temos saladas gregas autênticas com queijo feta DOP, mezze de fava e berinjelas assadas no forno a lenha.'),
            ('Existe estacionamento com manobrista?', 'Sim, dispomos de serviço de valet coberto na porta do restaurante para sua comodidade.')
        ],
        'reviews': [
            ('Mariana Fontana', 'O polvo grelhado é simplesmente espetacular! Clima acolhedor e atendimento nota 10.', '⭐⭐⭐⭐⭐'),
            ('Felipe Nogueira', 'Carta de vinhos gregos surpreendente. Uma verdadeira viagem gastronômica ao Mediterrâneo.', '⭐⭐⭐⭐⭐')
        ]
    },
    'boteco-portugues': {
        'schema_type': 'Restaurant',
        'business_name': 'O Tasco • Boteco Lusitano',
        'desc': 'Autêntica culinária portuguesa com bolinhos de bacalhau, chopp gelado e pastéis de nata artesanais.',
        'accent_color': 'amber',
        'gallery_title': 'Tradição Lusitana à Mesa',
        'gallery_subtitle': 'Petiscos tradicionais preparados com receitas centenárias e chopp tirado na temperatura certa.',
        'gallery': [
            {'img': 'assets/tasco-hero.jpg', 'title': 'Bacalhau à Lagareiro na Brasa', 'desc': 'Lombo alto de bacalhau Gadus morhua confitado no azeite com batatas ao murro e alho assado.'},
            {'img': 'assets/tasco-bacalhau.jpg', 'title': 'Bolinho de Bacalhau Cremoso', 'desc': 'Mais de 70% bacalhau no recheio, casquinha dourada crocante sem encharcar de óleo.'},
            {'img': 'assets/tasco-petiscos.jpg', 'title': 'Tábua de Queijos da Serra & Embutidos', 'desc': 'Queijo da Serra da Estrela, chouriço tostado na cachaça e pão alentejano quentinho.'},
            {'img': 'assets/tasco-pasteis.jpg', 'title': 'Pastéis de Belém Quentinhos com Canela', 'desc': 'Massa folhada estaladiça com recheio cremoso polvilhado com canela e açúcar.'}
        ],
        'faqs': [
            ('Qual o horário de funcionamento?', 'Funcionamos de terça a domingo a partir das 11h30 para almoço e até as 23h30 com petiscos e chopp.'),
            ('Aceitam encomendas de Bacalhau para eventos?', 'Sim! Fazemos travessas especiais para reuniões familiares e confraternizações mediante reserva.'),
            ('Vocês têm chopp artesanal e vinhos verdes?', 'Temos torneiras de chopp sempre abaixo de zero grau e rótulos selecionados de vinho verde português.')
        ],
        'reviews': [
            ('Antônio Manuel', 'Lembro de Lisboa em cada garfada. O bacalhau à lagareiro é insuperável.', '⭐⭐⭐⭐⭐'),
            ('Carla Peixoto', 'Os pastéis de nata chegam quentinhos à mesa! O chopp é o mais gelado da região.', '⭐⭐⭐⭐⭐')
        ]
    },
    'fotografo-casamento': {
        'schema_type': 'ProfessionalService',
        'business_name': 'Lucas & Helena Photography',
        'desc': 'Fotografia documental e cinematográfica de casamentos, pré-wedding e destination weddings.',
        'accent_color': 'rose',
        'gallery_title': 'Galeria de Histórias Reais',
        'gallery_subtitle': 'Sem poses engessadas: emoção pura, luz natural e color grading cinematográfico.',
        'gallery': [
            {'img': 'assets/photo-hero.jpg', 'title': 'Golden Hour no Campo', 'desc': 'Luz suave de fim de tarde que valoriza o abraço espontâneo e a leveza do vestido.'},
            {'img': 'assets/photo-ceremony.jpg', 'title': 'A Entrada Emocionante da Noiva', 'desc': 'Olhares cruzados, lágrimas contidas e o altar repleto de emoção genuína.'},
            {'img': 'assets/photo-rings.jpg', 'title': 'Detalhes Macro das Alianças', 'desc': 'Fotografia artística de alianças, convites e arranjos florais com lente macro.'},
            {'img': 'assets/photo-couple-dance.jpg', 'title': 'A Dança dos Noivos na Festa', 'desc': 'Primeira dança iluminada por velas e luzes de conto de fadas com movimento fluido.'}
        ],
        'faqs': [
            ('Quantas fotos são entregues ao casal?', 'Entregamos em média de 600 a 1.000 fotografias tratadas individualmente em alta resolução.'),
            ('Qual é o prazo de entrega?', 'Enviamos uma prévia com 30 fotos em até 48 horas e a galeria completa tratada em até 20 dias úteis.'),
            ('Vocês viajam para Destination Weddings?', 'Sim! Atendemos casamentos em todo o Brasil e no exterior com logística simplificada.')
        ],
        'reviews': [
            ('Beatriz & Gabriel', 'As fotos parecem cenas de cinema! Revivemos cada segundo do casamento ao olhar o álbum.', '⭐⭐⭐⭐⭐'),
            ('Camila & Rodrigo', 'Lucas e Helena nos deixaram super à vontade. Nenhuma foto pareceu forçada.', '⭐⭐⭐⭐⭐')
        ]
    },
    'lavanderia': {
        'schema_type': 'DryCleaningOrLaundry',
        'business_name': 'LavaClean Express • Lavanderia Sustentável',
        'desc': 'Lavanderia moderna com higienização bactericida a vapor, planos mensais e delivery leva e traz.',
        'accent_color': 'cyan',
        'gallery_title': 'Tecnologia em Cuidado Têxtil',
        'gallery_subtitle': 'Lavagem ecológica que preserva as fibras, cores e remove até 99,9% dos ácaros e bactérias.',
        'gallery': [
            {'img': 'assets/laundry-hero.jpg', 'title': 'Máquinas Industriais Inteligentes', 'desc': 'Ciclos dosados por computador com economia de 40% de água e sem agressão aos tecidos.'},
            {'img': 'assets/laundry-machines.jpg', 'title': 'Higienização a Vapor de Alta Temperatura', 'desc': 'Desinfecção profunda para edredons, cobertores, ternos e vestidos de festa.'},
            {'img': 'assets/laundry-folded.jpg', 'title': 'Passadoria Artesanal com Dobra Perfeita', 'desc': 'Roupas embaladas a vácuo ou cabides protetores prontas para ir direto ao closet.'},
            {'img': 'assets/laundry-steam.jpg', 'title': 'Tratamento Especial para Roupas Finas', 'desc': 'Limpeza a seco especializada para sedas, lãs, couros e peças delicadas.'}
        ],
        'faqs': [
            ('Como funciona o serviço de Leva e Traz?', 'Agende pelo WhatsApp que nosso motorista retira as roupas na sua casa e devolve limpas e passadas em 48h.'),
            ('Quais produtos vocês utilizam na lavagem?', 'Usamos insumos hipoalergênicos e biodegradáveis com pH neutro que não agridem a pele nem o meio ambiente.'),
            ('Vocês lavam edredons e cortinas grandes?', 'Sim! Nossos tambores industriais comportam peças volumosas até King Size sem amarrotar.')
        ],
        'reviews': [
            ('Juliana Vasques', 'O plano mensal salvou minha rotina. As camisas voltam impecavelmente passadas!', '⭐⭐⭐⭐⭐'),
            ('Marcelo Ramos', 'Edredom king limpo e com cheirinho suave maravilhoso. Super recomendo o delivery.', '⭐⭐⭐⭐⭐')
        ]
    },
    'contador': {
        'schema_type': 'AccountingService',
        'business_name': 'Exata Contábil & Consultoria Fiscal',
        'desc': 'Contabilidade consultiva, abertura rápida de empresas, planejamento tributário e redução legal de impostos.',
        'accent_color': 'emerald',
        'gallery_title': 'Gestão Contábil Estratégica',
        'gallery_subtitle': 'Relatórios em tempo real, assessoria para Simples Nacional, Lucro Presumido e BPO Financeiro.',
        'gallery': [
            {'img': 'assets/contador-hero.jpg', 'title': 'Planejamento Tributário Inteligente', 'desc': 'Análise da carga tributária para enquadramento na opção mais econômica e 100% legal.'},
            {'img': 'assets/contador-laptop.jpg', 'title': 'Plataforma 100% Digital em Nuvem', 'desc': 'Acesso a holerites, guias de impostos e DRE da sua empresa a um clique no smartphone.'},
            {'img': 'assets/contador-charts.jpg', 'title': 'BPO Financeiro & Fluxo de Caixa', 'desc': 'Terceirização das contas a pagar, receber e conciliação bancária diária sem erros.'},
            {'img': 'assets/contador-meeting.jpg', 'title': 'Consultoria Consultiva com Especialistas', 'desc': 'Reuniões mensais de alinhamento com contadores seniores para decisões de crescimento.'}
        ],
        'faqs': [
            ('Como migrar de contador sem complicações?', 'Cuidamos de 100% da transição com seu contador anterior sem que você precise se preocupar com burocracia.'),
            ('Quanto tempo leva para abrir um CNPJ?', 'Em média abrimos sua empresa em até 3 a 5 dias úteis com todas as licenças e certidões ativas.'),
            ('Vocês atendem MEI, ME e EPP?', 'Sim! Temos planos sob medida para prestadores de serviços, médicos, advogados, e-commerces e pequenas indústrias.')
        ],
        'reviews': [
            ('Roberto Silveira', 'Economizamos mais de R$ 40 mil no primeiro ano apenas com o reenquadramento tributário.', '⭐⭐⭐⭐⭐'),
            ('Dra. Vanessa Luz', 'Gestão contábil impecável da minha clínica médica. Sempre disponíveis pelo WhatsApp.', '⭐⭐⭐⭐⭐')
        ]
    },
    'professor-idiomas': {
        'schema_type': 'EducationalOrganization',
        'business_name': 'Polyglot Academy • Ensino Personalizado de Idiomas',
        'desc': 'Aulas particulares de Inglês, Espanhol e Francês focadas em fluência rápida, viagens e negócios.',
        'accent_color': 'blue',
        'gallery_title': 'Metodologia Prática & Foco em Conversação',
        'gallery_subtitle': 'Sem regras gramaticais cansativas: você fala o idioma desde a primeira aula com situações reais.',
        'gallery': [
            {'img': 'assets/idiomas-hero.jpg', 'title': 'Conversação Imersiva 1-on-1', 'desc': 'Treinamento de pronúncia e vocabulário natural aplicado à sua profissão e objetivos.'},
            {'img': 'assets/idiomas-class.jpg', 'title': 'Business English para Reuniões', 'desc': 'Preparação para entrevistas de emprego em multinacionais, e-mails executivos e apresentações.'},
            {'img': 'assets/idiomas-online.jpg', 'title': 'Flexibilidade Total Presencial ou Online', 'desc': 'Plataforma interativa com gravações das aulas, feedbacks de pronúncia e tarefas digitais.'},
            {'img': 'assets/idiomas-books.jpg', 'title': 'Material Didático Internacional Exclusivo', 'desc': 'Conteúdos da Universidade de Cambridge e Oxford adaptados ao seu ritmo de aprendizado.'}
        ],
        'faqs': [
            ('Em quanto tempo consigo atingir a fluência?', 'Com o método imersivo de 2 aulas por semana, nossos alunos atingem segurança em conversação em 6 a 9 meses.'),
            ('As aulas são gravadas?', 'Sim! Nas aulas online você recebe o link da gravação para revisar quantas vezes desejar.'),
            ('Posso cancelar ou reagendar aulas?', 'Com aviso de até 2 horas de antecedência, remarcamos sua aula sem qualquer taxa extra.')
        ],
        'reviews': [
            ('Lucas Meneses', 'Passei na entrevista de emprego para a empresa nos EUA depois de apenas 4 meses de aula!', '⭐⭐⭐⭐⭐'),
            ('Fernanda Bastos', 'Perdi totalmente o medo de falar em reuniões. O professor é extremamente paciente e didático.', '⭐⭐⭐⭐⭐')
        ]
    },
    'professor-musica': {
        'schema_type': 'EducationalOrganization',
        'business_name': 'Harmonia Instituto Musical',
        'desc': 'Aulas práticas de Piano, Violão, Guitarra e Canto com metodologia moderna e repertório do aluno.',
        'accent_color': 'violet',
        'gallery_title': 'Aprenda Tocando suas Músicas Favoritas',
        'gallery_subtitle': 'Aulas dinâmicas que unem técnica instrumental, percepção auditiva e prática no instrumento.',
        'gallery': [
            {'img': 'assets/musica-hero.jpg', 'title': 'Estúdio Acústico Equipado', 'desc': 'Instrumentos de alta performance, microfones profissionais e isolamento sonoro para sua prática.'},
            {'img': 'assets/musica-piano.jpg', 'title': 'Piano & Teclado para Todas as Idades', 'desc': 'Da postura correta à leitura rápida de partituras e cifras populares com harmonia moderna.'},
            {'img': 'assets/musica-guitar.jpg', 'title': 'Violão & Guitarra Acústica/Elétrica', 'desc': 'Técnicas de dedilhado, solos, batidas rítmicas e improvisação no seu estilo predileto.'},
            {'img': 'assets/musica-studio.jpg', 'title': 'Gravação de Áudio das Suas Apresentações', 'desc': 'Grave seus próprios covers e composições com qualidade profissional no estúdio da escola.'}
        ],
        'faqs': [
            ('Preciso ter meu próprio instrumento para começar?', 'Para as primeiras semanas você pode utilizar os instrumentos do nosso estúdio até escolher o seu.'),
            ('Adultos sem experiência prévia conseguem aprender?', 'Com certeza! Mais de 60% dos nossos alunos começaram do absoluto zero na fase adulta.'),
            ('Vocês realizam apresentações e recitais?', 'Sim, organizamos recitais semestrais em teatros para que os alunos vivenciem a emoção do palco.')
        ],
        'reviews': [
            ('Clara Duarte', 'Sempre sonhei em tocar piano. Em 3 meses já consigo tocar minhas músicas favoritas!', '⭐⭐⭐⭐⭐'),
            ('Marcos Vinícius', 'Professor nota mil! Didática leve, sem enrolação teórica chata.', '⭐⭐⭐⭐⭐')
        ]
    },
    'professor-particular': {
        'schema_type': 'EducationalOrganization',
        'business_name': 'Nota 10 Aulas & Mentoria Escolar',
        'desc': 'Reforço escolar personalizado em Matemática, Física, Química e Português para Ensino Fundamental, Médio e ENEM.',
        'accent_color': 'indigo',
        'gallery_title': 'Resultados Comprovados em Notas & Confiança',
        'gallery_subtitle': 'Identificação precisa das lacunas de aprendizado com metodologia que ensina a raciocinar.',
        'gallery': [
            {'img': 'assets/mentor-hero.jpg', 'title': 'Mentoria Individual Focada em Objetivos', 'desc': 'Plano de estudo semanal com exercícios comentados e acompanhamento direto das notas escolares.'},
            {'img': 'assets/mentor-study.jpg', 'title': 'Resolução de Dúvidas Passo a Passo', 'desc': 'Técnicas que desmistificam equações, cálculos e fórmulas de forma lógica e compreensível.'},
            {'img': 'assets/mentor-laptop.jpg', 'title': 'Acompanhamento Online & Presencial', 'desc': 'Material digital com simulados das melhores escolas e vestibulares mais concorridos.'},
            {'img': 'assets/mentor-success.jpg', 'title': 'Preparação Estratégica para o ENEM e Vestibulares', 'desc': 'Treinamento de gestão do tempo de prova e estratégias da Teoria de Resposta ao Item (TRI).'}
        ],
        'faqs': [
            ('Vocês ajudam nas tarefas e trabalhos escolares?', 'Sim! Ajudamos a compreender o conteúdo por trás das lições de casa e nos preparamos para as provas.'),
            ('Os pais recebem relatórios de evolução?', 'Enviamos feedback semanal aos responsáveis pelo WhatsApp relatando o progresso e notas alcançadas.'),
            ('Como funcionam os plantões de véspera de prova?', 'Disponibilizamos horários intensivos focados no conteúdo exato da prova que o aluno terá no dia seguinte.')
        ],
        'reviews': [
            ('Helena Barreto (Mãe do Pedro)', 'O Pedro subiu de 4,5 para 9,0 em Matemática logo no primeiro bimestre. O professor é fantástico!', '⭐⭐⭐⭐⭐'),
            ('Lucas Andrade (Aluno ENEM)', 'Consegui 880 em Matemática no ENEM graças aos simulados e dicas de raciocínio rápido.', '⭐⭐⭐⭐⭐')
        ]
    },
    'quiropraxista': {
        'schema_type': 'Chiropractic',
        'business_name': 'Coluna Viva • Quiropraxia Clínica',
        'desc': 'Clínica de quiropraxia especializada no tratamento de hérnia de disco, dor ciática, postura e alívio de tensões.',
        'accent_color': 'teal',
        'gallery_title': 'Tratamento Especializado da Coluna Vertebral',
        'gallery_subtitle': 'Ajustes quiropráticos seguros com macas de drop e tração computadorizada para alívio imediato.',
        'gallery': [
            {'img': 'assets/quiro-hero.jpg', 'title': 'Maca de Drop & Tecnologia Quiroprática', 'desc': 'Equipamentos modernos que proporcionam ajustes articulares precisos com máximo conforto.'},
            {'img': 'assets/quiro-spine.jpg', 'title': 'Descompressão da Coluna & Hérnia de Disco', 'desc': 'Alívio da pressão sobre os discos vertebrais e nervo ciático sem cirurgias invasivas.'},
            {'img': 'assets/quiro-clinic.jpg', 'title': 'Consultório Clínico Acolhedor', 'desc': 'Ambiente calmo, higienizado e projetado para um atendimento relaxante e individual.'},
            {'img': 'assets/quiro-wellness.jpg', 'title': 'Recuperação Postural & Mobilidade', 'desc': 'Exercícios complementares de fortalecimento para manutenção da estabilidade da coluna.'}
        ],
        'faqs': [
            ('O ajuste quiroprático dói?', 'Não! O ajuste é rápido e indolor. A grande maioria dos pacientes relata alívio imediato da pressão nas costas.'),
            ('O que é o barulho de estalo no ajuste?', 'É apenas a liberação de bolhas de gás (cavitação) do líquido sinovial dentro da cápsula articular.'),
            ('Quantas sessões são necessárias?', 'Varia de acordo com o caso, mas uma avaliação inicial define o protocolo exato para remissão dos sintomas.')
        ],
        'reviews': [
            ('Tatiane Fonseca', 'Cheguei travada com crise no ciático e saí andando normalmente. Profissional espetacular!', '⭐⭐⭐⭐⭐'),
            ('Eduardo Prado', 'Minhas dores de cabeça tensionais e rigidez no pescoço desapareceram após 3 semanas.', '⭐⭐⭐⭐⭐')
        ]
    },
    'acupunturista': {
        'schema_type': 'MedicalClinic',
        'business_name': 'Equilíbrio Oriental • Acupuntura & Medicina Tradicional Chinesa',
        'desc': 'Tratamentos integrativos com acupuntura médica, ventosaterapia, moxabustão e alívio de estresse e dores crônicas.',
        'accent_color': 'emerald',
        'gallery_title': 'Harmonia entre Corpo, Mente e Energia',
        'gallery_subtitle': 'Agulhas siliconadas ultrafinas descartáveis em pontos de meridianos para alívio duradouro.',
        'gallery': [
            {'img': 'assets/acup-hero.jpg', 'title': 'Acupuntura Tradicional sem Dor', 'desc': 'Aplicação precisa em pontos neurorreativos que estimulam a liberação de endorfinas naturais.'},
            {'img': 'assets/acup-needles.jpg', 'title': 'Material 100% Descartável e Esterilizado', 'desc': 'Agulhas descartáveis de uso único com guia de aplicação suave para máximo conforto.'},
            {'img': 'assets/acup-zen.jpg', 'title': 'Ambiente Aromaterápico e Zen', 'desc': 'Música suave, aromaterapia relaxante e iluminação terapêutica durante toda a sessão.'},
            {'img': 'assets/acup-stones.jpg', 'title': 'Ventosaterapia & Pedras Quentes', 'desc': 'Desintoxicação miofascial e alívio profundo de nós musculares nas costas e pescoço.'}
        ],
        'faqs': [
            ('A agulha de acupuntura causa dor?', 'As agulhas são tão finas quanto fios de cabelo. A sensação é de leve formigamento ou calor relaxante.'),
            ('Para quais problemas a acupuntura é indicada?', 'Dores lombares, ansiedade, insônia, enxaqueca, fibromialgia, estresse e regulação do ciclo hormonal.'),
            ('A acupuntura é reconhecida pela OMS e Conselho Médico?', 'Sim! A Organização Mundial da Saúde e os conselhos federais de saúde chancelam a prática.')
        ],
        'reviews': [
            ('Sabrina Paiva', 'Minha crise de ansiedade e insônia melhorou desde a primeira consulta. Saio renovada a cada sessão.', '⭐⭐⭐⭐⭐'),
            ('Jorge Antunes', 'As dores crônicas na lombar sumiram. Recomendo de olhos fechados!', '⭐⭐⭐⭐⭐')
        ]
    },
    'dentista': {
        'schema_type': 'Dentist',
        'business_name': 'Lumina Dental OS • Odontologia Estética & Implantes',
        'desc': 'Odontologia de alta precisão com scanner 3D intraoral, lentes de contato dentais, implantes e clareamento a laser.',
        'accent_color': 'cyan',
        'gallery_title': 'Tecnologia & Estética para o Seu Sorriso',
        'gallery_subtitle': 'Planejamento digital do sorriso com conforto absoluto e atendimento sem dor.',
        'gallery': [
            {'img': 'assets/dentist-hero.jpg', 'title': 'Lentes de Contato em Porcelana', 'desc': 'Correção milimétrica de formato, cor e alinhamento dos dentes com naturalidade máxima.'},
            {'img': 'assets/dental-chair.jpg', 'title': 'Cadeiras Odontológicas Ergonômicas', 'desc': 'Equipamentos de última geração com sedação consciente para pacientes que têm medo de dentista.'},
            {'img': 'assets/dental-scanner-tech.jpg', 'title': 'Scanner Intraoral Digital 3D', 'desc': 'Mapeamento computadorizado da boca em minutos sem a necessidade daquela massinha incômoda.'},
            {'img': 'assets/smile-makeover.jpg', 'title': 'Clareamento Dental a Laser de Consultório', 'desc': 'Sorrisos até 5 tons mais claros em uma única sessão com gel de proteção contra sensibilidade.'}
        ],
        'faqs': [
            ('O tratamento com lentes de contato desgasta muito o dente?', 'Utilizamos a técnica de preparo minimamente invasivo preservando a estrutura saudável do esmalte.'),
            ('Como funciona a sedação consciente?', 'Indicada para pacientes com ansiedade, proporciona relaxamento profundo com monitoramento vital contínuo.'),
            ('Qual o tempo de recuperação de um implante guiado?', 'Com a cirurgia guiada por computador, a recuperação é extremamente rápida e quase sem inchaço.')
        ],
        'reviews': [
            ('Débora Linhares', 'Fiz minhas facetas de porcelana e o resultado ficou super natural. Atendimento nota 1000!', '⭐⭐⭐⭐⭐'),
            ('Gustavo Meira', 'Tinha trauma de dentista mas a sedação me fez não sentir absolutamente nada. Recomendo!', '⭐⭐⭐⭐⭐')
        ]
    },
    'gtmotors': {
        'schema_type': 'AutoDealer',
        'business_name': 'GT Motors Brasil • Veículos Premium & Esportivos',
        'desc': 'Showroom especializado em carros esportivos e blindados com laudo cautelar 100% aprovado.',
        'accent_color': 'red',
        'gallery_title': 'Showroom de Veículos de Alta Performance',
        'gallery_subtitle': 'Seleção rigorosa com histórico de manutenção comprovado e garantia contratual.',
        'gallery': [
            {'img': 'assets/gt-hero.jpg', 'title': 'Superesportivos & Carros de Luxo', 'desc': 'Veículos revisados e higienizados prontos para entrega imediata no showroom.'},
            {'img': 'assets/gt-showroom.jpg', 'title': 'Espaço VIP & Lounge de Negociações', 'desc': 'Atendimento exclusivo com privacidade, café gourmet e consultoria financeira.'},
            {'img': 'assets/gt-supercar.jpg', 'title': 'Veículos Blindados Nível III-A', 'desc': 'Blindagens certificadas pelas melhores montadoras com vidros sem delaminação.'},
            {'img': 'assets/gt-detail.jpg', 'title': 'Detalhamento Estético & Vitrificação', 'desc': 'Proteção cerâmica na pintura que conserva o brilho espelhado da carroceria.'}
        ],
        'faqs': [
            ('Todos os carros possuem laudo cautelar?', 'Sim! 100% do nosso estoque passa por perícia cautelar Dekra e Supervisão sem nenhum apontamento.'),
            ('Vocês aceitam veículos na troca?', 'Sim, avaliamos seu veículo usado com base no mercado real com pagamento ou repasse imediato.'),
            ('É possível financiar com taxas reduzidas?', 'Operamos com os principais bancos do país com aprovação de crédito em minutos e parcelamento em até 60x.')
        ],
        'reviews': [
            ('Alexandre Bicalho', 'Comprei uma BMW M3 impecável. Transparência total da equipe e entrega impecável.', '⭐⭐⭐⭐⭐'),
            ('Vinícius Morais', 'Melhor pós-venda que já vi no segmento premium. Laudo 100% aprovado e carro como novo.', '⭐⭐⭐⭐⭐')
        ]
    },
    'concessionaria-honda': {
        'schema_type': 'AutoDealer',
        'business_name': 'AutoDrive Honda OS • Concessionária & Oficina Especializada',
        'desc': 'Motos e carros Honda zero km e seminovos revisados com planos de consórcio e oficina técnica oficial.',
        'accent_color': 'red',
        'gallery_title': 'A Linha Completa Honda para Você',
        'gallery_subtitle': 'Motos econômicas para o dia a dia e modelos de alta cilindrada com condições exclusivas de financiamento.',
        'gallery': [
            {'img': 'assets/honda-hero.jpg', 'title': 'Motos Honda Zero KM Pronta Entrega', 'desc': 'CG 160 Titan, CB 300F Twister e CB 500F com emplacamento cortesia e garantia de 3 anos.'},
            {'img': 'assets/honda-showroom.jpg', 'title': 'Showroom Moderno & Peças Genuínas', 'desc': 'Equipe de consultores prontos para montar a melhor simulação de consórcio ou financiamento.'},
            {'img': 'assets/honda-moto-speed.jpg', 'title': 'Linha Esportiva & Aventura', 'desc': 'Motos de alta performance para quem busca emoção nas estradas e finais de semana.'},
            {'img': 'assets/honda-workshop.jpg', 'title': 'Oficina Credenciada & Revisão Rápida', 'desc': 'Mecânicos certificados pela fábrica com ferramentas eletrônicas e peças originais Honda.'}
        ],
        'faqs': [
            ('Como funciona o Consórcio Nacional Honda?', 'Planos sem juros com parcelas acessíveis e contemplações mensais por sorteio e lance livre.'),
            ('A concessionária aceita minha moto usada como entrada?', 'Sim! Avaliamos sua moto na hora e você já sai com a Honda zero km.'),
            ('A garantia de fábrica é mantida?', 'Todas as motos novas contam com garantia de 3 anos Honda e óleo Pro Honda gratuito nas primeiras revisões.')
        ],
        'reviews': [
            ('Bruno Fagundes', 'Tirei minha CG 160 Titan no consórcio em menos de 3 meses com lance embutido. Atendimento nota 10!', '⭐⭐⭐⭐⭐'),
            ('Larissa Menezes', 'Oficina rápida e transparente. Fizeram a revisão da minha moto e entregaram lavada.', '⭐⭐⭐⭐⭐')
        ]
    },
    'personal-trainer': {
        'schema_type': 'HealthClub',
        'business_name': 'ProFit Performance • Treinamento Personalizado',
        'desc': 'Consultoria fitness individualizada para emagrecimento, hipertrofia e condicionamento físico de alta intensidade.',
        'accent_color': 'emerald',
        'gallery_title': 'Treinamento Inteligente com Resultados Reais',
        'gallery_subtitle': 'Biomecânica correta, progressão de carga sem lesões e suporte diário via aplicativo exclusivo.',
        'gallery': [
            {'img': 'assets/trainer-hero.jpg', 'title': 'Treino Personalizado 1-on-1', 'desc': 'Acompanhamento lado a lado com correção postural imediata e estímulo de alta intensidade.'},
            {'img': 'assets/trainer-session.jpg', 'title': 'Hipertrofia & Ganho de Massa Magra', 'desc': 'Periodização de força estruturada com base na sua rotina e tempo disponível para treinar.'},
            {'img': 'assets/trainer-weights.jpg', 'title': 'Equipamentos Livres e Funcionais', 'desc': 'Exercícios eficientes com barras, halteres e pesos livres que ativam mais grupos musculares.'},
            {'img': 'assets/trainer-cardio.jpg', 'title': 'Cardio Estratégico & Queima de Gordura', 'desc': 'Protocolos HIIT que aceleram o metabolismo sem perda de massa muscular magra.'}
        ],
        'faqs': [
            ('Iniciantes sedentários podem começar?', 'Sim! Montamos um período de adaptação neuromotora respeitando seus limites articulares para evitar lesões.'),
            ('O acompanhamento inclui plano alimentar?', 'Trabalhamos em parceria com nutricionistas esportivos para alinhar seus macros às metas do treino.'),
            ('Como funciona a consultoria online?', 'Você recebe seu treino montado em aplicativo com vídeos tutoriais e faz check-ins semanais de evolução.')
        ],
        'reviews': [
            ('Rodrigo Simas', 'Perdi 12kg em 4 meses sem loucuras e ganhei uma disposição incrível no dia a dia.', '⭐⭐⭐⭐⭐'),
            ('Ana Clara Vieira', 'Treinos dinâmicos e que não enjoam. O melhor personal trainer que já tive!', '⭐⭐⭐⭐⭐')
        ]
    }
}

print(f"Configurations prepared for {len(NICHES_DATA)} niches.")

