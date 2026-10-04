import os

# 1. Fix Capture Your Smile in index.html
filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target_capture = 'background: white; border-radius: var(--radius-lg); box-shadow: 0 15px 40px rgba(0,0,0,0.05); padding: 4rem;'
replacement_capture = 'background: var(--color-surface); border-radius: var(--radius-lg); box-shadow: 0 15px 40px var(--color-shadow); padding: 4rem;'
if target_capture in content:
    content = content.replace(target_capture, replacement_capture)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Fix Footer in components/footer.html
footer_path = 'c:/Users/vigas/Desktop/magiqo/components/footer.html'
with open(footer_path, 'r', encoding='utf-8') as f:
    footer_content = f.read()

# Change footer background to adaptive
target_footer_bg = """footer {
  position: relative;
  overflow: hidden;
  background: linear-gradient(
    125deg,
    #fff5fa 0%,
    #f8f6ff 50%,
    #f0f9ff 100%
  );
  padding: 85px 7% 0;
}"""
replacement_footer_bg = """footer {
  position: relative;
  overflow: hidden;
  background: var(--color-surface);
  padding: 85px 7% 0;
}"""

footer_content = footer_content.replace(target_footer_bg, replacement_footer_bg)

# Map internal footer variables to the global theme variables so it adapts
target_vars = """:root {
  --pink: #f17bac;
  --pink-dark: #d95791;
  --sky: #75bff2;
  --sky-dark: #439bdc;
  --purple: #49356b;
  --text: #777185;
  --dark: #302344;
  --light: #fff9fc;
  --border: rgba(100, 77, 124, 0.14);
}"""

replacement_vars = """:root {
  --pink: var(--color-primary);
  --pink-dark: var(--color-primary-hover);
  --sky: var(--color-secondary);
  --sky-dark: var(--color-secondary);
  --purple: var(--color-text);
  --text: var(--color-text-light);
  --dark: var(--color-text);
  --light: var(--color-bg);
  --border: var(--color-border);
}"""

footer_content = footer_content.replace(target_vars, replacement_vars)

# Remove hardcoded body colors in footer.html just in case
footer_content = footer_content.replace(
    'background: #fff9fc;\n  color: #625b70;',
    'background: transparent;\n  color: var(--color-text);'
)

with open(footer_path, 'w', encoding='utf-8') as f:
    f.write(footer_content)

print("Updated index.html and footer.html")
