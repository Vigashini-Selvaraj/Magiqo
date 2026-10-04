import re

filepath = r'c:\Users\vigas\Desktop\magiqo\admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Staff Directory table
old_table_pattern = r'<table class="table">.*?<tbody>.*?</tbody>\s*</table>'

new_table = """<table class="table" id="staffTable">
            <thead>
              <tr>
                <th>Staff Member</th>
                <th>Role</th>
                <th>Assigned Hall</th>
                <th>Shift Hour</th>
                <th>Contact</th>
                <th>Duty Status</th>
                <th>Toggle Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Max The Hero</td>
                <td>Entertainer</td>
                <td>Hall A (Main)</td>
                <td>09:00 AM - 05:00 PM</td>
                <td>(555) 123-4567</td>
                <td><span class="status-badge status-success" id="duty-1">On Duty</span></td>
                <td>
                  <select class="filter-select" onchange="updateDutyStatus('duty-1', this.value)" style="padding: 5px 10px; font-size: 0.85rem;">
                    <option value="On Duty" selected>On Duty</option>
                    <option value="Off Duty">Off Duty</option>
                    <option value="Standby">Standby</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>The Great Houdini</td>
                <td>Lead Entertainer</td>
                <td>Hall B (Gala)</td>
                <td>12:00 PM - 08:00 PM</td>
                <td>(555) 987-6543</td>
                <td><span class="status-badge status-pending" id="duty-2">En Route</span></td>
                <td>
                  <select class="filter-select" onchange="updateDutyStatus('duty-2', this.value)" style="padding: 5px 10px; font-size: 0.85rem;">
                    <option value="En Route" selected>En Route</option>
                    <option value="On Duty">On Duty</option>
                    <option value="Off Duty">Off Duty</option>
                    <option value="Standby">Standby</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>Princess Aurora</td>
                <td>Entertainer</td>
                <td>Hall C (Party)</td>
                <td>02:00 PM - 06:00 PM</td>
                <td>(555) 456-7890</td>
                <td><span class="status-badge" style="background: rgba(255,255,255,0.1); color: var(--color-text-light);" id="duty-3">Standby</span></td>
                <td>
                  <select class="filter-select" onchange="updateDutyStatus('duty-3', this.value)" style="padding: 5px 10px; font-size: 0.85rem;">
                    <option value="On Duty">On Duty</option>
                    <option value="Off Duty">Off Duty</option>
                    <option value="Standby" selected>Standby</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>Alice G.</td>
                <td>Event Coordinator</td>
                <td>Front Desk</td>
                <td>08:00 AM - 04:00 PM</td>
                <td>(555) 222-3333</td>
                <td><span class="status-badge status-success" id="duty-4">On Duty</span></td>
                <td>
                  <select class="filter-select" onchange="updateDutyStatus('duty-4', this.value)" style="padding: 5px 10px; font-size: 0.85rem;">
                    <option value="On Duty" selected>On Duty</option>
                    <option value="Off Duty">Off Duty</option>
                    <option value="Standby">Standby</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>Mark V.</td>
                <td>Super Admin</td>
                <td>HQ Office</td>
                <td>09:00 AM - 06:00 PM</td>
                <td>(555) 111-0000</td>
                <td><span class="status-badge" style="background: rgba(210, 75, 118, 0.1); color: var(--color-primary);" id="duty-5">Off Duty</span></td>
                <td>
                  <select class="filter-select" onchange="updateDutyStatus('duty-5', this.value)" style="padding: 5px 10px; font-size: 0.85rem;">
                    <option value="On Duty">On Duty</option>
                    <option value="Off Duty" selected>Off Duty</option>
                    <option value="Standby">Standby</option>
                  </select>
                </td>
              </tr>
            </tbody>
          </table>"""

content = re.sub(old_table_pattern, new_table, content, flags=re.DOTALL)

# Add the JS function for updateDutyStatus
js_function = """
    function updateDutyStatus(badgeId, newStatus) {
      const badge = document.getElementById(badgeId);
      badge.textContent = newStatus;
      
      // Reset classes
      badge.className = 'status-badge';
      badge.style.background = '';
      badge.style.color = '';
      
      // Apply appropriate styles based on status
      if (newStatus === 'On Duty') {
        badge.classList.add('status-success');
      } else if (newStatus === 'Off Duty') {
        badge.style.background = 'rgba(210, 75, 118, 0.1)';
        badge.style.color = 'var(--color-primary)';
      } else if (newStatus === 'En Route') {
        badge.classList.add('status-pending');
      } else if (newStatus === 'Standby') {
        badge.style.background = 'rgba(255,255,255,0.1)';
        badge.style.color = 'var(--color-text-light)';
      }
    }
"""

content = content.replace('function filterBookings() {', js_function + '\n    function filterBookings() {')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
