import os
import re

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up everything after </html>
idx = content.find('</html>')
if idx != -1:
    content = content[:idx + 7]

# 2. Fix Child's Age Select to be black
content = re.sub(
    r'<select\s+style="padding: 1rem; border-radius: var\(--radius-sm\); border: 1px solid var\(--color-border\); font-size: 1rem;">',
    '<select style="padding: 1rem; border-radius: var(--radius-sm); border: 1px solid var(--color-border); font-size: 1rem; background: var(--color-surface); color: var(--color-text);">',
    content
)

# 3. Add back the Experience Gallery Modal and Javascript
target_exp_modal = """  <!-- Experience Feedback Modal -->
  <div id="experience-modal" class="modal-overlay"
    onclick="if(event.target === this) document.getElementById('experience-modal').classList.remove('active')">
    <div class="card modal-content" style="text-align: center; padding: 3rem; max-width: 500px;">
      <h2 id="exp-modal-title" style="font-family: var(--font-magic); margin-bottom: 1rem;"><span
          style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Party</span> <span
          style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Experience</span></h2>
      <div style="display: flex; justify-content: center; margin-bottom: 1.5rem; color: #F6C344; font-size: 1.5rem;">
        ★★★★★</div>
      <p id="exp-modal-feedback"
        style="font-size: 1.25rem; font-style: italic; color: var(--color-text-light); margin-bottom: 2rem; line-height: 1.6;">
        "Feedback goes here"</p>
      <button class="btn btn-primary"
        style="background: #3895c8; border-color: #3895c8; color: white; padding: 0.75rem 2rem;"
        onclick="document.getElementById('experience-modal').classList.remove('active')">Close</button>
    </div>
  </div>"""

replacement_exp_modal = """  <!-- Experience Feedback Modal (Gallery Style) -->
  <div id="experience-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9999; align-items:center; justify-content:center; padding:20px; backdrop-filter: blur(5px);">
    <div style="background:var(--color-surface); border-radius:var(--radius-lg); overflow:hidden; display:flex; flex-wrap:wrap; max-width:900px; width:100%; position:relative; box-shadow: 0 25px 50px rgba(0,0,0,0.5);">
      <button onclick="document.getElementById('experience-modal').style.display='none'" style="position:absolute; top:15px; right:20px; background:rgba(255,255,255,0.8); border:none; font-size:1.5rem; color:#111; cursor:pointer; width:40px; height:40px; border-radius:50%; z-index:10; display:flex; align-items:center; justify-content:center;">&times;</button>
      <div style="flex:1; min-width:300px;">
        <img id="exp-modal-img" src="" alt="Party Experience" style="width:100%; height:100%; object-fit:cover; display:block; min-height:300px;">
      </div>
      <div style="flex:1; padding:3rem; display:flex; flex-direction:column; justify-content:center; min-width:300px;">
        <h2 id="exp-modal-title" style="font-family:var(--font-magic); font-size:2.5rem; margin-bottom:0.5rem;">Title</h2>
        <div style="display: flex; margin-bottom: 1.5rem; color: #F6C344; font-size: 1.5rem;">★★★★★</div>
        <p id="exp-modal-feedback" style="color:var(--color-text-light); font-size:1.1rem; line-height:1.6; font-style:italic;">"Feedback goes here"</p>
      </div>
    </div>
  </div>"""

content = content.replace(target_exp_modal, replacement_exp_modal)

target_old_script = """    function openExperienceModal(title, feedback) {
      const words = title.split(' ');
      const mid = Math.max(1, Math.floor(words.length / 2));
      const p1 = words.slice(0, mid).join(' ');
      const p2 = words.slice(mid).join(' ');
      document.getElementById('exp-modal-title').innerHTML = `<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">${p1}</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">${p2}</span>`;

      document.getElementById('exp-modal-feedback').innerText = `"${feedback}"`;
      document.getElementById('experience-modal').classList.add('active');
    }"""

