import re

with open('entertainers.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    # 1. David stage illusionist
    (r'<img src="assets/images/hero_magician_1790831867453\.jpg" alt="David">',
     r'<img src="assets/images/pro_magician_2.jpg" alt="David">'),
    
    # 2. Chloe (Balloon artist)
    (r'<img src="https://images.unsplash\.com/photo-1502086223501-7ea6ecd79368\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Chloe">',
     r'<img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Chloe">'),
     
    # 3. Giggles (face painting clown)
    (r'<img src="assets/images/pro_silly_clown\.jpg" alt="Giggles">',
     r'<img src="assets/images/pro_clown_blog.jpg" alt="Giggles">'),
     
    # 4. Mia (glitter tattoos)
    (r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Mia">',
     r'<img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Mia">'),
     
    # 5. James (Reviewer)
    (r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="James" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">',
     r'<img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="James" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">'),
     
    # 6. Emily (Reviewer)
    (r'<img src="https://images.unsplash\.com/photo-1519689680058-324335c77eba\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Emily" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">',
     r'<img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Emily" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">')
]

for old, new in replacements:
    html = re.sub(old, new, html)

with open('entertainers.html', 'w', encoding='utf-8') as f:
    f.write(html)
