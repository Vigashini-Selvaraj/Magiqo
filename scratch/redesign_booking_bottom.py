import re

filepath = r'c:\Users\vigas\Desktop\magiqo\booking.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Hero Heading
content = content.replace(
    '<h1>Reserve Your Date in <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">6 Easy Steps</span></h1>',
    '<h1><span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Reserve Your Date in</span> <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">6 Easy Steps</span></h1>'
)

# 2. Rebuild the bottom half (from WHY BOOK WITH US to the end of main)
old_bottom_pattern = re.compile(r'<!-- SECTION 4: WHY BOOK WITH US -->.*?</main>', re.DOTALL)

new_bottom_html = '''<!-- SECTION 4: WHY BOOK WITH US -->
    <section class="features-section reveal" style="padding: 80px 20px;">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 15px; text-align: center;">
        <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Why Book</span> 
        <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">With Magiqo?</span>
      </h2>
      <p style="color: var(--color-text-light); font-size: 1.15rem; max-width: 600px; margin: 0 auto 50px; text-align: center;">We take the stress out of party planning so you can focus on making memories.</p>
      
      <div class="features-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto;">
        <div class="feature-item" style="background: rgba(210, 75, 118, 0.05); padding: 40px 30px; border-radius: 20px; border: 1px solid rgba(210, 75, 118, 0.1); transition: transform 0.3s;">
          <div style="width: 70px; height: 70px; background: linear-gradient(135deg, var(--color-primary), #ff8fa3); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
            <i class="fa-solid fa-wand-magic-sparkles" style="color: white; font-size: 1.8rem; margin: 0;"></i>
          </div>
          <h4 style="font-size: 1.4rem; margin-bottom: 15px; color: var(--color-text);">Premium Entertainment</h4>
          <p style="color: var(--color-text-light); line-height: 1.6;">All our performers are vetted, trained professionals who specialize in children's engagement.</p>
        </div>
        <div class="feature-item" style="background: rgba(56, 149, 200, 0.05); padding: 40px 30px; border-radius: 20px; border: 1px solid rgba(56, 149, 200, 0.1); transition: transform 0.3s;">
          <div style="width: 70px; height: 70px; background: linear-gradient(135deg, #3895c8, #7addff); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
            <i class="fa-solid fa-clock-rotate-left" style="color: white; font-size: 1.8rem; margin: 0;"></i>
          </div>
          <h4 style="font-size: 1.4rem; margin-bottom: 15px; color: var(--color-text);">Hassle-Free Process</h4>
          <p style="color: var(--color-text-light); line-height: 1.6;">Book your entire party online in minutes. No endless email chains or confusing quotes.</p>
        </div>
        <div class="feature-item" style="background: rgba(210, 75, 118, 0.05); padding: 40px 30px; border-radius: 20px; border: 1px solid rgba(210, 75, 118, 0.1); transition: transform 0.3s;">
          <div style="width: 70px; height: 70px; background: linear-gradient(135deg, var(--color-primary), #ff8fa3); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
            <i class="fa-solid fa-heart" style="color: white; font-size: 1.8rem; margin: 0;"></i>
          </div>
          <h4 style="font-size: 1.4rem; margin-bottom: 15px; color: var(--color-text);">100% Satisfaction</h4>
          <p style="color: var(--color-text-light); line-height: 1.6;">We guarantee your child and their guests will have the absolute best time ever.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 5: GALLERY -->
    <section class="gallery-section reveal" style="padding: 80px 20px; max-width: 1200px; margin: 0 auto;">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 15px;">
        <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">Moments in</span> 
        <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Action</span>
      </h2>
      <p style="color: var(--color-text-light); font-size: 1.15rem; text-align: center; margin-bottom: 40px;">Pictures taken in similar types of events.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
        <img src="assets/images/magic_show_party_1790842468826.jpg" style="width: 100%; height: 250px; object-fit: cover; border-radius: 16px;">
        <img src="assets/images/superhero_party_1790842695325.jpg" style="width: 100%; height: 250px; object-fit: cover; border-radius: 16px;">
        <img src="assets/images/princess_party_1790842645232.jpg" style="width: 100%; height: 250px; object-fit: cover; border-radius: 16px;">
        <img src="assets/images/about_kids_birthday.jpg" style="width: 100%; height: 250px; object-fit: cover; border-radius: 16px;">
      </div>
    </section>

    <!-- SECTION 6: TESTIMONIALS -->
    <section class="testimonials-section reveal" style="padding: 80px 20px; max-width: 1200px; margin: 0 auto;">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 15px;">
        <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Happy</span> 
        <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">Parents</span>
      </h2>
      <p style="color: var(--color-text-light); font-size: 1.15rem; text-align: center; margin-bottom: 50px;">Reviews from similar types of events.</p>
      
      <div class="test-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
        <div class="test-card" style="background: rgba(56, 149, 200, 0.03); border: 1px solid rgba(56, 149, 200, 0.2); padding: 40px; border-radius: 20px; backdrop-filter: blur(10px);">
          <div style="display: flex; gap: 5px; color: #f5a623; margin-bottom: 15px; font-size: 1.2rem;">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <p style="font-size: 1.1rem; color: var(--color-text); line-height: 1.6; font-style: italic;">"Booking was so easy. The Princess arrived exactly on time and completely mesmerized the kids for two hours straight!"</p>
          <div class="test-author" style="margin-top: 25px; font-weight: bold; color: var(--color-primary); font-size: 1.1rem;">— Sarah Jenkins</div>
        </div>
        <div class="test-card" style="background: rgba(210, 75, 118, 0.03); border: 1px solid rgba(210, 75, 118, 0.2); padding: 40px; border-radius: 20px; backdrop-filter: blur(10px);">
          <div style="display: flex; gap: 5px; color: #f5a623; margin-bottom: 15px; font-size: 1.2rem;">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <p style="font-size: 1.1rem; color: var(--color-text); line-height: 1.6; font-style: italic;">"Magiqo took all the stress away. The Add-ons feature let me handle the cake, decor, and entertainment in one click."</p>
          <div class="test-author" style="margin-top: 25px; font-weight: bold; color: #3895c8; font-size: 1.1rem;">— Mark T.</div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: FAQs -->
    <section class="faq-section reveal" style="padding: 80px 20px; max-width: 800px; margin: 0 auto;">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 40px;">
        <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none;">Booking</span> 
        <span style="color: #3895c8; -webkit-text-fill-color: #3895c8; background: none;">FAQs</span>
      </h2>
      
      <style>
        details {
          background: var(--color-surface);
          border: 1px solid var(--color-border);
          border-radius: 12px;
          margin-bottom: 15px;
          box-shadow: 0 5px 15px rgba(0,0,0,0.05);
          overflow: hidden;
        }
        summary {
          padding: 20px 25px;
          font-family: var(--font-heading);
          font-size: 1.15rem;
          font-weight: bold;
          color: var(--color-text);
          cursor: pointer;
          list-style: none;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        summary::-webkit-details-marker { display: none; }
        summary::after {
          content: '\\f078'; /* fa-chevron-down */
          font-family: 'Font Awesome 6 Free';
          font-weight: 900;
          color: var(--color-primary);
          transition: transform 0.3s;
        }
        details[open] summary::after {
          transform: rotate(180deg);
        }
        .faq-content {
          padding: 0 25px 25px;
          color: var(--color-text-light);
          line-height: 1.6;
        }
      </style>

      <details>
        <summary>When is my advance payment due?</summary>
        <div class="faq-content">A 20% advance payment is required at the time of booking to secure your date. The remaining balance is due 24 hours before the event.</div>
      </details>
      <details>
        <summary>Can I modify my booking later?</summary>
        <div class="faq-content">Yes! You can add extra guests, add-ons, or even change your entertainer up to 7 days before your event, subject to availability.</div>
      </details>
      <details>
        <summary>What is the cancellation policy?</summary>
        <div class="faq-content">You can cancel for a full refund up to 14 days before the event. Cancellations within 14 days will forfeit the 20% deposit.</div>
      </details>
    </section>

    <!-- SECTION 8: QUERY BOX -->
    <section class="query-section reveal" style="padding: 60px 20px 100px; max-width: 800px; margin: 0 auto; text-align: center;">
      <div style="background: linear-gradient(135deg, rgba(210, 75, 118, 0.1), rgba(56, 149, 200, 0.1)); border-radius: 24px; padding: 50px 30px; border: 1px solid rgba(56, 149, 200, 0.2);">
        <h2 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 15px; color: var(--color-text);">Still have questions?</h2>
        <p style="color: var(--color-text-light); font-size: 1.1rem; margin-bottom: 30px;">If you couldn't find what you're looking for, our party experts are here to help!</p>
        
        <form style="display: flex; flex-direction: column; gap: 15px; max-width: 500px; margin: 0 auto;">
          <input type="text" placeholder="Your Name" style="padding: 15px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.1); font-size: 1rem; background: var(--color-surface); color: var(--color-text);">
          <input type="email" placeholder="Your Email" style="padding: 15px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.1); font-size: 1rem; background: var(--color-surface); color: var(--color-text);">
          <textarea placeholder="How can we help?" rows="4" style="padding: 15px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.1); font-size: 1rem; background: var(--color-surface); color: var(--color-text); resize: vertical;"></textarea>
          <button type="button" style="background: #3895c8; color: white; border: none; padding: 15px; border-radius: 12px; font-size: 1.1rem; font-weight: bold; cursor: pointer; transition: 0.3s; margin-top: 10px;">Send Message <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i></button>
        </form>
      </div>
    </section>

  </main>'''

content = old_bottom_pattern.sub(new_bottom_html, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
