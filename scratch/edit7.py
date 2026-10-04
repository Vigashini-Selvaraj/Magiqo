import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Have a Talent for Magic? color change to #9c3e79
content = content.replace('background: var(--color-secondary);', 'background: #9c3e79;')


# 2. Fix review images (Sarah, James, Emily)
review_section = re.search(r'<div class="review-grid">.*?</div>\s*</div>\s*</section>', content, re.DOTALL).group(0)

# The current HTML has emily_girl_smile in 1st, gallery_smile_1 in 2nd and 3rd.
# Let's completely rebuild the review grid inner HTML to be clean and correct.
new_review_grid = """<div class="review-grid">
        <div class="review-card" style="padding-top: 1rem;">
          <img src="assets/images/gallery_smile_1.jpg" alt="Sarah" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">
          <div class="review-content">
            <div class="stars" style="font-weight: bold; color: #ff9800;">Rating: 5/5</div>
            <p class="review-text">"Elias was absolutely incredible! He held the attention of 25 seven-year-olds for an entire hour. The parents were just as amazed by the magic."</p>
            <p class="reviewer">- Sarah M.</p>
          </div>
        </div>
        <div class="review-card" style="padding-top: 1rem;">
          <img src="assets/images/james_boy_smile.jpg" alt="James" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">
          <div class="review-content">
            <div class="stars" style="font-weight: bold; color: #ff9800;">Rating: 5/5</div>
            <p class="review-text">"Princess Lily made my daughter's dream come true. Her voice is beautiful and she was so patient and sweet with every single child."</p>
            <p class="reviewer">- James T.</p>
          </div>
        </div>
        <div class="review-card" style="padding-top: 1rem;">
          <img src="assets/images/emily_girl_smile.jpg" alt="Emily" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">
          <div class="review-content">
            <div class="stars" style="font-weight: bold; color: #ff9800;">Rating: 5/5</div>
            <p class="review-text">"Barnaby the Clown brought non-stop laughs. The physical comedy was perfect, and the balloon animals at the end were a huge hit!"</p>
            <p class="reviewer">- Emily R.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""
content = content.replace(review_section, new_review_grid)


# 3. Add attractive background/shapes to Quiz Box
quiz_box = '<div class="interactive-finder" style="background: linear-gradient(to bottom right, #ffffff, #f0f8ff); padding: 4rem; border-radius: var(--radius-xl); box-shadow: 0 20px 50px rgba(0,0,0,0.05); max-width: 900px; margin: 0 auto; text-align: center;">'
new_quiz_box = '<div class="interactive-finder" style="background: radial-gradient(circle at top left, #fff0f5 0%, transparent 40%), radial-gradient(circle at bottom right, #e0f7fa 0%, transparent 40%), linear-gradient(to bottom right, #ffffff, #f9f9f9); border: 2px dashed #a9e0ff; position: relative; padding: 4rem; border-radius: var(--radius-xl); box-shadow: 0 20px 50px rgba(0,0,0,0.05); max-width: 900px; margin: 0 auto; text-align: center; overflow: hidden;">'
content = content.replace(quiz_box, new_quiz_box)
# If it had the old string:
quiz_box2 = '<div class="interactive-finder" style="background: linear-gradient(to bottom right, #ffffff, #f0f8ff);'
new_quiz_box2 = '<div class="interactive-finder" style="background: radial-gradient(circle at top left, #fff0f5 0%, transparent 40%), radial-gradient(circle at bottom right, #e0f7fa 0%, transparent 40%), linear-gradient(to bottom right, #ffffff, #f9f9f9); border: 2px dashed #a9e0ff; position: relative;'
content = content.replace(quiz_box2, new_quiz_box2)

# 4. Magiqo Standards: Flip cards back (remove gradient, add image)
css_back = '.flip-card-back { background: linear-gradient(135deg, var(--color-primary), #3895c8); color: white; transform: rotateY(180deg); }'
css_back_new = '.flip-card-back { background: white; color: var(--color-text); transform: rotateY(180deg); }'
content = content.replace(css_back, css_back_new)

# Card 1 Back
old_c1 = """<div class="flip-card-back">
              <p>Every single entertainer undergoes a comprehensive nationwide background check and reference verification.</p>
            </div>"""
new_c1 = """<div class="flip-card-back">
              <img src="assets/images/magiqo_background_check.jpg" alt="Background Checked" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #3895c8;">
              <p style="color: var(--color-text);">Every single entertainer undergoes a comprehensive nationwide background check and reference verification.</p>
            </div>"""
content = content.replace(old_c1, new_c1)

# Card 2 Back
old_c2 = """<div class="flip-card-back">
              <p>Our talent attends rigorous Magiqo Workshops to master crowd control and the art of highly-engaging performance.</p>
            </div>"""
new_c2 = """<div class="flip-card-back">
              <img src="assets/images/magiqo_trained.jpg" alt="Professionally Trained" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #3895c8;">
              <p style="color: var(--color-text);">Our talent attends rigorous Magiqo Workshops to master crowd control and the art of highly-engaging performance.</p>
            </div>"""
content = content.replace(old_c2, new_c2)

# Card 3 Back
old_c3 = """<div class="flip-card-back">
              <p>We are fully licensed and hold robust liability insurance, giving parents complete peace of mind.</p>
            </div>"""
new_c3 = """<div class="flip-card-back">
              <img src="assets/images/magiqo_insured.jpg" alt="Fully Insured" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #3895c8;">
              <p style="color: var(--color-text);">We are fully licensed and hold robust liability insurance, giving parents complete peace of mind.</p>
            </div>"""
content = content.replace(old_c3, new_c3)

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
