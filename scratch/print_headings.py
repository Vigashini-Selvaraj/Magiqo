import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("SECTION DIVS:")
titles = re.findall(r'<div class="section-title.*?>.*?</div>', html, re.DOTALL)
for i, h in enumerate(titles):
    print(f'DIV {i}: {h.strip()}')

print("H2s:")
h2s = re.findall(r'<h2.*?>.*?</h2>', html, re.DOTALL)
for i, h in enumerate(h2s):
    print(f'H2 {i}: {h.strip()}')

print("H3s:")
h3s = re.findall(r'<h3.*?>.*?</h3>', html, re.DOTALL)
for i, h in enumerate(h3s):
    if 'var(--font-magic)' in h or 'section' in h.lower() or 'font-size' in h:
        print(f'H3 {i}: {h.strip()}')
