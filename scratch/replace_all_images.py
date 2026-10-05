import os

unsplash_map = {
    'assets/images/founder_mark.jpg': 'https://images.unsplash.com/photo-1542156822-6924d1a71ace?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/happy_kids_clown.jpg': 'https://images.unsplash.com/photo-1513689456070-07085750d535?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/clown_party_1790842566084.jpg': 'https://images.unsplash.com/photo-1513689456070-07085750d535?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/james_boy_smile.jpg': 'https://images.unsplash.com/photo-1508214751196-bfdd4ca401fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/emily_girl_smile.jpg': 'https://images.unsplash.com/photo-1519689680058-324335c77eba?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/magic_package.jpg': 'https://images.unsplash.com/photo-1518991669955-9c7e78ec80ca?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/princess_party_1790842645232.jpg': 'https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/princess_portrait_1790843055244.jpg': 'https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/superhero_party_1790842695325.jpg': 'https://images.unsplash.com/photo-1608889476561-6242cfdbf622?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/gallery_smile_1.jpg': 'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/cute_kids_clapping_1790833571210.jpg': 'https://images.unsplash.com/photo-1464047736614-af63643285bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/gallery_smile_2.jpg': 'https://images.unsplash.com/photo-1511895426328-dc8714191300?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/party_moments_2_1790918669697.jpg': 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/blog_party_ideas_1790831919409.jpg': 'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/magician_portrait_1790843004983.jpg': 'https://images.unsplash.com/photo-1542156822-6924d1a71ace?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/about_us_hero.jpg': 'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
    'assets/images/about_kids_birthday.jpg': 'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/about_mission.jpg': 'https://images.unsplash.com/photo-1511895426328-dc8714191300?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
}

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    for old, new in unsplash_map.items():
        if old in html:
            html = html.replace(old, new)
            modified = True
            
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated images in {file}")
