import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_h1 = """<h1 style="font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 5.5rem); line-height: 1.1; margin: 0 0 25px 0; color: var(--color-text);">
          Make Their Day <br><span style="color: var(--color-primary);">Magical</span>
        </h1>"""

new_h1 = """<h1 style="font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 5.5rem); line-height: 1.1; margin: 0 0 25px 0;">
          <span style="color: var(--color-primary);">Create Moments</span> <br><span style="color: #3895c8;">Of Pure Magic</span>
        </h1>"""

html = html.replace(old_h1, new_h1)

# Also let's double check if the button was successfully replaced.
old_btn = '<a href="packages.html" style="padding: 16px 35px; border-radius: 50px; font-weight: 700; font-size: 1.1rem; color: var(--color-text); border: 2px solid var(--color-border); text-decoration: none; transition: 0.3s;">View Packages</a>'
new_btn = '<a href="packages.html" class="btn btn-secondary" style="padding: 16px 35px; border-radius: 50px; font-weight: 700; font-size: 1.1rem; color: white; background: #3895c8; border: none; text-decoration: none; transition: 0.3s; box-shadow: 0 10px 25px rgba(56, 149, 200, 0.3);">View Packages</a>'

html = html.replace(old_btn, new_btn)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
