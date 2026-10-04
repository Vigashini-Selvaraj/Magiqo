import re

def fix_auth_layout(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace body flex alignment
    old_body_css = '''    body {
      margin: 0;
      padding: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;'''
    
    new_body_css = '''    body {
      margin: 0;
      padding: 40px 20px;
      box-sizing: border-box;
      min-height: 100vh;
      display: flex;
      align-items: flex-start;
      justify-content: center;'''
      
    content = content.replace(old_body_css, new_body_css)
    
    # Ensure auth-card has margin auto to center it but allow scrolling
    if '.auth-card {' in content:
        # Instead of replacing exact text, we can use regex to inject margin: auto
        content = re.sub(r'(\.auth-card\s*\{)', r'\1\n      margin: auto;', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_auth_layout(r'c:\Users\vigas\Desktop\magiqo\login.html')
fix_auth_layout(r'c:\Users\vigas\Desktop\magiqo\register.html')
