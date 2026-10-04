import re

filepath = r'c:\Users\vigas\Desktop\magiqo\admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Venues and Transactions to sidebar
sidebar_search = r'(<div class="admin-nav-item" onclick="switchTab\(\'enquiries\', this\)">\s*<i class="fa-solid fa-envelope-open-text"></i> Enquiries\s*</div>)'
sidebar_replace = r'''\1
      <div class="admin-nav-item" onclick="switchTab('venues', this)">
        <i class="fa-solid fa-map-location-dot"></i> Venues & Logistics
      </div>
      <div class="admin-nav-item" onclick="switchTab('transactions', this)">
        <i class="fa-solid fa-credit-card"></i> Transactions
      </div>'''
content = re.sub(sidebar_search, sidebar_replace, content)

# 2. Add Venues and Transactions tab content
tabs_to_add = """
    <!-- VENUES TAB -->
    <div id="venues" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0;">Venues & Logistics</h3>
          <button class="btn-primary"><i class="fa-solid fa-plus"></i> Add Logistics Order</button>
        </div>
        <p style="color: var(--color-text-light); margin-bottom: 25px;">Manage venue locations and logistical requirements for upcoming bookings.</p>
        
        <div class="stats-grid">
          <div class="stat-card" style="border-left: 4px solid var(--color-primary);">
            <div>
              <h4 style="margin: 0 0 5px; color: var(--color-primary);">Grand Plaza Hotel</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 10px;">Booking #BKG-8404 | Event: Wedding Reception</div>
              <p style="margin: 0; font-size: 0.9rem;"><strong>Logistics:</strong> Sound system, LED lighting, Smoke machine, DJ Booth setup.</p>
            </div>
            <div style="text-align: right; min-width: 80px;">
              <span class="status-badge status-pending">Pending</span>
            </div>
          </div>
          
          <div class="stat-card" style="border-left: 4px solid #3895c8;">
            <div>
              <h4 style="margin: 0 0 5px; color: #3895c8;">Community Hall A</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 10px;">Booking #BKG-8402 | Event: Kids Birthday</div>
              <p style="margin: 0; font-size: 0.9rem;"><strong>Logistics:</strong> Balloon arch, Magic props box, Face painting kit.</p>
            </div>
            <div style="text-align: right; min-width: 80px;">
              <span class="status-badge status-success">Ready</span>
            </div>
          </div>
          
          <div class="stat-card" style="border-left: 4px solid #f1c40f;">
            <div>
              <h4 style="margin: 0 0 5px; color: #f1c40f;">City Convention Center</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 10px;">Booking #BKG-8403 | Event: Corporate Gala</div>
              <p style="margin: 0; font-size: 0.9rem;"><strong>Logistics:</strong> Stage backdrop, Illusionist rig, Audio setup, Seating for 200.</p>
            </div>
            <div style="text-align: right; min-width: 80px;">
              <span class="status-badge status-pending">In Transit</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TRANSACTIONS TAB -->
    <div id="transactions" class="tab-content">
      <div class="content-panel">
        <div class="panel-header">
          <h3 style="font-size: 2rem; margin: 0;">Recent Transactions</h3>
          <button class="btn-primary" style="background: transparent; border: 1px solid var(--color-border); color: var(--color-text);"><i class="fa-solid fa-download"></i> Export CSV</button>
        </div>
        
        <div class="table-container">
          <table class="table">
            <thead>
              <tr>
                <th>Transaction ID</th>
                <th>Client Name</th>
                <th>Date</th>
                <th>Amount</th>
                <th>Payment Method</th>
                <th>Status</th>
                <th>Invoice</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>#TRX-99821</td>
                <td>Emily Davis</td>
                <td>Oct 02, 2026</td>
                <td>$800.00</td>
                <td>Credit Card (...4242)</td>
                <td><span class="status-badge status-success">Completed</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-file-invoice"></i></button></td>
              </tr>
              <tr>
                <td>#TRX-99820</td>
                <td>Sarah Jenkins</td>
                <td>Oct 01, 2026</td>
                <td>$450.00</td>
                <td>PayPal</td>
                <td><span class="status-badge status-success">Completed</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-file-invoice"></i></button></td>
              </tr>
              <tr>
                <td>#TRX-99819</td>
                <td>Michael Vance</td>
                <td>Sep 29, 2026</td>
                <td>$500.00</td>
                <td>Bank Transfer</td>
                <td><span class="status-badge status-pending">Processing</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-file-invoice"></i></button></td>
              </tr>
              <tr>
                <td>#TRX-99818</td>
                <td>Tony Stark</td>
                <td>Sep 28, 2026</td>
                <td>$3,500.00</td>
                <td>Credit Card (...1234)</td>
                <td><span class="status-badge status-success">Completed</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-file-invoice"></i></button></td>
              </tr>
              <tr>
                <td>#TRX-99817</td>
                <td>Bruce Wayne</td>
                <td>Sep 25, 2026</td>
                <td>$1,000.00</td>
                <td>Credit Card (...9876)</td>
                <td><span class="status-badge" style="background: rgba(210, 75, 118, 0.1); color: var(--color-primary);">Refunded</span></td>
                <td><button class="action-btn"><i class="fa-solid fa-file-invoice"></i></button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
"""

content = content.replace('<!-- SETTINGS TAB -->', tabs_to_add + '\n    <!-- SETTINGS TAB -->')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
