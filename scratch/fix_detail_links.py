import os

# Update index.html
with open('c:/Users/vigas/Desktop/magiqo/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Elias Book Now button
idx_content = idx_content.replace(
    '<a href="entertainers.html" class="btn btn-outline" style="padding: 0.5rem 1rem; border-color: #3895c8; color: #3895c8;">Book Now</a>',
    '<a href="entertainer_detail.html?id=elias" class="btn btn-outline" style="padding: 0.5rem 1rem; border-color: #3895c8; color: #3895c8;">Book Now</a>',
    1 
)

# Max Book Now button
idx_content = idx_content.replace(
    '<a href="entertainers.html" class="btn btn-outline" style="padding: 0.5rem 1rem; border-color: #3895c8; color: #3895c8;">Book Now</a>',
    '<a href="entertainer_detail.html?id=max" class="btn btn-outline" style="padding: 0.5rem 1rem; border-color: #3895c8; color: #3895c8;">Book Now</a>',
    1 
)

# Mia Book Now button
idx_content = idx_content.replace(
    '<a href="entertainers.html" class="btn btn-outline" style="padding: 0.5rem 1rem; border-color: #3895c8; color: #3895c8;">Book Now</a>',
    '<a href="entertainer_detail.html?id=mia" class="btn btn-outline" style="padding: 0.5rem 1rem; border-color: #3895c8; color: #3895c8;">Book Now</a>',
    1 
)

with open('c:/Users/vigas/Desktop/magiqo/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

# Update entertainer_detail.html
with open('c:/Users/vigas/Desktop/magiqo/entertainer_detail.html', 'r', encoding='utf-8') as f:
    det_content = f.read()

old_data = """    const entertainerData = {
      elias: { name: "Elias", title: "Master Magician & Illusionist", img: "assets/images/magician_portrait_1790843004983.jpg" },
      lily: { name: "Princess Lily", title: "Royal Visits & Vocals", img: "assets/images/princess_portrait_1790843055244.jpg" },
      barnaby: { name: "Barnaby", title: "Classic Clown", img: "assets/images/clown_party_1790842566084.jpg" },
      jojo: { name: "Jojo", title: "Comedy & Acrobatics", img: "assets/images/founder_mark.jpg" },
      sarah: { name: "Sarah", title: "Face Painter", img: "assets/images/gallery_smile_1.jpg" }
    };"""

new_data = """    const entertainerData = {
      elias: { name: "Elias the Magician", title: "Stage Magic & Illusionist", img: "assets/images/magician_portrait_1790843004983.jpg" },
      max: { name: "Max the Action Hero", title: "Superhero Performer", img: "https://images.unsplash.com/photo-1608889175123-8ee362201f81?q=80&w=600&auto=format&fit=crop" },
      mia: { name: "Princess Mia", title: "Royal Visits & Vocals", img: "assets/images/princess_portrait_1790843055244.jpg" },
      lily: { name: "Princess Lily", title: "Royal Visits & Vocals", img: "assets/images/princess_portrait_1790843055244.jpg" },
      barnaby: { name: "Barnaby", title: "Classic Clown", img: "assets/images/clown_party_1790842566084.jpg" },
      jojo: { name: "Jojo", title: "Comedy & Acrobatics", img: "assets/images/founder_mark.jpg" },
      sarah: { name: "Sarah", title: "Face Painter", img: "assets/images/gallery_smile_1.jpg" }
    };"""

det_content = det_content.replace(old_data, new_data)

with open('c:/Users/vigas/Desktop/magiqo/entertainer_detail.html', 'w', encoding='utf-8') as f:
    f.write(det_content)
