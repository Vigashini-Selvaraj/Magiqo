import re

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make image replacements first
html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1608889476561-6242cfdbf622\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" class="hero-main-img".*?>',
    r'<img src="assets/images/pro_magical_services.jpg" class="hero-main-img" alt="Superhero Party Inspiration">',
    html
)

html = re.sub(
    r'<img src="assets/images/hero_magician_1790831867453\.jpg" alt="10 Reasons to Hire a Professional Magician".*?>',
    r'<img src="assets/images/pro_magician_2.jpg" alt="10 Reasons to Hire a Professional Magician" class="blog-img" onclick="location.href=\'blog_detail.html\'" style="cursor:pointer;">',
    html
)

html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1464047736614-af63643285bf\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Halloween Party Ideas That Are Spooky Not Scary".*?>',
    r'<img src="https://images.unsplash.com/photo-1509557965875-b88c97052f0e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Halloween Party Ideas That Are Spooky Not Scary" class="blog-img" onclick="location.href=\'blog_detail.html\'" style="cursor:pointer;">',
    html
)

html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Choosing the Right Clown for Toddlers".*?>',
    r'<img src="assets/images/pro_clown_blog.jpg" alt="Choosing the Right Clown for Toddlers" class="blog-img" onclick="location.href=\'blog_detail.html\'" style="cursor:pointer;">',
    html
)

html = re.sub(
    r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="How to Keep Adults Entertained at a Kid\'s Party".*?>',
    r'<img src="https://images.unsplash.com/photo-1511795409834-ef04bbd61622?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="How to Keep Adults Entertained at a Kid\'s Party" class="blog-img" onclick="location.href=\'blog_detail.html\'" style="cursor:pointer;">',
    html
)

# Gallery Replacements
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

# Now, reduce the number of blog blocks to 9.
grid_start_idx = html.find('<div class="blog-grid" id="blog-grid">')
if grid_start_idx != -1:
    grid_end_idx = html.find('<!-- END 20 BLOGS GRID -->', grid_start_idx)
    if grid_end_idx == -1:
        # Just find the end of the section
        grid_end_idx = html.find('</section>', grid_start_idx)
    
    grid_html = html[grid_start_idx:grid_end_idx]
    
    # We can split the grid by finding '<div class="blog-card"'
    split_str = '<div class="blog-card"'
    parts = grid_html.split(split_str)
    
    if len(parts) > 10: # More than 9 cards (parts[0] is the start of the grid)
        # Keep parts 1 to 8
        kept_parts = parts[1:9]
        
        # Find the adult card part
        adult_card = None
        for p in parts[1:]:
            if "How to Keep Adults Entertained" in p:
                adult_card = p
                break
        
        if adult_card and adult_card not in kept_parts:
            kept_parts.append(adult_card)
        else:
            kept_parts.append(parts[9])
            
        # Reconstruct the grid html
        new_grid_html = parts[0] + split_str + split_str.join(kept_parts) + "\n      </div>\n"
        html = html[:grid_start_idx] + new_grid_html + html[grid_end_idx:]

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(html)
