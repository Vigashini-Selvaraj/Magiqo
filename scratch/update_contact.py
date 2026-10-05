import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove "Perfect For Every Occasion" section completely
# It starts at "<!-- 4. CHOOSE YOUR EVENT -->" and ends at "<!-- 5. HOW WE CAN HELP"
start_event = html.find('<!-- 4. CHOOSE YOUR EVENT -->')
end_event = html.find('<!-- 5. HOW WE CAN HELP')
if start_event != -1 and end_event != -1:
    html = html[:start_event] + html[end_event:]

# 2. Update James image
# Original: <img src="assets/images/pro_magician.jpg" class="team-img" alt="James">
html = html.replace(
    '<img src="assets/images/pro_magician.jpg" class="team-img" alt="James">',
    '<img src="assets/images/pro_magician_2.jpg" class="team-img" alt="James">'
)

# 3. Update Sarah Jenkins image
# Original: <img src="assets/images/pro_hero_party.jpg" class="team-img" alt="Sarah">
html = html.replace(
    '<img src="assets/images/pro_hero_party.jpg" class="team-img" alt="Sarah">',
    '<img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="team-img" alt="Sarah">'
)

# 4. Update Why Choose Magiqo image
# Original: <img src="assets/images/hero_magician_1790831867453.jpg" class="why-main-img" alt="Magician performing">
html = html.replace(
    '<img src="assets/images/hero_magician_1790831867453.jpg" class="why-main-img" alt="Magician performing">',
    '<img src="assets/images/pro_magical_services.jpg" class="why-main-img" alt="Magician performing">'
)

# 5. Fix animations by replacing the Framer Motion module with a robust IntersectionObserver
script_start = html.find('<!-- Framer Motion (Motion One for Vanilla JS) -->')
if script_start != -1:
    script_end = html.find('</body>', script_start)
    
    vanilla_js_animation = """<!-- Vanilla JS Scroll Animations -->
  <style>
    .reveal {
      opacity: 0;
      transform: translateY(40px);
      transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .reveal.active {
      opacity: 1;
      transform: translateY(0);
    }
    .stagger-children > * {
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .stagger-children.active > * {
      opacity: 1;
      transform: translateY(0);
    }
    .stagger-children.active > *:nth-child(1) { transition-delay: 0.1s; }
    .stagger-children.active > *:nth-child(2) { transition-delay: 0.2s; }
    .stagger-children.active > *:nth-child(3) { transition-delay: 0.3s; }
    .stagger-children.active > *:nth-child(4) { transition-delay: 0.4s; }
    .stagger-children.active > *:nth-child(5) { transition-delay: 0.5s; }
    .stagger-children.active > *:nth-child(6) { transition-delay: 0.6s; }
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      // Add stagger classes to grids for smooth child animations
      const grids = document.querySelectorAll('.contact-cards-container, .help-grid-modern, .team-grid, .why-features-side');
      grids.forEach(grid => grid.classList.add('stagger-children', 'reveal'));

      const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
      
      // Also manually animate the hero section immediately
      setTimeout(() => {
        const heroText = document.querySelector('.contact-hero-text');
        if(heroText) {
          heroText.style.opacity = '1';
          heroText.style.transform = 'translateY(0)';
        }
      }, 100);
    });
  </script>
"""
    html = html[:script_start] + vanilla_js_animation + html[script_end:]

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)
