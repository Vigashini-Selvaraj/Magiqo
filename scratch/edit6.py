import re

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero H1
old_h1 = r'<h1([^>]*)>The Children\'s Favourite Party Entertainers!</h1>'
new_h1 = r'<h1\1><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">The Children\'s Favourite</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Party Entertainers!</span></h1>'
content = re.sub(old_h1, new_h1, content)

# 2. Choose Your Performance Style (Ensure -webkit-text-fill-color is present)
old_choose = r'<h2><span style="color: #3895c8;">Choose Your</span> <span style="color: var\(--color-primary\);">Performance Style</span></h2>'
new_choose = r'<h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Choose Your</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Performance Style</span></h2>'
content = re.sub(old_choose, new_choose, content)

# 3. Loved by Little Guests
old_loved = r'<h2 style="color: #3895c8;">Loved by Little Guests</h2>'
new_loved = r'<h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Loved by</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Little Guests</span></h2>'
content = re.sub(old_loved, new_loved, content)

# 4. The Magiqo Standard
old_standard = r'<h2><span style="color: var\(--color-primary\);">The Magiqo</span> <span style="color: #3895c8;">Standard</span></h2>'
new_standard = r'<h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">The Magiqo</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Standard</span></h2>'
content = re.sub(old_standard, new_standard, content)

# 5. Questions About Our Talent
old_questions = r'<h2 style="color: #3895c8;">Questions About Our Talent</h2>'
new_questions = r'<h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Questions About</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Our Talent</span></h2>'
content = re.sub(old_questions, new_questions, content)

# Write back
with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
