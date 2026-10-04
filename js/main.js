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

  // Reveal animations on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.card, .step-card, .section-title').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
    observer.observe(el);
  });
});

window.resetPlanner = function () {
  document.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
  document.querySelectorAll('.planner-step').forEach(step => step.classList.remove('active'));
  document.getElementById('step-1').classList.add('active');
};
