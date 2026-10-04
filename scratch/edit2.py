import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS changes: Remove gradient from .sec-title h2
old_sec_title = ".sec-title h2 { font-family: var(--font-magic); font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem; background: var(--gradient-heading); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }"
new_sec_title = ".sec-title h2 { font-family: var(--font-magic); font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem; color: #180D20; }"
content = content.replace(old_sec_title, new_sec_title)

# Highlight texts
content = content.replace('<h2>Featured Stars</h2>', '<h2><span style="color: var(--color-primary);">Featured</span> <span style="color: #3895c8;">Stars</span></h2>')
content = content.replace('<h2>Find Your Perfect Entertainer</h2>', '<h2 style="color: var(--color-primary);">Find Your Perfect Entertainer</h2>')
content = content.replace('<h2>Choose Your Performance Style</h2>', '<h2><span style="color: #3895c8;">Choose Your</span> <span style="color: var(--color-primary);">Performance Style</span></h2>')
content = content.replace('<h2>Loved by Little Guests</h2>', '<h2 style="color: #3895c8;">Loved by Little Guests</h2>')
content = content.replace('<h2>The Magiqo Standard</h2>', '<h2><span style="color: var(--color-primary);">The Magiqo</span> <span style="color: #3895c8;">Standard</span></h2>')
content = content.replace('<h2>Questions About Our Talent</h2>', '<h2 style="color: #3895c8;">Questions About Our Talent</h2>')

# 2. Mark -> Elias
content = content.replace('Mark "The Magic"', 'Elias "The Magic"')
content = content.replace('alt="Mark The Magic"', 'alt="Elias The Magic"')
content = content.replace('data-name="Mark"', 'data-name="Elias"')
content = content.replace('alt="Mark"', 'alt="Elias"')
content = content.replace('<h4>Mark</h4>', '<h4>Elias</h4>')
content = content.replace('Mark (Magician)', 'Elias (Magician)')
content = content.replace('Mark was absolutely incredible', 'Elias was absolutely incredible')
content = content.replace('with Mark or', 'with Elias or')

# 3. Loved by little guests (kids image)
content = content.replace('assets/images/hero_baby_magician.jpg', 'assets/images/gallery_smile_1.jpg')

# 4. Magiqo Standards UI update (more spaces, animations)
standards_css_old = """    .standard-card { background: white; border-radius: var(--radius-lg); padding: 3rem 2rem; text-align: center; border: 1px solid var(--color-border); box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.4s; }
    .standard-card:hover { transform: translateY(-10px); border-color: #2e19a7; box-shadow: 0 20px 40px rgba(46, 25, 167, 0.1); }
    .standard-card svg { width: 70px; height: 70px; fill: #ff9800; margin-bottom: 1.5rem; padding: 15px; background: rgba(255,152,0,0.1); border-radius: 50%; }"""
standards_css_new = """    .standard-card { background: white; border-radius: var(--radius-xl); padding: 4rem 2.5rem; text-align: center; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 15px 40px rgba(0,0,0,0.04); transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); position: relative; overflow: hidden; }
    .standard-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, var(--color-primary), #3895c8); transform: scaleX(0); transition: transform 0.5s; transform-origin: left; }
    .standard-card:hover { transform: translateY(-15px) scale(1.02); box-shadow: 0 30px 60px rgba(56, 149, 200, 0.15); border-color: transparent; }
    .standard-card:hover::before { transform: scaleX(1); }
    .standard-card svg { width: 80px; height: 80px; fill: #3895c8; margin-bottom: 2rem; padding: 15px; background: rgba(56, 149, 200, 0.1); border-radius: 50%; transition: transform 0.5s, background 0.5s; }
    .standard-card:hover svg { transform: rotateY(180deg) scale(1.1); background: rgba(218, 47, 95, 0.1); fill: var(--color-primary); }"""
content = content.replace(standards_css_old, standards_css_new)


# 5. Book your star - UI colors
book_css_old = """    .book-info { flex: 1; padding: 4rem; background: linear-gradient(135deg, #ff9800, #2e19a7); color: white; display: flex; flex-direction: column; justify-content: center; }"""
book_css_new = """    .book-info { flex: 1; padding: 4rem; background: #3895c8; color: white; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden; }
    .book-info::after { content: ''; position: absolute; top: -50%; right: -50%; width: 100%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%); pointer-events: none; }"""
content = content.replace(book_css_old, book_css_new)

# 6. Have a talent for magic - Redesign & colors
join_css_old = """    .join-banner { background: linear-gradient(135deg, #ff9800, #2e19a7); border-radius: var(--radius-lg); padding: 4rem; color: white; display: flex; align-items: center; justify-content: space-between; gap: 2rem; box-shadow: 0 15px 35px rgba(46, 25, 167, 0.2); }"""
join_css_new = """    .join-banner { background: white; border: 2px dashed #3895c8; border-radius: var(--radius-xl); padding: 5rem 4rem; color: var(--color-text); display: flex; align-items: center; justify-content: space-between; gap: 3rem; box-shadow: 0 20px 50px rgba(0,0,0,0.05); position: relative; overflow: hidden; }
    .join-banner::before { content: '✨'; position: absolute; top: 20px; left: 20px; font-size: 2rem; opacity: 0.5; }
    .join-banner::after { content: '🎩'; position: absolute; bottom: 20px; right: 20px; font-size: 3rem; opacity: 0.2; transform: rotate(15deg); }
    .join-text h2 { color: var(--color-primary) !important; -webkit-text-fill-color: var(--color-primary) !important; font-size: 3rem; }
    .join-text p { color: var(--color-text-light); font-size: 1.2rem; }"""
