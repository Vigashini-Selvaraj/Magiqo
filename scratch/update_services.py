import re

with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    # 1. Hero
    (r'<img src="assets/images/service_hero\.jpg" alt="Magical Entertainment">', 
     r'<img src="assets/images/pro_services_hero.jpg" alt="Magical Entertainment">'),
    
    # 2. Grand Stage Magician
    (r'<img src="assets/images/hero_magician_1790831867453\.jpg" alt="Stage Magician">',
     r'<img src="assets/images/pro_grand_stage.jpg" alt="Stage Magician">'),
     
    # 3. Face Painting
    (r'<img src="assets/images/pro_hero_party\.jpg" alt="Face Painting">',
     r'<img src="https://images.unsplash.com/photo-1542841791-c990be44358a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Face Painting">'),
     
    # 4. Balloon Twisting
    (r'<img src="https://images.unsplash\.com/photo-1502086223501-7ea6ecd79368\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Balloon Twisting">',
     r'<img src="assets/images/pro_silly_clown.jpg" alt="Balloon Twisting">'),
     
    # 5. Party Host
    (r'<img src="assets/images/pro_hero_party\.jpg" alt="Party Host">',
     r'<img src="assets/images/pro_services_hero.jpg" alt="Party Host">'),
     
    # 6. Magic Workshop
    (r'<img src="https://images.unsplash\.com/photo-1511895426328-dc8714191300\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Magic Workshop">',
     r'<img src="assets/images/pro_classic_magic.jpg" alt="Magic Workshop">'),
     
    # 7. Storytelling
    (r'<img src="https://images.unsplash\.com/photo-1511895426328-dc8714191300\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Storytelling">',
     r'<img src="assets/images/pro_princess.jpg" alt="Storytelling">'),
     
    # 8. Birthdays
    (r'<img src="https://images.unsplash\.com/photo-1502086223501-7ea6ecd79368\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Birthdays">',
     r'<img src="assets/images/pro_memory.jpg" alt="Birthdays">'),
     
    # 9. Schools
    (r'<img src="assets/images/pro_hero_party\.jpg" alt="Schools">',
     r'<img src="assets/images/pro_gallery_alt.jpg" alt="Schools">'),
     
    # 10. Family Gatherings / Corporate
    (r'<img src="https://images.unsplash\.com/photo-1511895426328-dc8714191300\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Corporate">',
     r'<img src="assets/images/pro_about_hero.jpg" alt="Corporate">')
]

for old, new in replacements:
    html = re.sub(old, new, html)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html)
