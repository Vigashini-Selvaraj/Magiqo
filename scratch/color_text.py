import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_h1 = """<h1 style="font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 5.5rem); line-height: 1.1; margin: 0 0 25px 0;">
          <span style="color: var(--color-primary);">Create Moments</span> <br><span style="color: #3895c8;">Of Pure Magic</span>
        </h1>"""

new_h1 = """<h1 style="font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 5.5rem); line-height: 1.1; margin: 0 0 25px 0;">
          <span style="color: var(--color-primary);">Make Their</span> <span style="color: #3895c8;">Day</span><br>
          <span style="color: #3895c8;">Magical</span>
        </h1>"""

html = html.replace(old_h1, new_h1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
