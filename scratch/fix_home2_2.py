import re

with open('c:/Users/vigas/Desktop/magiqo/home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update View Profile links to entertainer_detail.html?id=...
# We know the HTML structure has Elias, then Mia, then Barnaby.
# We can use regex to replace them one by one.
occurrences = [m.start() for m in re.finditer(r'href="entertainer_detail\.html"', content)]
if len(occurrences) >= 3:
    content = content[:occurrences[0]] + 'href="entertainer_detail.html?id=elias"' + content[occurrences[0] + len('href="entertainer_detail.html"'):]
    occurrences = [m.start() for m in re.finditer(r'href="entertainer_detail\.html"', content)]
    if len(occurrences) >= 2:
        content = content[:occurrences[1]] + 'href="entertainer_detail.html?id=mia"' + content[occurrences[1] + len('href="entertainer_detail.html"'):]
        occurrences = [m.start() for m in re.finditer(r'href="entertainer_detail\.html"', content)]
        if len(occurrences) >= 1:
            content = content[:occurrences[2]] + 'href="entertainer_detail.html?id=barnaby"' + content[occurrences[2] + len('href="entertainer_detail.html"'):]


# 2. Fix Flip Card CSS (gradient color and going down issue)
old_flip_css = """
    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
      cursor: pointer;
    }
    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }
    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border-radius: var(--radius-lg);
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      box-shadow: 0 10px 20px var(--color-shadow);
    }
    .flip-card-front {
      background-color: var(--color-surface);
      color: var(--color-text);
      background-size: cover;
      background-position: center;
      position: relative;
    }
    /* Add an overlay to the front so text is readable over the image */
    .flip-card-front::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.6);
      border-radius: var(--radius-lg);
      z-index: 1;
    }
    .flip-card-front > * {
      position: relative;
      z-index: 2;
    }
    .flip-card-back {
      background: linear-gradient(135deg, var(--color-primary), #3895c8);
      color: white;
      transform: rotateY(180deg);
    }"""

new_flip_css = """
    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s cubic-bezier(0.4, 0.2, 0.2, 1);
      transform-style: preserve-3d;
      cursor: pointer;
      transform-origin: center center;
    }
    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg) translateZ(0);
    }
    .flip-card-front, .flip-card-back {
      position: absolute;
      top: 0; left: 0;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border-radius: var(--radius-lg);
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      box-shadow: 0 10px 20px var(--color-shadow);
      margin: 0;
    }
    .flip-card-front {
      background-color: var(--color-surface);
      color: var(--color-text);
      background-size: cover;
      background-position: center;
      position: absolute;
      z-index: 2;
    }
    /* Add an overlay to the front so text is readable over the image */
    .flip-card-front::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.6);
      border-radius: var(--radius-lg);
      z-index: 1;
    }
    .flip-card-front > * {
      position: relative;
      z-index: 2;
    }
    .flip-card-back {
      background: #8e44ad; /* Changed to solid premium purple instead of the gradient */
      color: white;
      transform: rotateY(180deg);
    }"""

content = content.replace(old_flip_css, new_flip_css)


# 3. Update the CTA background, heading color, and paragraph visibility
old_cta_start = """  <!-- 10. Let the Magic Begin (Royal Background CTA) -->
  <section class="royal-cta" style="padding: 8rem 0; text-align: center; background: #1F1033; position: relative; overflow: hidden;">"""
new_cta_start = """  <!-- 10. Let the Magic Begin (Premium Background CTA) -->
  <section class="royal-cta" style="padding: 8rem 0; text-align: center; background: linear-gradient(135deg, #2b113a, #11081a); position: relative; overflow: hidden;">"""
content = content.replace(old_cta_start, new_cta_start)

old_cta_h2 = """<h2 style="background: none !important; -webkit-text-fill-color: #E5C158 !important; color: #E5C158 !important; text-shadow: 0 4px 15px rgba(229, 193, 88, 0.4); font-family: var(--font-magic); font-size: clamp(3rem, 5vw, 4.5rem);">Let the Magic Begin</h2>"""
new_cta_h2 = """<h2 style="background: none !important; -webkit-text-fill-color: #FFFFFF !important; color: #FFFFFF !important; text-shadow: 0 4px 15px rgba(255, 255, 255, 0.4); font-family: var(--font-magic); font-size: clamp(3rem, 5vw, 4.5rem); position: relative; z-index: 2;">Let the Magic Begin</h2>"""
content = content.replace(old_cta_h2, new_cta_h2)

old_cta_p = """<p style="font-size: 1.25rem; max-width: 600px; margin: 0 auto 3rem; line-height: 1.6;">
        Secure your child's favorite entertainer before our calendar fills up completely. Let's create an unforgettable celebration together.
      </p>"""
new_cta_p = """<p style="font-size: 1.25rem; max-width: 600px; margin: 0 auto 3rem; line-height: 1.6; color: rgba(255,255,255,0.9) !important; position: relative; z-index: 2;">
        Secure your child's favorite entertainer before our calendar fills up completely. Let's create an unforgettable celebration together.
      </p>"""
content = content.replace(old_cta_p, new_cta_p)

with open('c:/Users/vigas/Desktop/magiqo/home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
