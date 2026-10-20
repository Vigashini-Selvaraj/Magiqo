import re

# 1. Update entertainers.html
with open('entertainers.html', 'r', encoding='utf-8') as f:
    ent_html = f.read()

# Clean spaces in query parameters
ent_html = ent_html.replace('href="entertainer_detail.html?id=captain ray"', 'href="entertainer_detail.html?id=captain_ray"')
ent_html = ent_html.replace('href="entertainer_detail.html?id=dj spark"', 'href="entertainer_detail.html?id=dj_spark"')
ent_html = ent_html.replace('href="entertainer_detail.html?id=the great z"', 'href="entertainer_detail.html?id=the_great_z"')

# Wrap featured cards images and titles in links
# Featured Card 1: Elias
ent_html = re.sub(
    r'<img src="assets/images/magician_portrait_1790843004983\.jpg" alt="Elias The Magic" class="featured-img">\s*<div class="feat-info">\s*<h3>Elias "The Magic"</h3>',
    '<a href="entertainer_detail.html?id=elias" style="display: block; overflow: hidden;"><img src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias The Magic" class="featured-img"></a><div class="feat-info"><h3><a href="entertainer_detail.html?id=elias" style="color: inherit; text-decoration: none;">Elias "The Magic"</a></h3>',
    ent_html
)

# Featured Card 2: Lily
ent_html = re.sub(
    r'<img src="assets/images/princess_portrait_1790843055244\.jpg" alt="Princess Lily" class="featured-img">\s*<div class="feat-info">\s*<h3>Princess Lily</h3>',
    '<a href="entertainer_detail.html?id=lily" style="display: block; overflow: hidden;"><img src="assets/images/princess_portrait_1790843055244.jpg" alt="Princess Lily" class="featured-img"></a><div class="feat-info"><h3><a href="entertainer_detail.html?id=lily" style="color: inherit; text-decoration: none;">Princess Lily</a></h3>',
    ent_html
)

# Featured Card 3: Jojo
ent_html = re.sub(
    r'<img src="assets/images/service_circus_juggler\.jpg" alt="Jojo" class="featured-img">\s*<div class="feat-info">\s*<h3>Jojo The Juggler</h3>',
    '<a href="entertainer_detail.html?id=jojo" style="display: block; overflow: hidden;"><img src="assets/images/service_circus_juggler.jpg" alt="Jojo" class="featured-img"></a><div class="feat-info"><h3><a href="entertainer_detail.html?id=jojo" style="color: inherit; text-decoration: none;">Jojo The Juggler</a></h3>',
    ent_html
)

# Wrap maker-card images in links to their respective entertainer_detail.html?id=...
def wrap_maker_card(match):
    full_card = match.group(0)
    # find the href inside this maker card
    href_m = re.search(r'href="(entertainer_detail\.html\?id=[^"]+)"', full_card)
    if not href_m:
        return full_card
    href = href_m.group(1)
    
    # Wrap img in maker-img-wrap if not already wrapped
    if f'<a href="{href}"' not in full_card:
        full_card = re.sub(
            r'<div class="maker-img-wrap">\s*(<img [^>]+>)\s*</div>',
            rf'<div class="maker-img-wrap"><a href="{href}" style="display:block;width:100%;height:100%;"><img \1 style="width:100%;height:100%;object-fit:cover;display:block;"></a></div>',
            full_card
        )
        # fix any duplicate <img <img
        full_card = full_card.replace('<img <img', '<img')
    return full_card

# Regex to match each maker-card block
maker_card_re = re.compile(r'<div class="maker-card"[^>]*>.*?</div>\s*<a href="entertainer_detail\.html\?[^"]+"[^>]*>View Details</a>\s*</div>', re.DOTALL)
ent_html = maker_card_re.sub(wrap_maker_card, ent_html)

with open('entertainers.html', 'w', encoding='utf-8') as f:
    f.write(ent_html)
print("Updated entertainers.html with clickable images and sanitized links!")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Make card 1 clickable
index_html = re.sub(
    r'<img src="assets/images/magician_portrait_1790843004983\.jpg"[^>]*alt="Elias the Magician">',
    '<a href="entertainer_detail.html?id=elias" style="display: block;"><img src="assets/images/magician_portrait_1790843004983.jpg" style="width: 100%; height: 260px; object-fit: cover; display: block;" alt="Elias the Magician"></a>',
    index_html
)

# Make card 2 clickable
index_html = re.sub(
    r'<img src="assets/images/performer_superhero\.jpg"[^>]*alt="Captain Leo Superhero Performer">',
    '<a href="entertainer_detail.html?id=max" style="display: block;"><img src="assets/images/performer_superhero.jpg" style="width: 100%; height: 260px; object-fit: cover; display: block;" alt="Captain Leo Superhero Performer"></a>',
    index_html
)

# Make card 3 Princess Lily (align with entertainers.html and portrait)
index_html = re.sub(
    r'<img src="assets/images/princess_portrait_1790843055244\.jpg"[^>]*alt="Princess Aurora">',
    '<a href="entertainer_detail.html?id=lily" style="display: block;"><img src="assets/images/princess_portrait_1790843055244.jpg" style="width: 100%; height: 260px; object-fit: cover; display: block;" alt="Princess Lily"></a>',
    index_html
)
index_html = index_html.replace(
    '<h3 class="entertainer-name">Princess Aurora</h3>',
    '<h3 class="entertainer-name"><a href="entertainer_detail.html?id=lily" style="color: inherit; text-decoration: none;">Princess Lily</a></h3>'
)
index_html = index_html.replace(
    'href="entertainer_detail.html?id=mia" class="btn btn-outline btn-sm">View Profile</a>',
    'href="entertainer_detail.html?id=lily" class="btn btn-outline btn-sm">View Profile</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("Updated index.html with clickable images and synced Princess Lily card!")

# 3. Update home2.html
with open('home2.html', 'r', encoding='utf-8') as f:
    home2_html = f.read()

# Sync Princess Lily card in home2.html
home2_html = home2_html.replace(
    '<img src="assets/images/pro_princess.jpg" alt="Princess">',
    '<img src="assets/images/princess_portrait_1790843055244.jpg" alt="Princess Lily">'
)
home2_html = home2_html.replace(
    '<h3>Mia</h3>',
    '<h3>Princess Lily</h3>'
)
home2_html = home2_html.replace(
    'href="entertainer_detail.html?id=mia" class="btn btn-outline" style="width: 100%;">View Profile</a>',
    'href="entertainer_detail.html?id=lily" class="btn btn-outline" style="width: 100%;">View Profile</a>'
)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(home2_html)
print("Updated home2.html with synced Princess Lily card!")
