import re

files = [
    'c:/Users/vigas/Desktop/magiqo/entertainers.html',
    'c:/Users/vigas/Desktop/magiqo/entertainer_detail.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all variations of background: white/fff
    content = re.sub(r'background:\s*white;?', 'background: var(--color-surface);', content)
    content = re.sub(r'background:\s*#ffffff;?', 'background: var(--color-surface);', content, flags=re.IGNORECASE)
    content = re.sub(r'background:\s*#fff;?', 'background: var(--color-surface);', content, flags=re.IGNORECASE)
    content = re.sub(r'background:\s*#fff0f5;?', 'background: var(--color-surface);', content, flags=re.IGNORECASE)
    
    # Update body background to have !important
    content = re.sub(r'body\s*\{\s*background-color:\s*var\(--color-bg\);', 
                     r'body {\n      background-color: var(--color-bg) !important;\n      background: var(--color-bg) !important;', 
                     content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file_path}")
