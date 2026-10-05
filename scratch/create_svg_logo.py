import re

with open('components/navbar.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_logo_pattern = r'<a href="index\.html" class="logo" style="text-decoration: none; display: flex; align-items: center; gap: 8px;">.*?</a>'

new_logo = '''<a href="index.html" class="logo" style="text-decoration: none; display: flex; align-items: center; gap: 10px;">
      <svg width="45" height="45" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="magiqoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#D24B76" />
            <stop offset="100%" stop-color="#3895c8" />
          </linearGradient>
        </defs>
        
        <!-- Sparkle -->
        <path d="M 60 5 Q 60 25 80 25 Q 60 25 60 45 Q 60 25 40 25 Q 60 25 60 5 Z" fill="#D24B76" />
        
        <!-- Modern M -->
        <path d="M 20 110 L 20 65 A 15 15 0 0 1 50 65 L 60 85 L 70 65 A 15 15 0 0 1 100 65 L 100 110" 
              fill="none" 
              stroke="url(#magiqoGrad)" 
              stroke-width="14" 
              stroke-linecap="round" 
              stroke-linejoin="round" />
      </svg>
      <span style="font-family: var(--font-heading); font-size: 1.8rem; color: var(--color-text); font-weight: 700; letter-spacing: -0.5px; line-height: 1;">Magiqo</span>
    </a>'''

html = re.sub(old_logo_pattern, new_logo, html, flags=re.DOTALL)

with open('components/navbar.html', 'w', encoding='utf-8') as f:
    f.write(html)
