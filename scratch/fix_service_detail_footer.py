import re

def fix_service_detail():
    file_path = r'c:\Users\vigas\Desktop\magiqo\service_detail.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS for CTA Section & button
    old_cta_css = '''    /* 10. Official Booking CTA Banner */
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
    }'''

    new_cta_css = '''    /* 10. Official Booking CTA (Full-Width Brand Section) */
    .cta-section {
      background: linear-gradient(135deg, var(--color-primary) 0%, #8c1e3e 100%);
      padding: 6rem 0;
      color: white;
      text-align: center;
      width: 100%;
      position: relative;
    }
    .cta-section h2 {
      font-family: var(--font-magic);
      font-size: clamp(2.4rem, 4.5vw, 3.5rem);
      font-weight: 800;
      color: #FFFFFF !important;
      -webkit-text-fill-color: #FFFFFF !important;
      margin-bottom: 1rem;
    }
    .cta-section p {
      color: rgba(255, 255, 255, 0.92);
      font-size: 1.25rem;
      max-width: 650px;
      margin: 0 auto 2.5rem;
      line-height: 1.7;
    }
    .btn-outline-white {
      background: transparent;
      color: white;
      border: 2px solid rgba(255, 255, 255, 0.85);
      border-radius: var(--radius-pill);
      padding: 0.85rem 2.2rem;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.3s ease;
    }
    .btn-outline-white:hover {
      background: white;
      color: var(--color-primary);
      border-color: white;
      transform: translateY(-2px);
    }'''

    if old_cta_css in content:
        content = content.replace(old_cta_css, new_cta_css)
    else:
        print("Note: old_cta_css exact match not found, checking regex replacement")
        content = re.sub(
            r'/\* 10\. Official Booking CTA Banner \*/\s*\.cta-banner-section\s*\{.*?\.cta-banner-section p\s*\{.*?\}',
            new_cta_css,
            content,
            flags=re.DOTALL
        )

    # 2. Fix the HTML structure after masonry-gallery:
    # Close .container.section-pad
    # Replace CTA banner & remove submitModal
    old_bottom_pattern = re.compile(
        r'(\s*<div class="masonry-item"><img src="assets/images/service_face_painting\.jpg" alt="Colorful Face Painting"></div>\s*</div>)'
        r'(.*?)(<div id="footer"></div>)',
        re.DOTALL
    )

    new_bottom_html = r'''\1
  </div> <!-- /container.section-pad -->

  <!-- 10. Official Booking CTA Banner (Full-Width) -->
  <section id="booking" class="cta-section">
    <div class="container text-center">
      <h2>Ready to Make Memories?</h2>
      <p>Secure your preferred date with our verified entertainers before calendar slots fill up. Fast, flexible, and fully guaranteed.</p>
      <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;">
        <a href="booking.html" class="btn btn-white btn-lg"><i class="fa-solid fa-calendar-check"></i> Book This Service Now</a>
        <a href="packages.html" class="btn btn-outline-white btn-lg"><i class="fa-solid fa-wand-magic-sparkles"></i> View All Packages</a>
      </div>
    </div>
  </section>

  <!-- Dynamic Footer (Full-Width, Unconstrained) -->
  \3'''

    content = old_bottom_pattern.sub(new_bottom_html, content)

    # 3. Remove obsolete modal script
    content = re.sub(
        r'\s*// Modal button wiring\s*const modalBtn = document\.getElementById\(\'modalEntertainerBtn\'\);.*?modalBtn\.href = "entertainer_detail\.html";\s*\}\s*\}',
        '',
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated service_detail.html: closed container, eliminated unstyled modal, and restored full-width footer alignment!")

if __name__ == '__main__':
    fix_service_detail()
