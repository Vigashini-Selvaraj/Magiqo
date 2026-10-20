import re
import os

base_dir = r'c:\Users\vigas\Desktop\magiqo'

def fix_about_html():
    file_path = os.path.join(base_dir, 'about.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix .journey-year visibility in light theme (change color: var(--color-supporting) to color: var(--color-primary); font-weight: 800;)
    old_year = re.compile(r'\.journey-year\s*\{\s*font-family:\s*var\(--font-magic\);\s*font-size:\s*3rem;\s*color:\s*var\(--color-supporting\);', re.DOTALL)
    new_year = '''.journey-year {
      font-family: var(--font-magic);
      font-size: 3.2rem;
      font-weight: 900;
      color: #C92A58;'''
    
    if old_year.search(content):
        content = old_year.sub(new_year, content)
        print("Updated .journey-year in about.html")
    else:
        # Fallback replacement
        content = content.replace('color: var(--color-supporting);', 'color: #C92A58; font-weight: 900;')
        print("Updated journey-year with fallback replacement")

    # 2. Ensure "Not just a party" uses solid #C92A58
    content = content.replace(
        'style="background: var(--color-primary); color: white;"',
        'style="background: #C92A58; color: white;"'
    )

    # 3. Ensure .cta-section uses solid #C92A58
    content = re.sub(
        r'\.cta-section\s*\{\s*background:\s*[^;]+;',
        '.cta-section {\n      background: #C92A58 !important;',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed about.html successfully!")

def fix_all_cta_colors():
    files_to_check = [
        'service_detail.html',
        'services.html',
        'blog_detail.html',
        'blog.html',
        'entertainers.html',
        'entertainer_detail.html',
        'packages.html',
        'join.html',
        'home2.html',
        'upload.html'
    ]

    for fname in files_to_check:
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        # Replace linear-gradient or other background in .cta-section / .cta-banner-section with #C92A58 !important
        # 1. .cta-section CSS
        pattern_cta_section = re.compile(r'(\.cta-section\s*\{[^}]*?background:\s*)([^;]+)(;)', re.DOTALL)
        if pattern_cta_section.search(content):
            content = pattern_cta_section.sub(r'\1#C92A58 !important\3', content)
            modified = True

        # 2. .cta-banner-section CSS
        pattern_cta_banner = re.compile(r'(\.cta-banner-section\s*\{[^}]*?background:\s*)([^;]+)(;)', re.DOTALL)
        if pattern_cta_banner.search(content):
            content = pattern_cta_banner.sub(r'\1#C92A58 !important\3', content)
            modified = True

        # 3. Inline style="background: linear-gradient(...)" on <section class="cta-section"...> or <section class="cta-banner-section"...>
        pattern_inline_cta = re.compile(r'(<section[^>]*class=["\'][^"\']*(?:cta-section|cta-banner-section)[^"\']*["\'][^>]*style=["\'][^"\']*?background:\s*)([^;]+)(;[^"\']*["\'])', re.IGNORECASE | re.DOTALL)
        if pattern_inline_cta.search(content):
            content = pattern_inline_cta.sub(r'\1#C92A58 !important\3', content)
            modified = True

        # Also replace any repeating-conic-gradient in entertainers.html
        if 'repeating-conic-gradient' in content:
            content = re.sub(r'repeating-conic-gradient\([^;]+;', '#C92A58 !important;', content)
            modified = True

        # Also replace #D24B76 in services.html
        if '#D24B76' in content:
            content = content.replace('#D24B76', '#C92A58')
            modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated CTA color in {fname} to #C92A58")
        else:
            print(f"No CTA modification needed in {fname}")

def update_global_style_css():
    fpath = os.path.join(base_dir, 'css', 'style.css')
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    global_rule = '''
/* ========================================================
   UNIVERSAL MAGIQO CTA BRAND PINK (#C92A58)
   Consistent vibrant brand pink across all pages & themes
   ======================================================== */
.cta-section, .cta-banner-section {
  background: #C92A58 !important;
  background-color: #C92A58 !important;
  color: #FFFFFF !important;
}

.cta-section h2, .cta-banner-section h2 {
  color: #FFFFFF !important;
  -webkit-text-fill-color: #FFFFFF !important;
  background: none !important;
}

.cta-section p, .cta-banner-section p {
  color: rgba(255, 255, 255, 0.95) !important;
}

.cta-section .btn-white, .cta-banner-section .btn-white {
  background: #FFFFFF !important;
  color: #C92A58 !important;
  border-color: #FFFFFF !important;
  font-weight: 700 !important;
}

.cta-section .btn-white:hover, .cta-banner-section .btn-white:hover {
  background: #FFF8F0 !important;
  color: #A71C44 !important;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

.cta-section .btn-outline-white, .cta-banner-section .btn-outline-white {
  background: transparent !important;
  color: #FFFFFF !important;
  border: 2px solid rgba(255, 255, 255, 0.85) !important;
  font-weight: 700 !important;
}

.cta-section .btn-outline-white:hover, .cta-banner-section .btn-outline-white:hover {
  background: #FFFFFF !important;
  color: #C92A58 !important;
  border-color: #FFFFFF !important;
  transform: translateY(-2px);
}
'''
    if 'UNIVERSAL MAGIQO CTA BRAND PINK' not in content:
        content += global_rule
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Added universal Magiqo CTA brand pink rules to css/style.css")
    else:
        print("Universal CTA rule already present in css/style.css")

if __name__ == '__main__':
    fix_about_html()
    fix_all_cta_colors()
    update_global_style_css()
