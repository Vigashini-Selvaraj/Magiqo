import re

file_path = 'c:/Users/vigas/Desktop/magiqo/home2.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Title
content = re.sub(
    r'<h1 class="hero-title">.*?</h1>',
    '<h1 class="hero-title"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Make Their</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Day Magical</span></h1>',
    content
)

# 2. Update h2 headings
replacements = {
    '<h2>Meet Our Magical Stars</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Meet Our</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Magical Stars</span></h2>',
    '<h2>Choose Your Experience</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Choose Your</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Experience</span></h2>',
    '<h2>How the Magic Happens</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">How the</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Magic Happens</span></h2>',
    '<h2>Check Your Party Date</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Check Your</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Party Date</span></h2>',
    '<h2>Happy Little Moments</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Happy Little</span> <span style=\"color: #3895c8; -webkit-text-fill-color: #3895c8;\">Moments</span></h2>',
    '<h2>A Little Extra Magic</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">A Little</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Extra Magic</span></h2>',
    '<h2>Frequently Asked Questions</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Frequently Asked</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Questions</span></h2>',
    '<h2>Visual Memories</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Visual</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Memories</span></h2>',
    '<h2>Let the Magic Begin</h2>': '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Let the</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Magic Begin</span></h2>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
