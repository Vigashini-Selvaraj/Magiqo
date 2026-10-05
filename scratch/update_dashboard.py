import re

with open('user_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Change "Super Admin" to "User"
html = html.replace('<div style="font-size: 0.85rem; color: var(--color-text-light);">Super Admin</div>', '<div style="font-size: 0.85rem; color: var(--color-text-light);">User</div>')

# 2. Fix broken image photo-1508214751196-bfdd4ca401fc
html = html.replace('https://images.unsplash.com/photo-1508214751196-bfdd4ca401fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', 'assets/images/pro_magician_2.jpg')

# 3. Add Log Out button to sidebar
log_out_html = """      <div class="admin-nav-item" onclick="window.location.href='index.html'" style="color: #D24B76; border-top: 1px solid var(--color-border); border-radius: 0; margin-top: 10px; padding-top: 20px;">
        <i class="fa-solid fa-arrow-right-from-bracket"></i> Log Out
      </div>
    </div>"""
html = html.replace('    </div>\n    <div class="sidebar-toggles">', log_out_html + '\n    <div class="sidebar-toggles">')

# 4. Change alert('Added to Favorites!') to addToFavorites(this)
html = html.replace("alert('Added to Favorites!')", "addToFavorites(this)")

# 5. Add JavaScript functions at the bottom for Add to Favorites and Real Moments File Upload
js_code = """
    // Custom logic for User Dashboard tasks
    function addToFavorites(btn) {
      // Find the card element
      const card = btn.closest('div[style*="background: rgba(255,255,255,0.02)"]');
      if (!card) return;
      
      const imgPath = card.querySelector('img').src;
      const title = card.querySelector('h4').textContent;
      const desc = card.querySelector('p').textContent;
      
      const favGrid = document.querySelector('#favorites .content-panel > div[style*="display: grid"]');
      if (!favGrid) return;
      
      // Check if already exists in favorites
      let exists = false;
      favGrid.querySelectorAll('h4').forEach(h4 => {
        if (h4.textContent === title) exists = true;
      });
      
      if (exists) {
        alert(title + ' is already in your favorites!');
        return;
      }
      
      const newFav = document.createElement('div');
      newFav.style.cssText = "background: rgba(255,255,255,0.02); border: 1px solid var(--color-primary); border-radius: 12px; overflow: hidden; position: relative; animation: fadeIn 0.4s ease;";
      newFav.innerHTML = `
        <div style="position: absolute; top: 10px; right: 10px; color: var(--color-primary); font-size: 1.5rem; background: rgba(0,0,0,0.5); padding: 5px; border-radius: 50%;"><i class="fa-solid fa-heart"></i></div>
        <img src="${imgPath}" alt="${title}" style="width: 100%; height: 200px; object-fit: cover;">
        <div style="padding: 20px;">
          <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">${title}</h4>
          <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">${desc}</p>
          <button class="btn-primary" style="width: 100%;" onclick="openModal()">Book Now</button>
        </div>
      `;
      
      favGrid.appendChild(newFav);
      
      // Change the heart icon in explore to filled pink
      btn.style.color = 'var(--color-primary)';
      btn.style.borderColor = 'var(--color-primary)';
      
      alert(title + ' added to Favorites!');
    }
    
    document.addEventListener('DOMContentLoaded', () => {
      const fileInput = document.getElementById('file-input');
      if (fileInput) {
        fileInput.addEventListener('change', function(e) {
          const files = e.target.files;
          if (!files || files.length === 0) return;
          
          const grid = document.querySelector('#real-moments .content-panel > div[style*="display: grid"]');
          const addMoreBtn = grid.lastElementChild; // The add more box
          
          for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const reader = new FileReader();
            reader.onload = function(event) {
              const newMoment = document.createElement('div');
              newMoment.style.cssText = "border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2); animation: fadeIn 0.4s ease;";
              newMoment.innerHTML = `<img src="${event.target.result}" alt="New Moment" style="width: 100%; height: 100%; object-fit: cover;">`;
              
              grid.insertBefore(newMoment, addMoreBtn);
            };
            reader.readAsDataURL(file);
          }
        });
      }
    });
  </script>
</body>"""

html = html.replace('  </script>\n</body>', js_code)

with open('user_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
