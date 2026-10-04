filepath = r'c:\Users\vigas\Desktop\magiqo\entertainer_detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the hardcoded white backgrounds in dark mode
content = content.replace('.service-card { background: white;', '.service-card { background: var(--color-surface);')
content = content.replace('.process-item { text-align: center; position: relative; z-index: 2; padding: 2rem 1rem; background: white;', '.process-item { text-align: center; position: relative; z-index: 2; padding: 2rem 1rem; background: var(--color-surface);')
content = content.replace('.review-card { background: white;', '.review-card { background: var(--color-surface);')

# Fix the CTA section's invisible text by removing the white background
content = content.replace(
    '<div style="background: white; border-radius: 40px 40px 0 0; padding: 6rem 3rem; text-align: center; box-shadow: 0 -20px 50px rgba(0,0,0,0.1);">',
    '<div style="background: transparent; padding: 6rem 3rem; text-align: center;">'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
