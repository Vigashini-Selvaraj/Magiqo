import re
f = 'c:/Users/vigas/Desktop/magiqo/entertainers.html'
c = open(f, 'r', encoding='utf-8').read()

# Replace hardcoded blue with var(--color-secondary)
c = c.replace('#3895c8', 'var(--color-secondary)')

# Add golden text shadow to the dual-colored headers
def add_shadow(match):
    style = match.group(1)
    if 'text-shadow' not in style:
        style = style.rstrip(';') + '; text-shadow: 2px 2px 0 #F6C344;'
    return f'<span style="{style}">'

c = re.sub(r'<span style="(.*?color: var\(--color-(?:primary|secondary)\).*?)">', add_shadow, c)

open(f, 'w', encoding='utf-8').write(c)
print('Updated entertainers.html with var(--color-secondary) and text-shadow')
