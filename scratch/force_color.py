import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_h1 = """<h1 style="font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 5.5rem); line-height: 1.1; margin: 0 0 25px 0; color: transparent;">
          <span style="color: #D24B76 !important;">Make Their</span> <span style="color: #3895c8 !important;">Day</span><br>
          <span style="color: #3895c8 !important;">Magical</span>
        </h1>"""

html = re.sub(r'<h1.*?</h1>', new_h1, html, flags=re.DOTALL, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
