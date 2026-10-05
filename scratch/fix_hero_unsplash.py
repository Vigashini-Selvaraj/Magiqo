import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Hero Section
hero_pattern = r'<header class="hero">.*?</header>'
new_hero = """  <header class="hero" style="background: var(--color-bg); padding: 80px 0; overflow: hidden; position: relative;">
    
    <!-- Subtle background accent -->
    <div style="position: absolute; top: -100px; right: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(210, 75, 118, 0.05) 0%, rgba(0,0,0,0) 70%); border-radius: 50%; pointer-events: none;"></div>

    <div class="container hero-container" style="display: flex; align-items: center; justify-content: space-between; gap: 4rem; position: relative;">
      
      <div class="hero-text-content" style="flex: 1; max-width: 600px;">
        <h1 style="font-size: clamp(3rem, 5vw + 1rem, 4.5rem); line-height: 1.1; margin-bottom: 1.5rem; font-family: var(--font-magic, 'Berkshire Swash'); font-weight: 900;">
          <span style="color: var(--color-primary);">Make Their</span><br>
          <span style="color: #3895c8;">Day Magical.</span>
        </h1>
        <p style="font-size: clamp(1.1rem, 2vw, 1.25rem); color: var(--color-text-light); margin-bottom: 2.5rem; max-width: 480px; line-height: 1.6;">
          Discover top-tier entertainers, choose the perfect experience, and create a birthday celebration they'll never forget with our premium performers.
        </p>

        <div class="hero-buttons" style="display: flex; gap: 1rem;">
          <a href="entertainers.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2rem; border-radius: 8px;">Explore Entertainers</a>
          <a href="packages.html" class="btn btn-secondary" style="font-size: 1.1rem; padding: 1rem 2rem; background: #3895c8; border-color: #3895c8; color: white; border-radius: 8px;">Book Now</a>
        </div>
      </div>

      <div class="hero-image-content" style="flex: 1; display: flex; justify-content: center; align-items: center; position: relative;">
        <!-- Premium Unsplash image of a kid's birthday party -->
        <img src="https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Magical Birthday Party" style="width: 100%; max-width: 550px; border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); object-fit: cover; aspect-ratio: 4/3;">
        
        <!-- Decorative floating element -->
        <div style="position: absolute; bottom: -20px; left: -20px; background: var(--color-surface); padding: 15px 25px; border-radius: 12px; border: 1px solid var(--color-border); box-shadow: 0 10px 20px rgba(0,0,0,0.2); display: flex; align-items: center; gap: 15px;">
          <i class="fa-solid fa-star" style="color: #FFBE0B; font-size: 1.5rem;"></i>
          <div>
            <div style="font-weight: bold; color: var(--color-text);">500+ Events</div>
            <div style="font-size: 0.85rem; color: var(--color-text-light);">Successfully hosted</div>
          </div>
        </div>
      </div>
      
    </div>
  </header>"""

html = re.sub(hero_pattern, new_hero, html, flags=re.DOTALL)


# 2. Replace all AI images with beautiful Unsplash alternatives in index.html
unsplash_map = {
    'assets/images/founder_mark.jpg': 'https://images.unsplash.com/photo-1542156822-6924d1a71ace?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Magician/performer guy
    'assets/images/happy_kids_clown.jpg': 'https://images.unsplash.com/photo-1513689456070-07085750d535?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Clown/party
    'assets/images/clown_party_1790842566084.jpg': 'https://images.unsplash.com/photo-1513689456070-07085750d535?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Clown/party
    'assets/images/james_boy_smile.jpg': 'https://images.unsplash.com/photo-1508214751196-bfdd4ca401fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Kid smiling
    'assets/images/emily_girl_smile.jpg': 'https://images.unsplash.com/photo-1519689680058-324335c77eba?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Kid girl smiling
    'assets/images/magic_package.jpg': 'https://images.unsplash.com/photo-1518991669955-9c7e78ec80ca?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Magic wand/hat
    'assets/images/princess_party_1790842645232.jpg': 'https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Princess
    'assets/images/superhero_party_1790842695325.jpg': 'https://images.unsplash.com/photo-1608889476561-6242cfdbf622?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', # Superhero
    'assets/images/gallery_smile_1.jpg': 'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/cute_kids_clapping_1790833571210.jpg': 'https://images.unsplash.com/photo-1464047736614-af63643285bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/gallery_smile_2.jpg': 'https://images.unsplash.com/photo-1511895426328-dc8714191300?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/party_moments_2_1790918669697.jpg': 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
    'assets/images/blog_party_ideas_1790831919409.jpg': 'https://images.unsplash.com/photo-1530103862676-de8892bc952f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
}

for old, new in unsplash_map.items():
    html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
