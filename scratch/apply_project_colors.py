import re

file_path = 'c:/Users/vigas/Desktop/magiqo/entertainer_detail.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Fonts and CSS Variables
# Remove the old font imports
content = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Playfair\+Display.*?rel="stylesheet">', '', content)

# Map the --ed-* variables to project variables
new_css_vars = '''
    :root {
      --ed-pink: var(--color-primary);
      --ed-pink-dark: var(--color-primary-hover);
      --ed-blue: #3895c8;
      --ed-purple: var(--color-secondary);
      --ed-bg: var(--color-bg);
      --ed-soft: var(--color-surface);
      --ed-text: var(--color-text);
      --ed-muted: var(--color-text-light);
      --ed-border: var(--color-border);
      --ed-shadow: 0 20px 55px var(--color-shadow);
      --ed-heading: var(--font-heading);
      --ed-body: var(--font-body);
    }
'''
content = re.sub(r':root\s*\{.*?\-\-ed\-body.*?;[\s\n]*\}', new_css_vars, content, flags=re.DOTALL)

# Also fix the `font-family` usage to make sure we use --font-magic where appropriate, like the hero heading.
content = re.sub(r'\.profile-info h1\s*\{.*?\n.*?margin', r'.profile-info h1 {\n      font-family: var(--font-magic);\n      font-size: clamp(3.6rem, 6vw, 5.8rem);\n      font-weight: 600;\n      line-height: 1;\n      color: var(--ed-purple);\n      margin', content, flags=re.DOTALL)

# 2. Redesign Section 9 (PLAN YOUR EVENT)
section_9 = '''
  <!-- 9. BOOKING INFORMATION -->
  <section class="ed-booking-info ed-reveal" style="background: var(--color-surface); padding: 80px 0;">
    <div class="ed-container">

      <div class="ed-booking-box" style="background: var(--color-bg); border: 2px solid var(--color-border); transform: translateY(0); transition: transform 0.3s ease, box-shadow 0.3s ease;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">

        <div class="ed-booking-copy">
          <span class="ed-eyebrow" style="color: var(--color-primary);">PLAN YOUR EVENT</span>
          <h2 style="font-family: var(--font-magic); font-weight: normal; font-size: 3.5rem; background: none; -webkit-text-fill-color: var(--color-text);">Ready to make it memorable?</h2>
          <p>
            Check availability, tell us about your celebration
            and choose the experience that works for you.
          </p>
        </div>

        <div class="ed-booking-details">
          <div class="ed-booking-detail" style="border-bottom-color: rgba(0,0,0,0.1);">
            <span>Entertainer</span>
            <strong id="booking-entertainer-name">Elias</strong>
          </div>

          <div class="ed-booking-detail" style="border-bottom-color: rgba(0,0,0,0.1);">
            <span>Rating</span>
            <strong>5.0 / 5</strong>
          </div>

          <div class="ed-booking-detail" style="border-bottom-color: rgba(0,0,0,0.1);">
            <span>Booking</span>
            <strong>Availability Request</strong>
          </div>
        </div>

        <a
          href="booking.html?id=elias"
          id="ent-book-btn"
          class="ed-book-button"
          style="background: var(--color-primary); color: white; padding: 1.5rem 2rem; font-size: 1.1rem; box-shadow: 0 10px 20px rgba(210, 75, 118, 0.3);"
        >
          Check Availability <span aria-hidden="true">→</span>
        </a>

      </div>
    </div>
  </section>
'''

content = re.sub(r'<!-- 9\. BOOKING INFORMATION -->.*?</section>', section_9, content, flags=re.DOTALL)

# 3. Redesign Section 10 (FINAL CTA)
section_10 = '''
  <!-- 10. FINAL CTA -->
  <section class="ed-final-cta ed-reveal" style="background: var(--color-primary); padding: 100px 0; border-radius: 40px 40px 0 0; margin-top: 40px; box-shadow: 0 -20px 50px rgba(210, 75, 118, 0.2);">
    
    <div class="ed-container" style="position:relative;z-index:1; text-align: center;">
      <span class="ed-eyebrow" style="color: white; opacity: 0.9; font-size: 1rem; letter-spacing: 4px;">YOUR CELEBRATION STARTS HERE</span>

      <h2 style="font-family: var(--font-magic); font-size: 4.5rem; background: none; -webkit-text-fill-color: white; color: white; margin-top: 1rem; font-weight: normal;">
        Make this a moment
        <span style="color: #FFEED6; display: block;">they'll never forget.</span>
      </h2>

      <p style="font-size: 1.3rem; color: rgba(255,255,255,0.9); max-width: 600px; margin: 0 auto 3rem;">
        Choose your entertainer, tell us what you're planning
        and let Magiqo take care of the experience.
      </p>

      <a href="booking.html?id=elias" id="final-book-btn" class="ed-final-button" style="background: white; color: var(--color-primary); padding: 1.5rem 3rem; font-size: 1.3rem; border-radius: 50px; box-shadow: 0 15px 30px rgba(0,0,0,0.15);" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.2)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 15px 30px rgba(0,0,0,0.15)';">
        Start Your Booking <span aria-hidden="true" style="margin-left: 10px;">→</span>
      </a>
    </div>
  </section>
'''

content = re.sub(r'<!-- 10\. FINAL CTA -->.*?</section>', section_10, content, flags=re.DOTALL)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CSS and CTA sections in entertainer_detail.html")
