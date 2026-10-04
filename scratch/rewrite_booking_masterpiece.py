booking_full_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book Your Celebration | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* Hero Section */
    .booking-hero {
      padding: 160px 0 80px;
      background-color: var(--color-bg);
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    .booking-hero h1 {
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-family: var(--font-magic);
      line-height: 1.2;
      margin-bottom: 20px;
    }
    .booking-hero p {
      max-width: 600px;
      margin: 0 auto;
      font-size: 1.15rem;
      color: var(--color-text-light);
    }
    .hero-bubble {
      position: absolute;
      border-radius: 50%;
      background: var(--color-primary);
      opacity: 0.1;
      animation: float 6s infinite ease-in-out;
    }
    .hero-bubble-1 { width: 100px; height: 100px; top: 120px; left: 10%; }
    .hero-bubble-2 { width: 150px; height: 150px; bottom: 20px; right: 10%; background: #3895c8; animation-delay: 2s; }
    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-20px); }
    }

    /* Trust Badges */
    .trust-badges {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-wrap: wrap;
      gap: 40px;
      padding: 40px 20px;
      background: var(--color-surface);
      border-top: 1px solid var(--color-border);
      border-bottom: 1px solid var(--color-border);
    }
    .trust-badge {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      color: var(--color-text-light);
      font-weight: 600;
      font-size: 0.95rem;
    }
    .trust-badge i {
      font-size: 2rem;
      color: #3895c8;
    }

    /* Layout */
    .booking-layout {
      max-width: 1300px;
      margin: 60px auto 100px;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 40px;
      align-items: start;
    }

    /* Stepper UI */
    .stepper-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 40px;
      position: relative;
      background: var(--color-surface);
      padding: 20px 30px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      box-shadow: 0 10px 30px var(--color-shadow);
    }
    .stepper-header::before {
      content: '';
      position: absolute;
      top: 50%;
      left: 40px;
      right: 40px;
      height: 3px;
      background: var(--color-bg);
      z-index: 1;
      transform: translateY(-50%);
    }
    .step-indicator {
      position: relative;
      z-index: 2;
      background: var(--color-surface);
      width: 45px;
      height: 45px;
      border-radius: 50%;
      border: 2px solid var(--color-border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      color: var(--color-text-light);
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .step-indicator.active {
      border-color: var(--color-primary);
      background: var(--color-primary);
      color: white;
      box-shadow: 0 0 20px rgba(210, 75, 118, 0.4);
      transform: scale(1.1);
    }
    .step-indicator.completed {
      border-color: #3895c8;
      background: #3895c8;
      color: white;
    }
    .step-label {
      position: absolute;
      top: 55px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.9rem;
      white-space: nowrap;
      color: var(--color-text-light);
      font-weight: 600;
      transition: color 0.3s;
    }
    .step-indicator.active .step-label { color: var(--color-primary); font-weight: 800; }
    .step-indicator.completed .step-label { color: #3895c8; }

    /* Step Contents */
    .step-content {
      display: none;
      background: var(--color-surface);
      padding: 45px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      box-shadow: 0 20px 50px var(--color-shadow);
    }
    .step-content.active {
      display: block;
      animation: slideIn 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    @keyframes slideIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .step-title {
      font-family: var(--font-magic);
      font-size: 2.5rem;
      margin-bottom: 35px;
      color: var(--color-text);
      text-align: center;
    }

    /* Cards */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 20px;
    }
    .selection-card {
      border: 2px solid var(--color-border);
      border-radius: var(--radius-md);
      padding: 20px;
      cursor: pointer;
      transition: all 0.3s;
      text-align: center;
      position: relative;
      background: var(--color-bg);
    }
    .selection-card:hover {
      border-color: #3895c8;
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(56, 149, 200, 0.15);
    }
    .selection-card.selected {
      border-color: var(--color-primary);
      background: var(--color-surface);
      box-shadow: 0 15px 30px rgba(210, 75, 118, 0.2);
    }
    .selection-card.selected::after {
      content: '\\f00c';
      font-family: 'Font Awesome 6 Free';
      font-weight: 900;
      position: absolute;
      top: 15px; right: 15px;
      background: var(--color-primary);
      color: white;
      width: 28px; height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
      box-shadow: 0 4px 10px rgba(210, 75, 118, 0.4);
    }
    .card-img {
      width: 100%;
      height: 150px;
      object-fit: cover;
      border-radius: var(--radius-sm);
      margin-bottom: 15px;
    }
    .card-title {
      font-family: var(--font-heading);
      font-weight: 800;
      font-size: 1.15rem;
      margin-bottom: 8px;
      color: var(--color-text);
    }
    .card-price {
      color: var(--color-primary);
      font-weight: 900;
      font-size: 1.3rem;
    }

    /* Forms */
    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 25px;
    }
    .form-group { margin-bottom: 5px; }
    .form-group.full { grid-column: 1 / -1; }
    .form-label {
      display: block;
      margin-bottom: 10px;
      font-weight: 700;
      color: var(--color-text);
      font-size: 0.95rem;
    }
    .form-control {
      width: 100%;
      padding: 14px 18px;
      border: 1px solid var(--color-border);
      border-radius: var(--radius-sm);
      background: var(--color-bg);
      color: var(--color-text);
      font-family: var(--font-body);
      font-size: 1rem;
      transition: all 0.3s;
    }
    .form-control:focus {
      outline: none;
      border-color: #3895c8;
      box-shadow: 0 0 0 4px rgba(56, 149, 200, 0.15);
      background: var(--color-surface);
    }

    /* Stepper Controls */
    .stepper-controls {
      display: flex;
      justify-content: space-between;
      margin-top: 50px;
      padding-top: 30px;
      border-top: 1px solid var(--color-border);
    }
    .btn-nav {
      padding: 15px 35px;
      font-size: 1.1rem;
      border-radius: var(--radius-pill);
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      border: none;
      transition: all 0.3s;
    }
    .btn-nav-prev {
      background: var(--color-bg);
      color: var(--color-text);
      border: 1px solid var(--color-border);
    }
    .btn-nav-prev:hover {
      background: var(--color-border);
    }
    .btn-nav-next {
      background: var(--color-primary);
      color: white;
      box-shadow: 0 10px 20px rgba(210, 75, 118, 0.3);
    }
    .btn-nav-next:hover {
      background: var(--color-primary-hover);
      transform: translateY(-2px);
      box-shadow: 0 15px 25px rgba(210, 75, 118, 0.4);
    }

    /* Summary Sidebar */
    .summary-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 35px;
      position: sticky;
      top: 100px;
      box-shadow: 0 20px 50px var(--color-shadow);
    }
    .summary-title {
      font-family: var(--font-magic);
      font-size: 2rem;
      color: var(--color-primary);
      margin-bottom: 25px;
      border-bottom: 2px solid var(--color-bg);
      padding-bottom: 15px;
      text-align: center;
    }
    .summary-item {
      display: flex;
      justify-content: space-between;
      margin-bottom: 18px;
      color: var(--color-text);
      font-size: 1.05rem;
    }
    .summary-item span:first-child { color: var(--color-text-light); }
    .summary-total {
      margin-top: 25px;
      padding-top: 25px;
      border-top: 2px dashed var(--color-border);
      display: flex;
      justify-content: space-between;
      font-size: 1.5rem;
      font-weight: 900;
      color: #3895c8;
    }

    /* Additional Section: Why Book With Us */
    .features-section {
      background: var(--color-surface);
      padding: 100px 20px;
      text-align: center;
      border-top: 1px solid var(--color-border);
    }
    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 40px;
      max-width: 1200px;
      margin: 50px auto 0;
    }
    .feature-item {
      padding: 40px 30px;
      background: var(--color-bg);
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      transition: transform 0.3s;
    }
    .feature-item:hover {
      transform: translateY(-10px);
      border-color: #3895c8;
    }
    .feature-item i {
      font-size: 3rem;
      color: var(--color-primary);
      margin-bottom: 20px;
    }
    .feature-item h4 {
      font-family: var(--font-heading);
      font-size: 1.4rem;
      margin-bottom: 15px;
      color: var(--color-text);
    }

    /* Additional Section: Testimonials */
    .testimonials-section {
      padding: 100px 20px;
      background: var(--color-bg);
      text-align: center;
    }
    .test-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
      max-width: 1100px;
      margin: 50px auto 0;
    }
    .test-card {
      background: var(--color-surface);
      padding: 40px 30px;
      border-radius: var(--radius-md);
      box-shadow: 0 10px 30px var(--color-shadow);
      border: 1px solid var(--color-border);
      text-align: left;
    }
    .test-card i.fa-quote-left {
      font-size: 2rem;
      color: #3895c8;
      opacity: 0.3;
      margin-bottom: 20px;
    }
    .test-card p {
      font-size: 1.1rem;
      font-style: italic;
      color: var(--color-text);
      margin-bottom: 20px;
    }
    .test-author {
      font-weight: 700;
      color: var(--color-primary);
    }

    /* Support Banner */
    .support-banner {
      background: #3895c8;
      color: white;
      padding: 60px 20px;
      text-align: center;
    }
    .support-banner h2 {
      font-family: var(--font-magic);
      font-size: 2.5rem;
      margin-bottom: 15px;
    }
    .support-banner p {
      font-size: 1.15rem;
      margin-bottom: 30px;
      opacity: 0.9;
    }
    .btn-support {
      background: white;
      color: #3895c8;
      padding: 15px 40px;
      border-radius: var(--radius-pill);
      font-weight: 800;
      text-decoration: none;
      display: inline-block;
      transition: transform 0.3s;
    }
    .btn-support:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }

    @media (max-width: 992px) {
      .booking-layout { grid-template-columns: 1fr; }
      .summary-card { position: relative; top: 0; }
    }
    @media (max-width: 768px) {
      .form-grid { grid-template-columns: 1fr; }
      .stepper-header { display: none; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <main>
    <!-- HERO -->
    <section class="booking-hero">
      <div class="hero-bubble hero-bubble-1"></div>
      <div class="hero-bubble hero-bubble-2"></div>
      <div class="container reveal">
        <h1>Reserve Your Date in <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">5 Easy Steps</span></h1>
        <p>Follow our simple booking progress to completely customize and lock in your magical celebration.</p>
      </div>
    </section>

    <!-- TRUST BADGES -->
    <section class="trust-badges reveal">
      <div class="trust-badge">
        <i class="fa-solid fa-shield-halved"></i>
        <span>Secure Booking</span>
      </div>
      <div class="trust-badge">
        <i class="fa-solid fa-star"></i>
        <span>5-Star Performers</span>
      </div>
      <div class="trust-badge">
        <i class="fa-solid fa-calendar-check"></i>
        <span>Guaranteed Arrival</span>
      </div>
      <div class="trust-badge">
        <i class="fa-solid fa-face-smile"></i>
        <span>100% Joy Guarantee</span>
      </div>
    </section>

    <div class="booking-layout">
      <!-- LEFT: STEPPER -->
      <div class="stepper-container reveal">
        
        <!-- Header -->
        <div class="stepper-header">
          <div class="step-indicator active" data-step="1">1<div class="step-label">Package</div></div>
          <div class="step-indicator" data-step="2">2<div class="step-label">Theme</div></div>
          <div class="step-indicator" data-step="3">3<div class="step-label">Guests</div></div>
          <div class="step-indicator" data-step="4">4<div class="step-label">Add-ons</div></div>
          <div class="step-indicator" data-step="5">5<div class="step-label">Payment</div></div>
        </div>

        <!-- STEP 1: PACKAGE -->
        <div class="step-content active" id="step-1">
          <h2 class="step-title">Select Your Package</h2>
          <div class="card-grid">
            <div class="selection-card package-sel selected" onclick="selectCard(this, 'package')">
              <img src="assets/images/magic_show_party_1790842468826.jpg" class="card-img" alt="Sparkle Party">
              <div class="card-title">Sparkle Party</div>
              <p style="font-size: 0.95rem; margin-bottom: 12px; color: var(--color-text-light);">1 hour • 1 Entertainer</p>
              <div class="card-price">$99</div>
            </div>
            <div class="selection-card package-sel" onclick="selectCard(this, 'package')">
              <img src="assets/images/superhero_party_1790842695325.jpg" class="card-img" alt="Magic Adventure">
              <div class="card-title">Magic Adventure</div>
              <p style="font-size: 0.95rem; margin-bottom: 12px; color: var(--color-text-light);">1.5 hours • Magic Show</p>
              <div class="card-price">$149</div>
            </div>
            <div class="selection-card package-sel" onclick="selectCard(this, 'package')">
              <img src="assets/images/princess_party_1790842645232.jpg" class="card-img" alt="Fantasy World">
              <div class="card-title">Fantasy World</div>
              <p style="font-size: 0.95rem; margin-bottom: 12px; color: var(--color-text-light);">2 hours • Custom Theme</p>
              <div class="card-price">$199</div>
            </div>
          </div>
          <div class="stepper-controls" style="justify-content: flex-end;">
            <button class="btn-nav btn-nav-next" onclick="nextStep(2)">Continue to Theme <i class="fa-solid fa-arrow-right"></i></button>
          </div>
        </div>

        <!-- STEP 2: THEME -->
        <div class="step-content" id="step-2">
          <h2 class="step-title">Select Your Theme</h2>
          <div class="card-grid">
            <div class="selection-card theme-sel selected" onclick="selectCard(this, 'theme')">
              <img src="assets/images/princess_party_1790842645232.jpg" class="card-img" alt="Princess Royal">
              <div class="card-title">Princess Royal</div>
            </div>
            <div class="selection-card theme-sel" onclick="selectCard(this, 'theme')">
              <img src="assets/images/superhero_party_1790842695325.jpg" class="card-img" alt="Superhero League">
              <div class="card-title">Superhero League</div>
            </div>
            <div class="selection-card theme-sel" onclick="selectCard(this, 'theme')">
              <img src="assets/images/about_kids_birthday.jpg" class="card-img" alt="Jungle Explorer">
              <div class="card-title">Jungle Explorer</div>
            </div>
            <div class="selection-card theme-sel" onclick="selectCard(this, 'theme')">
              <img src="assets/images/magic_show_party_1790842468826.jpg" class="card-img" alt="Fairy Garden">
              <div class="card-title">Fairy Garden</div>
            </div>
          </div>
          <div class="stepper-controls">
            <button class="btn-nav btn-nav-prev" onclick="nextStep(1)"><i class="fa-solid fa-arrow-left"></i> Back</button>
            <button class="btn-nav btn-nav-next" onclick="nextStep(3)">Continue to Guests <i class="fa-solid fa-arrow-right"></i></button>
          </div>
        </div>

        <!-- STEP 3: GUESTS & EVENT DETAILS -->
        <div class="step-content" id="step-3">
          <h2 class="step-title">Event & Guest Details</h2>
          <div class="form-grid">
            <div class="form-group">
              <label class="form-label">Number of Children</label>
              <input type="number" class="form-control" placeholder="e.g. 15">
            </div>
            <div class="form-group">
              <label class="form-label">Number of Adults</label>
              <input type="number" class="form-control" placeholder="e.g. 10">
            </div>
            <div class="form-group">
              <label class="form-label">Child's Age (turning)</label>
              <input type="number" class="form-control" placeholder="e.g. 6">
            </div>
            <div class="form-group">
              <label class="form-label">Event Date</label>
              <input type="date" class="form-control">
            </div>
            <div class="form-group">
              <label class="form-label">Event Time</label>
              <input type="time" class="form-control">
            </div>
            <div class="form-group">
              <label class="form-label">Event Location (City/Area)</label>
              <input type="text" class="form-control" placeholder="e.g. New York, Indoor Hall">
            </div>
          </div>
          <div class="stepper-controls">
            <button class="btn-nav btn-nav-prev" onclick="nextStep(2)"><i class="fa-solid fa-arrow-left"></i> Back</button>
            <button class="btn-nav btn-nav-next" onclick="nextStep(4)">Continue to Add-ons <i class="fa-solid fa-arrow-right"></i></button>
          </div>
        </div>

        <!-- STEP 4: ADD-ONS -->
        <div class="step-content" id="step-4">
          <h2 class="step-title">Customize with Add-ons</h2>
          <div class="card-grid">
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Balloon Decor</div>
              <p style="font-size: 0.95rem; color: var(--color-text-light); margin-bottom: 10px;">Arch and table balloons</p>
              <div class="card-price">+$50</div>
            </div>
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Photography</div>
              <p style="font-size: 0.95rem; color: var(--color-text-light); margin-bottom: 10px;">2 hours of pro photos</p>
              <div class="card-price">+$150</div>
            </div>
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Custom Cake</div>
              <p style="font-size: 0.95rem; color: var(--color-text-light); margin-bottom: 10px;">Themed 2-tier cake</p>
              <div class="card-price">+$80</div>
            </div>
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Party Favors</div>
              <p style="font-size: 0.95rem; color: var(--color-text-light); margin-bottom: 10px;">Goodie bags for 15 kids</p>
              <div class="card-price">+$60</div>
            </div>
          </div>
          <div class="stepper-controls">
            <button class="btn-nav btn-nav-prev" onclick="nextStep(3)"><i class="fa-solid fa-arrow-left"></i> Back</button>
            <button class="btn-nav btn-nav-next" onclick="nextStep(5)">Continue to Payment <i class="fa-solid fa-arrow-right"></i></button>
          </div>
        </div>

        <!-- STEP 5: PAYMENT -->
        <div class="step-content" id="step-5">
          <h2 class="step-title">Payment & Confirmation</h2>
          <div class="form-grid">
            <div class="form-group full">
              <label class="form-label">Name on Card</label>
              <input type="text" class="form-control" placeholder="John Doe">
            </div>
            <div class="form-group full">
              <label class="form-label">Card Number</label>
              <input type="text" class="form-control" placeholder="0000 0000 0000 0000">
            </div>
            <div class="form-group">
              <label class="form-label">Expiry Date</label>
              <input type="text" class="form-control" placeholder="MM/YY">
            </div>
            <div class="form-group">
              <label class="form-label">CVV</label>
              <input type="text" class="form-control" placeholder="123">
            </div>
            <div class="form-group full" style="margin-top: 15px;">
              <label style="display: flex; align-items: flex-start; gap: 15px; cursor: pointer; color: var(--color-text-light); line-height: 1.5;">
                <input type="checkbox" style="width: 24px; height: 24px; margin-top: 2px;">
                I agree to the cancellation terms, booking policy, and authorize the advance deposit charge.
              </label>
            </div>
          </div>
          <div class="stepper-controls">
            <button class="btn-nav btn-nav-prev" onclick="nextStep(4)"><i class="fa-solid fa-arrow-left"></i> Back</button>
            <button class="btn-nav btn-nav-next" style="background: #3895c8;">Complete Booking <i class="fa-solid fa-check"></i></button>
          </div>
        </div>

      </div>

      <!-- RIGHT: SUMMARY -->
      <div class="summary-card reveal">
        <h3 class="summary-title">Booking Summary</h3>
        <div class="summary-item">
          <span>Package:</span>
          <span style="font-weight: 800;">Sparkle Party</span>
        </div>
        <div class="summary-item">
          <span>Theme:</span>
          <span style="font-weight: 800;">Princess Royal</span>
        </div>
        <div class="summary-item">
          <span>Event Date:</span>
          <span style="font-weight: 800;">TBD</span>
        </div>
        <div class="summary-item">
          <span>Guests:</span>
          <span style="font-weight: 800;">-</span>
        </div>
        <div class="summary-item">
          <span>Add-ons:</span>
          <span style="font-weight: 800;">None</span>
        </div>
        
        <div class="summary-total">
          <span>Total:</span>
          <span>$99.00</span>
        </div>
        <p style="font-size: 0.9rem; color: var(--color-text-light); margin-top: 20px; text-align: center; line-height: 1.5;">20% Advance deposit required to lock in your date. Balance due 24h prior.</p>
      </div>
    </div>

    <!-- NEW SECTION: WHY BOOK WITH US -->
    <section class="features-section reveal">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 15px; color: var(--color-primary);">Why Book With Magiqo?</h2>
      <p style="color: var(--color-text-light); font-size: 1.15rem; max-width: 600px; margin: 0 auto;">We take the stress out of party planning so you can focus on making memories.</p>
      
      <div class="features-grid">
        <div class="feature-item">
          <i class="fa-solid fa-wand-magic-sparkles"></i>
          <h4>Premium Entertainment</h4>
          <p style="color: var(--color-text-light);">All our performers are vetted, trained professionals who specialize in children's engagement.</p>
        </div>
        <div class="feature-item">
          <i class="fa-solid fa-clock-rotate-left"></i>
          <h4>Hassle-Free Process</h4>
          <p style="color: var(--color-text-light);">Book your entire party online in minutes. No endless email chains or confusing quotes.</p>
        </div>
        <div class="feature-item">
          <i class="fa-solid fa-heart"></i>
          <h4>100% Satisfaction</h4>
          <p style="color: var(--color-text-light);">We guarantee your child and their guests will have the absolute best time ever.</p>
        </div>
      </div>
    </section>

    <!-- NEW SECTION: TESTIMONIALS -->
    <section class="testimonials-section reveal">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 15px; color: #3895c8;">Happy Parents</h2>
      <p style="color: var(--color-text-light); font-size: 1.15rem;">Don't just take our word for it.</p>
      
      <div class="test-grid">
        <div class="test-card">
          <i class="fa-solid fa-quote-left"></i>
          <p>"Booking was so easy. The Princess arrived exactly on time and completely mesmerized the kids for two hours straight!"</p>
          <div class="test-author">— Sarah Jenkins</div>
        </div>
        <div class="test-card">
          <i class="fa-solid fa-quote-left"></i>
          <p>"Magiqo took all the stress away. The Add-ons feature let me handle the cake, decor, and entertainment in one click."</p>
          <div class="test-author">— Mark T.</div>
        </div>
      </div>
    </section>

    <!-- FAQs -->
    <section class="faq-section reveal" style="margin-top: 100px;">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 40px;"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Booking Help</span> & FAQs</h2>
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 20px; padding: 25px; box-shadow: 0 5px 15px var(--color-shadow);">
        <h4 style="font-family: var(--font-heading); font-size: 1.25rem; margin-bottom: 12px; color: var(--color-text);">When is my advance payment due?</h4>
        <p style="color: var(--color-text-light); line-height: 1.6;">A 20% advance payment is required at the time of booking to secure your date. The remaining balance is due 24 hours before the event.</p>
      </div>
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 20px; padding: 25px; box-shadow: 0 5px 15px var(--color-shadow);">
        <h4 style="font-family: var(--font-heading); font-size: 1.25rem; margin-bottom: 12px; color: var(--color-text);">What is your cancellation policy?</h4>
        <p style="color: var(--color-text-light); line-height: 1.6;">You may cancel up to 7 days before the event for a full refund of your deposit. Cancellations within 7 days are non-refundable.</p>
      </div>
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 20px; padding: 25px; box-shadow: 0 5px 15px var(--color-shadow);">
        <h4 style="font-family: var(--font-heading); font-size: 1.25rem; margin-bottom: 12px; color: var(--color-text);">Can I change my theme or add-ons later?</h4>
        <p style="color: var(--color-text-light); line-height: 1.6;">Yes! You can modify your theme and add-ons up to 48 hours before the event, subject to availability.</p>
      </div>
    </section>

    <!-- SUPPORT BANNER -->
    <section class="support-banner">
      <div class="container reveal">
        <h2>Need help with your booking?</h2>
        <p>Our magical support team is available 24/7 to assist you.</p>
        <a href="contact.html" class="btn-support">Contact Support</a>
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
    // Stepper Logic
    function nextStep(stepNumber) {
      document.querySelectorAll('.step-content').forEach(el => el.classList.remove('active'));
      document.getElementById('step-' + stepNumber).classList.add('active');
      
      document.querySelectorAll('.step-indicator').forEach(el => {
        const num = parseInt(el.getAttribute('data-step'));
        el.classList.remove('active', 'completed');
        if (num < stepNumber) el.classList.add('completed');
        if (num === stepNumber) el.classList.add('active');
      });
      
      document.querySelector('.stepper-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function selectCard(element, type) {
      const group = type === 'package' ? '.package-sel' : '.theme-sel';
      document.querySelectorAll(group).forEach(el => el.classList.remove('selected'));
      element.classList.add('selected');
    }

    function toggleCard(element) {
      element.classList.toggle('selected');
    }
  </script>
</body>
</html>
"""

with open('c:/Users/vigas/Desktop/magiqo/booking.html', 'w', encoding='utf-8') as f:
    f.write(booking_full_html)

print("Redesigned booking.html into an absolute masterpiece with new sections!")
