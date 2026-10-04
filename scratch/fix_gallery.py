import re

filepath = r'c:\Users\vigas\Desktop\magiqo\entertainer_detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the gallery grid to make all images exactly the same size.
old_gallery = '''      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;">
        <div style="grid-column: span 2; grid-row: span 2; border-radius: 24px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
           <img src="assets/images/magic_show_party_1790842468826.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
        <div style="border-radius: 24px; overflow: hidden; box-shadow: 0 10px 20px rgba(0,0,0,0.05); height: 250px;">
           <img src="assets/images/about_art_of_magic.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
        <div style="border-radius: 24px; overflow: hidden; box-shadow: 0 10px 20px rgba(0,0,0,0.05); height: 250px;">
           <img src="assets/images/cute_kids_clapping_1790833571210.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
      </div>'''

new_gallery = '''      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
        <div style="border-radius: 24px; overflow: hidden; box-shadow: 0 10px 20px rgba(0,0,0,0.05); aspect-ratio: 4/3;">
           <img src="assets/images/magic_show_party_1790842468826.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
        <div style="border-radius: 24px; overflow: hidden; box-shadow: 0 10px 20px rgba(0,0,0,0.05); aspect-ratio: 4/3;">
           <img src="assets/images/about_art_of_magic.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
        <div style="border-radius: 24px; overflow: hidden; box-shadow: 0 10px 20px rgba(0,0,0,0.05); aspect-ratio: 4/3;">
           <img src="assets/images/cute_kids_clapping_1790833571210.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
      </div>'''

if old_gallery in content:
    content = content.replace(old_gallery, new_gallery)
else:
    print("Could not find the old gallery text.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
