document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('theme-toggle');
  const html = document.documentElement;
  
  // Check local storage or system preference
  const savedTheme = localStorage.getItem('magiqo-theme');
  if (savedTheme) {
    html.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    html.setAttribute('data-theme', 'dark');
  }

  // Set initial icon
  updateIcon();

  // Wait for toggle to be injected
  document.body.addEventListener('click', (e) => {
    if (e.target.closest('#theme-toggle')) {
      const currentTheme = html.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('magiqo-theme', newTheme);
      updateIcon();
    }
  });

  function updateIcon() {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;
    const isDark = html.getAttribute('data-theme') === 'dark';
    
    const sunIcon = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
    
    const moonIcon = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;

    btn.innerHTML = isDark ? sunIcon : moonIcon;
  }
  
  // Re-run icon update when navbar loads
  window.addEventListener('navbarLoaded', updateIcon);
});
