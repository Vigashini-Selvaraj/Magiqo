import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add FontAwesome link before the closing </head>
link_tag = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">\n'

if link_tag not in html:
    html = html.replace('</head>', f'{link_tag}</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
