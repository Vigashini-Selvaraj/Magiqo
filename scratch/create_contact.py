contact_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* Hero Section */
    .contact-hero {
      padding: 160px 0 80px;
      background-color: var(--color-bg);
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    .contact-hero h1 {
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-family: var(--font-magic);
      line-height: 1.2;
      margin-bottom: 20px;
    }
    .contact-hero p {
      max-width: 650px;
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

    /* Common Section Styles */
    .section-title {
      font-family: var(--font-magic);
      font-size: 3rem;
      text-align: center;
      margin-bottom: 20px;
    }
    .section-desc {
      text-align: center;
      color: var(--color-text-light);
      max-width: 600px;
      margin: 0 auto 50px;
      font-size: 1.15rem;
    }
    
    .text-pink { color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none; }
    .text-blue { color: #3895c8; -webkit-text-fill-color: #3895c8; background: none; }

    /* Contact Cards */
    .contact-cards-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 30px;
      margin-bottom: 80px;
    }
    .contact-card {
      background: var(--color-surface);
      padding: 40px 30px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      text-align: center;
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .contact-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 15px 30px var(--color-shadow);
      border-color: #3895c8;
    }
    .contact-card i {
      font-size: 2.5rem;
      color: var(--color-primary);
      margin-bottom: 20px;
      display: inline-block;
      transition: transform 0.3s;
    }
    .contact-card:hover i { transform: scale(1.1); color: #3895c8; }
    .contact-card h3 {
      font-family: var(--font-heading);
      font-size: 1.3rem;
      margin-bottom: 10px;
      color: var(--color-text);
    }
    .contact-card p {
      color: var(--color-text-light);
      font-size: 1rem;
      line-height: 1.5;
    }

    /* Layout for Form & Map */
    .contact-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 50px;
      margin-bottom: 100px;
      align-items: stretch;
    }

    /* Form */
    .contact-form-box {
      background: var(--color-surface);
      padding: 50px;
      border-radius: var(--radius-xl);
      border: 1px solid var(--color-border);
      box-shadow: 0 20px 50px var(--color-shadow);
    }
    .form-group { margin-bottom: 20px; }
    .form-group.full { grid-column: 1 / -1; }
    .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .form-label {
      display: block;
      margin-bottom: 8px;
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
    textarea.form-control { resize: vertical; min-height: 150px; }

    /* Map */
    .map-container {
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--color-border);
      box-shadow: 0 20px 50px var(--color-shadow);
      height: 100%;
      min-height: 400px;
    }
    .map-container iframe {
      width: 100%;
      height: 100%;
      border: 0;
    }

    /* Event Types Cards */
    .events-section { padding: 100px 0; background: var(--color-bg); }
    .events-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
    }
    .event-card {
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      aspect-ratio: 4/5;
      cursor: pointer;
    }
    .event-card img {
      width: 100%; height: 100%;
      object-fit: cover;
      transition: transform 0.5s;
    }
    .event-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
      z-index: 1;
    }
    .event-card:hover img { transform: scale(1.1); }
    .event-card h3 {
      position: absolute;
      bottom: 20px;
      left: 20px;
      color: white;
      z-index: 2;
      font-family: var(--font-heading);
      font-size: 1.25rem;
    }

    /* How We Can Help */
    .help-section { padding: 100px 0; }
    .help-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 30px;
    }
    .help-card {
      display: flex;
      gap: 20px;
      background: var(--color-surface);
      padding: 30px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      align-items: flex-start;
      transition: transform 0.3s;
    }
    .help-card:hover { transform: translateX(10px); border-color: var(--color-primary); }
    .help-icon {
      width: 50px; height: 50px;
      border-radius: 50%;
      background: rgba(210, 75, 118, 0.1);
      color: var(--color-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      flex-shrink: 0;
    }
    .help-text h4 { font-family: var(--font-heading); font-size: 1.15rem; margin-bottom: 8px; color: var(--color-text); }
    .help-text p { color: var(--color-text-light); font-size: 0.95rem; line-height: 1.5; }

    /* Why Contact Magiqo (Features) */
    .why-section { padding: 100px 0; background: var(--color-surface); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border); }
    .why-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 40px;
      text-align: center;
    }
    .why-item i { font-size: 3rem; color: #3895c8; margin-bottom: 20px; }
    .why-item h4 { font-size: 1.2rem; margin-bottom: 10px; color: var(--color-text); }
    .why-item p { color: var(--color-text-light); line-height: 1.6; }

    /* Meet Our Experts */
    .team-section { padding: 100px 0; }
    .team-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 30px;
    }
    .team-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      text-align: center;
      transition: transform 0.3s;
    }
    .team-card:hover { transform: translateY(-10px); box-shadow: 0 15px 30px var(--color-shadow); }
    .team-img { width: 100%; height: 250px; object-fit: cover; border-bottom: 3px solid var(--color-primary); }
    .team-info { padding: 25px; }
    .team-info h4 { font-family: var(--font-magic); font-size: 1.5rem; color: var(--color-text); margin-bottom: 5px; }
    .team-info span { color: #3895c8; font-weight: bold; font-size: 0.9rem; display: block; margin-bottom: 15px; }
    .team-info p { color: var(--color-text-light); font-size: 0.95rem; line-height: 1.5; }

    /* FAQs */
    .faq-section { max-width: 900px; margin: 0 auto 100px; padding: 0 20px; }

    /* Social / Insta Gallery */
    .social-section { padding: 80px 0 120px; text-align: center; overflow: hidden; }
    .insta-grid {
      display: flex;
      gap: 15px;
      margin-top: 40px;
      justify-content: center;
      flex-wrap: wrap;
    }
    .insta-item {
      width: 200px; height: 200px;
      border-radius: var(--radius-md);
      overflow: hidden;
      position: relative;
    }
    .insta-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s; }
    .insta-item::after {
      content: '\\f16d';
      font-family: 'Font Awesome 6 Brands';
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.6);
      color: white;
      font-size: 3rem;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.3s;
    }
    .insta-item:hover img { transform: scale(1.1); }
    .insta-item:hover::after { opacity: 1; }

    /* Final CTA */
    .cta-section {
      text-align: center;
      padding: 100px 30px;
      background: var(--color-surface);
      border-radius: var(--radius-xl);
      margin: 0 20px 100px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 25px 60px var(--color-shadow), inset 0 0 0 8px var(--color-bg), inset 0 0 0 10px var(--color-primary);
    }
    .cta-section h2 { font-size: clamp(3rem, 5vw, 4.5rem); margin-bottom: 30px; }
    
    @media (max-width: 992px) {
      .contact-layout { grid-template-columns: 1fr; }
      .map-container { min-height: 350px; }
    }
    @media (max-width: 768px) {
      .form-row { grid-template-columns: 1fr; }
      .contact-form-box { padding: 30px 20px; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <main>
    <!-- 1. HERO -->
    <section class="contact-hero">
      <div class="hero-bubble hero-bubble-1"></div>
      <div class="hero-bubble hero-bubble-2"></div>
      <div class="container reveal">
        <h1><span class="text-pink">Let's Make Your</span> <br><span class="text-blue">Celebration Magical</span></h1>
        <p>Whether you have a question about packages, need custom event planning, or just want to say hi, we're here to help.</p>
      </div>
    </section>

    <div class="container">
      
      <!-- 2. CONTACT INFO CARDS -->
      <div class="contact-cards-container reveal">
        <div class="contact-card">
          <i class="fa-solid fa-phone"></i>
          <h3>Call Us</h3>
          <p>+1 (555) 123-4567<br>Mon-Sat: 9AM - 7PM</p>
        </div>
        <div class="contact-card">
          <i class="fa-solid fa-envelope"></i>
          <h3>Email Us</h3>
          <p>hello@magiqo.com<br>Support 24/7</p>
        </div>
        <div class="contact-card">
          <i class="fa-solid fa-location-dot"></i>
          <h3>Visit Us</h3>
          <p>123 Magic Boulevard<br>Wonderland City, NY 10001</p>
        </div>
      </div>

      <!-- 3. FORM & 8. MAP -->
      <div class="contact-layout reveal">
        <div class="contact-form-box">
          <h3 style="font-family: var(--font-magic); font-size: 2.2rem; color: var(--color-primary); margin-bottom: 25px;">Send a Message</h3>
          <form>
            <div class="form-row">
              <div class="form-group">
                <label class="form-label">Your Name</label>
                <input type="text" class="form-control" placeholder="John Doe" required>
              </div>
              <div class="form-group">
                <label class="form-label">Phone Number</label>
                <input type="tel" class="form-control" placeholder="(555) 000-0000" required>
              </div>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label class="form-label">Email Address</label>
                <input type="email" class="form-control" placeholder="john@example.com" required>
              </div>
              <div class="form-group">
                <label class="form-label">Event Date</label>
                <input type="date" class="form-control">
              </div>
            </div>
            <div class="form-group full">
              <label class="form-label">Event Type</label>
              <select class="form-control">
                <option>Birthday Party</option>
                <option>School Event</option>
                <option>Wedding/Baby Shower</option>
                <option>Corporate Family Day</option>
                <option>Other</option>
              </select>
            </div>
            <div class="form-group full">
              <label class="form-label">Your Message</label>
              <textarea class="form-control" placeholder="Tell us about your magical ideas..." required></textarea>
            </div>
            <button type="button" class="btn btn-primary" style="width: 100%; padding: 15px; font-size: 1.1rem; margin-top: 10px;">Send Message <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i></button>
          </form>
        </div>
        
        <div class="map-container">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.2528000654!2d-74.1448301594916!3d40.69766374865766!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </div>

    <!-- 4. CHOOSE YOUR EVENT -->
    <section class="events-section reveal">
      <div class="container">
        <h2 class="section-title"><span class="text-pink">Perfect For</span> <span class="text-blue">Every Occasion</span></h2>
        <div class="events-grid">
          <div class="event-card">
            <img src="assets/images/about_kids_birthday.jpg" alt="Birthdays">
            <h3>Birthdays</h3>
          </div>
          <div class="event-card">
            <img src="assets/images/blog_party_ideas_1790831919409.jpg" alt="Weddings">
            <h3>Weddings</h3>
          </div>
          <div class="event-card">
            <img src="assets/images/princess_party_1790842645232.jpg" alt="Baby Showers">
            <h3>Baby Showers</h3>
          </div>
          <div class="event-card">
            <img src="assets/images/magic_show_party_1790842468826.jpg" alt="School Events">
            <h3>School Events</h3>
          </div>
          <div class="event-card">
            <img src="assets/images/superhero_party_1790842695325.jpg" alt="Other">
            <h3>Other Events</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. HOW WE CAN HELP -->
    <section class="help-section reveal">
      <div class="container">
        <h2 class="section-title"><span class="text-pink">How We</span> <span class="text-blue">Can Help</span></h2>
        <div class="help-grid">
          <div class="help-card">
            <div class="help-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
            <div class="help-text">
              <h4>Entertainer Bookings</h4>
              <p>Looking for a specific magician, clown, or princess? We match you with the perfect talent.</p>
            </div>
          </div>
          <div class="help-card">
            <div class="help-icon"><i class="fa-solid fa-box-open"></i></div>
            <div class="help-text">
              <h4>Package Enquiries</h4>
              <p>Need help understanding what's included in the Sparkle or Ultimate packages? Just ask!</p>
            </div>
          </div>
          <div class="help-card">
            <div class="help-icon"><i class="fa-solid fa-palette"></i></div>
            <div class="help-text">
              <h4>Custom Themes</h4>
              <p>Have a unique vision? Our decorators and planners can bring any imagination to life.</p>
            </div>
          </div>
          <div class="help-card">
            <div class="help-icon"><i class="fa-solid fa-calendar-star"></i></div>
            <div class="help-text">
              <h4>Full Event Planning</h4>
              <p>Sit back and relax. Let our expert event coordinators handle everything from A to Z.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. WHY CONTACT MAGIQO -->
    <section class="why-section reveal">
      <div class="container">
        <h2 class="section-title"><span class="text-pink">Why Choose</span> <span class="text-blue">Magiqo?</span></h2>
        <div class="why-grid">
          <div class="why-item">
            <i class="fa-solid fa-user-group"></i>
            <h4>Personalized Planning</h4>
            <p>Every child is unique, and so is every party we plan. We listen closely to your specific needs.</p>
          </div>
          <div class="why-item">
            <i class="fa-solid fa-star"></i>
            <h4>Tailored Entertainment</h4>
            <p>We don't do cookie-cutter shows. Our entertainers adapt their acts to fit your crowd.</p>
          </div>
          <div class="why-item">
            <i class="fa-solid fa-lightbulb"></i>
            <h4>Creative Themes</h4>
            <p>From deep jungles to royal castles, our props and costumes are incredibly high quality.</p>
          </div>
          <div class="why-item">
            <i class="fa-solid fa-headset"></i>
            <h4>24/7 Booking Support</h4>
            <p>Last minute changes? Extra guests? Our support team is always just a phone call away.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. MEET OUR EVENT EXPERTS -->
    <section class="team-section reveal">
      <div class="container">
        <h2 class="section-title"><span class="text-pink">Meet Our</span> <span class="text-blue">Event Experts</span></h2>
        <p class="section-desc">The magical minds behind the scenes ensuring your celebration is absolutely flawless.</p>
        
        <div class="team-grid">
          <div class="team-card">
            <img src="assets/images/about_hero.jpg" class="team-img" alt="Sarah">
            <div class="team-info">
              <h4>Sarah Jenkins</h4>
              <span>Lead Event Coordinator</span>
              <p>Sarah has planned over 500 children's parties and knows exactly how to keep the chaos organized.</p>
            </div>
          </div>
          <div class="team-card">
            <img src="assets/images/magician_portrait_1790843004983.jpg" class="team-img" alt="Elias">
            <div class="team-info">
              <h4>Elias Thorne</h4>
              <span>Head of Entertainment</span>
              <p>As our senior magician, Elias vets and trains every single performer who wears a Magiqo badge.</p>
            </div>
          </div>
          <div class="team-card">
            <img src="assets/images/james_boy_smile.jpg" class="team-img" alt="James">
            <div class="team-info">
              <h4>James Wright</h4>
              <span>Creative Director</span>
              <p>James designs all our custom themes, ensuring the decorations and props look breathtaking.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. FAQs -->
    <section class="faq-section reveal">
      <h2 class="section-title"><span class="text-pink">Frequently</span> <span class="text-blue">Asked Questions</span></h2>
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 20px; padding: 25px; box-shadow: 0 5px 15px var(--color-shadow);">
        <h4 style="font-family: var(--font-heading); font-size: 1.25rem; margin-bottom: 12px; color: var(--color-text);">How far in advance should I contact you?</h4>
        <p style="color: var(--color-text-light); line-height: 1.6;">We recommend reaching out at least 4-6 weeks before your desired event date to ensure the best entertainer availability.</p>
      </div>
      <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); margin-bottom: 20px; padding: 25px; box-shadow: 0 5px 15px var(--color-shadow);">
        <h4 style="font-family: var(--font-heading); font-size: 1.25rem; margin-bottom: 12px; color: var(--color-text);">Can I customize a standard package?</h4>
        <p style="color: var(--color-text-light); line-height: 1.6;">Absolutely! Just fill out the form above with your custom requests and our planning team will send a tailored quote.</p>
      </div>
    </section>

    <!-- 10. SOCIAL MEDIA & COMMUNITY -->
    <section class="social-section reveal">
      <div class="container">
        <h2 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 15px; color: var(--color-text);">Join the <span style="color: var(--color-primary);">#MagiqoMoments</span> Community</h2>
        <p style="color: var(--color-text-light); font-size: 1.1rem;">Follow us on Instagram for daily doses of joy and celebration inspiration!</p>
        
        <div class="insta-grid">
          <a href="#" class="insta-item"><img src="assets/images/hero_magician_1790831867453.jpg" alt="Insta 1"></a>
          <a href="#" class="insta-item"><img src="assets/images/magic_show_party_1790842468826.jpg" alt="Insta 2"></a>
          <a href="#" class="insta-item"><img src="assets/images/princess_party_1790842645232.jpg" alt="Insta 3"></a>
          <a href="#" class="insta-item"><img src="assets/images/superhero_party_1790842695325.jpg" alt="Insta 4"></a>
          <a href="#" class="insta-item"><img src="assets/images/about_kids_birthday.jpg" alt="Insta 5"></a>
        </div>
      </div>
    </section>

    <!-- 11. FINAL CTA -->
    <section class="container">
      <div class="cta-section reveal">
        <h2><span class="text-pink">Ready to Plan</span> <br><span class="text-blue">Something Magical?</span></h2>
        <p style="font-size: 1.2rem; color: var(--color-text); margin-bottom: 40px; max-width: 600px; margin-inline: auto;">Don't wait! Secure your date and let us create an unforgettable experience for your child.</p>
        <a href="booking.html" class="btn btn-primary" style="padding: 20px 50px; font-size: 1.3rem; border-radius: var(--radius-pill); text-transform: uppercase; font-weight: bold; letter-spacing: 1px;">Book Now <i class="fa-solid fa-arrow-right" style="margin-left: 10px;"></i></a>
      </div>
    </section>
  </main>

  <!-- 12. FOOTER -->
  <div id="footer"></div>

  <script src="js/theme.js"></script>
  <script src="js/rtl.js"></script>
  <script src="js/components.js"></script>
  <script src="js/main.js"></script>
</body>
</html>
"""

with open('c:/Users/vigas/Desktop/magiqo/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

print("Created contact.html perfectly according to the 12 sections requested.")
