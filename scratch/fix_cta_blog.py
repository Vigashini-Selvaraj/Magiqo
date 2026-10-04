import re

filepath_blog = r'c:\Users\vigas\Desktop\magiqo\blog.html'
with open(filepath_blog, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old giant CTA block
old_cta_regex = r'<!-- 12\. FINAL CTA -->.*?</section>'

new_cta = '''<!-- 12. FINAL CTA -->
    <section class="cta-section">
      <div class="container text-center" style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
        <div class="sec-title" style="margin-bottom: 2rem;">
          <h2 style="color: white !important; -webkit-text-fill-color: white !important; background: none !important; font-family: var(--font-heading);">Ready to make magic happen</h2>
        </div>
        <p style="font-size: 1.25rem; max-width: 600px; margin: 0 auto 3rem; line-height: 1.6; color: rgba(255,255,255,0.9);">
          Stop dreaming about the perfect party and let us bring it to life. Book your magical celebration today.
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="contact.html" class="btn btn-animated" style="background: white; color: var(--color-primary); padding: 1.25rem 3rem; font-size: 1.125rem; border-radius: 50px; font-weight: bold; text-decoration: none;">Contact Us</a>
        </div>
      </div>
    </section>'''

content = re.sub(old_cta_regex, new_cta, content, flags=re.DOTALL)

# Add .cta-section CSS if missing
if '.cta-section {' not in content:
    css_to_add = '''
    .cta-section {
      background: var(--color-primary); /* Requested pink shade */
      padding: 6rem 0;
      text-align: center;
      margin-top: 80px;
    }
    .cta-section h2 {
      color: white !important;
      -webkit-text-fill-color: white !important;
      background: none !important;
    }
'''
    content = content.replace('/* New 3D and Hover Effects */', css_to_add + '    /* New 3D and Hover Effects */')

with open(filepath_blog, 'w', encoding='utf-8') as f:
    f.write(content)
