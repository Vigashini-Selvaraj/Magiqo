import re

filepath = r'c:\Users\vigas\Desktop\magiqo\admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add "Enquiries" to sidebar
sidebar_search = r'(<div class="admin-nav-item" onclick="switchTab\(\'administration\', this\)">\s*<i class="fa-solid fa-user-shield"></i> Administration\s*</div>)'
sidebar_replace = r'''\1
      <div class="admin-nav-item" onclick="switchTab('enquiries', this)">
        <i class="fa-solid fa-envelope-open-text"></i> Enquiries
      </div>'''
content = re.sub(sidebar_search, sidebar_replace, content)

# 2. Update Add Staff button
content = content.replace(
    '<button class="btn-primary"><i class="fa-solid fa-user-plus"></i> Add Staff</button>',
    '<button class="btn-primary" onclick="openStaffModal()"><i class="fa-solid fa-user-plus"></i> Add Staff</button>'
)

# 3. Add Enquiries Tab Content just before <!-- SETTINGS TAB -->
enquiries_tab = """
    <!-- ENQUIRIES TAB -->
    <div id="enquiries" class="tab-content">
      <div class="content-panel">
        <h3 style="font-size: 2rem; margin: 0 0 20px 0;">Client Enquiries</h3>
        <p style="color: var(--color-text-light); margin-bottom: 25px;">Respond to potential leads, resolve questions, or convert them into bookings.</p>
        
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <!-- Enquiry 1 -->
          <div class="enquiry-card" id="enq-1" style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
              <div>
                <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Jessica Thompson</h4>
                <div style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 15px;">Email: jessica@example.com | Date: Today, 10:45 AM</div>
                <p style="margin: 0; font-size: 0.95rem; line-height: 1.5;">"Hi Magiqo! We are planning a large corporate event for next month and we were wondering if you offer customized packages that include both a Magic Show and a DJ. Please let me know!"</p>
              </div>
              <span class="status-badge status-pending" id="badge-enq-1">Open</span>
            </div>
            <div style="margin-top: 20px; display: flex; gap: 10px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px;">
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="openReplyModal('enq-1')"><i class="fa-solid fa-reply"></i> Reply</button>
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem; background: #2ecc71;" onclick="openModal()"><i class="fa-solid fa-calendar-check"></i> Convert to Booking</button>
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem; background: rgba(0,0,0,0.5); border: 1px solid var(--color-border);" onclick="resolveEnquiry('enq-1')"><i class="fa-solid fa-check"></i> Resolve</button>
            </div>
          </div>
          
          <!-- Enquiry 2 -->
          <div class="enquiry-card" id="enq-2" style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
              <div>
                <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">David Lee</h4>
                <div style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 15px;">Email: david@example.com | Date: Yesterday, 4:20 PM</div>
                <p style="margin: 0; font-size: 0.95rem; line-height: 1.5;">"My son's 7th birthday is coming up and he loves superheroes. Is Max The Hero available on Nov 12th?"</p>
              </div>
              <span class="status-badge status-pending" id="badge-enq-2">Open</span>
            </div>
            <div style="margin-top: 20px; display: flex; gap: 10px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px;">
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="openReplyModal('enq-2')"><i class="fa-solid fa-reply"></i> Reply</button>
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem; background: #2ecc71;" onclick="openModal()"><i class="fa-solid fa-calendar-check"></i> Convert to Booking</button>
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem; background: rgba(0,0,0,0.5); border: 1px solid var(--color-border);" onclick="resolveEnquiry('enq-2')"><i class="fa-solid fa-check"></i> Resolve</button>
            </div>
          </div>
          
          <!-- Enquiry 3 -->
          <div class="enquiry-card" id="enq-3" style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
              <div>
                <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Amanda Clark</h4>
                <div style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 15px;">Phone: (555) 345-6789 | Date: Yesterday, 1:15 PM</div>
                <p style="margin: 0; font-size: 0.95rem; line-height: 1.5;">"Can you send me your full pricing sheet for Wedding Receptions? Also do you provide your own lighting equipment?"</p>
              </div>
              <span class="status-badge status-pending" id="badge-enq-3">Open</span>
            </div>
            <div style="margin-top: 20px; display: flex; gap: 10px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px;">
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="openReplyModal('enq-3')"><i class="fa-solid fa-reply"></i> Reply</button>
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem; background: rgba(0,0,0,0.5); border: 1px solid var(--color-border);" onclick="resolveEnquiry('enq-3')"><i class="fa-solid fa-check"></i> Resolve</button>
            </div>
          </div>

          <!-- Enquiry 4 -->
          <div class="enquiry-card" id="enq-4" style="background: rgba(255,255,255,0.02); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
              <div>
                <h4 style="margin: 0 0 5px; font-size: 1.2rem; color: var(--color-primary);">Sarah Jenkins</h4>
                <div style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 15px;">Existing Client | Date: Oct 1, 09:30 AM</div>
                <p style="margin: 0; font-size: 0.95rem; line-height: 1.5;">"Hi, I just wanted to confirm what time Max The Hero will arrive for the party today. Thanks!"</p>
              </div>
              <span class="status-badge status-success" id="badge-enq-4">Resolved</span>
            </div>
            <div style="margin-top: 20px; display: flex; gap: 10px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px;">
              <button class="btn-primary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="openReplyModal('enq-4')"><i class="fa-solid fa-reply"></i> Reply</button>
            </div>
          </div>
        </div>
      </div>
    </div>
"""
content = content.replace('<!-- SETTINGS TAB -->', enquiries_tab + '\n    <!-- SETTINGS TAB -->')

