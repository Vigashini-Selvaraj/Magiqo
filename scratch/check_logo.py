import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's just find the logo class
matches = re.findall(r'<a[^>]*class="[^"]*logo[^"]*"[^>]*>.*?</a>', html, re.DOTALL)
if matches:
    print(matches[0])
else:
    print("No logo found.")

# Let's also check the navbar.js or components.js if the navbar is dynamic!
import glob
for file in glob.glob('js/*.js'):
    content = open(file, 'r', encoding='utf-8').read()
    m = re.findall(r'<a[^>]*class="[^"]*logo[^"]*"[^>]*>.*?</a>', content, re.DOTALL)
    if m:
        print(f"Found in {file}:")
        print(m[0])
