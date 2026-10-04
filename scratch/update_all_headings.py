import re
import os

files_to_update = [
    'c:/Users/vigas/Desktop/magiqo/index.html',
    'c:/Users/vigas/Desktop/magiqo/entertainers.html',
    'c:/Users/vigas/Desktop/magiqo/services.html',
    'c:/Users/vigas/Desktop/magiqo/service_detail.html',
    'c:/Users/vigas/Desktop/magiqo/about.html',
    'c:/Users/vigas/Desktop/magiqo/entertainer_detail.html'
]

def split_text_and_wrap(match):
    full_tag = match.group(0)
    tag_name = match.group(1)
    attrs = match.group(2)
    inner_text = match.group(3)
    
    # If it already contains a span or is empty, leave it alone
    if '<span' in inner_text.lower() or not inner_text.strip() or '<img' in inner_text.lower() or '<br' in inner_text.lower() or '<a' in inner_text.lower():
        return full_tag
        
    words = inner_text.split()
    if len(words) < 2:
        return full_tag # Can't split one word
        
    mid = len(words) // 2
    if len(words) == 3:
        mid = 1 # e.g. "Our Magical Stars" -> "Our" "Magical Stars" or "Visual Memories" -> "Visual" "Memories"
        
    part1 = ' '.join(words[:mid])
    part2 = ' '.join(words[mid:])
    
    new_inner = f'<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">{part1}</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">{part2}</span>'
    return f'<{tag_name}{attrs}>{new_inner}</{tag_name}>'

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Match <h1> and <h2> tags
    new_content = re.sub(r'<(h[12])([^>]*)>(.*?)</\1>', split_text_and_wrap, content, flags=re.DOTALL | re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Successfully updated headings in all pages!")
