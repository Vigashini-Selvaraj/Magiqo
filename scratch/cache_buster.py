import os

filepath = 'c:/Users/vigas/Desktop/magiqo/js/components.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace loadComponent calls to add a cache-buster so the browser is FORCED to fetch the latest HTML
content = content.replace("loadComponent('navbar', 'components/navbar.html');", "loadComponent('navbar', 'components/navbar.html?v=' + new Date().getTime());")
content = content.replace("loadComponent('footer', 'components/footer.html');", "loadComponent('footer', 'components/footer.html?v=' + new Date().getTime());")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
