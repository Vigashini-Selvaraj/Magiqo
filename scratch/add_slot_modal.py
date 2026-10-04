import re

filepath = r'c:\Users\vigas\Desktop\magiqo\admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the "Add Slot" button in the panel header to call openSlotModal
content = content.replace(
    '<button class="btn-primary" onclick="openModal()"><i class="fa-solid fa-plus"></i> Add Slot</button>',
    '<button class="btn-primary" onclick="openSlotModal()"><i class="fa-solid fa-plus"></i> Add Slot</button>'
)

# 2. Update the empty slot cards to call openSlotModal
content = content.replace(
    '<div class="slot-card empty" onclick="openModal()">',
    '<div class="slot-card empty" onclick="openSlotModal()">'
)

# 3. Add the slotModal HTML right after the bookingModal
slot_modal_html = """
  <!-- Slot Modal -->
  <div class="modal" id="slotModal">
    <div class="modal-content">
      <button class="close-modal" onclick="closeSlotModal()"><i class="fa-solid fa-xmark"></i></button>
      <h2 style="margin-top: 0; font-family: var(--font-heading); color: var(--color-primary);">Add New Slot</h2>
      
      <form id="newSlotForm" onsubmit="event.preventDefault(); submitSlot();">
        <div class="form-group">
          <label>Client Name</label>
          <input type="text" class="form-control" id="slotClientName" required>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
          <div class="form-group">
            <label>Event Type</label>
            <select class="form-control" id="slotEventType" required>
              <option value="Kids Birthday">Kids Birthday</option>
              <option value="Corporate Gala">Corporate Gala</option>
              <option value="Magic Show">Magic Show</option>
              <option value="Wedding Reception">Wedding Reception</option>
            </select>
          </div>
          <div class="form-group">
            <label>Date</label>
            <input type="date" class="form-control" id="slotDate" required>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
          <div class="form-group">
            <label>Amount ($)</label>
            <input type="number" class="form-control" id="slotAmount" required>
          </div>
          <div class="form-group">
            <label>Paid Status</label>
            <select class="form-control" id="slotPaid">
              <option value="Yes">Yes</option>
              <option value="No">No</option>
            </select>
          </div>
          <div class="form-group">
            <label>Timing</label>
            <input type="time" class="form-control" id="slotTime" required>
          </div>
        </div>
        <button type="submit" class="btn-primary" style="width: 100%; margin-top: 10px;">Add Slot</button>
      </form>
    </div>
  </div>
"""

content = content.replace('<!-- Booking Modal -->', slot_modal_html + '\n  <!-- Booking Modal -->')

# 4. Add the JS functions for slot modal
js_addition = """
    function openSlotModal() { document.getElementById('slotModal').classList.add('active'); }
    function closeSlotModal() { document.getElementById('slotModal').classList.remove('active'); document.getElementById('newSlotForm').reset(); }

    function submitSlot() {
      const client = document.getElementById('slotClientName').value;
      const type = document.getElementById('slotEventType').value;
      const dateRaw = document.getElementById('slotDate').value;
      const timeRaw = document.getElementById('slotTime').value;
      
      const dateObj = new Date(dateRaw);
      const dateStr = dateObj.toLocaleDateString('en-US', { month: 'short', day: '2-digit' });
      
      // Parse time
      let [hours, minutes] = timeRaw.split(':');
      let ampm = hours >= 12 ? 'PM' : 'AM';
      hours = hours % 12;
      hours = hours ? hours : 12; // the hour '0' should be '12'
      let timeStr = hours.toString().padStart(2, '0') + ':' + minutes + ' ' + ampm;
      
      const newSlot = `
          <div class="slot-time" style="line-height:1.2;">${dateStr}<br><span style="font-size:0.75rem;font-weight:normal;">${timeStr}</span></div>
          <div class="slot-card" style="border-left: 4px solid var(--color-primary); animation: fadeIn 0.5s;">
            <div>
              <h4 style="margin: 0 0 5px;">${type}</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light);">Lead: Unassigned | Client: ${client}</div>
            </div>
            <span class="status-badge status-success">Booked</span>
          </div>
      `;
      
      // Append to the Upcoming Future Slots grid (the second grid in the slots tab)
      const grids = document.querySelectorAll('.slot-grid');
      if (grids.length > 1) {
        grids[1].insertAdjacentHTML('beforeend', newSlot);
      }
      
      closeSlotModal();
    }
"""

content = content.replace('function filterBookings() {', js_addition + '\n    function filterBookings() {')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
