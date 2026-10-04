import re

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the misplaced third blog cards from hero and other places
bad_card = """
        <div class="card" style="padding: 0; overflow: hidden;">
          <img src="assets/images/superhero_party_1790842695325.jpg" alt="Action Hero Theme"
            style="width: 100%; height: 250px; object-fit: cover; display: block;" />
          <div style="padding: 1.5rem;">
            <span
              style="color: var(--color-primary); font-size: 0.875rem; font-weight: bold; text-transform: uppercase;">Themes</span>
            <h3 style="margin: 0.5rem 0; font-size: 1.5rem;">How to Host an Epic Superhero Action Party</h3>
            <p style="color: var(--color-text-light); margin-bottom: 1rem;">Action-packed games and ideas that will make your child feel like they have superpowers.</p>
            <a href="blog-detail.html" class="text-primary" style="font-weight: 600;">Read More &rarr;</a>
          </div>
        </div>"""
content = content.replace(bad_card, '')

# 2. Add the modal styles back
modal_styles = """
  <style>
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(5px);
      z-index: 2000;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      visibility: hidden;
      transition: all 0.3s ease;
    }
    .modal-overlay.active {
      opacity: 1;
      visibility: visible;
    }
    .modal-content {
      transform: translateY(20px);
      transition: transform 0.3s ease;
    }
    .modal-overlay.active .modal-content {
      transform: translateY(0);
    }
  </style>
"""
if '.modal-overlay {' not in content:
    content = content.replace('<!-- Experience Feedback Modal -->', modal_styles + '\n  <!-- Experience Feedback Modal -->')

# 3. Add the third blog card exactly in the blog section
# The blog section ends before the </section> of #blog. Let's find it.
blog_end = """        </div>
      </div>
    </div>
  </section>"""
if 'How to Host an Epic Superhero Action Party' not in content:
    content = content.replace(blog_end, bad_card + '\n' + blog_end)

# 4. Fix MOST POPULAR badge and Select Package button to Golden
# Badge currently has background: #3895c8; color: white;
# Change to Golden background: #F6C344; color: #180D20;
content = content.replace(
    '<div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #3895c8; color: white; padding: 0.5rem 1.5rem; border-radius: 20px; font-weight: bold; font-size: 0.875rem; letter-spacing: 1px;">MOST POPULAR</div>',
    '<div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #F6C344; color: #180D20; padding: 0.5rem 1.5rem; border-radius: 20px; font-weight: bold; font-size: 0.875rem; letter-spacing: 1px;">MOST POPULAR</div>'
)

# Button currently has class="btn btn-primary" in Magic Spell card
# Let's find the Select Package button for Magic spell. It's the second button.
# Replace the specific button.
magic_button_old = '<a href="packages.html" class="btn btn-primary" style="width: 100%;">Select Package</a>'
magic_button_new = '<a href="packages.html" class="btn" style="width: 100%; background: #F6C344; color: #180D20; font-weight: bold; border-color: #F6C344;">Select Package</a>'
# Let's be safer:
content = re.sub(
    r'(<div class="card text-center" style="padding: 3rem 2rem; border: none; background: var\(--color-primary\);.*?)<a href="packages.html" class="btn btn-primary" style="width: 100%;">Select Package</a>(.*?)</div>\s*</div>\s*<!-- Card 3 -->',
    r'\1' + magic_button_new + r'\2</div>\n        </div>\n        <!-- Card 3 -->',
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html fully cleaned up!")
