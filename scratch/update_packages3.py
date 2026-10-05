import re

with open('packages.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the compare section
start_marker = "<!-- COMPARE -->"
end_marker = "</section>"

start_idx = html.find(start_marker)
if start_idx != -1:
    # Find the matching closing section tag for COMPARE
    # Since there are multiple </section> tags, we find the first one after the COMPARE section content ends.
    # The COMPARE section starts at 601, we want the </section> after it.
    end_idx = html.find(end_marker, start_idx) + len(end_marker)
    
    new_compare = """<!-- COMPARE (Magical Cards) -->
    <section class="container" style="background: var(--color-surface); padding: 4rem 2rem; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); margin-bottom: 4rem;">
      <h2 class="section-title reveal"><span class="text-pink">Compare</span> <span class="text-blue">the experiences</span></h2>
      <p class="reveal" style="text-align: center; color: var(--color-text-light); max-width: 600px; margin: 0 auto;">Review our carefully crafted packages side-by-side to find the perfect magical experience for your upcoming celebration.</p>
      
      <style>
        .magical-cards-container {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
          gap: 2rem;
          margin-top: 3rem;
        }
        .magic-card {
          background: var(--color-bg);
          border-radius: var(--radius-xl);
          padding: 3rem 2rem;
          text-align: center;
          box-shadow: 0 15px 35px rgba(0,0,0,0.05);
          border: 1px solid var(--color-border);
          position: relative;
          transition: all 0.4s ease;
          overflow: hidden;
        }
        .magic-card:hover {
          transform: translateY(-15px);
          box-shadow: 0 25px 50px rgba(46, 25, 167, 0.15);
          border-color: var(--color-primary);
        }
        .magic-card.popular {
          border-color: #3895c8;
          box-shadow: 0 15px 35px rgba(56, 149, 200, 0.15);
        }
        .magic-card.popular::before {
          content: 'Most Magical';
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          background: linear-gradient(90deg, #3895c8, #5bb4e5);
          color: white;
          padding: 8px 0;
          font-weight: bold;
          font-size: 0.85rem;
          text-transform: uppercase;
          letter-spacing: 2px;
        }
        .magic-card-icon {
          font-size: 3rem;
          color: var(--color-primary);
          margin-bottom: 1.5rem;
        }
        .magic-card.popular .magic-card-icon {
          color: #3895c8;
        }
        .magic-card h3 {
          font-family: var(--font-magic);
          font-size: 2rem;
          margin-bottom: 0.5rem;
          color: var(--color-text);
        }
        .magic-card .price {
          font-size: 1.5rem;
          font-weight: bold;
          color: var(--color-primary);
          margin-bottom: 2rem;
        }
        .magic-card.popular .price {
          color: #3895c8;
        }
        .magic-features {
          list-style: none;
          padding: 0;
          margin: 0 0 2.5rem 0;
          text-align: left;
        }
        .magic-features li {
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-bottom: 1rem;
          color: var(--color-text-light);
          font-size: 1.05rem;
        }
        .magic-features li i {
          color: var(--color-primary);
          font-size: 1.25rem;
        }
        .magic-card.popular .magic-features li i {
          color: #3895c8;
        }
        .magic-features li.unavailable {
          color: rgba(0,0,0,0.3);
        }
        .magic-features li.unavailable i {
          color: rgba(0,0,0,0.2);
        }
        .magic-btn {
          display: inline-block;
          width: 100%;
          padding: 1rem;
          border-radius: var(--radius-pill);
          font-weight: bold;
          text-decoration: none;
          background: rgba(46, 25, 167, 0.05);
          color: var(--color-primary);
          transition: all 0.3s;
        }
        .magic-btn:hover {
          background: var(--color-primary);
          color: white;
        }
        .magic-card.popular .magic-btn {
          background: #3895c8;
          color: white;
        }
        .magic-card.popular .magic-btn:hover {
          background: #2a739d;
        }
      </style>

      <div class="magical-cards-container">
        <!-- Sparkle Card -->
        <div class="magic-card">
          <div class="magic-card-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
          <h3>Sparkle</h3>
          <div class="price">$99</div>
          <ul class="magic-features">
            <li><i class="fa-solid fa-clock"></i> 1 Hour Duration</li>
            <li><i class="fa-solid fa-user"></i> 1 Entertainer</li>
            <li><i class="fa-solid fa-star"></i> Interactive Games</li>
            <li><i class="fa-solid fa-music"></i> Live Performance</li>
            <li class="unavailable"><i class="fa-solid fa-xmark"></i> Themed Activities</li>
            <li class="unavailable"><i class="fa-solid fa-xmark"></i> Meet & Greet</li>
          </ul>
          <a href="booking.html" class="magic-btn">Select Sparkle</a>
        </div>

        <!-- Magic Adv Card -->
        <div class="magic-card popular">
          <div class="magic-card-icon" style="margin-top: 15px;"><i class="fa-solid fa-hat-wizard"></i></div>
          <h3>Magic Adv.</h3>
          <div class="price">$149</div>
          <ul class="magic-features">
            <li><i class="fa-solid fa-clock"></i> 1.5 Hours Duration</li>
            <li><i class="fa-solid fa-user"></i> 1 Entertainer</li>
            <li><i class="fa-solid fa-star"></i> Interactive Games</li>
            <li><i class="fa-solid fa-music"></i> Live Performance</li>
            <li><i class="fa-solid fa-masks-theater"></i> Themed Activities</li>
            <li><i class="fa-solid fa-camera"></i> Meet & Greet</li>
          </ul>
          <a href="booking.html" class="magic-btn">Select Magic Adv.</a>
        </div>

        <!-- Fantasy Card -->
        <div class="magic-card">
          <div class="magic-card-icon"><i class="fa-solid fa-crown"></i></div>
          <h3>Fantasy</h3>
          <div class="price">$199</div>
          <ul class="magic-features">
            <li><i class="fa-solid fa-clock"></i> 2 Hours Duration</li>
            <li><i class="fa-solid fa-user-group"></i> 2 Entertainers</li>
            <li><i class="fa-solid fa-star"></i> Interactive Games</li>
            <li><i class="fa-solid fa-music"></i> Live Performance</li>
            <li><i class="fa-solid fa-masks-theater"></i> Themed Activities</li>
            <li><i class="fa-solid fa-camera"></i> Meet & Greet</li>
          </ul>
          <a href="booking.html" class="magic-btn">Select Fantasy</a>
        </div>

        <!-- Ultimate Card -->
        <div class="magic-card">
          <div class="magic-card-icon"><i class="fa-solid fa-gem"></i></div>
          <h3>Ultimate</h3>
          <div class="price">$349</div>
          <ul class="magic-features">
            <li><i class="fa-solid fa-clock"></i> 3 Hours Duration</li>
            <li><i class="fa-solid fa-users"></i> 3 Entertainers</li>
            <li><i class="fa-solid fa-star"></i> Interactive Games</li>
            <li><i class="fa-solid fa-music"></i> Live Performance</li>
            <li><i class="fa-solid fa-masks-theater"></i> Themed Activities</li>
            <li><i class="fa-solid fa-gift"></i> Magic Gift Box</li>
          </ul>
          <a href="booking.html" class="magic-btn">Select Ultimate</a>
        </div>
      </div>
    </section>"""
    html = html[:start_idx] + new_compare + html[end_idx:]

with open('packages.html', 'w', encoding='utf-8') as f:
    f.write(html)
