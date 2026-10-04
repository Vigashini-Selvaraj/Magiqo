import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero title color
content = content.replace('color: var(--color-text) !important; -webkit-text-fill-color: var(--color-text) !important;', 'color: var(--color-primary) !important; -webkit-text-fill-color: var(--color-primary) !important;')

# 2. Find your perfect entertainer colors
old_find = '<h2 style="color: var(--color-primary);">Find Your Perfect Entertainer</h2>'
new_find = '<h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Find Your</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Perfect Entertainer</span></h2>'
content = content.replace(old_find, new_find)

# 3. Add background color to quiz box to make it attractive
old_quiz = 'div class="interactive-finder" style="background: white;'
new_quiz = 'div class="interactive-finder" style="background: linear-gradient(to bottom right, #ffffff, #f0f8ff);'
content = content.replace(old_quiz, new_quiz)

# 4. Review images for James and Emily
parts = content.split('<img src="assets/images/gallery_smile_1.jpg"')
if len(parts) >= 4:
    parts[2] = parts[2].replace('alt="Happy Kid"', 'alt="James"')
    parts[3] = parts[3].replace('alt="Happy Kid"', 'alt="Emily"')
    
    content = parts[0] + '<img src="assets/images/gallery_smile_1.jpg"' + parts[1] + '<img src="assets/images/james_boy_smile.jpg"' + parts[2] + '<img src="assets/images/emily_girl_smile.jpg"' + parts[3]
    for i in range(4, len(parts)):
        content += '<img src="assets/images/gallery_smile_1.jpg"' + parts[i]

# 5. Magiqo standards flip cards
standards_css_old = """    .standards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem; }
    .standard-item { display: flex; align-items: flex-start; gap: 1.5rem; background: white; padding: 2rem; border-radius: var(--radius-lg); border-left: 4px solid var(--color-primary); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .standard-item svg { width: 50px; height: 50px; fill: #3895c8; flex-shrink: 0; }
    .standard-text h3 { font-family: var(--font-heading); font-size: 1.5rem; color: var(--color-text); margin-bottom: 0.5rem; }
    .standard-text p { color: var(--color-text-light); line-height: 1.6; font-size: 1rem; margin: 0; }"""

standards_css_new = """    .standards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2.5rem; perspective: 1000px; }
    .flip-card { background-color: transparent; height: 350px; perspective: 1000px; cursor: pointer; }
    .flip-card-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.8s; transform-style: preserve-3d; }
    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }
    .flip-card-front, .flip-card-back { position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: var(--radius-xl); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 2rem; box-shadow: 0 15px 35px rgba(0,0,0,0.05); border: 1px solid var(--color-border); }
    .flip-card-front { background-color: white; color: var(--color-text); }
    .flip-card-front svg { width: 80px; height: 80px; fill: #3895c8; margin-bottom: 1.5rem; padding: 15px; background: rgba(56, 149, 200, 0.1); border-radius: 50%; }
    .flip-card-front h3 { font-family: var(--font-magic); font-size: 2rem; color: #2e19a7; margin-bottom:0; }
    .flip-card-back { background: linear-gradient(135deg, var(--color-primary), #3895c8); color: white; transform: rotateY(180deg); }
    .flip-card-back p { font-size: 1.2rem; line-height: 1.6; opacity: 0.95; font-weight: 500; }"""
content = content.replace(standards_css_old, standards_css_new)

old_standards_html = """<div class="standards-grid">
        <div class="standard-item">
          <svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
          <div class="standard-text">
             <h3>Background Checked</h3>
             <p>Every single entertainer undergoes a comprehensive nationwide background check and reference verification.</p>
          </div>
        </div>
        <div class="standard-item">
          <svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"/></svg>
          <div class="standard-text">
             <h3>Professionally Trained</h3>
             <p>Our talent attends rigorous Magiqo Workshops to master crowd control and the art of highly-engaging performance.</p>
          </div>
        </div>
        <div class="standard-item">
          <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 12h-4v-4h4v4zm0-6h-4V5h4v4zm6 6h-4v-4h4v4zm0-6h-4V5h4v4z"/></svg>
          <div class="standard-text">
             <h3>Fully Insured</h3>
             <p>We are fully licensed and hold robust liability insurance, giving parents complete peace of mind.</p>
          </div>
        </div>
      </div>"""

new_standards_html = """<div class="standards-grid">
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
              <h3>Background Checked</h3>
            </div>
            <div class="flip-card-back">
              <p>Every single entertainer undergoes a comprehensive nationwide background check and reference verification.</p>
            </div>
          </div>
        </div>
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"/></svg>
              <h3>Professionally Trained</h3>
            </div>
            <div class="flip-card-back">
              <p>Our talent attends rigorous Magiqo Workshops to master crowd control and the art of highly-engaging performance.</p>
            </div>
          </div>
        </div>
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 12h-4v-4h4v4zm0-6h-4V5h4v4zm6 6h-4v-4h4v4zm0-6h-4V5h4v4z"/></svg>
              <h3>Fully Insured</h3>
            </div>
            <div class="flip-card-back">
              <p>We are fully licensed and hold robust liability insurance, giving parents complete peace of mind.</p>
            </div>
          </div>
        </div>
      </div>"""
content = content.replace(old_standards_html, new_standards_html)

# 6. Book your star to be in white font
content = content.replace('<h2>Book Your Star</h2>', '<h2 style="color: white !important; -webkit-text-fill-color: white !important;">Book Your Star</h2>')

# 7. Add close icon to modal
old_modal = """<div class="modal-avail-content">
      <h3>Good News!</h3>"""
new_modal = """<div class="modal-avail-content" style="position: relative;">
      <button onclick="document.getElementById('availModal').classList.remove('active')" style="position: absolute; top: 1rem; right: 1rem; background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--color-text);">&times;</button>
      <h3>Good News!</h3>"""
content = content.replace(old_modal, new_modal)

# 8. Have a talent for magic - use purple color
content = content.replace('.join-banner { background: white; border: 2px dashed #3895c8;', '.join-banner { background: var(--color-secondary); border: none;')
content = content.replace('.join-text h2 { color: var(--color-primary) !important; -webkit-text-fill-color: var(--color-primary) !important; font-size: 3rem; }', '.join-text h2 { color: white !important; -webkit-text-fill-color: white !important; font-size: 3rem; }')
content = content.replace('.join-text p { color: var(--color-text-light); font-size: 1.2rem; }', '.join-text p { color: rgba(255,255,255,0.9); font-size: 1.2rem; }')

# 9. Let the magic begin redesign
old_cta_css = '.cta-section { background: #6a1b9a; padding: 6rem 0; text-align: center; color: white; }'
new_cta_css = '.cta-section { background: repeating-conic-gradient(from 0deg, var(--color-primary) 0deg 10deg, #c72551 10deg 20deg); padding: 8rem 0; text-align: center; color: white; position: relative; overflow: hidden; }'
content = content.replace(old_cta_css, new_cta_css)

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
