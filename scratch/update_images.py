import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    modified = False

    # 1. Global Clown Replacement
    old_clown_url = 'https://images.unsplash.com/photo-1513689456070-07085750d535?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
    if old_clown_url in html:
        html = html.replace(old_clown_url, 'assets/images/pro_silly_clown.jpg')
        modified = True

    # about.html specific replacements
    if file == 'about.html':
        # 2. Hero Image Replace
        old_hero_url = 'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
        if old_hero_url in html:
            html = html.replace(old_hero_url, 'assets/images/pro_about_hero.jpg')
            modified = True

        # 3. Mark and David have same picture. Give David the new picture.
        # Find the David block
        david_block = html.find('alt="David"')
        if david_block != -1:
            # We want to replace the src just before it.
            # The line is something like <img src="assets/images/pro_magician.jpg" class="maker-avatar" alt="David">
            before = html[:david_block]
            after = html[david_block:]
            # Find the last src= before David
            src_start = before.rfind('src="')
            if src_start != -1:
                src_end = before.find('"', src_start + 5)
                before = before[:src_start + 5] + 'assets/images/pro_magician_2.jpg' + before[src_end:]
                html = before + after
                modified = True

        # 4. Little Smiles, Big Memories Grid
        grid_pattern = r'<div class="masonry-grid">.*?</div>'
        new_grid = '''<div class="masonry-grid">
        <img src="assets/images/pro_memory.jpg" alt="Memory">
        <img src="assets/images/pro_classic_magic.jpg" alt="Memory">
        <img src="assets/images/pro_gallery_alt.jpg" alt="Memory">
        <img src="assets/images/pro_hero_party.jpg" alt="Memory">
        <img src="assets/images/pro_princess.jpg" alt="Memory">
        <img src="assets/images/pro_silly_clown.jpg" alt="Memory">
        <img src="assets/images/pro_magical_services.jpg" alt="Memory">
        <img src="assets/images/pro_about_hero.jpg" alt="Memory">
      </div>'''
        html = re.sub(grid_pattern, new_grid, html, flags=re.DOTALL)
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {file}")
