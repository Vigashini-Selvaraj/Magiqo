import re

# 1. Update entertainers.html
with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    ent_html = f.read()

# Add script at the end of makers-grid to dynamic update links
script_injection = """
      </div>
      <script>
        // Dynamically update all maker cards to pass their name in URL
        document.querySelectorAll('.maker-card').forEach(card => {
            const name = card.dataset.name ? card.dataset.name.toLowerCase() : '';
            const btn = card.querySelector('a');
            if(btn && name) {
                btn.href = 'entertainer_detail.html?id=' + name;
            }
        });
      </script>
"""
ent_html = ent_html.replace('      </div>\n\n      <!-- Interactive Quiz Suggestion -->', script_injection + '\n\n      <!-- Interactive Quiz Suggestion -->')
# Also fallback just in case the quiz suggestion is not caught
ent_html = ent_html.replace('<a href="entertainer_detail.html" class="btn btn-primary"', '<a href="entertainer_detail.html?id=elias" class="btn btn-primary"')

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(ent_html)

# 2. Update entertainer_detail.html
with open('c:/Users/vigas/Desktop/magiqo/entertainer_detail.html', 'r', encoding='utf-8') as f:
    detail_html = f.read()

# Add IDs to elements
detail_html = detail_html.replace('<h1>Elias</h1>', '<h1 id="ent-name">Elias</h1>')
detail_html = detail_html.replace('<div class="profile-specialty">Master Magician & Illusionist</div>', '<div class="profile-specialty" id="ent-title">Master Magician & Illusionist</div>')
detail_html = detail_html.replace('<img src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias the Magician">', '<img id="ent-img" src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias the Magician">')
detail_html = detail_html.replace('<h2><span style="color: #3895c8;">Meet</span> <span style="color: var(--color-primary);">Elias</span></h2>', '<h2><span style="color: #3895c8;">Meet</span> <span style="color: var(--color-primary);" id="ent-meet-name">Elias</span></h2>')
detail_html = detail_html.replace('Book Elias Now', 'Book <span id="ent-book-btn">Elias</span> Now')
detail_html = detail_html.replace('Book</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Elias</span></h2>', 'Book</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);" id="ent-book-title">Elias</span></h2>')
detail_html = detail_html.replace('Good News! Elias is Available!', 'Good News! <span id="ent-avail-name">Elias</span> is Available!')
detail_html = detail_html.replace('secured Elias the Magician', 'secured <span id="ent-success-name">Elias</span>')


# Add the javascript logic at the bottom
js_logic = """
  <script>
    const entertainerData = {
      elias: { name: "Elias", title: "Master Magician & Illusionist", img: "assets/images/magician_portrait_1790843004983.jpg" },
      lily: { name: "Princess Lily", title: "Royal Visits & Vocals", img: "assets/images/princess_portrait_1790843055244.jpg" },
      barnaby: { name: "Barnaby", title: "Classic Clown", img: "assets/images/clown_party_1790842566084.jpg" },
      jojo: { name: "Jojo", title: "Comedy & Acrobatics", img: "assets/images/founder_mark.jpg" },
      sarah: { name: "Sarah", title: "Face Painter", img: "assets/images/gallery_smile_1.jpg" }
    };

    document.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        let id = urlParams.get('id');
        if(id) {
            id = id.toLowerCase();
            let data = entertainerData[id];
            
            // Fallback for dynamically generated names not in dictionary
            if(!data) {
                const Capitalized = id.charAt(0).toUpperCase() + id.slice(1);
                data = { name: Capitalized, title: "Premium Entertainer", img: "assets/images/gallery_smile_1.jpg" };
            }
            
            // Update DOM
            document.getElementById('ent-name').innerText = data.name;
            document.getElementById('ent-title').innerText = data.title;
            document.getElementById('ent-img').src = data.img;
            document.getElementById('ent-meet-name').innerText = data.name;
            document.getElementById('ent-book-btn').innerText = data.name;
            document.getElementById('ent-book-title').innerText = data.name;
            document.getElementById('ent-avail-name').innerText = data.name;
            document.getElementById('ent-success-name').innerText = data.name;
            
            // Update document title
            document.title = data.name + " - " + data.title + " | Magiqo";
            
            // Update package links
            const packageLinks = document.querySelectorAll('a[href^="packages.html"]');
            packageLinks.forEach(link => {
                link.href = 'packages.html?entertainer=' + id;
            });
        }
    });
  </script>
"""

detail_html = detail_html.replace('</script>\n</body>', js_logic + '\n</script>\n</body>')

with open('c:/Users/vigas/Desktop/magiqo/entertainer_detail.html', 'w', encoding='utf-8') as f:
    f.write(detail_html)
