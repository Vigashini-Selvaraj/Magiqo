import os

filepath = r'c:\Users\vigas\Desktop\magiqo\blog.html'

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Blog | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* 1. Blog Hero */
    .blog-hero {
      padding: 180px 20px 100px;
      text-align: center;
      background: linear-gradient(rgba(19, 49, 92, 0.8), rgba(19, 49, 92, 0.9)), url('assets/images/magic_show_party_1790842468826.jpg') center/cover no-repeat;
      position: relative;
      overflow: hidden;
      color: white;
    }
    .blog-hero h1 {
      font-family: var(--font-magic);
      font-size: clamp(3rem, 5vw, 5rem);
      margin-bottom: 20px;
      position: relative;
      z-index: 2;
    }
    .blog-hero h1 .gradient-text {
      background: linear-gradient(90deg, #ff8fa3, #7addff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .blog-hero p {
      font-size: 1.2rem;
      color: #e0e0e0;
      max-width: 600px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }
    .wand-animation {
      position: absolute;
      top: 50%;
      left: 10%;
      font-size: 5rem;
      color: #ff8fa3;
      opacity: 0.8;
      animation: floatWand 4s infinite ease-in-out;
      z-index: 1;
      transform: rotate(45deg);
    }
    .star-animation {
      position: absolute;
      top: 30%;
      right: 15%;
      font-size: 3rem;
      color: #f5a623;
      animation: twinkle 3s infinite;
      z-index: 1;
    }
    @keyframes floatWand {
      0%, 100% { transform: translateY(0) rotate(45deg); }
      50% { transform: translateY(-30px) rotate(55deg); }
    }
    @keyframes twinkle {
      0%, 100% { opacity: 0.3; transform: scale(0.8); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    .section-container { max-width: 1200px; margin: 0 auto 80px; padding: 0 20px; }
    .section-title { font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 40px; color: var(--color-text); }
    .section-title .text-pink { color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none; }
    .section-title .text-blue { color: #3895c8; -webkit-text-fill-color: #3895c8; background: none; }
    
    /* Explore Categories */
    .cat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; margin-top: -40px; position: relative; z-index: 10; padding: 0 20px;}
    .cat-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 16px;
      padding: 25px 20px;
      text-align: center;
      cursor: pointer;
      transition: all 0.3s;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .cat-card:hover { transform: translateY(-10px); border-color: #3895c8; box-shadow: 0 15px 40px rgba(56, 149, 200, 0.2); }
    .cat-card i { font-size: 2.5rem; color: var(--color-primary); margin-bottom: 15px; transition: 0.3s; }
    .cat-card:hover i { transform: scale(1.1); color: #3895c8; }
    .cat-card h4 { font-size: 1.1rem; color: var(--color-text); margin:0; }

    /* Featured Story */
    .featured-story {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      background: var(--color-surface);
      border-radius: 24px;
      overflow: hidden;
      border: 1px solid var(--color-border);
      box-shadow: 0 10px 30px var(--color-shadow);
      transition: transform 0.3s;
    }
    .featured-story:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.1); }
    .featured-img-wrap { width: 100%; height: 100%; min-height: 350px; overflow: hidden; }
    .featured-img-wrap img { width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }
    .featured-story:hover .featured-img-wrap img { transform: scale(1.05); }
    .featured-content { padding: 40px; display: flex; flex-direction: column; justify-content: center; }
    .category-tag {
      display: inline-block;
      padding: 6px 15px;
      border-radius: 50px;
      background: rgba(210, 75, 118, 0.1);
      color: var(--color-primary);
      font-weight: bold;
      font-size: 0.85rem;
      text-transform: uppercase;
      margin-bottom: 15px;
      width: fit-content;
    }
    .featured-content h2 { font-family: var(--font-heading); font-size: 2.2rem; color: var(--color-text); margin-bottom: 15px; line-height: 1.3; }
    .featured-content p { color: var(--color-text-light); margin-bottom: 25px; line-height: 1.6; font-size: 1.1rem; }
    .read-more { font-weight: bold; color: #3895c8; text-decoration: none; display: flex; align-items: center; gap: 8px; font-size: 1.1rem; }
    .read-more:hover { color: var(--color-primary); }

    /* Search & Filter Bar */
    .filter-bar {
      padding: 20px 30px;
      background: var(--color-surface);
      border-radius: 20px;
      box-shadow: 0 10px 30px var(--color-shadow);
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      align-items: center;
      justify-content: space-between;
      border: 1px solid var(--color-border);
      margin-bottom: 40px;
    }
    .search-input {
      flex: 1;
      min-width: 250px;
      padding: 12px 20px;
      border-radius: 50px;
      border: 1px solid rgba(0,0,0,0.1);
      background: var(--color-bg);
      color: var(--color-text);
      font-size: 1rem;
    }
    .search-input:focus { outline: none; border-color: #3895c8; }
    .category-filters { display: flex; gap: 10px; flex-wrap: wrap; }
    .filter-btn {
      padding: 8px 20px;
      border-radius: 50px;
      border: 1px solid rgba(0,0,0,0.1);
      background: var(--color-bg);
      color: var(--color-text);
      cursor: pointer;
      font-weight: 600;
      transition: 0.3s;
    }
    .filter-btn.active, .filter-btn:hover { background: #3895c8; color: white; border-color: #3895c8; }

    /* Blog Grid */
    .blog-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; }
    .blog-card {
      background: var(--color-surface);
      border-radius: 20px;
      overflow: hidden;
      border: 1px solid var(--color-border);
      box-shadow: 0 10px 30px var(--color-shadow);
      transition: transform 0.4s, box-shadow 0.4s;
      display: flex;
      flex-direction: column;
    }
    .blog-card.hidden { display: none; }
    .blog-card:hover { transform: translateY(-8px); box-shadow: 0 15px 40px rgba(0,0,0,0.1); }
    .blog-img { width: 100%; height: 200px; object-fit: cover; }
    .blog-content { padding: 25px; flex-grow: 1; display: flex; flex-direction: column; }
    .blog-meta { display: flex; justify-content: space-between; color: var(--color-text-light); font-size: 0.85rem; margin-bottom: 10px; }
    .blog-content h3 { font-size: 1.3rem; margin-bottom: 10px; color: var(--color-text); line-height: 1.4; cursor: pointer; }
    .blog-content p { color: var(--color-text-light); font-size: 0.95rem; margin-bottom: 20px; flex-grow: 1; }
    .no-results { text-align: center; padding: 50px; font-size: 1.2rem; color: var(--color-text-light); width: 100%; grid-column: 1 / -1; display: none; }

    /* Other Sections */
    .gallery-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
    .gallery-grid img { width: 100%; height: 200px; object-fit: cover; border-radius: 12px; transition: transform 0.4s; cursor: pointer; }
    .gallery-grid img:hover { transform: scale(1.05) translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }
    
    .newsletter-section {
      background: linear-gradient(135deg, rgba(210, 75, 118, 0.1), rgba(56, 149, 200, 0.1));
      border-radius: 24px;
      padding: 60px 30px;
      text-align: center;
      margin: 80px auto;
      max-width: 1000px;
      border: 1px solid rgba(56, 149, 200, 0.2);
    }
    .newsletter-input {
      padding: 15px 25px;
      border-radius: 50px;
      border: none;
      width: 100%;
      max-width: 400px;
      font-size: 1rem;
      margin-right: 10px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .btn-subscribe {
      padding: 15px 35px;
      border-radius: 50px;
      border: none;
      background: var(--color-primary);
      color: white;
      font-weight: bold;
      font-size: 1rem;
      cursor: pointer;
      transition: 0.3s;
    }
    .btn-subscribe:hover { background: #3895c8; transform: translateY(-3px); }
    .cta-final { background: var(--color-bg); padding: 80px 20px; text-align: center; border-top: 1px solid var(--color-border); }

    @media (max-width: 768px) {
      .featured-story { grid-template-columns: 1fr; }
      .featured-img-wrap { min-height: 250px; }
      .cat-grid { margin-top: 40px; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <!-- 1. BLOG HERO -->
  <header class="blog-hero">
    <i class="fa-solid fa-wand-magic-sparkles wand-animation"></i>
    <i class="fa-solid fa-star star-animation"></i>
    <div class="container reveal">
      <h1><span class="gradient-text">Ideas That Make Every</span> <br><span style="color: #7addff;">Celebration Magical</span></h1>
      <p>Discover inspiration, themes, expert planning tips, and fun activities to create unforgettable moments.</p>
    </div>
  </header>

  <main>
    <!-- 2. EXPLORE CATEGORIES (Acts as Filter triggers) -->
    <div class="cat-grid reveal" style="max-width: 1200px; margin-left: auto; margin-right: auto; margin-bottom: 80px;">
      <div class="cat-card" onclick="document.querySelector('[data-filter=Themes]').click()">
        <i class="fa-solid fa-wand-sparkles"></i><h4>Party Themes</h4>
      </div>
      <div class="cat-card" onclick="document.querySelector('[data-filter=Entertainers]').click()">
        <i class="fa-solid fa-masks-theater"></i><h4>Entertainers</h4>
      </div>
      <div class="cat-card" onclick="document.querySelector('[data-filter=Planning]').click()">
        <i class="fa-solid fa-calendar-check"></i><h4>Event Planning</h4>
      </div>
      <div class="cat-card" onclick="document.querySelector('[data-filter=Decor]').click()">
        <i class="fa-solid fa-gem"></i><h4>Decorations</h4>
      </div>
      <div class="cat-card" onclick="document.querySelector('[data-filter=Kids]').click()">
        <i class="fa-solid fa-gamepad"></i><h4>Kids' Activities</h4>
      </div>
    </div>

    <!-- 3. FEATURED STORY -->
    <section class="section-container reveal">
      <div class="featured-story">
        <div class="featured-img-wrap">
          <img src="assets/images/magic_show_party_1790842468826.jpg" alt="Featured Magic Show">
        </div>
        <div class="featured-content">
          <span class="category-tag">Featured • Themes</span>
          <h2>The Ultimate Guide to Hosting a Magic-Themed Birthday</h2>
          <p>Transform your living room into a mystical stage! From floating balloons to hiring the perfect master illusionist, we cover everything you need to know.</p>
          <a href="blog_detail.html" class="read-more">Read Article <i class="fa-solid fa-arrow-right"></i></a>
        </div>
      </div>
    </section>

    <!-- 4. FILTER BAR -->
    <section class="section-container reveal" id="articles">
      <h2 class="section-title" style="margin-top: 60px;"><span class="text-pink">All</span> <span class="text-blue">Articles</span></h2>
      <div class="filter-bar">
        <div class="category-filters" id="category-filters">
          <button class="filter-btn active" data-filter="all">All</button>
          <button class="filter-btn" data-filter="Themes">Party Themes</button>
          <button class="filter-btn" data-filter="Entertainers">Entertainers</button>
          <button class="filter-btn" data-filter="Planning">Event Planning</button>
          <button class="filter-btn" data-filter="Kids">Kids' Activities</button>
          <button class="filter-btn" data-filter="Decor">Decorations</button>
        </div>
        <input type="text" class="search-input" id="search-input" placeholder="Search articles, themes, tips...">
      </div>

      <!-- 5. 20 BLOGS GRID (Hardcoded to avoid JS rendering issues) -->
      <div class="blog-grid" id="blog-grid">
        <div class="no-results" id="no-results">No articles found matching your criteria.</div>
"""

# Generating 20 articles in HTML
articles_data = [
    ("10 Reasons to Hire a Professional Magician", "Entertainers", "assets/images/hero_magician_1790831867453.jpg", "Oct 1, 2026", "5 min"),
    ("How to Build a Superhero Obstacle Course", "Kids", "assets/images/superhero_party_1790842695325.jpg", "Sep 28, 2026", "4 min"),
    ("DIY Princess Crowns for the Royal Court", "Themes", "assets/images/princess_party_1790842645232.jpg", "Sep 25, 2026", "6 min"),
    ("The Ultimate Guide to Balloon Arch Decorations", "Decor", "assets/images/magic_show_party_1790842468826.jpg", "Sep 22, 2026", "7 min"),
    ("5 Tips from Event Experts to Reduce Stress", "Planning", "assets/images/about_kids_birthday.jpg", "Sep 20, 2026", "5 min"),
    ("Halloween Party Ideas That Are Spooky Not Scary", "Themes", "assets/images/cute_kids_clapping_1790833571210.jpg", "Sep 15, 2026", "4 min"),
    ("Choosing the Right Clown for Toddlers", "Entertainers", "assets/images/james_boy_smile.jpg", "Sep 12, 2026", "3 min"),
    ("Top 5 Party Favors Kids Actually Keep", "Planning", "assets/images/superhero_party_1790842695325.jpg", "Sep 10, 2026", "5 min"),
    ("How Much Space Do You Need for an Indoor Show?", "Planning", "assets/images/magic_show_party_1790842468826.jpg", "Sep 8, 2026", "4 min"),
    ("Eco-Friendly Party Decorations", "Decor", "assets/images/about_kids_birthday.jpg", "Sep 5, 2026", "6 min"),
    ("The Best Board Games for an 8-Year-Old's Party", "Kids", "assets/images/princess_party_1790842645232.jpg", "Sep 1, 2026", "5 min"),
    ("Summer Splash: Water-Themed Birthday Ideas", "Themes", "assets/images/james_boy_smile.jpg", "Aug 28, 2026", "4 min"),
    ("Face Painting 101: Safe Paints for Kids", "Entertainers", "assets/images/hero_magician_1790831867453.jpg", "Aug 25, 2026", "6 min"),
    ("How to Create a Photo Booth at Home", "Decor", "assets/images/cute_kids_clapping_1790833571210.jpg", "Aug 20, 2026", "5 min"),
    ("Managing Food Allergies at a Children's Party", "Planning", "assets/images/about_kids_birthday.jpg", "Aug 15, 2026", "7 min"),
    ("Fairy Garden Setup: A Magical Afternoon", "Themes", "assets/images/princess_party_1790842645232.jpg", "Aug 10, 2026", "4 min"),
    ("Best Ice-Breaker Games for Shy Kids", "Kids", "assets/images/superhero_party_1790842695325.jpg", "Aug 5, 2026", "3 min"),
    ("What to Look for When Hiring an Entertainer", "Entertainers", "assets/images/hero_magician_1790831867453.jpg", "Jul 28, 2026", "6 min"),
    ("Winter Wonderland Party Ideas", "Themes", "assets/images/magic_show_party_1790842468826.jpg", "Jul 20, 2026", "5 min"),
    ("How to Keep Adults Entertained at a Kid's Party", "Planning", "assets/images/james_boy_smile.jpg", "Jul 15, 2026", "4 min")
]

for title, cat, img, date, read in articles_data:
    html_content += f"""
        <div class="blog-card" data-category="{cat}" data-title="{title.lower()}">
          <img src="{img}" alt="{title}" class="blog-img" onclick="location.href='blog_detail.html'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">{cat}</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html'">{title}</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> {date}</span>
              <span><i class="fa-regular fa-clock"></i> {read}</span>
            </div>
            <a href="blog_detail.html" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>"""

html_content += """
      </div>
    </section>

    <!-- 6. PARTY INSPIRATION GALLERY -->
    <section class="section-container reveal">
      <h2 class="section-title"><span class="text-pink">Party Inspiration</span> <span class="text-blue">Gallery</span></h2>
      <div class="gallery-grid">
        <img src="assets/images/superhero_party_1790842695325.jpg" alt="Superhero Setup">
        <img src="assets/images/princess_party_1790842645232.jpg" alt="Princess Setup">
        <img src="assets/images/about_kids_birthday.jpg" alt="Kids Setup">
        <img src="assets/images/james_boy_smile.jpg" alt="Happy Kid">
      </div>
    </section>

    <!-- 10. NEWSLETTER -->
    <section class="section-container reveal">
      <div class="newsletter-section" id="newsletter-box">
        <h2 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 15px; color: var(--color-text);">A Little Magic in Your Inbox</h2>
        <p style="color: var(--color-text-light); font-size: 1.1rem; margin-bottom: 30px;">Subscribe to get the latest party themes, DIY ideas, and exclusive Magiqo offers.</p>
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 15px;" id="nl-form">
          <input type="email" class="newsletter-input" placeholder="Enter your email address">
          <button type="button" class="btn-subscribe" onclick="document.getElementById('nl-form').innerHTML='<h3 style=\\'color:#10b981;\\'><i class=\\'fa-solid fa-circle-check\\'></i> Subscribed Successfully!</h3>'">Subscribe <i class="fa-solid fa-paper-plane" style="margin-left: 5px;"></i></button>
        </div>
      </div>
    </section>

    <!-- 12. FINAL CTA -->
    <section class="cta-final reveal">
      <h2 class="section-title" style="margin-bottom: 20px;"><span class="text-pink">Planning Your Next</span> <span class="text-blue">Celebration?</span></h2>
      <p style="color: var(--color-text-light); font-size: 1.15rem; margin-bottom: 30px;">Let us handle the entertainment while you enjoy the moment.</p>
      <a href="booking.html" class="btn btn-primary" style="padding: 15px 40px; font-size: 1.2rem;">Book Now <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></a>
    </section>

  </main>

  <!-- 13. FOOTER -->
  <div id="footer"></div>

  <script src="js/components.js"></script>
  <script src="js/theme.js"></script>
  <script>
    // Filtering Logic
    const searchInput = document.getElementById("search-input");
    const filterBtns = document.querySelectorAll(".filter-btn");
    const blogCards = document.querySelectorAll(".blog-card");
    const noResults = document.getElementById("no-results");

    function applyFilters() {
      const searchTerm = searchInput.value.toLowerCase();
      let currentFilter = 'all';
      
      filterBtns.forEach(btn => {
        if(btn.classList.contains('active')) {
          currentFilter = btn.getAttribute('data-filter');
        }
      });
      
      let visibleCount = 0;
      
      blogCards.forEach(card => {
        const cat = card.getAttribute('data-category');
        const title = card.getAttribute('data-title');
        
        const matchesCat = (currentFilter === 'all') || (cat === currentFilter);
        const matchesSearch = title.includes(searchTerm);
        
        if (matchesCat && matchesSearch) {
          card.classList.remove('hidden');
          visibleCount++;
        } else {
          card.classList.add('hidden');
        }
      });
      
      if (visibleCount === 0) {
        noResults.style.display = 'block';
      } else {
        noResults.style.display = 'none';
      }
    }

    filterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        applyFilters();
      });
    });

    searchInput.addEventListener("input", applyFilters);
  </script>
</body>
</html>
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_content)
