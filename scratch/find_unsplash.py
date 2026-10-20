import re

for f in ['blog.html', 'blog_detail.html', 'service_detail.html', 'upload.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    matches = re.findall(r'https://images\.unsplash\.com[^\s"\'<>]+', content)
    print(f"{f}: {len(matches)} unsplash links found")
    for m in matches:
        print("  ", m)
