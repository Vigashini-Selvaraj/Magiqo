import re

about_path = r'c:\Users\vigas\Desktop\magiqo\about.html'
blog_path = r'c:\Users\vigas\Desktop\magiqo\blog.html'

with open(about_path, 'r', encoding='utf-8') as f:
    about_lines = f.readlines()

hero_css_lines = about_lines[49:193] + ["\n    @media (max-width: 992px) {\n"] + about_lines[485:506] + ["    }\n"]
hero_css = "".join(hero_css_lines)

hero_html_lines = about_lines[534:570]
hero_html = "".join(hero_html_lines)

with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

# Replace Blog Hero CSS
blog_content = re.sub(r'/\* 1\. Blog Hero \*/.*?/\* Explore Categories \*/', '/* Explore Categories */', blog_content, flags=re.DOTALL)

# Insert new CSS at the top of <style>
blog_content = blog_content.replace('<style>', '<style>\n' + hero_css)

# Replace Blog Hero HTML
blog_content = re.sub(r'<!-- 1\. BLOG HERO -->.*?<main>', '<!-- 1. BLOG HERO -->\n' + hero_html + '\n  <main>', blog_content, flags=re.DOTALL)

# Modify the Blog Hero text
blog_content = blog_content.replace(
    '''<h1 class="hero-title"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Parties they'll</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">look forward to.</span></h1>''',
    '''<h1 class="hero-title"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Ideas That Make</span> <br><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Every Celebration Magical</span></h1>'''
)
blog_content = blog_content.replace(
    '''<p class="hero-desc">Expert premium entertainment for children of all ages. Bringing joy directly to your door.</p>''',
    '''<p class="hero-desc">Discover inspiration, themes, expert planning tips, and fun activities to create unforgettable moments.</p>'''
)
blog_content = blog_content.replace(
    '''<div class="hero-badge">
          <i class="fa-solid fa-star"></i> Award-Winning Entertainment
        </div>''',
    '''<div class="hero-badge">
          <i class="fa-solid fa-pen-nib"></i> Magiqo Official Blog
        </div>'''
)

# Modify float card
blog_content = blog_content.replace(
    '''<span style="font-weight: bold; color: var(--color-text); font-size: 1.1rem;">500+</span>''',
    '''<span style="font-weight: bold; color: var(--color-text); font-size: 1.1rem;">Daily</span>'''
)
blog_content = blog_content.replace(
    '''<span style="font-size: 0.9rem; color: var(--color-text-light);">Events Hosted</span>''',
    '''<span style="font-size: 0.9rem; color: var(--color-text-light);">Inspiration</span>'''
)
# Modify Image
blog_content = blog_content.replace(
    '''<img src="assets/images/about_kids_birthday.jpg" class="hero-main-img" alt="Kids celebrating a magical birthday">''',
    '''<img src="assets/images/superhero_party_1790842695325.jpg" class="hero-main-img" alt="Superhero Party Inspiration">'''
)
# Modify buttons
blog_content = blog_content.replace(
    '''<a href="booking.html" class="btn btn-primary" style="padding: 15px 30px; font-size: 1.1rem; border-radius: 50px; text-decoration: none; font-weight: bold;">Book Now</a>''',
    '''<a href="#articles" class="btn btn-primary" style="padding: 15px 30px; font-size: 1.1rem; border-radius: 50px; text-decoration: none; font-weight: bold;">Explore Articles</a>'''
)
blog_content = blog_content.replace(
    '''<a href="packages.html" class="btn btn-outline" style="padding: 15px 30px; font-size: 1.1rem; border-radius: 50px; text-decoration: none; font-weight: bold; border: 2px solid var(--color-primary); color: var(--color-primary);">View Packages</a>''',
    ''''''
)

with open(blog_path, 'w', encoding='utf-8') as f:
    f.write(blog_content)
print('Done!')
