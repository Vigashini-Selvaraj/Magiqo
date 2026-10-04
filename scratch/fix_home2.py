import re

with open('c:/Users/vigas/Desktop/magiqo/home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update View Profile links to entertainer_detail.html
content = content.replace('href="entertainers.html" class="btn btn-outline" style="width: 100%;">View Profile', 'href="entertainer_detail.html" class="btn btn-outline" style="width: 100%;">View Profile')

# 2. Add Flip Card CSS
flip_card_css = """
    /* Flip Card CSS */
    .flip-card {
      background-color: transparent;
      perspective: 1000px;
      height: 280px;
      margin-bottom: 2rem;
    }
    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
      cursor: pointer;
    }
    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }
    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border-radius: var(--radius-lg);
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      box-shadow: 0 10px 20px var(--color-shadow);
    }
    .flip-card-front {
      background-color: var(--color-surface);
      color: var(--color-text);
      background-size: cover;
      background-position: center;
      position: relative;
    }
    /* Add an overlay to the front so text is readable over the image */
    .flip-card-front::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.6);
      border-radius: var(--radius-lg);
      z-index: 1;
    }
    .flip-card-front > * {
      position: relative;
      z-index: 2;
    }
    .flip-card-back {
      background: linear-gradient(135deg, var(--color-primary), #3895c8);
      color: white;
      transform: rotateY(180deg);
    }
    .flip-card-back p {
      color: rgba(255,255,255,0.9);
      font-size: 1.1rem;
      line-height: 1.6;
    }
"""

if "/* Flip Card CSS */" not in content:
    content = content.replace("</style>", flip_card_css + "\n</style>", 1)

# 3. Replace How the Magic Happens steps with flip cards
old_steps = """      <div class="steps-container">
        <div class="step-card">
          <div class="step-number">1</div>
          <h3>Discover</h3>
          <p>Browse our carefully vetted roster and select your child's absolute favorite entertainer based on age and theme.</p>
        </div>
        <div class="step-card">
          <div class="step-number">2</div>
          <h3>Customize</h3>
          <p>Choose your preferred date, precise duration, and select any special magical add-ons like decorations or gifts.</p>
        </div>
        <div class="step-card">
          <div class="step-number">3</div>
          <h3>Celebrate</h3>
          <p>Sit back and relax. Our professionals arrive fully prepared, on time, and ready to deliver an amazing experience.</p>
        </div>
      </div>"""

new_steps = """      <div class="steps-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
        
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front" style="background-image: url('assets/images/magic_show_party_1790842468826.jpg');">
              <div class="step-number" style="background: var(--color-primary); color: white; border: none;">1</div>
              <h3 style="color: white; -webkit-text-fill-color: white; text-shadow: 0 2px 5px rgba(0,0,0,0.5);">Discover</h3>
            </div>
            <div class="flip-card-back">
              <h3 style="color: white; -webkit-text-fill-color: white; margin-bottom: 1rem;">Discover</h3>
              <p>Browse our carefully vetted roster and select your child's absolute favorite entertainer based on age and theme.</p>
            </div>
          </div>
        </div>

        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front" style="background-image: url('assets/images/clown_party_1790842566084.jpg');">
              <div class="step-number" style="background: var(--color-primary); color: white; border: none;">2</div>
              <h3 style="color: white; -webkit-text-fill-color: white; text-shadow: 0 2px 5px rgba(0,0,0,0.5);">Customize</h3>
            </div>
            <div class="flip-card-back">
              <h3 style="color: white; -webkit-text-fill-color: white; margin-bottom: 1rem;">Customize</h3>
              <p>Choose your preferred date, precise duration, and select any special magical add-ons like decorations or gifts.</p>
            </div>
          </div>
        </div>

        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front" style="background-image: url('assets/images/superhero_party_1790842695325.jpg');">
              <div class="step-number" style="background: var(--color-primary); color: white; border: none;">3</div>
              <h3 style="color: white; -webkit-text-fill-color: white; text-shadow: 0 2px 5px rgba(0,0,0,0.5);">Celebrate</h3>
            </div>
            <div class="flip-card-back">
              <h3 style="color: white; -webkit-text-fill-color: white; margin-bottom: 1rem;">Celebrate</h3>
              <p>Sit back and relax. Our professionals arrive fully prepared, on time, and ready to deliver an amazing experience.</p>
            </div>
          </div>
        </div>

      </div>"""

content = content.replace(old_steps, new_steps)


# 4. Replace the Let the Magic Begin CTA styling
old_cta_start = """  <!-- 10. Let the Magic Begin (Orange Background CTA) -->
  <section class="cta-section">"""

new_cta_start = """  <!-- 10. Let the Magic Begin (Royal Background CTA) -->
  <section class="royal-cta" style="padding: 8rem 0; text-align: center; background: #1F1033; position: relative; overflow: hidden;">
    <style>
      .royal-cta::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at center, rgba(229, 193, 88, 0.15) 0%, transparent 70%);
        pointer-events: none;
      }
      .royal-btn-gold {
        background: #E5C158;
        color: #1F1033;
        padding: 1.25rem 4rem;
        font-size: 1.25rem;
        font-weight: 800;
        border-radius: var(--radius-pill);
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        border: 2px solid #E5C158;
        box-shadow: 0 10px 20px rgba(229, 193, 88, 0.3);
      }
      .royal-btn-gold:hover {
        background: transparent;
        color: #E5C158;
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(229, 193, 88, 0.4);
      }
    </style>"""

content = content.replace(old_cta_start, new_cta_start)

# Update the H2 styling in the CTA to use the golden color, circumventing the background-clip
old_cta_h2 = """<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Let the</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Magic Begin</span></h2>"""
new_cta_h2 = """<h2 style="background: none !important; -webkit-text-fill-color: #E5C158 !important; color: #E5C158 !important; text-shadow: 0 4px 15px rgba(229, 193, 88, 0.4); font-family: var(--font-magic); font-size: clamp(3rem, 5vw, 4.5rem);">Let the Magic Begin</h2>"""
content = content.replace(old_cta_h2, new_cta_h2)

# Update the CTA button
old_cta_btn = """<a href="packages.html" class="btn" style="padding: 1.25rem 4rem; font-size: 1.25rem; font-weight: bold;">Book Your Party Now</a>"""
new_cta_btn = """<a href="packages.html" class="royal-btn-gold">Book Your Party Now</a>"""
content = content.replace(old_cta_btn, new_cta_btn)


with open('c:/Users/vigas/Desktop/magiqo/home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
