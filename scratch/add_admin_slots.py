import re

filepath = r'c:\Users\vigas\Desktop\magiqo\admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add 2 more recent booking activities (to make it 5)
activities_pattern = r'(<h4 style="margin: 0; font-size: 1rem;">Client Message</h4>\s*<p style="margin: 5px 0 0; font-size: 0.85rem; color: var\(--color-text-light\);">John Smith sent a message regarding his Magic Show\.</p>\s*</div>\s*</div>)'

two_more_activities = r'''\1
              <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border: 1px solid var(--color-border); display: flex; align-items: center; gap: 15px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(210, 75, 118, 0.1); color: var(--color-primary); display: flex; align-items: center; justify-content: center;"><i class="fa-solid fa-xmark"></i></div>
                <div>
                  <h4 style="margin: 0; font-size: 1rem;">Booking Cancelled</h4>
                  <p style="margin: 5px 0 0; font-size: 0.85rem; color: var(--color-text-light);">Bruce Wayne cancelled his Corporate Gala.</p>
                </div>
              </div>
              <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border: 1px solid var(--color-border); display: flex; align-items: center; gap: 15px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(56, 149, 200, 0.1); color: #3895c8; display: flex; align-items: center; justify-content: center;"><i class="fa-solid fa-calendar-check"></i></div>
                <div>
                  <h4 style="margin: 0; font-size: 1rem;">Event Completed</h4>
                  <p style="margin: 5px 0 0; font-size: 0.85rem; color: var(--color-text-light);">Tony Stark\'s Gala event finished successfully.</p>
                </div>
              </div>'''

content = re.sub(activities_pattern, two_more_activities, content)


# 2. Add "Add Slot" button to Slot header
slot_header_pattern = r'(<h3 style="font-size: 2rem;">Daily Slots</h3>\s*<input type="date" class="filter-select" value="2026-10-02">)'

new_slot_header = r'''<h3 style="font-size: 2rem;">Daily Slots</h3>
          <div style="display: flex; gap: 10px; align-items: center;">
            <input type="date" class="filter-select" value="2026-10-02">
            <button class="btn-primary" onclick="openModal()"><i class="fa-solid fa-plus"></i> Add Slot</button>
          </div>'''
content = re.sub(slot_header_pattern, new_slot_header, content)


# 3. Add 5 more slots for future
slot_grid_end_pattern = r'(<span class="status-badge status-success">Booked</span>\s*</div>\s*</div>\s*</div>\s*</div>)'

future_slots = r'''<span class="status-badge status-success">Booked</span>
          </div>
        </div>
        
        <h4 style="margin: 30px 0 15px; font-size: 1.2rem; color: var(--color-primary); border-bottom: 1px solid var(--color-border); padding-bottom: 10px;">Upcoming Future Slots</h4>
        <div class="slot-grid">
          <div class="slot-time" style="line-height:1.2;">Oct 10<br><span style="font-size:0.75rem;font-weight:normal;">02:00 PM</span></div>
          <div class="slot-card" style="border-left: 4px solid var(--color-primary);">
            <div>
              <h4 style="margin: 0 0 5px;">Kids Birthday</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light);">Lead: Max The Hero</div>
            </div>
            <span class="status-badge status-success">Booked</span>
          </div>
          
          <div class="slot-time" style="line-height:1.2;">Oct 13<br><span style="font-size:0.75rem;font-weight:normal;">06:00 PM</span></div>
          <div class="slot-card empty" onclick="openModal()">
            <i class="fa-solid fa-plus"></i> Add Booking to Slot
          </div>

          <div class="slot-time" style="line-height:1.2;">Oct 15<br><span style="font-size:0.75rem;font-weight:normal;">10:00 AM</span></div>
          <div class="slot-card" style="border-left: 4px solid #3895c8;">
            <div>
              <h4 style="margin: 0 0 5px;">Corporate Gala</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light);">Lead: The Great Houdini</div>
            </div>
            <span class="status-badge status-success">Booked</span>
          </div>

          <div class="slot-time" style="line-height:1.2;">Nov 02<br><span style="font-size:0.75rem;font-weight:normal;">03:30 PM</span></div>
          <div class="slot-card empty" onclick="openModal()">
            <i class="fa-solid fa-plus"></i> Add Booking to Slot
          </div>

          <div class="slot-time" style="line-height:1.2;">Nov 10<br><span style="font-size:0.75rem;font-weight:normal;">05:00 PM</span></div>
          <div class="slot-card" style="border-left: 4px solid #f1c40f;">
            <div>
              <h4 style="margin: 0 0 5px;">Wedding Reception</h4>
              <div style="font-size: 0.85rem; color: var(--color-text-light);">Lead: DJ Sparkles</div>
            </div>
            <span class="status-badge status-success">Booked</span>
          </div>
        </div>
      </div>
    </div>'''
content = re.sub(slot_grid_end_pattern, future_slots, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
