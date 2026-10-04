import re

def fix_colors(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # 1. Remove the golden shadow
    c = c.replace('text-shadow: 2px 2px 0 #F6C344;', '')
    c = c.replace('text-shadow: 2px 2px 0 #F6C344', '')
    
    # 2. Replace var(--color-secondary) with #3895c8 where it relates to the blue text
    if 'packages.html' in filepath:
        c = c.replace('.text-blue { color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary); background: none; }',
                      '.text-blue { color: #3895c8; -webkit-text-fill-color: #3895c8; background: none; }')
    
    if 'entertainers.html' in filepath:
        # Revert var(--color-secondary) back to #3895c8 in the hero section span
        c = c.replace('color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary);', 'color: #3895c8; -webkit-text-fill-color: #3895c8;')
        
    if 'booking.html' in filepath:
        # Change 'Magical' from pink to blue and remove shadow
        c = c.replace('<span style=\"color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none; \">Magical</span>',
                      '<span style=\"color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;\">Magical</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

for f in ['c:/Users/vigas/Desktop/magiqo/packages.html', 'c:/Users/vigas/Desktop/magiqo/entertainers.html', 'c:/Users/vigas/Desktop/magiqo/booking.html']:
    fix_colors(f)
print('Fixed colors and removed shadows!')
