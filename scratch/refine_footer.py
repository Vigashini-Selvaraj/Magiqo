import os

new_footer = """<footer class="footer" style="background: var(--color-surface); padding: 4rem 0 2rem; border-top: 1px solid var(--color-border); font-family: 'Inter', sans-serif;">
  <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1rem;">
    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 2rem; margin-bottom: 3rem;">
      
      <!-- Column 1: Brand -->
      <div style="padding-right: 2rem;">
        <a href="index.html" style="display: flex; align-items: center; gap: 0.75rem; text-decoration: none; color: var(--color-primary); font-family: var(--font-magic); font-size: 2.2rem; font-weight: bold; margin-bottom: 0.5rem;">
          <img src="assets/images/magiqo_logo_1790915438485.jpg" alt="Magiqo Logo" style="height: 45px; border-radius: 50%;"> MAGIQO
        </a>
        <p style="font-style: italic; color: #3895c8; font-weight: 600; font-size: 1.1rem; margin-bottom: 1.5rem; padding-left: 0.5rem;">"Make Their Day Magical."</p>
        
        <div style="display: flex; gap: 1rem; padding-left: 0.5rem;">
          <a href="#" aria-label="Instagram" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #ffe4e6; color: var(--color-primary); text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.background='var(--color-primary)'; this.style.color='white';" onmouseout="this.style.background='#ffe4e6'; this.style.color='var(--color-primary)';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
          <a href="#" aria-label="Facebook" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #ffe4e6; color: var(--color-primary); text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.background='var(--color-primary)'; this.style.color='white';" onmouseout="this.style.background='#ffe4e6'; this.style.color='var(--color-primary)';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
          <a href="#" aria-label="YouTube" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #ffe4e6; color: var(--color-primary); text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.background='var(--color-primary)'; this.style.color='white';" onmouseout="this.style.background='#ffe4e6'; this.style.color='var(--color-primary)';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
          <a href="#" aria-label="TikTok" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #ffe4e6; color: var(--color-primary); text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.background='var(--color-primary)'; this.style.color='white';" onmouseout="this.style.background='#ffe4e6'; this.style.color='var(--color-primary)';"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"></path></svg></a>
        </div>
      </div>

      <!-- Column 2: Quick Links -->
      <div>
        <h3 style="font-family: 'Inter', sans-serif; font-size: 1.1rem; color: var(--color-text); margin-bottom: 1.5rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Quick Links</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.8rem;">
          <li><a href="index.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Home</a></li>
          <li><a href="about.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">About Us</a></li>
          <li><a href="services.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Services</a></li>
          <li><a href="entertainers.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Entertainers</a></li>
          <li><a href="packages.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Packages</a></li>
          <li><a href="blog.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Blog</a></li>
        </ul>
      </div>

      <!-- Column 3: Support -->
      <div>
        <h3 style="font-family: 'Inter', sans-serif; font-size: 1.1rem; color: var(--color-text); margin-bottom: 1.5rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Support</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.8rem;">
          <li><a href="contact.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Contact Us</a></li>
          <li><a href="pricing.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Pricing Policy</a></li>
          <li><a href="terms.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Terms & Conditions</a></li>
          <li><a href="privacy.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Privacy Policy</a></li>
          <li><a href="faqs.html" style="color: var(--color-text-light); text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">FAQ</a></li>
        </ul>
      </div>

      <!-- Column 4: Contact -->
      <div>
        <h3 style="font-family: 'Inter', sans-serif; font-size: 1.1rem; color: var(--color-text); margin-bottom: 1.5rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Contact</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li style="display: flex; align-items: center; gap: 0.75rem; color: var(--color-text-light); font-size: 0.95rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span>+1 (555) 123-4567</span>
          </li>
          <li style="display: flex; align-items: center; gap: 0.75rem; color: var(--color-text-light); font-size: 0.95rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            <span>hello@magiqo.com</span>
          </li>
          <li style="display: flex; align-items: center; gap: 0.75rem; color: var(--color-text-light); font-size: 0.95rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="flex-shrink: 0;"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
            <span>magiqo_official</span>
          </li>
        </ul>
      </div>
    </div>

    <!-- Footer Bottom -->
    <div style="border-top: 1px solid var(--color-border); padding-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
      <p style="color: var(--color-text-light); margin: 0; font-size: 0.9rem;">&copy; 2026 MAGIQO. All rights reserved.</p>
      <div style="display: flex; gap: 1.5rem;">
        <a href="terms.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.9rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Terms</a>
        <a href="privacy.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.9rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Privacy</a>
        <a href="cookies.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.9rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Cookies</a>
      </div>
    </div>
  </div>
</footer>"""

with open('c:/Users/vigas/Desktop/magiqo/components/footer.html', 'w', encoding='utf-8') as f:
    f.write(new_footer)

print("footer.html refined and aligned perfectly!")
