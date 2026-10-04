import re

filepath = r'c:\Users\vigas\Desktop\magiqo\blog_detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
old_css_regex = r'\.share-btn \{.*?\n    \}\n    \.share-btn i \{.*?\n    \}'

new_css = '''.share-btn {
      width: 45px;
      height: 45px;
      border-radius: 50%;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      color: var(--color-text) !important;
      font-size: 1.2rem;
      cursor: pointer;
      transition: 0.3s;
      text-decoration: none;
      padding: 0;
      margin: 0;
    }
    .share-btn:hover, .share-btn:hover i {
      background: var(--color-primary) !important;
      color: white !important;
      border-color: var(--color-primary) !important;
      transform: translateY(-3px);
    }
    .share-btn i {
      display: block !important;
      line-height: 1 !important;
      margin: 0 !important;
      padding: 0 !important;
    }'''

content = re.sub(old_css_regex, new_css, content, flags=re.DOTALL)

# Replace HTML
old_html = '''<div class="share-box">
          <a href="#" class="share-btn" title="Share on Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="#" class="share-btn" title="Share on Twitter"><i class="fa-brands fa-twitter"></i></a>
          <a href="#" class="share-btn" title="Share on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          <button class="share-btn" title="Copy Link" onclick="alert('Link copied to clipboard!')"><i class="fa-solid fa-link"></i></button>
        </div>'''
new_html = '''<div class="share-box">
          <button class="share-btn" title="Share on Facebook" onclick="window.open('#','_blank')"><i class="fa-brands fa-facebook-f"></i></button>
          <button class="share-btn" title="Share on Twitter" onclick="window.open('#','_blank')"><i class="fa-brands fa-twitter"></i></button>
          <button class="share-btn" title="Share on WhatsApp" onclick="window.open('#','_blank')"><i class="fa-brands fa-whatsapp"></i></button>
          <button class="share-btn" title="Copy Link" onclick="alert('Link copied to clipboard!')"><i class="fa-solid fa-link"></i></button>
        </div>'''

if old_html in content:
    content = content.replace(old_html, new_html)
else:
    # If the old HTML has different spacing, use regex
    html_regex = r'<div class="share-box">.*?</div>'
    content = re.sub(html_regex, new_html, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
