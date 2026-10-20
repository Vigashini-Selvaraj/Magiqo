import glob
import re

for fn in sorted(glob.glob('*.html')):
    if 'backup' in fn or 'index2' in fn:
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    btns = re.findall(r'<[a-z]+[^>]*class=["\'][^"\']*btn[^"\']*["\'][^>]*>', c)
    inlines = []
    for b in btns:
        if 'style=' in b:
            sm = re.search(r'style=["\']([^"\']+)["\']', b)
            if sm and any(k in sm.group(1) for k in ['background', 'color', 'border']):
                inlines.append(b)
    if inlines:
        print(f"=== {fn}: {len(inlines)} styled buttons ===")
        for item in inlines[:6]:
            print("  ", item[:100])