content = content.replace(join_css_old, join_css_new)

old_btn = 'style="background: white; color: #2e19a7; padding: 1rem 2.5rem; font-size: 1.1rem; white-space: nowrap; font-weight: bold;"'
new_btn = 'style="background: var(--color-primary); color: white; padding: 1.25rem 3rem; font-size: 1.125rem; white-space: nowrap; font-weight: bold; border-radius: var(--radius-pill); box-shadow: 0 10px 20px rgba(218,47,95,0.2); transition: transform 0.3s;" onmouseover="this.style.transform=\'scale(1.05)\'" onmouseout="this.style.transform=\'scale(1)\'"'
content = content.replace(old_btn, new_btn)


# 7. Choose your performance style - Redesign
style_html_old = """      <div class="style-grid">
        <div class="style-box">
          <svg viewBox="0 0 24 24"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>
          <h3>High Energy</h3>
        </div>
        <div class="style-box">
          <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm3-13.5V9h-4v2h4v2.5l3.5-3.5L15 6.5z"/></svg>
          <h3>Comedy & Laughs</h3>
        </div>
        <div class="style-box">
          <svg viewBox="0 0 24 24"><path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9 9-4.03 9-9-4.03-9-9-9zm0 16c-3.86 0-7-3.14-7-7s3.14-7 7-7 7 3.14 7 7-3.14 7-7 7zm1-11h-2v3H8v2h3v3h2v-3h3v-2h-3V8z"/></svg>
          <h3>Magic & Wonder</h3>
        </div>
        <div class="style-box">
          <svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
          <h3>Storytelling</h3>
        </div>
      </div>"""

style_html_new = """      <div class="interactive-finder" style="background: white; padding: 4rem; border-radius: var(--radius-xl); box-shadow: 0 20px 50px rgba(0,0,0,0.05); max-width: 900px; margin: 0 auto; text-align: center;">
        <h3 style="color: #3895c8; font-size: 2rem; margin-bottom: 2rem; font-family: var(--font-heading);">What kind of magic does your party need?</h3>
        <p style="color: var(--color-text-light); margin-bottom: 3rem; font-size: 1.1rem;">Select a vibe below and we'll suggest the perfect entertainer type for your child.</p>
        
        <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; justify-content: center; margin-bottom: 3rem;">
           <button class="btn style-btn" onclick="suggestTalent('energy')">High Energy</button>
           <button class="btn style-btn" onclick="suggestTalent('comedy')">Comedy & Laughs</button>
           <button class="btn style-btn" onclick="suggestTalent('magic')">Magic & Wonder</button>
           <button class="btn style-btn" onclick="suggestTalent('story')">Storytelling</button>
        </div>
        
        <div id="talentSuggestion" style="display: none; padding: 2.5rem; background: var(--color-bg); border-radius: var(--radius-lg); border: 2px dashed #3895c8; animation: fadeIn 0.5s ease-out;">
           <h4 id="sugTitle" style="color: var(--color-primary); font-size: 1.5rem; margin-bottom: 1rem; font-family: var(--font-magic);">We Suggest...</h4>
           <p id="sugDesc" style="font-size: 1.1rem; color: var(--color-text-light); margin-bottom: 1.5rem;"></p>
           <a href="#roster" class="btn btn-primary" style="background: #3895c8; box-shadow: none;" onclick="document.getElementById('makerSearch').value=''; document.querySelectorAll('.style-pill').forEach(p=>p.classList.remove('active')); document.querySelector('.style-pill[data-filter=\\'all\\']').classList.add('active'); document.querySelector('#makerSearch').dispatchEvent(new Event('input'));">Find Them Now</a>
        </div>
      </div>
      
      <style>
        .style-btn { background: transparent; border: 2px solid #e0e0e0; color: var(--color-text); padding: 1rem 2rem; border-radius: var(--radius-pill); font-size: 1.1rem; font-weight: bold; transition: all 0.3s; }
        .style-btn:hover, .style-btn.active { border-color: var(--color-primary); color: white; background: var(--color-primary); transform: translateY(-3px); box-shadow: 0 10px 20px rgba(218, 47, 95, 0.2); }
      </style>
      <script>
        function suggestTalent(type) {
            document.querySelectorAll('.style-btn').forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');
            
            const box = document.getElementById('talentSuggestion');
            const title = document.getElementById('sugTitle');
            const desc = document.getElementById('sugDesc');
            
            box.style.display = 'block';
            if(type === 'energy') {
                title.innerText = 'Superheroes & Mascot Actors!';
                desc.innerText = 'Perfect for active kids who love games, running around, and action-packed training courses.';
            } else if (type === 'comedy') {
                title.innerText = 'Classic Clowns & Jugglers!';
                desc.innerText = 'Ideal for endless giggles, silly antics, slapstick comedy, and awesome balloon animals.';
            } else if (type === 'magic') {
                title.innerText = 'Master Magicians & Illusionists!';
                desc.innerText = 'The classic choice to leave everyone wide-eyed with incredible tricks and mind-bending stage magic.';
            } else if (type === 'story') {
                title.innerText = 'Fairytale Princesses & Puppeteers!';
                desc.innerText = 'A magical, calming experience featuring sing-alongs, royal coronations, and beautiful tales.';
            }
        }
      </script>"""

content = content.replace(style_html_old, style_html_new)


with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
