booking_stepper_html = """<!DOCTYPE html>
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
    /* Hero */
    .booking-hero {
      padding: 160px 0 60px;
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
    /* Animated bubbles */
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

    /* Layout */
    .booking-layout {
      max-width: 1300px;
      margin: 40px auto 100px;
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
      height: 2px;
      background: var(--color-border);
      z-index: 1;
      transform: translateY(-50%);
    }
    .step-indicator {
      position: relative;
      z-index: 2;
      background: var(--color-surface);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      border: 2px solid var(--color-border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      color: var(--color-text-light);
      transition: all 0.3s;
    }
    .step-indicator.active {
      border-color: var(--color-primary);
      background: var(--color-primary);
      color: white;
      box-shadow: 0 0 15px rgba(210, 75, 118, 0.4);
    }
    .step-indicator.completed {
      border-color: #3895c8;
      background: #3895c8;
      color: white;
    }
    .step-label {
      position: absolute;
      top: 50px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.85rem;
      white-space: nowrap;
      color: var(--color-text-light);
      font-weight: 600;
    }
    .step-indicator.active .step-label { color: var(--color-primary); }

    /* Step Contents */
    .step-content {
      display: none;
      background: var(--color-surface);
      padding: 40px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      box-shadow: 0 15px 40px var(--color-shadow);
    }
    .step-content.active {
      display: block;
      animation: fadeIn 0.4s ease forwards;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .step-title {
      font-family: var(--font-magic);
      font-size: 2.2rem;
      margin-bottom: 30px;
      color: var(--color-text);
    }

    /* Step 1 & 2 Cards */
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
    }
    .selection-card:hover {
      border-color: #3895c8;
      transform: translateY(-5px);
    }
    .selection-card.selected {
      border-color: var(--color-primary);
      background: rgba(210, 75, 118, 0.05);
      box-shadow: 0 10px 20px rgba(210, 75, 118, 0.2);
    }
    .selection-card.selected::after {
      content: '\\f00c';
      font-family: 'Font Awesome 6 Free';
      font-weight: 900;
      position: absolute;
      top: 10px; right: 10px;
      background: var(--color-primary);
      color: white;
      width: 24px; height: 24px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
    }
    .card-img {
      width: 100%;
      height: 140px;
      object-fit: cover;
      border-radius: var(--radius-sm);
      margin-bottom: 15px;
    }
    .card-title {
      font-family: var(--font-heading);
      font-weight: 800;
      font-size: 1.1rem;
      margin-bottom: 8px;
    }
    .card-price {
      color: var(--color-primary);
      font-weight: bold;
      font-size: 1.2rem;
    }

    /* Forms */
    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .form-group { margin-bottom: 20px; }
    .form-group.full { grid-column: 1 / -1; }
    .form-label {
      display: block;
      margin-bottom: 8px;
      font-weight: 600;
      color: var(--color-text);
    }
    .form-control {
      width: 100%;
      padding: 12px 15px;
      border: 1px solid var(--color-border);
      border-radius: var(--radius-sm);
      background: var(--color-bg);
      color: var(--color-text);
      font-family: var(--font-body);
    }
    .form-control:focus {
      outline: none;
      border-color: var(--color-primary);
      box-shadow: 0 0 0 3px rgba(210, 75, 118, 0.1);
    }

    /* Stepper Controls */
    .stepper-controls {
      display: flex;
      justify-content: space-between;
      margin-top: 40px;
      padding-top: 20px;
      border-top: 1px solid var(--color-border);
    }
    
    /* Summary Sidebar */
    .summary-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 30px;
      position: sticky;
      top: 100px;
      box-shadow: 0 15px 40px var(--color-shadow);
    }
    .summary-title {
      font-family: var(--font-magic);
      font-size: 1.8rem;
      color: var(--color-primary);
      margin-bottom: 20px;
      border-bottom: 1px solid var(--color-border);
      padding-bottom: 15px;
    }
    .summary-item {
      display: flex;
      justify-content: space-between;
      margin-bottom: 15px;
      color: var(--color-text);
    }
    .summary-item span:first-child { color: var(--color-text-light); }
    .summary-total {
      margin-top: 20px;
      padding-top: 20px;
      border-top: 2px dashed var(--color-border);
      display: flex;
      justify-content: space-between;
      font-size: 1.3rem;
      font-weight: 900;
      color: var(--color-primary);
    }

    /* FAQs */
    .faq-section {
      max-width: 900px;
      margin: 0 auto 100px;
      padding: 0 20px;
    }

    @media (max-width: 992px) {
      .booking-layout { grid-template-columns: 1fr; }
      .summary-card { position: relative; top: 0; }
    }
    @media (max-width: 768px) {
      .form-grid { grid-template-columns: 1fr; }
      .stepper-header { display: none; /* Simplify on very small screens or scroll it */ }
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
              <p style="font-size: 0.9rem; margin-bottom: 10px; color: var(--color-text-light);">1 hour • 1 Entertainer</p>
              <div class="card-price">$99</div>
            </div>
            <div class="selection-card package-sel" onclick="selectCard(this, 'package')">
              <img src="assets/images/superhero_party_1790842695325.jpg" class="card-img" alt="Magic Adventure">
              <div class="card-title">Magic Adventure</div>
              <p style="font-size: 0.9rem; margin-bottom: 10px; color: var(--color-text-light);">1.5 hours • Magic Show</p>
              <div class="card-price">$149</div>
            </div>
            <div class="selection-card package-sel" onclick="selectCard(this, 'package')">
              <img src="assets/images/princess_party_1790842645232.jpg" class="card-img" alt="Fantasy World">
              <div class="card-title">Fantasy World</div>
              <p style="font-size: 0.9rem; margin-bottom: 10px; color: var(--color-text-light);">2 hours • Custom Theme</p>
              <div class="card-price">$199</div>
            </div>
          </div>
          <div class="stepper-controls" style="justify-content: flex-end;">
            <button class="btn btn-primary" onclick="nextStep(2)">Continue to Theme <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></button>
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
            <button class="btn btn-secondary" onclick="nextStep(1)"><i class="fa-solid fa-arrow-left" style="margin-right: 8px;"></i> Back</button>
            <button class="btn btn-primary" onclick="nextStep(3)">Continue to Guests <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></button>
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
            <button class="btn btn-secondary" onclick="nextStep(2)"><i class="fa-solid fa-arrow-left" style="margin-right: 8px;"></i> Back</button>
            <button class="btn btn-primary" onclick="nextStep(4)">Continue to Add-ons <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></button>
          </div>
        </div>

        <!-- STEP 4: ADD-ONS -->
        <div class="step-content" id="step-4">
          <h2 class="step-title">Customize with Add-ons</h2>
          <div class="card-grid">
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Balloon Decor</div>
              <p style="font-size: 0.9rem; color: var(--color-text-light);">Arch and table balloons</p>
              <div class="card-price">+$50</div>
            </div>
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Photography</div>
              <p style="font-size: 0.9rem; color: var(--color-text-light);">2 hours of professional photos</p>
              <div class="card-price">+$150</div>
            </div>
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Custom Cake</div>
              <p style="font-size: 0.9rem; color: var(--color-text-light);">Themed 2-tier cake</p>
              <div class="card-price">+$80</div>
            </div>
            <div class="selection-card addon-sel" onclick="toggleCard(this)">
              <div class="card-title">Party Favors</div>
              <p style="font-size: 0.9rem; color: var(--color-text-light);">Goodie bags for 15 kids</p>
              <div class="card-price">+$60</div>
            </div>
          </div>
          <div class="stepper-controls">
            <button class="btn btn-secondary" onclick="nextStep(3)"><i class="fa-solid fa-arrow-left" style="margin-right: 8px;"></i> Back</button>
            <button class="btn btn-primary" onclick="nextStep(5)">Continue to Payment <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></button>
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
            <div class="form-group full">
              <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; color: var(--color-text-light);">
                <input type="checkbox" style="width: 20px; height: 20px;">
                I agree to the cancellation terms and booking policy.
              </label>
            </div>
          </div>
          <div class="stepper-controls">
            <button class="btn btn-secondary" onclick="nextStep(4)"><i class="fa-solid fa-arrow-left" style="margin-right: 8px;"></i> Back</button>
            <button class="btn btn-primary" style="background: var(--color-primary);">Complete Booking</button>
          </div>
        </div>

      </div>

      <!-- RIGHT: SUMMARY -->
      <div class="summary-card reveal">
        <h3 class="summary-title">Booking Summary</h3>
        <div class="summary-item">
          <span>Package:</span>
          <span style="font-weight: bold;">Sparkle Party</span>
        </div>
        <div class="summary-item">
          <span>Theme:</span>
          <span style="font-weight: bold;">Princess Royal</span>
        </div>
        <div class="summary-item">
          <span>Event Date:</span>
          <span style="font-weight: bold;">TBD</span>
        </div>
        <div class="summary-item">
          <span>Guests:</span>
          <span style="font-weight: bold;">-</span>
        </div>
        <div class="summary-item">
          <span>Add-ons:</span>
          <span style="font-weight: bold;">None</span>
        </div>
        
        <div class="summary-total">
          <span>Total Cost:</span>
          <span>$99.00</span>
        </div>
        <p style="font-size: 0.85rem; color: var(--color-text-light); margin-top: 15px; text-align: center;">Taxes and travel fees calculated upon final confirmation.</p>
      </div>
    </div>

    <!-- FAQs -->
    <section class="faq-section reveal">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 30px;"><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Booking Help</span> & FAQs</h2>
      <!-- Reusing the standard FAQ HTML from other pages -->
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 15px; padding: 20px;">
        <h4 style="font-family: var(--font-body); font-size: 1.15rem; margin-bottom: 10px;">When is my advance payment due?</h4>
        <p style="color: var(--color-text-light);">A 20% advance payment is required at the time of booking to secure your date. The remaining balance is due 24 hours before the event.</p>
      </div>
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 15px; padding: 20px;">
        <h4 style="font-family: var(--font-body); font-size: 1.15rem; margin-bottom: 10px;">What is your cancellation policy?</h4>
        <p style="color: var(--color-text-light);">You may cancel up to 7 days before the event for a full refund of your deposit. Cancellations within 7 days are non-refundable.</p>
      </div>
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 15px; padding: 20px;">
        <h4 style="font-family: var(--font-body); font-size: 1.15rem; margin-bottom: 10px;">Can I change my theme or add-ons later?</h4>
        <p style="color: var(--color-text-light);">Yes! You can modify your theme and add-ons up to 48 hours before the event, subject to availability.</p>
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
      // Hide all
      document.querySelectorAll('.step-content').forEach(el => el.classList.remove('active'));
      // Show target
      document.getElementById('step-' + stepNumber).classList.add('active');
      
      // Update indicators
      document.querySelectorAll('.step-indicator').forEach(el => {
        const num = parseInt(el.getAttribute('data-step'));
        el.classList.remove('active', 'completed');
        if (num < stepNumber) el.classList.add('completed');
        if (num === stepNumber) el.classList.add('active');
      });
      
      // Scroll to top of stepper
      document.querySelector('.stepper-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Single Select Card Logic
    function selectCard(element, type) {
      const group = type === 'package' ? '.package-sel' : '.theme-sel';
      document.querySelectorAll(group).forEach(el => el.classList.remove('selected'));
      element.classList.add('selected');
    }

    // Multi Select Card Logic
    function toggleCard(element) {
      element.classList.toggle('selected');
    }
  </script>
</body>
</html>
"""

with open('c:/Users/vigas/Desktop/magiqo/booking.html', 'w', encoding='utf-8') as f:
    f.write(booking_stepper_html)

print("Redesigned booking.html as a 5-step stepper workflow!")