replacement_new_script = """    function openExperienceGalleryModal(title, feedback, imgUrl) {
      const words = title.split(' ');
      const mid = Math.max(1, Math.floor(words.length / 2));
      const p1 = words.slice(0, mid).join(' ');
      const p2 = words.slice(mid).join(' ');
      document.getElementById('exp-modal-title').innerHTML = `<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">${p1}</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">${p2}</span>`;
      document.getElementById('exp-modal-feedback').innerText = `"${feedback}"`;
      document.getElementById('exp-modal-img').src = imgUrl;
      document.getElementById('experience-modal').style.display = 'flex';
    }
    
    function findParty() {
      var theme = document.getElementById('themePref');
      var val = theme ? theme.value : '';
      if (!val || val === 'Theme Preference') val = 'Magic Show';
      
      var data = {
        'Magic Show': { title: 'The Great Magic Show', desc: 'A classic stage magic experience with illusions.', img: 'assets/images/magic_show_party_1790842468826.jpg' },
        'Superheroes': { title: 'Ultimate Hero Training', desc: 'Action-packed games and hero lessons.', img: 'assets/images/superhero_party_1790842695325.jpg' },
        'Princesses': { title: 'Royal Coronation', desc: 'A beautiful crowning ceremony for the birthday girl.', img: 'assets/images/princess_party_1790842645232.jpg' },
        'Clowns & Balloons': { title: 'Silly Clown Antics', desc: 'Hilarious comedy and slapstick fun.', img: 'assets/images/clown_party_1790842566084.jpg' }
      };
      
      var item = data[val] || data['Magic Show'];
      
      document.getElementById('finderResultsTitle').innerText = 'Here is a suggestion for ' + val.toLowerCase() + ':';
      
      var grid = document.getElementById('finderResultsGrid');
      grid.innerHTML = `
          <div style="background:var(--color-surface); border-radius:var(--radius-md); overflow:hidden; box-shadow:0 10px 20px var(--color-shadow); text-align:center; display:flex; flex-direction:column; max-width:400px; margin:0 auto;">
            <img src="${item.img}" style="width:100%; height:200px; object-fit:cover;">
            <div style="padding:2rem; flex:1; display:flex; flex-direction:column;">
              <h4 style="color:var(--color-primary); font-size:1.5rem; margin-bottom:1rem;">${item.title}</h4>
              <p style="color:var(--color-text-light); font-size:1rem; margin-bottom:1.5rem; flex:1;">${item.desc}</p>
              <a href="packages.html" class="btn btn-primary" style="padding:0.8rem 1.5rem; font-size:1rem; width:100%; display:block; box-sizing:border-box;">View Package</a>
            </div>
          </div>
      `;
      
      document.getElementById('finderResults').style.display = 'block';
    }"""

content = content.replace(target_old_script, replacement_new_script)

# Remove the broken closing brace
content = content.replace('    }\n  </script>\n\n\n\n</body>', '  </script>\n\n</body>')
content = content.replace('    }\n  </script>\n\n</body>', '  </script>\n\n</body>')

# Replace finderResults HTML to inline inline 1 item
target_finder_results = """        <div id="finderResults" style="display:none; margin-top:3rem; text-align:left;">
          <h3 id="finderResultsTitle" style="color:var(--color-text); margin-bottom:1.5rem; font-family:var(--font-magic); font-size:2rem; text-align:center;">Here are 3 options for you:</h3>
          <div id="finderResultsGrid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:1.5rem;">
          </div>
        </div>"""

