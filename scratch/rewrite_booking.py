booking_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book Your Celebration | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* Custom Booking Styles */
    .booking-hero {
      padding: 160px 0 60px;
      text-align: center;
      background-color: var(--color-bg);
    }
    .booking-hero h1 {
      font-size: clamp(3rem, 5vw, 4.5rem);
      margin-bottom: 20px;
      font-family: var(--font-magic);
      color: var(--color-text);
    }
    .booking-hero p {
      max-width: 650px;
      margin: 0 auto;
      font-size: 1.15rem;
      color: var(--color-text-light);
    }
    
    .booking-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 40px 20px;
      display: grid;
      grid-template-columns: 1fr 400px;
      gap: 40px;
      align-items: start;
    }
    
    @media (max-width: 992px) {
      .booking-container {
        grid-template-columns: 1fr;
      }
      .summary-sidebar {
        order: -1;
      }
    }
    
    .booking-main {
      display: flex;
      flex-direction: column;
      gap: 30px;
    }
    
    .booking-section {
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      padding: 35px;
      box-shadow: 0 10px 30px var(--color-shadow);
      transition: border-color 0.3s;
    }
    .booking-section:hover {
      border-color: var(--color-primary);
    }
    
    .booking-section-title {
      font-family: var(--font-magic);
      font-size: 1.8rem;
      margin-bottom: 25px;
      color: var(--color-text);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    
    /* Inputs */
    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 25px;
    }
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .form-group.full {
      grid-column: 1 / -1;
    }
    .form-label {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--color-text);
    }
    .form-control {
      padding: 14px 18px;
      background: var(--color-bg);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-md);
      color: var(--color-text);
      font-family: var(--font-body);
      font-size: 1rem;
      transition: all 0.3s;
    }
    .form-control:focus {
      border-color: var(--color-primary);
      outline: none;
      box-shadow: 0 0 0 2px rgba(210, 75, 118, 0.3);
    }
    
    /* Summary Sidebar */
    .summary-sidebar {
      position: sticky;
      top: 100px;
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      padding: 35px;
      box-shadow: 0 15px 40px var(--color-shadow);
    }
    .summary-title {
      font-family: var(--font-magic);
      font-size: 2rem;
      margin-bottom: 25px;
      border-bottom: 1px solid var(--color-border);
      padding-bottom: 15px;
      color: var(--color-text);
    }
    .summary-item {
      display: flex;
      justify-content: space-between;
      margin-bottom: 15px;
      font-size: 1.05rem;
    }
    .summary-item.total {
      font-size: 1.5rem;
      font-weight: bold;
      color: var(--color-primary);
      border-top: 1px solid var(--color-border);
      padding-top: 20px;
      margin-top: 15px;
    }
    
    /* Selection Cards */
    .selection-card {
      display: flex;
      align-items: center;
      gap: 20px;
      background: var(--color-bg);
      padding: 20px;
      border-radius: var(--radius-md);
      border: 1px solid var(--color-border);
    }
    .selection-img {
      width: 90px;
      height: 90px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--color-primary);
    }
    .package-img {
      border-radius: 15px;
    }
    .selection-details .sel-title {
      font-size: 1.3rem;
      font-weight: 700;
      margin-bottom: 5px;
      color: var(--color-text);
      font-family: var(--font-body);
    }
    .selection-details p {
      font-size: 0.95rem;
      color: var(--color-text-light);
    }
    .change-btn {
      margin-left: auto;
      color: var(--color-primary);
      background: none;
      border: none;
      font-weight: bold;
      font-size: 1rem;
      cursor: pointer;
      font-family: var(--font-body);
      transition: transform 0.2s;
    }
    .change-btn:hover {
      transform: scale(1.05);
    }
    
    /* Checkboxes/Addons */
    .addon-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .addon-card {
      display: flex;
      align-items: center;
      gap: 15px;
      padding: 15px;
      background: var(--color-bg);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: all 0.3s;
    }
    .addon-card:hover {
      border-color: var(--color-primary);
    }
    .addon-card input {
      accent-color: var(--color-primary);
      width: 22px;
      height: 22px;
    }
    .addon-info {
      flex-grow: 1;
    }
    .addon-info .add-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 3px;
      color: var(--color-text);
    }
    .addon-price {
      font-weight: bold;
      color: var(--color-primary);
      font-size: 1.1rem;
    }
    
    /* FAQs */
    .faq-section {
      max-width: 900px;
      margin: 80px auto 120px;
      padding: 0 20px;
    }
    .faq-title {
      text-align: center;
      font-size: 3rem;
      font-family: var(--font-magic);
      margin-bottom: 40px;
      color: var(--color-text);
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
    
    @media (max-width: 768px) {
      .form-grid, .addon-grid {
        grid-template-columns: 1fr;
      }
      .selection-card {
        flex-direction: column;
        text-align: center;
        align-items: center;
      }
      .change-btn {
        margin: 10px auto 0;
      }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <main>
    <!-- HERO -->
    <section class="booking-hero">
      <div class="container reveal">
        <h1>Secure Your <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Magical</span> Experience</h1>
        <p>Complete your booking details below to finalize your perfect celebration.</p>
      </div>
    </section>

    <!-- BOOKING LAYOUT -->
    <section class="booking-container">
      
      <!-- LEFT: FORM -->
      <form class="booking-main">
        
        <!-- SELECTED ENTERTAINER -->
        <div class="booking-section reveal">
          <h3 class="booking-section-title">Selected Entertainer</h3>
          <div class="selection-card">
            <img src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias" class="selection-img">
            <div class="selection-details">
              <div class="sel-title">Elias</div>
              <p>Magician & Illusionist • <i class="fa-solid fa-star" style="color: #FFD700;"></i> 5.0</p>
              <a href="entertainer_detail.html?id=elias" style="font-size: 0.95rem; color: var(--color-secondary); text-decoration: underline; margin-top: 5px; display: inline-block;">View Profile</a>
            </div>
            <button type="button" class="change-btn">Change</button>
          </div>
        </div>

        <!-- SELECTED PACKAGE -->
        <div class="booking-section reveal">
          <h3 class="booking-section-title">Selected Package</h3>
          <div class="selection-card">
            <img src="assets/images/magic_show_party_1790842468826.jpg" alt="Sparkle Party" class="selection-img package-img">
            <div class="selection-details">
              <div class="sel-title">Sparkle Party</div>
              <p>1 hour • 1 Entertainer • Interactive Games</p>
            </div>
            <button type="button" class="change-btn">Change</button>
          </div>
        </div>

        <!-- EVENT DETAILS -->
        <div class="booking-section reveal">
          <h3 class="booking-section-title">Event Details</h3>
          <div class="form-grid">
            <div class="form-group">
              <label class="form-label">Event Type</label>
              <select class="form-control">
                <option>Birthday Party</option>
                <option>School Event</option>
                <option>Themed Party</option>
                <option>Other Celebration</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Guest Count</label>
              <select class="form-control">
                <option>1-10 Guests</option>
                <option>11-20 Guests</option>
                <option>21-50 Guests</option>
                <option>50+ Guests</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Event Date</label>
              <input type="date" class="form-control">
            </div>
            <div class="form-group">
              <label class="form-label">Start Time</label>
              <input type="time" class="form-control">
            </div>
            <div class="form-group full">
              <label class="form-label">Duration</label>
              <input type="text" class="form-control" value="1 hour" readonly style="background: rgba(255,255,255,0.05); color: var(--color-text-light);">
            </div>
          </div>
        </div>

        <!-- LOCATION DETAILS -->
        <div class="booking-section reveal">
          <h3 class="booking-section-title">Location Details</h3>
          <div class="form-grid">
            <div class="form-group full">
              <label class="form-label">Event Address</label>
              <input type="text" class="form-control" placeholder="123 Magic Street">
            </div>
            <div class="form-group">
              <label class="form-label">City</label>
              <input type="text" class="form-control" placeholder="City">
            </div>
            <div class="form-group">
              <label class="form-label">Venue Type</label>
              <select class="form-control">
                <option>Indoor</option>
                <option>Outdoor</option>
              </select>
            </div>
          </div>
        </div>

        <!-- CUSTOMIZE EXPERIENCE -->
        <div class="booking-section reveal">
          <h3 class="booking-section-title">Customize Your Experience</h3>
          <p style="margin-bottom: 25px; color: var(--color-text-light); font-size: 1.05rem;">Optional add-ons to make your event even more special.</p>
          <div class="addon-grid">
            <label class="addon-card">
              <input type="checkbox">
              <div class="addon-info">
                <div class="add-title">Balloon Decor</div>
                <div style="font-size: 0.9rem; color: var(--color-text-light);">Colorful party decor</div>
              </div>
              <div class="addon-price">+$15</div>
            </label>
            <label class="addon-card">
              <input type="checkbox">
              <div class="addon-info">
                <div class="add-title">Extra Entertainer</div>
                <div style="font-size: 0.9rem; color: var(--color-text-light);">Another performer</div>
              </div>
              <div class="addon-price">+$50</div>
            </label>
            <label class="addon-card">
              <input type="checkbox">
              <div class="addon-info">
                <div class="add-title">Photo Experience</div>
                <div style="font-size: 0.9rem; color: var(--color-text-light);">Extra photo moments</div>
              </div>
              <div class="addon-price">+$25</div>
            </label>
            <label class="addon-card">
              <input type="checkbox">
              <div class="addon-info">
                <div class="add-title">Special Props</div>
                <div style="font-size: 0.9rem; color: var(--color-text-light);">Props for fun</div>
              </div>
              <div class="addon-price">+$10</div>
            </label>
          </div>
          <div class="form-group full" style="margin-top: 30px;">
            <label class="form-label">Special Requests</label>
            <textarea class="form-control" rows="4" placeholder="Any special instructions, theme requests, or important notes..."></textarea>
          </div>
        </div>

        <!-- CONTACT INFO -->
        <div class="booking-section reveal">
          <h3 class="booking-section-title">Contact Information</h3>
          <div class="form-grid">
            <div class="form-group full">
              <label class="form-label">Full Name</label>
              <input type="text" class="form-control" placeholder="Your Name">
            </div>
            <div class="form-group">
              <label class="form-label">Email Address</label>
              <input type="email" class="form-control" placeholder="you@example.com">
            </div>
            <div class="form-group">
              <label class="form-label">Phone Number</label>
              <input type="tel" class="form-control" placeholder="(555) 123-4567">
            </div>
          </div>
        </div>

        <!-- TERMS -->
        <div class="booking-section reveal">
          <h3 class="booking-section-title">Terms & Cancellation Policy</h3>
          <p style="font-size: 1rem; color: var(--color-text-light); margin-bottom: 20px; line-height: 1.6;">By booking, you agree to our terms. Cancellations made 48 hours prior to the event will receive a full refund. Cancellations made later may incur a fee.</p>
          <label style="display: flex; align-items: center; gap: 15px; cursor: pointer; background: var(--color-bg); padding: 20px; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
            <input type="checkbox" style="width: 22px; height: 22px; accent-color: var(--color-primary);">
            <span style="font-weight: bold; font-size: 1.05rem; color: var(--color-text);">I agree to the Terms & Conditions</span>
          </label>
        </div>

        <!-- CTA -->
        <div class="reveal" style="margin-top: 10px;">
          <button type="button" class="btn btn-primary" style="width: 100%; padding: 22px; font-size: 1.3rem; border-radius: var(--radius-pill);">Send Booking Request <i class="fa-solid fa-paper-plane" style="margin-left: 10px;"></i></button>
        </div>
      </form>

      <!-- RIGHT: SIDEBAR -->
      <aside class="summary-sidebar reveal">
        <h3 class="summary-title">Booking Summary</h3>
        <div class="summary-item">
          <span style="color: var(--color-text-light);">Package</span>
          <span style="font-weight: bold; color: var(--color-text);">Sparkle Party</span>
        </div>
        <div class="summary-item">
          <span style="color: var(--color-text-light);">Entertainer</span>
          <span style="font-weight: bold; color: var(--color-text);">Elias</span>
        </div>
        <div class="summary-item">
          <span style="color: var(--color-text-light);">Event Type</span>
          <span style="font-weight: bold; color: var(--color-text);">Birthday Party</span>
        </div>
        <div class="summary-item">
          <span style="color: var(--color-text-light);">Date</span>
          <span style="font-weight: bold; color: var(--color-text);">Pending</span>
        </div>
        <div class="summary-item">
          <span style="color: var(--color-text-light);">Add-ons</span>
          <span style="font-weight: bold; color: var(--color-text);">$0</span>
        </div>
        <div class="summary-item total">
          <span>Estimated Total</span>
          <span>$99</span>
        </div>
        
        <p style="font-size: 0.9rem; color: var(--color-text-light); text-align: center; margin-top: 30px;">
          <i class="fa-solid fa-shield-halved" style="color: var(--color-primary); margin-right: 5px;"></i> Safe and secure booking process.
        </p>
      </aside>
    </section>

    <!-- FAQS -->
    <section class="faq-section reveal">
      <h2 class="faq-title">Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">
          When do I need to pay? <i class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
        </div>
        <div class="faq-answer">
          <p>You do not need to pay to submit a booking request. Once we review your details and confirm our availability, we will send an invoice for a deposit to secure your date.</p>
        </div>
      </div>
      <div class="faq-item">
        <div class="faq-question">
          Can I change my package later? <i class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
        </div>
        <div class="faq-answer">
          <p>Absolutely! You can modify your package, switch entertainers, or add optional extras up to 48 hours before the event date, subject to availability.</p>
        </div>
      </div>
      <div class="faq-item">
        <div class="faq-question">
          What is the cancellation policy? <i class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
        </div>
        <div class="faq-answer">
          <p>We offer full refunds for cancellations made at least 48 hours in advance. Last minute cancellations may forfeit the deposit as we block out our calendar for you.</p>
        </div>
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
    // Simple FAQ Accordion Logic
    document.addEventListener('DOMContentLoaded', () => {
      const faqItems = document.querySelectorAll('.faq-item');
      faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
          const isActive = item.classList.contains('active');
          // Close all
          faqItems.forEach(i => i.classList.remove('active'));
          // Toggle current
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

with open('c:/Users/vigas/Desktop/magiqo/booking.html', 'w', encoding='utf-8') as f:
    f.write(booking_html_content)

print("Booking completely redesigned.")
