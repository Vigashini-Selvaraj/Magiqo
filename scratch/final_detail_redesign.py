import re
import os

filepath = r'c:\Users\vigas\Desktop\magiqo\entertainer_detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: CSS colors and body background
content = content.replace('--ed-purple: var(--color-secondary);', '--ed-purple: #3895c8;')
content = content.replace('body {\n      margin: 0;\n      font-family: var(--ed-body);\n      color: var(--ed-text);\n      background: white;\n    }', 'body {\n      margin: 0;\n      font-family: var(--ed-body);\n      color: var(--ed-text);\n      background: var(--color-bg);\n    }')

# Fix 2: Split Headings
content = content.replace(
    '<span class="blue-text">What you can book</span>',
    '<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">What you</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">can book</span>'
)
content = content.replace(
    '<span class="pink-text">See the magic unfold</span>',
    '<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">See the</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">magic unfold</span>'
)
content = content.replace(
    '<span class="blue-text">From booking to celebration</span>',
    '<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">From booking</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">to celebration</span>'
)
content = content.replace(
    '<span class="pink-text">What families are saying</span>',
    '<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">What families</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">are saying</span>'
)
content = content.replace(
    '<span class="pink-text">So many celebrations.</span>',
    '<span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">So many</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">celebrations</span>'
)

# Fix 3: "What you can book" boxes dark theme
# Originally: <div class="ed-event-card"> ... background: white; ...
content = re.sub(
    r'\.ed-event-card \{[\s\S]*?\}',
    r'.ed-event-card {\n      background: var(--color-surface);\n      padding: 3rem 2.5rem;\n      border-radius: 20px;\n      text-align: center;\n      box-shadow: var(--ed-shadow);\n      border-top: 5px solid var(--ed-pink);\n      transition: .4s ease;\n      display: flex;\n      flex-direction: column;\n      height: 100%;\n    }',
    content
)

# Fix 4: Gallery equal sizes
content = re.sub(
    r'\.ed-gallery-grid img \{[\s\S]*?\}',
    r'.ed-gallery-grid img {\n      width: 100%;\n      aspect-ratio: 1;\n      object-fit: cover;\n      border-radius: 20px;\n      transition: .4s ease;\n    }',
    content
)

# Fix 5: Testimonials equal height and dark theme compatible
content = re.sub(
    r'\.ed-review-card \{[\s\S]*?\}',
    r'.ed-review-card {\n      background: var(--color-surface);\n      padding: 3rem;\n      border-radius: 20px;\n      box-shadow: var(--ed-shadow);\n      position: relative;\n      height: 100%;\n      display: flex;\n      flex-direction: column;\n    }',
    content
)
# Ensure the grid for testimonials uses stretch
content = re.sub(
    r'\.ed-reviews-grid \{[\s\S]*?\}',
    r'.ed-reviews-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));\n      gap: 2rem;\n      align-items: stretch;\n    }',
    content
)

# Fix 6: Redesign "From booking to celebration" timeline
content = re.sub(
    r'\.ed-process-grid \{[\s\S]*?\}',
    r'.ed-process-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));\n      gap: 2rem;\n      position: relative;\n      align-items: stretch;\n    }',
    content
)
content = re.sub(
    r'\.ed-process-step \{[\s\S]*?\}',
    r'.ed-process-step {\n      background: var(--color-surface);\n      padding: 3rem 2rem;\n      border-radius: 20px;\n      text-align: center;\n      box-shadow: 0 10px 30px rgba(0,0,0,0.05);\n      border: 1px solid var(--color-border);\n      height: 100%;\n    }',
    content
)

# Fix 7: "Designed around your celebration" box dark theme
content = content.replace(
    '<div style="background: white; padding: 3rem; border-radius: 30px; box-shadow: 0 20px 50px rgba(0,0,0,0.08); border-left: 8px solid #3895c8; position: relative;">',
    '<div style="background: var(--color-surface); padding: 3rem; border-radius: 30px; box-shadow: 0 20px 50px rgba(0,0,0,0.08); border-left: 8px solid #3895c8; position: relative; height: 100%; display: flex; flex-direction: column; justify-content: center;">'
)

# Fix 8: Final CTA totally pink
content = content.replace(
    '<section class="ed-section ed-reveal" style="padding-bottom: 0;">',
    '<section class="ed-section ed-reveal" style="padding-bottom: 0; background: var(--color-primary); padding-top: 6rem;">'
)
content = content.replace(
    '<span class="blue-text">Ready to make it</span><br>',
    '<span style="color: white !important; -webkit-text-fill-color: white !important; background: none;">Ready to make it</span><br>'
)
content = content.replace(
    '<span class="pink-text">memorable?</span>',
    '<span style="color: white !important; -webkit-text-fill-color: white !important; background: none;">memorable?</span>'
)
content = content.replace(
    '<p style="font-size: 1.25rem; color: var(--color-text-light); max-width: 600px; margin: 0 auto 3rem;">',
    '<p style="font-size: 1.25rem; color: rgba(255,255,255,0.9); max-width: 600px; margin: 0 auto 3rem;">'
)
# We also need to change ed-eyebrow for the CTA to white
content = content.replace(
    '<span class="ed-eyebrow">Plan Your Event</span>',
    '<span class="ed-eyebrow" style="color: rgba(255,255,255,0.8);">Plan Your Event</span>'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
