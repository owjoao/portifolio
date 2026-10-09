const fs = require('fs');
const sites = ['energia-solar', 'dentista', 'advogado', 'concessionaria-honda', 'arquiteto', 'banho-e-tosa', 'barbearia', 'corretor-imoveis'];

sites.forEach(s => {
  const file = s + '/index.html';
  if (!fs.existsSync(file)) {
    console.log(s, 'does not exist');
    return;
  }
  const content = fs.readFileSync(file, 'utf8');
  const title = (content.match(/<title>(.*?)<\/title>/i) || [])[1] || 'no title';
  const fonts = (content.match(/family=([^&"']+)/g) || []).map(f => f.replace('family=', ''));
  const heroMatch = content.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
  const heroText = heroMatch ? heroMatch[1].replace(/<[^>]+>/g, '').trim().slice(0, 80) : 'no h1';
  const bgColors = (content.match(/bg-\[(#[a-zA-Z0-9]+)\]/g) || []).slice(0, 5);
  
  console.log(`=== ${s.toUpperCase()} ===`);
  console.log('Title:', title.slice(0, 70));
  console.log('Fonts:', fonts.join('; '));
  console.log('H1:', heroText.replace(/\s+/g, ' '));
  console.log('Custom BGs:', bgColors.join(', '));
  console.log('Lines:', content.split('\n').length);
  console.log('');
});
