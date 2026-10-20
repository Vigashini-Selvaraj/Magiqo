import re
import os

def check_images(file_name):
    print(f'Checking {file_name}:')
    base_dir = r'c:\Users\vigas\Desktop\magiqo'
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Matches src="..." and src='...'
    srcs = re.findall(r'src=["\'](assets/images/[^"\']+)["\']', content)
    # Also find any in onclick or href
    other_imgs = re.findall(r'img=(assets/images/[^&"\']+)', content)
    all_imgs = set(srcs + other_imgs)
    
    all_ok = True
    for img in sorted(all_imgs):
        full_path = os.path.join(base_dir, img.replace('/', os.sep))
        if os.path.exists(full_path):
            print(f'  [OK] {img}')
        else:
            print(f'  [MISSING!] {img}')
            all_ok = False
    return all_ok

print("=== IMAGE VERIFICATION ===")
s_ok = check_images('service_detail.html')
b_ok = check_images('blog_detail.html')
bl_ok = check_images('blog.html')

if s_ok and b_ok and bl_ok:
    print("\nALL IMAGES ACROSS ALL DETAIL PAGES AND BLOG PAGE ARE 100% VALID AND EXIST ON DISK!")
else:
    print("\nSOME IMAGES ARE MISSING!")
