const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const PREVIEWS_DIR = path.resolve(__dirname, '../assets/previews');
const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

const destPng = path.join(PREVIEWS_DIR, 'reforma-moveis.png');
const destJpg = path.join(PREVIEWS_DIR, 'preview_reforma_moveis.jpg');
const fullPng = path.resolve(__dirname, '../reforma-moveis/preview-full.png');

console.log('Capturing standard preview...');
const cmd1 = `"${edgePath}" --headless --disable-gpu --screenshot="${destPng}" --window-size=1280,820 http://localhost:8080/reforma-moveis/index.html`;
execSync(cmd1, { stdio: 'inherit', timeout: 25000 });
fs.copyFileSync(destPng, destJpg);
console.log(`✅ Standard preview updated (${(fs.statSync(destPng).size / 1024).toFixed(1)} KB)`);

console.log('Capturing full page preview (3600px)...');
const cmd2 = `"${edgePath}" --headless --disable-gpu --screenshot="${fullPng}" --window-size=1280,3600 http://localhost:8080/reforma-moveis/index.html`;
execSync(cmd2, { stdio: 'inherit', timeout: 25000 });
console.log(`✅ Full preview captured (${(fs.statSync(fullPng).size / 1024).toFixed(1)} KB)`);

