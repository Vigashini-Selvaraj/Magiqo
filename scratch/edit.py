import re
import os

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero CSS redesign
hero_css_old = """    /* 1. Entertainers Hero */
    .ent-hero {
      position: relative; min-height: 80vh; display: flex; align-items: center; justify-content: center;
      text-align: center; background: url('assets/images/service_hero.jpg') center/cover no-repeat;
      padding-top: 120px; padding-bottom: 80px;
    }
    .ent-hero::before { content: ''; position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(24,13,32,0.6), rgba(24,13,32,0.9)); }
    .ent-hero-content { position: relative; z-index: 2; color: white; max-width: 800px; padding: 0 20px; }
    .ent-hero h1 { font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 6rem); margin-bottom: 1.5rem; text-shadow: 0 4px 20px rgba(0,0,0,0.5); color: white !important; -webkit-text-fill-color: white !important; background: none !important; }
    .ent-hero p { font-size: 1.5rem; font-weight: 300; margin-bottom: 2.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5); }"""

hero_css_new = """    /* 1. Entertainers Hero (Redesigned) */
    .ent-hero {
      position: relative; min-height: 80vh; display: flex; align-items: center; justify-content: center;
      text-align: center; background: linear-gradient(135deg, var(--color-bg) 0%, #ffe4ec 100%);
      padding-top: 120px; padding-bottom: 80px; overflow: hidden;
    }
    .ent-hero::before { content: ''; position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(46, 25, 167, 0.05) 0%, transparent 70%); animation: pulse-glow 4s infinite alternate; }
    .ent-hero-content { position: relative; z-index: 2; color: var(--color-text); max-width: 800px; padding: 0 20px; }
    .ent-hero h1 { font-family: var(--font-magic); font-size: clamp(3.5rem, 6vw, 6rem); margin-bottom: 1.5rem; color: var(--color-text) !important; -webkit-text-fill-color: var(--color-text) !important; background: none !important; animation: fadeIn 1s ease-out; }
    .ent-hero p { font-size: 1.5rem; font-weight: 300; margin-bottom: 2.5rem; color: var(--color-text-light); animation: fadeIn 1.2s ease-out; }
    .ent-hero .btn { transition: transform 0.3s, box-shadow 0.3s; }
    .ent-hero .btn:hover { transform: translateY(-5px) scale(1.05); box-shadow: 0 10px 25px rgba(218, 47, 95, 0.4); }"""
content = content.replace(hero_css_old, hero_css_new)

# 2. Hero HTML redesign
hero_html_old = """  <!-- 1. Hero -->
  <section class="ent-hero">
    <div class="container ent-hero-content">
      <h1>Meet Our Entertainers</h1>
      <p>The highly-trained, passionate performers who bring the magic to your child's most important days.</p>
      <a href="#roster" class="btn btn-primary" style="padding: 1.25rem 3rem; font-size: 1.125rem;">Explore The Talent</a>
    </div>
  </section>"""
hero_html_new = """  <!-- 1. Hero -->
  <section class="ent-hero">
    <div class="sparkle" style="top: 20%; left: 10%;"></div>
    <div class="sparkle" style="top: 70%; left: 80%; animation-delay: 1s;"></div>
    <div class="sparkle" style="top: 40%; right: 15%; animation-delay: 0.5s;"></div>
    <div class="container ent-hero-content floating">
      <h1>Meet Our Entertainers</h1>
      <p>The highly-trained, passionate performers who bring the magic to your child's most important days.</p>
      <a href="#roster" class="btn btn-primary" style="padding: 1.25rem 3rem; font-size: 1.125rem;">Explore The Talent</a>
    </div>
  </section>"""
content = content.replace(hero_html_old, hero_html_new)


# 3. Find Your Perfect Entertainer - Grid to 4 cols, add button
content = content.replace('.makers-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 2rem; }',
                          '.makers-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; } \n    @media(max-width: 992px) { .makers-grid { grid-template-columns: repeat(2, 1fr); } } \n    @media(max-width: 576px) { .makers-grid { grid-template-columns: 1fr; } }')

# Replace emojis and add button in maker-card
import re
def repl_maker_card(m):
    # m.group(0) is the full card HTML
    html = m.group(0)
    # replace emojis
    html = re.sub(r'★★★★★ \(([\d.]+)\)', r'Rating: \1/5', html)
    html = re.sub(r'★★★★☆ \(([\d.]+)\)', r'Rating: \1/5', html)
    # insert view details link
    html = html.replace('</div>\n        </div>', '</div>\n          <a href="entertainer_detail.html" class="btn btn-outline" style="margin: 1rem; width: calc(100% - 2rem);">View Details</a>\n        </div>')
    return html

