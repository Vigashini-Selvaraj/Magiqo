import re

def update_file(filename, is_register):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove Back to Home
    html = re.sub(r'<a href="index\.html" class="home-back">.*?</a>', '', html)

    # 2. Make logo clickable
    logo_block = """<div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 20px;">
      <img src="assets/images/magic_hat_logo.png" alt="Magiqo Logo" class="auth-logo" style="margin-bottom: 0; margin-top: 0;">
      <span style="font-family: var(--font-magic); font-size: 2.5rem; color: var(--color-primary);">Magiqo</span>
    </div>"""
    
    clickable_logo_block = """<a href="index.html" style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 20px; text-decoration: none;">
      <img src="assets/images/magic_hat_logo.png" alt="Magiqo Logo" class="auth-logo" style="margin-bottom: 0; margin-top: 0;">
      <span style="font-family: var(--font-magic); font-size: 2.5rem; color: var(--color-primary);">Magiqo</span>
    </a>"""
    html = html.replace(logo_block, clickable_logo_block)

    # Add relative positioning to form-group if not already there
    # We will add it inline for the password field
    
    if not is_register:
        # login.html
        # Update form submit
        html = html.replace("onsubmit=\"event.preventDefault(); window.location.href='index.html';\"", "onsubmit=\"event.preventDefault(); window.location.href='user_dashboard.html';\"")
        
        # Forgot password
        html = html.replace('<a href="#" class="forgot-link">Forgot Password?</a>', '<a href="#" class="forgot-link" onclick="alert(\'A password reset link has been sent to your email.\');">Forgot Password?</a>')
        
        # Add eye icon
        old_pwd = '<input type="password" class="form-control" placeholder="Password" required>'
        new_pwd = """<div style="position: relative;">
          <input type="password" id="login-pwd" class="form-control" placeholder="Password" required style="padding-right: 40px;">
          <i class="fa-solid fa-eye" id="toggle-pwd" style="position: absolute; right: 15px; top: 15px; color: rgba(255,255,255,0.5); cursor: pointer;" onclick="const pwd = document.getElementById('login-pwd'); if(pwd.type === 'password'){ pwd.type='text'; this.classList.remove('fa-eye'); this.classList.add('fa-eye-slash'); } else { pwd.type='password'; this.classList.remove('fa-eye-slash'); this.classList.add('fa-eye'); }"></i>
        </div>"""
        html = html.replace(old_pwd, new_pwd)
        
    else:
        # register.html
        # Update form submit with validation
        html = html.replace("onsubmit=\"event.preventDefault(); window.location.href='index.html';\"", "onsubmit=\"event.preventDefault(); if(document.getElementById('reg-pwd').value !== document.getElementById('reg-confirm').value) { alert('Passwords do not match!'); return; } window.location.href='user_dashboard.html';\"")
        
        # Replace password with pwd + confirm
        old_pwd = '<input type="password" class="form-control" placeholder="Password" required>'
        new_pwd = """<div style="position: relative;">
          <input type="password" id="reg-pwd" class="form-control" placeholder="Password" required style="padding-right: 40px;">
          <i class="fa-solid fa-eye" style="position: absolute; right: 15px; top: 15px; color: rgba(255,255,255,0.5); cursor: pointer;" onclick="const pwd = document.getElementById('reg-pwd'); if(pwd.type === 'password'){ pwd.type='text'; this.classList.remove('fa-eye'); this.classList.add('fa-eye-slash'); } else { pwd.type='password'; this.classList.remove('fa-eye-slash'); this.classList.add('fa-eye'); }"></i>
        </div>
      </div>
      <div class="form-group">
        <div style="position: relative;">
          <input type="password" id="reg-confirm" class="form-control" placeholder="Confirm Password" required style="padding-right: 40px;">
          <i class="fa-solid fa-eye" style="position: absolute; right: 15px; top: 15px; color: rgba(255,255,255,0.5); cursor: pointer;" onclick="const pwd = document.getElementById('reg-confirm'); if(pwd.type === 'password'){ pwd.type='text'; this.classList.remove('fa-eye'); this.classList.add('fa-eye-slash'); } else { pwd.type='password'; this.classList.remove('fa-eye-slash'); this.classList.add('fa-eye'); }"></i>
        </div>"""
        html = html.replace(old_pwd, new_pwd)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

update_file('login.html', False)
update_file('register.html', True)

print("Auth pages updated successfully.")
