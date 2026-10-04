import re

filepath = r'c:\Users\vigas\Desktop\magiqo\blog.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
old_css = '''    /* 1. Blog Hero */
    .blog-hero {
      padding: 180px 20px 100px;
      text-align: center;
      background: linear-gradient(rgba(19, 49, 92, 0.8), rgba(19, 49, 92, 0.9)), url('assets/images/magic_show_party_1790842468826.jpg') center/cover no-repeat;
      position: relative;
      overflow: hidden;
      color: white;
    }
    .blog-hero h1 {
      font-family: var(--font-magic);
      font-size: clamp(3rem, 5vw, 5rem);
      margin-bottom: 20px;
      position: relative;
      z-index: 2;
    }
    .blog-hero h1 .gradient-text {
      background: linear-gradient(90deg, #ff8fa3, #7addff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .blog-hero p {
      font-size: 1.2rem;
      color: #e0e0e0;
      max-width: 600px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }'''

new_css = '''    /* 1. Blog Hero */
    .blog-hero {
      padding: 180px 20px 100px;
      text-align: center;
      background: var(--color-bg);
      position: relative;
      overflow: hidden;
    }
    .blog-hero::before {
      content: '';
      position: absolute;
      top: -20%; left: -10%;
      width: 50%; height: 50%;
      background: radial-gradient(circle, rgba(210,75,118,0.15) 0%, transparent 70%);
      z-index: 0;
    }
    .blog-hero::after {
      content: '';
      position: absolute;
      bottom: -20%; right: -10%;
      width: 50%; height: 50%;
      background: radial-gradient(circle, rgba(56,149,200,0.15) 0%, transparent 70%);
      z-index: 0;
    }
    .blog-hero h1 {
      font-family: var(--font-magic);
      font-size: clamp(3rem, 5vw, 5rem);
      margin-bottom: 20px;
      position: relative;
      z-index: 2;
      color: var(--color-text);
    }
    .blog-hero h1 .gradient-text {
      background: linear-gradient(90deg, var(--color-primary), #3895c8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .blog-hero p {
      font-size: 1.2rem;
      color: var(--color-text-light);
      max-width: 600px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }'''

content = content.replace(old_css, new_css)

# 2. Update HTML inline style for Celebration Magical text
old_html = '<h1><span class="gradient-text">Ideas That Make Every</span> <br><span style="color: #7addff;">Celebration Magical</span></h1>'
new_html = '<h1><span class="gradient-text">Ideas That Make Every</span> <br><span style="color: #3895c8;">Celebration Magical</span></h1>'
content = content.replace(old_html, new_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
