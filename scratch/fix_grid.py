import re
filepath = r'c:\Users\vigas\Desktop\magiqo\packages.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix container scroll
content = content.replace('overflow-x: auto;', '')

# Fix grid layout to 3x2
content = content.replace(
'''        .modern-compare-grid {
          display: flex;
          gap: 1.5rem;
          min-width: 900px; /* Ensure horizontal scroll on small screens */
        }''',
'''        .modern-compare-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 2rem;
        }'''
)

# Remove scaling from the second item so internal items align perfectly
content = content.replace(
    '<div class="compare-column" style="border-top-color: #3895c8; transform: scale(1.03); box-shadow: 0 15px 35px rgba(56,149,200,0.15);">',
    '<div class="compare-column" style="border-top-color: #3895c8; box-shadow: 0 15px 35px rgba(56,149,200,0.15);">'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
