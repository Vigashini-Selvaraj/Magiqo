async function loadComponent(id, file) {
  try {
    const element = document.getElementById(id);
    if (!element) return;
    
    const response = await fetch(file);
    if (!response.ok) throw new Error(`Could not fetch ${file}`);
    
    const html = await response.text();
    element.innerHTML = html;
    
    // Dispatch event so other scripts know it's loaded
    if (id === 'navbar') {
      window.dispatchEvent(new Event('navbarLoaded'));
      initNavbar();
    }
  } catch (error) {
    console.error('Error loading component:', error);
  }
}

function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');

  // Set Active Link
  const links = document.querySelectorAll('.nav-links a');
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  links.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  // Sticky Navbar
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // Mobile Menu
  if (hamburger) {
    hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      hamburger.classList.toggle('active');
    });

    // Close mobile menu when a nav link is clicked
    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        hamburger.classList.remove('active');
      });
    });
  }

  // Dropdown Toggle
  const profileToggle = document.querySelector('.profile-toggle');
  const profileDropdown = document.querySelector('.profile-dropdown');
  
  if (profileToggle) {
    profileToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      profileDropdown.classList.toggle('active');
    });

    document.addEventListener('click', () => {
      profileDropdown.classList.remove('active');
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  loadComponent('navbar', 'components/navbar.html?v=' + new Date().getTime());
  loadComponent('footer', 'components/footer.html?v=' + new Date().getTime());
});
