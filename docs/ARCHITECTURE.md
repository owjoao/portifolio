# 🏗️ Arquitetura do Sistema NEXUS FLOW

## Visão Geral

O NEXUS FLOW é um ecossistema de engenharia digital composto por:
- **Portal Central** (Hub de navegação com i18n + Omnibar)
- **36 Landing Pages** de nicho (HTML estático, alta conversão)
- **2 CRMs Enterprise** (Sistemas desktop completos)
- **Pipeline de Build** (Python scripts para geração estática)
- **Deploy Automatizado** (Vercel + GitHub Actions)

---

## Estrutura de Diretórios

```
NEXUS_FLOW_ORGANIZADO/
├── portal/                      # Ponto de entrada único
│   ├── index.html              # SPA com navegação por hash/history
│   ├── vercel.json             # Rotas limpas (rewrite)
│   └── assets/                 # Assets globais compartilhados
├── niches/                      # Landing pages isoladas por nicho
│   └── {nicho}/
│       ├── index.html          # Landing page principal
│       └── admin/              # Painel CRM embutido (quando aplicável)
│           └── index.html
├── crms/                        # CRMs standalone
│   ├── crm-vendas/
│   │   └── index.html
│   └── crm-servicos/
│       └── index.html
├── shared/                      # Código compartilhado (DRY)
│   ├── design-tokens/          # JSON por nicho: cores, fontes, copy
│   ├── components/             # Componentes React reutilizáveis
│   └── templates/              # Jinja2 + WhatsApp templates
├── scripts/                     # Automação (Python)
│   ├── build_clean_light_portal.py
│   ├── build_niche_db.py
│   ├── projects_catalog.json
│   ├── niche_configs.py
│   ├── originkit_data.py
│   └── remaining_niches_data.py
└── .github/workflows/           # CI/CD
    └── deploy.yml
```

---

## Fluxo de Dados

### 1. Geração do Portal Principal
```
projects_catalog.json
       │
       ▼
build_clean_light_portal.py
       │
       ▼
portal/index.html (com i18n, omnibar, catálogo dinâmico)
```

### 2. Geração de Nicho Individual
```
niche_configs.py / remaining_niches_data.py
       │
       ▼
Template Jinja2 (shared/templates/base.html.j2)
       │
       ▼
niches/{nicho}/index.html
```

### 3. Deploy Vercel
```
Git Push → GitHub Actions → Vercel CLI → Preview/Production
```

---

## Convenções de Nomenclatura

| Item | Padrão | Exemplo |
|------|--------|---------|
| Pasta de nicho | kebab-case | `energia-solar` |
| Arquivo principal | `index.html` | `niches/energia-solar/index.html` |
| CRM embutido | `admin/index.html` | `niches/dentista/admin/index.html` |
| Assets de preview | `{nicho}.png` | `portal/assets/previews/energia-solar.png` |
| Tokens de design | `{nicho}.json` | `shared/design-tokens/energia-solar.json` |

---

## Tecnologias por Camada

| Camada | Tecnologias |
|--------|-------------|
| **Markup** | HTML5 semântico, Schema.org JSON-LD |
| **Estilos** | Tailwind CSS 3.4 (CDN), CSS Custom Properties |
| **Animações** | GSAP 3.12 + ScrollTrigger |
| **Ícones** | FontAwesome 6.5 (CDN) |
| **Fonts** | Plus Jakarta Sans, Outfit, JetBrains Mono (Google Fonts) |
| **i18n** | JavaScript vanilla + localStorage |
| **Build** | Python 3.10+, BeautifulSoup4, Jinja2 |
| **Deploy** | Vercel (Static + Edge Functions) |
| **CI/CD** | GitHub Actions + Vercel CLI |

---

## Requisitos de Sistema

- Python 3.10+
- Node.js 18+ (para Vercel CLI)
- Git
- Navegador moderno (ES2020+)

---

## Variáveis de Ambiente (Vercel)

| Variável | Descrição | Obrigatória |
|----------|-----------|-------------|
| `VERCEL_TOKEN` | Token de acesso da Vercel | Sim (CI/CD) |
| `VERCEL_ORG_ID` | ID da organização Vercel | Sim (CI/CD) |
| `VERCEL_PROJECT_ID` | ID do projeto Vercel | Sim (CI/CD) |

---

## Escalabilidade

### Adicionar Novo Nicho
1. Criar `shared/design-tokens/{novo-nicho}.json`
2. Adicionar entrada em `scripts/projects_catalog.json`
3. Adicionar config em `scripts/niche_configs.py` ou `remaining_niches_data.py`
4. Executar `python scripts/build_niche_db.py`
5. Commit + Push → Deploy automático

### Atualizar Portal Principal
1. Modificar `scripts/projects_catalog.json`
2. Executar `python scripts/build_clean_light_portal.py`
3. Commit + Push

---

## Segurança

- **Headers de Segurança**: Configurados via `vercel.json` (X-Content-Type-Options, Referrer-Policy)
- **CSP**: Não aplicado (scripts inline necessários para GSAP/Tailwind CDN)
- **HTTPS**: Forçado pela Vercel
- **Sanitização**: Entradas de usuário escapadas nos templates Jinja2

---

## Performance

- **Static Generation**: Todos os HTMLs pré-renderizados
- **CDN Global**: Vercel Edge Network
- **Lazy Loading**: Imagens com `loading="lazy"`
- **Code Splitting**: Não aplicável (vanilla JS)
- **Bundle Size**: ~0 KB JS próprio (CDN externo)
- **Core Web Vitals**: LCP < 2.5s, FID < 100ms, CLS < 0.1

---

## Monitoramento

- **Vercel Analytics**: Page views, Web Vitals
- **GitHub Actions**: Status de build/deploy
- **Error Tracking**: Console errors logados no build