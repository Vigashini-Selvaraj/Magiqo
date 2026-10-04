import re

filepath = r'c:\Users\vigas\Desktop\magiqo\join.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Career Opportunities
content = content.replace(
    '<h2 class="section-title"><span class="text-pink">Career</span> Opportunities</h2>',
    '<h2 class="section-title"><span class="text-pink">Career</span> <span class="text-blue">Opportunities</span></h2>'
)

# 2. Application Process
content = content.replace(
    '<h2 class="section-title">The <span class="text-blue">Application</span> Process</h2>',
    '<h2 class="section-title">The <span class="text-pink">Application</span> <span class="text-blue">Process</span></h2>'
)

# 3. Life at Magiqo
content = content.replace(
    '<h2 class="section-title">Life at <span class="text-blue">Magiqo</span></h2>',
    '<h2 class="section-title"><span class="text-pink">Life at</span> <span class="text-blue">Magiqo</span></h2>'
)

# 4. Career FAQs
content = content.replace(
    '<h2 class="section-title">Career <span class="text-pink">FAQs</span></h2>',
    '<h2 class="section-title"><span class="text-pink">Career</span> <span class="text-blue">FAQs</span></h2>'
)

# 5. Ready to start your journey
content = content.replace(
    '<h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 20px; color: #ffffff !important;">Ready to start your journey?</h2>',
    '<h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 20px; color: #ffffff !important; -webkit-text-fill-color: #ffffff !important;">Ready to start your journey?</h2>'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
