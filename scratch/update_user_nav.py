import re

with open('user_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_nav = """    <div class="admin-nav">
      <div class="admin-nav-item active" onclick="switchTab('overview', this)">
        <i class="fa-solid fa-house"></i> Dashboard
      </div>
      <a href="entertainers.html" class="admin-nav-item" style="text-decoration: none;">
        <i class="fa-solid fa-wand-magic-sparkles"></i> Explore Entertainers
      </a>
      <div class="admin-nav-item" onclick="switchTab('bookings', this)">
        <i class="fa-solid fa-calendar-check"></i> My Bookings
      </div>
      <div class="admin-nav-item" onclick="switchTab('events', this)">
        <i class="fa-solid fa-cake-candles"></i> My Events
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
      <div class="admin-nav-item" onclick="switchTab('reviews', this)">
        <i class="fa-solid fa-star"></i> Reviews & Ratings
      </div>
      <div class="admin-nav-item" onclick="switchTab('real-moments', this)">
        <i class="fa-solid fa-camera-retro"></i> Real Moments
      </div>
      <div class="admin-nav-item" onclick="switchTab('notifications', this)">
        <i class="fa-solid fa-bell"></i> Notifications
      </div>
      <div class="admin-nav-item" onclick="switchTab('profile', this)">
        <i class="fa-solid fa-user"></i> Profile Settings
      </div>
    </div>"""

html = re.sub(r'<div class="admin-nav">.*?</div>\s*<div class="sidebar-toggles">', new_nav + '\n    <div class="sidebar-toggles">', html, flags=re.DOTALL)

# Add missing tab divs at the end of the tabs section
missing_tabs = """
    <!-- EVENTS TAB -->
    <div id="events" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">My Events</h3>
          <button class="btn-primary" onclick="openModal()"><i class="fa-solid fa-plus"></i> Create Event</button>
        </div>
        <p style="color: var(--color-text-light);">Manage event details, dates, venues, guest/member count, and themes.</p>
        <div style="padding: 40px; text-align: center; color: var(--color-text-light); background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--color-border);">
          <i class="fa-solid fa-cake-candles" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
          <p>You have no upcoming events.</p>
        </div>
      </div>
    </div>

    <!-- FAVORITES TAB -->
    <div id="favorites" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Favorites</h3>
        </div>
        <p style="color: var(--color-text-light);">Saved entertainers and preferred packages.</p>
        <div style="padding: 40px; text-align: center; color: var(--color-text-light); background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--color-border);">
          <i class="fa-solid fa-heart-crack" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
          <p>No favorites added yet.</p>
        </div>
      </div>
    </div>

    <!-- MESSAGES TAB -->
    <div id="messages" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Messages</h3>
        </div>
        <p style="color: var(--color-text-light);">Chat or communicate with entertainers/support.</p>
        <div style="padding: 40px; text-align: center; color: var(--color-text-light); background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--color-border);">
          <i class="fa-solid fa-comments" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
          <p>No messages to display.</p>
        </div>
      </div>
    </div>

    <!-- PAYMENTS TAB -->
    <div id="payments" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Payments & Invoices</h3>
        </div>
        <p style="color: var(--color-text-light);">Payment history, pending payments, invoices, and refunds.</p>
        <div style="padding: 40px; text-align: center; color: var(--color-text-light); background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--color-border);">
          <i class="fa-solid fa-file-invoice-dollar" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
          <p>No recent transactions.</p>
        </div>
      </div>
    </div>

    <!-- REVIEWS TAB -->
    <div id="reviews" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Reviews & Ratings</h3>
        </div>
        <p style="color: var(--color-text-light);">Reviews given and entertainer feedback.</p>
        <div style="padding: 40px; text-align: center; color: var(--color-text-light); background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--color-border);">
          <i class="fa-solid fa-star-half-stroke" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
          <p>You haven't reviewed any entertainers yet.</p>
        </div>
      </div>
    </div>

    <!-- REAL MOMENTS TAB -->
    <div id="real-moments" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Real Moments</h3>
          <button class="btn-primary" onclick="alert('Open file picker')"><i class="fa-solid fa-upload"></i> Upload Media</button>
        </div>
        <p style="color: var(--color-text-light);">Upload and manage photos/videos from completed events.</p>
        <div style="padding: 40px; text-align: center; color: var(--color-text-light); background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--color-border);">
          <i class="fa-solid fa-camera-retro" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
          <p>No media uploaded. Share your magic moments!</p>
        </div>
      </div>
    </div>

    <!-- NOTIFICATIONS TAB -->
    <div id="notifications" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Notifications</h3>
          <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);"><i class="fa-solid fa-check-double"></i> Mark all as read</button>
        </div>
        <p style="color: var(--color-text-light);">Booking confirmations, reminders, payment updates.</p>
        <div style="padding: 40px; text-align: center; color: var(--color-text-light); background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed var(--color-border);">
          <i class="fa-regular fa-bell-slash" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
          <p>You're all caught up!</p>
        </div>
      </div>
    </div>

    <!-- PROFILE TAB -->
    <div id="profile" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0; font-family: var(--font-magic); color: var(--color-primary); background: none; -webkit-text-fill-color: initial;">Profile Settings</h3>
          <button class="btn-primary"><i class="fa-solid fa-floppy-disk"></i> Save Changes</button>
        </div>
        <p style="color: var(--color-text-light);">Manage your personal information and preferences.</p>
        <form style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
          <div class="form-group">
            <label>Full Name</label>
            <input type="text" class="form-control" value="Jane Doe">
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="email" class="form-control" value="jane@example.com">
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="text" class="form-control" value="(555) 123-4567">
          </div>
          <div class="form-group">
            <label>Location</label>
            <input type="text" class="form-control" value="New York, NY">
          </div>
        </form>
      </div>
    </div>
"""

# Insert missing tabs right before the closing div of admin-content
html = re.sub(r'    </div>\s*</div>\s*<!-- Staff Modal -->', missing_tabs + '\n    </div>\n\n  </div>\n\n  <!-- Staff Modal -->', html, flags=re.DOTALL)

with open('user_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
