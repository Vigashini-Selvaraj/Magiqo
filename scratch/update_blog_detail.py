import re

filepath = r'c:\Users\vigas\Desktop\magiqo\blog_detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update font-family for headings
content = content.replace('.blog-title {\n      font-family: var(--font-heading);', '.blog-title {\n      font-family: var(--font-magic);')
content = content.replace('.article-content h2, .article-content h3 {\n      font-family: var(--font-heading);', '.article-content h2, .article-content h3 {\n      font-family: var(--font-magic);')

# 2. Fix the Share Buttons
old_share_css = '''.share-btn {
      width: 45px;
      height: 45px;
      border-radius: 50%;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-text);
      font-size: 1.2rem;
      cursor: pointer;
      transition: 0.3s;
      text-decoration: none;
    }'''
new_share_css = '''.share-btn {
      width: 45px;
      height: 45px;
      border-radius: 50%;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: var(--color-text);
      font-size: 1.2rem;
      cursor: pointer;
      transition: 0.3s;
      text-decoration: none;
      padding: 0;
      line-height: 0;
    }
    .share-btn i {
      display: block;
      margin: auto;
    }'''
content = content.replace(old_share_css, new_share_css)

# 3. Add missing CSS classes for section-title and text-colors
missing_css = '''
    .section-title { font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 40px; color: var(--color-text); }
    .section-title .text-pink { color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none; }
    .section-title .text-blue { color: #3895c8; -webkit-text-fill-color: #3895c8; background: none; }
    .text-pink { color: var(--color-primary) !important; -webkit-text-fill-color: var(--color-primary) !important; }
    .text-blue { color: #3895c8 !important; -webkit-text-fill-color: #3895c8 !important; }
'''
content = content.replace('/* Layout */', missing_css + '\n    /* Layout */')

# 4. Format "More Magic in Your Inbox"
old_newsletter_h2 = '<h2 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 15px; color: var(--color-text);">More Magic in Your Inbox</h2>'
new_newsletter_h2 = '<h2 class="section-title" style="margin-bottom: 15px;"><span class="text-pink">More Magic</span> <span class="text-blue">in Your Inbox</span></h2>'
content = content.replace(old_newsletter_h2, new_newsletter_h2)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
