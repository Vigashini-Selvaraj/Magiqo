import re

def update_blog_detail():
    file_path = r'c:\Users\vigas\Desktop\magiqo\blog_detail.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure Google Fonts are included
    google_fonts = '''  <!-- Core Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">'''
    
    if 'family=Outfit' not in content:
        content = content.replace('<link rel="stylesheet" href="css/style.css">', google_fonts + '\n  <link rel="stylesheet" href="css/style.css">')

    # 2. Modernize style block
    style_replacement = '''  <style>
    body {
      background: var(--color-bg) !important;
      background-color: var(--color-bg) !important;
      color: var(--color-text);
      font-family: var(--font-body);
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }

    /* Hero & Cover */
    .blog-detail-hero {
      padding: 160px 20px 45px;
      text-align: center;
      background: radial-gradient(circle at 10% 20%, rgba(201, 42, 88, 0.08) 0%, transparent 45%),
                  radial-gradient(circle at 90% 80%, rgba(56, 149, 200, 0.08) 0%, transparent 45%),
                  var(--color-surface);
      border-bottom: 1px solid var(--color-border);
      position: relative;
    }

    .blog-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 22px;
      border-radius: var(--radius-pill);
      background: rgba(201, 42, 88, 0.08);
      color: var(--color-primary);
      border: 1px solid rgba(201, 42, 88, 0.25);
      font-weight: 700;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 22px;
    }

    .blog-title {
      font-family: var(--font-magic);
      font-size: clamp(2.4rem, 4.5vw, 4rem);
      font-weight: 900;
      line-height: 1.2;
      color: var(--color-text);
      max-width: 950px;
      margin: 0 auto 22px;
    }

    .blog-meta-hero {
      display: flex;
      justify-content: center;
      gap: 16px;
      color: var(--color-text-light);
      font-size: 0.95rem;
      font-weight: 600;
      flex-wrap: wrap;
    }

    .blog-meta-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--color-bg);
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--color-border);
    }

    .cover-image-container {
      max-width: 1100px;
      margin: 40px auto 60px;
      padding: 0 20px;
    }

    .cover-image-container img {
      width: 100%;
      height: 500px;
      object-fit: cover;
      border-radius: var(--radius-lg);
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.15);
      border: 4px solid var(--color-surface);
      background: var(--color-surface);
      display: block;
    }

    .section-title {
      font-family: var(--font-magic);
      font-size: clamp(2.2rem, 3.5vw, 3rem);
      font-weight: 800;
      text-align: center;
      margin-bottom: 40px;
      color: var(--color-text);
    }
    .text-pink {
      color: var(--color-primary) !important;
      -webkit-text-fill-color: var(--color-primary) !important;
      background: none !important;
    }
    .text-blue {
      color: #3895c8 !important;
      -webkit-text-fill-color: #3895c8 !important;
      background: none !important;
    }

    /* Layout */
    .article-container {
      max-width: 1100px;
      margin: 0 auto 80px;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 45px;
    }

    /* Content Styles */
    .article-content {
      color: var(--color-text);
      font-size: 1.15rem;
      line-height: 1.8;
    }
    .article-content h2, .article-content h3 {
      font-family: var(--font-magic);
      font-weight: 800;
      color: var(--color-text);
      margin: 40px 0 20px;
      line-height: 1.3;
    }
    .article-content h2 { font-size: 2.1rem; }
    .article-content h3 { font-size: 1.6rem; }
    .article-content p {
      margin-bottom: 22px;
      color: var(--color-text-light);
      line-height: 1.8;
      font-size: 1.1rem;
    }
    .article-content ul, .article-content ol {
      margin: 20px 0;
      padding-left: 24px;
      color: var(--color-text-light);
    }
    .article-content li {
      margin-bottom: 12px;
      line-height: 1.6;
    }

    .highlight-quote {
      background: linear-gradient(135deg, rgba(201, 42, 88, 0.08) 0%, rgba(56, 149, 200, 0.08) 100%);
      border-left: 5px solid var(--color-primary);
      padding: 30px 35px;
      border-radius: 0 var(--radius-lg) var(--radius-lg) 0;
      margin: 40px 0;
      font-size: 1.25rem;
      font-style: italic;
      color: var(--color-text);
      line-height: 1.7;
      border-top: 1px solid var(--color-border);
      border-right: 1px solid var(--color-border);
      border-bottom: 1px solid var(--color-border);
    }

    /* Sidebar (TOC & Share) */
    .sidebar { position: sticky; top: 110px; height: fit-content; }
    .toc-box {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 28px;
      margin-bottom: 30px;
      box-shadow: 0 10px 25px var(--color-shadow);
    }
    .toc-box h4 {
      font-family: var(--font-magic);
      font-size: 1.35rem;
      font-weight: 800;
      margin-bottom: 18px;
      border-bottom: 1px solid var(--color-border);
      padding-bottom: 12px;
      color: var(--color-text);
    }
    .toc-box ul { list-style: none; padding: 0; margin: 0; }
    .toc-box li { margin-bottom: 14px; }
    .toc-box a {
      color: var(--color-text-light);
      text-decoration: none;
      transition: color 0.3s, transform 0.3s;
      display: block;
      font-weight: 600;
      font-size: 0.95rem;
    }
    .toc-box a:hover {
      color: var(--color-primary);
      transform: translateX(6px);
    }

    .share-box {
      display: flex;
      gap: 12px;
      margin-top: 18px;
    }
    .share-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--color-bg);
      border: 1px solid var(--color-border);
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      color: var(--color-text) !important;
      font-size: 1.15rem;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      padding: 0;
      margin: 0;
    }
    .share-btn:hover {
      background: var(--color-primary) !important;
      color: white !important;
      border-color: var(--color-primary) !important;
      transform: translateY(-3px);
      box-shadow: 0 6px 15px rgba(201, 42, 88, 0.3);
    }
    .share-btn i {
      display: block !important;
      line-height: 1 !important;
    }

    /* Key Takeaways & Tips */
    .key-takeaways {
      background: rgba(56, 149, 200, 0.06);
      border: 1px solid rgba(56, 149, 200, 0.25);
      border-radius: var(--radius-lg);
      padding: 30px;
      margin: 40px 0;
    }
    .key-takeaways h4 {
      color: #3895c8;
      font-family: var(--font-magic);
      font-weight: 800;
      font-size: 1.35rem;
      margin-bottom: 15px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .key-takeaways ul {
      margin: 0;
      padding-left: 20px;
      color: var(--color-text);
    }
    .key-takeaways li {
      margin-bottom: 10px;
      line-height: 1.6;
    }

    /* Inspiration Gallery */
    .article-gallery { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 40px 0; }
    .article-gallery img {
      width: 100%;
      height: 250px;
      object-fit: cover;
      border-radius: var(--radius-md);
      box-shadow: 0 8px 20px var(--color-shadow);
      border: 1px solid var(--color-border);
      transition: transform 0.4s ease;
    }
    .article-gallery img:hover { transform: scale(1.03); }

    /* Author & Tags */
    .author-profile {
      display: flex;
      align-items: center;
      gap: 20px;
      background: var(--color-surface);
      padding: 28px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--color-border);
      margin-top: 50px;
      box-shadow: 0 10px 25px var(--color-shadow);
    }
    .author-profile img {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid var(--color-primary);
    }
    .author-info h4 {
      margin-bottom: 6px;
      font-family: var(--font-magic);
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--color-text);
    }
    .author-info p {
      color: var(--color-text-light);
      font-size: 0.95rem;
      margin-bottom: 0;
      line-height: 1.6;
    }

    .tags-section {
      margin-top: 30px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
    }
    .tag {
      padding: 8px 18px;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-pill);
      color: var(--color-text-light);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.3s;
    }
    .tag:hover {
      background: var(--color-primary);
      color: white;
      border-color: var(--color-primary);
      transform: translateY(-2px);
    }

    /* Related Articles */
    .related-section {
      max-width: 1100px;
      margin: 0 auto 80px;
      padding: 0 20px;
    }
    .related-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
    }
    .blog-card {
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      overflow: hidden;
      border: 1px solid var(--color-border);
      transition: transform 0.4s, box-shadow 0.4s;
      box-shadow: 0 10px 25px var(--color-shadow);
    }
    .blog-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 20px 40px rgba(0,0,0,0.15);
      border-color: rgba(201, 42, 88, 0.3);
    }
    .blog-img {
      width: 100%;
      height: 220px;
      object-fit: cover;
      display: block;
    }
    .blog-content {
      padding: 25px;
    }

    /* CTA Section */
    .cta-banner-section {
      background: linear-gradient(135deg, var(--color-primary) 0%, #8c1e3e 100%);
      padding: 5rem 2rem;
      border-radius: var(--radius-lg);
      color: white;
      text-align: center;
      margin: 0 auto 80px;
      max-width: 1100px;
      box-shadow: 0 20px 50px rgba(201, 42, 88, 0.25);
    }
    .cta-banner-section h2 {
      font-family: var(--font-magic);
      font-size: clamp(2.4rem, 4vw, 3.2rem);
      font-weight: 800;
      color: #FFFFFF !important;
      -webkit-text-fill-color: #FFFFFF !important;
      margin-bottom: 1rem;
    }
    .cta-banner-section p {
      color: rgba(255, 255, 255, 0.92);
      font-size: 1.2rem;
      max-width: 650px;
      margin: 0 auto 2.5rem;
      line-height: 1.6;
    }

    @media (max-width: 992px) {
      .article-container { grid-template-columns: 1fr; }
      .sidebar { position: static; margin-bottom: 40px; order: -1; }
      .cover-image-container img { height: 350px; }
      .article-gallery { grid-template-columns: 1fr; }
    }
  </style>'''

    # Replace <style>...</style>
    content = re.sub(r'<style>.*?</style>', style_replacement, content, flags=re.DOTALL)

    # 3. Update Hero HTML to include nice badges
    hero_html = '''  <!-- 1. BLOG HERO -->
  <header class="blog-detail-hero">
    <span class="blog-badge" id="dyn-category"><i class="fa-solid fa-sparkles"></i> Planning</span>
    <h1 class="blog-title" id="dyn-title"><span class="text-pink">5 Tips from</span> <span class="text-blue">Event Experts</span></h1>
    <div class="blog-meta-hero">
      <span class="blog-meta-item"><img src="assets/images/pro_magician_2.jpg" style="width:26px; height:26px; border-radius:50%; object-fit: cover;"> By Magiqo Experts</span>
      <span class="blog-meta-item"><i class="fa-regular fa-calendar"></i> Oct 2, 2026</span>
      <span class="blog-meta-item"><i class="fa-regular fa-clock"></i> 5 min read</span>
    </div>
  </header>'''

    content = re.sub(r'<!-- 1\. BLOG HERO -->\s*<header class="blog-detail-hero">.*?</header>', hero_html, content, flags=re.DOTALL)

    # 4. Update Cover Image Container to guarantee local image fallback
    cover_html = '''  <!-- 2. FEATURED COVER IMAGE -->
  <div class="cover-image-container reveal">
    <img src="assets/images/about_kids_birthday.jpg" id="dyn-img" alt="Cover Image" onerror="this.onerror=null; this.src='assets/images/about_kids_birthday.jpg';">
  </div>'''

    content = re.sub(r'<!-- 2\. FEATURED COVER IMAGE -->\s*<div class="cover-image-container reveal">.*?</div>', cover_html, content, flags=re.DOTALL)

    # 5. Replace broken unsplash in Inspiration gallery
    old_gal = '''      <!-- 6. INSPIRATION GALLERY -->
      <div class="article-gallery">
        <img src="assets/images/pro_princess.jpg" alt="Gallery 1">
        <img src="https://images.unsplash.com/photo-1608889476561-6242cfdbf622?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery 2">
      </div>'''

    new_gal = '''      <!-- 6. INSPIRATION GALLERY -->
      <div class="article-gallery">
        <img src="assets/images/pro_princess.jpg" alt="Gallery 1">
        <img src="assets/images/service_balloon_twisting.jpg" alt="Gallery 2">
      </div>'''
    content = content.replace(old_gal, new_gal)

    # 6. Replace author photo
    content = re.sub(
        r'<div class="author-profile">\s*<img src="https://images\.unsplash\.com/[^"]+".*?<div class="author-info">',
        '''<div class="author-profile">
        <img src="assets/images/founder_mark.jpg" alt="Author">
        <div class="author-info">''',
        content,
        flags=re.DOTALL
    )

    # 7. Replace Related Articles with local images and proper links
    related_html = '''  <!-- 11. RELATED ARTICLES -->
  <section class="related-section reveal">
    <h2 class="section-title"><span class="text-pink">Related</span> <span class="text-blue">Articles</span></h2>
    <div class="related-grid">
      <div class="blog-card" onclick="location.href='blog_detail.html?title=Winter%20Wonderland%20Party%20Ideas&cat=Themes&img=assets/images/pro_classic_magic.jpg'" style="cursor:pointer;">
        <img src="assets/images/pro_classic_magic.jpg" alt="Winter Wonderland Party Ideas" class="blog-img">
        <div class="blog-content">
          <span class="blog-badge" style="margin-bottom:12px;">Themes</span>
          <h3 style="color: var(--color-text); font-family: var(--font-magic); font-weight: 700; margin-bottom: 10px;">Winter Wonderland Party Ideas</h3>
          <p style="color: var(--color-text-light); font-size: 0.95rem;">Everything you need for an enchanting, snow-kissed celebration.</p>
        </div>
      </div>
      <div class="blog-card" onclick="location.href='blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained&cat=Planning&img=assets/images/family_holiday_party.jpg'" style="cursor:pointer;">
        <img src="assets/images/family_holiday_party.jpg" alt="How to Keep Adults Entertained" class="blog-img">
        <div class="blog-content">
          <span class="blog-badge" style="margin-bottom:12px;">Planning</span>
          <h3 style="color: var(--color-text); font-family: var(--font-magic); font-weight: 700; margin-bottom: 10px;">How to Keep Adults Entertained</h3>
          <p style="color: var(--color-text-light); font-size: 0.95rem;">Expert advice on balancing fun for all ages and family guests.</p>
        </div>
      </div>
      <div class="blog-card" onclick="location.href='blog_detail.html?title=Eco-Friendly%20Party%20Decorations&cat=Decor&img=assets/images/service_balloon_twisting.jpg'" style="cursor:pointer;">
        <img src="assets/images/service_balloon_twisting.jpg" alt="Eco-Friendly Party Decorations" class="blog-img">
        <div class="blog-content">
          <span class="blog-badge" style="margin-bottom:12px;">Decor</span>
          <h3 style="color: var(--color-text); font-family: var(--font-magic); font-weight: 700; margin-bottom: 10px;">Eco-Friendly Party Decorations</h3>
          <p style="color: var(--color-text-light); font-size: 0.95rem;">Celebrate responsibly with sustainable and reusable festive decor.</p>
        </div>
      </div>
    </div>
  </section>'''

    content = re.sub(r'<!-- 11\. RELATED ARTICLES -->\s*<section class="related-section reveal">.*?</section>', related_html, content, flags=re.DOTALL)

    # 8. Modernize CTA section
    cta_html = '''  <!-- 13. BOOKING CTA BANNER -->
  <section class="cta-banner-section reveal">
    <h2>Ready to Make Your Celebration <span style="color: #ffe6ee !important; -webkit-text-fill-color: #ffe6ee !important;">Magical</span>?</h2>
    <p>Let our verified entertainers and event creators bring your dream celebration to life with zero hassle.</p>
    <div style="display: flex; gap: 1.25rem; justify-content: center; flex-wrap: wrap;">
      <a href="booking.html" class="btn btn-white btn-lg"><i class="fa-solid fa-wand-magic-sparkles"></i> Book An Entertainer</a>
      <a href="packages.html" class="btn btn-outline-white btn-lg"><i class="fa-solid fa-gift"></i> View All Packages</a>
    </div>
  </section>'''

    content = re.sub(r'<!-- 13\. BOOKING CTA -->\s*<section class="cta-section".*?</section>', cta_html, content, flags=re.DOTALL)

    # 9. Update JS Dynamic Content loader
    dynamic_script = '''  <script>
    // Dynamic Content Loading from URL Parameters with Smart Fallback
    const urlParams = new URLSearchParams(window.location.search);
    let title = urlParams.get('title');
    let img = urlParams.get('img');
    let cat = urlParams.get('cat');

    const catFallbacks = {
      "planning": "assets/images/about_kids_birthday.jpg",
      "themes": "assets/images/pro_classic_magic.jpg",
      "entertainers": "assets/images/pro_magician_2.jpg",
      "decor": "assets/images/service_balloon_twisting.jpg",
      "kids": "assets/images/superhero_party_1790842695325.jpg"
    };

    if (cat && !title) {
      if (cat.toLowerCase().includes('plan')) {
        title = "5 Tips from Event Experts to Reduce Stress";
      } else if (cat.toLowerCase().includes('theme')) {
        title = "Winter Wonderland Party Ideas";
      } else if (cat.toLowerCase().includes('entertain')) {
        title = "10 Reasons to Hire a Professional Magician";
      }
    }

    if (!title) {
      title = "5 Tips from Event Experts to Reduce Stress";
    }
    if (!cat) {
      cat = "Planning";
    }

    const catKey = cat.toLowerCase();
    if (!img || img.includes('unsplash.com') || img.trim() === '') {
      if (catKey.includes('plan')) {
        img = "assets/images/about_kids_birthday.jpg";
      } else if (catFallbacks[catKey]) {
        img = catFallbacks[catKey];
      } else {
        img = "assets/images/about_kids_birthday.jpg";
      }
    }

    // Set Category Badges
    const badgeEl = document.getElementById('dyn-category');
    if (badgeEl) badgeEl.innerHTML = `<i class="fa-solid fa-sparkles"></i> ` + cat;
    const tagEl = document.getElementById('dyn-tag');
    if (tagEl) tagEl.textContent = cat;

    // Two-tone split heading for official Magiqo branding
    const words = title.split(' ');
    if (words.length > 1) {
      const mid = Math.ceil(words.length / 2);
      const pinkPart = words.slice(0, mid).join(' ');
      const bluePart = words.slice(mid).join(' ');
      document.getElementById('dyn-title').innerHTML = `<span class="text-pink">${pinkPart}</span> <span class="text-blue">${bluePart}</span>`;
    } else {
      document.getElementById('dyn-title').innerHTML = `<span class="text-pink">${title}</span>`;
    }
    document.getElementById('page-title').textContent = title + " | Magiqo Blog";

    // Set verified cover image with fail-safe error recovery
    const dynImg = document.getElementById('dyn-img');
    if (dynImg) {
      dynImg.src = img;
      dynImg.onerror = function() {
        this.onerror = null;
        this.src = 'assets/images/about_kids_birthday.jpg';
      };
    }

    // Update intro paragraph
    const introP = document.getElementById('intro-p');
    if (introP) {
      introP.textContent = `Welcome to our comprehensive guide on ${title.toLowerCase()}. Planning a memorable celebration can be overwhelming, but with the right ideas, proven strategies, and expert support, you can create effortless magic that children and families will cherish forever.`;
    }
  </script>'''

    content = re.sub(r'<script>\s*// Dynamic Content Loading from URL Parameters.*?</script>', dynamic_script, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated blog_detail.html with Magiqo UI design, Google fonts, two-tone titles, and verified local assets!")

if __name__ == '__main__':
    update_blog_detail()
