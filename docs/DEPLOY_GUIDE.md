# 🚀 Guia de Deploy do NEXUS FLOW

## Pré-requisitos

### Sistema Local
- [Python 3.10+](https://python.org/downloads)
- [Node.js 18+](https://nodejs.org/) (para Vercel CLI)
- [Git](https://git-scm.com/)
- Terminal com acesso à internet

### Contas Necessárias
- [GitHub](https://github.com/) (gratuito)
- [Vercel](https://vercel.com/) (gratuito para projetos públicos)

---

## Opção 1: Deploy Direto com Vercel CLI (Desenvolvimento/Teste)

### Etapa 1: Instalar Vercel CLI
```bash
npm install -g vercel
```

### Etapa 2: Login na Vercel
```bash
npx vercel login
```
> Abrirá navegador para autenticação

### Etapa 3: Deploy de Preview
```bash
cd F:\Nova\ pasta\NEXUS_FLOW_ORGANIZADO
npx vercel
```
- Cria deploy preview único
- URL: `https://nexus-flow-{hash}.vercel.app`
- Útil para testes e validação

### Etapa 4: Deploy de Produção
```bash
npx vercel --prod
```
- Deploy na branch de produção
- Perguntará para confirmar produção
- URL: `https://nexus-flow.vercel.app` (ou subdomínio customizado)

---

## Opção 2: GitHub + Vercel Dashboard (Produção/Time)

### Etapa 1: Preparar Repositório GitHub
```bash
# Inicializar repositório (se ainda não for)
git init

# Configurar usuário/email (se necessário)
git config user.name "Seu Nome"
git config user.email "seu@email.com"

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "feat: portfolio organizado - estrutura inicial"

# Adicionar remote (substitua pelo seu repo)
git remote add origin https://github.com/seu-usuario/nexus-flow-portfolio.git

# Fazer push
git push -u origin main
```

### Etapa 2: Configurar na Vercel
1. Acesse [vercel.com](https://vercel.com) e faça login
2. Clique em **"Add New Project"**
3. Selecione **"Import Git Repository"**
4. Escolha seu repositório `nexus-flow-portfolio`
5. **Deixe as configurações padrão** (Vercel detecta `vercel.json` automaticamente)
6. Clique em **"Deploy"**

### Etapa 3: Configurar Variáveis de Ambiente (Opcional)
Se quiser usar variáveis de ambiente no futuro:
1. No painel do projeto Vercel → **Settings** → **Environment Variables**
2. Adicione variáveis conforme necessário
3. Redeploy automático

### Etapa 4: Verificar Deploy
- Aguarde o build completar (2-5 minutos)
- Acesse a URL fornecida pela Vercel
- Teste:
  - Portal principal: `https://seu-projeto.vercel.app/`
  - Nicho exemplo: `https://seu-projeto.vercel.app/energia-solar/`
  - CRM exemplo: `https://seu-projeto.vercel.app/crm-vendas/`
  - Mobile: Redimensione a janela ou use DevTools

---

## Opção 3: Deploy Manual (Sem Vercel CLI)

### Para Ambientes Customizados
Se precisar deployar em outro servidor (NGINX, Apache, IIS):

1. **Build Local**
```bash
cd scripts
python build_clean_light_portal.py
python build_niche_db.py
```

2. **Copiar para Servidor**
- Tudo dentro de `NEXUS_FLOW_ORGANIZADO/` deve ser servido como estático
- Configurar servidor para servir `index.html` em rotas não encontradas (SPA fallback)

3. **Configurar Headers de Segurança** (recomendado)
```nginx
# Exemplo para NGINX
add_header X-Content-Type-Options nosniff;
add_header Referrer-Policy strict-origin-when-cross-origin;
```

---

## Scripts de Build Disponíveis

| Script | Descrição |
|--------|-----------|
| `scripts/build_clean_light_portal.py` | Gera `portal/index.html` com i18n, omnibar e catálogo dinâmico |
| `scripts/build_niche_db.py` | Gera base de dados de nichos para funcionalidades futuras |
| `scripts/niche_configs.py` | Pré-visualiza configurações de nicho |
| `scripts/originkit_data.py` | Mostra matrizes de comparação por nicho |
| `scripts/remaining_niches_data.py` | Mostra dados dos nichos restantes |

---

## Troubleshooting

### Problema: "404 em nicho específico"
**Solução**: 
1. Verifique se `niches/{nicho}/index.html` existe
2. Execute `python scripts/build_niche_db.py` para atualizar catálogo
3. Faça commit e push novamente

### Problema: "CSS/Tailwind não carregando"
**Solução**:
1. Verifique se `portal/assets/css/` existe
2. Confira se o `<script src="https://cdn.tailwindcss.com"></script>` está no `<head>`
3. Teste em modo incognito (evitar cache)

### Problema: "Falha no build do GitHub Actions"
**Solução**:
1. Verifique os logs do workflow em `.github/workflows/deploy.yml`
2. Confira se o Python 3.10+ está disponível no runner
3. Teste o build localmente primeiro
4. Verifique se `requirements.txt` ou dependências estão faltando

---

## URLs Padrão Após Deploy

| Tipo | URL Padrão |
|------|------------|
| Portal Principal | `https://{seu-subdominio}.vercel.app/` |
| Nicho | `https://{seu-subdominio}.vercel.app/{nicho}/` |
| CRM Vendas | `https://{seu-subdominio}.vercel.app/crm-vendas/` |
| CRM Serviços | `https://{seu-subdominio}.vercel.app/crm-servicos/` |
| Asset Preview | `https://{seu-subdominio}.vercel.app/assets/previews/{nicho}.png` |
| Build Logs | Ver nas Actions do GitHub |

---

## Customização de Domínio

### Adicionar Domínio Customizado na Vercel
1. No painel do projeto → **Domains**
2. Clique em **"Add"** → **"Domain"**
3. Digite seu domínio (ex: `nexusflow.app`)
4. Siga as instruções de DNS da Vercel
5. Aguarde propagação (5-30 minutos)

### Subdomínios para Nichos (Avançado)
Para `energia-solar.nexusflow.app`:
1. Configure CNAME no DNS apontando para `cname.vercel-dns.com`
2. No projeto Vercel → Domains → Add Domain
3. Adicione `energia-solar.nexusflow.app`
4. Vercel servirá automaticamente do caminho correto

---

## Manutenção Contínua

### Atualização Semanal Recomendada
```bash
# 1. Pull últimas mudanças
git pull origin main

# 2. Testar build local
cd scripts
python build_clean_light_portal.py
python build_niche_db.py

# 3. Commit se houver mudanças locais
git add .
git commit -m "maintenance: atualização local"
git push origin main

# 4. Vercel faz deploy automático
```

### Backup do Banco de Dados (se aplicável)
O arquivo `projects_catalog.json` é a fonte da verdade:
- Mantenha versionado no Git
- Faça backup ocasional em backups/
- Nunca edite manualmente sem entender o impacto

---

## Suporte

Para problemas de deploy:
1. Verifique os **Logs do GitHub Actions**
2. Check **Vercel Deployment Logs**
3. Teste o build localmente primeiro
4. Consulte `docs/ARCHITECTURE.md` para detalhes técnicos

---
*Guia atualizado em: $(date +%Y-%m-%d)*