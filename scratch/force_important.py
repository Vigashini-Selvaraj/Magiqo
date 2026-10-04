import os

filepath = 'c:/Users/vigas/Desktop/magiqo/components/footer.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add !important to color and font styles to prevent aggressive overriding by style.css or footer.css
content = content.replace('color: #112A22;', 'color: #112A22 !important;')
content = content.replace('color: #666666;', 'color: #666666 !important;')
content = content.replace('color: #180D20;', 'color: #180D20 !important;')
content = content.replace("font-family: 'Inter', sans-serif;", "font-family: 'Inter', sans-serif !important;")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