content = re.sub(r'<div class="maker-card"[\s\S]+?</div>\n        </div>', repl_maker_card, content)

# 4. Choose Your Performance Style
style_css_old = """    /* 6. Performance Styles */
    .style-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; }
    .style-box { background: var(--color-bg); padding: 2rem; border-radius: var(--radius-lg); text-align: center; border: 1px solid var(--color-border); transition: all 0.3s; cursor: pointer; }
    .style-box:hover { background: var(--color-primary); color: white; border-color: var(--color-primary); transform: translateY(-5px); }
    .style-box h3 { font-size: 1.25rem; margin-top: 1rem; transition: color 0.3s; }
    .style-box svg { width: 40px; height: 40px; fill: var(--color-accent); transition: fill 0.3s; }
    .style-box:hover svg { fill: white; }"""

style_css_new = """    /* 6. Performance Styles */
    .style-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; }
    .style-box { background: linear-gradient(135deg, #ffffff, var(--color-bg)); padding: 2rem; border-radius: var(--radius-lg); text-align: center; border: 2px solid transparent; transition: all 0.3s; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .style-box:hover { background: linear-gradient(135deg, #ff9800, #2e19a7); color: white; transform: translateY(-8px) scale(1.02); box-shadow: 0 15px 30px rgba(46, 25, 167, 0.2); }
    .style-box h3 { font-size: 1.25rem; margin-top: 1rem; transition: color 0.3s; }
    .style-box svg { width: 50px; height: 50px; fill: #2e19a7; transition: fill 0.3s; }
    .style-box:hover svg { fill: white; }"""
content = content.replace(style_css_old, style_css_new)


# 5. Loved by Little Guests
# Replace emojis
content = content.replace('<div class="stars">★★★★★</div>', '<div class="stars" style="font-weight: bold; color: #ff9800;">Rating: 5/5</div>')

# Add baby image to review grid
review_html_old = """      <div class="review-grid">
        <div class="review-card">"""
review_html_new = """      <div class="review-grid">
        <div class="review-card" style="padding-top: 1rem;">
          <img src="assets/images/hero_baby_magician.jpg" alt="Happy Kid" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">
"""
content = content.replace(review_html_old, review_html_new)


# 6. Magiqo Standards
standards_css_old = """    /* 9. The Magiqo Standard (Safety) */
    .standards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; }
    .standard-card { text-align: center; padding: 2rem; }
    .standard-card svg { width: 60px; height: 60px; fill: var(--color-primary); margin-bottom: 1.5rem; }
    .standard-card h3 { font-family: var(--font-heading); font-size: 1.5rem; margin-bottom: 1rem; color: var(--color-text); }
    .standard-card p { color: var(--color-text-light); line-height: 1.6; }"""
standards_css_new = """    /* 9. The Magiqo Standard (Safety) */
    .standards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
    .standard-card { background: white; border-radius: var(--radius-lg); padding: 3rem 2rem; text-align: center; border: 1px solid var(--color-border); box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.4s; }
    .standard-card:hover { transform: translateY(-10px); border-color: #2e19a7; box-shadow: 0 20px 40px rgba(46, 25, 167, 0.1); }
    .standard-card svg { width: 70px; height: 70px; fill: #ff9800; margin-bottom: 1.5rem; padding: 15px; background: rgba(255,152,0,0.1); border-radius: 50%; }
    .standard-card h3 { font-family: var(--font-magic); font-size: 1.75rem; margin-bottom: 1rem; color: #2e19a7; }
    .standard-card p { color: var(--color-text-light); line-height: 1.7; font-size: 1.05rem; }"""
content = content.replace(standards_css_old, standards_css_new)


# 8. Booking Section / Check availability
book_css_old = """    /* 11. Booking Form Split */
    .book-split { display: flex; gap: 4rem; background: var(--color-surface); border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--color-border); }
    .book-info { flex: 1; padding: 4rem; background: var(--color-primary); color: white; display: flex; flex-direction: column; justify-content: center; }
    .book-info h2 { font-family: var(--font-magic); font-size: 3rem; margin-bottom: 1rem; color: white !important; -webkit-text-fill-color: white !important; background: none !important; }"""
