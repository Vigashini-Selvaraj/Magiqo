import re
import os

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Title
content = re.sub(
    r'<h1([^>]*)>Make Their<br>Day Magical\.</h1>',
    r'<h1\1><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Make Their</span><br><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Day Magical.</span></h1>',
    content
)

# 2. Update Book Now button in Hero
content = content.replace(
    '<a href="entertainers.html" class="btn btn-secondary" style="font-size: 1.125rem; padding: 1rem 2rem;">Book Now</a>',
    '<a href="entertainers.html" class="btn btn-secondary" style="font-size: 1.125rem; padding: 1rem 2rem; background: #3895c8; border-color: #3895c8; color: white;">Book Now</a>'
)

# 3. Fix section titles
# Replace the existing spans in section titles to use the correct colors
# Example: <span style="color: var(--color-text); -webkit-text-fill-color: initial;">Featured</span>
content = re.sub(
    r'<span style="color: var\(--color-text\); -webkit-text-fill-color: initial;">(.*?)</span>',
    r'<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">\1</span>',
    content
)
# Example: <span class="text-primary" style="-webkit-text-fill-color: initial;">Entertainers</span>
content = re.sub(
    r'<span class="text-primary" style="-webkit-text-fill-color: initial;">(.*?)</span>',
    r'<span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">\1</span>',
    content
)
# Example: <div class="section-title text-center" style="font-family: var(--font-magic);">Why Choose <span class="text-primary">MAGIQO</span></div>
content = content.replace(
    '<div class="section-title text-center" style="font-family: var(--font-magic);">Why Choose <span class="text-primary">MAGIQO</span></div>',
    '<div class="section-title text-center" style="font-family: var(--font-magic);"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Why Choose</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">MAGIQO</span></div>'
)
content = content.replace(
    '<div class="section-title text-center" style="font-family: var(--font-magic);">Popular <span class="text-primary">Packages</span></div>',
    '<div class="section-title text-center" style="font-family: var(--font-magic);"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Popular</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Packages</span></div>'
)
content = content.replace(
    '<div class="section-title text-center" style="font-family: var(--font-magic);">Party <span class="text-primary">Experiences</span></div>',
    '<div class="section-title text-center" style="font-family: var(--font-magic);"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Party</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Experiences</span></div>'
)
content = content.replace(
    '<div class="section-title text-center" style="font-family: var(--font-magic);">Real Party <span class="text-primary">Moments</span></div>',
    '<div class="section-title text-center" style="font-family: var(--font-magic);"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Real Party</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Moments</span></div>'
)
content = content.replace(
    '<h3 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 1rem;">Capture Your Smile & Post To Us!</h3>',
    '<h3 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 1rem;"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Capture Your Smile</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">& Post To Us!</span></h3>'
)
content = content.replace(
    '<div class="section-title text-center" style="font-family: var(--font-magic);">Parent <span class="text-primary">Reviews</span></div>',
    '<div class="section-title text-center" style="font-family: var(--font-magic);"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Parent</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Reviews</span></div>'
)

# 4. Remove CTAs
# We can use regex to remove everything from <!-- Smart Party Suggestions Modal Trigger Section --> to the end of <!-- Final CTA -->
content = re.sub(
    r'<!-- Smart Party Suggestions Modal Trigger Section -->.*?<!-- Final CTA -->.*?</section>',
    '',
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")
