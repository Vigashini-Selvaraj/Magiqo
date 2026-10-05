import re

with open('packages.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    # 1. Joyful Moments
    (r'<img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Joyful Moments" class="package-img">',
     r'<img src="assets/images/pro_gallery_alt.jpg" alt="Joyful Moments" class="package-img">'),
     
    # 2. Unlimited/Ultimate Celebration
    (r'<img src="assets/images/hero_magician_1790831867453\.jpg" alt="Ultimate Celebration" class="package-img">',
     r'<img src="assets/images/pro_services_hero.jpg" alt="Ultimate Celebration" class="package-img">'),
     
    # 3. Little Explorers
    (r'<img src="https://images.unsplash\.com/photo-1502086223501-7ea6ecd79368\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Little Explorers" class="package-img">',
     r'<img src="assets/images/pro_memory.jpg" alt="Little Explorers" class="package-img">'),
     
    # 4. Share Details
    (r'<div class="step-img-wrap"><img src="https://images.unsplash\.com/photo-1502086223501-7ea6ecd79368\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Share Details"></div>',
     r'<div class="step-img-wrap"><img src="https://images.unsplash.com/photo-1512428559087-560fa5ceab42?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Share Details"></div>'),
     
    # 5. Confirm
    (r'<div class="step-img-wrap"><img src="https://images.unsplash\.com/photo-1508214751196-bfdd4ca401fc\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=600&q=80" alt="Confirm"></div>',
     r'<div class="step-img-wrap"><img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Confirm"></div>')
]

for old, new in replacements:
    html = re.sub(old, new, html)

# Redesign the comparison section
# We will replace everything from <style> inside "3. Compare the Experience" up to the end of the section.
# Let's find the start of the style block for the comparison section.

compare_start = html.find('<!-- 3. Compare the Experience -->')
if compare_start != -1:
    compare_end = html.find('</section>', compare_start) + 10
    
    new_compare_section = """<!-- 3. Compare the Experience (Redesigned SaaS Table) -->
  <section class="section-pad" style="background: var(--color-bg);">
    <div class="container">
      <div class="sec-title">
        <h2><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Compare</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">the Packages</span></h2>
        <p>A simple side-by-side breakdown so you can choose the perfect fit for your magical day.</p>
      </div>

      <style>
        .pricing-table-wrapper {
          overflow-x: auto;
          box-shadow: 0 15px 35px rgba(0,0,0,0.05);
          border-radius: var(--radius-xl);
          background: var(--color-surface);
          border: 1px solid var(--color-border);
        }
        .pricing-table {
          width: 100%;
          min-width: 800px;
          border-collapse: collapse;
          text-align: center;
        }
        .pricing-table th, .pricing-table td {
          padding: 1.5rem;
          border-bottom: 1px solid var(--color-border);
          border-right: 1px solid var(--color-border);
        }
        .pricing-table th:last-child, .pricing-table td:last-child {
          border-right: none;
        }
        .pricing-table tr:last-child td {
          border-bottom: none;
        }
        .pricing-table thead th {
          background: rgba(46, 25, 167, 0.02);
          position: relative;
        }
        .pricing-table th.popular {
          background: rgba(56, 149, 200, 0.05);
          border-top: 4px solid #3895c8;
        }
        .pkg-name {
          font-family: var(--font-magic);
          font-size: 1.5rem;
          color: var(--color-text);
          margin-bottom: 0.5rem;
        }
        .pkg-price {
          font-size: 1.25rem;
          font-weight: bold;
          color: var(--color-primary);
        }
        .feature-name {
          text-align: left;
          font-weight: bold;
          color: var(--color-text);
          background: rgba(0,0,0,0.01);
          width: 25%;
        }
        .check-icon {
          color: var(--color-primary);
          font-size: 1.25rem;
        }
        .x-icon {
          color: rgba(0,0,0,0.15);
          font-size: 1.25rem;
        }
        .popular-badge {
          position: absolute;
          top: -12px;
          left: 50%;
          transform: translateX(-50%);
          background: #3895c8;
          color: white;
          padding: 4px 12px;
          border-radius: 12px;
          font-size: 0.75rem;
          font-weight: bold;
          text-transform: uppercase;
        }
        .btn-select {
          display: inline-block;
          margin-top: 1rem;
          padding: 0.75rem 1.5rem;
          border-radius: var(--radius-pill);
          text-decoration: none;
          font-weight: bold;
          transition: 0.3s;
          border: 1px solid var(--color-primary);
          color: var(--color-primary);
        }
        .btn-select:hover {
          background: var(--color-primary);
          color: white;
        }
        .btn-select.popular-btn {
          background: #3895c8;
          color: white;
          border-color: #3895c8;
        }
        .btn-select.popular-btn:hover {
          background: #2a739d;
        }
      </style>

      <div class="pricing-table-wrapper">
        <table class="pricing-table">
          <thead>
            <tr>
              <th class="feature-name">Features</th>
              <th>
                <div class="pkg-name">Sparkle</div>
                <div class="pkg-price">$99</div>
              </th>
              <th class="popular">
                <div class="popular-badge">Most Popular</div>
                <div class="pkg-name" style="color:#3895c8;">Magic Adv.</div>
                <div class="pkg-price" style="color:#3895c8;">$149</div>
              </th>
              <th>
                <div class="pkg-name">Fantasy</div>
                <div class="pkg-price">$199</div>
              </th>
              <th>
                <div class="pkg-name">Ultimate</div>
                <div class="pkg-price">$349</div>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="feature-name">Duration</td>
              <td>1 Hour</td>
              <td>1.5 Hours</td>
              <td>2 Hours</td>
              <td>3 Hours</td>
            </tr>
            <tr>
              <td class="feature-name">Entertainers</td>
              <td>1</td>
              <td>1</td>
              <td>2</td>
              <td>3</td>
            </tr>
            <tr>
              <td class="feature-name">Interactive Games</td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
            </tr>
            <tr>
              <td class="feature-name">Live Performance</td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
            </tr>
            <tr>
              <td class="feature-name">Themed Activities</td>
              <td><i class="fa-solid fa-xmark x-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
            </tr>
            <tr>
              <td class="feature-name">Meet & Greet / Photos</td>
              <td><i class="fa-solid fa-xmark x-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
            </tr>
            <tr>
              <td class="feature-name">Magic Gift Box</td>
              <td><i class="fa-solid fa-xmark x-icon"></i></td>
              <td><i class="fa-solid fa-xmark x-icon"></i></td>
              <td><i class="fa-solid fa-xmark x-icon"></i></td>
              <td><i class="fa-solid fa-check check-icon"></i></td>
            </tr>
            <tr>
              <td class="feature-name"></td>
              <td><a href="booking.html" class="btn-select">Select</a></td>
              <td><a href="booking.html" class="btn-select popular-btn">Select</a></td>
              <td><a href="booking.html" class="btn-select">Select</a></td>
              <td><a href="booking.html" class="btn-select">Select</a></td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
  </section>"""
    html = html[:compare_start] + new_compare_section + html[compare_end:]

with open('packages.html', 'w', encoding='utf-8') as f:
    f.write(html)
