import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix hero h1 text-fill-color
html = html.replace(
    '<span style="color: #D24B76 !important;">Make Their</span>',
    '<span style="color: #D24B76 !important; -webkit-text-fill-color: initial !important;">Make Their</span>'
)
html = html.replace(
    '<span style="color: #3895c8 !important;">Day</span><br>',
    '<span style="color: #3895c8 !important; -webkit-text-fill-color: initial !important;">Day</span><br>'
)
html = html.replace(
    '<span style="color: #3895c8 !important;">Magical</span>',
    '<span style="color: #3895c8 !important; -webkit-text-fill-color: initial !important;">Magical</span>'
)

# 2. Fix Quick Party Finder: change color: white; to color: var(--color-text); for selects
# And add overflow: visible to the card.
html = html.replace(
    'style="padding: 4rem; text-align: center; border-radius: var(--radius-lg); box-shadow: 0 20px 40px var(--color-shadow); max-width: 800px; margin: 0 auto;"',
    'style="padding: 4rem; text-align: center; border-radius: var(--radius-lg); box-shadow: 0 20px 40px var(--color-shadow); max-width: 800px; margin: 0 auto; overflow: visible;"'
)

html = html.replace(
    'style="padding: 1rem; border-radius: var(--radius-sm); border: 1px solid var(--color-border); font-size: 1rem; background: var(--color-surface); color: white;"',
    'style="padding: 1rem; border-radius: var(--radius-sm); border: 1px solid var(--color-border); font-size: 1rem; background: var(--color-surface); color: var(--color-text);"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
