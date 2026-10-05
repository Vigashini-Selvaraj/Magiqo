import re

with open('packages.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = "<!-- COMPARE (Magical Cards) -->"
end_marker = "</section>"

start_idx = html.find(start_marker)
if start_idx != -1:
    end_idx = html.find(end_marker, start_idx) + len(end_marker)
    
    new_compare = """<!-- COMPARE (Interactive Accordion) -->
    <section class="container" style="background: var(--color-surface); padding: 4rem 2rem; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); margin-bottom: 4rem;">
      <h2 class="section-title reveal"><span class="text-pink">Compare</span> <span class="text-blue">the experiences</span></h2>
      <p class="reveal" style="text-align: center; color: var(--color-text-light); max-width: 600px; margin: 0 auto; margin-bottom: 3rem;">Click on a package below to reveal its magical features and find the perfect fit for your celebration.</p>
      
      <style>
        .accordion-container {
          max-width: 800px;
          margin: 0 auto;
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }
        .accordion-item {
          background: var(--color-bg);
          border: 1px solid var(--color-border);
          border-radius: var(--radius-lg);
          overflow: hidden;
          transition: all 0.3s ease;
        }
        .accordion-item.active {
          border-color: var(--color-primary);
          box-shadow: 0 10px 30px rgba(46, 25, 167, 0.1);
        }
        .accordion-item.popular {
          border-color: #3895c8;
        }
        .accordion-item.popular.active {
          box-shadow: 0 10px 30px rgba(56, 149, 200, 0.15);
        }
        .accordion-header {
          padding: 1.5rem 2rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          cursor: pointer;
          background: var(--color-surface);
          transition: background 0.3s;
        }
        .accordion-header:hover {
          background: rgba(0,0,0,0.02);
        }
        .accordion-title-wrap {
          display: flex;
          align-items: center;
          gap: 1rem;
        }
        .accordion-icon {
          font-size: 1.75rem;
          color: var(--color-primary);
        }
        .accordion-item.popular .accordion-icon {
          color: #3895c8;
        }
        .accordion-title {
          font-family: var(--font-magic);
          font-size: 1.5rem;
          color: var(--color-text);
          margin: 0;
        }
        .accordion-price-wrap {
          display: flex;
          align-items: center;
          gap: 1.5rem;
        }
        .accordion-price {
          font-size: 1.25rem;
          font-weight: bold;
          color: var(--color-text-light);
        }
        .accordion-item.active .accordion-price {
          color: var(--color-primary);
        }
        .accordion-item.popular.active .accordion-price {
          color: #3895c8;
        }
        .accordion-toggle {
          font-size: 1.25rem;
          color: var(--color-text-light);
          transition: transform 0.3s;
        }
        .accordion-item.active .accordion-toggle {
          transform: rotate(180deg);
          color: var(--color-primary);
        }
        .accordion-content {
          max-height: 0;
          overflow: hidden;
          transition: max-height 0.4s ease, padding 0.4s ease;
          background: var(--color-bg);
        }
        .accordion-item.active .accordion-content {
          max-height: 500px;
          padding: 2rem;
          border-top: 1px solid var(--color-border);
        }
        .features-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
          gap: 1.5rem;
        }
        .feature-item {
          display: flex;
          align-items: center;
          gap: 0.75rem;
          color: var(--color-text-light);
        }
        .feature-item i {
          color: var(--color-primary);
        }
        .accordion-item.popular .feature-item i {
          color: #3895c8;
        }
        .feature-item.unavailable {
          color: rgba(0,0,0,0.3);
        }
        .feature-item.unavailable i {
          color: rgba(0,0,0,0.2);
        }
        .accordion-action {
          margin-top: 2rem;
          text-align: right;
        }
        .popular-badge {
          background: linear-gradient(90deg, #3895c8, #5bb4e5);
          color: white;
          padding: 4px 12px;
          border-radius: 12px;
          font-size: 0.75rem;
          font-weight: bold;
          text-transform: uppercase;
          margin-right: 1rem;
        }
      </style>

      <div class="accordion-container">
        
        <!-- Sparkle -->
        <div class="accordion-item active" onclick="toggleAccordion(this)">
          <div class="accordion-header">
            <div class="accordion-title-wrap">
              <i class="fa-solid fa-wand-magic-sparkles accordion-icon"></i>
              <h3 class="accordion-title">Sparkle Party</h3>
            </div>
            <div class="accordion-price-wrap">
              <span class="accordion-price">$99</span>
              <i class="fa-solid fa-chevron-down accordion-toggle"></i>
            </div>
          </div>
          <div class="accordion-content">
            <div class="features-grid">
              <div class="feature-item"><i class="fa-solid fa-clock"></i> 1 Hour Duration</div>
              <div class="feature-item"><i class="fa-solid fa-user"></i> 1 Entertainer</div>
              <div class="feature-item"><i class="fa-solid fa-star"></i> Interactive Games</div>
              <div class="feature-item"><i class="fa-solid fa-music"></i> Live Performance</div>
              <div class="feature-item unavailable"><i class="fa-solid fa-xmark"></i> Themed Activities</div>
              <div class="feature-item unavailable"><i class="fa-solid fa-xmark"></i> Meet & Greet</div>
            </div>
            <div class="accordion-action">
              <a href="booking.html" class="btn btn-primary" style="padding: 0.75rem 2rem;">Select Sparkle</a>
            </div>
          </div>
        </div>

        <!-- Magic Adv -->
        <div class="accordion-item popular" onclick="toggleAccordion(this)">
          <div class="accordion-header">
            <div class="accordion-title-wrap">
              <i class="fa-solid fa-hat-wizard accordion-icon"></i>
              <h3 class="accordion-title">Magic Adventure</h3>
            </div>
            <div class="accordion-price-wrap">
              <span class="popular-badge">Most Popular</span>
              <span class="accordion-price">$149</span>
              <i class="fa-solid fa-chevron-down accordion-toggle"></i>
            </div>
          </div>
          <div class="accordion-content">
            <div class="features-grid">
              <div class="feature-item"><i class="fa-solid fa-clock"></i> 1.5 Hours Duration</div>
              <div class="feature-item"><i class="fa-solid fa-user"></i> 1 Entertainer</div>
              <div class="feature-item"><i class="fa-solid fa-star"></i> Interactive Games</div>
              <div class="feature-item"><i class="fa-solid fa-music"></i> Live Performance</div>
              <div class="feature-item"><i class="fa-solid fa-masks-theater"></i> Themed Activities</div>
              <div class="feature-item"><i class="fa-solid fa-camera"></i> Meet & Greet</div>
            </div>
            <div class="accordion-action">
              <a href="booking.html" class="btn btn-primary" style="background: #3895c8; border-color: #3895c8; padding: 0.75rem 2rem;">Select Magic Adv.</a>
            </div>
          </div>
        </div>

        <!-- Fantasy -->
        <div class="accordion-item" onclick="toggleAccordion(this)">
          <div class="accordion-header">
            <div class="accordion-title-wrap">
              <i class="fa-solid fa-crown accordion-icon"></i>
              <h3 class="accordion-title">Fantasy World</h3>
            </div>
            <div class="accordion-price-wrap">
              <span class="accordion-price">$199</span>
              <i class="fa-solid fa-chevron-down accordion-toggle"></i>
            </div>
          </div>
          <div class="accordion-content">
            <div class="features-grid">
              <div class="feature-item"><i class="fa-solid fa-clock"></i> 2 Hours Duration</div>
              <div class="feature-item"><i class="fa-solid fa-user-group"></i> 2 Entertainers</div>
              <div class="feature-item"><i class="fa-solid fa-star"></i> Interactive Games</div>
              <div class="feature-item"><i class="fa-solid fa-music"></i> Live Performance</div>
              <div class="feature-item"><i class="fa-solid fa-masks-theater"></i> Themed Activities</div>
              <div class="feature-item"><i class="fa-solid fa-camera"></i> Meet & Greet</div>
            </div>
            <div class="accordion-action">
              <a href="booking.html" class="btn btn-primary" style="padding: 0.75rem 2rem;">Select Fantasy</a>
            </div>
          </div>
        </div>

        <!-- Ultimate -->
        <div class="accordion-item" onclick="toggleAccordion(this)">
          <div class="accordion-header">
            <div class="accordion-title-wrap">
              <i class="fa-solid fa-gem accordion-icon"></i>
              <h3 class="accordion-title">Ultimate Celebration</h3>
            </div>
            <div class="accordion-price-wrap">
              <span class="accordion-price">$349</span>
              <i class="fa-solid fa-chevron-down accordion-toggle"></i>
            </div>
          </div>
          <div class="accordion-content">
            <div class="features-grid">
              <div class="feature-item"><i class="fa-solid fa-clock"></i> 3 Hours Duration</div>
              <div class="feature-item"><i class="fa-solid fa-users"></i> 3 Entertainers</div>
              <div class="feature-item"><i class="fa-solid fa-star"></i> Interactive Games</div>
              <div class="feature-item"><i class="fa-solid fa-music"></i> Live Performance</div>
              <div class="feature-item"><i class="fa-solid fa-masks-theater"></i> Themed Activities</div>
              <div class="feature-item"><i class="fa-solid fa-gift"></i> Magic Gift Box</div>
            </div>
            <div class="accordion-action">
              <a href="booking.html" class="btn btn-primary" style="padding: 0.75rem 2rem;">Select Ultimate</a>
            </div>
          </div>
        </div>

      </div>

      <script>
        function toggleAccordion(element) {
          // Optional: Close all other accordions
          const accordions = document.querySelectorAll('.accordion-item');
          accordions.forEach(acc => {
            if (acc !== element) acc.classList.remove('active');
          });
          
          // Toggle current
          element.classList.toggle('active');
        }
      </script>
    </section>"""
    html = html[:start_idx] + new_compare + html[end_idx:]

with open('packages.html', 'w', encoding='utf-8') as f:
    f.write(html)
