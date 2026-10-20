import re

with open('entertainers.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern for maker-card
# <div class="maker-card" data-name="..." data-category="...">
#   <div class="maker-img-wrap"><img src="..." alt="..."></div>
#   <div class="maker-info"><h4>...</h4><p>...</p>...</div>
#   <a href="entertainer_detail.html?id=..." class="btn btn-outline btn-sm"...>View Details</a>
# </div>

def update_maker_card(match):
    card_html = match.group(0)
    href_match = re.search(r'href="(entertainer_detail\.html\?id=[^"]+)"', card_html)
    if not href_match:
        return card_html
    href = href_match.group(1)
    
    # Wrap img inside maker-img-wrap if not already wrapped
    if f'<a href="{href}"' not in card_html.split('<div class="maker-info">')[0]:
        card_html = re.sub(
            r'<div class="maker-img-wrap"><img src="([^"]+)" alt="([^"]+)"></div>',
            rf'<div class="maker-img-wrap"><a href="{href}" style="display:block;width:100%;height:100%;"><img src="\1" alt="\2" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.4s ease;"></a></div>',
            card_html
        )
    
    # Wrap h4 if not already wrapped in <a>
    if not re.search(r'<h4><a ', card_html):
        card_html = re.sub(
            r'<h4>(.*?)</h4>',
            rf'<h4><a href="{href}" style="color: inherit; text-decoration: none;">\1</a></h4>',
            card_html
        )
        
    return card_html

pattern = re.compile(r'<div class="maker-card" data-name="[^"]+" data-category="[^"]+">.*?View Details</a>\s*</div>', re.DOTALL)
new_html = pattern.sub(update_maker_card, html)

with open('entertainers.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Wrapped all maker card images and titles with clickable links to entertainer_detail.html!")
