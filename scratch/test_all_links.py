import re
import urllib.parse

with open('entertainer_detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract database keys
keys = re.findall(r'["\']([a-zA-Z0-9_\s]+)["\']:\s*\{', content)
print("Keys in database:", keys)

# Read entertainers from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

print("\n--- Links in index.html ---")
index_links = re.findall(r'href=["\'](entertainer_detail\.html\?[^"\']*)["\']', index_html)
for l in index_links:
    parsed = urllib.parse.parse_qs(urllib.parse.urlparse(l).query)
    eid = parsed.get('id', [''])[0].lower().strip()
    match = eid in keys
    print(f"Link: {l:<35} | ID: {eid:<15} | In DB: {match}")

# Read entertainers from home2.html
with open('home2.html', 'r', encoding='utf-8') as f:
    home2_html = f.read()

print("\n--- Links in home2.html ---")
home2_links = re.findall(r'href=["\'](entertainer_detail\.html\?[^"\']*)["\']', home2_html)
for l in home2_links:
    parsed = urllib.parse.parse_qs(urllib.parse.urlparse(l).query)
    eid = parsed.get('id', [''])[0].lower().strip()
    match = eid in keys
    print(f"Link: {l:<35} | ID: {eid:<15} | In DB: {match}")

# Read entertainers from entertainers.html
with open('entertainers.html', 'r', encoding='utf-8') as f:
    ent_html = f.read()

print("\n--- Links in entertainers.html ---")
ent_links = re.findall(r'href=["\'](entertainer_detail\.html\?[^"\']*)["\']', ent_html)
for l in ent_links:
    parsed = urllib.parse.parse_qs(urllib.parse.urlparse(l).query)
    eid = parsed.get('id', [''])[0].lower().strip()
    match = eid in keys
    print(f"Link: {l:<35} | ID: {eid:<15} | In DB: {match}")
