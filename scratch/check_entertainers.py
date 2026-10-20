import re
import json

def check_file(filename):
    print(f"=== {filename} ===")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all card-like sections containing entertainer_detail.html
    # Look for links
    pattern = r'href=["\'](entertainer_detail\.html(?:\?[^"\']*)?)["\']'
    for m in re.finditer(pattern, content):
        link = m.group(1)
        # Find preceding image and heading within 800 chars before the link
        start = max(0, m.start() - 1000)
        snippet = content[start:m.start() + 200]
        
        img_match = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', snippet)
        h_match = re.findall(r'<h[2-4][^>]*>(.*?)</h[2-4]>', snippet)
        
        img = img_match[-1] if img_match else "None"
        name = re.sub(r'<[^>]+>', '', h_match[-1]) if h_match else "None"
        print(f"  Link: {link:<35} | Name: {name:<25} | Img: {img}")

for f in ['index.html', 'home2.html', 'entertainers.html']:
    check_file(f)

# Also check entertainersDatabase in entertainer_detail.html
print("\n=== entertainer_detail.html Database ===")
with open('entertainer_detail.html', 'r', encoding='utf-8') as f:
    detail_content = f.read()

# Extract keys and images
key_pattern = r'["\']([a-zA-Z0-9_\s]+)["\']:\s*\{[^}]*?name:\s*["\']([^"\']+)["\'][^}]*?img:\s*["\']([^"\']+)["\']'
for km in re.finditer(key_pattern, detail_content, re.DOTALL):
    print(f"  Key: {km.group(1):<15} | Name: {km.group(2):<25} | Img: {km.group(3)}")
