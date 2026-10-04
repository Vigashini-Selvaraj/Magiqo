import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hardcode IDs into maker-card buttons
# The HTML looks like:
# <div class="maker-card" data-name="Elias" data-category="magic">
#   ...
#   <a href="entertainer_detail.html" class="btn btn-outline" ...>View Details</a>
# </div>

def replace_maker_link(match):
    name = match.group(1).lower()
    card_html = match.group(0)
    # Replace the href inside this specific card
    card_html = card_html.replace('href="entertainer_detail.html"', f'href="entertainer_detail.html?id={name}"')
    return card_html

content = re.sub(r'<div class="maker-card" data-name="([^"]+)".*?</div>\s*</div>\s*<a href="entertainer_detail\.html"[^>]*>View Details</a>\s*</div>', replace_maker_link, content, flags=re.DOTALL)
# Actually, a simpler way is just regexing the whole blocks:
def quick_replace(match):
    name = match.group(1).lower()
    rest = match.group(2)
    rest = rest.replace('href="entertainer_detail.html"', f'href="entertainer_detail.html?id={name}"')
    return f'<div class="maker-card" data-name="{match.group(1)}"{rest}'

content = re.sub(r'<div class="maker-card" data-name="([^"]+)"(.*?)</a>', quick_replace, content, flags=re.DOTALL)

# 2. Add buttons to Featured Stars
content = content.replace(
    '<div class="stat"><strong>12 Yrs</strong><span>Exp.</span></div>\n            </div>\n          </div>',
    '<div class="stat"><strong>12 Yrs</strong><span>Exp.</span></div>\n            </div>\n            <a href="entertainer_detail.html?id=elias" class="btn btn-outline" style="margin-top: 1rem; width: 100%;">View Details</a>\n          </div>'
)

content = content.replace(
    '<div class="stat"><strong>8 Yrs</strong><span>Exp.</span></div>\n            </div>\n          </div>',
    '<div class="stat"><strong>8 Yrs</strong><span>Exp.</span></div>\n            </div>\n            <a href="entertainer_detail.html?id=lily" class="btn btn-outline" style="margin-top: 1rem; width: 100%;">View Details</a>\n          </div>'
)

content = content.replace(
    '<div class="stat"><strong>10 Yrs</strong><span>Exp.</span></div>\n            </div>\n          </div>',
    '<div class="stat"><strong>10 Yrs</strong><span>Exp.</span></div>\n            </div>\n            <a href="entertainer_detail.html?id=jojo" class="btn btn-outline" style="margin-top: 1rem; width: 100%;">View Details</a>\n          </div>'
)

# 3. Just in case there are any leftover 'entertainer_detail.html' without '?id='
content = content.replace('href="entertainer_detail.html"', 'href="entertainer_detail.html?id=elias"')

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
