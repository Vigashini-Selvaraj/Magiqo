import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove gradient from .sec-title h2
# The current CSS for .sec-title h2 in entertainers.html might still have the gradient if previous replace failed.
content = re.sub(
    r'\.sec-title h2\s*\{[^}]*\}',
    r'.sec-title h2 { font-family: var(--font-magic); font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem; color: var(--color-text); }',
    content
)

# Fix "Featured Stars" colors specifically
content = content.replace(
    '<h2><span style="color: var(--color-primary);">Featured</span> <span style="color: #3895c8;">Stars</span></h2>',
    '<h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Featured</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Stars</span></h2>'
)
# If it's still <h2>Featured Stars</h2>
content = content.replace(
    '<h2>Featured Stars</h2>',
    '<h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Featured</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Stars</span></h2>'
)

# 2. Add kid images to the 2nd and 3rd review cards
review1 = '<div class="review-card" style="padding-top: 1rem;">'
review_other = '<div class="review-card">'
kid_img_html = '<img src="assets/images/gallery_smile_1.jpg" alt="Happy Kid" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; border: 3px solid #ff9800;">'

# Replace review cards to ensure they all have the image
content = re.sub(
    r'<div class="review-card">(\s*)<div class="review-content">',
    r'<div class="review-card" style="padding-top: 1rem;">\1' + kid_img_html + r'\n\1<div class="review-content">',
    content
)

# 3. Choose your performance style: 5 Questions Quiz
quiz_html = """      <div class="interactive-finder" style="background: white; padding: 4rem; border-radius: var(--radius-xl); box-shadow: 0 20px 50px rgba(0,0,0,0.05); max-width: 900px; margin: 0 auto; text-align: center;">
        <h3 id="quizTitle" style="color: #3895c8; font-size: 2rem; margin-bottom: 1.5rem; font-family: var(--font-heading);">Let's find the perfect match!</h3>
        <p id="quizDesc" style="color: var(--color-text-light); margin-bottom: 2.5rem; font-size: 1.1rem;">Answer 5 quick questions.</p>
        
        <div id="quizContainer" style="margin-bottom: 3rem;">
           <h4 id="questionText" style="font-size: 1.5rem; margin-bottom: 2rem; color: var(--color-text);">1. What is the age of the birthday child?</h4>
           <div id="answersContainer" style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;">
              <button class="btn style-btn" onclick="nextQuestion(1)">1-4 years</button>
              <button class="btn style-btn" onclick="nextQuestion(2)">5-7 years</button>
              <button class="btn style-btn" onclick="nextQuestion(3)">8-10 years</button>
              <button class="btn style-btn" onclick="nextQuestion(4)">11+ years</button>
           </div>
        </div>
        
        <div id="talentSuggestion" style="display: none; padding: 3rem; background: var(--color-bg); border-radius: var(--radius-lg); border: 2px solid var(--color-primary); animation: fadeIn 0.5s ease-out;">
           <h4 id="sugTitle" style="color: #3895c8; font-size: 2rem; margin-bottom: 1rem; font-family: var(--font-magic);">We Suggest...</h4>
           <p id="sugDesc" style="font-size: 1.2rem; color: var(--color-text-light); margin-bottom: 2rem;"></p>
           <a href="entertainer_detail.html" class="btn btn-primary" style="background: var(--color-primary); font-size: 1.2rem; padding: 1rem 3rem;">View Entertainer Details</a>
        </div>
      </div>
      
      <style>
        .style-btn { background: transparent; border: 2px solid #e0e0e0; color: var(--color-text); padding: 1rem 2rem; border-radius: var(--radius-pill); font-size: 1.1rem; font-weight: bold; transition: all 0.3s; cursor: pointer; }
        .style-btn:hover { border-color: var(--color-primary); color: white; background: var(--color-primary); transform: translateY(-3px); box-shadow: 0 10px 20px rgba(218, 47, 95, 0.2); }
      </style>
      <script>
        const questions = [
            { q: "1. What is the age of the birthday child?", a: ["1-4 years", "5-7 years", "8-10 years", "11+ years"] },
            { q: "2. How active is your group?", a: ["Very Active", "Moderate", "Quiet & Focused", "Mixed"] },
            { q: "3. What's the party setting?", a: ["Indoor (House)", "Indoor (Hall)", "Outdoor (Park)", "Backyard"] },
            { q: "4. Group size?", a: ["Under 10 kids", "10-20 kids", "20-30 kids", "Huge Party!"] },
            { q: "5. What vibe are you going for?", a: ["Laughs & Silliness", "Magic & Mystery", "Action & Games", "Story & Music"] }
        ];
        let currentQ = 0;
        
        function nextQuestion(ans) {
            currentQ++;
            if(currentQ < questions.length) {
                document.getElementById('questionText').innerText = questions[currentQ].q;
                let html = '';
                questions[currentQ].a.forEach((ans, i) => {
                    html += '<button class="btn style-btn" onclick="nextQuestion(' + i + ')">' + ans + '</button>';
                });
                document.getElementById('answersContainer').innerHTML = html;
            } else {
                document.getElementById('quizContainer').style.display = 'none';
                document.getElementById('quizTitle').style.display = 'none';
                document.getElementById('quizDesc').style.display = 'none';
                
                const box = document.getElementById('talentSuggestion');
                box.style.display = 'block';
                document.getElementById('sugTitle').innerText = 'Elias the Magician!';
                document.getElementById('sugDesc').innerText = 'Based on your answers, Elias is the perfect fit. He brings the perfect mix of wonder, interaction, and magic for your group.';
            }
        }
      </script>"""

