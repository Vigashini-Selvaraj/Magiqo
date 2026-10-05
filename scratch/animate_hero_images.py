import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add animation styles to the <style> block of the split hero
style_insert_idx = html.find('</style>', html.find('<style>', html.find('<header class="hero-split"')))
if style_insert_idx != -1:
    animations = """
      .bento-img-1 { animation: floatBento 6s ease-in-out infinite; }
      .bento-img-2 { animation: floatBento 7s ease-in-out infinite 1s; }
      .bento-img-3 { animation: floatBento 8s ease-in-out infinite 2s; }
      
      @keyframes floatBento {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
      }
"""
    html = html[:style_insert_idx] + animations + html[style_insert_idx:]

    # Add the classes to the image wrapper divs
    # 1. Large Left Image
    html = html.replace(
        '<div style="grid-row: 1 / span 2; border-radius: 30px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.15);">',
        '<div class="bento-img-1" style="grid-row: 1 / span 2; border-radius: 30px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.15);">'
    )
    # 2. Top Right Image
    html = html.replace(
        '<div style="border-radius: 30px; overflow: hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">\n          <img src="assets/images/pro_princess.jpg"',
        '<div class="bento-img-2" style="border-radius: 30px; overflow: hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">\n          <img src="assets/images/pro_princess.jpg"'
    )
    # 3. Bottom Right Image
    html = html.replace(
        '<div style="border-radius: 30px; overflow: hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">\n          <img src="assets/images/pro_silly_clown.jpg"',
        '<div class="bento-img-3" style="border-radius: 30px; overflow: hidden; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">\n          <img src="assets/images/pro_silly_clown.jpg"'
    )
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added animations to the bento images.")
else:
    print("Could not find the style block in the split hero.")
