import re

filepath = r'c:\Users\vigas\Desktop\magiqo\booking.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for 3D Animations on feature-item and gallery images
css_to_add = '''
    /* New 3D and Hover Effects */
    .feature-item {
      transform: perspective(1000px) rotateX(0) rotateY(0) scale(1);
      transition: transform 0.5s ease, box-shadow 0.5s ease;
    }
    .feature-item:hover {
      transform: perspective(1000px) rotateX(10deg) rotateY(-5deg) scale(1.05);
      box-shadow: 0 20px 40px rgba(0,0,0,0.15) !important;
      z-index: 10;
    }
    .gallery-section img {
      transition: transform 0.4s ease, box-shadow 0.4s ease, filter 0.4s;
      cursor: pointer;
    }
    .gallery-section img:hover {
      transform: scale(1.05) translateY(-10px);
      box-shadow: 0 15px 30px rgba(0,0,0,0.2);
      filter: brightness(1.1);
      z-index: 5;
    }
  </style>'''
content = content.replace('</style>', css_to_add)

# 2. Add onclick and ID to "Complete Booking" button and add success div safely inside #step-6
content = content.replace(
    '<button class="btn-nav btn-nav-next" style="background: #3895c8;">Complete Booking <i class="fa-solid fa-check"></i></button>',
    '<button class="btn-nav btn-nav-next" style="background: #3895c8;" id="complete-booking-btn" onclick="completeBooking()">Complete Booking <i class="fa-solid fa-check"></i></button>'
)

content = content.replace(
    '<div class="stepper-controls" id="final-controls">',
    'already_replaced'
)
# Just insert the success message div right after the stepper-controls in step-6
step_6_controls = '''<div class="stepper-controls">
            <button class="btn-nav btn-nav-prev" onclick="nextStep(5)"><i class="fa-solid fa-arrow-left"></i> Back</button>
            <button class="btn-nav btn-nav-next" style="background: #3895c8;" id="complete-booking-btn" onclick="completeBooking()">Complete Booking <i class="fa-solid fa-check"></i></button>
          </div>'''
step_6_replacement = '''<div class="stepper-controls" id="final-controls">
            <button class="btn-nav btn-nav-prev" onclick="nextStep(5)"><i class="fa-solid fa-arrow-left"></i> Back</button>
            <button class="btn-nav btn-nav-next" style="background: #3895c8;" id="complete-booking-btn" onclick="completeBooking()">Complete Booking <i class="fa-solid fa-check"></i></button>
          </div>
          <div id="booking-success" style="display: none; text-align: center; margin-top: 30px; padding: 40px; background: rgba(16, 185, 129, 0.1); border: 2px dashed #10b981; border-radius: 20px; animation: slideIn 0.5s forwards;">
            <i class="fa-solid fa-circle-check" style="font-size: 4rem; color: #10b981; margin-bottom: 20px;"></i>
            <h3 style="font-size: 2.2rem; color: var(--color-text); margin-bottom: 15px; font-family: var(--font-magic);">Transaction Successful!</h3>
            <p style="color: var(--color-text-light); font-size: 1.1rem;">Your magical celebration is officially locked in! We've sent a receipt and full details to your email.</p>
          </div>'''
content = content.replace(step_6_controls, step_6_replacement)

# 3. Add onclick and ID to "Send Message" button and add success div safely inside query box
old_send_btn = '<button type="button" style="background: #3895c8; color: white; border: none; padding: 15px; border-radius: 12px; font-size: 1.1rem; font-weight: bold; cursor: pointer; transition: 0.3s; margin-top: 10px;">Send Message <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i></button>'
new_send_btn = '''<button type="button" id="send-msg-btn" onclick="sendMessage()" style="background: #3895c8; color: white; border: none; padding: 15px; border-radius: 12px; font-size: 1.1rem; font-weight: bold; cursor: pointer; transition: 0.3s; margin-top: 10px;">Send Message <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i></button>
          <div id="msg-success" style="display: none; text-align: center; margin-top: 15px; padding: 15px; background: rgba(16, 185, 129, 0.1); border-radius: 12px; color: #10b981; font-weight: bold;">
            <i class="fa-solid fa-check"></i> Message sent successfully! Our team will reply shortly.
          </div>'''
content = content.replace(old_send_btn, new_send_btn)

# 4. Add JS Functions
js_to_add = '''
    function completeBooking() {
      const step6Content = document.getElementById('step-6');
      const formGrid = step6Content.querySelector('.form-grid');
      const controls = document.getElementById('final-controls');
      const desc = step6Content.querySelector('.step-desc');
      
      if(formGrid) formGrid.style.display = 'none';
      if(controls) controls.style.display = 'none';
      if(desc) desc.style.display = 'none';
      
      document.getElementById('booking-success').style.display = 'block';
    }

    function sendMessage() {
      const btn = document.getElementById('send-msg-btn');
      btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';
      
      setTimeout(() => {
        btn.style.display = 'none';
        document.getElementById('msg-success').style.display = 'block';
      }, 1000);
    }
  </script>'''
content = content.replace('</script>', js_to_add)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
