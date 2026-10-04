import json
import os

filepath = r'c:\Users\vigas\Desktop\magiqo\blog.html'

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Blog | Magiqo</title>

  <!-- External Stylesheets -->
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* 1. Blog Hero */
    .blog-hero {
      padding: 160px 20px 80px;
      text-align: center;
      background: var(--color-bg);
      position: relative;
      overflow: hidden;
    }
    .blog-hero h1 {
      font-family: var(--font-magic);
      font-size: clamp(3rem, 5vw, 4.5rem);
      margin-bottom: 20px;
    }
    .blog-hero h1 .gradient-text {
      background: linear-gradient(90deg, var(--color-primary), #3895c8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .blog-hero p {
      font-size: 1.15rem;
      color: var(--color-text-light);
      max-width: 600px;
      margin: 0 auto;
    }
    
    /* Search & Filter Bar */
    .filter-bar {
      max-width: 1200px;
      margin: -30px auto 50px;
      padding: 20px 30px;
      background: var(--color-surface);
      border-radius: 20px;
      box-shadow: 0 10px 30px var(--color-shadow);
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      align-items: center;
      justify-content: space-between;
      position: relative;
      z-index: 10;
      border: 1px solid var(--color-border);
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
    .category-filters {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
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
    .filter-btn.active, .filter-btn:hover {
      background: #3895c8;
      color: white;
      border-color: #3895c8;
    }

    /* 2. Featured Story */
    .section-container { max-width: 1200px; margin: 0 auto 80px; padding: 0 20px; }
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
    
    /* 3. Explore Categories */
    .section-title { font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 40px; color: var(--color-text); }
    .section-title .text-pink { color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none; }
    .section-title .text-blue { color: #3895c8; -webkit-text-fill-color: #3895c8; background: none; }
    .cat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; }
    .cat-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 16px;
      padding: 25px 20px;
      text-align: center;
      cursor: pointer;
      transition: all 0.3s;
      box-shadow: 0 5px 15px rgba(0,0,0,0.03);
    }
    .cat-card:hover { transform: translateY(-5px); border-color: #3895c8; box-shadow: 0 10px 20px rgba(56, 149, 200, 0.15); }
    .cat-card i { font-size: 2.5rem; color: var(--color-primary); margin-bottom: 15px; transition: 0.3s; }
    .cat-card:hover i { transform: scale(1.1); color: #3895c8; }
    .cat-card h4 { font-size: 1.1rem; color: var(--color-text); }
    
    /* 4. Blog Grid (Latest Articles) */
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
    .blog-card:hover { transform: translateY(-8px); box-shadow: 0 15px 40px rgba(0,0,0,0.1); }
    .blog-img { width: 100%; height: 200px; object-fit: cover; }
    .blog-content { padding: 25px; flex-grow: 1; display: flex; flex-direction: column; }
    .blog-meta { display: flex; justify-content: space-between; color: var(--color-text-light); font-size: 0.85rem; margin-bottom: 10px; }
    .blog-content h3 { font-size: 1.3rem; margin-bottom: 10px; color: var(--color-text); line-height: 1.4; }
    .blog-content p { color: var(--color-text-light); font-size: 0.95rem; margin-bottom: 20px; flex-grow: 1; }

    /* Empty state */
    .no-results { text-align: center; padding: 50px; font-size: 1.2rem; color: var(--color-text-light); width: 100%; grid-column: 1 / -1; }

    /* Other Sections */
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

    .gallery-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
    .gallery-grid img { width: 100%; height: 200px; object-fit: cover; border-radius: 12px; transition: transform 0.4s; cursor: pointer; }
    .gallery-grid img:hover { transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }
    
    .cta-final { background: var(--color-bg); padding: 80px 20px; text-align: center; border-top: 1px solid var(--color-border); }
    
    @media (max-width: 768px) {
      .featured-story { grid-template-columns: 1fr; }
      .featured-img-wrap { min-height: 250px; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <!-- 1. BLOG HERO -->
  <header class="blog-hero">
    <div class="container reveal">
      <h1><span class="gradient-text">Ideas That Make Every</span> <br><span class="text-blue">Celebration Magical</span></h1>
      <p>Discover inspiration, themes, expert planning tips, and fun activities to create unforgettable moments.</p>
    </div>
  </header>

  <!-- SEARCH & FILTER BAR -->
  <div class="filter-bar reveal">
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

  <main>
    <!-- 2. FEATURED STORY -->
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

    <!-- 3. EXPLORE CATEGORIES -->
    <section class="section-container reveal">
      <h2 class="section-title"><span class="text-pink">Explore</span> <span class="text-blue">Categories</span></h2>
      <div class="cat-grid">
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
    </section>

    <!-- 4, 5, 7, 8, 9. LATEST ARTICLES (Grid populated by JS) -->
    <section class="section-container reveal">
      <h2 class="section-title"><span class="text-pink">Latest</span> <span class="text-blue">Articles</span></h2>
      <div class="blog-grid" id="blog-grid">
        <!-- Rendered by JS -->
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
      <div class="newsletter-section">
        <h2 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 15px; color: var(--color-text);">A Little Magic in Your Inbox</h2>
        <p style="color: var(--color-text-light); font-size: 1.1rem; margin-bottom: 30px;">Subscribe to get the latest party themes, DIY ideas, and exclusive Magiqo offers.</p>
        <form style="display: flex; justify-content: center; flex-wrap: wrap; gap: 15px;" onsubmit="event.preventDefault(); this.innerHTML='<h3 style=\\'color:#10b981;\\'><i class=\\'fa-solid fa-check\\'></i> Subscribed Successfully!</h3>'">
          <input type="email" class="newsletter-input" placeholder="Enter your email address" required>
          <button type="submit" class="btn-subscribe">Subscribe <i class="fa-solid fa-paper-plane" style="margin-left: 5px;"></i></button>
        </form>
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
    // 20 Blog Articles Data
    const allBlogs = [
      { id: 1, title: "10 Reasons to Hire a Professional Magician", category: "Entertainers", img: "assets/images/hero_magician_1790831867453.jpg", date: "Oct 1, 2026", read: "5 min" },
      { id: 2, title: "How to Build a Superhero Obstacle Course", category: "Kids", img: "assets/images/superhero_party_1790842695325.jpg", date: "Sep 28, 2026", read: "4 min" },
      { id: 3, title: "DIY Princess Crowns for the Royal Court", category: "Themes", img: "assets/images/princess_party_1790842645232.jpg", date: "Sep 25, 2026", read: "6 min" },
      { id: 4, title: "The Ultimate Guide to Balloon Arch Decorations", category: "Decor", img: "assets/images/magic_show_party_1790842468826.jpg", date: "Sep 22, 2026", read: "7 min" },
      { id: 5, title: "5 Tips from Event Experts to Reduce Stress", category: "Planning", img: "assets/images/about_kids_birthday.jpg", date: "Sep 20, 2026", read: "5 min" },
      { id: 6, title: "Halloween Party Ideas That Are Spooky Not Scary", category: "Themes", img: "assets/images/cute_kids_clapping_1790833571210.jpg", date: "Sep 15, 2026", read: "4 min" },
      { id: 7, title: "Choosing the Right Clown for Toddlers", category: "Entertainers", img: "assets/images/james_boy_smile.jpg", date: "Sep 12, 2026", read: "3 min" },
      { id: 8, title: "Top 5 Party Favors Kids Actually Keep", category: "Planning", img: "assets/images/superhero_party_1790842695325.jpg", date: "Sep 10, 2026", read: "5 min" },
      { id: 9, title: "How Much Space Do You Need for an Indoor Show?", category: "Planning", img: "assets/images/magic_show_party_1790842468826.jpg", date: "Sep 8, 2026", read: "4 min" },
      { id: 10, title: "Eco-Friendly Party Decorations", category: "Decor", img: "assets/images/about_kids_birthday.jpg", date: "Sep 5, 2026", read: "6 min" },
      { id: 11, title: "The Best Board Games for an 8-Year-Old's Party", category: "Kids", img: "assets/images/princess_party_1790842645232.jpg", date: "Sep 1, 2026", read: "5 min" },
      { id: 12, title: "Summer Splash: Water-Themed Birthday Ideas", category: "Themes", img: "assets/images/james_boy_smile.jpg", date: "Aug 28, 2026", read: "4 min" },
      { id: 13, title: "Face Painting 101: Safe Paints for Kids", category: "Entertainers", img: "assets/images/hero_magician_1790831867453.jpg", date: "Aug 25, 2026", read: "6 min" },
      { id: 14, title: "How to Create a Photo Booth at Home", category: "Decor", img: "assets/images/cute_kids_clapping_1790833571210.jpg", date: "Aug 20, 2026", read: "5 min" },
      { id: 15, title: "Managing Food Allergies at a Children's Party", category: "Planning", img: "assets/images/about_kids_birthday.jpg", date: "Aug 15, 2026", read: "7 min" },
      { id: 16, title: "Fairy Garden Setup: A Magical Afternoon", category: "Themes", img: "assets/images/princess_party_1790842645232.jpg", date: "Aug 10, 2026", read: "4 min" },
      { id: 17, title: "Best Ice-Breaker Games for Shy Kids", category: "Kids", img: "assets/images/superhero_party_1790842695325.jpg", date: "Aug 5, 2026", read: "3 min" },
      { id: 18, title: "What to Look for When Hiring an Entertainer", category: "Entertainers", img: "assets/images/hero_magician_1790831867453.jpg", date: "Jul 28, 2026", read: "6 min" },
      { id: 19, title: "Winter Wonderland Party Ideas", category: "Themes", img: "assets/images/magic_show_party_1790842468826.jpg", date: "Jul 20, 2026", read: "5 min" },
      { id: 20, title: "How to Keep Adults Entertained at a Kid's Party", category: "Planning", img: "assets/images/james_boy_smile.jpg", date: "Jul 15, 2026", read: "4 min" }
    ];

    const grid = document.getElementById("blog-grid");
    const searchInput = document.getElementById("search-input");
    const filterBtns = document.querySelectorAll(".filter-btn");

    function renderBlogs(blogs) {
      grid.innerHTML = "";
      if (blogs.length === 0) {
        grid.innerHTML = '<div class="no-results">No articles found matching your criteria.</div>';
        return;
      }
      
      blogs.forEach(blog => {
        grid.innerHTML += `
          <div class="blog-card reveal active">
            <img src="${blog.img}" alt="${blog.title}" class="blog-img">
            <div class="blog-content">
              <span class="category-tag" style="margin-bottom:10px;">${blog.category}</span>
              <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html'">${blog.title}</h3>
              <div class="blog-meta">
                <span><i class="fa-regular fa-calendar"></i> ${blog.date}</span>
                <span><i class="fa-regular fa-clock"></i> ${blog.read}</span>
              </div>
              <a href="blog_detail.html" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>
        `;
      });
    }

    // Initial render
    renderBlogs(allBlogs);

    // Filtering Logic
    let currentFilter = 'all';
    
    function applyFilters() {
      const searchTerm = searchInput.value.toLowerCase();
      
      const filtered = allBlogs.filter(blog => {
        const matchesCat = (currentFilter === 'all') || (blog.category === currentFilter);
        const matchesSearch = blog.title.toLowerCase().includes(searchTerm);
        return matchesCat && matchesSearch;
      });
      
      renderBlogs(filtered);
    }

    filterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentFilter = btn.getAttribute("data-filter");
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
