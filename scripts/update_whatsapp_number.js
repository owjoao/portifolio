const fs = require('fs');
const path = require('path');

const targetNumber = '5532999292311';
const formattedNumber = '(32) 99929-2311';
const rawMessage = 'gostei desse site, qual o valor?';
const encodedUrl = `https://wa.me/${targetNumber}?text=${encodeURIComponent(rawMessage)}`;

// 1. Update nutricionista/index.html
const nutriPath = path.resolve(__dirname, '../nutricionista/index.html');
if (fs.existsSync(nutriPath)) {
  let content = fs.readFileSync(nutriPath, 'utf8');

  // Replace visible phone numbers
  content = content.replace(/\(11\)\s*99853-1124/g, formattedNumber);

  // Replace any wa.me links
  content = content.replace(/https:\/\/wa\.me\/5532999292311[^\s"'>]*/g, encodedUrl);
  content = content.replace(/https:\/\/wa\.me\/[0-9]{10,13}[^\s"'>]*/g, encodedUrl);

  // In the IMC calculator script
  content = content.replace(
    /document\.getElementById\('btn-imc-whatsapp'\)\.href\s*=\s*['"][^'"]+['"]\s*\+\s*encodeURIComponent\(msg\);/g,
    `document.getElementById('btn-imc-whatsapp').href = 'https://wa.me/${targetNumber}?text=' + encodeURIComponent('${rawMessage}');`
  );

  fs.writeFileSync(nutriPath, content, 'utf8');
  console.log('✅ Updated nutricionista/index.html');
}

// 2. Update master hub index.html
const masterPath = path.resolve(__dirname, '../index.html');
if (fs.existsSync(masterPath)) {
  let content = fs.readFileSync(masterPath, 'utf8');
  content = content.replace(/https:\/\/wa\.me\/5532999292311[^\s"'>]*/g, encodedUrl);
  content = content.replace(/\(11\)\s*99853-1124/g, formattedNumber);
  fs.writeFileSync(masterPath, content, 'utf8');
  console.log('✅ Updated master index.html');
}

// 3. Update all niche sites with the new WhatsApp number & message
const rootDir = path.resolve(__dirname, '..');
const dirs = fs.readdirSync(rootDir, { withFileTypes: true });

for (const d of dirs) {
  if (!d.isDirectory()) continue;
  if (['node_modules', '.git', 'scripts', 'assets'].includes(d.name)) continue;

  const siteHtml = path.join(rootDir, d.name, 'index.html');
  if (fs.existsSync(siteHtml)) {
    let html = fs.readFileSync(siteHtml, 'utf8');
    let modified = false;

    if (html.includes('5532999292311') || html.includes('99853-1124')) {
      html = html.replace(/\(11\)\s*99853-1124/g, formattedNumber);
      html = html.replace(/https:\/\/wa\.me\/5532999292311[^\s"'>]*/g, encodedUrl);
      modified = true;
    }

    if (modified) {
      fs.writeFileSync(siteHtml, html, 'utf8');
      console.log(`✅ Updated ${d.name}/index.html`);
    }
  }
}
