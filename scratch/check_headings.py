import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("SECTION TITLES:")
headings = re.findall(r'<div class="section-title.*?</div>', html, re.DOTALL)
for i, h in enumerate(headings):
    print(f"Heading {i}: {h.strip()[:100]}")

print("\nH2 TITLES:")
h2s = re.findall(r'<h2.*?>.*?</h2>', html, re.DOTALL)
for i, h in enumerate(h2s):
    print(f"H2 {i}: {h.strip()[:100]}")
    
print("\nH3 TITLES:")
h3s = re.findall(r'<h3.*?>.*?</h3>', html, re.DOTALL)
for i, h in enumerate(h3s[:5]):
    print(f"H3 {i}: {h.strip()[:100]}")
