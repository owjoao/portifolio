const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const PREVIEWS_DIR = path.resolve('assets/previews');
const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

const targets = [
  { id: 'concessionaria-honda', url: 'http://localhost:8080/concessionaria-honda/index.html' },
  { id: 'corretor-imoveis', url: 'http://localhost:8080/corretor-imoveis/index.html' },
  { id: 'personal-trainer', url: 'http://localhost:8080/personal-trainer/index.html' },
  { id: 'banho-e-tosa', url: 'http://localhost:8080/banho-e-tosa/index.html' },
  { id: 'restaurante-egeu', url: 'http://localhost:8080/restaurante-egeu/index.html' }
];

for (const t of targets) {
  const destPng = path.join(PREVIEWS_DIR, t.id + '.png');
  const destJpg = path.join(PREVIEWS_DIR, 'preview_' + t.id.replace(/-/g, '_') + '.jpg');
  try {
    const cmd = `"${edgePath}" --headless --disable-gpu --screenshot="${destPng}" --window-size=1280,820 ${t.url}`;
    execSync(cmd, { stdio: 'ignore', timeout: 20000 });
    fs.copyFileSync(destPng, destJpg);
    console.log(`✅ Screenshot updated for ${t.id} (${(fs.statSync(destPng).size / 1024).toFixed(1)} KB)`);
  } catch (e) {
    console.error(`Error capturing ${t.id}:`, e.message);
  }
}
