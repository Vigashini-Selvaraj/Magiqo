import os

new_footer = """<footer style="font-family: var(--font-primary, 'Inter', sans-serif) !important; background: #180D20 !important; color: #91a1b1 !important; padding: 5rem 0 2rem !important; position: relative !important;">
  <div style="max-width: 1200px !important; margin: 0 auto !important; padding: 0 2rem !important;">
    
    <!-- Bulletproof Flexbox Layout -->
    <div style="display: flex !important; flex-wrap: wrap !important; justify-content: space-between !important; gap: 3rem !important; margin-bottom: 4rem !important;">
      
      <!-- Column 1: Brand -->
      <div style="flex: 1.5 !important; min-width: 250px !important;">
        <a href="index.html" style="display: flex !important; align-items: center !important; gap: 15px !important; margin-bottom: 30px !important; text-decoration: none !important;">
          <img src="assets/images/magiqo_logo_1790915438485.jpg" alt="Magiqo" style="width: 45px !important; height: 45px !important; border-radius: 50% !important; object-fit: cover !important;">
          <span style="font-family: var(--font-magic, 'Inter', sans-serif) !important; color: #f8f5f0 !important; font-size: 26px !important; font-weight: 700 !important;">MAGIQO</span>
        </a>

        <p style="font-size: 16px !important; line-height: 1.75 !important; max-width: 320px !important; margin-bottom: 30px !important; color: #91a1b1 !important;">
          A modern destination for discovering entertainers, exploring ideas and planning unforgettable celebrations.
        </p>

        <div style="display: flex !important; gap: 15px !important; flex-wrap: wrap !important;">
          <a href="#" aria-label="Facebook" style="width: 42px !important; height: 42px !important; border: 1px solid #343a3c !important; border-radius: 50% !important; display: flex !important; align-items: center !important; justify-content: center !important; color: #929da4 !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.background='#D24B76'; this.style.color='#ffffff'; this.style.borderColor='#D24B76';" onmouseout="this.style.background='transparent'; this.style.color='#929da4'; this.style.borderColor='#343a3c';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
          <a href="#" aria-label="Twitter" style="width: 42px !important; height: 42px !important; border: 1px solid #343a3c !important; border-radius: 50% !important; display: flex !important; align-items: center !important; justify-content: center !important; color: #929da4 !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.background='#D24B76'; this.style.color='#ffffff'; this.style.borderColor='#D24B76';" onmouseout="this.style.background='transparent'; this.style.color='#929da4'; this.style.borderColor='#343a3c';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          <a href="#" aria-label="Instagram" style="width: 42px !important; height: 42px !important; border: 1px solid #343a3c !important; border-radius: 50% !important; display: flex !important; align-items: center !important; justify-content: center !important; color: #929da4 !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.background='#D24B76'; this.style.color='#ffffff'; this.style.borderColor='#D24B76';" onmouseout="this.style.background='transparent'; this.style.color='#929da4'; this.style.borderColor='#343a3c';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
          <a href="#" aria-label="LinkedIn" style="width: 42px !important; height: 42px !important; border: 1px solid #343a3c !important; border-radius: 50% !important; display: flex !important; align-items: center !important; justify-content: center !important; color: #929da4 !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.background='#D24B76'; this.style.color='#ffffff'; this.style.borderColor='#D24B76';" onmouseout="this.style.background='transparent'; this.style.color='#929da4'; this.style.borderColor='#343a3c';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
          <a href="#" aria-label="YouTube" style="width: 42px !important; height: 42px !important; border: 1px solid #343a3c !important; border-radius: 50% !important; display: flex !important; align-items: center !important; justify-content: center !important; color: #929da4 !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.background='#D24B76'; this.style.color='#ffffff'; this.style.borderColor='#D24B76';" onmouseout="this.style.background='transparent'; this.style.color='#929da4'; this.style.borderColor='#343a3c';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
        </div>
      </div>

      <!-- Column 2: Quick Links -->
      <div style="flex: 1 !important; min-width: 150px !important;">
        <h3 style="font-family: var(--font-magic, 'Inter', sans-serif) !important; color: #f8f5f0 !important; font-size: 21px !important; font-weight: 700 !important; margin-bottom: 32px !important;">Quick Links</h3>
        <ul style="list-style: none !important; padding: 0 !important; margin: 0 !important; display: flex !important; flex-direction: column !important; gap: 16px !important;">
          <li><a href="index.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Home</a></li>
          <li><a href="home2.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Home 2</a></li>
          <li><a href="about.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">About</a></li>
          <li><a href="services.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Services</a></li>
          <li><a href="blog.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Blog</a></li>
          <li><a href="packages.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Packages</a></li>
          <li><a href="entertainers.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Entertainers</a></li>
        </ul>
      </div>

      <!-- Column 3: Support -->
      <div style="flex: 1 !important; min-width: 150px !important;">
        <h3 style="font-family: var(--font-magic, 'Inter', sans-serif) !important; color: #f8f5f0 !important; font-size: 21px !important; font-weight: 700 !important; margin-bottom: 32px !important;">Support</h3>
        <ul style="list-style: none !important; padding: 0 !important; margin: 0 !important; display: flex !important; flex-direction: column !important; gap: 16px !important;">
          <li><a href="contact.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Contact</a></li>
          <li><a href="faqs.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">FAQ</a></li>
          <li><a href="help.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Help</a></li>
          <li><a href="privacy.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Privacy Policy</a></li>
          <li><a href="terms.html" style="color: #91a1b1 !important; text-decoration: none !important; font-size: 15px !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#91a1b1'">Terms & Condition</a></li>
        </ul>
      </div>

      <!-- Column 4: Contact Us -->
      <div style="flex: 1.2 !important; min-width: 200px !important;">
        <h3 style="font-family: var(--font-magic, 'Inter', sans-serif) !important; color: #f8f5f0 !important; font-size: 21px !important; font-weight: 700 !important; margin-bottom: 32px !important;">Contact Us</h3>
        <ul style="list-style: none !important; padding: 0 !important; margin: 0 !important; display: flex !important; flex-direction: column !important; gap: 20px !important;">
          <li style="display: flex !important; gap: 12px !important; align-items: flex-start !important; font-size: 15px !important; line-height: 1.6 !important; color: #91a1b1 !important;">
            <svg style="color: #D24B76 !important; margin-top: 2px !important;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            <a href="mailto:hello@magiqo.com" style="color: inherit !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='inherit'">hello@magiqo.com</a>
          </li>
          <li style="display: flex !important; gap: 12px !important; align-items: flex-start !important; font-size: 15px !important; line-height: 1.6 !important; color: #91a1b1 !important;">
            <svg style="color: #D24B76 !important; margin-top: 2px !important;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <a href="tel:+15551234567" style="color: inherit !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='inherit'">+1 (555) 123-4567</a>
          </li>
          <li style="display: flex !important; gap: 12px !important; align-items: flex-start !important; font-size: 15px !important; line-height: 1.6 !important; color: #91a1b1 !important;">
            <svg style="color: #D24B76 !important; margin-top: 2px !important;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            <span>123 Magical Lane, NY</span>
          </li>
          <li style="display: flex !important; gap: 12px !important; align-items: flex-start !important; font-size: 15px !important; line-height: 1.6 !important; color: #91a1b1 !important;">
            <svg style="color: #D24B76 !important; margin-top: 2px !important;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <span>Mon - Sat: 9AM - 6PM</span>
          </li>
        </ul>
      </div>

    </div>

    <!-- Copyright -->
    <div style="border-top: 1px solid #303536 !important; min-height: 70px !important; display: flex !important; justify-content: space-between !important; align-items: center !important; flex-wrap: wrap !important; gap: 20px !important; font-size: 14px !important; color: #718294 !important;">
      <p style="margin: 0 !important;">© 2026 MAGIQO. All rights reserved.</p>
      <div style="display: flex !important; gap: 32px !important; flex-wrap: wrap !important;">
        <a href="privacy.html" style="color: #718294 !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#718294'">Privacy Policy</a>
        <a href="terms.html" style="color: #718294 !important; text-decoration: none !important; transition: 0.3s ease !important;" onmouseover="this.style.color='#D24B76'" onmouseout="this.style.color='#718294'">Terms &amp; Conditions</a>
      </div>
    </div>

  </div>
</footer>"""

with open('c:/Users/vigas/Desktop/magiqo/components/footer.html', 'w', encoding='utf-8') as f:
    f.write(new_footer)
