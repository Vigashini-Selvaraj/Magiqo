import os

filepath = r'c:\Users\vigas\Desktop\magiqo\blog_detail.html'

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="page-title">Blog Article | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* Hero & Cover */
    .blog-detail-hero {
      padding: 160px 20px 40px;
      text-align: center;
      background: var(--color-bg);
      position: relative;
    }
    .blog-badge {
      display: inline-block;
      padding: 6px 15px;
      border-radius: 50px;
      background: rgba(210, 75, 118, 0.1);
      color: var(--color-primary);
      font-weight: bold;
      font-size: 0.85rem;
      text-transform: uppercase;
      margin-bottom: 20px;
    }
    .blog-title {
      font-family: var(--font-heading);
      font-size: clamp(2.5rem, 4vw, 4rem);
      margin-bottom: 20px;
      color: var(--color-text);
      max-width: 1000px;
      margin: 0 auto 20px;
      line-height: 1.2;
    }
    .blog-meta-hero {
      display: flex;
      justify-content: center;
      gap: 20px;
      color: var(--color-text-light);
      font-size: 1rem;
      flex-wrap: wrap;
    }
    .blog-meta-hero span { display: flex; align-items: center; gap: 8px; }
    
    .cover-image-container {
      max-width: 1200px;
      margin: 0 auto 60px;
      padding: 0 20px;
    }
    .cover-image-container img {
      width: 100%;
      height: 500px;
      object-fit: cover;
      border-radius: 24px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }

    /* Layout */
    .article-container {
      max-width: 1200px;
      margin: 0 auto 80px;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 1fr 350px;
      gap: 50px;
    }
    
    /* Content Styles */
    .article-content {
      color: var(--color-text);
      font-size: 1.15rem;
      line-height: 1.8;
    }
    .article-content h2, .article-content h3 {
      font-family: var(--font-heading);
      color: var(--color-text);
      margin: 40px 0 20px;
    }
    .article-content h2 { font-size: 2.2rem; }
    .article-content h3 { font-size: 1.6rem; }
    .article-content p { margin-bottom: 20px; color: var(--color-text-light); }
    .article-content ul, .article-content ol { margin: 20px 0; padding-left: 20px; color: var(--color-text-light); }
    .article-content li { margin-bottom: 10px; }
    
    .highlight-quote {
      background: linear-gradient(135deg, rgba(210, 75, 118, 0.05), rgba(56, 149, 200, 0.05));
      border-left: 5px solid var(--color-primary);
      padding: 30px;
      border-radius: 0 16px 16px 0;
      margin: 40px 0;
      font-size: 1.3rem;
      font-style: italic;
      color: var(--color-text);
    }
    
    /* Sidebar (TOC & Share) */
    .sidebar { position: sticky; top: 100px; height: fit-content; }
    .toc-box {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 16px;
      padding: 30px;
      margin-bottom: 30px;
    }
    .toc-box h4 { font-size: 1.3rem; margin-bottom: 20px; border-bottom: 1px solid var(--color-border); padding-bottom: 10px; }
    .toc-box ul { list-style: none; padding: 0; margin: 0; }
    .toc-box li { margin-bottom: 15px; }
    .toc-box a { color: var(--color-text-light); text-decoration: none; transition: 0.3s; display: block; }
    .toc-box a:hover { color: var(--color-primary); transform: translateX(5px); }

    .share-box {
      display: flex;
      gap: 15px;
      margin-top: 20px;
    }
    .share-btn {
      width: 45px;
      height: 45px;
      border-radius: 50%;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-text);
      font-size: 1.2rem;
      cursor: pointer;
      transition: 0.3s;
      text-decoration: none;
    }
    .share-btn:hover { background: var(--color-primary); color: white; border-color: var(--color-primary); transform: translateY(-3px); }

    /* Takeaways & Tips */
    .key-takeaways {
      background: rgba(56, 149, 200, 0.05);
      border: 1px solid rgba(56, 149, 200, 0.2);
      border-radius: 16px;
      padding: 30px;
      margin: 40px 0;
    }
    .key-takeaways h4 { color: #3895c8; font-size: 1.4rem; margin-bottom: 15px; display: flex; align-items: center; gap: 10px; }
    
    /* Inspiration Gallery */
    .article-gallery { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 40px 0; }
    .article-gallery img { width: 100%; height: 250px; object-fit: cover; border-radius: 12px; cursor: pointer; transition: 0.3s; }
    .article-gallery img:hover { transform: scale(1.03); }

    /* Author & Tags */
    .author-profile {
      display: flex;
      align-items: center;
      gap: 20px;
      background: var(--color-surface);
      padding: 30px;
      border-radius: 16px;
      border: 1px solid var(--color-border);
      margin-top: 50px;
    }
    .author-profile img { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; }
    .author-info h4 { margin-bottom: 5px; font-size: 1.2rem; }
    .author-info p { color: var(--color-text-light); font-size: 0.95rem; margin-bottom: 0; }

    .tags-section { margin-top: 30px; display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
    .tag { padding: 8px 15px; background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 50px; color: var(--color-text-light); text-decoration: none; font-size: 0.9rem; transition: 0.3s; }
    .tag:hover { background: var(--color-primary); color: white; border-color: var(--color-primary); }

    /* Related Articles */
    .related-section { max-width: 1200px; margin: 0 auto 80px; padding: 0 20px; }
    .related-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
    .blog-card { background: var(--color-surface); border-radius: 20px; overflow: hidden; border: 1px solid var(--color-border); transition: transform 0.4s; }
    .blog-card:hover { transform: translateY(-8px); box-shadow: 0 15px 40px rgba(0,0,0,0.1); }
    .blog-img { width: 100%; height: 200px; object-fit: cover; }
    .blog-content { padding: 25px; }
    
    @media (max-width: 992px) {
      .article-container { grid-template-columns: 1fr; }
      .sidebar { position: static; margin-bottom: 40px; order: -1; }
      .cover-image-container img { height: 350px; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <!-- 1. BLOG HERO -->
  <header class="blog-detail-hero">
    <span class="blog-badge" id="dyn-category">Category</span>
    <h1 class="blog-title" id="dyn-title">Article Title</h1>
    <div class="blog-meta-hero">
      <span><img src="assets/images/james_boy_smile.jpg" style="width:30px; height:30px; border-radius:50%;"> By Magiqo Experts</span>
      <span><i class="fa-regular fa-calendar"></i> Oct 2, 2026</span>
      <span><i class="fa-regular fa-clock"></i> 5 min read</span>
    </div>
  </header>

  <!-- 2. FEATURED COVER IMAGE -->
  <div class="cover-image-container reveal">
    <img src="assets/images/magic_show_party_1790842468826.jpg" id="dyn-img" alt="Cover Image">
  </div>

  <!-- MAIN ARTICLE CONTAINER -->
  <div class="article-container reveal">
    
    <!-- Left Column: Content -->
    <main class="article-content">
      
      <p id="intro-p">Welcome to our ultimate guide! Planning a memorable celebration can be overwhelming, but with the right ideas and expert advice, you can create magic effortlessly. In this article, we dive deep into the best strategies and themes that will leave everyone amazed.</p>

      <h2 id="section-1">1. Setting the Stage for Magic</h2>
      <p>Every great event starts with a solid foundation. You need to consider the venue space, lighting, and overall atmosphere. If you are hosting indoors, ensure there's enough room for entertainers and activities. Creating a designated "magic zone" can help focus the kids' attention and make the performance feel like a real stage show.</p>

      <!-- 5. KEY TAKEAWAYS -->
      <div class="key-takeaways">
        <h4><i class="fa-solid fa-lightbulb"></i> Key Takeaways</h4>
        <ul>
          <li>Always plan your space before booking an entertainer.</li>
          <li>Keep the guest list manageable to ensure a personalized experience.</li>
          <li>Incorporate interactive elements that keep kids engaged.</li>
        </ul>
      </div>

      <h2 id="section-2">2. Choosing the Right Activities</h2>
      <p>While the main event is crucial, having engaging side activities keeps the momentum going. Consider simple DIY crafts, photo booths with fun props, or interactive games that match your theme. The goal is to minimize downtime so that the children are always engaged.</p>

      <!-- HIGHLIGHT QUOTE -->
      <blockquote class="highlight-quote">
        "The secret to a perfect party isn't just the cake or the presents—it's the continuous flow of magical moments that keep children enchanted from start to finish."
      </blockquote>

      <h2 id="section-3">3. Decor That Dazzles</h2>
      <p>Your decorations set the tone. Use colors that pop and consider elements like balloon arches, themed banners, and interactive backdrops. Even simple changes like dimming the main lights and adding colorful LED up-lighting can completely transform a living room.</p>
      
      <!-- 6. INSPIRATION GALLERY -->
      <div class="article-gallery">
        <img src="assets/images/princess_party_1790842645232.jpg" alt="Gallery 1">
        <img src="assets/images/superhero_party_1790842695325.jpg" alt="Gallery 2">
      </div>

      <!-- 7. EXPERT TIPS -->
      <h3 id="section-4">Expert Tips & Recommendations</h3>
      <ul>
        <li><strong>Timings:</strong> Keep the party to about 2 hours for younger kids to avoid exhaustion.</li>
        <li><strong>Food:</strong> Opt for bite-sized, easy-to-eat snacks rather than sit-down meals.</li>
        <li><strong>Music:</strong> Create a playlist that matches your theme and play it softly in the background during transitions.</li>
      </ul>

      <!-- 8. AUTHOR PROFILE -->
      <div class="author-profile">
        <img src="assets/images/james_boy_smile.jpg" alt="Author">
        <div class="author-info">
          <h4>Written by Magiqo Events Team</h4>
          <p>Our team of seasoned event planners and entertainers share their years of experience to help you host unforgettable, stress-free celebrations.</p>
        </div>
      </div>

      <!-- 10. TAGS -->
      <div class="tags-section">
        <strong>Tags:</strong>
        <a href="#" class="tag">Party Planning</a>
        <a href="#" class="tag" id="dyn-tag">Themes</a>
        <a href="#" class="tag">Kids Events</a>
      </div>

    </main>

    <!-- Right Column: Sidebar -->
    <aside class="sidebar">
      <!-- 4. TABLE OF CONTENTS -->
      <div class="toc-box">
        <h4>Table of Contents</h4>
        <ul>
          <li><a href="#section-1">1. Setting the Stage for Magic</a></li>
          <li><a href="#section-2">2. Choosing the Right Activities</a></li>
          <li><a href="#section-3">3. Decor That Dazzles</a></li>
          <li><a href="#section-4">Expert Tips & Recommendations</a></li>
        </ul>
      </div>

      <!-- 9. SHARE THIS ARTICLE -->
      <div class="toc-box">
        <h4>Share This Article</h4>
        <p style="color: var(--color-text-light); font-size: 0.95rem; margin-bottom: 10px;">Love these ideas? Share the magic with other parents!</p>
        <div class="share-box">
          <a href="#" class="share-btn" title="Share on Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="#" class="share-btn" title="Share on Twitter"><i class="fa-brands fa-twitter"></i></a>
          <a href="#" class="share-btn" title="Share on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          <button class="share-btn" title="Copy Link" onclick="alert('Link copied to clipboard!')"><i class="fa-solid fa-link"></i></button>
        </div>
      </div>
    </aside>
  </div>

  <!-- 11. RELATED ARTICLES -->
  <section class="related-section reveal">
    <h2 class="section-title"><span class="text-pink">Related</span> <span class="text-blue">Articles</span></h2>
    <div class="related-grid">
      <div class="blog-card" onclick="location.href='blog_detail.html?title=Winter%20Wonderland%20Party%20Ideas&cat=Themes&img=assets/images/magic_show_party_1790842468826.jpg'" style="cursor:pointer;">
        <img src="assets/images/magic_show_party_1790842468826.jpg" alt="Related" class="blog-img">
        <div class="blog-content">
          <span class="blog-badge" style="margin-bottom:10px;">Themes</span>
          <h3 style="color: var(--color-text); margin-bottom: 10px;">Winter Wonderland Party Ideas</h3>
          <p style="color: var(--color-text-light);">Everything you need for a snowy celebration.</p>
        </div>
      </div>
      <div class="blog-card" onclick="location.href='blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained&cat=Planning&img=assets/images/james_boy_smile.jpg'" style="cursor:pointer;">
        <img src="assets/images/james_boy_smile.jpg" alt="Related" class="blog-img">
        <div class="blog-content">
          <span class="blog-badge" style="margin-bottom:10px;">Planning</span>
          <h3 style="color: var(--color-text); margin-bottom: 10px;">How to Keep Adults Entertained</h3>
          <p style="color: var(--color-text-light);">Expert advice on balancing fun for all ages.</p>
        </div>
      </div>
      <div class="blog-card" onclick="location.href='blog_detail.html?title=Eco-Friendly%20Party%20Decorations&cat=Decor&img=assets/images/about_kids_birthday.jpg'" style="cursor:pointer;">
        <img src="assets/images/about_kids_birthday.jpg" alt="Related" class="blog-img">
        <div class="blog-content">
          <span class="blog-badge" style="margin-bottom:10px;">Decor</span>
          <h3 style="color: var(--color-text); margin-bottom: 10px;">Eco-Friendly Party Decorations</h3>
          <p style="color: var(--color-text-light);">Party responsibly without sacrificing the fun.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 12. NEWSLETTER SUBSCRIPTION -->
  <section class="related-section reveal">
    <div style="background: linear-gradient(135deg, rgba(210, 75, 118, 0.1), rgba(56, 149, 200, 0.1)); border-radius: 24px; padding: 60px 30px; text-align: center; border: 1px solid rgba(56, 149, 200, 0.2);">
      <h2 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 15px; color: var(--color-text);">More Magic in Your Inbox</h2>
      <p style="color: var(--color-text-light); font-size: 1.1rem; margin-bottom: 30px;">Subscribe to receive more celebration ideas, expert planning tips, and exclusive Magiqo offers.</p>
      <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 15px;" id="nl-form-detail">
        <input type="email" placeholder="Enter your email address" style="padding: 15px 25px; border-radius: 50px; border: 1px solid rgba(0,0,0,0.1); width: 100%; max-width: 400px; font-size: 1rem; background: var(--color-surface); color: var(--color-text);">
        <button type="button" class="btn btn-primary" onclick="document.getElementById('nl-form-detail').innerHTML='<h3 style=\\'color:#10b981;\\'><i class=\\'fa-solid fa-circle-check\\'></i> Subscribed Successfully!</h3>'" style="padding: 15px 35px; border-radius: 50px; border: none; font-weight: bold; font-size: 1rem; cursor: pointer;">Subscribe <i class="fa-solid fa-paper-plane" style="margin-left: 5px;"></i></button>
      </div>
    </div>
  </section>

  <!-- 13. BOOKING CTA -->
  <section class="cta-section" style="background: var(--color-primary); padding: 6rem 0; text-align: center;">
    <div class="container text-center" style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
      <div class="sec-title" style="margin-bottom: 2rem;">
        <h2 style="color: white !important; -webkit-text-fill-color: white !important; background: none !important; font-family: var(--font-magic); font-size: 3rem;">Ready to Make Your Celebration Magical?</h2>
      </div>
      <p style="font-size: 1.25rem; max-width: 600px; margin: 0 auto 3rem; line-height: 1.6; color: rgba(255,255,255,0.9);">
        Let our expert entertainers and event planners bring your vision to life.
      </p>
      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
        <a href="booking.html" class="btn" style="background: white; color: var(--color-primary); padding: 1.25rem 3rem; font-size: 1.125rem; border-radius: 50px; font-weight: bold; text-decoration: none; display:inline-block; transition: 0.3s; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">Book Now</a>
      </div>
    </div>
  </section>

  <!-- 14. FOOTER -->
  <div id="footer"></div>

  <script src="js/components.js"></script>
  <script src="js/theme.js"></script>
  <script>
    // Dynamic Content Loading from URL Parameters
    const urlParams = new URLSearchParams(window.location.search);
    const title = urlParams.get('title');
    const img = urlParams.get('img');
    const cat = urlParams.get('cat');

    if (title) {
      document.getElementById('dyn-title').textContent = title;
      document.getElementById('page-title').textContent = title + " | Magiqo Blog";
      // Update intro text slightly based on title for realism
      document.getElementById('intro-p').textContent = `Welcome to our comprehensive guide on ${title.toLowerCase()}. Planning a memorable celebration can be overwhelming, but with the right ideas and expert advice, you can create magic effortlessly.`;
    }
    if (img) {
      document.getElementById('dyn-img').src = img;
    }
    if (cat) {
      document.getElementById('dyn-category').textContent = cat;
      document.getElementById('dyn-tag').textContent = cat;
    }
  </script>
</body>
</html>
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_content)
