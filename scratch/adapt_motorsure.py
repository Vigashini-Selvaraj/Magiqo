import os

new_footer = """<style>
/* Magiqo-adapted Dark Footer (Based on your provided code) */
.magiqo-footer {
  font-family: var(--font-primary, 'Inter', sans-serif);
  background: #180D20; /* Magiqo Dark Theme */
  color: #91a1b1;
  padding: 80px 6.8% 0;
  position: relative;
}

.magiqo-footer-container {
  max-width: 1200px;
  margin: auto;
  display: grid;
  grid-template-columns: 1.65fr 1fr 1.05fr 1.15fr;
  gap: 65px;
  padding-bottom: 80px;
}

/* Brand */
.magiqo-footer-logo {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
  text-decoration: none;
}

.magiqo-logo-img {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  object-fit: cover;
}

.magiqo-logo-name {
  font-family: var(--font-magic, 'Inter', sans-serif);
  color: #f8f5f0;
  font-size: 26px;
  font-weight: 700;
}

.magiqo-footer-about {
  font-size: 16px;
  line-height: 1.75;
  max-width: 460px;
  margin-bottom: 30px;
  color: #91a1b1;
}

/* Social links */
.magiqo-social-links {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.magiqo-social-links a {
  width: 42px;
  height: 42px;
  border: 1px solid #343a3c;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #929da4;
  text-decoration: none;
  transition: 0.3s ease;
}

.magiqo-social-links a:hover {
  background: var(--color-primary, #D24B76);
  color: #ffffff;
  border-color: var(--color-primary, #D24B76);
  transform: translateY(-4px);
}

/* Headings */
.magiqo-footer-column h3 {
  font-family: var(--font-magic, 'Inter', sans-serif);
  color: #f8f5f0;
  font-size: 21px;
  font-weight: 700;
  margin-bottom: 32px;
}

/* Links */
.magiqo-footer-column ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.magiqo-footer-column ul li {
  margin-bottom: 16px;
}

.magiqo-footer-column ul li a {
  color: #91a1b1;
  text-decoration: none;
  font-size: 15px;
  transition: color 0.3s ease, padding 0.3s ease;
}

.magiqo-footer-column ul li a:hover {
  color: var(--color-primary, #D24B76);
  padding-left: 5px;
}

/* Contact */
.magiqo-contact-item {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  align-items: flex-start;
  font-size: 15px;
  line-height: 1.6;
  color: #91a1b1;
}

.magiqo-contact-icon {
  color: var(--color-primary, #D24B76);
  margin-top: 2px;
}

.magiqo-contact-item a {
  color: inherit;
  text-decoration: none;
  transition: color 0.3s ease;
}

.magiqo-contact-item a:hover {
  color: var(--color-primary, #D24B76);
}

/* Bottom bar */
.magiqo-footer-bottom {
  border-top: 1px solid #303536;
  min-height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  max-width: 1200px;
  margin: auto;
  font-size: 14px;
  color: #718294;
}

.magiqo-footer-legal {
  display: flex;
  gap: 32px;
  flex-wrap: wrap;
}

.magiqo-footer-legal a {
  color: #718294;
  text-decoration: none;
  transition: color 0.3s ease;
}

.magiqo-footer-legal a:hover {
  color: var(--color-primary, #D24B76);
}

/* Back to top */
.magiqo-back-to-top {
  position: absolute;
  right: 2.5%;
  bottom: 0;
  transform: translateY(0);
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: var(--color-primary, #D24B76);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  box-shadow: 0 0 25px rgba(210,75,118,0.3);
  transition: 0.3s ease;
}
.magiqo-back-to-top:hover {
  transform: translateY(-6px);
  box-shadow: 0 5px 25px rgba(210,75,118,0.5);
}

/* Responsive */
@media (max-width: 1100px) {
  .magiqo-footer-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 55px 40px;
  }
  .magiqo-footer {
    padding: 70px 6% 0;
  }
}
@media (max-width: 600px) {
  .magiqo-footer {
    padding: 55px 7% 0;
  }
  .magiqo-footer-container {
    grid-template-columns: 1fr;
    gap: 38px;
    padding-bottom: 45px;
  }
  .magiqo-footer-bottom {
    flex-direction: column;
    align-items: flex-start;
    padding: 22px 0 28px;
  }
  .magiqo-back-to-top {
    right: 5%;
    bottom: 10px;
  }
}
</style>

<footer class="magiqo-footer">
  <div class="magiqo-footer-container">

    <!-- Brand -->
    <div class="magiqo-footer-brand">
      <a href="index.html" class="magiqo-footer-logo">
        <img src="assets/images/magiqo_logo_1790915438485.jpg" alt="Magiqo" class="magiqo-logo-img">
        <span class="magiqo-logo-name">MAGIQO</span>
      </a>

      <p class="magiqo-footer-about">
        A modern destination for discovering entertainers, exploring ideas and planning unforgettable celebrations.
      </p>

      <div class="magiqo-social-links">
        <a href="#" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
        <a href="#" aria-label="Twitter"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
        <a href="#" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        <a href="#" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
        <a href="#" aria-label="YouTube"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
      </div>
    </div>

    <!-- Quick Links -->
    <div class="magiqo-footer-column">
      <h3>Quick Links</h3>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="home2.html">Home 2</a></li>
        <li><a href="about.html">About Us</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="packages.html">Packages</a></li>
        <li><a href="entertainers.html">Entertainers</a></li>
      </ul>
    </div>

    <!-- Support -->
    <div class="magiqo-footer-column">
      <h3>Support</h3>
      <ul>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="faqs.html">FAQ</a></li>
        <li><a href="help.html">Help</a></li>
        <li><a href="privacy.html">Privacy Policy</a></li>
        <li><a href="terms.html">Terms and Condition</a></li>
      </ul>
    </div>

    <!-- Contact Us -->
    <div class="magiqo-footer-column">
      <h3>Contact Us</h3>

      <div class="magiqo-contact-item">
        <svg class="magiqo-contact-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
        <span>
          <a href="mailto:hello@magiqo.com">hello@magiqo.com</a><br>
        </span>
      </div>

      <div class="magiqo-contact-item">
        <svg class="magiqo-contact-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        <span>
          <a href="tel:+15551234567">+1 (555) 123-4567</a>
        </span>
      </div>

      <div class="magiqo-contact-item">
        <svg class="magiqo-contact-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
        <span>123 Magical Lane, NY</span>
      </div>

      <div class="magiqo-contact-item">
        <svg class="magiqo-contact-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        <span>Mon - Sat: 9AM - 6PM</span>
      </div>

    </div>

  </div>

  <!-- Copyright -->
  <div class="magiqo-footer-bottom">
    <p>© 2026 MAGIQO. All rights reserved.</p>

    <div class="magiqo-footer-legal">
      <a href="privacy.html">Privacy Policy</a>
      <a href="terms.html">Terms &amp; Conditions</a>
    </div>
  </div>

  <!-- Back to top (adapted) -->
  <a href="#top" class="magiqo-back-to-top" aria-label="Back to top">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg>
  </a>
</footer>"""

with open('c:/Users/vigas/Desktop/magiqo/components/footer.html', 'w', encoding='utf-8') as f:
    f.write(new_footer)
