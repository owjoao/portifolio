import os

niches = [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(os.path.join(d, 'index.html'))]
print(f"Total niches with index.html: {len(niches)}")

results = []
for n in sorted(niches):
    html = open(os.path.join(n, 'index.html'), encoding='utf-8', errors='ignore').read()
    has_mobile_dock = 'md:hidden fixed bottom-0' in html or 'fixed bottom-0 left-0 right-0 z-40' in html or 'fixed bottom-0 left-0 right-0 z-50' in html or ('sm:hidden' in html and 'fixed bottom-0' in html)
    has_shimmer = 'shimmer-btn' in html
    has_originkit = 'originkit' in html.lower() or 'nossa metodologia' in html.lower() or 'outras alternativas' in html.lower() or 'nós vs' in html.lower() or 'comparativo' in html.lower()
    has_slider = 'ba-container' in html or 'ba-slider' in html or 'antes e depois' in html.lower() or 'ba-photo' in html or 'comparador' in html.lower()
    has_glass_header = 'backdrop-blur' in html and ('<header' in html or 'nav' in html)
    
    results.append({
        'niche': n,
        'mobile_dock': has_mobile_dock,
        'shimmer': has_shimmer,
        'matrix': has_originkit,
        'slider': has_slider,
        'glass_header': has_glass_header
    })

print(f"{'NICHE':24} | {'DOCK':5} | {'SHIM':5} | {'MATRIX':6} | {'SLIDER':6} | {'GLASS_HDR':9}")
print('-'*68)
for r in results:
    print(f"{r['niche']:24} | {str(r['mobile_dock']):5} | {str(r['shimmer']):5} | {str(r['matrix']):6} | {str(r['slider']):6} | {str(r['glass_header']):9}")

