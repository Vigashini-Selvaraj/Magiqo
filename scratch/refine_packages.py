packages_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Party Packages | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* Custom Packages Styles using strict Magiqo variables */
    .packages-hero {
      padding: 160px 0 80px;
      background-color: var(--color-bg);
      position: relative;
    }
    .hero-container {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 30px;
    }
    .hero-text-side { flex: 1; max-width: 600px; text-align: left; }
    .hero-img-side { flex: 1; display: flex; justify-content: flex-end; }
    
    .hero-main-img {
      width: 100%; max-width: 550px;
      border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
      border: 8px solid var(--color-surface);
      box-shadow: 0 20px 40px var(--color-shadow);
      object-fit: cover; height: 500px;
      animation: morph 8s ease-in-out infinite;
    }
    @keyframes morph {
      0% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; }
      50% { border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%; }
      100% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; }
    }

    .packages-hero h1 {
      font-size: clamp(3.5rem, 5vw, 5rem);
      font-family: var(--font-magic);
      line-height: 1.1;
      margin: 0 0 30px 0;
    }
    .text-pink { color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none; }
    .text-blue { color: var(--color-secondary); -webkit-text-fill-color: var(--color-secondary); background: none; }
    
    .packages-hero p {
      max-width: 650px;
      margin: 0 0 30px 0;
      font-size: 1.15rem;
      color: var(--color-text-light);
      line-height: 1.6;
    }
    
    .filter-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      margin: 50px 0;
    }
    .filter-btn {
      padding: 12px 25px;
      border-radius: 50px;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      color: var(--color-text);
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition-normal);
      font-family: var(--font-body);
      font-size: 1rem;
    }
    .filter-btn:hover, .filter-btn.active {
      background: var(--color-primary);
      color: #fff;
      border-color: var(--color-primary);
      box-shadow: 0 4px 14px rgba(210, 75, 118, 0.3);
    }
    
    .packages-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 30px;
      padding-bottom: 80px;
    }
    .package-card {
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      overflow: hidden;
      transition: all var(--transition-normal);
      display: flex;
      flex-direction: column;
    }
    .package-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 15px 30px var(--color-shadow);
      border-color: var(--color-primary);
    }
    .package-img {
      width: 100%;
      height: 240px;
      object-fit: cover;
    }
    .package-content {
      padding: 30px;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }
    .package-content h3 {
      font-family: var(--font-magic);
      font-size: 1.8rem;
      color: var(--color-text);
      margin-bottom: 10px;
      -webkit-text-fill-color: initial;
      background: none;
    }
    .package-content p {
      color: var(--color-text-light);
      margin-bottom: 20px;
      font-size: 1rem;
      line-height: 1.6;
      flex-grow: 1;
    }
    .package-price {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--color-primary);
      margin-bottom: 20px;
      font-family: var(--font-heading);
    }
    .package-features {
      list-style: none;
      margin-bottom: 25px;
      padding: 0;
    }
    .package-features li {
      margin-bottom: 12px;
      font-size: 0.95rem;
      color: var(--color-text);
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .package-features li i {
      color: var(--color-secondary);
      font-size: 1.1rem;
    }
    
    .section-title {
      font-family: var(--font-magic);
      font-size: 3rem;
      text-align: center;
      margin-bottom: 20px;
      background: none;
      -webkit-text-fill-color: initial;
    }
    
    .compare-table-wrapper {
      overflow-x: auto;
      margin: 40px 0 100px;
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
    }
    .compare-table {
      width: 100%;
      border-collapse: collapse;
      min-width: 800px;
    }
    .compare-table th, .compare-table td {
      padding: 25px 20px;
      text-align: center;
      border-bottom: 1px solid var(--color-border);
    }
    .compare-table th {
      font-family: var(--font-magic);
      font-size: 1.4rem;
      color: var(--color-text);
      background: rgba(0,0,0,0.02);
      -webkit-text-fill-color: initial;
    }
    [data-theme="dark"] .compare-table th { background: rgba(255,255,255,0.02); }
    .compare-table th:first-child, .compare-table td:first-child {
      text-align: left;
      font-family: var(--font-body);
      font-weight: 700;
      font-size: 1.1rem;
    }
    .compare-table i.fa-check { color: var(--color-primary); font-size: 1.2rem; }
    .compare-table i.fa-xmark { color: var(--color-text-light); opacity: 0.3; font-size: 1.2rem; }
    
    .steps-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 30px;
      margin: 50px 0 100px;
    }
    .step-card {
      text-align: left;
      padding: 40px 30px;
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      transition: transform 0.3s ease;
    }
    .step-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 20px 40px var(--color-shadow);
      border-color: var(--color-secondary);
    }
    .step-number {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: var(--color-secondary);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      font-weight: bold;
      margin-bottom: 25px;
      box-shadow: 0 10px 20px rgba(56, 149, 200, 0.3);
    }
    .step-card h3 {
      font-family: var(--font-magic);
      font-size: 1.6rem;
      margin-bottom: 15px;
      color: var(--color-text);
      background: none;
      -webkit-text-fill-color: initial;
    }
    .step-card p {
      color: var(--color-text-light);
      font-size: 1rem;
      line-height: 1.6;
    }
    
    .cta-section {
      text-align: center;
      padding: 100px 20px;
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      border: 2px solid var(--color-primary);
      margin-bottom: 100px;
      box-shadow: 0 20px 50px rgba(210, 75, 118, 0.15);
      position: relative;
      overflow: hidden;
    }
    .cta-section::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 50% 50%, rgba(210, 75, 118, 0.1), transparent 70%);
      pointer-events: none;
    }
    .cta-section h2 {
      font-family: var(--font-magic);
      font-size: 3.5rem;
      margin-bottom: 25px;
      position: relative;
      background: none;
      -webkit-text-fill-color: initial;
    }
    .cta-desc {
      color: var(--color-text);
      max-width: 700px;
      margin: 0 auto 40px;
      font-size: 1.15rem;
      line-height: 1.6;
      position: relative;
    }
    
    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 20px;
    }

    /* FAQs */
    .faq-section {
      max-width: 900px;
      margin: 80px auto 120px;
      padding: 0 20px;
    }
    .faq-item {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-md);
      margin-bottom: 20px;
      overflow: hidden;
      transition: border-color 0.3s;
    }
    .faq-item:hover {
      border-color: var(--color-primary);
    }
    .faq-question {
      padding: 25px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-weight: bold;
      cursor: pointer;
      font-size: 1.2rem;
      color: var(--color-text);
    }
    .faq-answer {
      padding: 0 25px;
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease, padding 0.4s ease;
      color: var(--color-text-light);
      font-size: 1.05rem;
      line-height: 1.6;
    }
    .faq-item.active .faq-answer {
      padding: 0 25px 25px;
      max-height: 300px;
    }
    .faq-item.active .fa-chevron-down {
      transform: rotate(180deg);
      color: var(--color-primary);
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <main>
    <!-- HERO -->
    <section class="packages-hero">
      <div class="container hero-container reveal">
        <div class="hero-text-side">
          <h1><span class="text-pink">A little magic.</span><br><span class="text-blue">A lot of joy.</span></h1>
          <p>From joyful birthdays to extraordinary celebrations, discover experiences designed to make every little moment unforgettable.</p>
          <div class="hero-actions">
            <a href="#packages" class="btn btn-primary" style="padding: 15px 30px; font-size: 1.1rem;">Explore Packages</a>
          </div>
        </div>
        <div class="hero-img-side">
          <img src="assets/images/blog_party_ideas_1790831919409.jpg" alt="Magical Party" class="hero-main-img">
        </div>
      </div>
    </section>

    <!-- PACKAGES GRID -->
    <section id="packages" class="container">
      <h2 class="section-title reveal"><span class="text-pink">Packages made for</span> <span class="text-blue">your wow moments</span></h2>
      
      <div class="filter-container reveal">
        <button class="filter-btn active" data-filter="all">All Packages</button>
        <button class="filter-btn" data-filter="birthday">Birthdays</button>
        <button class="filter-btn" data-filter="school">School Events</button>
        <button class="filter-btn" data-filter="theme">Themed Parties</button>
      </div>

      <div class="packages-grid">
        <!-- Package 1 -->
        <div class="package-card reveal" data-category="birthday">
          <img src="assets/images/magic_show_party_1790842468826.jpg" alt="Sparkle Party" class="package-img">
          <div class="package-content">
            <h3>Sparkle Party</h3>
            <p>Perfect for birthdays! Includes games, music, and joyful entertainment that kids absolutely love.</p>
            <div class="package-price">$99 <span style="font-size: 1rem; font-weight: normal; color: var(--color-text-light);">/ event</span></div>
            <ul class="package-features">
              <li><i class="fa-solid fa-clock"></i> 1 hour of entertainment</li>
              <li><i class="fa-solid fa-user"></i> 1 Professional Entertainer</li>
              <li><i class="fa-solid fa-gamepad"></i> Interactive Games & Fun</li>
            </ul>
            <a href="booking.html?package=sparkle-party" class="btn btn-secondary" style="width: 100%;">Choose Package</a>
          </div>
        </div>

        <!-- Package 2 -->
        <div class="package-card reveal" data-category="birthday theme">
          <img src="assets/images/superhero_party_1790842695325.jpg" alt="Magic Adventure" class="package-img">
          <div class="package-content">
            <h3>Magic Adventure</h3>
            <p>Captivating performances and interactive fun designed to amaze larger celebrations and parties.</p>
            <div class="package-price">$149 <span style="font-size: 1rem; font-weight: normal; color: var(--color-text-light);">/ event</span></div>
            <ul class="package-features">
              <li><i class="fa-solid fa-clock"></i> 1.5 hours of entertainment</li>
              <li><i class="fa-solid fa-wand-magic-sparkles"></i> Spectacular Magic Show</li>
              <li><i class="fa-solid fa-camera"></i> Meet & Greet Moments</li>
            </ul>
            <a href="booking.html?package=magic-adventure" class="btn btn-primary" style="width: 100%;">Choose Package</a>
          </div>
        </div>

        <!-- Package 3 -->
        <div class="package-card reveal" data-category="theme">
          <img src="assets/images/princess_party_1790842645232.jpg" alt="Fantasy World" class="package-img">
          <div class="package-content">
            <h3>Fantasy World</h3>
            <p>Story-inspired play and themed activities that transport kids straight into a magical fantasy world.</p>
            <div class="package-price">$199 <span style="font-size: 1rem; font-weight: normal; color: var(--color-text-light);">/ event</span></div>
            <ul class="package-features">
              <li><i class="fa-solid fa-clock"></i> 2 hours of entertainment</li>
              <li><i class="fa-solid fa-crown"></i> Custom Themed Activities</li>
              <li><i class="fa-solid fa-music"></i> Interactive Story & Music</li>
            </ul>
            <a href="booking.html?package=fantasy-world" class="btn btn-secondary" style="width: 100%;">Choose Package</a>
          </div>
        </div>

        <!-- Package 4 -->
        <div class="package-card reveal" data-category="school">
          <img src="assets/images/about_kids_birthday.jpg" alt="Little Explorers" class="package-img">
          <div class="package-content">
            <h3>Little Explorers</h3>
            <p>Exciting group activities, team games, and challenges perfectly suited for school events and big crowds.</p>
            <div class="package-price">$249 <span style="font-size: 1rem; font-weight: normal; color: var(--color-text-light);">/ event</span></div>
            <ul class="package-features">
              <li><i class="fa-solid fa-clock"></i> 2.5 hours of entertainment</li>
              <li><i class="fa-solid fa-users"></i> 2 Professional Entertainers</li>
              <li><i class="fa-solid fa-puzzle-piece"></i> Exciting Team Challenges</li>
            </ul>
            <a href="booking.html?package=little-explorers" class="btn btn-secondary" style="width: 100%;">Choose Package</a>
          </div>
        </div>

        <!-- Package 5 -->
        <div class="package-card reveal" data-category="theme">
          <img src="assets/images/james_boy_smile.jpg" alt="Joyful Moments" class="package-img">
          <div class="package-content">
            <h3>Joyful Moments</h3>
            <p>An intimate experience for smaller gatherings focused on personal interaction and close-up magic.</p>
            <div class="package-price">$129 <span style="font-size: 1rem; font-weight: normal; color: var(--color-text-light);">/ event</span></div>
            <ul class="package-features">
              <li><i class="fa-solid fa-clock"></i> 1 hour of entertainment</li>
              <li><i class="fa-solid fa-wand-sparkles"></i> Close-up Magic</li>
              <li><i class="fa-solid fa-gift"></i> Custom Keepsake</li>
            </ul>
            <a href="booking.html?package=joyful-moments" class="btn btn-secondary" style="width: 100%;">Choose Package</a>
          </div>
        </div>

        <!-- Package 6 -->
        <div class="package-card reveal" data-category="birthday school">
          <img src="assets/images/hero_magician_1790831867453.jpg" alt="Ultimate Celebration" class="package-img">
          <div class="package-content">
            <h3>Ultimate Celebration</h3>
            <p>The premium package that includes everything. Perfect for huge parties, with massive stage performances.</p>
            <div class="package-price">$349 <span style="font-size: 1rem; font-weight: normal; color: var(--color-text-light);">/ event</span></div>
            <ul class="package-features">
              <li><i class="fa-solid fa-clock"></i> 3 hours of entertainment</li>
              <li><i class="fa-solid fa-users"></i> 3 Professional Entertainers</li>
              <li><i class="fa-solid fa-star"></i> Full Stage Magic Show</li>
            </ul>
            <a href="booking.html?package=ultimate-celebration" class="btn btn-secondary" style="width: 100%;">Choose Package</a>
          </div>
        </div>

      </div>
    </section>

    <!-- COMPARE -->
    <section class="container">
      <h2 class="section-title reveal"><span class="text-pink">Compare</span> <span class="text-blue">the experiences</span></h2>
      <p class="reveal" style="text-align: center; color: var(--color-text-light); max-width: 600px; margin: 0 auto;">Review our carefully crafted packages side-by-side to find the perfect magical experience for your upcoming celebration.</p>
      
      <div class="compare-table-wrapper reveal">
        <table class="compare-table">
          <thead>
            <tr>
              <th>Package Features</th>
              <th>Sparkle Party</th>
              <th>Magic Adventure</th>
              <th>Fantasy World</th>
              <th>Little Explorers</th>
              <th>Joyful Moments</th>
              <th>Ultimate Celebration</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Duration</td>
              <td>1 hour</td>
              <td>1.5 hours</td>
              <td>2 hours</td>
              <td>2.5 hours</td>
              <td>1 hour</td>
              <td>3 hours</td>
            </tr>
            <tr>
              <td>Entertainers</td>
              <td>1</td>
              <td>1</td>
              <td>1-2</td>
              <td>2</td>
              <td>1</td>
              <td>3</td>
            </tr>
            <tr>
              <td>Interactive games</td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-xmark"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
            </tr>
            <tr>
              <td>Live performance</td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
            </tr>
            <tr>
              <td>Themed activities</td>
              <td><i class="fa-solid fa-xmark"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-xmark"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
            </tr>
            <tr>
              <td>Meet & Greet</td>
              <td><i class="fa-solid fa-xmark"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
              <td><i class="fa-solid fa-check"></i></td>
            </tr>
            <tr>
              <td>Starting price</td>
              <td style="color: var(--color-primary); font-size: 1.15rem; font-weight: bold;">$99</td>
              <td style="color: var(--color-primary); font-size: 1.15rem; font-weight: bold;">$149</td>
              <td style="color: var(--color-primary); font-size: 1.15rem; font-weight: bold;">$199</td>
              <td style="color: var(--color-primary); font-size: 1.15rem; font-weight: bold;">$249</td>
              <td style="color: var(--color-primary); font-size: 1.15rem; font-weight: bold;">$129</td>
              <td style="color: var(--color-primary); font-size: 1.15rem; font-weight: bold;">$349</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- HOW IT WORKS -->
    <section class="container">
      <h2 class="section-title reveal"><span class="text-pink">How</span> <span class="text-blue">booking works</span></h2>
      <p class="reveal" style="text-align: center; color: var(--color-text-light); max-width: 600px; margin: 0 auto;">Plan your celebration with our simple 4-step process, from choosing your magical experience to confirming the final details.</p>
      
      <div class="steps-grid">
        <div class="step-card reveal">
          <div class="step-number">1</div>
          <h3>Pick a Package</h3>
          <p>Explore our crafted experiences in real-time. Review the pricing, features, and durations. Select the package that perfectly aligns with your event's scale and theme directly from this page.</p>
        </div>
        <div class="step-card reveal">
          <div class="step-number">2</div>
          <h3>Select Entertainer</h3>
          <p>Tell us exactly who you want to invite! You'll be asked to pick the type of entertainer (Magician, Princess, Clown, etc.) and you can even request specific performers by name when checking out.</p>
        </div>
        <div class="step-card reveal">
          <div class="step-number">3</div>
          <h3>Share Details</h3>
          <p>Fill out the comprehensive booking form. We'll need the date, specific venue location (indoor/outdoor), expected guest count, and any unique requests so we can prepare deeply for your event.</p>
        </div>
        <div class="step-card reveal">
          <div class="step-number">4</div>
          <h3>Confirm</h3>
          <p>Review all your magical details in the summary pane and finalize your booking request. Our team will verify availability and send you a secure confirmation link to lock in your date.</p>
        </div>
      </div>
    </section>

    <!-- FAQs -->
    <section class="faq-section reveal">
      <h2 class="section-title"><span class="text-pink">Frequently</span> <span class="text-blue">Asked Questions</span></h2>
      <div style="margin-top: 40px;">
        <div class="faq-item">
          <div class="faq-question">
            Are the displayed package prices final? <i class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
          </div>
          <div class="faq-answer">
            <p>The prices shown are sample starting prices for our standard packages. The final cost may vary slightly depending on your exact location, the specific entertainer you choose, and any optional add-ons you select during the booking process.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-question">
            How early should I book a package? <i class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
          </div>
          <div class="faq-answer">
            <p>We highly recommend booking at least 3-4 weeks in advance, especially for weekend events or holidays, as our most popular entertainers' schedules fill up quickly. Booking early gives you maximum flexibility for your preferred date and time.</p>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-question">
            Can packages be customized for unique events? <i class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
          </div>
          <div class="faq-answer">
            <p>Absolutely! All our packages serve as a magical foundation. When you proceed to the booking page, you will find a "Customize Your Experience" section where you can add special requests, extra entertainers, or unique themes.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- FINAL CTA -->
    <section class="container">
      <div class="cta-section reveal">
        <h2><span class="text-pink">Let's make</span> <span class="text-blue">a little magic happen</span></h2>
        <p class="cta-desc">Choose an experience, find your entertainer, and start planning a celebration filled with laughter, wonder, and unforgettable moments.</p>
        <a href="booking.html" class="btn btn-primary" style="position: relative; padding: 20px 50px; font-size: 1.35rem; box-shadow: 0 10px 30px rgba(210, 75, 118, 0.4); text-transform: uppercase; letter-spacing: 1px;">Plan Your Celebration <i class="fa-solid fa-arrow-right" style="margin-left: 10px;"></i></a>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <div id="footer"></div>

  <script src="js/theme.js"></script>
  <script src="js/rtl.js"></script>
  <script src="js/components.js"></script>
  <script src="js/main.js"></script>
  <script>
    // Package filtering logic
    document.addEventListener('DOMContentLoaded', () => {
      const filterBtns = document.querySelectorAll('.filter-btn');
      const packageCards = document.querySelectorAll('.package-card');

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          
          const filterValue = btn.getAttribute('data-filter');
          
          packageCards.forEach(card => {
            if (filterValue === 'all') {
              card.style.display = 'flex';
            } else {
              if (card.getAttribute('data-category').includes(filterValue)) {
                card.style.display = 'flex';
              } else {
                card.style.display = 'none';
              }
            }
          });
        });
      });

      // FAQ Accordion
      const faqItems = document.querySelectorAll('.faq-item');
      faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
          const isActive = item.classList.contains('active');
          faqItems.forEach(i => i.classList.remove('active'));
          if (!isActive) {
            item.classList.add('active');
          }
        });
      });
    });
  </script>
</body>
</html>
"""

with open('c:/Users/vigas/Desktop/magiqo/packages.html', 'w', encoding='utf-8') as f:
    f.write(packages_html_content)

print("Packages completely overhauled with dual colors and expanded content.")
