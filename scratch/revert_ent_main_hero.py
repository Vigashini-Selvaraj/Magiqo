import re

file_path = 'c:/Users/vigas/Desktop/magiqo/entertainers.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Restore CSS
original_css = '''
    /* 1. Entertainers Hero (Redesigned) */
    .ent-hero {
      position: relative; min-height: 90vh; display: flex; align-items: center; justify-content: center;
      background: linear-gradient(135deg, var(--color-bg) 0%, var(--color-bg) 45%, #3895c8 45%, #3895c8 100%);
      padding-top: 150px; padding-bottom: 120px; overflow: hidden;
    }
    .ent-hero-content { position: relative; z-index: 2; width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 3rem; }
    .hero-text { flex: 1; text-align: left; max-width: 600px; }
    .hero-text h1 { font-family: var(--font-magic, 'Berkshire Swash'); font-size: clamp(3rem, 5vw + 1rem, 5.5rem); font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); margin-bottom: 1.5rem; color: var(--color-primary) !important; -webkit-text-fill-color: var(--color-primary) !important; background: none !important; line-height: 1.1; }
    .hero-text p { font-size: 1.25rem; font-weight: 400; margin-bottom: 2.5rem; color: var(--color-text-light); line-height: 1.6; }
    .hero-btn { background: var(--color-primary); color: #fff; padding: 1rem 2.5rem; border-radius: var(--radius-pill); font-weight: bold; font-size: 1.125rem; display: inline-block; transition: transform 0.3s; box-shadow: 0 5px 15px rgba(218, 47, 95, 0.3); }
    .hero-btn:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(218, 47, 95, 0.4); color: white; background-color: var(--color-primary-hover); }
    
    .hero-visual { flex: 1; display: flex; justify-content: center; position: relative; }
    .scallop-container { 
      position: relative; width: 450px; height: 450px; 
      display: flex; align-items: center; justify-content: center;
      background: var(--color-surface); border-radius: 50%; padding: 15px;
      box-shadow: 0 0 0 10px #a9e0ff, 0 15px 40px rgba(0,0,0,0.15);
      animation: float 6s ease-in-out infinite;
    }
    .scallop-img { width: 100%; height: 100%; border-radius: 50%; object-fit: cover; }
    
    /* Decorative elements */
    .hero-deco { position: absolute; pointer-events: none; z-index: 3; }
    .bubble { border-radius: 50%; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.9), rgba(255,255,255,0.4) 70%, transparent); box-shadow: inset -5px -5px 15px rgba(0,0,0,0.1), 0 10px 20px rgba(0,0,0,0.1); animation: float 4s infinite ease-in-out alternate; }
    
    /* Wavy Divider at bottom */
    .custom-shape-divider-bottom { position: absolute; bottom: 0; left: 0; width: 100%; overflow: hidden; line-height: 0; }
    .custom-shape-divider-bottom svg { position: relative; display: block; width: calc(100% + 1.3px); height: 80px; }
    .custom-shape-divider-bottom .shape-fill { fill: var(--color-bg); }
    
    @media (max-width: 992px) {
      .ent-hero-content { flex-direction: column; text-align: center; }
      .hero-text { text-align: center; margin-bottom: 3rem; }
      .scallop-container { width: 350px; height: 350px; }
    }
'''
content = re.sub(r'/\* 1\. Entertainers Hero.*?/\* 4\. Featured Stars \*/', original_css + '\n\n    /* 4. Featured Stars */', content, flags=re.DOTALL)


# Restore HTML
original_html = '''
  <!-- 1. Hero -->
  <section class="ent-hero">
    <!-- Decorative Bubbles -->
    <div class="hero-deco bubble" style="width: 80px; height: 80px; top: 15%; left: 10%;"></div>
    <div class="hero-deco bubble" style="width: 50px; height: 50px; top: 65%; left: 5%;"></div>
    <div class="hero-deco bubble" style="width: 100px; height: 100px; top: 20%; right: 10%; animation-delay: 1s;"></div>
    <div class="hero-deco bubble" style="width: 60px; height: 60px; bottom: 30%; right: 25%; animation-delay: 0.5s;"></div>
    
    <div class="container ent-hero-content">
      <div class="hero-text">
        <h1><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">The Children's Favourite</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Party Entertainers!</span></h1>
        <p>Our mission is to make kids parties hassle-free and enjoyable experience. So you can relax and have fun with your kids.</p>
        <a href="#roster" class="hero-btn">View All Parties &rarr;</a>
      </div>
      <div class="hero-visual">
        <div class="scallop-container">
          <img src="assets/images/entertainer_ui_hero.jpg" alt="Happy Kids at Party" class="scallop-img">
        </div>
      </div>
    </div>

    <!-- Wavy Divider -->
    <div class="custom-shape-divider-bottom">
        <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V0C73.23,12,143.14,24.12,209.4,35.48,247.16,42,284.52,50,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
  </section>
'''

content = re.sub(r'<!-- 1\. Hero -->.*?</section>', original_html, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Reverted entertainers.html hero section')
