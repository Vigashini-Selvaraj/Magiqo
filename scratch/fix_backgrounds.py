import os

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Why Choose Magiqo background
content = content.replace(
    'style="padding: 6rem 0; background: linear-gradient(135deg, #f8f6ff 0%, #fff9fc 100%); position: relative; overflow: hidden;"',
    'style="padding: 6rem 0; background: var(--color-bg); position: relative; overflow: hidden;"'
)

# 2. Fix Party Packages background
content = content.replace(
    'style="padding: 8rem 0; background: linear-gradient(135deg, #090a10 0%, #151125 100%); position: relative;"',
    'style="padding: 8rem 0; background: var(--color-bg); position: relative;"'
)

# 3. Fix Packages Title
content = content.replace(
    '<span style="color: #ffffff;">Royal</span>',
    '<span style="color: var(--color-text);">Royal</span>'
)
content = content.replace(
    'style="margin-bottom: 5rem; color: #a9a2b5; font-size: 1.1rem; letter-spacing: 1px;"',
    'style="margin-bottom: 5rem; color: var(--color-text-light); font-size: 1.1rem; letter-spacing: 1px;"'
)

# 4. Fix Royal Cards Background & Text Colors
content = content.replace(
    'background: rgba(255, 255, 255, 0.03);',
    'background: var(--color-surface);'
)

# Fix Sparkle & Grand Illusion Titles
content = content.replace(
    '<h3 style="font-family: \'Playfair Display\', serif; font-size: 2.2rem; margin-bottom: 0.5rem; color: #ffffff;">',
    '<h3 style="font-family: \'Playfair Display\', serif; font-size: 2.2rem; margin-bottom: 0.5rem; color: var(--color-text);">'
)
# Fix Sparkle & Grand Illusion Descriptions
content = content.replace(
    'style="color: #a9a2b5; margin-bottom: 1.5rem; letter-spacing: 1px; font-size: 0.9rem; text-transform: uppercase;"',
    'style="color: var(--color-text-light); margin-bottom: 1.5rem; letter-spacing: 1px; font-size: 0.9rem; text-transform: uppercase;"'
)
# Fix List Items color (for Sparkle & Grand Illusion)
content = content.replace(
    'color: #d1cdd8;',
    'color: var(--color-text-light);'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
