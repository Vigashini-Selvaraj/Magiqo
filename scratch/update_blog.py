import re

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hero Section Image
html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1608889476561-6242cfdbf622\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" class="hero-main-img" alt="Superhero Party Inspiration">',
    r'<img src="assets/images/pro_magical_services.jpg" class="hero-main-img" alt="Superhero Party Inspiration">',
    html
)

# 2. "10 Reasons to Hire a Professional Magician"
html = re.sub(
    r'<img src="assets/images/hero_magician_1790831867453\.jpg" alt="10 Reasons to Hire a Professional Magician"',
    r'<img src="assets/images/pro_magician_2.jpg" alt="10 Reasons to Hire a Professional Magician"',
    html
)

# 3. "Halloween Party Ideas That Are Spooky Not Scary"
html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1464047736614-af63643285bf\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Halloween Party Ideas That Are Spooky Not Scary"',
    r'<img src="https://images.unsplash.com/photo-1509557965875-b88c97052f0e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Halloween Party Ideas That Are Spooky Not Scary"',
    html
)

# 4. "Choosing the Right Clown for Toddlers"
html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Choosing the Right Clown for Toddlers"',
    r'<img src="assets/images/pro_clown_blog.jpg" alt="Choosing the Right Clown for Toddlers"',
    html
)

# 5. "How to Keep Adults Entertained at a Kid's Party"
html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="How to Keep Adults Entertained at a Kid\'s Party"',
    r'<img src="https://images.unsplash.com/photo-1511795409834-ef04bbd61622?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="How to Keep Adults Entertained at a Kid\'s Party"',
    html
)

# 6. Party Inspiration Gallery (Lines 705-708)
# We have a block of images: 
# <img src="https://images.unsplash.com/photo-1608889476561-6242cfdbf622?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Superhero Setup">
# <img src="assets/images/pro_princess.jpg" alt="Princess Setup">
# <img src="https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Kids Setup">
# <img src="https://images.unsplash.com/photo-1508214751196-bfdd4ca401fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Happy Kid">
gallery_replacements = [
    (r'<img src="https://images.unsplash\.com/photo-1608889476561-6242cfdbf622\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Superhero Setup">',
     r'<img src="assets/images/pro_magician_2.jpg" alt="Magician Setup">'),
    (r'<img src="https://images.unsplash\.com/photo-1502086223501-7ea6ecd79368\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Kids Setup">',
     r'<img src="assets/images/pro_memory.jpg" alt="Kids Setup">'),
    (r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Happy Kid">',
     r'<img src="assets/images/pro_gallery_alt.jpg" alt="Happy Kid">')
]
for old, new in gallery_replacements:
    html = re.sub(old, new, html)


# 7. Remove all blog blocks except 9.
# We will find all `<div class="blog-card"` blocks.
cards = re.split(r'(<div class="blog-card")', html)
# cards[0] is everything before the first card
# cards[1] is `<div class="blog-card"`
# cards[2] is the rest of the first card up to the second card, etc.
# Actually, re.split with a group will return [before_1, div, after_1_before_2, div, after_2_before_3...]

# Let's write a safer card extractor
card_pattern = re.compile(r'<div class="blog-card"(?:(?!<div class="blog-card").)*?</article>\s*</div>(?=\s*(?:<div class="blog-card"|</section>))', re.DOTALL)
# Wait, the cards end with `</div>` (actually they might end with just `</div>` without `</article>`).
# Let's just find the start of `<div class="blog-grid" id="blog-grid">`
# and the end `</section>` (which ends the blog section).

def keep_9_blocks(html_text):
    grid_start_idx = html_text.find('<div class="blog-grid" id="blog-grid">')
    if grid_start_idx == -1: return html_text
    
    grid_end_idx = html_text.find('</section>', grid_start_idx)
    grid_html = html_text[grid_start_idx:grid_end_idx]
    
    # Split by blog-card
    parts = grid_html.split('<div class="blog-card"')
    if len(parts) <= 10: 
        return html_text # Already 9 or fewer
    
    # parts[0] is the <div class="blog-grid"...> and <div class="no-results"...>
    # parts[1] is the content of card 1, starting with ` data-category=...`
    # We want to keep 9 specific cards.
    # We definitely want:
    # 1. 10 Reasons...
    # 2. How to Build...
    # 3. DIY Princess...
    # 4. Ultimate Guide...
    # 5. 5 Tips...
    # 6. Halloween Party Ideas...
    # 7. Choosing the Right Clown...
    # 8. (Any, let's keep Top 5 Party Favors)
    # 9. How to Keep Adults Entertained (which is in part 20)
    
    # Let's find the adult one
    adult_card = None
    for p in parts[1:]:
        if 'How to Keep Adults Entertained' in p:
            adult_card = p
            break
            
    if not adult_card:
        adult_card = parts[9] if len(parts) > 9 else ""

    # Build the new grid html
    new_grid_html = parts[0]
    for i in range(1, 9):
        new_grid_html += '<div class="blog-card"' + parts[i]
        
    new_grid_html += '<div class="blog-card"' + adult_card
    
    # Add closing div for blog-grid if not present in the last card
    # Wait, the last card in parts[20] has the closing `</div> <!-- end container -->` inside it?
    # No, `parts` is just split by `<div class="blog-card"`. The closing `</div>` of the grid might be in the last part.
    # Let's check what's at the end of grid_html.
    if "</div>\n    </div>" in parts[-1]:
        # We need to extract the closing tags from the very last part
        closing_tags = parts[-1][parts[-1].rfind('</div>', 0, parts[-1].rfind('</div>')):] 
        # This is messy. Let's just do a simpler approach.
        pass
        
    # Better approach:
    return html_text

html = keep_9_blocks(html)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(html)
