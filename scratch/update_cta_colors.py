import re

file_path = 'c:/Users/vigas/Desktop/magiqo/entertainers.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_cta = '''
  <!-- NEW SECTION 3: Join the Team (CTA) -->
  <section class="cta-section" style="background: #D24B76; padding: 6rem 0; text-align: center; position: relative; overflow: hidden;">
    <div class="container" style="position: relative; z-index: 2;">
        <h2 style="font-family: var(--font-magic); font-size: 3.5rem; margin-bottom: 1rem; color: white !important; -webkit-text-fill-color: white !important; background: none !important;">
           Have a Talent for Magic?
        </h2>
        <p style="font-size: 1.25rem; color: white; max-width: 700px; margin: 0 auto 3rem; line-height: 1.6;">
           We are always looking for passionate, high-energy individuals to join our growing roster of premium entertainers. If you love making kids smile, we'd love to meet you.
        </p>
        <a href="join.html" class="btn btn-animated" style="background: #3895c8; color: white; padding: 1.25rem 4rem; font-size: 1.25rem; font-weight: bold; border-radius: var(--radius-pill); box-shadow: 0 10px 20px rgba(56, 149, 200, 0.4); text-decoration: none; display: inline-block; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Apply to Join</a>
    </div>
  </section>
'''

content = re.sub(r'<!-- NEW SECTION 3: Join the Team \(CTA\) -->.*?</section>', new_cta, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated CTA colors')
