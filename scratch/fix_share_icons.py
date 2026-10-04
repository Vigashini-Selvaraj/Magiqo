import re

filepath = r'c:\Users\vigas\Desktop\magiqo\blog_detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Share Buttons
old_share_css = '''.share-btn {
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

new_share_css = '''.share-btn {
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
      padding: 0;
      margin: 0;
      line-height: 1;
    }
    .share-btn i {
      margin: 0;
      padding: 0;
      line-height: 1;
      display: flex;
      align-items: center;
      justify-content: center;
    }'''

content = content.replace(old_share_css, new_share_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
