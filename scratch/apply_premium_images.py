import os
import re

updates = {
    # Replace broken unsplash hero
    'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80': 'assets/images/pro_hero_party.jpg',
    'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80': 'assets/images/pro_hero_party.jpg',
    'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80': 'assets/images/pro_hero_party.jpg',
    
    # Elias the Magician / Classic Magic
    'https://images.unsplash.com/photo-1542156822-6924d1a71ace?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80': 'assets/images/pro_magician.jpg',
    
    # Princess Mia / Royal Princess
    'https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80': 'assets/images/pro_princess.jpg',
    
    # Unforgettable Magical Services (the one next to the list) - it was magic_package.jpg or similar.
    # From screenshot, it was actually a gemini generated image that was probably never replaced correctly, 
    # or was replaced with `1518991669955-9c7e78ec80ca`. 
    'https://images.unsplash.com/photo-1518991669955-9c7e78ec80ca?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80': 'assets/images/pro_classic_magic.jpg',
    
    # Any leftovers in Real Moments gallery that didn't get caught
    'assets/images/magic_show_party_1790842468826.jpg': 'assets/images/pro_classic_magic.jpg',
    'assets/images/kids_clapping_party_1790917531872.jpg': 'assets/images/pro_hero_party.jpg',
}

# Apply to all html files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    for old, new in updates.items():
        if old in html:
            html = html.replace(old, new)
            modified = True
            
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated images in {file}")
