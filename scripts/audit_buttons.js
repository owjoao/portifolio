const fs = require('fs');
const path = require('path');

const targetFile = path.resolve(__dirname, '../reforma-moveis/index.html');
const content = fs.readFileSync(targetFile, 'utf8');

console.log('Auditing:', targetFile);

// Check 1: WhatsApp links
const waRegex = /href=["'](https?:\/\/wa\.me\/[^"']+)["']/g;
let match;
let countWa = 0;
let errors = [];

while ((match = waRegex.exec(content)) !== null) {
  countWa++;
  const url = match[1];
  console.log(`[WA Link #${countWa}] ${url}`);
  
  if (!url.includes('5532999292311')) {
    errors.push(`Invalid phone number in URL: ${url}`);
  }
  
  const expectedParam = 'text=gostei%20desse%20site%2C%20qual%20o%20valor%3F';
  if (!url.includes(expectedParam)) {
    errors.push(`Missing or incorrect default message param: ${url}`);
  }
}

// Check 2: Form action or JS submission
if (content.includes('form') || content.includes('window.open')) {
  console.log('Checking form / JS WhatsApp integration...');
  const formWaMatches = content.match(/5532999292311/g);
  console.log(`Found ${(formWaMatches || []).length} occurrences of target number 5532999292311.`);
}

// Check 3: Check for obsolete/placeholder phone numbers
const placeholderPhones = ['1199999', '11 99999', '0000-0000', '12345678', '99999-9999'];
placeholderPhones.forEach(ph => {
  if (content.includes(ph)) {
    errors.push(`Found placeholder phone pattern: ${ph}`);
  }
});

// Check 4: Check phone text displayed to user
const displayedPhoneMatches = content.match(/\(?32\)?\s*99929-?2311/g);
console.log(`Found ${(displayedPhoneMatches || []).length} displayed occurrences of (32) 99929-2311.`);

// Check 5: Image paths existence
const imgRegex = /src=["']([^"']+\.(?:jpg|jpeg|png|svg|webp))["']/g;
let imgMatch;
let missingImages = [];
while ((imgMatch = imgRegex.exec(content)) !== null) {
  const imgSrc = imgMatch[1];
  if (imgSrc.startsWith('http://') || imgSrc.startsWith('https://')) {
    continue;
  }
  const fullPath = path.resolve(path.dirname(targetFile), imgSrc);
  if (!fs.existsSync(fullPath)) {
    missingImages.push(imgSrc);
  }
}

if (missingImages.length > 0) {
  errors.push(`Missing images: ${missingImages.join(', ')}`);
} else {
  console.log('All referenced local images exist on disk.');
}

console.log('\n--- AUDIT SUMMARY ---');
console.log(`Total WhatsApp CTA links found: ${countWa}`);
if (errors.length > 0) {
  console.error('ERRORS FOUND:');
  errors.forEach(e => console.error('  - ' + e));
  process.exit(1);
} else {
  console.log('ALL CHECKS PASSED PERFECTLY!');
}

