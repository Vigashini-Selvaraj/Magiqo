import os

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Theme Preference select block
old_select = """          <select style="padding: 1rem; border-radius: var(--radius-sm); border: 1px solid var(--color-border); font-size: 1rem; background: var(--color-surface); color: var(--color-text);">
            <option>Theme Preference</option>
            <option>Magic Show</option>
            <option>Superheroes</option>
            <option>Princesses</option>
            <option>Clowns & Balloons</option>
          </select>"""

new_select = """          <select id="themePref" style="padding: 1rem; border-radius: var(--radius-sm); border: 1px solid var(--color-border); font-size: 1rem; background: var(--color-surface); color: var(--color-text);">
            <option>Theme Preference</option>
            <option value="Magic Show">Magic Show</option>
            <option value="Superheroes">Superheroes</option>
            <option value="Princesses">Princesses</option>
            <option value="Clowns & Balloons">Clowns & Balloons</option>
          </select>"""

content = content.replace(old_select, new_select)

# Fix Find My Magic button and append the results block
old_button = """<a href="#services" class="btn btn-primary" style="font-size: 1.125rem; padding: 1rem 3rem;">Find My Magic</a>"""

new_button_with_results = """<a href="javascript:void(0)" class="btn btn-primary" style="font-size: 1.125rem; padding: 1rem 3rem;" onclick="findParty()">Find My Magic</a>
        
        <div id="finderResults" style="display:none; margin-top:3rem; text-align:left;">
          <h3 id="finderResultsTitle" style="color:var(--color-text); margin-bottom:1.5rem; font-family:var(--font-magic); font-size:2rem; text-align:center;">Here is a suggestion for you:</h3>
          <div id="finderResultsGrid" style="display:block; text-align:center;">
          </div>
        </div>"""

content = content.replace(old_button, new_button_with_results)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