# 4. Add Staff Modal and Reply Modal HTML
modals = """
  <!-- Staff Modal -->
  <div class="modal" id="staffModal">
    <div class="modal-content">
      <button class="close-modal" onclick="closeStaffModal()"><i class="fa-solid fa-xmark"></i></button>
      <h2 style="margin-top: 0; font-family: var(--font-heading); color: var(--color-primary);">Add New Staff</h2>
      
      <form id="newStaffForm" onsubmit="event.preventDefault(); submitStaff();">
        <div class="form-group">
          <label>Staff Name</label>
          <input type="text" class="form-control" id="staffName" required>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
          <div class="form-group">
            <label>Role</label>
            <input type="text" class="form-control" id="staffRole" placeholder="e.g. Entertainer" required>
          </div>
          <div class="form-group">
            <label>Assigned Hall</label>
            <input type="text" class="form-control" id="staffHall" placeholder="e.g. Hall A" required>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
          <div class="form-group">
            <label>Shift Hour</label>
            <input type="text" class="form-control" id="staffShift" placeholder="e.g. 09:00 AM - 05:00 PM" required>
          </div>
          <div class="form-group">
            <label>Contact Number</label>
            <input type="text" class="form-control" id="staffContact" placeholder="(555) 000-0000" required>
          </div>
        </div>
        <button type="submit" class="btn-primary" style="width: 100%; margin-top: 10px;">Add Staff Member</button>
      </form>
    </div>
  </div>

  <!-- Reply Modal -->
  <div class="modal" id="replyModal">
    <div class="modal-content">
      <button class="close-modal" onclick="closeReplyModal()"><i class="fa-solid fa-xmark"></i></button>
      <h2 style="margin-top: 0; font-family: var(--font-heading); color: var(--color-primary);">Respond to Enquiry</h2>
      
      <form id="replyForm" onsubmit="event.preventDefault(); submitReply();">
        <input type="hidden" id="replyEnquiryId">
        <div class="form-group">
          <label>Response Message</label>
          <textarea class="form-control" rows="5" required placeholder="Type your response here..."></textarea>
        </div>
        <button type="submit" class="btn-primary" style="width: 100%; margin-top: 10px;"><i class="fa-solid fa-paper-plane"></i> Send Reply & Resolve</button>
      </form>
    </div>
  </div>
"""
content = content.replace('<!-- Slot Modal -->', modals + '\n  <!-- Slot Modal -->')

# 5. Add JavaScript for the new modals
js_addition = """
    // Staff JS
    function openStaffModal() { document.getElementById('staffModal').classList.add('active'); }
    function closeStaffModal() { document.getElementById('staffModal').classList.remove('active'); document.getElementById('newStaffForm').reset(); }
    
    function submitStaff() {
      const name = document.getElementById('staffName').value;
      const role = document.getElementById('staffRole').value;
      const hall = document.getElementById('staffHall').value;
      const shift = document.getElementById('staffShift').value;
      const contact = document.getElementById('staffContact').value;
      const newId = 'duty-' + Math.floor(Math.random() * 1000);
      
      const newRow = `
        <tr style="animation: fadeIn 0.5s;">
          <td>${name}</td>
          <td>${role}</td>
          <td>${hall}</td>
          <td>${shift}</td>
          <td>${contact}</td>
          <td><span class="status-badge status-success" id="${newId}">On Duty</span></td>
          <td>
            <select class="filter-select" onchange="updateDutyStatus('${newId}', this.value)" style="padding: 5px 10px; font-size: 0.85rem;">
              <option value="On Duty" selected>On Duty</option>
              <option value="Off Duty">Off Duty</option>
              <option value="Standby">Standby</option>
            </select>
          </td>
        </tr>
      `;
      
      document.querySelector('#staffTable tbody').insertAdjacentHTML('beforeend', newRow);
      closeStaffModal();
    }

    // Enquiry JS
    function openReplyModal(enquiryId) {
      document.getElementById('replyEnquiryId').value = enquiryId;
      document.getElementById('replyModal').classList.add('active');
    }
    
    function closeReplyModal() {
      document.getElementById('replyModal').classList.remove('active');
      document.getElementById('replyForm').reset();
    }
    
    function submitReply() {
      const enqId = document.getElementById('replyEnquiryId').value;
      resolveEnquiry(enqId);
      closeReplyModal();
    }
    
    function resolveEnquiry(enquiryId) {
      const badge = document.getElementById('badge-' + enquiryId);
      if(badge) {
        badge.className = 'status-badge status-success';
        badge.textContent = 'Resolved';
      }
      // Add a subtle green border to indicate it's resolved
      const card = document.getElementById(enquiryId);
      if(card) {
        card.style.borderColor = '#2ecc71';
      }
    }
"""

content = content.replace('function openSlotModal()', js_addition + '\n    function openSlotModal()')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
