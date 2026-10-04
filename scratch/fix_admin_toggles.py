import re

filepath = r'c:\Users\vigas\Desktop\magiqo\admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove settings from sidebar
settings_sidebar_pattern = r'\s*<div class="admin-nav-item" onclick="switchTab\(\'settings\', this\)">\s*<i class="fa-solid fa-gear"></i> Settings\s*</div>'
content = re.sub(settings_sidebar_pattern, '', content)

# 2. Remove SETTINGS TAB block
# Look for <!-- SETTINGS TAB --> ... </div>\s*</div> (the closing of admin-content)
settings_tab_pattern = r'<!-- SETTINGS TAB -->\s*<div id="settings".*?</div>\s*</div>\s*</div>'
content = re.sub(settings_tab_pattern, '</div>', content, flags=re.DOTALL)

# Also check if there's a trailing <!-- SETTINGS TAB -->, it might have been duplicated
content = content.replace('<!-- SETTINGS TAB -->', '')

# 3. Change body tag
content = content.replace('<body data-theme="dark">', '<body>')

# 4. Remove theme.js inclusion
content = content.replace('<script src="js/theme.js"></script>', '')

# 5. Rename IDs of toggles
content = content.replace('id="theme-toggle"', 'id="admin-theme-toggle"')
content = content.replace('id="rtl-toggle"', 'id="admin-rtl-toggle"')

# 6. Inject the custom JS for admin toggles
custom_js = """
  <!-- Admin Theme & RTL Toggles -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const themeBtn = document.getElementById('admin-theme-toggle');
      const rtlBtn = document.getElementById('admin-rtl-toggle');
      const html = document.documentElement;

      // 1. Theme Initialization
      const savedTheme = localStorage.getItem('magiqo-theme') || 'dark';
      html.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);

      // 2. RTL Initialization
      const savedDir = localStorage.getItem('magiqo-dir') || 'ltr';
      html.setAttribute('dir', savedDir);

      // 3. Theme Toggle Click
      if (themeBtn) {
        themeBtn.addEventListener('click', () => {
          const currentTheme = html.getAttribute('data-theme');
          const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
          html.setAttribute('data-theme', newTheme);
          localStorage.setItem('magiqo-theme', newTheme);
          updateThemeIcon(newTheme);
        });
      }

      // 4. RTL Toggle Click
      if (rtlBtn) {
        rtlBtn.addEventListener('click', () => {
          const currentDir = html.getAttribute('dir');
          const newDir = currentDir === 'ltr' ? 'rtl' : 'ltr';
          html.setAttribute('dir', newDir);
          localStorage.setItem('magiqo-dir', newDir);
        });
      }

      function updateThemeIcon(theme) {
        if (!themeBtn) return;
        const span = themeBtn.querySelector('span');
        const icon = themeBtn.querySelector('i');
        if (theme === 'dark') {
          if(span) span.textContent = 'Light Theme';
          if(icon) icon.className = 'fa-solid fa-sun';
        } else {
          if(span) span.textContent = 'Dark Theme';
          if(icon) icon.className = 'fa-solid fa-moon';
        }
      }
    });
  </script>
</body>
"""

content = content.replace('</body>', custom_js)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
