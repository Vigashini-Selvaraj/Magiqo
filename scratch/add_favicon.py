import glob
import re

files = glob.glob('*.html')
favicon = '<link rel="icon" type="image/png" href="assets/images/magic_hat_logo.png">'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if favicon not in html:
        # Check if there is already an icon link, if so replace it, else append before </head>
        if '<link rel="icon"' in html:
            html = re.sub(r'<link rel="icon".*?>', favicon, html)
        elif '<link rel="shortcut icon"' in html:
            html = re.sub(r'<link rel="shortcut icon".*?>', favicon, html)
        else:
            html = html.replace('</head>', f'  {favicon}\n</head>')
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)

print(f"Added favicon to {len(files)} files.")
