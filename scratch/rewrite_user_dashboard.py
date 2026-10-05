import re

with open('user_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sidebar Nav
nav_pattern = r'<div class="admin-nav">.*?</div>\s*<div class="sidebar-toggles">'
nav_replacement = """    <div class="admin-nav">
      <div class="admin-nav-item active" onclick="switchTab('overview', this)">
        <i class="fa-solid fa-house"></i> Dashboard
      </div>
      <div class="admin-nav-item" onclick="switchTab('explore', this)">
        <i class="fa-solid fa-wand-magic-sparkles"></i> Explore Entertainers
      </div>
      <div class="admin-nav-item" onclick="switchTab('bookings', this)">
        <i class="fa-solid fa-calendar-check"></i> My Bookings
      </div>
      <div class="admin-nav-item" onclick="switchTab('favorites', this)">
        <i class="fa-solid fa-heart"></i> Favorites
      </div>
      <div class="admin-nav-item" onclick="switchTab('messages', this)">
        <i class="fa-solid fa-envelope"></i> Messages
      </div>
      <div class="admin-nav-item" onclick="switchTab('payments', this)">
        <i class="fa-solid fa-file-invoice-dollar"></i> Payments & Invoices
      </div>
      <div class="admin-nav-item" onclick="switchTab('real-moments', this)">
        <i class="fa-solid fa-camera-retro"></i> Real Moments
      </div>
    </div>
    <div class="sidebar-toggles">"""
html = re.sub(nav_pattern, nav_replacement, html, flags=re.DOTALL)

# 2. Extract content from '<!-- OVERVIEW TAB -->' to the end of the tabs.
# We will completely replace all tabs.
tabs_pattern = r'<!-- OVERVIEW TAB -->.*?    </div>\s*</div>\s*<!-- Staff Modal -->'

tabs_replacement = """<!-- OVERVIEW TAB -->
    <div id="overview" class="tab-content active">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
        <h2 style="margin: 0; font-family: var(--font-magic); font-size: 2.5rem; color: var(--color-primary);">Welcome back, Jane!</h2>
        <a href="#" onclick="openModal()" class="btn-primary" style="background: #3895c8; text-decoration: none;"><i class="fa-solid fa-plus"></i> New Booking</a>
      </div>
      
      <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));">
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(46, 204, 113, 0.1); color: #2ecc71;"><i class="fa-solid fa-calendar-check"></i></div>
          <div class="stat-info">
            <h3>Upcoming Events</h3>
            <p>2</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(56, 149, 200, 0.1); color: #3895c8;"><i class="fa-solid fa-clock-rotate-left"></i></div>
          <div class="stat-info">
            <h3>Past Events</h3>
            <p>1</p>
          </div>
        </div>
      </div>

      <div class="content-panel">
        <div class="panel-header">
          <h3><i class="fa-solid fa-calendar" style="color: var(--color-primary); margin-right: 10px;"></i> Upcoming Events (2)</h3>
        </div>
        <div style="background: rgba(56,149,200,0.05); border: 1px solid rgba(56,149,200,0.2); border-radius: 12px; padding: 20px; margin-bottom: 15px;">
          <h4 style="margin: 0 0 10px; font-size: 1.2rem; color: #3895c8;">Liam's 7th Birthday Party</h4>
          <p style="margin: 0 0 5px; color: var(--color-text-light);"><i class="fa-regular fa-calendar"></i> <strong>Date:</strong> Saturday, Oct 15th, 2026</p>
          <p style="margin: 0 0 15px; color: var(--color-text-light);"><i class="fa-regular fa-clock"></i> <strong>Time:</strong> 2:00 PM - 4:00 PM</p>
          <div style="display: flex; gap: 10px;">
            <a href="#" class="btn-primary" style="padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">View Details</a>
            <a href="#" class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text); padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">Contact Support</a>
          </div>
        </div>
        
        <div style="background: rgba(56,149,200,0.05); border: 1px solid rgba(56,149,200,0.2); border-radius: 12px; padding: 20px;">
          <h4 style="margin: 0 0 10px; font-size: 1.2rem; color: #3895c8;">Halloween Magic Show</h4>
          <p style="margin: 0 0 5px; color: var(--color-text-light);"><i class="fa-regular fa-calendar"></i> <strong>Date:</strong> Friday, Oct 31st, 2026</p>
          <p style="margin: 0 0 15px; color: var(--color-text-light);"><i class="fa-regular fa-clock"></i> <strong>Time:</strong> 6:00 PM - 8:00 PM</p>
          <div style="display: flex; gap: 10px;">
            <a href="#" class="btn-primary" style="padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">View Details</a>
            <a href="#" class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text); padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">Contact Support</a>
          </div>
        </div>
      </div>
      
      <div class="content-panel">
        <div class="panel-header">
          <h3><i class="fa-solid fa-clock-rotate-left" style="color: var(--color-primary); margin-right: 10px;"></i> Past Events (1)</h3>
        </div>
        <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
          <h4 style="margin: 0 0 10px; font-size: 1.2rem; color: var(--color-text);">Jane's Anniversary Party</h4>
          <p style="margin: 0 0 5px; color: var(--color-text-light);"><i class="fa-regular fa-calendar"></i> <strong>Date:</strong> August 12th, 2026</p>
          <div style="display: flex; gap: 10px; margin-top: 15px;">
            <a href="#" onclick="switchTab('real-moments', document.querySelectorAll('.admin-nav-item')[6])" class="btn-primary" style="padding: 8px 15px; font-size: 0.9rem; text-decoration: none;">View Media</a>
          </div>
        </div>
      </div>
    </div>

    <!-- EXPLORE ENTERTAINERS TAB -->
    <div id="explore" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Explore Entertainers</h3>
        </div>
        <p style="color: var(--color-text-light); margin-bottom: 25px;">Browse magicians, clowns, storytellers, and balloon artists to book for your next event.</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px;">
          <!-- Card 1 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden;">
            <img src="assets/images/founder_mark.jpg" alt="Max The Hero" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Max The Hero</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Superhero Impersonator & Action Games</p>
              <div style="display: flex; gap: 10px;">
                <button class="btn-primary" style="flex: 1;" onclick="openModal()">Book Now</button>
                <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);" onclick="alert('Added to Favorites!')"><i class="fa-solid fa-heart"></i></button>
              </div>
            </div>
          </div>
          <!-- Card 2 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden;">
            <img src="assets/images/james_boy_smile.jpg" alt="The Great Houdini" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">The Great Houdini</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Master Magician & Illusionist</p>
              <div style="display: flex; gap: 10px;">
                <button class="btn-primary" style="flex: 1;" onclick="openModal()">Book Now</button>
                <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);" onclick="alert('Added to Favorites!')"><i class="fa-solid fa-heart"></i></button>
              </div>
            </div>
          </div>
          <!-- Card 3 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden;">
            <img src="assets/images/happy_kids_clown.jpg" alt="Chuckles the Clown" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Chuckles the Clown</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Comedy, Juggling & Balloon Animals</p>
              <div style="display: flex; gap: 10px;">
                <button class="btn-primary" style="flex: 1;" onclick="openModal()">Book Now</button>
                <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);" onclick="alert('Added to Favorites!')"><i class="fa-solid fa-heart"></i></button>
              </div>
            </div>
          </div>
          <!-- Card 4 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden;">
            <div style="width: 100%; height: 200px; background: rgba(210, 75, 118, 0.1); display: flex; align-items: center; justify-content: center; color: var(--color-primary); font-size: 3rem;">
              <i class="fa-solid fa-crown"></i>
            </div>
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Princess Aurora</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Storytelling & Royal Activities</p>
              <div style="display: flex; gap: 10px;">
                <button class="btn-primary" style="flex: 1;" onclick="openModal()">Book Now</button>
                <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);" onclick="alert('Added to Favorites!')"><i class="fa-solid fa-heart"></i></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- BOOKINGS TAB -->
    <div id="bookings" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">My Bookings</h3>
          <button class="btn-primary" onclick="openModal()"><i class="fa-solid fa-plus"></i> New Booking</button>
        </div>
        
        <div class="table-container">
          <table class="table" id="bookingsTable">
            <thead>
              <tr>
                <th>Booking ID</th>
                <th>Event Type</th>
                <th>Date</th>
                <th>Amount</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="bookingsBody">
              <tr data-status="confirmed">
                <td>#BKG-8410</td><td>Halloween Magic Show</td><td>Oct 31, 2026</td><td>$350</td><td><span class="status-badge status-success">Confirmed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button></td>
              </tr>
              <tr data-status="confirmed">
                <td>#BKG-8409</td><td>Liam's 7th Birthday Party</td><td>Oct 15, 2026</td><td>$600</td><td><span class="status-badge status-success">Confirmed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button></td>
              </tr>
              <tr data-status="completed">
                <td>#BKG-8407</td><td>Jane's Anniversary Party</td><td>Aug 12, 2026</td><td>$400</td><td><span class="status-badge" style="background: rgba(56, 149, 200, 0.1); color: #3895c8;">Completed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- FAVORITES TAB -->
    <div id="favorites" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">My Favorites</h3>
        </div>
        <p style="color: var(--color-text-light); margin-bottom: 25px;">Quickly book your favorite entertainers and packages.</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px;">
          <!-- Fav 1 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-primary); border-radius: 12px; overflow: hidden; position: relative;">
            <div style="position: absolute; top: 10px; right: 10px; color: var(--color-primary); font-size: 1.5rem; background: rgba(0,0,0,0.5); padding: 5px; border-radius: 50%;"><i class="fa-solid fa-heart"></i></div>
            <img src="assets/images/james_boy_smile.jpg" alt="The Great Houdini" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">The Great Houdini</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Master Magician & Illusionist</p>
              <button class="btn-primary" style="width: 100%;" onclick="openModal()">Book Now</button>
            </div>
          </div>
          <!-- Fav 2 -->
          <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-primary); border-radius: 12px; overflow: hidden; position: relative;">
            <div style="position: absolute; top: 10px; right: 10px; color: var(--color-primary); font-size: 1.5rem; background: rgba(0,0,0,0.5); padding: 5px; border-radius: 50%;"><i class="fa-solid fa-heart"></i></div>
            <div style="width: 100%; height: 200px; background: rgba(210, 75, 118, 0.1); display: flex; align-items: center; justify-content: center; color: var(--color-primary); font-size: 3rem;">
              <i class="fa-solid fa-crown"></i>
            </div>
            <div style="padding: 20px;">
              <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Princess Aurora</h4>
              <p style="margin: 0 0 15px; color: var(--color-text-light); font-size: 0.9rem;">Storytelling & Royal Activities</p>
              <button class="btn-primary" style="width: 100%;" onclick="openModal()">Book Now</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- MESSAGES TAB -->
    <div id="messages" class="tab-content">
      <div class="content-panel" style="display: flex; flex-direction: column; height: 600px; padding: 0; overflow: hidden;">
        <div class="panel-header" style="padding: 20px; border-bottom: 1px solid var(--color-border); margin: 0; background: rgba(255,255,255,0.02);">
          <h3 style="font-size: 1.8rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Messages</h3>
          <span style="font-size: 0.9rem; color: var(--color-text-light);">Chatting with: Magiqo Support</span>
        </div>
        
        <div style="flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; background: rgba(0,0,0,0.2);">
          <div style="align-self: flex-end; background: var(--color-primary); color: white; padding: 12px 18px; border-radius: 18px 18px 0 18px; max-width: 70%;">
            Hi, I'm interested in the Halloween Magic Show package. Does it include spooky balloon animals?
            <div style="font-size: 0.7rem; margin-top: 5px; opacity: 0.8; text-align: right;">10:30 AM</div>
          </div>
          <div style="align-self: flex-start; background: var(--color-surface); border: 1px solid var(--color-border); padding: 12px 18px; border-radius: 18px 18px 18px 0; max-width: 70%;">
            Hello Jane! Yes, the Halloween package includes spooky themed balloon animals, such as bats, spiders, and pumpkins! Let me know if you'd like to proceed with the booking.
            <div style="font-size: 0.7rem; margin-top: 5px; color: var(--color-text-light);">10:35 AM</div>
          </div>
          <div style="align-self: flex-end; background: var(--color-primary); color: white; padding: 12px 18px; border-radius: 18px 18px 0 18px; max-width: 70%;">
            That sounds perfect! Can I add an extra 30 minutes to the show?
            <div style="font-size: 0.7rem; margin-top: 5px; opacity: 0.8; text-align: right;">10:42 AM</div>
          </div>
        </div>
        
        <div style="padding: 15px 20px; background: var(--color-surface); border-top: 1px solid var(--color-border); display: flex; gap: 10px;">
          <input type="text" class="form-control" placeholder="Type a message..." style="flex: 1;">
          <button class="btn-primary" style="padding: 10px 20px;"><i class="fa-solid fa-paper-plane"></i></button>
        </div>
      </div>
    </div>

    <!-- PAYMENTS TAB -->
    <div id="payments" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Payments & Invoices</h3>
        </div>
        
        <div class="table-container">
          <table class="table">
            <thead>
              <tr>
                <th>Invoice ID</th>
                <th>Event</th>
                <th>Date</th>
                <th>Amount</th>
                <th>Status</th>
                <th>Download</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>#INV-99821</td>
                <td>Liam's 7th Birthday Party</td>
                <td>Oct 02, 2026</td>
                <td>$600.00</td>
                <td><span class="status-badge status-success">Paid</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-download"></i></button></td>
              </tr>
              <tr>
                <td>#INV-99820</td>
                <td>Halloween Magic Show</td>
                <td>Oct 01, 2026</td>
                <td>$350.00</td>
                <td><span class="status-badge status-success">Paid</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-download"></i></button></td>
              </tr>
              <tr>
                <td>#INV-99810</td>
                <td>Jane's Anniversary Party</td>
                <td>Aug 01, 2026</td>
                <td>$400.00</td>
                <td><span class="status-badge status-success">Paid</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-download"></i></button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- REAL MOMENTS TAB -->
    <div id="real-moments" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Real Moments</h3>
          <button class="btn-primary" onclick="document.getElementById('file-input').click()"><i class="fa-solid fa-upload"></i> Upload Media</button>
          <input type="file" id="file-input" multiple style="display: none;" accept="image/*">
        </div>
        <p style="color: var(--color-text-light); margin-bottom: 25px;">Photos and videos from your completed events.</p>
        
        <h4 style="margin: 0 0 15px; font-size: 1.2rem; color: var(--color-primary);">Jane's Anniversary Party (Aug 12, 2026)</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px;">
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2);">
            <img src="assets/images/happy_kids_clown.jpg" alt="Moment 1" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2);">
            <img src="assets/images/james_boy_smile.jpg" alt="Moment 2" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--color-border); aspect-ratio: 1/1; background: rgba(0,0,0,0.2);">
            <img src="assets/images/founder_mark.jpg" alt="Moment 3" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px dashed var(--color-border); aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; flex-direction: column; color: var(--color-text-light); cursor: pointer;" onclick="document.getElementById('file-input').click()">
            <i class="fa-solid fa-plus" style="font-size: 2rem; margin-bottom: 10px;"></i>
            <span>Add More</span>
          </div>
        </div>
      </div>
    </div>
    
    </div>

  </div>

  <!-- Booking Modal -->"""

html = re.sub(tabs_pattern, tabs_replacement, html, flags=re.DOTALL)

with open('user_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
