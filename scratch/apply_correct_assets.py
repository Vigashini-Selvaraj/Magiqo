import re
import glob

# 1. Update Navbar to use the full logo
with open('components/navbar.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_logo_pattern = r'<a href="index\.html" class="logo"[^>]*>.*?</a>'

# Replace with full logo from assets directory
new_logo = '''<a href="index.html" class="logo" style="text-decoration: none; display: flex; align-items: center;">
      <img src="assets/full logo.png" alt="Magiqo Premium Events Logo" style="height: 75px; width: auto; object-fit: contain;">
    </a>'''

html = re.sub(old_logo_pattern, new_logo, html, flags=re.DOTALL)
with open('components/navbar.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update favicons to use logoooo.png in all HTML files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        file_html = f.read()
        
    file_html = re.sub(
        r'<link rel="icon".*?href=".*?favicon\.(svg|ico|png)".*?>',
        r'<link rel="icon" type="image/png" href="assets/logoooo.png">',
        file_html
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(file_html)

print("Updated navbar and favicons to use correct assets")
