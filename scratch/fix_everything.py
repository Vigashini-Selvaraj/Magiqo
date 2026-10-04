import re

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. REMOVE ALL INJECTED BLOG CARDS
# The card contains "How to Host an Epic Superhero Action Party"
bad_card_pattern = r'\s*<div class="card" style="padding: 0; overflow: hidden;">\s*<img src="assets/images/superhero_party_1790842695325\.jpg" alt="Action Hero Theme".*?How to Host an Epic Superhero Action Party.*?</div>\s*</div>'

content = re.sub(bad_card_pattern, '', content, flags=re.DOTALL)

# 2. INSERT ONE BLOG CARD INTO THE BLOG SECTION
blog_card = """
        <div class="card" style="padding: 0; overflow: hidden;">
          <img src="assets/images/superhero_party_1790842695325.jpg" alt="Action Hero Theme"
            style="width: 100%; height: 250px; object-fit: cover; display: block;" />
          <div style="padding: 1.5rem;">
            <span style="color: var(--color-primary); font-size: 0.875rem; font-weight: bold; text-transform: uppercase;">Themes</span>
            <h3 style="margin: 0.5rem 0; font-size: 1.5rem;">How to Host an Epic Superhero Action Party</h3>
            <p style="color: var(--color-text-light); margin-bottom: 1rem;">Action-packed games and ideas that will make your child feel like they have superpowers.</p>
            <a href="blog-detail.html" class="text-primary" style="font-weight: 600;">Read More &rarr;</a>
          </div>
        </div>
"""
# Find the blog grid and insert the card at the end of it
blog_grid_end = r'(<section id="blog".*?<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); gap: 2rem;">.*?)(\s*</div>\s*</div>\s*</section>)'
content = re.sub(blog_grid_end, r'\1' + blog_card + r'\2', content, flags=re.DOTALL)

# 3. REVERT THE EXPERIENCE MODAL TO A SIMPLE, LESS DRAMATIC DESIGN
simple_modal = """
  <!-- Experience Feedback Modal -->
  <div id="experience-modal" class="modal-overlay" onclick="if(event.target === this) document.getElementById('experience-modal').classList.remove('active')">
    <div class="card modal-content" style="text-align: center; padding: 3rem; max-width: 500px;">
      <h2 id="exp-modal-title" style="font-family: var(--font-magic); margin-bottom: 1rem;"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Party</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Experience</span></h2>
      <div style="display: flex; justify-content: center; margin-bottom: 1.5rem; color: #F6C344; font-size: 1.5rem;">★★★★★</div>
      <p id="exp-modal-feedback" style="font-size: 1.25rem; font-style: italic; color: var(--color-text-light); margin-bottom: 2rem; line-height: 1.6;">"Feedback goes here"</p>
      <button class="btn btn-primary" style="background: #3895c8; border-color: #3895c8; color: white; padding: 0.75rem 2rem;" onclick="document.getElementById('experience-modal').classList.remove('active')">Close</button>
    </div>
  </div>

  <script>
    function openExperienceModal(title, feedback) {
      const words = title.split(' ');
      const mid = Math.max(1, Math.floor(words.length / 2));
      const p1 = words.slice(0, mid).join(' ');
      const p2 = words.slice(mid).join(' ');
      document.getElementById('exp-modal-title').innerHTML = `<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">${p1}</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">${p2}</span>`;
      
      document.getElementById('exp-modal-feedback').innerText = `"${feedback}"`;
      document.getElementById('experience-modal').classList.add('active');
    }
  </script>
"""
content = re.sub(r'<!-- Experience Feedback Modal -->.*?</script>', simple_modal, content, flags=re.DOTALL)

# 4. FIX THE ONCLICK EVENTS FOR PARTY EXPERIENCES (REMOVE THE IMAGE ARGUMENT)
content = re.sub(
    r'onclick="let img = this\.style\.backgroundImage\.match\(/url\(\\\'(.*?)\\\'\)/\)\[1\]; openExperienceModal\(\'Party Feedback\', \'(.*?)\', img\)"',
    r'onclick="openExperienceModal(\'Party Feedback\', \'\2\')"',
    content
)

# 5. FIX THE DUPLICATE GEMINI IMAGE IN REAL PARTY MOMENTS (GALLERY)
# The gallery has 2 rows of images. I will find the second occurrence of kids_clapping_party and replace it.
content = content.replace('kids_clapping_party_1790917531872.jpg', 'party_moments_2_1790918669697.jpg', 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html completely repaired and updated!")
