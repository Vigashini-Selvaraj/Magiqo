import urllib.request
import re

# 1. Verify HTTP server response
for page in ['index.html', 'entertainers.html', 'entertainer_detail.html', 'home2.html']:
    url = f"http://localhost:8000/{page}"
    try:
        res = urllib.request.urlopen(url)
        print(f"[HTTP 200] {url} - {len(res.read())} bytes")
    except Exception as e:
        print(f"[HTTP ERROR] {url}: {e}")

# 2. Check entertainers.html links to entertainer_detail
with open('entertainers.html', 'r', encoding='utf-8') as f:
    ent_html = f.read()

links = re.findall(r'href="(entertainer_detail\.html\?[^"]+)"', ent_html)
print(f"\nTotal links to entertainer_detail.html in entertainers.html: {len(links)}")
for l in set(links):
    print(f"  {l}")

# 3. Check index.html links to entertainer_detail
with open('index.html', 'r', encoding='utf-8') as f:
    idx_html = f.read()

idx_links = re.findall(r'href="(entertainer_detail\.html\?[^"]+)"', idx_html)
print(f"\nTotal links to entertainer_detail.html in index.html: {len(idx_links)}")
for l in set(idx_links):
    print(f"  {l}")

# 4. Check home2.html links to entertainer_detail
with open('home2.html', 'r', encoding='utf-8') as f:
    h2_html = f.read()

h2_links = re.findall(r'href="(entertainer_detail\.html\?[^"]+)"', h2_html)
print(f"\nTotal links to entertainer_detail.html in home2.html: {len(h2_links)}")
for l in set(h2_links):
    print(f"  {l}")
