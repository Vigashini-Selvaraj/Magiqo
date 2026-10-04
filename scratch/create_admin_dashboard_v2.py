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
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  
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
    .admin-logo img { height: 50px; object-fit: contain; }
    .admin-logo span { font-family: var(--font-magic); font-size: 2.2rem; color: var(--color-primary); }
    
    .admin-nav { flex: 1; display: flex; flex-direction: column; gap: 8px; overflow-y: auto; }
    .admin-nav-item {
      display: flex; align-items: center; gap: 15px; padding: 12px 18px;
      border-radius: 12px; color: var(--color-text-light); text-decoration: none;
      font-weight: 600; transition: 0.3s; cursor: pointer;
    }
    .admin-nav-item i { font-size: 1.2rem; width: 25px; text-align: center; }
    .admin-nav-item:hover, .admin-nav-item.active { background: rgba(210, 75, 118, 0.1); color: var(--color-primary); }
    
    .sidebar-toggles { margin-top: auto; border-top: 1px solid var(--color-border); padding-top: 20px; display: flex; flex-direction: column; gap: 10px; }
    .toggle-btn {
      display: flex; align-items: center; justify-content: space-between; padding: 10px 15px;
      background: rgba(0,0,0,0.2); border: 1px solid var(--color-border); border-radius: 10px;
      color: var(--color-text); cursor: pointer; font-weight: 600; transition: 0.3s;
    }
    .toggle-btn:hover { background: rgba(0,0,0,0.4); border-color: var(--color-primary); }
    
    /* Content Area */
    .admin-content { flex: 1; padding: 30px 40px; overflow-y: auto; background: var(--color-bg); position: relative; }
    
    .dashboard-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
    .dashboard-title { font-family: var(--font-heading); font-size: 2.2rem; color: var(--color-text); margin: 0; }
    .user-profile { display: flex; align-items: center; gap: 15px; }
    .user-profile img { width: 45px; height: 45px; border-radius: 50%; object-fit: cover; border: 2px solid var(--color-primary); }
    
    /* Grid Stats */
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 30px; }
    .stat-card {
      background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 16px;
      padding: 20px; display: flex; align-items: center; gap: 15px; transition: 0.3s;
    }
    .stat-card:hover { transform: translateY(-5px); border-color: var(--color-primary); }
    .stat-icon { width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; }
    .stat-info h3 { margin: 0 0 5px; font-size: 0.9rem; color: var(--color-text-light); }
    .stat-info p { margin: 0; font-size: 1.6rem; font-weight: bold; color: var(--color-text); }
    
    /* Panels */
    .content-panel { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 16px; padding: 25px; margin-bottom: 25px; }
    .panel-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .panel-header h3 { font-size: 1.3rem; margin: 0; font-family: var(--font-heading); }
    
    /* Quick Shortcuts */
    .shortcuts-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
    .shortcut-btn {
      padding: 15px; background: rgba(56, 149, 200, 0.05); border: 1px solid rgba(56, 149, 200, 0.2);
      border-radius: 12px; color: var(--color-text); font-weight: bold; cursor: pointer; display: flex; align-items: center; gap: 10px; transition: 0.3s;
    }
    .shortcut-btn:hover { background: rgba(56, 149, 200, 0.15); border-color: #3895c8; }
    .shortcut-btn i { color: #3895c8; font-size: 1.2rem; }
    
    /* Schedule Timeline */
    .timeline { position: relative; padding-left: 30px; }
    .timeline::before { content: ''; position: absolute; left: 7px; top: 0; bottom: 0; width: 2px; background: var(--color-border); }
    .timeline-item { position: relative; margin-bottom: 20px; }
    .timeline-item::before {
      content: ''; position: absolute; left: -28.5px; top: 5px; width: 12px; height: 12px;
      border-radius: 50%; background: var(--color-primary); border: 2px solid var(--color-surface);
    }
    .timeline-time { font-size: 0.85rem; color: var(--color-primary); font-weight: bold; margin-bottom: 5px; }
    .timeline-content { background: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border: 1px solid var(--color-border); }
    .timeline-content h4 { margin: 0 0 5px; font-size: 1.1rem; }
    .timeline-content p { margin: 0; font-size: 0.9rem; color: var(--color-text-light); }
    
    /* Tables */
    .table-container { overflow-x: auto; }
    .table { width: 100%; border-collapse: collapse; min-width: 700px; }
    .table th, .table td { padding: 12px 15px; text-align: left; border-bottom: 1px solid var(--color-border); font-size: 0.95rem; }
    .table th { color: var(--color-text-light); font-weight: 600; }
    .table tr:hover td { background: rgba(255,255,255,0.02); }
    .status-badge { padding: 5px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
    .status-success { background: rgba(46, 204, 113, 0.1); color: #2ecc71; }
    .status-pending { background: rgba(241, 196, 15, 0.1); color: #f1c40f; }
    
    .action-btn { background: none; border: none; color: #3895c8; cursor: pointer; padding: 5px; font-size: 1rem; margin-right: 5px; }
    .action-btn:hover { color: var(--color-primary); }

    /* Forms & Filters */
    .filter-bar { display: flex; gap: 15px; margin-bottom: 20px; align-items: center; }
    .filter-select { padding: 8px 15px; background: rgba(0,0,0,0.2); border: 1px solid var(--color-border); color: var(--color-text); border-radius: 8px; outline: none; }
    .btn-primary { padding: 10px 20px; background: var(--color-primary); border: none; color: white; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.3s; }
    .btn-primary:hover { background: #b83a62; }
    
    /* Slot Calendar */
    .slot-grid { display: grid; grid-template-columns: 80px 1fr; gap: 15px; margin-bottom: 15px; }
    .slot-time { font-weight: bold; color: var(--color-text-light); padding-top: 15px; text-align: right; }
    .slot-card { background: rgba(56, 149, 200, 0.05); border: 1px solid rgba(56, 149, 200, 0.2); padding: 15px; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; }
    .slot-card.empty { background: rgba(255,255,255,0.02); border: 1px dashed var(--color-border); color: var(--color-text-light); justify-content: center; cursor: pointer; }
    .slot-card.empty:hover { border-color: var(--color-primary); color: var(--color-primary); }
    
    /* Modal */
    .modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.8); backdrop-filter: blur(5px); z-index: 100; align-items: center; justify-content: center; }
    .modal.active { display: flex; }
    .modal-content { background: var(--color-surface); width: 100%; max-width: 500px; padding: 30px; border-radius: 16px; border: 1px solid var(--color-border); position: relative; }
    .close-modal { position: absolute; top: 15px; right: 15px; background: none; border: none; color: var(--color-text); font-size: 1.5rem; cursor: pointer; }
    .form-group { margin-bottom: 15px; }
    .form-group label { display: block; margin-bottom: 5px; color: var(--color-text-light); font-size: 0.9rem; }
    .form-control { width: 100%; padding: 10px 15px; background: rgba(0,0,0,0.2); border: 1px solid var(--color-border); border-radius: 8px; color: white; box-sizing: border-box; }

    /* RTL Support */
    [dir="rtl"] .admin-sidebar { border-right: none; border-left: 1px solid var(--color-border); }
    [dir="rtl"] .table th, [dir="rtl"] .table td { text-align: right; }
    [dir="rtl"] .timeline { padding-left: 0; padding-right: 30px; }
    [dir="rtl"] .timeline::before { left: auto; right: 7px; }
    [dir="rtl"] .timeline-item::before { left: auto; right: -28.5px; }
    
    /* Tab Logic */
    .tab-content { display: none; }
    .tab-content.active { display: block; animation: fadeIn 0.4s ease; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    
    @media (max-width: 768px) {
      body { flex-direction: column; overflow: auto; }
      .admin-sidebar { width: 100%; height: auto; border-right: none; border-bottom: 1px solid var(--color-border); }
      .admin-content { padding: 20px; }
      .shortcuts-grid { grid-template-columns: 1fr; }
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
      <div class="admin-nav-item" onclick="switchTab('slots', this)">
        <i class="fa-solid fa-clock"></i> Slot & Calendar
      </div>
      <div class="admin-nav-item" onclick="switchTab('analytics', this)">
        <i class="fa-solid fa-chart-pie"></i> Analytics
      </div>
      <div class="admin-nav-item" onclick="switchTab('administration', this)">
        <i class="fa-solid fa-user-shield"></i> Administration
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
          <div class="stat-icon" style="background: rgba(210, 75, 118, 0.1); color: var(--color-primary);"><i class="fa-solid fa-calendar-day"></i></div>
          <div class="stat-info">
            <h3>Events Today</h3>
            <p>4</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(56, 149, 200, 0.1); color: #3895c8;"><i class="fa-solid fa-calendar-check"></i></div>
          <div class="stat-info">
            <h3>Total Bookings</h3>
            <p>1,284</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(46, 204, 113, 0.1); color: #2ecc71;"><i class="fa-solid fa-dollar-sign"></i></div>
          <div class="stat-info">
            <h3>Revenue</h3>
            <p>$45,200</p>
          </div>
        </div>
      </div>
      
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 25px;">
        <div>
          <div class="content-panel">
            <div class="panel-header">
              <h3>Today's Schedule</h3>
              <button class="btn-primary" onclick="openModal()"><i class="fa-solid fa-plus"></i> Slot It</button>
            </div>
            <div class="timeline">
              <div class="timeline-item">
                <div class="timeline-time">10:00 AM</div>
                <div class="timeline-content">
                  <h4>Superhero Birthday Party</h4>
                  <p>Client: Sarah Jenkins | Entertainer: Max The Hero</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-time">01:30 PM</div>
                <div class="timeline-content">
                  <h4>Corporate Magic Show</h4>
                  <p>Client: TechCorp Inc. | Entertainer: The Great Houdini</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-time">04:00 PM</div>
                <div class="timeline-content">
                  <h4>Princess Tea Party</h4>
                  <p>Client: Emily Davis | Entertainer: Princess Aurora</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-time">07:00 PM</div>
                <div class="timeline-content">
                  <h4>Wedding Reception DJ</h4>
                  <p>Client: John & Mary | Entertainer: DJ Sparkles</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div>
          <div class="content-panel">
            <div class="panel-header">
              <h3>Quick Operational</h3>
            </div>
            <div style="display: flex; flex-direction: column; gap: 15px;">
              <button class="shortcut-btn"><i class="fa-solid fa-file-invoice-dollar"></i> Invoice Log</button>
              <button class="shortcut-btn"><i class="fa-solid fa-user-plus"></i> Client Leads</button>
              <button class="shortcut-btn"><i class="fa-solid fa-calendar-plus"></i> Quick Booking</button>
              <button class="shortcut-btn"><i class="fa-solid fa-comments"></i> Messages (3 New)</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- BOOKINGS TAB -->
    <div id="bookings" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem;">Manage Bookings</h3>
          <button class="btn-primary" onclick="openModal()"><i class="fa-solid fa-plus"></i> Add New Booking</button>
        </div>
        
        <div class="filter-bar">
          <span style="color: var(--color-text-light);">Filter:</span>
          <select class="filter-select" id="bookingFilter" onchange="filterBookings()">
            <option value="all">All Bookings</option>
            <option value="confirmed">Confirmed</option>
            <option value="pending">Pending</option>
          </select>
        </div>
        
        <div class="table-container">
          <table class="table" id="bookingsTable">
            <thead>
              <tr>
                <th>Booking ID</th>
                <th>Client Name</th>
                <th>Event Type</th>
                <th>Date</th>
                <th>Amount</th>
                <th>Paid</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="bookingsBody">
              <tr data-status="confirmed">
                <td>#BKG-8402</td>
                <td>Sarah Jenkins</td>
                <td>Kids Birthday</td>
                <td>Oct 15, 2026</td>
                <td>$450</td>
                <td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td>
                <td><span class="status-badge status-success">Confirmed</span></td>
                <td>
                  <button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button>
                  <button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button>
                </td>
              </tr>
              <tr data-status="pending">
                <td>#BKG-8403</td>
                <td>Michael Vance</td>
                <td>Corporate Gala</td>
                <td>Oct 18, 2026</td>
                <td>$2,100</td>
                <td><i class="fa-solid fa-xmark" style="color: var(--color-primary);"></i> No</td>
                <td><span class="status-badge status-pending">Pending</span></td>
                <td>
                  <button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button>
                  <button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button>
                </td>
              </tr>
              <tr data-status="confirmed">
                <td>#BKG-8404</td>
                <td>Emily Davis</td>
                <td>Wedding Reception</td>
                <td>Oct 20, 2026</td>
                <td>$800</td>
                <td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td>
                <td><span class="status-badge status-success">Confirmed</span></td>
                <td>
                  <button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button>
                  <button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- SLOT & CALENDAR TAB -->
    <div id="slots" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem;">Daily Slots</h3>
          <input type="date" class="filter-select" value="2026-10-02">
        </div>
        
        <div class="slot-grid">
          <div class="slot-time">09:00 AM</div>
          <div class="slot-card empty" onclick="openModal()">
            <i class="fa-solid fa-plus"></i> Add Booking to Slot
          </div>
          
          <div class="slot-time">10:00 AM</div>
          <div class="slot-card" style="border-left: 4px solid var(--color-primary);">
            <div>
              <h4 style="margin: 0 0 5px;">Superhero Birthday Party</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light);">Lead: Max The Hero</div>
            </div>
            <span class="status-badge status-success">Booked</span>
          </div>
          
          <div class="slot-time">11:30 AM</div>
          <div class="slot-card empty" onclick="openModal()">
            <i class="fa-solid fa-plus"></i> Add Booking to Slot
          </div>
          
          <div class="slot-time">01:30 PM</div>
          <div class="slot-card" style="border-left: 4px solid #3895c8;">
            <div>
              <h4 style="margin: 0 0 5px;">Corporate Magic Show</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light);">Lead: The Great Houdini</div>
            </div>
            <span class="status-badge status-success">Booked</span>
          </div>
          
          <div class="slot-time">04:00 PM</div>
          <div class="slot-card" style="border-left: 4px solid #f1c40f;">
            <div>
              <h4 style="margin: 0 0 5px;">Princess Tea Party</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light);">Lead: Princess Aurora</div>
            </div>
            <span class="status-badge status-success">Booked</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ANALYTICS TAB -->
    <div id="analytics" class="tab-content">
      <div class="content-panel">
        <h3 style="font-size: 2rem; margin-bottom: 20px; font-family: var(--font-heading);">Performance Analytics</h3>
        
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 20px;">
          <div style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 12px; border: 1px solid var(--color-border);">
            <h4 style="margin-top: 0; color: var(--color-text-light);">Monthly Revenue Trend</h4>
            <canvas id="revenueChart" height="200"></canvas>
          </div>
          <div style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 12px; border: 1px solid var(--color-border);">
            <h4 style="margin-top: 0; color: var(--color-text-light);">Bookings by Event Type</h4>
            <canvas id="typeChart" height="200"></canvas>
          </div>
        </div>
      </div>
    </div>

    <!-- ADMINISTRATION TAB -->
    <div id="administration" class="tab-content">
      <div class="stats-grid">
        <div class="stat-card" style="cursor: pointer; background: rgba(56, 149, 200, 0.1); border-color: #3895c8;">
          <div class="stat-icon" style="color: #3895c8;"><i class="fa-solid fa-file-pdf"></i></div>
          <div class="stat-info">
            <h3>Generate Reports</h3>
            <p style="font-size: 1rem; font-weight: normal; margin-top: 5px;">Tax, Revenue, Payroll</p>
          </div>
        </div>
        <div class="stat-card" style="cursor: pointer; background: rgba(210, 75, 118, 0.1); border-color: var(--color-primary);">
          <div class="stat-icon" style="color: var(--color-primary);"><i class="fa-solid fa-user-shield"></i></div>
          <div class="stat-info">
            <h3>Staff & Permissions</h3>
            <p style="font-size: 1rem; font-weight: normal; margin-top: 5px;">Manage roles</p>
          </div>
        </div>
      </div>
      
      <div class="content-panel">
        <div class="panel-header">
          <h3>Staff Directory</h3>
          <button class="btn-primary"><i class="fa-solid fa-user-plus"></i> Add Staff</button>
        </div>
        <div class="table-container">
          <table class="table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Role</th>
                <th>Department</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Mark V.</td>
                <td>Super Admin</td>
                <td>Management</td>
                <td><span class="status-badge status-success">Active</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr>
                <td>Alice G.</td>
                <td>Event Coordinator</td>
                <td>Planning</td>
                <td><span class="status-badge status-success">Active</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr>
                <td>Tom H.</td>
                <td>Entertainer (Lead)</td>
                <td>Performance</td>
                <td><span class="status-badge status-success">Active</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    
    <!-- SETTINGS TAB -->
    <div id="settings" class="tab-content">
      <div class="content-panel">
        <h3 style="font-size: 2rem; margin-top:0;">Platform Settings</h3>
        <p style="color: var(--color-text-light);">Configure global settings, payment gateways, and email templates.</p>
        <div style="height: 300px; display: flex; align-items: center; justify-content: center; border: 2px dashed var(--color-border); border-radius: 12px; margin-top: 20px; color: var(--color-text-light);">
          Global Configuration Form
        </div>
      </div>
    </div>

  </div>

  <!-- Booking Modal -->
  <div class="modal" id="bookingModal">
    <div class="modal-content">
      <button class="close-modal" onclick="closeModal()"><i class="fa-solid fa-xmark"></i></button>
      <h2 style="margin-top: 0; font-family: var(--font-heading); color: var(--color-primary);">Add New Booking</h2>
      
      <form id="newBookingForm" onsubmit="event.preventDefault(); submitBooking();">
        <div class="form-group">
          <label>Client Name</label>
          <input type="text" class="form-control" id="clientName" required>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
          <div class="form-group">
            <label>Event Type</label>
            <select class="form-control" id="eventType" required>
              <option value="Kids Birthday">Kids Birthday</option>
              <option value="Corporate Gala">Corporate Gala</option>
              <option value="Magic Show">Magic Show</option>
            </select>
          </div>
          <div class="form-group">
            <label>Date</label>
            <input type="date" class="form-control" id="eventDate" required>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
          <div class="form-group">
            <label>Amount ($)</label>
            <input type="number" class="form-control" id="eventAmount" required>
          </div>
          <div class="form-group">
            <label>Paid Status</label>
            <select class="form-control" id="eventPaid">
              <option value="Yes">Yes</option>
              <option value="No">No</option>
            </select>
          </div>
        </div>
        <button type="submit" class="btn-primary" style="width: 100%; margin-top: 10px;">Create Booking</button>
      </form>
    </div>
  </div>

  <script src="js/theme.js"></script>
  <script>
    // Tab Switching
    function switchTab(tabId, element) {
      document.querySelectorAll('.admin-nav-item').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
      
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      
      document.querySelector('.dashboard-title').textContent = element.textContent.trim();
      
      // Render charts if analytics is clicked and not yet rendered
      if (tabId === 'analytics' && !window.chartsRendered) {
        renderCharts();
        window.chartsRendered = true;
      }
    }

    // Modal Logic
    function openModal() { document.getElementById('bookingModal').classList.add('active'); }
    function closeModal() { document.getElementById('bookingModal').classList.remove('active'); document.getElementById('newBookingForm').reset(); }

    function submitBooking() {
      const client = document.getElementById('clientName').value;
      const type = document.getElementById('eventType').value;
      const dateRaw = document.getElementById('eventDate').value;
      const amount = document.getElementById('eventAmount').value;
      const paid = document.getElementById('eventPaid').value;
      
      const dateObj = new Date(dateRaw);
      const dateStr = dateObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
      
      const paidHtml = paid === 'Yes' ? '<i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes' : '<i class="fa-solid fa-xmark" style="color: var(--color-primary);"></i> No';
      
      const newRow = `
        <tr data-status="pending">
          <td>#BKG-${Math.floor(Math.random() * 1000) + 8500}</td>
          <td>${client}</td>
          <td>${type}</td>
          <td>${dateStr}</td>
          <td>$${amount}</td>
          <td>${paidHtml}</td>
          <td><span class="status-badge status-pending">Pending</span></td>
          <td>
            <button class="action-btn"><i class="fa-solid fa-eye"></i></button>
            <button class="action-btn"><i class="fa-solid fa-pen"></i></button>
          </td>
        </tr>
      `;
      
      document.getElementById('bookingsBody').insertAdjacentHTML('afterbegin', newRow);
      closeModal();
      
      // Switch to bookings tab to see the result
      const bookingsNav = document.querySelector('.admin-nav-item:nth-child(2)');
      switchTab('bookings', bookingsNav);
    }

    // Filter Logic
    function filterBookings() {
      const filter = document.getElementById('bookingFilter').value;
      const rows = document.querySelectorAll('#bookingsBody tr');
      
      rows.forEach(row => {
        if (filter === 'all' || row.dataset.status === filter) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    }

    // Analytics Charts using Chart.js
    function renderCharts() {
      const ctxRev = document.getElementById('revenueChart').getContext('2d');
      new Chart(ctxRev, {
        type: 'line',
        data: {
          labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
          datasets: [{
            label: 'Revenue ($)',
            data: [22000, 28000, 31000, 36000, 42000, 45200],
            borderColor: '#D24B76',
            backgroundColor: 'rgba(210, 75, 118, 0.2)',
            borderWidth: 2,
            fill: true,
            tension: 0.4
          }]
        },
        options: {
          responsive: true,
          plugins: { legend: { display: false } },
          scales: {
            y: { grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: 'rgba(255,255,255,0.6)' } },
            x: { grid: { display: false }, ticks: { color: 'rgba(255,255,255,0.6)' } }
          }
        }
      });

      const ctxType = document.getElementById('typeChart').getContext('2d');
      new Chart(ctxType, {
        type: 'doughnut',
        data: {
          labels: ['Kids Birthday', 'Corporate', 'Weddings', 'Shows'],
          datasets: [{
            data: [45, 25, 20, 10],
            backgroundColor: ['#D24B76', '#3895c8', '#f1c40f', '#2ecc71'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { position: 'right', labels: { color: 'rgba(255,255,255,0.8)' } }
          }
        }
      });
    }
  </script>
</body>
</html>
"""

with open(r'c:\Users\vigas\Desktop\magiqo\admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
