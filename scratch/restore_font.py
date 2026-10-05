import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the font-family and text-transform in the h1
html = html.replace(
    "font-family: 'Inter', sans-serif; font-size: clamp(3rem, 7vw, 7.5rem); font-weight: 900; line-height: 0.95; margin: 0 0 35px 0; color: var(--color-text); text-transform: uppercase; letter-spacing: -2px;",
    "font-family: var(--font-magic); font-size: clamp(4rem, 8vw, 8.5rem); font-weight: normal; line-height: 1.1; margin: 0 0 35px 0; color: var(--color-text);"
)

# Change the uppercase text back to Title Case so Berkshire Swash looks good
html = html.replace(
    "MAKE<br>\n        THEIR<br>\n        <span style=\"color: var(--color-primary);\">DAY<br>MAGICAL.</span>",
    "Make<br>\n        Their<br>\n        <span style=\"color: var(--color-primary);\">Day<br>Magical.</span>"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
