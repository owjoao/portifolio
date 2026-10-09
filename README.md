# 🌐 NEXUS FLOW — Portfólio Organizado de Engenharia Digital

Portfólio corporativo e ecossistema de soluções digitais desenvolvido para apresentar sistemas de vendas, landing pages de alta conversão e CRMs especializados por segmento de mercado.

---

## 🏗️ Estrutura do Projeto

```
NEXUS_FLOW_ORGANIZADO/
├── portal/                      # Hub central (index.html principal)
│   ├── index.html               # Portal NEXUS FLOW com i18n (PT/EN/ES) + Omnibar
│   ├── vercel.json              # Configuração de rotas limpas da Vercel
│   └── assets/                  # Recursos visuais globais
│       ├── css/
│       ├── js/
│       └── previews/            # 36 thumbnails dos projetos
├── niches/                      # 36 Landing Pages de Nicho
│   ├── acupunturista/           # Shen Zen Medicina Oriental
│   ├── advogado/                # Valente & Associados (LexPro OS)
│   ├── arquiteto/               # ArtVista Wall Art
│   ├── banho-e-tosa/            # Pawly Pet Spa
│   ├── barbearia/               # Barber Club OS
│   ├── boteco-portugues/        # O Tasco Boteco Lusitano
│   ├── caxixi/                  # Bar & Restaurante Caxixi
│   ├── clinica-oftalmo/         # Clínica Oftalmológica
│   ├── concessionaria-honda/    # AutoDrive Honda OS
│   ├── contador/                # Exata Contábil
│   ├── corretor-imoveis/        # ImobMax OS
│   ├── dentista/                # Lumina Dental OS
│   ├── energia-solar/           # SunEco OS
│   ├── fotografo-casamento/     # Lumière Photography
│   ├── fumaca-motos/            # Fumaça Motos
│   ├── gtmotors/                # GT Motors Brasil
│   ├── lavanderia/              # LavaClean Express
│   ├── nutricionista/           # NutriViva
│   ├── oftalmologista/          # Instituto de Oftalmologia
│   ├── personal-trainer/        # ProFit Performance
│   ├── podologo/                # PodoSaúde
│   ├── professor-idiomas/       # Polyglot Academy
│   ├── professor-musica/        # Harmonia Instituto Musical
│   ├── professor-particular/    # Nota 10 Aulas
│   ├── psicologia/              # Mente Serena
│   ├── quiropraxista/           # Coluna Viva
│   ├── rampabike/               # Rampa Bike Especializada
│   ├── reconcavo/               # Recôncavo Culinária
│   ├── reforma-moveis/          # Ateliê Renova Móveis
│   ├── restaurante-egeu/        # Restaurante Egeu Mediterrâneo
│   ├── shineray-uba/            # Shineray Ubá
│   ├── topmotos032/             # TOP MOTOS 032
│   ├── vrum-motos/              # Vrum Motos
│   ├── sorveteria/              # SCOOPÉRA Gelato
│   ├── pizzaria_landingpage/    # Forneria Napolitana
│   └── lanchonete/              # SmashBurger Artesanal
├── crms/                        # 2 Sistemas CRM Enterprise
│   ├── crm-vendas/              # CRM Vendas & Veículos (Dark/Light, Margens)
│   └── crm-servicos/            # CRM Ordens de Serviço & Insumos por Lote
├── shared/                      # Componentes e tokens compartilhados
│   ├── design-tokens/           # Tokens de design por nicho (JSON)
│   ├── components/              # Componentes React reutilizáveis
│   └── templates/               # Templates Jinja2 + WhatsApp
├── scripts/                     # Automação de build e geração
│   ├── build_clean_light_portal.py   # Compilador principal do portal
│   ├── build_niche_db.py             # Gerador da base de dados de nichos
│   ├── projects_catalog.json         # Metadados dos 36 projetos
│   ├── niche_configs.py              # Configs detalhadas por nicho
│   ├── originkit_data.py             # Matrizes de comparação
│   ├── remaining_niches_data.py      # Dados nichos restantes
│   └── utils/                        # Utilitários diversos
├── docs/                        # Documentação técnica
│   ├── PORTFOLIO.md             # Catálogo detalhado
│   ├── ARCHITECTURE.md          # Arquitetura do sistema
│   ├── DEPLOY_GUIDE.md          # Guia de deploy
│   └── NICHE_REGISTRY.md        # Registro de nichos
├── .github/workflows/           # CI/CD para Vercel
│   └── deploy.yml
├── vercel.json                  # Configuração raiz (rewrite para /portal)
└── README.md
```

---

## 🚀 Deploy na Vercel

### Opção 1: Vercel CLI (Rápido)
```bash
cd NEXUS_FLOW_ORGANIZADO
npx vercel login
npx vercel          # Preview
npx vercel --prod   # Produção
```

### Opção 2: GitHub + Vercel Dashboard (Recomendado)
1. Crie repositório no GitHub
2. `git init && git add . && git commit -m "feat: portfolio organizado" && git push -u origin main`
3. Acesse [vercel.com](https://vercel.com) → **Add New Project** → Import GitHub Repo
4. Deploy automático a cada push na `main`

### URLs Resultantes
- **Portal Principal**: `https://seu-projeto.vercel.app/`
- **Nichos**: `https://seu-projeto.vercel.app/energia-solar/`, `/dentista/`, etc.
- **CRMs**: `https://seu-projeto.vercel.app/crm-vendas/`, `/crm-servicos/`

---

## 🛠️ Build Local

```bash
# Recompilar portal principal após mudanças
cd scripts
python build_clean_light_portal.py

# Gerar base de dados de nichos
python build_niche_db.py
```

---

## 📋 Catálogo Completo

Consulte [`docs/PORTFOLIO.md`](docs/PORTFOLIO.md) para a tabela detalhada de todos os 36 nichos com links diretos, tecnologias e recursos de conversão.

---

## 🔧 Tecnologias

- **Frontend**: HTML5, Tailwind CSS 3.4+, GSAP 3.12, FontAwesome 6.5
- **Fonts**: Plus Jakarta Sans, Outfit, JetBrains Mono
- **Animações**: GSAP + ScrollTrigger (cinematic intro < 2.3s)
- **i18n**: PT-BR, EN-US, ES-ES (localStorage persistence)
- **Deploy**: Vercel (Clean URLs via `vercel.json`)
- **Build**: Python scripts para geração estática

---

## 📱 Contato Unificado

WhatsApp Oficial: `(32) 99929-2311` → `5532999292311`

---

## 📄 Licença

Proprietário — NEXUS FLOW Engenharia Digital & Sistemas de Vendas