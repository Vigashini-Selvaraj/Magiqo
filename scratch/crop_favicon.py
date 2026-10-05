import base64
import glob

# Read the png
with open('assets/images/magic_hat_logo.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <image href="data:image/png;base64,{b64}" x="-25" y="-25" width="150" height="150" preserveAspectRatio="xMidYMid slice" />
</svg>'''

with open('assets/images/favicon.svg', 'w') as f:
    f.write(svg_content)

# Update all html files
favicon_link = '<link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">'

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace the old one with the new svg one
    import re
    if 'rel="icon"' in html:
        html = re.sub(r'<link rel="icon" type="image/png" href="assets/images/magic_hat_logo\.png">', favicon_link, html)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
