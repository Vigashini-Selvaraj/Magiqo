import re

with open('entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Match all cards in entertainers.html
# 1. Featured cards
print("=== FEATURED CARDS in entertainers.html ===")
feat_pattern = r'<div class="featured-card">.*?<img src="([^"]+)".*?<h3>(.*?)</h3>.*?<h4>(.*?)</h4>.*?href="([^"]+)"'
for m in re.finditer(feat_pattern, content, re.DOTALL):
    print(f"Name: {m.group(2):<25} | Role: {m.group(3):<25} | Img: {m.group(1):<45} | Link: {m.group(4)}")

# 2. Maker cards
print("\n=== MAKER CARDS in entertainers.html ===")
maker_pattern = r'<div class="maker-card" data-name="([^"]+)" data-category="([^"]+)">\s*<div class="maker-img-wrap"><img src="([^"]+)"[^>]*></div>\s*<div class="maker-info"><h4>(.*?)</h4><p>(.*?)</p>.*?href="([^"]+)"'
for m in re.finditer(maker_pattern, content, re.DOTALL):
    print(f"Data-Name: {m.group(1):<15} | Cat: {m.group(2):<12} | Title: {m.group(5):<25} | Img: {m.group(3):<45} | Link: {m.group(6)}")

print("\n=== CARDS in index.html ===")
with open('index.html', 'r', encoding='utf-8') as f:
    icontent = f.read()

icard_pattern = r'<div class="card entertainer-card">\s*<img src="([^"]+)"[^>]*>.*?<h3 class="entertainer-name">(.*?)</h3>.*?<div class="entertainer-tags"[^>]*>(.*?)</div>.*?href="([^"]+)"'
for m in re.finditer(icard_pattern, icontent, re.DOTALL):
    print(f"Name: {m.group(2):<25} | Tags: {m.group(3):<30} | Img: {m.group(1):<45} | Link: {m.group(4)}")
