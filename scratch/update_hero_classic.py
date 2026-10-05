import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the start and end of the hero section
start_idx = html.find('<header class="hero-editorial"')
if start_idx == -1:
    start_idx = html.find('<header class="hero"')

end_idx = html.find('</header>') + len('</header>')

if start_idx != -1 and end_idx != -1:
    new_hero = """  <header class="hero-classic" style="position: relative; width: 100%; min-height: 90vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 100px 20px; background: url('assets/images/pro_hero_party.jpg') center/cover no-repeat; overflow: hidden;">
    
    <!-- Dark overlay for readability -->
    <div style="position: absolute; inset: 0; background: rgba(10, 10, 15, 0.75); z-index: 1;"></div>
    
    <!-- Content Container -->
    <div style="position: relative; z-index: 10; max-width: 900px; display: flex; flex-direction: column; align-items: center;">
      
      <!-- Label -->
      <div style="font-size: 0.9rem; font-weight: 800; letter-spacing: 3px; color: var(--color-primary); margin-bottom: 25px; text-transform: uppercase;">
        ENTERTAINMENT FOR MOMENTS THAT MATTER
      </div>
      
      <!-- Title -->
      <h1 style="font-family: var(--font-magic); font-size: clamp(3.5rem, 8vw, 6.5rem); font-weight: normal; line-height: 1.1; margin: 0 0 25px 0; color: white;">
        Make Their Day Magical
      </h1>
      
      <!-- Description -->
      <p style="font-size: 1.3rem; color: rgba(255,255,255,0.85); max-width: 700px; line-height: 1.7; margin-bottom: 45px; font-weight: 400;">
        Discover talented entertainers, choose the perfect experience, and create a celebration they'll remember forever.
      </p>
      
      <!-- Buttons -->
      <div style="display: flex; gap: 20px; justify-content: center; margin-bottom: 50px; flex-wrap: wrap;">
        <a href="entertainers.html" class="btn btn-primary" style="padding: 18px 45px; border-radius: 50px; font-weight: 700; font-size: 1.15rem; box-shadow: 0 10px 30px rgba(232, 62, 135, 0.4);">Explore Entertainers</a>
        <a href="packages.html" style="padding: 18px 45px; border-radius: 50px; font-weight: 700; font-size: 1.15rem; color: white; background: rgba(255,255,255,0.1); border: 2px solid rgba(255,255,255,0.3); text-decoration: none; transition: 0.3s; backdrop-filter: blur(5px);">View Packages</a>
      </div>

      <!-- Trust indicators -->
      <div style="display: flex; gap: 25px; font-size: 1rem; color: rgba(255,255,255,0.7); font-weight: 600; flex-wrap: wrap; justify-content: center;">
        <span style="display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-check" style="color: var(--color-primary);"></i> 500+ Celebrations</span>
        <span class="d-none-mobile">•</span>
        <span style="display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-check" style="color: var(--color-primary);"></i> Verified Entertainers</span>
        <span class="d-none-mobile">•</span>
        <span style="display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-check" style="color: var(--color-primary);"></i> Easy Booking</span>
      </div>
      
    </div>

    <!-- Scroll Indicator -->
    <div style="position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); z-index: 10; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; color: rgba(255,255,255,0.6); text-transform: uppercase; display: flex; flex-direction: column; align-items: center; gap: 10px;">
      <span>Scroll To Discover</span>
      <span style="font-size: 1.5rem; font-weight: 300;">↓</span>
    </div>
  </header>"""

    html = html[:start_idx] + new_hero + html[end_idx:]
    
    # Let's add some hover effect to the secondary button for polish
    if ".hero-classic .btn-outline:hover" not in html:
        css_addition = """<style>
    .hero-classic a[href="packages.html"]:hover {
        background: rgba(255,255,255,0.2) !important;
        border-color: rgba(255,255,255,0.6) !important;
    }
  </style>"""
        html = html.replace('</head>', f'{css_addition}\n</head>')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Updated index.html to classic hero successfully.")
else:
    print("Could not find hero section boundaries.")
