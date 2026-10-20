import os
import re

workspace = r"c:\Users\vigas\Desktop\magiqo"
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

print(f"Scanning {len(html_files)} HTML files...")

missing_count = 0
for hf in html_files:
    path = os.path.join(workspace, hf)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # find all src="assets/..." or src="img/..."
    matches = re.findall(r'src=["\']([^"\']+)["\']', content)
    for m in matches:
        if m.startswith('http') or m.startswith('data:') or m.startswith('#') or m.startswith('javascript:'):
            continue
        # clean query params
        clean_m = m.split('?')[0]
        full_path = os.path.join(workspace, clean_m.replace('/', '\\'))
        if not os.path.exists(full_path):
            print(f"[{hf}] Missing image: {m} (checked {full_path})")
            missing_count += 1

print(f"Scan complete. Total missing local image references: {missing_count}")
