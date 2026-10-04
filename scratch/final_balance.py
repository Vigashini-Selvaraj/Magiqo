import re

# 1. Remove the "How to Host an Epic Superhero Action Party" card from index.html
filepath_index = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath_index, 'r', encoding='utf-8') as f:
    content = f.read()

bad_card_pattern = r'\s*<div class="card" style="padding: 0; overflow: hidden;">\s*<img src="assets/images/superhero_party_1790842695325\.jpg" alt="Action Hero Theme".*?How to Host an Epic Superhero Action Party.*?</div>\s*</div>'
content = re.sub(bad_card_pattern, '', content, flags=re.DOTALL)

with open(filepath_index, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Perfect the footer layout to ensure it uses Flexbox (prevents cutoffs) and perfectly mimics Archivia
new_footer = """<footer class="footer" style="background: var(--color-surface); padding: 5rem 0 2rem; border-top: 1px solid rgba(0,0,0,0.05); font-family: 'Inter', sans-serif;">
  <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
    <!-- FLEXBOX LAYOUT ensures perfectly responsive and balanced columns -->
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 3rem; margin-bottom: 4rem;">
      
      <!-- Column 1: Brand -->
      <div style="flex: 1.5; min-width: 250px; max-width: 320px;">
        <a href="index.html" style="display: flex; align-items: center; gap: 0.75rem; text-decoration: none; color: var(--color-primary); font-family: var(--font-magic); font-size: 2rem; font-weight: bold; margin-bottom: 1.5rem;">
          <img src="assets/images/magiqo_logo_1790915438485.jpg" alt="Magiqo Logo" style="height: 40px; border-radius: 50%;"> MAGIQO
        </a>
        
        <p style="color: var(--color-text-light); line-height: 1.7; font-size: 0.95rem; margin-bottom: 1.5rem;">
          A modern destination for discovering entertainers, exploring ideas and planning unforgettable celebrations.
        </p>
        
        <div style="display: flex; gap: 0.75rem;">
          <a href="#" aria-label="Instagram" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #EDCBB1; color: #180D20; text-decoration: none; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform='translateY(0)'"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
          <a href="#" aria-label="Twitter" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #EDCBB1; color: #180D20; text-decoration: none; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform='translateY(0)'"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          <a href="#" aria-label="LinkedIn" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #EDCBB1; color: #180D20; text-decoration: none; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform='translateY(0)'"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
          <a href="#" aria-label="YouTube" style="display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #EDCBB1; color: #180D20; text-decoration: none; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform='translateY(0)'"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></a>
        </div>
      </div>

      <!-- Column 2: Quick Links -->
      <div style="flex: 1; min-width: 150px;">
        <h3 style="font-style: italic; font-size: 1.15rem; color: #180D20; margin-bottom: 1.5rem; font-weight: 700;">Quick Links</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li><a href="index.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Home</a></li>
          <li><a href="home2.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Home 2</a></li>
          <li><a href="about.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">About Us</a></li>
          <li><a href="services.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Library</a></li>
          <li><a href="packages.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Services</a></li>
          <li><a href="blog.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Blog</a></li>
          <li><a href="pricing.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Pricing</a></li>
        </ul>
      </div>

      <!-- Column 3: Support -->
      <div style="flex: 1; min-width: 150px;">
        <h3 style="font-style: italic; font-size: 1.15rem; color: #180D20; margin-bottom: 1.5rem; font-weight: 700;">Support</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li><a href="contact.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Contact</a></li>
          <li><a href="faqs.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">FAQ</a></li>
          <li><a href="privacy.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Privacy Policy</a></li>
          <li><a href="terms.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.95rem; transition: color 0.3s;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Terms & Conditions</a></li>
        </ul>
      </div>

      <!-- Column 4: Contact -->
      <div style="flex: 1.2; min-width: 250px;">
        <h3 style="font-style: italic; font-size: 1.15rem; color: #180D20; margin-bottom: 1.5rem; font-weight: 700;">Get in Touch</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.2rem;">
          <li style="display: flex; align-items: center; gap: 0.75rem; color: var(--color-text-light); font-size: 0.95rem;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D24B76" stroke-width="2" style="flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            <span>hello@magiqo.com</span>
          </li>
          <li style="display: flex; align-items: center; gap: 0.75rem; color: var(--color-text-light); font-size: 0.95rem;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D24B76" stroke-width="2" style="flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span>+1 (555) 123-4567</span>
          </li>
          <li style="display: flex; align-items: center; gap: 0.75rem; color: var(--color-text-light); font-size: 0.95rem;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D24B76" stroke-width="2" style="flex-shrink: 0;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            <span>123 Magical Lane, NY</span>
          </li>
          <li style="display: flex; align-items: center; gap: 0.75rem; color: var(--color-text-light); font-size: 0.95rem;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#D24B76" stroke-width="2" style="flex-shrink: 0;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <span>Mon - Sat: 9AM - 6PM</span>
          </li>
        </ul>
      </div>
    </div>

    <!-- Footer Bottom -->
    <div style="border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
      <p style="color: var(--color-text-light); margin: 0; font-size: 0.9rem;">&copy; 2026 MAGIQO. All Rights Reserved.</p>
      <div style="display: flex; gap: 2rem;">
        <a href="privacy.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.9rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Privacy Policy</a>
        <a href="terms.html" style="color: var(--color-text-light); text-decoration: none; font-size: 0.9rem;" onmouseover="this.style.color='var(--color-primary)'" onmouseout="this.style.color='var(--color-text-light)'">Terms & Conditions</a>
      </div>
    </div>
  </div>
</footer>"""

with open('c:/Users/vigas/Desktop/magiqo/components/footer.html', 'w', encoding='utf-8') as f:
    f.write(new_footer)
