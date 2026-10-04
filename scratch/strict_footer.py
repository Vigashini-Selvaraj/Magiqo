import os

new_footer = """<footer class="footer" style="background: #FFFFFF; padding: 4rem 0 2rem; border-top: 1px solid #EAEAEA; font-family: 'Inter', sans-serif;">
  <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
    <!-- CSS GRID LAYOUT forces exactly 4 columns side by side -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; margin-bottom: 4rem;">
      
      <!-- Column 1: Brand -->
      <div>
        <a href="index.html" style="display: flex; align-items: center; gap: 0.5rem; text-decoration: none; color: #180D20; font-family: var(--font-magic), serif; font-size: 1.75rem; font-weight: bold; margin-bottom: 1rem;">
          <img src="assets/images/magiqo_logo_1790915438485.jpg" alt="Magiqo Logo" style="height: 35px; border-radius: 50%;"> MAGIQO
        </a>
        <p style="color: #666666; line-height: 1.6; font-size: 0.85rem; max-width: 280px;">
          A modern destination for discovering entertainers, exploring ideas and planning unforgettable celebrations.
        </p>
      </div>

      <!-- Column 2: Quick Links -->
      <div>
        <h3 style="font-style: italic; font-size: 1rem; color: #112A22; margin-bottom: 1.5rem; font-weight: 700; font-family: serif;">Quick Links</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li><a href="index.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Home</a></li>
          <li><a href="home2.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Home 2</a></li>
          <li><a href="about.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">About Us</a></li>
          <li><a href="entertainers.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Entertainers</a></li>
          <li><a href="packages.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Packages</a></li>
          <li><a href="blog.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Blogs</a></li>
        </ul>
      </div>

      <!-- Column 3: Support -->
      <div>
        <h3 style="font-style: italic; font-size: 1rem; color: #112A22; margin-bottom: 1.5rem; font-weight: 700; font-family: serif;">Support</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li><a href="contact.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Contact</a></li>
          <li><a href="terms.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Terms & Conditions</a></li>
          <li><a href="privacy.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Privacy Policy</a></li>
          <li><a href="faqs.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">FAQ</a></li>
          <li><a href="help.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Help</a></li>
          <li><a href="pricing.html" style="color: #666666; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Pricing</a></li>
        </ul>
      </div>

      <!-- Column 4: Contact -->
      <div>
        <h3 style="font-style: italic; font-size: 1rem; color: #112A22; margin-bottom: 1.5rem; font-weight: 700; font-family: serif;">Contact</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li style="display: flex; align-items: center; gap: 0.75rem; color: #666666; font-size: 0.85rem;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#B88A58" stroke-width="2" style="flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span>+1 (555) 123-4567</span>
          </li>
          <li style="display: flex; align-items: center; gap: 0.75rem; color: #666666; font-size: 0.85rem;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#B88A58" stroke-width="2" style="flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            <span>hello@magiqo.com</span>
          </li>
          <li style="margin-top: 0.5rem;">
            <div style="display: flex; gap: 0.75rem;">
              <a href="#" aria-label="Instagram" style="display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 50%; background: #F5EBE1; color: #000000; text-decoration: none; transition: background 0.2s ease;" onmouseover="this.style.background='#E6D5C3'" onmouseout="this.style.background='#F5EBE1'"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
              <a href="#" aria-label="Facebook" style="display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 50%; background: #F5EBE1; color: #000000; text-decoration: none; transition: background 0.2s ease;" onmouseover="this.style.background='#E6D5C3'" onmouseout="this.style.background='#F5EBE1'"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
              <a href="#" aria-label="YouTube" style="display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 50%; background: #F5EBE1; color: #000000; text-decoration: none; transition: background 0.2s ease;" onmouseover="this.style.background='#E6D5C3'" onmouseout="this.style.background='#F5EBE1'"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <!-- Footer Bottom -->
    <div style="border-top: 1px solid #EAEAEA; padding-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
      <p style="color: #666666; margin: 0; font-size: 0.8rem;">&copy; 2026 MAGIQO. All Rights Reserved.</p>
      <div style="display: flex; gap: 2rem;">
        <a href="privacy.html" style="color: #666666; text-decoration: none; font-size: 0.8rem;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Privacy Policy</a>
        <a href="terms.html" style="color: #666666; text-decoration: none; font-size: 0.8rem;" onmouseover="this.style.color='#112A22'" onmouseout="this.style.color='#666666'">Terms & Conditions</a>
      </div>
    </div>
  </div>
</footer>"""

with open('c:/Users/vigas/Desktop/magiqo/components/footer.html', 'w', encoding='utf-8') as f:
    f.write(new_footer)
