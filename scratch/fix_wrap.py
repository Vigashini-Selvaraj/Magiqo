import os

# 1. Empty out footer.css as requested
with open('c:/Users/vigas/Desktop/magiqo/css/footer.css', 'w', encoding='utf-8') as f:
    f.write('/* footer CSS removed as requested. Using pure inline grid styles now. */\n')

# 2. Update footer.html to use strict GRID layout instead of flex wrap
filepath = 'c:/Users/vigas/Desktop/magiqo/components/footer.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace flexbox layout with strict grid layout from the MotorSure template
flex_layout_str = 'display: flex !important; flex-wrap: wrap !important; justify-content: space-between !important; gap: 3rem !important; margin-bottom: 4rem !important;'
grid_layout_str = 'display: grid !important; grid-template-columns: 1.65fr 1fr 1.05fr 1.15fr !important; gap: 3rem !important; margin-bottom: 4rem !important;'

html = html.replace(flex_layout_str, grid_layout_str)

# Also remove min-width limits from flex children as they might interfere with grid
html = html.replace('flex: 1.5 !important; min-width: 250px !important;', '')
html = html.replace('flex: 1 !important; min-width: 150px !important;', '')
html = html.replace('flex: 1.2 !important; min-width: 200px !important;', '')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
