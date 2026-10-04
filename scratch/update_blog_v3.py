import re

filepath_blog = r'c:\Users\vigas\Desktop\magiqo\blog.html'
with open(filepath_blog, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Append 21st article to grid
new_article = '''        <div class="blog-card" data-category="Themes" data-title="the ultimate pirate adventure">
          <img src="assets/images/superhero_party_1790842695325.jpg" alt="The Ultimate Pirate Adventure" class="blog-img" onclick="location.href='blog_detail.html'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Themes</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html'">The Ultimate Pirate Adventure</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Jul 10, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 5 min</span>
            </div>
            <a href="blog_detail.html" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
      </div>'''
content = content.replace('      </div>\n    </section>\n\n    <!-- 6. PARTY INSPIRATION GALLERY -->', new_article + '\n    </section>\n\n    <!-- 6. PARTY INSPIRATION GALLERY -->')

# 2. Trending Reads images
trending_1 = '''        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">
          <img src="assets/images/james_boy_smile.jpg" alt="Adults Entertained" class="blog-img" onclick="location.href='blog_detail.html'" style="cursor:pointer; border-radius: 20px 20px 0 0;">
          <div class="blog-content">'''
content = content.replace('''        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">\n          <div class="blog-content">''', trending_1, 1)

trending_2 = '''        <div class="blog-card" style="background: rgba(56, 149, 200, 0.05); border: 1px solid rgba(56, 149, 200, 0.2);">
          <img src="assets/images/magic_show_party_1790842468826.jpg" alt="Winter Wonderland" class="blog-img" onclick="location.href='blog_detail.html'" style="cursor:pointer; border-radius: 20px 20px 0 0;">
          <div class="blog-content">'''
content = content.replace('''        <div class="blog-card" style="background: rgba(56, 149, 200, 0.05); border: 1px solid rgba(56, 149, 200, 0.2);">\n          <div class="blog-content">''', trending_2, 1)

trending_3 = '''        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">
          <img src="assets/images/about_kids_birthday.jpg" alt="Eco-Friendly Party" class="blog-img" onclick="location.href='blog_detail.html'" style="cursor:pointer; border-radius: 20px 20px 0 0;">
          <div class="blog-content">'''
content = content.replace('''        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">\n          <div class="blog-content">''', trending_3)

# 3. Testimonials Avatars instead of stars
avatar_1 = '''<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
            <img src="assets/images/james_boy_smile.jpg" alt="Sarah Jenkins" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;">
          </div>'''
content = content.replace('''<div style="display: flex; gap: 5px; color: #f5a623; margin-bottom: 15px; font-size: 1.2rem;">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>''', avatar_1, 1)

avatar_2 = '''<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
            <img src="assets/images/cute_kids_clapping_1790833571210.jpg" alt="Mark T." style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;">
          </div>'''
content = content.replace('''<div style="display: flex; gap: 5px; color: #f5a623; margin-bottom: 15px; font-size: 1.2rem;">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>''', avatar_2, 1)

# 4. FAQ Plus/Minus
faq_css_old = r"""        summary::after {
          content: '\x0c078'; /* fa-chevron-down */
          font-family: 'Font Awesome 6 Free';
          font-weight: 900;
          color: var(--color-primary);
          transition: transform 0.3s;
        }
        details[open] summary::after {
          transform: rotate(180deg);
        }"""
faq_css_new = r"""        summary::after {
          content: '+';
          font-family: inherit;
          font-size: 1.8rem;
          font-weight: 900;
          color: var(--color-primary);
        }
        details[open] summary::after {
          content: '-';
          transform: none;
        }"""
# In case Python string escape messed it up before, use a generic regex replacement
content = re.sub(r'summary::after\s*\{.*?\n\s*\}', r"""summary::after {
          content: '+';
          font-family: inherit;
          font-size: 1.8rem;
          font-weight: 900;
          color: var(--color-primary);
        }""", content, flags=re.DOTALL)
content = re.sub(r'details\[open\] summary::after\s*\{.*?\n\s*\}', r"""details[open] summary::after {
          content: '-';
          transform: none;
        }""", content, flags=re.DOTALL)

# 5. Send Message function
script_injection = '''
    function sendMessage() {
      const form = document.querySelector('.query-section form');
      form.innerHTML = '<div style="text-align: center; color: #10b981;"><i class="fa-solid fa-circle-check" style="font-size: 3rem; margin-bottom: 15px;"></i><h3>Message Sent!</h3><p>We will get back to you shortly.</p></div>';
    }
'''
if 'function sendMessage()' not in content:
    content = content.replace('function applyFilters()', script_injection + '\n    function applyFilters()')

# Also add button click listener to the query box
content = content.replace('<button type="submit" class="btn btn-primary" style="padding: 15px; border-radius: 12px; font-size: 1.1rem; border: none; cursor: pointer;">Send Message <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i></button>', '<button type="button" class="btn btn-primary" onclick="sendMessage()" style="padding: 15px; border-radius: 12px; font-size: 1.1rem; border: none; cursor: pointer;">Send Message <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i></button>')

# 6 & 7. Remove Newsletter and replace CTA
newsletter_cta_regex = r'<!-- 10\. NEWSLETTER -->.*?</section>\s*<!-- 12\. FINAL CTA -->.*?</section>'
new_cta = '''<!-- 12. FINAL CTA -->
    <section class="cta-final reveal" style="background: var(--color-primary); padding: 100px 20px; text-align: center;">
      <div class="section-container" style="margin-bottom: 0;">
        <h2 style="font-family: var(--font-magic); font-size: 4rem; margin-bottom: 20px; font-weight: 900; line-height: 1.1; text-transform: uppercase; letter-spacing: 2px; color: white;">Ready to Make <br>Magic Happen?</h2>
        <p style="font-size: 1.3rem; margin-bottom: 40px; font-weight: 500; max-width: 600px; margin-left: auto; margin-right: auto; color: white; opacity: 0.9;">Stop dreaming about the perfect party and let us bring it to life. Book your magical celebration today.</p>
        <a href="contact.html" class="btn" style="background: white; color: var(--color-primary); padding: 20px 50px; font-size: 1.5rem; font-weight: 900; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: transform 0.3s; display: inline-block;">Contact Us <i class="fa-solid fa-bolt" style="margin-left: 10px;"></i></a>
      </div>
    </section>'''

content = re.sub(newsletter_cta_regex, new_cta, content, flags=re.DOTALL)

with open(filepath_blog, 'w', encoding='utf-8') as f:
    f.write(content)
