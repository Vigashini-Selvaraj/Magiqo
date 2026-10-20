import re

with open('service_detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Google Fonts in <head>
google_fonts = """  <!-- Core Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
"""

if "family=Outfit" not in html:
    html = html.replace('<link rel="stylesheet" href="css/style.css">', google_fonts + '  <link rel="stylesheet" href="css/style.css">')

# 2. Update CSS in <style>
# Replace styling of .perfect-card, .sec-title h2, .hero-title, .booking-cta
new_css = """
    body {
      background: var(--color-bg) !important;
      background-color: var(--color-bg) !important;
      color: var(--color-text);
      font-family: var(--font-body);
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }

    .section-pad {
      padding: 6rem 0;
    }

    .sec-title {
      text-align: center;
      margin-bottom: 3.5rem;
    }

    .sec-title h2 {
      font-family: var(--font-magic);
      font-size: clamp(2.5rem, 4vw, 3.5rem);
      font-weight: 800;
      margin-bottom: 1rem;
      color: var(--color-text);
      line-height: 1.2;
    }

    .sec-title p {
      color: var(--color-text-light);
      font-size: 1.15rem;
      max-width: 700px;
      margin: 0 auto;
      line-height: 1.6;
    }

    /* 1. Detail Hero */
    .detail-hero {
      position: relative;
      min-height: 80vh;
      display: flex;
      align-items: center;
      padding-top: 140px;
      padding-bottom: 5rem;
      background: radial-gradient(circle at 10% 20%, rgba(201, 42, 88, 0.08) 0%, transparent 45%),
                  radial-gradient(circle at 90% 80%, rgba(56, 149, 200, 0.08) 0%, transparent 45%),
                  var(--color-surface);
      border-bottom: 1px solid var(--color-border);
      overflow: hidden;
    }

    .hero-container {
      display: flex;
      gap: 4rem;
      align-items: center;
      width: 100%;
      position: relative;
      z-index: 2;
    }

    .hero-text {
      flex: 1;
      max-width: 600px;
    }

    .hero-title {
      font-family: var(--font-magic);
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-weight: 900;
      margin-bottom: 1rem;
      line-height: 1.15;
      color: var(--color-text);
    }

    .hero-subtitle {
      font-size: 1.2rem;
      color: var(--color-text-light);
      margin-bottom: 2rem;
      line-height: 1.7;
    }

    .hero-badges-row {
      display: flex;
      gap: 1rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }

    .hero-badge-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--color-bg);
      padding: 0.5rem 1.25rem;
      border-radius: var(--radius-pill);
      font-weight: 700;
      font-size: 0.9rem;
      border: 1px solid var(--color-border);
      color: var(--color-text);
    }
    .hero-badge-item.pink {
      border-color: rgba(201, 42, 88, 0.3);
      color: var(--color-primary);
      background: rgba(201, 42, 88, 0.06);
    }
    .hero-badge-item.blue {
      border-color: rgba(56, 149, 200, 0.3);
      color: #3895c8;
      background: rgba(56, 149, 200, 0.06);
    }

    .hero-card {
      background: var(--color-bg);
      border: 1px solid var(--color-border);
      box-shadow: 0 10px 30px var(--color-shadow);
      padding: 2rem;
      border-radius: var(--radius-lg);
      margin-top: 2rem;
    }

    .hero-card h4 {
      font-family: var(--font-magic);
      font-size: 1.4rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
      color: var(--color-text);
    }

    .hero-card p {
      font-size: 0.95rem;
      margin-bottom: 1.5rem;
      color: var(--color-text-light);
      line-height: 1.6;
    }

    .hero-img-wrapper {
      flex: 1;
      position: relative;
      display: flex;
      justify-content: center;
    }

    .hero-img-wrapper img {
      width: 100%;
      max-width: 500px;
      height: 480px;
      object-fit: cover;
      border-radius: var(--radius-lg);
      box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
      border: 6px solid var(--color-surface);
      transition: transform 0.5s ease;
    }

    .hero-img-wrapper:hover img {
      transform: scale(1.02);
    }

    /* Feature Cards (What Makes it Magical) */
    .magical-feature-card {
      text-align: center;
      padding: 2.75rem 2rem;
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      box-shadow: 0 10px 25px var(--color-shadow);
      border: 1px solid var(--color-border);
      transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .magical-feature-card:hover {
      transform: translateY(-6px);
      border-color: rgba(201, 42, 88, 0.3);
    }
    .magical-feature-icon {
      width: 70px;
      height: 70px;
      margin: 0 auto 1.5rem;
      background: linear-gradient(135deg, rgba(201, 42, 88, 0.12) 0%, rgba(56, 149, 200, 0.12) 100%);
      border: 1px solid rgba(201, 42, 88, 0.2);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-primary);
      font-size: 1.8rem;
    }
    .magical-feature-card h4 {
      font-size: 1.35rem;
      font-family: var(--font-magic);
      font-weight: 800;
      color: var(--color-text);
      margin-bottom: 0.75rem;
    }
    .magical-feature-card p {
      color: var(--color-text-light);
      line-height: 1.6;
      font-size: 0.95rem;
    }

    /* 4. Timeline */
    .timeline-container {
      position: relative;
      max-width: 900px;
      margin: 0 auto 6rem;
      padding: 2rem 0;
    }
    .timeline-container::before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      width: 3px;
      background: linear-gradient(to bottom, var(--color-primary), #3895c8);
      transform: translateX(-50%);
      opacity: 0.3;
    }
    .timeline-item {
      display: flex;
      justify-content: flex-end;
      padding-right: 50%;
      position: relative;
      margin-bottom: 3.5rem;
      width: 100%;
    }
    .timeline-item:nth-child(even) {
      justify-content: flex-start;
      padding-right: 0;
      padding-left: 50%;
    }
    .timeline-content {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 2.25rem;
      width: 88%;
      box-shadow: 0 10px 30px var(--color-shadow);
      position: relative;
      transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .timeline-item:hover .timeline-content {
      transform: translateY(-4px);
      border-color: var(--color-primary);
    }
    .timeline-content::before {
      content: attr(data-step);
      position: absolute;
      top: 2rem;
      width: 44px;
      height: 44px;
      background: var(--color-primary);
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.2rem;
      font-family: var(--font-magic);
      box-shadow: 0 0 0 6px var(--color-bg);
      z-index: 2;
    }
    .timeline-item:nth-child(odd) .timeline-content::before {
      right: -67px;
    }
    .timeline-item:nth-child(even) .timeline-content::before {
      left: -67px;
    }
    .timeline-content h4 {
      font-size: 1.4rem;
      font-family: var(--font-magic);
      font-weight: 800;
      color: var(--color-text);
      margin-bottom: 0.6rem;
    }
    .timeline-content p {
      color: var(--color-text-light);
      line-height: 1.6;
      font-size: 0.95rem;
    }

    /* 5. What's Included */
    .included-wrapper {
      padding: 5rem 0;
      margin-bottom: 6rem;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
    }
    .included-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 2rem;
      padding: 0 2.5rem;
    }
    .included-card {
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      height: 320px;
      box-shadow: 0 10px 25px var(--color-shadow);
      border: 1px solid var(--color-border);
    }
    .included-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }
    .included-card:hover img {
      transform: scale(1.08);
    }
    .included-overlay {
      position: absolute;
      bottom: 0; left: 0; right: 0;
      background: linear-gradient(to top, rgba(14, 20, 36, 0.92) 0%, transparent 100%);
      padding: 2rem 1.5rem 1.5rem;
      display: flex;
      align-items: flex-end;
    }
    .included-overlay h5 {
      font-size: 1.5rem;
      font-family: var(--font-magic);
      font-weight: 800;
      color: #FFFFFF !important;
      -webkit-text-fill-color: #FFFFFF !important;
      margin: 0;
    }

    /* 6. Perfect For Grid */
    .perfect-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.5rem;
      margin-bottom: 6rem;
    }
    .perfect-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 2.5rem 1.5rem;
      text-align: center;
      box-shadow: 0 10px 25px var(--color-shadow);
      transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .perfect-card:hover {
      transform: translateY(-5px);
      border-color: var(--color-primary);
    }
    .perfect-card h3 {
      font-family: var(--font-magic);
      font-size: 2.4rem;
      font-weight: 900;
      color: var(--color-primary);
      margin-bottom: 0.5rem;
    }
    .perfect-card p {
      font-size: 1rem;
      font-weight: 600;
      color: var(--color-text);
      margin: 0;
    }

    /* 7. Performer Box */
    .performer-box {
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      border: 1px solid var(--color-border);
      box-shadow: 0 15px 40px var(--color-shadow);
      max-width: 1040px;
      margin: 0 auto 6rem;
    }
    .performer-img {
      width: 380px;
      height: 420px;
      object-fit: cover;
      display: block;
    }
    .performer-info {
      padding: 3rem;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .performer-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(46, 204, 113, 0.12);
      color: #2ecc71;
      border: 1px solid rgba(46, 204, 113, 0.3);
      padding: 0.35rem 0.9rem;
      border-radius: var(--radius-pill);
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      width: fit-content;
      margin-bottom: 1rem;
    }

    /* 8. Pricing Grid */
    .pricing-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 2rem;
      align-items: stretch;
      margin-bottom: 6rem;
    }
    .pricing-card {
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      padding: 3rem 2rem;
      text-align: center;
      box-shadow: 0 10px 30px var(--color-shadow);
      border: 1px solid var(--color-border);
      position: relative;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      display: flex;
      flex-direction: column;
    }
    .pricing-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 45px var(--color-shadow);
    }
    .pricing-card.featured {
      border: 2px solid var(--color-primary);
      box-shadow: 0 15px 40px rgba(201, 42, 88, 0.15);
    }
    .pricing-card.featured::before {
      content: 'Most Popular';
      position: absolute;
      top: -15px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--color-primary);
      color: white;
      padding: 0.4rem 1.5rem;
      border-radius: var(--radius-pill);
      font-weight: 700;
      font-size: 0.85rem;
      letter-spacing: 0.5px;
      box-shadow: 0 5px 15px rgba(201, 42, 88, 0.3);
    }
    .price-title {
      font-family: var(--font-magic);
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--color-text);
      margin-bottom: 0.5rem;
    }
    .price-amount {
      font-size: 3rem;
      font-weight: 900;
      font-family: var(--font-magic);
      color: var(--color-primary);
      margin-bottom: 0.25rem;
      line-height: 1;
    }
    .price-duration {
      color: var(--color-text-light);
      margin-bottom: 2rem;
      font-weight: 600;
      font-size: 1rem;
    }
    .price-features {
      list-style: none;
      margin-bottom: 2.5rem;
      text-align: left;
      padding: 0;
      flex-grow: 1;
    }
    .price-features li {
      padding: 0.75rem 0;
      border-bottom: 1px solid var(--color-border);
      color: var(--color-text-light);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 0.95rem;
    }
    .price-features li i {
      color: var(--color-primary);
      font-size: 1rem;
      flex-shrink: 0;
    }

    /* 9. Masonry Gallery */
    .masonry-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-bottom: 6rem;
    }
    .masonry-item {
      border-radius: var(--radius-lg);
      overflow: hidden;
      height: 260px;
      box-shadow: 0 10px 25px var(--color-shadow);
      border: 1px solid var(--color-border);
    }
    .masonry-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }
    .masonry-item:hover img {
      transform: scale(1.06);
    }

    /* 10. Official Booking CTA Banner */
    .cta-banner-section {
      background: linear-gradient(135deg, var(--color-primary) 0%, #8c1e3e 100%);
      padding: 5rem 0;
      border-radius: var(--radius-lg);
      color: white;
      text-align: center;
      margin: 4rem 0;
    }
    .cta-banner-section h2 {
      font-family: var(--font-magic);
      font-size: clamp(2.4rem, 4vw, 3.2rem);
      font-weight: 800;
      color: #FFFFFF !important;
      -webkit-text-fill-color: #FFFFFF !important;
      margin-bottom: 1rem;
    }
    .cta-banner-section p {
      color: rgba(255, 255, 255, 0.92);
      font-size: 1.2rem;
      max-width: 650px;
      margin: 0 auto 2.5rem;
      line-height: 1.6;
    }

    /* Brand text classes */
    .text-pink {
      color: var(--color-primary) !important;
      -webkit-text-fill-color: var(--color-primary) !important;
    }
    .text-blue {
      color: #3895c8 !important;
      -webkit-text-fill-color: #3895c8 !important;
    }

    @media (max-width: 992px) {
      .hero-container { flex-direction: column; text-align: center; }
      .hero-badges-row { justify-content: center; }
      .performer-box { flex-direction: column; text-align: center; }
      .performer-img { width: 100%; height: 350px; }
      .timeline-container::before { left: 20px; }
      .timeline-item, .timeline-item:nth-child(even) {
        padding-left: 50px;
        padding-right: 0;
        justify-content: flex-start;
      }
      .timeline-content { width: 100%; }
      .timeline-content::before, .timeline-item:nth-child(even) .timeline-content::before {
        left: -42px;
        right: auto;
      }
    }
"""

# Replace <style> block
style_pattern = r'<style>.*?</style>'
html = re.sub(style_pattern, f'<style>{new_css}\n  </style>', html, flags=re.DOTALL)

# 3. Update HTML markup in body for brand titles & buttons
# Replace hero title
html = html.replace(
    '<h1 class="hero-title" id="dynamicHeroTitle"><span\n            style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Magical</span> <span\n            style="color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary);">Experience</span></h1>',
    '<h1 class="hero-title" id="dynamicHeroTitle"><span class="text-pink">Magical</span> <span class="text-blue">Experience</span></h1>'
)
html = html.replace(
    '<h1 class="hero-title" id="dynamicHeroTitle"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Magical</span> <span style="color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary);">Experience</span></h1>',
    '<h1 class="hero-title" id="dynamicHeroTitle"><span class="text-pink">Magical</span> <span class="text-blue">Experience</span></h1>'
)

# Replace hero badges
old_hero_badges = """        <div style="display: flex; gap: 1rem; margin-bottom: 2rem;">
          <span
            style="background: var(--color-surface); padding: 0.5rem 1rem; border-radius: var(--radius-pill); font-weight: bold; font-size: 0.9rem; border: 1px solid var(--color-primary); color: var(--color-primary);">From
            $199</span>
          <span
            style="background: var(--color-surface); padding: 0.5rem 1rem; border-radius: var(--radius-pill); font-weight: bold; font-size: 0.9rem; border: 1px solid var(--color-accent); color: var(--color-accent);">45
            - 120 Mins</span>
        </div>"""
new_hero_badges = """        <div class="hero-badges-row">
          <span class="hero-badge-item pink"><i class="fa-solid fa-tag"></i> From $199</span>
          <span class="hero-badge-item blue"><i class="fa-solid fa-clock"></i> 45 - 120 Mins</span>
          <span class="hero-badge-item"><i class="fa-solid fa-shield-halved"></i> 100% DBS Vetted</span>
        </div>"""
html = html.replace(old_hero_badges, new_hero_badges)

# Replace section headings with .text-pink and .text-blue
html = html.replace(
    '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">What Makes It</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Magical?</span></h2>',
    '<h2><span class="text-pink">What Makes It</span> <span class="text-blue">Magical?</span></h2>'
)
html = html.replace(
    '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">The</span> <span\n          style="color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary);">Show Unfolds</span></h2>',
    '<h2><span class="text-pink">The</span> <span class="text-blue">Show Unfolds</span></h2>'
)
html = html.replace(
    '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">What\'s</span>\n          <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Included</span></h2>',
    '<h2><span class="text-pink">What\'s</span> <span class="text-blue">Included</span></h2>'
)
html = html.replace(
    '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Perfect For</span>\n      <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Little Celebrations</span></h2>',
    '<h2><span class="text-pink">Perfect For</span> <span class="text-blue">Little Celebrations</span></h2>'
)
html = html.replace(
    '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Meet</span> <span\n        style="color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary);">Your Performer</span></h2>',
    '<h2><span class="text-pink">Meet</span> <span class="text-blue">Your Performer</span></h2>'
)
html = html.replace(
    '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Choose</span> <span\n        style="color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary);">Your Package</span></h2>',
    '<h2><span class="text-pink">Choose</span> <span class="text-blue">Your Package</span></h2>'
)
html = html.replace(
    '<h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Moments</span> <span\n        style="color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary);">of Magic</span></h2>',
    '<h2><span class="text-pink">Moments</span> <span class="text-blue">of Magic</span></h2>'
)

# Replace "What Makes it Magical" cards to use magical-feature-card with FontAwesome icons
old_magical_cards_pattern = r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\); gap: 2\.5rem; margin-bottom: 7rem;">.*?</div>\s*</div>\s*<!-- 4\. The Show Unfolds'
new_magical_cards = """<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2.5rem; margin-bottom: 7rem;">
      <div class="magical-feature-card">
        <div class="magical-feature-icon">
          <i class="fa-solid fa-star"></i>
        </div>
        <h4>Star of the Show</h4>
        <p>The birthday child is integrated into the climax of the performance, making them feel truly celebrated with their own magic wand.</p>
      </div>
      <div class="magical-feature-card">
        <div class="magical-feature-icon">
          <i class="fa-solid fa-wand-magic-sparkles"></i>
        </div>
        <h4>Fully Immersive</h4>
        <p>We bring our own professional sound systems, backdrops, and lighting for a complete theatrical experience anywhere.</p>
      </div>
      <div class="magical-feature-card">
        <div class="magical-feature-icon">
          <i class="fa-solid fa-heart"></i>
        </div>
        <h4>Adaptable Flow</h4>
        <p>We read the room and seamlessly adjust pacing and comedy to keep every child from toddlers to tweens captivated.</p>
      </div>
    </div>
    <!-- 4. The Show Unfolds"""

