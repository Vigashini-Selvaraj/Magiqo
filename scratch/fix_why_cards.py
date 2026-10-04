import os

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'background: rgba(255, 255, 255, 0.7);',
    'background: var(--color-surface);'
)
content = content.replace(
    'border: 1px solid rgba(255, 255, 255, 0.5);',
    'border: 1px solid var(--color-border);'
)
content = content.replace(
    'color: #302344;',
    'color: var(--color-text);'
)
content = content.replace(
    'color: #777185;',
    'color: var(--color-text-light);'
)
content = content.replace(
    'background: linear-gradient(135deg, #fff0f7, #edf8ff);',
    'background: var(--color-bg);'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed why-card")
