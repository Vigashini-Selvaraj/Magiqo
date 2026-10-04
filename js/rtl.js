document.addEventListener('DOMContentLoaded', () => {
  const html = document.documentElement;
  
  const savedDir = localStorage.getItem('magiqo-direction') || 'ltr';
  html.setAttribute('dir', savedDir);

  document.body.addEventListener('click', (e) => {
    if (e.target.closest('#rtl-toggle')) {
      const currentDir = html.getAttribute('dir');
      const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
      
      html.setAttribute('dir', newDir);
      localStorage.setItem('magiqo-direction', newDir);
      updateText();
    }
  });

  function updateText() {
    const btn = document.getElementById('rtl-toggle');
    if (!btn) return;
    const isRtl = html.getAttribute('dir') === 'rtl';
    btn.innerHTML = isRtl ? 'LTR' : 'RTL';
  }

  window.addEventListener('navbarLoaded', updateText);
});
