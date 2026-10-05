import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern for div section titles
# <div class="section-title text-center" style="font-family: var(--font-magic);"><span ...>...</span></div>
# Let's replace the opening tag and closing tag for those specific section titles

# 1. Featured Entertainers
html = re.sub(
    r'<div class="section-title text-center" style="font-family: var\(--font-magic\);">(.*?)</div>',
    r'<h2 class="section-title text-center" style="font-family: var(--font-magic); font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem;">\1</h2>',
    html,
    flags=re.DOTALL
)

# 2. Why Choose MAGIQO
html = re.sub(
    r'<div class="section-title text-center" style="font-family: var\(--font-magic\); margin-bottom: 1rem;">(.*?)</div>',
    r'<h2 class="section-title text-center" style="font-family: var(--font-magic); font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem;">\1</h2>',
    html,
    flags=re.DOTALL
)

# 3. Quick Party Finder
html = re.sub(
    r'<h2 style="font-family: var\(--font-magic\); font-size: 2\.5rem; margin-bottom: 1rem;">(.*?)</h2>',
    r'<h2 class="section-title text-center" style="font-family: var(--font-magic); font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem;">\1</h2>',
    html,
    flags=re.DOTALL
)

# 4. Capture Your Smile
html = re.sub(
    r'<h3 style="font-family: var\(--font-magic\); font-size: 2\.5rem; margin-bottom: 1rem;">(.*?)</h3>',
    r'<h2 class="section-title text-center" style="font-family: var(--font-magic); font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem;">\1</h2>',
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
