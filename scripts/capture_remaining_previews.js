const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const PREVIEWS_DIR = path.resolve(__dirname, '..', 'assets', 'previews');

const missing = [
  { id: 'restaurante-egeu', url: 'http://localhost:8080/restaurante-egeu/index.html' }
];

for (const m of missing) {
  const dest = path.join(PREVIEWS_DIR, `preview_${m.id.replace(/-/g, '_')}.jpg`);
  console.log(`Taking screenshot for ${m.id} -> ${dest}`);
  try {
    const cmd = `"${edgePath}" --headless --disable-gpu --screenshot="${dest}" --window-size=1280,820 ${m.url}`;
    execSync(cmd, { stdio: 'ignore', timeout: 15000 });
    console.log(`  -> OK: ${fs.statSync(dest).size} bytes`);
  } catch (e) {
    console.warn(`  -> Failed: ${e.message}`);
  }
}
