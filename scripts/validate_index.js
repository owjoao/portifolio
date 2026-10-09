const fs = require('fs');
const vm = require('vm');

const content = fs.readFileSync('index.html', 'utf8');

// Check script tags
const scripts = content.match(/<script[\s\S]*?<\/script>/gi) || [];
scripts.forEach((s, idx) => {
  if (!s.includes('src=')) {
    const code = s.replace(/<script[^>]*>/i, '').replace(/<\/script>/i, '');
    try {
      new vm.Script(code);
      console.log('Script #' + idx + ' syntax OK');
    } catch (e) {
      console.error('Syntax error in script #' + idx, e.message);
    }
  }
});

// Check local links
const hrefs = content.match(/href="([^"]+)"/g) || [];
const checked = new Set();
let brokenCount = 0;
hrefs.forEach(h => {
  const url = h.replace('href="', '').replace('"', '');
  if (!url.startsWith('http') && !url.startsWith('#') && !url.startsWith('data:') && !checked.has(url)) {
    checked.add(url);
    const exists = fs.existsSync(url);
    if (!exists) {
      console.warn('Broken local link:', url);
      brokenCount++;
    }
  }
});

console.log('Total unique local links checked:', checked.size);
console.log('Broken links count:', brokenCount);
