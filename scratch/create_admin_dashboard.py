import os

admin_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Dashboard | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    body {
      margin: 0;
      padding: 0;
      background: var(--color-bg);
      color: var(--color-text);
      display: flex;
      height: 100vh;
      overflow: hidden;
    }
    
    /* Sidebar */
    .admin-sidebar {
      width: 280px;
      background: var(--color-surface);
      border-right: 1px solid var(--color-border);
      display: flex;
      flex-direction: column;
      padding: 30px 20px;
      transition: all 0.3s;
      z-index: 10;
    }
    .admin-logo {
      display: flex;
      align-items: center;
      gap: 15px;
      margin-bottom: 40px;
      text-decoration: none;
    }
    .admin-logo img {
      height: 50px;
      object-fit: contain;
    }
    .admin-logo span {
      font-family: var(--font-magic);
      font-size: 2.2rem;
      color: var(--color-primary);
    }
    
    .admin-nav {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .admin-nav-item {
      display: flex;
      align-items: center;
      gap: 15px;
      padding: 15px 20px;
      border-radius: 12px;
      color: var(--color-text-light);
      text-decoration: none;
      font-weight: 600;
      transition: 0.3s;
      cursor: pointer;
    }
    .admin-nav-item i {
      font-size: 1.2rem;
      width: 25px;
      text-align: center;
    }
    .admin-nav-item:hover, .admin-nav-item.active {
      background: rgba(210, 75, 118, 0.1);
      color: var(--color-primary);
    }
    
    .sidebar-toggles {
      margin-top: auto;
      border-top: 1px solid var(--color-border);
      padding-top: 20px;
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    .toggle-btn {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 20px;
      background: rgba(0,0,0,0.2);
      border: 1px solid var(--color-border);
      border-radius: 12px;
      color: var(--color-text);
      cursor: pointer;
      font-weight: 600;
      transition: 0.3s;
    }
    .toggle-btn:hover { background: rgba(0,0,0,0.4); border-color: var(--color-primary); }
    
    /* Content Area */
    .admin-content {
      flex: 1;
      padding: 40px;
      overflow-y: auto;
      background: var(--color-bg);
    }
    
    .dashboard-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 40px;
    }
    .dashboard-title {
      font-family: var(--font-heading);
      font-size: 2.5rem;
      color: var(--color-text);
      margin: 0;
    }
    .user-profile {
      display: flex;
      align-items: center;
      gap: 15px;
    }
    .user-profile img {
      width: 45px;
      height: 45px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--color-primary);
    }
    
    /* Grid Stats */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 25px;
      margin-bottom: 40px;
    }
    .stat-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 20px;
      padding: 30px;
      display: flex;
      align-items: center;
      gap: 20px;
      transition: 0.3s;
    }
    .stat-card:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,0,0,0.2); border-color: var(--color-primary); }
    .stat-icon {
      width: 60px;
      height: 60px;
      border-radius: 15px;
      background: rgba(56, 149, 200, 0.1);
      color: #3895c8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
    }
    .stat-info h3 { margin: 0 0 5px; font-size: 1.1rem; color: var(--color-text-light); }
    .stat-info p { margin: 0; font-size: 2rem; font-weight: bold; color: var(--color-text); }
    
    /* Recent Activity / Tables */
    .content-panel {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 20px;
      padding: 30px;
      margin-bottom: 30px;
    }
    .panel-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 25px;
    }
    .panel-header h3 { font-size: 1.5rem; margin: 0; font-family: var(--font-heading); }
    .table-container { overflow-x: auto; }
    .table { width: 100%; border-collapse: collapse; min-width: 600px; }
    .table th, .table td { padding: 15px; text-align: left; border-bottom: 1px solid var(--color-border); }
    .table th { color: var(--color-text-light); font-weight: 600; }
    .table tr:hover td { background: rgba(255,255,255,0.02); }
    .status-badge { padding: 6px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; }
    .status-success { background: rgba(46, 204, 113, 0.1); color: #2ecc71; }
    .status-pending { background: rgba(241, 196, 15, 0.1); color: #f1c40f; }

    /* RTL Support */
    [dir="rtl"] .admin-sidebar { border-right: none; border-left: 1px solid var(--color-border); }
    [dir="rtl"] .table th, [dir="rtl"] .table td { text-align: right; }
    
    /* Tab Logic */
    .tab-content { display: none; }
    .tab-content.active { display: block; animation: fadeIn 0.4s ease; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    
    @media (max-width: 768px) {
      body { flex-direction: column; overflow: auto; }
      .admin-sidebar { width: 100%; border-right: none; border-bottom: 1px solid var(--color-border); }
      .admin-content { padding: 20px; }
    }
  </style>
</head>
<body data-theme="dark">

  <div class="admin-sidebar">
    <a href="index.html" class="admin-logo">
      <img src="assets/images/logoo.png" alt="Magiqo">
      <span>Magiqo</span>
    </a>
    
    <div class="admin-nav">
      <div class="admin-nav-item active" onclick="switchTab('overview', this)">
        <i class="fa-solid fa-house"></i> Overview
      </div>
      <div class="admin-nav-item" onclick="switchTab('bookings', this)">
        <i class="fa-solid fa-calendar-check"></i> Bookings
      </div>
      <div class="admin-nav-item" onclick="switchTab('entertainers', this)">
        <i class="fa-solid fa-wand-magic-sparkles"></i> Entertainers
      </div>
      <div class="admin-nav-item" onclick="switchTab('users', this)">
        <i class="fa-solid fa-users"></i> Users
      </div>
      <div class="admin-nav-item" onclick="switchTab('settings', this)">
        <i class="fa-solid fa-gear"></i> Settings
      </div>
    </div>
    
    <div class="sidebar-toggles">
      <button id="theme-toggle" class="toggle-btn">
        <span>Dark / Light</span>
        <i class="fa-solid fa-moon"></i>
      </button>
      <button id="rtl-toggle" class="toggle-btn">
        <span>LTR / RTL</span>
        <i class="fa-solid fa-language"></i>
      </button>
    </div>
  </div>

  <div class="admin-content">
    
    <div class="dashboard-header">
      <h1 class="dashboard-title">Overview</h1>
      <div class="user-profile">
        <div style="text-align: right;">
          <div style="font-weight: bold;">Admin User</div>
          <div style="font-size: 0.85rem; color: var(--color-text-light);">Super Admin</div>
        </div>
        <img src="assets/images/founder_mark.jpg" alt="Admin">
      </div>
    </div>
    
    <!-- OVERVIEW TAB -->
    <div id="overview" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(210, 75, 118, 0.1); color: var(--color-primary);"><i class="fa-solid fa-calendar-check"></i></div>
          <div class="stat-info">
            <h3>Total Bookings</h3>
            <p>1,284</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon"><i class="fa-solid fa-users"></i></div>
          <div class="stat-info">
            <h3>Active Users</h3>
            <p>8,592</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(46, 204, 113, 0.1); color: #2ecc71;"><i class="fa-solid fa-dollar-sign"></i></div>
          <div class="stat-info">
            <h3>Monthly Revenue</h3>
            <p>$45,200</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(241, 196, 15, 0.1); color: #f1c40f;"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
          <div class="stat-info">
            <h3>Entertainers</h3>
            <p>156</p>
          </div>
        </div>
      </div>
      
      <div class="content-panel">
        <div class="panel-header">
          <h3>Recent Bookings</h3>
          <button style="padding: 8px 15px; border-radius: 8px; background: transparent; border: 1px solid var(--color-border); color: var(--color-text); cursor: pointer; transition: 0.3s;" onmouseover="this.style.borderColor='var(--color-primary)'" onmouseout="this.style.borderColor='var(--color-border)'">View All</button>
        </div>
        <div class="table-container">
          <table class="table">
            <thead>
              <tr>
                <th>Client</th>
                <th>Event Type</th>
                <th>Date</th>
                <th>Amount</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Sarah Jenkins</td>
                <td>Kids Birthday</td>
                <td>Oct 15, 2026</td>
                <td>$450</td>
                <td><span class="status-badge status-success">Confirmed</span></td>
              </tr>
              <tr>
                <td>Michael Vance</td>
                <td>Corporate Gala</td>
                <td>Oct 18, 2026</td>
                <td>$2,100</td>
                <td><span class="status-badge status-pending">Pending</span></td>
              </tr>
              <tr>
                <td>Emily Davis</td>
                <td>Wedding Reception</td>
                <td>Oct 20, 2026</td>
                <td>$800</td>
                <td><span class="status-badge status-success">Confirmed</span></td>
              </tr>
              <tr>
                <td>John Smith</td>
                <td>Magic Show</td>
                <td>Oct 25, 2026</td>
                <td>$300</td>
                <td><span class="status-badge status-pending">Pending</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    
    <!-- BOOKINGS TAB -->
    <div id="bookings" class="tab-content">
      <div class="content-panel">
        <h2 style="margin-top:0;">All Bookings</h2>
        <p style="color: var(--color-text-light);">Manage and track all event reservations here.</p>
        <div style="height: 300px; display: flex; align-items: center; justify-content: center; border: 2px dashed var(--color-border); border-radius: 12px; margin-top: 20px; color: var(--color-text-light);">
          Booking Management Interface
        </div>
      </div>
    </div>

    <!-- ENTERTAINERS TAB -->
    <div id="entertainers" class="tab-content">
      <div class="content-panel">
        <h2 style="margin-top:0;">Our Entertainers</h2>
        <p style="color: var(--color-text-light);">Approve, manage, and review performance metrics for your magicians and artists.</p>
        <div style="height: 300px; display: flex; align-items: center; justify-content: center; border: 2px dashed var(--color-border); border-radius: 12px; margin-top: 20px; color: var(--color-text-light);">
          Entertainer Directory & Analytics
        </div>
      </div>
    </div>

    <!-- USERS TAB -->
    <div id="users" class="tab-content">
      <div class="content-panel">
        <h2 style="margin-top:0;">User Management</h2>
        <p style="color: var(--color-text-light);">Control user accounts, roles, and permissions.</p>
        <div style="height: 300px; display: flex; align-items: center; justify-content: center; border: 2px dashed var(--color-border); border-radius: 12px; margin-top: 20px; color: var(--color-text-light);">
          User Database Table
        </div>
      </div>
    </div>
    
    <!-- SETTINGS TAB -->
    <div id="settings" class="tab-content">
      <div class="content-panel">
        <h2 style="margin-top:0;">Platform Settings</h2>
        <p style="color: var(--color-text-light);">Configure global settings, payment gateways, and email templates.</p>
        <div style="height: 300px; display: flex; align-items: center; justify-content: center; border: 2px dashed var(--color-border); border-radius: 12px; margin-top: 20px; color: var(--color-text-light);">
          Global Configuration Form
        </div>
      </div>
    </div>

  </div>

  <script src="js/theme.js"></script>
  <script>
    function switchTab(tabId, element) {
      // Remove active class from all nav items
      document.querySelectorAll('.admin-nav-item').forEach(el => el.classList.remove('active'));
      // Add active class to clicked nav item
      element.classList.add('active');
      
      // Hide all tab content
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      // Show requested tab content
      document.getElementById(tabId).classList.add('active');
      
      // Update header title based on text
      document.querySelector('.dashboard-title').textContent = element.textContent.trim();
    }
  </script>
</body>
</html>
"""

with open(r'c:\Users\vigas\Desktop\magiqo\admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
