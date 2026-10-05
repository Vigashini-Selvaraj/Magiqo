import re

html = open('user_dashboard.html', encoding='utf-8').read()
tabs = re.findall(r'<div id="(.*?)" class="tab-content', html)
print(tabs)

for tab in tabs:
    idx = html.find(f'id="{tab}"')
    print(f"{tab}: Line {html[:idx].count(chr(10))+1}")
