import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the backslash in "The Children\'s"
content = content.replace("The Children\\'s Favourite", "The Children's Favourite")

# 2. Fix the CTA UI
# Make sure text inside .cta-section is readable. 
# Previously it had <p style="... color: rgba(255,255,255,0.9); ...">, wait, maybe I removed that in a previous edit.
# Let's just fix the whole CTA section HTML to be clean and readable.

cta_old = re.search(r'<section class="cta-section">.*?</section>', content, re.DOTALL).group(0)

# Create a clean CTA section with good contrast and a nice button
cta_new = """<section class="cta-section" style="background: var(--color-secondary); padding: 8rem 0; text-align: center; color: white; position: relative; overflow: hidden;">
    <div class="container text-center" style="position: relative; z-index: 2;">
      <div class="sec-title" style="margin-bottom: 2rem;">
        <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Let the</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Magic Begin</span></h2>
      </div>
      <p style="font-size: 1.25rem; max-width: 600px; margin: 0 auto 3rem; line-height: 1.6; color: rgba(255,255,255,0.9);">
        Don't leave the entertainment to chance. Hire a professional and make your child's birthday the talk of the playground.
      </p>
      <a href="contact.html" class="btn btn-animated" style="background: var(--color-primary); color: white; padding: 1.25rem 4rem; font-size: 1.25rem; font-weight: bold; border-radius: var(--radius-pill); text-decoration: none; display: inline-block; box-shadow: 0 10px 20px rgba(218, 47, 95, 0.4); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Start Booking Now</a>
    </div>
  </section>"""

content = content.replace(cta_old, cta_new)

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
