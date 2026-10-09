# Recôncavo Culinária — site institucional

Site estático de apresentação do Recôncavo Culinária, preparado para publicação no GitHub Pages.

A nova direção visual combina creme, verde de raiz, açafrão e terracota com tipografia editorial, fotografia real da casa, cardápio em destaque e uma experiência cultural sofisticada e responsiva.

## Verificar localmente

Com Python instalado, execute na pasta do projeto:

```bash
python -m http.server 4173
```

Depois abra `http://127.0.0.1:4173` no navegador.

## O que está incluído

- Hero editorial com a promessa “Sabores que nascem do Recôncavo”.
- Seção de identidade com os valores de ingrediente, memória e produção artesanal.
- Prévia de seis nomes de pratos identificados no cardápio público, sem preços inventados.
- CTA para o cardápio oficial no Strelo em vários pontos da página.
- Seções de experiência cultural, galeria, história, FAQ, mapa e contato.
- WhatsApp, telefone, Instagram, endereço e horários confirmados.
- SEO local com `Restaurant` e `FAQPage` em JSON-LD, Open Graph, Twitter Card, manifesto e robots.
- Menu mobile, animações de entrada, parallax leve, progresso de scroll e suporte a `prefers-reduced-motion`.

## Publicar no GitHub Pages

1. Crie um repositório público no GitHub.
2. Envie os arquivos desta pasta para a branch `main`.
3. No repositório, abra **Settings → Pages**.
4. Em **Build and deployment**, escolha **Deploy from a branch**.
5. Selecione `main` e `/ (root)`.
6. Salve e aguarde a URL `https://SEU-USUARIO.github.io/SEU-REPOSITORIO/`.

## Publicação e SEO

- `PROMPTS_IMAGENS.md` contém prompts prontos para gerar novas imagens com outra IA.
- `assets/og-image.jpg` é a imagem de compartilhamento para Open Graph/Twitter Card.
- `assets/presentation-cover.jpg` e `assets/cultura-galeria-v2.jpg` são composições locais feitas com as fotografias fornecidas.
- O HTML inclui `Restaurant` e `FAQPage` em JSON-LD, Open Graph, Twitter Card, manifesto, robots.txt e palavras-chave locais em texto visível.
- Após publicar, copie `sitemap.xml.template` para `sitemap.xml`, substitua `SEU-USUARIO/SEU-REPOSITORIO` e adicione a URL absoluta ao `robots.txt`.
- Para alguns coletores de redes sociais, prefira trocar `assets/og-image.jpg` por uma URL absoluta depois que o repositório existir.
- O mapa usa uma consulta embeddable do Google Maps, sem chave de API. Confirmar a política de uso antes de publicar.

## Conteúdo e direitos

- O cardápio de referência é o link oficial do Strelo: <https://reconcavoculinaria.strelo.com.br/loja/casa/>.
- Os destaques visuais do cardápio foram conferidos em referências públicas do menu; a seleção pode mudar. Valores, porções e disponibilidade devem ser confirmados no cardápio oficial.
- A nota numérica do Google não foi inventada: o site leva o visitante ao perfil público para ver a avaliação atual.
- Confirme autorização de uso do logotipo, das fotografias e das composições antes de publicar a versão final.
- Não há login, senha, checkout ou banco de dados.