# Fallback in case they reverted back to the old one:
old_target_finder_results = """        <div id="finderResults" style="display:none; margin-top:3rem; text-align:left;">
          <h3 style="color:var(--color-text); margin-bottom:1.5rem; font-family:var(--font-magic); font-size:2rem; text-align:center;">Here are 3 magic shows for you:</h3>
          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1.5rem;">
            <div style="background:var(--color-surface); border-radius:var(--radius-md); padding:1.5rem; box-shadow:0 10px 20px var(--color-shadow); text-align:center;">
              <h4 style="color:var(--color-primary); font-size:1.2rem; margin-bottom:0.5rem;">The Great Magic Show</h4>
              <p style="color:var(--color-text-light); font-size:0.9rem; margin-bottom:1rem;">A classic stage magic experience with illusions.</p>
              <a href="packages.html" class="btn btn-outline" style="padding:0.5rem 1rem; font-size:0.9rem;">View Package</a>
            </div>
            <div style="background:var(--color-surface); border-radius:var(--radius-md); padding:1.5rem; box-shadow:0 10px 20px var(--color-shadow); text-align:center;">
              <h4 style="color:var(--color-primary); font-size:1.2rem; margin-bottom:0.5rem;">Close-Up Magic</h4>
              <p style="color:var(--color-text-light); font-size:0.9rem; margin-bottom:1rem;">Interactive magic tricks right before your eyes.</p>
              <a href="packages.html" class="btn btn-outline" style="padding:0.5rem 1rem; font-size:0.9rem;">View Package</a>
            </div>
            <div style="background:var(--color-surface); border-radius:var(--radius-md); padding:1.5rem; box-shadow:0 10px 20px var(--color-shadow); text-align:center;">
              <h4 style="color:var(--color-primary); font-size:1.2rem; margin-bottom:0.5rem;">Comedy Magic</h4>
              <p style="color:var(--color-text-light); font-size:0.9rem; margin-bottom:1rem;">Laughs and magic combined for kids.</p>
              <a href="packages.html" class="btn btn-outline" style="padding:0.5rem 1rem; font-size:0.9rem;">View Package</a>
            </div>
          </div>
        </div>"""

replacement_finder_results = """        <div id="finderResults" style="display:none; margin-top:3rem; text-align:left;">
          <h3 id="finderResultsTitle" style="color:var(--color-text); margin-bottom:1.5rem; font-family:var(--font-magic); font-size:2rem; text-align:center;">Here is a suggestion for you:</h3>
          <div id="finderResultsGrid" style="display:block; text-align:center;">
          </div>
        </div>"""

if target_finder_results in content:
    content = content.replace(target_finder_results, replacement_finder_results)
elif old_target_finder_results in content:
    content = content.replace(old_target_finder_results, replacement_finder_results)


# Fix the onclick handlers for the Party Experiences
content = content.replace(
    'onclick="openExperienceModal(\'Feedback\', \'The Classic Magic show was astounding! Our 6-year-old was captivated the entire time. - Jane Doe\')"',
    'onclick="openExperienceGalleryModal(\'Classic Magic\', \'The Classic Magic show was astounding! Our 6-year-old was captivated the entire time. - Jane Doe\', \'assets/images/magic_show_party_1790842468826.jpg\')"'
)
content = content.replace(
    'onclick="openExperienceModal(\'Feedback\', \'Princess Mia made my daughter feel like royalty! Best birthday ever. - Mark Smith\')"',
    'onclick="openExperienceGalleryModal(\'Royal Princess\', \'Princess Mia made my daughter feel like royalty! Best birthday ever. - Mark Smith\', \'assets/images/princess_party_1790842645232.jpg\')"'
)
content = content.replace(
    'onclick="openExperienceModal(\'Feedback\', \'Max the Action Hero brought so much energy! The kids had a blast doing superhero training. - Sarah K.\')"',
    'onclick="openExperienceGalleryModal(\'Superhero Action\', \'Max the Action Hero brought so much energy! The kids had a blast doing superhero training. - Sarah K.\', \'assets/images/superhero_party_1790842695325.jpg\')"'
)
content = content.replace(
    'onclick="openExperienceModal(\'Feedback\', \'The Silly Clowns were hilarious and kept the toddlers laughing non-stop. - Emily R.\')"',
    'onclick="openExperienceGalleryModal(\'Silly Clowns\', \'The Silly Clowns were hilarious and kept the toddlers laughing non-stop. - Emily R.\', \'assets/images/clown_party_1790842566084.jpg\')"'
)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
