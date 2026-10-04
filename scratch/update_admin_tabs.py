import re

filepath = r'c:\Users\vigas\Desktop\magiqo\admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

overview_pattern = r'<!-- OVERVIEW TAB -->.*?<!-- BOOKINGS TAB -->'
new_overview = """<!-- OVERVIEW TAB -->
    <div id="overview" class="tab-content active">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
        <h2 style="margin: 0; font-family: var(--font-magic); font-size: 2.5rem; color: var(--color-primary);">Welcome to Magiqo!</h2>
        <button class="btn-primary" style="background: #3895c8;"><i class="fa-solid fa-file-pdf"></i> Export Daily Briefings</button>
      </div>
      
      <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));">
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(46, 204, 113, 0.1); color: #2ecc71;"><i class="fa-solid fa-dollar-sign"></i></div>
          <div class="stat-info">
            <h3>Total Revenue</h3>
            <p>$45,200 <span style="font-size: 0.8rem; color: #2ecc71;">+12%</span></p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(56, 149, 200, 0.1); color: #3895c8;"><i class="fa-solid fa-calendar-check"></i></div>
          <div class="stat-info">
            <h3>Active Bookings</h3>
            <p>156 <span style="font-size: 0.8rem; color: #3895c8;">+5%</span></p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(241, 196, 15, 0.1); color: #f1c40f;"><i class="fa-solid fa-star"></i></div>
          <div class="stat-info">
            <h3>Avg. Rating</h3>
            <p>4.8</p>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(210, 75, 118, 0.1); color: var(--color-primary);"><i class="fa-solid fa-bell"></i></div>
          <div class="stat-info">
            <h3>Pending Actions</h3>
            <p>14</p>
          </div>
        </div>
      </div>
      
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px;">
        <div>
          <div class="content-panel">
            <div class="panel-header">
              <h3>Today's Live Schedule</h3>
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="switchTab('administration', document.querySelectorAll('.admin-nav-item')[4])"><i class="fa-solid fa-users"></i> Staff Roster</button>
            </div>
            <div class="timeline">
              <div class="timeline-item">
                <div class="timeline-time">10:00 AM</div>
                <div class="timeline-content">
                  <h4>Superhero Birthday Party</h4>
                  <p>Client: Sarah Jenkins</p>
                  <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.85rem;">
                    <strong>Staff:</strong> Max The Hero <span class="status-badge status-success" style="margin-left: 5px; font-size: 0.7rem; padding: 2px 8px;">On Duty</span>
                  </div>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-time">01:30 PM</div>
                <div class="timeline-content">
                  <h4>Corporate Magic Show</h4>
                  <p>Client: TechCorp Inc.</p>
                  <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.85rem;">
                    <strong>Staff:</strong> The Great Houdini <span class="status-badge status-pending" style="margin-left: 5px; font-size: 0.7rem; padding: 2px 8px;">En Route</span>
                  </div>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-time">04:00 PM</div>
                <div class="timeline-content">
                  <h4>Princess Tea Party</h4>
                  <p>Client: Emily Davis</p>
                  <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.85rem;">
                    <strong>Staff:</strong> Princess Aurora <span style="margin-left: 5px; color: var(--color-text-light);">Standby</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div>
          <div class="content-panel">
            <div class="panel-header">
              <h3>Recent Booking Activities</h3>
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="switchTab('bookings', document.querySelectorAll('.admin-nav-item')[1])">View All Bookings</button>
            </div>
            <div style="display: flex; flex-direction: column; gap: 15px;">
              <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border: 1px solid var(--color-border); display: flex; align-items: center; gap: 15px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(46, 204, 113, 0.1); color: #2ecc71; display: flex; align-items: center; justify-content: center;"><i class="fa-solid fa-check"></i></div>
                <div>
                  <h4 style="margin: 0; font-size: 1rem;">Booking Confirmed</h4>
                  <p style="margin: 5px 0 0; font-size: 0.85rem; color: var(--color-text-light);">Emily Davis paid $800 for Wedding Reception.</p>
                </div>
              </div>
              <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border: 1px solid var(--color-border); display: flex; align-items: center; gap: 15px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(241, 196, 15, 0.1); color: #f1c40f; display: flex; align-items: center; justify-content: center;"><i class="fa-solid fa-spinner"></i></div>
                <div>
                  <h4 style="margin: 0; font-size: 1rem;">New Booking Pending</h4>
                  <p style="margin: 5px 0 0; font-size: 0.85rem; color: var(--color-text-light);">Michael Vance requested a Corporate Gala ($2,100).</p>
                </div>
              </div>
              <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border: 1px solid var(--color-border); display: flex; align-items: center; gap: 15px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(56, 149, 200, 0.1); color: #3895c8; display: flex; align-items: center; justify-content: center;"><i class="fa-solid fa-message"></i></div>
                <div>
                  <h4 style="margin: 0; font-size: 1rem;">Client Message</h4>
                  <p style="margin: 5px 0 0; font-size: 0.85rem; color: var(--color-text-light);">John Smith sent a message regarding his Magic Show.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- BOOKINGS TAB -->"""

