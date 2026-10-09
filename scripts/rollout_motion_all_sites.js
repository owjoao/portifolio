const fs = require('fs');
const path = require('path');

console.log('=== Rollout Motion Core & Visual-First Architecture to All Sites ===');

const dirs = fs.readdirSync('.').filter(d => 
  fs.statSync(d).isDirectory() && 
  !d.startsWith('.') && 
  d !== 'assets' && 
  d !== 'scripts' && 
  d !== 'templates' &&
  fs.existsSync(path.join(d, 'index.html'))
);

console.log(`Processing ${dirs.length} sites...`);

let updatedCount = 0;

for (const dir of dirs) {
  const filePath = path.join(dir, 'index.html');
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  // 1. Link motion-core.css in <head>
  if (!html.includes('motion-core.css')) {
    if (html.includes('</head>')) {
      html = html.replace('</head>', '  <link rel="stylesheet" href="../assets/css/motion-core.css">\n</head>');
      modified = true;
    }
  }

  // 2. Link motion-core.js before </body>
  if (!html.includes('motion-core.js')) {
    if (html.includes('</body>')) {
      html = html.replace('</body>', '  <script src="../assets/js/motion-core.js"></script>\n</body>');
      modified = true;
    }
  }

  // 3. Add .reveal to sections (skip hero if desired, or smooth reveal)
  // Replace <section (if not already containing reveal)
  html = html.replace(/<section\s+(class="[^"]*")/gi, (match, classAttr) => {
    if (!classAttr.includes('reveal')) {
      modified = true;
      return match.replace(classAttr, classAttr.slice(0, 7) + 'reveal ' + classAttr.slice(7));
    }
    return match;
  });

  // 4. Add shimmer-btn to primary CTA anchor links (wa.me, agendar, or primary gradient buttons)
  html = html.replace(/class="([^"]*(?:bg-gradient|bg-emerald|bg-teal|bg-amber|bg-rose|bg-primary|from-)[^"]*shadow-[^"]*)"/gi, (match, classes) => {
    if (!classes.includes('shimmer-btn') && (classes.includes('py-') || classes.includes('px-')) && !classes.includes('card-')) {
      modified = true;
      return `class="shimmer-btn ${classes}"`;
    }
    return match;
  });

  // 5. Add card-lift to feature/service cards
  html = html.replace(/class="([^"]*(?:rounded-2xl|rounded-3xl)[^"]*border[^"]*(?:shadow|bg-)[^"]*)"/gi, (match, classes) => {
    if (!classes.includes('card-lift') && !classes.includes('fixed') && !classes.includes('modal') && !classes.includes('header')) {
      modified = true;
      return `class="card-lift ${classes}"`;
    }
    return match;
  });

  // 6. Find stats/numbers and add counter-up
  // Pattern: >+1.200< or >98%< or >15 Anos< or >+500<
  html = html.replace(/>(\+\d+[\d.,]*%?|\d+[\d.,]*%|\d+\s*(?:Anos|Clientes|Horas|Causas|Projetos))</gi, (match, numText) => {
    // Only if not already counter-up
    return ` class="counter-up" data-target="${numText}">${numText}<`;
  });

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    updatedCount++;
    console.log(`  ✓ Updated ${dir}`);
  }
}

console.log(`\n🎉 Total sites upgraded with Motion Core: ${updatedCount}`);