book_css_new = """    /* 11. Booking Form Split */
    .book-split { display: flex; gap: 4rem; background: var(--color-surface); border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--color-border); box-shadow: 0 20px 50px rgba(0,0,0,0.05); }
    .book-info { flex: 1; padding: 4rem; background: linear-gradient(135deg, #ff9800, #2e19a7); color: white; display: flex; flex-direction: column; justify-content: center; }
    .book-info h2 { font-family: var(--font-magic); font-size: 3rem; margin-bottom: 1rem; color: white !important; -webkit-text-fill-color: white !important; background: none !important; }
    .modal-availability { position: fixed; inset: 0; background: rgba(0,0,0,0.6); display: none; align-items: center; justify-content: center; z-index: 9999; }
    .modal-availability.active { display: flex; }
    .modal-avail-content { background: white; padding: 3rem; border-radius: var(--radius-lg); text-align: center; max-width: 400px; }
    .modal-avail-content h3 { font-family: var(--font-magic); color: #2e19a7; font-size: 2rem; }"""
content = content.replace(book_css_old, book_css_new)

book_html_old = """          <button class="btn btn-primary" style="width: 100%; padding: 1rem; font-size: 1.1rem; margin-top: 1rem;">Check Availability</button>"""
book_html_new = """          <button class="btn btn-primary" style="width: 100%; padding: 1rem; font-size: 1.1rem; margin-top: 1rem; background-color: #2e19a7;" onclick="document.getElementById('availModal').classList.add('active')">Check Availability</button>
        </div>
      </div>
    </div>
  </section>
  
  <div class="modal-availability" id="availModal" onclick="if(event.target===this) this.classList.remove('active')">
    <div class="modal-avail-content">
      <h3>Good News!</h3>
      <p style="font-size: 1.1rem; margin: 1rem 0 2rem;">The selected entertainer is available for your schedule.</p>
      <a href="availability.html" class="btn btn-primary" style="background-color: #ff9800;">Proceed to Availability Page</a>
    </div>
  </div>"""
content = content.replace(book_html_old + '\n        </div>\n      </div>\n    </div>\n  </section>', book_html_new)

# 9. Join The Team Banner
join_css_old = """    /* 12. Join The Team Banner */
    .join-banner { background: linear-gradient(135deg, var(--color-primary), var(--color-accent)); border-radius: var(--radius-lg); padding: 4rem; color: white; display: flex; align-items: center; justify-content: space-between; gap: 2rem; }"""
join_css_new = """    /* 12. Join The Team Banner */
    .join-banner { background: linear-gradient(135deg, #ff9800, #2e19a7); border-radius: var(--radius-lg); padding: 4rem; color: white; display: flex; align-items: center; justify-content: space-between; gap: 2rem; box-shadow: 0 15px 35px rgba(46, 25, 167, 0.2); }"""
content = content.replace(join_css_old, join_css_new)

join_html_old = """<a href="#" class="btn btn-animated" style="background: white; color: var(--color-primary); padding: 1rem 2.5rem; font-size: 1.1rem; white-space: nowrap;">Apply to Join</a>"""
join_html_new = """<a href="join.html" class="btn btn-animated" style="background: white; color: #2e19a7; padding: 1rem 2.5rem; font-size: 1.1rem; white-space: nowrap; font-weight: bold;">Apply to Join</a>"""
content = content.replace(join_html_old, join_html_new)


# 10. Final CTA
cta_css_old = """    /* 13. Final CTA */
    .cta-section { background: #da2f5f; padding: 6rem 0; text-align: center; color: white; }"""
cta_css_new = """    /* 13. Final CTA */
    .cta-section { background: #2e19a7; padding: 6rem 0; text-align: center; color: white; }"""
content = content.replace(cta_css_old, cta_css_new)

cta_html_old = """<a href="contact.html" class="btn btn-animated" style="background: white; color: #da2f5f; padding: 1.25rem 4rem; font-size: 1.25rem; font-weight: bold; border-radius: var(--radius-pill); text-decoration: none; display: inline-block;">Start Booking Now</a>"""
cta_html_new = """<a href="contact.html" class="btn btn-animated" style="background: white; color: #2e19a7; padding: 1.25rem 4rem; font-size: 1.25rem; font-weight: bold; border-radius: var(--radius-pill); text-decoration: none; display: inline-block;">Start Booking Now</a>"""
content = content.replace(cta_html_old, cta_html_new)

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
