import re

with open('user_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<title>Admin Dashboard | Magiqo</title>', '<title>User Dashboard | Magiqo</title>')

nav_replacement = """
    <div class="admin-nav">
      <div class="admin-nav-item active" onclick="switchTab('overview', this)">
        <i class="fa-solid fa-house"></i> Dashboard
      </div>
      <div class="admin-nav-item" onclick="switchTab('my-bookings', this)">
        <i class="fa-solid fa-calendar-check"></i> My Bookings
      </div>
      <div class="admin-nav-item" onclick="switchTab('wishlist', this)">
        <i class="fa-solid fa-heart"></i> Wishlist
      </div>
      <div class="admin-nav-item" onclick="switchTab('profile', this)">
        <i class="fa-solid fa-user"></i> Profile Settings
      </div>
    </div>
"""
html = re.sub(r'<div class="admin-nav">.*?</div>\s*<div class="sidebar-toggles">', nav_replacement + '\n    <div class="sidebar-toggles">', html, flags=re.DOTALL)

html = html.replace('<div style="font-weight: bold;">Admin User</div>', '<div style="font-weight: bold;">Jane Doe</div>')
html = html.replace('<div style="font-size: 0.85rem; color: var(--color-text-light);" class="d-none-mobile">Super Admin</div>', '<div style="font-size: 0.85rem; color: var(--color-text-light);" class="d-none-mobile">Magiqo Member</div>')
html = html.replace('assets/images/founder_mark.jpg', 'assets/images/james_boy_smile.jpg')

overview_content_replacement = """
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
        <h2 style="margin: 0; font-family: var(--font-magic); font-size: 2.5rem; color: var(--color-primary);">Welcome back, Jane!</h2>
        <a href="packages.html" class="btn-primary" style="background: #3895c8; text-decoration: none;"><i class="fa-solid fa-plus"></i> New Booking</a>
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
            <p>5</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(210, 75, 118, 0.1); color: var(--color-primary);"><i class="fa-solid fa-heart"></i></div>
          <div class="stat-info">
            <h3>Saved Packages</h3>
            <p>3</p>
          </div>
        </div>
      </div>

      <div class="content-panel">
        <div class="panel-header">
          <h3><i class="fa-solid fa-calendar" style="color: var(--color-primary); margin-right: 10px;"></i> Your Next Event</h3>
        </div>
        <div style="background: rgba(56,149,200,0.05); border: 1px solid rgba(56,149,200,0.2); border-radius: 12px; padding: 20px;">
          <h4 style="margin: 0 0 10px; font-size: 1.2rem; color: #3895c8;">Liam's 7th Birthday Party</h4>
          <p style="margin: 0 0 5px; color: var(--color-text-light);"><i class="fa-regular fa-calendar"></i> <strong>Date:</strong> Saturday, Oct 15th, 2026</p>
          <p style="margin: 0 0 15px; color: var(--color-text-light);"><i class="fa-regular fa-clock"></i> <strong>Time:</strong> 2:00 PM - 4:00 PM</p>
          <div style="display: flex; gap: 10px;">
            <button class="btn-primary" style="padding: 8px 15px; font-size: 0.9rem;">View Details</button>
            <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text); padding: 8px 15px; font-size: 0.9rem;">Contact Support</button>
          </div>
        </div>
      </div>
"""

html = re.sub(r'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">.*?<div class="content-panel" style="flex: 2;">', overview_content_replacement + '\n    <div class="content-panel" style="flex: 2; display: none;">', html, flags=re.DOTALL)

with open('user_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
