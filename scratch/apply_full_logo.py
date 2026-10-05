import re

# Update Navbar to use the full_logo.png and remove the text
with open('components/navbar.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_logo_pattern = r'<a href="index\.html" class="logo"[^>]*>.*?</a>'

# The user requested full_logo as the logo, and a "good size so it should be visible"
# I'll use a height of around 70px.
new_logo = '''<a href="index.html" class="logo" style="text-decoration: none; display: flex; align-items: center;">
      <img src="assets/images/full_logo.png" alt="Magiqo Premium Events Logo" style="height: 75px; width: auto; object-fit: contain;">
    </a>'''

html = re.sub(old_logo_pattern, new_logo, html, flags=re.DOTALL)
with open('components/navbar.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated navbar to use full_logo.png without text")