content = re.sub(overview_pattern, new_overview, content, flags=re.DOTALL)

bookings_pattern = r'<!-- BOOKINGS TAB -->.*?<!-- SLOT & CALENDAR TAB -->'
new_bookings = """<!-- BOOKINGS TAB -->
    <div id="bookings" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0;">Manage Bookings</h3>
          <button class="btn-primary" onclick="openModal()"><i class="fa-solid fa-plus"></i> Add New Booking</button>
        </div>
        
        <div class="filter-bar">
          <span style="color: var(--color-text-light);">Filter:</span>
          <select class="filter-select" id="bookingFilter" onchange="filterBookings()">
            <option value="all">All Bookings</option>
            <option value="confirmed">Confirmed</option>
            <option value="pending">Pending</option>
            <option value="completed">Completed</option>
            <option value="cancelled">Cancelled</option>
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
              <tr data-status="pending">
                <td>#BKG-8410</td><td>Jason Bourne</td><td>Magic Show</td><td>Nov 02, 2026</td><td>$350</td><td><i class="fa-solid fa-xmark" style="color: var(--color-primary);"></i> No</td><td><span class="status-badge status-pending">Pending</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="confirmed">
                <td>#BKG-8409</td><td>Alice Wonderland</td><td>Princess Tea Party</td><td>Oct 31, 2026</td><td>$600</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge status-success">Confirmed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="cancelled">
                <td>#BKG-8408</td><td>Bruce Wayne</td><td>Corporate Gala</td><td>Oct 28, 2026</td><td>$5,000</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge" style="background: rgba(210, 75, 118, 0.1); color: var(--color-primary);">Cancelled</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="completed">
                <td>#BKG-8407</td><td>Clark Kent</td><td>Kids Birthday</td><td>Oct 20, 2026</td><td>$400</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge" style="background: rgba(56, 149, 200, 0.1); color: #3895c8;">Completed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="confirmed">
                <td>#BKG-8406</td><td>Peter Parker</td><td>Superhero Party</td><td>Oct 19, 2026</td><td>$500</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge status-success">Confirmed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="completed">
                <td>#BKG-8405</td><td>Tony Stark</td><td>Corporate Gala</td><td>Oct 15, 2026</td><td>$3,500</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge" style="background: rgba(56, 149, 200, 0.1); color: #3895c8;">Completed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="confirmed">
                <td>#BKG-8404</td><td>Emily Davis</td><td>Wedding Reception</td><td>Oct 14, 2026</td><td>$800</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge status-success">Confirmed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="pending">
                <td>#BKG-8403</td><td>Michael Vance</td><td>Corporate Gala</td><td>Oct 13, 2026</td><td>$2,100</td><td><i class="fa-solid fa-xmark" style="color: var(--color-primary);"></i> No</td><td><span class="status-badge status-pending">Pending</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="confirmed">
                <td>#BKG-8402</td><td>Sarah Jenkins</td><td>Kids Birthday</td><td>Oct 10, 2026</td><td>$450</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge status-success">Confirmed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
              <tr data-status="completed">
                <td>#BKG-8401</td><td>John Doe</td><td>Magic Show</td><td>Oct 05, 2026</td><td>$300</td><td><i class="fa-solid fa-check" style="color: #2ecc71;"></i> Yes</td><td><span class="status-badge" style="background: rgba(56, 149, 200, 0.1); color: #3895c8;">Completed</span></td><td><button class="action-btn" title="View"><i class="fa-solid fa-eye"></i></button><button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- SLOT & CALENDAR TAB -->"""

content = re.sub(bookings_pattern, new_bookings, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
