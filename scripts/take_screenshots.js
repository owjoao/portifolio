const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const PREVIEWS_DIR = path.resolve(__dirname, '..', 'assets', 'previews');
if (!fs.existsSync(PREVIEWS_DIR)) {
  fs.mkdirSync(PREVIEWS_DIR, { recursive: true });
}

// First, copy user uploaded image specifically for energia-solar as well
const userUploadImg = 'C:/Users/jvna1/.gemini/antigravity/brain/b28a8cf9-f9da-40fd-96f7-f4464143af22/.user_uploaded/media_1790720503636.png';
if (fs.existsSync(userUploadImg)) {
  fs.copyFileSync(userUploadImg, path.join(PREVIEWS_DIR, 'energia-solar.png'));
  console.log('✅ Copied user uploaded image to assets/previews/energia-solar.png');
}

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

const SITES = [
  { id: 'dentista', url: 'http://localhost:8080/dentista/index.html' },
  { id: 'advogado', url: 'http://localhost:8080/advogado/index.html' },
  { id: 'concessionaria-honda', url: 'http://localhost:8080/concessionaria-honda/index.html' },
  { id: 'arquiteto', url: 'http://localhost:8080/arquiteto/index.html' },
  { id: 'banho-e-tosa', url: 'http://localhost:8080/banho-e-tosa/index.html' },
  { id: 'barbearia', url: 'http://localhost:8080/barbearia/index.html' },
  { id: 'corretor-imoveis', url: 'http://localhost:8080/corretor-imoveis/index.html' }
];

for (const site of SITES) {
  const dest = path.join(PREVIEWS_DIR, `${site.id}.png`);
  console.log(`Taking screenshot for ${site.id}...`);
  try {
    const cmd = `"${edgePath}" --headless --disable-gpu --screenshot="${dest}" --window-size=1280,820 ${site.url}`;
    execSync(cmd, { stdio: 'ignore', timeout: 15000 });
    console.log(`  -> Saved ${dest} (${fs.statSync(dest).size} bytes)`);
  } catch (err) {
    console.warn(`  Failed screenshot for ${site.id}:`, err.message);
  }
}
