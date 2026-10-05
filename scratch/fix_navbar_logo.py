import re

with open('components/navbar.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_logo_pattern = r'<a href="index\.html" class="logo" style="text-decoration: none;">.*?</a>'

new_logo = '''<a href="index.html" class="logo" style="text-decoration: none; display: flex; align-items: center; gap: 8px;">
      <div style="background: linear-gradient(135deg, var(--color-primary), #B7245C); color: white; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-family: var(--font-heading); font-size: 1.6rem; font-weight: 700; box-shadow: 0 4px 12px rgba(210, 75, 118, 0.4);">M</div>
      <span style="font-family: var(--font-heading); font-size: 1.8rem; color: var(--color-text); font-weight: 700; letter-spacing: -0.5px; line-height: 1;">Magiqo</span>
    </a>'''

html = re.sub(old_logo_pattern, new_logo, html, flags=re.DOTALL)

with open('components/navbar.html', 'w', encoding='utf-8') as f:
    f.write(html)
