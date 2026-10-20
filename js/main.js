// Main interactions
document.addEventListener('DOMContentLoaded', () => {
  // Planner interaction logic
  const plannerSteps = document.querySelectorAll('.planner-step');
  const optionBtns = document.querySelectorAll('.option-btn');

  optionBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      // visual feedback
      this.classList.add('selected');

      const stepNum = parseInt(this.getAttribute('data-step'));

      // Delay to show selected state
      setTimeout(() => {
        // Hide current step
        document.getElementById(`step-${stepNum}`).classList.remove('active');

        // Show next step or result
        if (stepNum === 1) {
          document.getElementById('step-2').classList.add('active');
        } else if (stepNum === 2) {
          document.getElementById('step-3').classList.add('active');
        } else if (stepNum === 3) {
          document.getElementById('step-result').classList.add('active');
        }
      }, 400);
    });
  });

  // Smooth reveal animations on scroll for explicitly designated elements
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: '50px' });

    document.querySelectorAll('.reveal-on-scroll').forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
      observer.observe(el);
    });
  }
});

window.resetPlanner = function () {
  document.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
  document.querySelectorAll('.planner-step').forEach(step => step.classList.remove('active'));
  document.getElementById('step-1').classList.add('active');
};
