import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the start and end of the hero section
start_idx = html.find('<header class="hero-classic"')
if start_idx == -1:
    start_idx = html.find('<header class="hero"')
if start_idx == -1:
    start_idx = html.find('<header class="hero-editorial"')

end_idx = html.find('</header>') + len('</header>')

if start_idx != -1 and end_idx != -1:
    new_hero = """  <header class="hero-split" style="position: relative; width: 100%; min-height: 90vh; display: flex; align-items: center; background: var(--color-bg); overflow: hidden; padding: 120px 0 80px 0;">
    
    <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; position: relative; z-index: 2;">
      
      <!-- Left Content -->
      <div style="max-width: 600px;">
        <div style="display: inline-block; padding: 8px 16px; background: rgba(232, 62, 135, 0.1); border-radius: 50px; color: var(--color-primary); font-weight: 700; font-size: 0.85rem; margin-bottom: 25px; letter-spacing: 2px;">
          <i class="fa-solid fa-star" style="margin-right: 8px;"></i> PREMIUM EVENT ENTERTAINMENT
        </div>
        
        <h1 style="font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 5.5rem); line-height: 1.1; margin: 0 0 25px 0; color: var(--color-text);">
          Make Their Day <br><span style="color: var(--color-primary);">Magical</span>
        </h1>
        
        <p style="font-size: 1.25rem; color: var(--color-text-light); line-height: 1.7; margin-bottom: 40px;">
          Discover talented entertainers, choose the perfect experience, and create a celebration they'll remember forever.
        </p>
        
        <div style="display: flex; gap: 20px; flex-wrap: wrap;">
          <a href="entertainers.html" class="btn btn-primary" style="padding: 16px 35px; border-radius: 50px; font-weight: 700; font-size: 1.1rem; box-shadow: 0 10px 25px rgba(232, 62, 135, 0.3);">Explore Entertainers</a>
          <a href="packages.html" style="padding: 16px 35px; border-radius: 50px; font-weight: 700; font-size: 1.1rem; color: var(--color-text); border: 2px solid var(--color-border); text-decoration: none; transition: 0.3s;">View Packages</a>
        </div>
        
        <div style="margin-top: 45px; display: flex; align-items: center; gap: 20px; border-top: 1px solid var(--color-border); padding-top: 25px;">
          <div style="display: flex;">
            <img src="assets/images/pro_hero_party.jpg" style="width: 45px; height: 45px; border-radius: 50%; border: 3px solid var(--color-bg); object-fit: cover; margin-left: 0; z-index: 3;">
            <img src="assets/images/pro_princess.jpg" style="width: 45px; height: 45px; border-radius: 50%; border: 3px solid var(--color-bg); object-fit: cover; margin-left: -15px; z-index: 2;">
            <img src="assets/images/pro_magician_2.jpg" style="width: 45px; height: 45px; border-radius: 50%; border: 3px solid var(--color-bg); object-fit: cover; margin-left: -15px; z-index: 1;">
          </div>
          <div>
            <div style="font-weight: 800; color: var(--color-text); font-size: 1.1rem;">500+ Verified Performers</div>
            <div style="font-size: 0.9rem; color: var(--color-text-light);">Ready to amaze your guests</div>
          </div>
        </div>
      </div>
      
      <!-- Right Image Grid (Bento Style) -->
      <div style="position: relative; height: 600px; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr; gap: 20px;">
        
        <!-- Large Left Image -->
        <div style="grid-row: 1 / span 2; border-radius: 30px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.15);">
          <img src="assets/images/pro_magician_2.jpg" alt="Magician" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        
        <!-- Top Right Image -->
        <div style="border-radius: 30px; overflow: hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">
          <img src="assets/images/pro_princess.jpg" alt="Princess" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        
        <!-- Bottom Right Image -->
        <div style="border-radius: 30px; overflow: hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">
          <img src="assets/images/pro_silly_clown.jpg" alt="Clown" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        
        <!-- Floating Badge -->
        <div style="position: absolute; top: 40px; left: -40px; background: var(--color-surface); padding: 15px 25px; border-radius: 20px; border: 1px solid var(--color-border); box-shadow: 0 20px 40px rgba(0,0,0,0.15); display: flex; align-items: center; gap: 15px; animation: floatCard 5s infinite ease-in-out;">
          <div style="background: rgba(255, 190, 11, 0.15); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
            <i class="fa-solid fa-star" style="color: #FFBE0B; font-size: 1.5rem;"></i>
          </div>
          <div>
            <div style="font-weight: 800; color: var(--color-text); font-size: 1.2rem;">4.9/5</div>
            <div style="font-size: 0.9rem; color: var(--color-text-light);">Customer Rating</div>
          </div>
        </div>

      </div>
      
    </div>
    
    <!-- Responsive CSS for Split Hero -->
    <style>
      @media (max-width: 992px) {
        .hero-split .container { grid-template-columns: 1fr !important; }
        .hero-split { padding: 100px 0 50px 0 !important; }
      }
    </style>
  </header>"""

    html = html[:start_idx] + new_hero + html[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Updated index.html to split hero successfully.")
else:
    print("Could not find hero section boundaries.")