# Replace the interactive-finder section
content = re.sub(
    r'<div class="interactive-finder".*?</script>\s*</div>',
    quiz_html + '\n    </div>',
    content,
    flags=re.DOTALL
)

# 4. Magiqo Standards: redesign completely (simple layout)
standards_css_new = """    .standards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem; }
    .standard-item { display: flex; align-items: flex-start; gap: 1.5rem; background: white; padding: 2rem; border-radius: var(--radius-lg); border-left: 4px solid var(--color-primary); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .standard-item svg { width: 50px; height: 50px; fill: #3895c8; flex-shrink: 0; }
    .standard-text h3 { font-family: var(--font-heading); font-size: 1.5rem; color: var(--color-text); margin-bottom: 0.5rem; }
    .standard-text p { color: var(--color-text-light); line-height: 1.6; font-size: 1rem; margin: 0; }"""

# Replace old standard card CSS with this new one
content = re.sub(r'\.standard-card \{[^\}]+\}', '', content)
content = re.sub(r'\.standard-card::before \{[^\}]+\}', '', content)
content = re.sub(r'\.standard-card:hover \{[^\}]+\}', '', content)
content = re.sub(r'\.standard-card:hover::before \{[^\}]+\}', '', content)
content = re.sub(r'\.standard-card svg \{[^\}]+\}', '', content)
content = re.sub(r'\.standard-card:hover svg \{[^\}]+\}', '', content)

content = content.replace('.standards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }', standards_css_new)

# Replace the HTML for standards
old_standards_html = re.search(r'<div class="standards-grid">.*?</div>\s*</div>\s*</section>', content, re.DOTALL).group(0)
new_standards_html = """<div class="standards-grid">
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
      </div>
    </div>
  </section>"""
content = content.replace(old_standards_html, new_standards_html)


# 5. Book your star "Check Availability" button in pink
content = content.replace(
    'background-color: #2e19a7;" onclick="document.getElementById(\'availModal\')',
    'background-color: var(--color-primary);" onclick="document.getElementById(\'availModal\')'
)

# 6. Have a Talent for magic - Emojis removal
content = re.sub(r'\.join-banner::before\s*\{\s*content:\s*\'[^\']*\';[^\}]+\}', '', content)
content = re.sub(r'\.join-banner::after\s*\{\s*content:\s*\'[^\']*\';[^\}]+\}', '', content)

# 7. Let the magic begin completely purple
# The current CSS is `.cta-section { background: #8338ec; padding: 6rem 0; text-align: center; color: white; }`
# The user wants dark pink / purple shade. Let's use var(--color-primary) if they mean dark pink, or #702670 (deep purple).
# Let's set it to #6a1b9a (purple) or var(--color-primary)
content = re.sub(
    r'\.cta-section\s*\{[^}]*\}',
    r'.cta-section { background: #6a1b9a; padding: 6rem 0; text-align: center; color: white; }',
    content
)

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
