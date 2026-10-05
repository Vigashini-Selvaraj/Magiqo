import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The container is: 
old_circle = r'<div style="background: rgba\(255,\s*190,\s*11,\s*0\.15\); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">\s*<i class="fa-solid fa-star" style="color: #FFBE0B; font-size: 1\.5rem;"></i>\s*</div>'

html = re.sub(old_circle, '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