html = re.sub(old_magical_cards_pattern, new_magical_cards, html, flags=re.DOTALL)

# Update pricing features checkmarks to FontAwesome
html = re.sub(r'<svg viewBox="0 0 24 24">\s*<path d="M9 16\.2L4\.8 12l-1\.4 1\.4L9 19 21 7l-1\.4-1\.4L9 16\.2z" />\s*</svg>', '<i class="fa-solid fa-circle-check"></i>', html)

# Replace Booking CTA Section with official Magiqo CTA
old_booking_cta_pattern = r'<!-- 10\. Booking CTA -->.*?</div>\s*<!-- Submit Modal -->'
new_booking_cta = """<!-- 10. Official Booking CTA Banner -->
  <section id="booking" class="cta-banner-section">
    <div class="container text-center">
      <h2>Ready to Make Memories?</h2>
      <p>Secure your preferred date with our verified entertainers before calendar slots fill up. Fast, flexible, and fully guaranteed.</p>
      <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;">
        <a href="booking.html" class="btn btn-white btn-lg"><i class="fa-solid fa-calendar-check"></i> Book This Service Now</a>
        <a href="packages.html" class="btn btn-outline-white btn-lg"><i class="fa-solid fa-wand-magic-sparkles"></i> View All Packages</a>
      </div>
    </div>
  </section>

  <!-- Submit Modal -->"""

html = re.sub(old_booking_cta_pattern, new_booking_cta, html, flags=re.DOTALL)

with open('service_detail.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully redesigned service_detail.html UI with Magiqo typography, brand colors, and modern components!")
