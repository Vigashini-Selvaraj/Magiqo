import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hero Section Redesign
hero_pattern = r'<header class="hero" style="background: var\(--color-bg\); padding: 80px 0; overflow: hidden; position: relative;">.*?</header>'
new_hero = """  <header class="hero" style="position: relative; padding: 120px 0; overflow: hidden; display: flex; align-items: center; min-height: 80vh;">
    <!-- Full Width Background Image -->
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('assets/images/pro_hero_party.jpg') center/cover no-repeat; z-index: 1;"></div>
    
    <!-- Premium Dark Overlay for text readability -->
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(90deg, rgba(15,15,20,0.95) 0%, rgba(15,15,20,0.8) 50%, rgba(15,15,20,0.4) 100%); z-index: 2;"></div>

    <div class="container hero-container" style="position: relative; z-index: 3; display: flex; align-items: center; width: 100%;">
      
      <!-- Glassmorphism Card -->
      <div class="hero-text-content" style="max-width: 650px; background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); padding: 3rem; border-radius: 24px; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 30px 60px rgba(0,0,0,0.3);">
        
        <div style="display: inline-block; padding: 8px 16px; background: rgba(232, 62, 135, 0.2); border: 1px solid var(--color-primary); border-radius: 50px; color: var(--color-primary); font-weight: 600; font-size: 0.9rem; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 1px;">
          <i class="fa-solid fa-wand-magic-sparkles" style="margin-right: 8px;"></i> Premium Entertainment
        </div>

        <h1 style="font-size: clamp(3.5rem, 6vw + 1rem, 5.5rem); line-height: 1.1; margin-bottom: 1.5rem; font-family: var(--font-magic, 'Berkshire Swash'); font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
          <span style="color: #fff; -webkit-text-fill-color: #fff;">Make Their</span><br>
          <span style="background: linear-gradient(45deg, var(--color-primary), #3895c8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Day Magical.</span>
        </h1>
        
        <p style="font-size: clamp(1.1rem, 2vw, 1.25rem); color: rgba(255,255,255,0.85); margin-bottom: 2.5rem; line-height: 1.7;">
          Discover top-tier entertainers, choose the perfect experience, and create a birthday celebration they'll never forget with our premium performers.
        </p>

        <div class="hero-buttons" style="display: flex; gap: 1rem; flex-wrap: wrap;">
          <a href="entertainers.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2.5rem; border-radius: 50px; box-shadow: 0 10px 20px rgba(232, 62, 135, 0.3);">Explore Entertainers</a>
          <a href="packages.html" class="btn btn-secondary" style="font-size: 1.1rem; padding: 1rem 2.5rem; background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.2); color: white; border-radius: 50px; backdrop-filter: blur(5px);">Book Now</a>
        </div>
        
        <div style="margin-top: 2.5rem; display: flex; align-items: center; gap: 15px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
          <div style="display: flex;">
            <img src="assets/images/pro_hero_party.jpg" style="width: 40px; height: 40px; border-radius: 50%; border: 2px solid #111; object-fit: cover; margin-left: -10px; z-index: 3;">
            <img src="assets/images/pro_princess.jpg" style="width: 40px; height: 40px; border-radius: 50%; border: 2px solid #111; object-fit: cover; margin-left: -15px; z-index: 2;">
            <img src="assets/images/pro_magician.jpg" style="width: 40px; height: 40px; border-radius: 50%; border: 2px solid #111; object-fit: cover; margin-left: -15px; z-index: 1;">
          </div>
          <div>
            <div style="font-weight: bold; color: #fff; font-size: 1rem;">500+ Events</div>
            <div style="font-size: 0.85rem; color: rgba(255,255,255,0.6);">Successfully hosted this year</div>
          </div>
        </div>

      </div>
    </div>
  </header>"""

html = re.sub(hero_pattern, new_hero, html, flags=re.DOTALL)


# 2. Unforgettable Magical Services
html = html.replace('assets/images/service_magic_1790831898290.jpg', 'assets/images/pro_magical_services.jpg')

# 3. Silly Clowns Card and Blog Post (which both use the same old URL)
old_clown_url = 'https://images.unsplash.com/photo-1513689456070-07085750d535?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'

# Find the Silly Clowns card occurrence and replace with pro_silly_clown
silly_clowns_pattern = r"(<h3[^>]*>Silly Clowns</h3>.*?)(https://images.unsplash.com/photo-1513689456070-07085750d535\?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80)"
# Wait, regex might be tricky if they are backwards. The URL appears in the style tag and onclick before the h3. 
# Let's just do an exact replace for the first one that appears in the experiences grid.
# The URL appears multiple times. Let's replace them carefully based on context.

# Let's replace the blog one specifically:
html = html.replace(old_clown_url + "'\"", "assets/images/pro_clown_blog.jpg'\"") # In onclick
html = html.replace('img src="' + old_clown_url + '"', 'img src="assets/images/pro_clown_blog.jpg"')

# And the remaining ones (Silly Clowns grid card and finder results) with pro_silly_clown:
html = html.replace(old_clown_url, 'assets/images/pro_silly_clown.jpg')


# 4. Real Party Moments - 4th Image (First image in capture-smile-wrapper)
# Currently:
# <img src="assets/images/pro_hero_party.jpg" alt="Gallery Image"
# style="width: 100%; height: 250px; object-fit: cover; border-radius: var(--radius-md); cursor: pointer; transition: transform 0.3s;"
# onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
# Let's just find the first instance of pro_hero_party in the capture-smile-wrapper block and replace it.

capture_block = html.find('capture-smile-wrapper')
if capture_block != -1:
    before = html[:capture_block]
    after = html[capture_block:]
    after = after.replace('assets/images/pro_hero_party.jpg', 'assets/images/pro_gallery_alt.jpg', 1)
    html = before + after

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
