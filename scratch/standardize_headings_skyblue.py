import glob
import re
import os

print("Starting heading standardization to Sky Blue (#3895c8)...")

# 1. Update packages.html & contact.html .text-blue
for fn in ['packages.html', 'contact.html']:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('.text-blue { color: var(--color-secondary);', '.text-blue { color: #3895c8;')
        c = c.replace('-webkit-text-fill-color: var(--color-secondary);', '-webkit-text-fill-color: #3895c8;')
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {fn} .text-blue")

# 2. Update entertainers.html inverted headings
if os.path.exists('entertainers.html'):
    with open('entertainers.html', 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace(
        '<h1><span style="color: var(--color-secondary);">The Children\'s Favourite</span> <br><span style="color: var(--color-primary);">Party Entertainers!</span></h1>',
        '<h1><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">The Children\'s Favourite</span> <br><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Party Entertainers!</span></h1>'
    )

    c = re.sub(
        r'<h2><span style="color: var\(--color-secondary\);">([^<]+)</span>\s*<span style="color: var\(--color-primary\);">([^<]+)</span></h2>',
        r'<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">\1</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">\2</span></h2>',
        c
    )

    with open('entertainers.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated entertainers.html headings")

# 3. Update index.html, about.html, services.html, service_detail.html, blog.html
for fn in ['index.html', 'about.html', 'services.html', 'service_detail.html', 'blog.html']:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        
        # Replace Day Magical on index.html
        c = c.replace('<span style="color: var(--color-secondary);">Day Magical</span>',
                      '<span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Day Magical</span>')
        
        # Replace secondary color in headings with #3895c8
        c = re.sub(
            r'<span style="color: var\(--color-secondary\);(?: -webkit-text-fill-color: [^;]+;)?">',
            '<span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">',
            c
        )
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {fn} headings")

print("All headings successfully standardized to uniform sky blue (#3895c8)!")
