import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .ent-hero background
old_hero = r'background: repeating-conic-gradient\(from 0deg, #4da8da 0deg 10deg, #3895c8 10deg 20deg\);'
new_hero = r'background: linear-gradient(135deg, var(--color-bg) 0%, var(--color-bg) 45%, #3895c8 45%, #3895c8 100%);'
content = re.sub(old_hero, new_hero, content)

# 2. Update .hero-text h1 color (remove white, use var(--color-text))
old_h1 = r'color: white !important; -webkit-text-fill-color: white !important;'
new_h1 = r'color: var(--color-text) !important; -webkit-text-fill-color: var(--color-text) !important;'
content = re.sub(old_h1, new_h1, content)

# 3. Update .hero-text p color
old_p = r'color: rgba\(255,255,255,0\.9\);'
new_p = r'color: var(--color-text-light);'
content = re.sub(old_p, new_p, content)

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
