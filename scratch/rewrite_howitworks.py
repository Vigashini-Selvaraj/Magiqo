import re
filepath = r'c:\Users\vigas\Desktop\magiqo\packages.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add margin-top to section-title
content = content.replace(
    '.section-title {\n      font-family: var(--font-magic);\n      font-size: 3rem;\n      text-align: center;\n      margin-bottom: 20px;\n      background: none;\n      -webkit-text-fill-color: initial;\n    }',
    '.section-title {\n      font-family: var(--font-magic);\n      font-size: 3rem;\n      text-align: center;\n      margin-top: 5rem;\n      margin-bottom: 20px;\n      background: none;\n      -webkit-text-fill-color: initial;\n    }'
)

# 2. Replace the old "How booking works" steps grid
old_steps_html = '''      <div class="steps-grid">
        <div class="step-card reveal">
          <div class="step-number">1</div>
          <h3>Pick a Package</h3>
          <p>Explore our crafted experiences in real-time. Review the pricing, features, and durations. Select the package that perfectly aligns with your event's scale and theme directly from this page.</p>
        </div>
        <div class="step-card reveal">
          <div class="step-number">2</div>
          <h3>Select Entertainer</h3>
          <p>Tell us exactly who you want to invite! You'll be asked to pick the type of entertainer (Magician, Princess, Clown, etc.) and you can even request specific performers by name when checking out.</p>
        </div>
        <div class="step-card reveal">
          <div class="step-number">3</div>
          <h3>Share Details</h3>
          <p>Fill out the comprehensive booking form. We'll need the date, specific venue location (indoor/outdoor), expected guest count, and any unique requests so we can prepare deeply for your event.</p>
        </div>
        <div class="step-card reveal">
          <div class="step-number">4</div>
          <h3>Confirm</h3>
          <p>Review all your magical details in the summary pane and finalize your booking request. Our team will verify availability and send you a secure confirmation link to lock in your date.</p>
        </div>
      </div>'''

new_steps_html = '''      <div class="steps-grid">
        <div class="step-card reveal clickable-step" data-step="1">
          <div class="step-img-wrap"><img src="assets/images/magic_show_party_1790842468826.jpg" alt="Pick a Package"></div>
          <div class="step-number">1</div>
          <h3 style="background: linear-gradient(90deg, var(--color-primary), #3895c8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Pick a Package</h3>
          <p>Explore our crafted experiences and pick the perfect magic package for your event.</p>
        </div>
        <div class="step-card reveal clickable-step" data-step="2">
          <div class="step-img-wrap"><img src="assets/images/superhero_party_1790842695325.jpg" alt="Select Entertainer"></div>
          <div class="step-number">2</div>
          <h3 style="background: linear-gradient(90deg, var(--color-primary), #3895c8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Select Entertainer</h3>
          <p>Tell us who you want to invite! Choose the entertainer or character for your child.</p>
        </div>
        <div class="step-card reveal clickable-step" data-step="3">
          <div class="step-img-wrap"><img src="assets/images/about_kids_birthday.jpg" alt="Share Details"></div>
          <div class="step-number">3</div>
          <h3 style="background: linear-gradient(90deg, var(--color-primary), #3895c8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Share Details</h3>
          <p>Fill out our simple form with your date, location, and any special requests you have.</p>
        </div>
        <div class="step-card reveal clickable-step" data-step="4">
          <div class="step-img-wrap"><img src="assets/images/james_boy_smile.jpg" alt="Confirm"></div>
          <div class="step-number">4</div>
          <h3 style="background: linear-gradient(90deg, var(--color-primary), #3895c8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Confirm</h3>
          <p>Review your booking and submit. We will verify and lock in your special date!</p>
        </div>
      </div>
'''

content = content.replace(old_steps_html, new_steps_html)

