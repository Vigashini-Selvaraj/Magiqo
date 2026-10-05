import re

with open('user_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Overview buttons
html = html.replace(
    '<a href="#" class="btn-primary" style="padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">View Details</a>',
    '<a href="#" class="btn-primary" onclick="openDetailsModal()" style="padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">View Details</a>'
)
html = html.replace(
    '<a href="#" class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text); padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">Contact Support</a>',
    '<a href="#" class="btn-primary" onclick="switchTab(\'messages\', document.querySelectorAll(\'.admin-nav-item\')[4])" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text); padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">Contact Support</a>'
)

# 2. Princess Aurora image
html = html.replace(
    '<div style="width: 100%; height: 200px; background: rgba(210, 75, 118, 0.1); display: flex; align-items: center; justify-content: center; color: var(--color-primary); font-size: 3rem;">\n              <i class="fa-solid fa-crown"></i>\n            </div>',
    '<img src="assets/images/princess_portrait_1790843055244.jpg" alt="Princess Aurora" style="width: 100%; height: 200px; object-fit: cover;">'
)

# Add 2 more entertainers to Explore
extra_entertainers = """
          <!-- Card 5 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden;">
            <img src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias Thorne" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Elias Thorne</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Modern Magician & Mind Reader</p>
              <div style="display: flex; gap: 10px;">
                <button class="btn-primary" style="flex: 1;" onclick="openModal()">Book Now</button>
                <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);" onclick="alert('Added to Favorites!')"><i class="fa-solid fa-heart"></i></button>
              </div>
            </div>
          </div>
          <!-- Card 6 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden;">
            <img src="assets/images/superhero_party_1790842695325.jpg" alt="Captain Cosmic" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Captain Cosmic</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Superhero Training & Games</p>
              <div style="display: flex; gap: 10px;">
                <button class="btn-primary" style="flex: 1;" onclick="openModal()">Book Now</button>
                <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);" onclick="alert('Added to Favorites!')"><i class="fa-solid fa-heart"></i></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
"""
html = html.replace('        </div>\n      </div>\n    </div>\n\n    <!-- BOOKINGS TAB -->', extra_entertainers + '\n    <!-- BOOKINGS TAB -->')

# 3. Bookings - remove actions
html = html.replace('<th>Actions</th>', '')
html = re.sub(r'<td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button></td>', '', html)

# 4. Messages IDs
html = html.replace(
    '<div style="flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; background: rgba(0,0,0,0.2);">',
    '<div id="chatWindow" style="flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; background: rgba(0,0,0,0.2);">'
)
html = html.replace(
    '<input type="text" class="form-control" placeholder="Type a message..." style="flex: 1;">',
    '<input type="text" id="chatInput" class="form-control" placeholder="Type a message..." style="flex: 1;" onkeypress="if(event.key === \'Enter\') sendMessage()">'
)
html = html.replace(
    '<button class="btn-primary" style="padding: 10px 20px;"><i class="fa-solid fa-paper-plane"></i></button>',
    '<button class="btn-primary" onclick="sendMessage()" style="padding: 10px 20px;"><i class="fa-solid fa-paper-plane"></i></button>'
)

# 5. Payments alert
html = html.replace(
    '<button class="action-btn"><i class="fa-solid fa-download"></i></button>',
    '<button class="action-btn" onclick="alert(\'Download complete!\')"><i class="fa-solid fa-download"></i></button>'
)

# 6. Real Moments extra pictures
extra_moments = """
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2);">
            <img src="assets/images/gallery_smile_1.jpg" alt="Moment 4" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2);">
            <img src="assets/images/cute_kids_clapping_1790833571210.jpg" alt="Moment 5" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2);">
            <img src="assets/images/party_moments_2_1790918669697.jpg" alt="Moment 6" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2);">
            <img src="assets/images/gallery_smile_2.jpg" alt="Moment 7" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px dashed var(--color-border); aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; flex-direction: column; color: var(--color-text-light); cursor: pointer;" onclick="document.getElementById('file-input').click()">
"""
html = html.replace(
    '<div style="border-radius: 12px; overflow: hidden; border: 1px dashed var(--color-border); aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; flex-direction: column; color: var(--color-text-light); cursor: pointer;" onclick="document.getElementById(\'file-input\').click()">',
    extra_moments
)

# 7. Details modal and JS
details_modal = """
  <!-- Details Modal -->
  <div class="modal" id="detailsModal">
    <div class="modal-content">
      <button class="close-modal" onclick="closeDetailsModal()"><i class="fa-solid fa-xmark"></i></button>
      <h2 style="margin-top: 0; font-family: var(--font-heading); color: var(--color-primary);">Event Details</h2>
      
      <div style="margin-bottom: 15px;">
        <h4 style="margin: 0 0 5px; color: var(--color-text);">Liam's 7th Birthday Party</h4>
        <p style="margin: 0; color: var(--color-text-light); font-size: 0.9rem;">#BKG-8409</p>
      </div>
      
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
        <div>
          <p style="margin: 0 0 5px; color: var(--color-text-light); font-size: 0.85rem;">Date</p>
          <p style="margin: 0; font-weight: bold;">Oct 15, 2026</p>
        </div>
        <div>
          <p style="margin: 0 0 5px; color: var(--color-text-light); font-size: 0.85rem;">Time</p>
          <p style="margin: 0; font-weight: bold;">2:00 PM - 4:00 PM</p>
        </div>
        <div>
          <p style="margin: 0 0 5px; color: var(--color-text-light); font-size: 0.85rem;">Location</p>
          <p style="margin: 0; font-weight: bold;">123 Magic Ave, NY</p>
        </div>
        <div>
          <p style="margin: 0 0 5px; color: var(--color-text-light); font-size: 0.85rem;">Entertainer</p>
          <p style="margin: 0; font-weight: bold;">Max The Hero</p>
        </div>
      </div>
      
      <div style="padding: 15px; background: rgba(56,149,200,0.1); border-left: 3px solid #3895c8; border-radius: 4px; margin-bottom: 20px;">
        <p style="margin: 0; font-size: 0.9rem;">Status: <strong style="color: #3895c8;">Confirmed</strong></p>
        <p style="margin: 5px 0 0; font-size: 0.85rem; color: var(--color-text-light);">Everything is ready for the party!</p>
      </div>
      
      <button class="btn-primary" style="width: 100%;" onclick="closeDetailsModal(); switchTab('messages', document.querySelectorAll('.admin-nav-item')[4])">Message Entertainer</button>
    </div>
  </div>
"""

js_addition = """
    function openDetailsModal() { document.getElementById('detailsModal').classList.add('active'); }
    function closeDetailsModal() { document.getElementById('detailsModal').classList.remove('active'); }
    
    function sendMessage() {
      const input = document.getElementById('chatInput');
      const text = input.value.trim();
      if (!text) return;
      
      const chatWindow = document.getElementById('chatWindow');
      
      const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      chatWindow.innerHTML += `
        <div style="align-self: flex-end; background: var(--color-primary); color: white; padding: 12px 18px; border-radius: 18px 18px 0 18px; max-width: 70%; animation: fadeIn 0.3s ease;">
          ${text}
          <div style="font-size: 0.7rem; margin-top: 5px; opacity: 0.8; text-align: right;">${timeStr}</div>
        </div>
      `;
      
      input.value = '';
      chatWindow.scrollTop = chatWindow.scrollHeight;
      
      setTimeout(() => {
        chatWindow.innerHTML += `
          <div style="align-self: flex-start; background: var(--color-surface); border: 1px solid var(--color-border); padding: 12px 18px; border-radius: 18px 18px 18px 0; max-width: 70%; animation: fadeIn 0.3s ease;">
            Thank you for reaching out! We've received your message and will respond with the best suggestions right away.
            <div style="font-size: 0.7rem; margin-top: 5px; color: var(--color-text-light);">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
          </div>
        `;
        chatWindow.scrollTop = chatWindow.scrollHeight;
      }, 1000);
    }
"""

html = html.replace('  <!-- Staff Modal -->', details_modal + '\n  <!-- Staff Modal -->')
html = html.replace('// Modal Logic', js_addition + '\n    // Modal Logic')

with open('user_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