# 3. Add styling for step cards images & Modal UI just above </head> or inline
modal_css = '''
    /* Step Cards Redesign */
    .step-card {
      padding: 0 !important;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .step-card:hover {
      transform: translateY(-10px);
    }
    .step-img-wrap {
      width: 100%;
      height: 140px;
      overflow: hidden;
    }
    .step-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s;
    }
    .step-card:hover .step-img-wrap img {
      transform: scale(1.1);
    }
    .step-card h3 {
      margin: 15px 20px 10px;
      font-size: 1.5rem;
    }
    .step-card p {
      margin: 0 20px 25px;
      font-size: 0.95rem;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .step-card .step-number {
      position: absolute;
      top: 120px;
      right: 20px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    /* Modal Styling */
    .step-modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.7);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.3s;
    }
    .step-modal-overlay.active {
      display: flex;
      opacity: 1;
    }
    .step-modal-content {
      background: var(--color-surface);
      width: 90%;
      max-width: 500px;
      border-radius: 20px;
      padding: 2rem;
      position: relative;
      transform: translateY(20px);
      transition: transform 0.3s;
      box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    }
    .step-modal-overlay.active .step-modal-content {
      transform: translateY(0);
    }
    .close-modal {
      position: absolute;
      top: 15px; right: 20px;
      font-size: 1.5rem;
      cursor: pointer;
      color: var(--color-text-light);
    }
    .step-modal-title {
      font-family: var(--font-magic);
      font-size: 2rem;
      background: linear-gradient(90deg, var(--color-primary), #3895c8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 1rem;
    }
    .step-modal-desc {
      color: var(--color-text);
      font-size: 1.05rem;
      line-height: 1.6;
      margin-bottom: 2rem;
    }
    .step-modal-btn {
      display: block;
      width: 100%;
      text-align: center;
      background: var(--color-primary);
      color: white;
      padding: 12px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: bold;
      transition: 0.3s;
      cursor: pointer;
      border: none;
      font-size: 1.05rem;
    }
    .step-modal-btn:hover {
      background: #3895c8;
      color: white;
    }
'''
content = content.replace('/* Custom Packages Styles using strict Magiqo variables */', '/* Custom Packages Styles using strict Magiqo variables */\n' + modal_css)

# 4. Add the Modal HTML & JS right before </body>
modal_html = '''
  <!-- STEP MODAL -->
  <div class="step-modal-overlay" id="stepModal">
    <div class="step-modal-content">
      <div class="close-modal" id="closeStepModal"><i class="fa-solid fa-xmark"></i></div>
      <h3 class="step-modal-title" id="modalTitle">Title</h3>
      <p class="step-modal-desc" id="modalDesc">Desc</p>
      <button class="step-modal-btn" id="modalNextBtn">Next Step <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></button>
    </div>
  </div>

  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const modal = document.getElementById("stepModal");
      const closeBtn = document.getElementById("closeStepModal");
      const titleEl = document.getElementById("modalTitle");
      const descEl = document.getElementById("modalDesc");
      const nextBtn = document.getElementById("modalNextBtn");
      
      const stepData = {
        1: { title: "Pick a Package", desc: "Explore our crafted experiences in real-time. Review the pricing, features, and durations. Select the package that perfectly aligns with your event's scale and theme directly from this page.", next: 2 },
        2: { title: "Select Entertainer", desc: "Tell us exactly who you want to invite! You'll be asked to pick the type of entertainer (Magician, Princess, Clown, etc.) and you can even request specific performers by name when checking out.", next: 3 },
        3: { title: "Share Details", desc: "Fill out the comprehensive booking form. We'll need the date, specific venue location (indoor/outdoor), expected guest count, and any unique requests so we can prepare deeply for your event.", next: 4 },
        4: { title: "Confirm", desc: "Review all your magical details in the summary pane and finalize your booking request. Our team will verify availability and send you a secure confirmation link to lock in your date.", next: null }
      };

      let currentStep = 1;

      function openModal(stepNum) {
        const data = stepData[stepNum];
        if(!data) return;
        currentStep = stepNum;
        titleEl.textContent = data.title;
        descEl.textContent = data.desc;
        if(data.next) {
          nextBtn.innerHTML = 'Next Step <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i>';
        } else {
          nextBtn.innerHTML = 'Close';
        }
        modal.classList.add("active");
      }

      document.querySelectorAll(".clickable-step").forEach(card => {
        card.addEventListener("click", () => {
          openModal(parseInt(card.getAttribute("data-step")));
        });
      });

      closeBtn.addEventListener("click", () => {
        modal.classList.remove("active");
      });

      modal.addEventListener("click", (e) => {
        if(e.target === modal) modal.classList.remove("active");
      });

      nextBtn.addEventListener("click", () => {
        if(stepData[currentStep].next) {
          openModal(stepData[currentStep].next);
        } else {
          modal.classList.remove("active");
        }
      });
    });
  </script>
'''

content = content.replace('</body>', modal_html + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
