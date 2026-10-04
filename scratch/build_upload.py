import os

html_content = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Real Moments - Magiqo Community Gallery</title>
  <meta name="description" content="Share your magical moments, photos, and videos with entertainers booked through Magiqo.">

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  
  <style>
    /* Specific styles for upload page */
    .hero-upload {
      position: relative;
      padding: 8rem 0 6rem;
      text-align: center;
      background: linear-gradient(135deg, var(--hero-bg-start), var(--hero-bg-end));
      overflow: hidden;
    }
    
    .masonry-gallery {
      column-count: 3;
      column-gap: 1.5rem;
    }
    @media (max-width: 992px) {
      .masonry-gallery { column-count: 2; }
    }
    @media (max-width: 576px) {
      .masonry-gallery { column-count: 1; }
    }
    
    .masonry-item {
      break-inside: avoid;
      margin-bottom: 1.5rem;
      border-radius: var(--radius-md);
      overflow: hidden;
      position: relative;
      background: var(--color-surface);
      box-shadow: 0 10px 20px var(--color-shadow);
      cursor: pointer;
      transition: transform 0.3s ease;
    }
    .masonry-item:hover { transform: translateY(-5px); }
    .masonry-item img {
      width: 100%;
      display: block;
    }
    .masonry-item-info {
      padding: 1rem;
    }
    
    .upload-zone {
      border: 2px dashed var(--color-primary);
      border-radius: var(--radius-lg);
      padding: 4rem 2rem;
      text-align: center;
      background: rgba(255,255,255,0.05);
      cursor: pointer;
      transition: background 0.3s ease;
      margin-bottom: 2rem;
    }
    .upload-zone:hover {
      background: rgba(255,255,255,0.1);
    }
    
    .form-control {
      width: 100%;
      padding: 1rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--color-border);
      background: var(--color-bg);
      color: var(--color-text);
      font-size: 1rem;
      margin-bottom: 1rem;
    }
    
    .category-card {
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 10px 20px var(--color-shadow);
      text-align: center;
      transition: transform 0.3s ease;
    }
    .category-card:hover { transform: translateY(-10px); }
    
    .feature-card {
      display: flex;
      background: var(--color-surface);
      border-radius: var(--radius-lg);
      overflow: hidden;
      margin-bottom: 3rem;
      box-shadow: 0 15px 30px var(--color-shadow);
    }
    @media (max-width: 768px) {
      .feature-card { flex-direction: column; }
    }
  </style>
</head>

<body>

  <!-- Dynamic Navbar -->
  <div id="navbar"></div>

  <!-- 01. Hero Section -->
  <section class="hero-upload">
    <div class="container" style="position: relative; z-index: 2;">
      <h1 style="font-family: var(--font-magic); font-size: clamp(3rem, 5vw, 5rem); margin-bottom: 1rem;">
        <span style="color: var(--color-primary);">Every Moment</span> 
        <span style="color: #3895c8;">Has a Story</span>
      </h1>
      <p style="font-size: 1.25rem; color: var(--color-text-light); max-width: 600px; margin: 0 auto 2.5rem; line-height: 1.6;">
        Join our community gallery. Share your magical memories, photos, and videos of celebrations brought to life by Magiqo entertainers.
      </p>
      <a href="#upload-form" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2.5rem;">Share Your Moment</a>
    </div>
  </section>

  <!-- 02. Moments That Matter (Community Gallery) -->
  <section id="gallery" style="padding: 6rem 0; background: var(--color-bg);">
    <div class="container">
      <div class="section-title text-center" style="font-family: var(--font-magic);">
        <span style="color: var(--color-primary);">Moments</span> <span style="color: #3895c8;">That Matter</span>
      </div>
      <div class="section-subtitle text-center">Real smiles, real magic, shared by you.</div>
      
      <div class="masonry-gallery" style="margin-top: 3rem;">
        <div class="masonry-item" onclick="openLightbox('assets/images/magic_show_party_1790842468826.jpg', 'The kids couldn\\'t stop laughing! Best magician ever.')">
          <img src="assets/images/magic_show_party_1790842468826.jpg" alt="Magic Show">
          <div class="masonry-item-info">
            <h4 style="color:var(--color-primary); font-size:1.1rem; margin-bottom:0.5rem;">Leo's 6th Birthday</h4>
            <p style="color:var(--color-text-light); font-size:0.9rem; font-style:italic;">"The kids couldn't stop laughing! Best magician ever."</p>
            <div style="margin-top:0.5rem; font-size:0.8rem; color:#888;">Entertainer: The Great Magic Show</div>
          </div>
        </div>
        <div class="masonry-item" onclick="openLightbox('assets/images/princess_party_1790842645232.jpg', 'A truly royal experience.')">
          <img src="assets/images/princess_party_1790842645232.jpg" alt="Princess Party">
          <div class="masonry-item-info">
            <h4 style="color:var(--color-primary); font-size:1.1rem; margin-bottom:0.5rem;">Mia's Royal Tea</h4>
            <p style="color:var(--color-text-light); font-size:0.9rem; font-style:italic;">"A truly royal experience."</p>
            <div style="margin-top:0.5rem; font-size:0.8rem; color:#888;">Entertainer: Royal Princess</div>
          </div>
        </div>
        <div class="masonry-item" onclick="openLightbox('assets/images/party_moments_2_1790918669697.jpg', 'So much fun and joy!')">
          <img src="assets/images/party_moments_2_1790918669697.jpg" alt="Party Moments">
          <div class="masonry-item-info">
            <h4 style="color:var(--color-primary); font-size:1.1rem; margin-bottom:0.5rem;">Summer Bash</h4>
            <p style="color:var(--color-text-light); font-size:0.9rem; font-style:italic;">"So much fun and joy!"</p>
            <div style="margin-top:0.5rem; font-size:0.8rem; color:#888;">Entertainer: Close-Up Magic</div>
          </div>
        </div>
        <div class="masonry-item" onclick="openLightbox('assets/images/superhero_party_1790842695325.jpg', 'Action packed!')">
          <img src="assets/images/superhero_party_1790842695325.jpg" alt="Superhero Party">
          <div class="masonry-item-info">
            <h4 style="color:var(--color-primary); font-size:1.1rem; margin-bottom:0.5rem;">Hero Training</h4>
            <p style="color:var(--color-text-light); font-size:0.9rem; font-style:italic;">"Action packed!"</p>
            <div style="margin-top:0.5rem; font-size:0.8rem; color:#888;">Entertainer: Ultimate Hero</div>
          </div>
        </div>
        <div class="masonry-item" onclick="openLightbox('assets/images/clown_party_1790842566084.jpg', 'Balloons everywhere!')">
          <img src="assets/images/clown_party_1790842566084.jpg" alt="Clowns">
          <div class="masonry-item-info">
            <h4 style="color:var(--color-primary); font-size:1.1rem; margin-bottom:0.5rem;">Toddler Fun</h4>
            <p style="color:var(--color-text-light); font-size:0.9rem; font-style:italic;">"Balloons everywhere!"</p>
            <div style="margin-top:0.5rem; font-size:0.8rem; color:#888;">Entertainer: Silly Clowns</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 03. Share Your Moment (Upload Form) -->
  <section id="upload-form" style="padding: 6rem 0; background: var(--color-surface);">
    <div class="container" style="max-width: 800px;">
      <div class="section-title text-center" style="font-family: var(--font-magic);">
        <span style="color: var(--color-primary);">Share Your</span> <span style="color: #3895c8;">Moment</span>
      </div>
      
      <form style="margin-top: 3rem;" onsubmit="event.preventDefault(); alert('Submission simulated successfully! Real uploads require a backend.');">
        <div class="upload-zone">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom:1rem;">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="17 8 12 3 7 8"></polyline>
            <line x1="12" y1="3" x2="12" y2="15"></line>
          </svg>
          <h3 style="color:var(--color-text); font-size:1.5rem; margin-bottom:0.5rem;">Drag & Drop Photos/Videos</h3>
          <p style="color:var(--color-text-light);">or click to browse files</p>
        </div>
        
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem;">
          <input type="text" class="form-control" placeholder="Event Title (e.g. Leo's 6th Birthday)" required>
          <input type="text" class="form-control" placeholder="Your Name" required>
        </div>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem;">
          <select class="form-control" required>
            <option value="">Select Event Category</option>
            <option>Kids Party</option>
            <option>Wedding</option>
            <option>Corporate Event</option>
            <option>Special Celebration</option>
          </select>
          <input type="text" class="form-control" placeholder="Entertainer Name (if known)">
        </div>
        <textarea class="form-control" rows="4" placeholder="Tell us about the magic! Add a caption..." required></textarea>
        
        <div style="margin-bottom: 2rem; display: flex; align-items: flex-start; gap: 0.5rem;">
          <input type="checkbox" id="consent" required style="margin-top: 0.3rem;">
          <label for="consent" style="color:var(--color-text-light); font-size:0.9rem; line-height:1.5;">
            I confirm I have permission to share these images/videos, including permission from any identifiable individuals, and I agree to the <a href="#guidelines" style="color:var(--color-primary);">Upload Guidelines</a>.
          </label>
        </div>
        
        <button type="submit" class="btn btn-primary" style="width: 100%; font-size: 1.125rem; padding: 1rem;">Submit for Review</button>
      </form>
    </div>
  </section>

  <!-- 04. Choose Your Celebration -->
  <section id="categories" style="padding: 6rem 0; background: var(--color-bg);">
    <div class="container">
      <div class="section-title text-center" style="font-family: var(--font-magic);">
        <span style="color: var(--color-primary);">Explore by</span> <span style="color: #3895c8;">Category</span>
      </div>
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:2rem; margin-top:3rem;">
        <div class="category-card">
          <img src="assets/images/kids_clapping_party_1790917531872.jpg" style="width:100%; height:180px; object-fit:cover;">
          <div style="padding: 1.5rem;">
            <h3 style="color:var(--color-primary); font-family:var(--font-magic); font-size:1.5rem;">Kids' Parties</h3>
          </div>
        </div>
        <div class="category-card">
          <img src="assets/images/party_moments_2_1790918669697.jpg" style="width:100%; height:180px; object-fit:cover;">
          <div style="padding: 1.5rem;">
            <h3 style="color:var(--color-primary); font-family:var(--font-magic); font-size:1.5rem;">Special Celebrations</h3>
          </div>
        </div>
        <div class="category-card">
          <img src="assets/images/blog_party_ideas_1790831919409.jpg" style="width:100%; height:180px; object-fit:cover;">
          <div style="padding: 1.5rem;">
            <h3 style="color:var(--color-primary); font-family:var(--font-magic); font-size:1.5rem;">Weddings & Events</h3>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 05. Stories Behind the Smiles -->
  <section id="featured" style="padding: 6rem 0; background: var(--color-surface);">
    <div class="container">
      <div class="section-title text-center" style="font-family: var(--font-magic);">
        <span style="color: var(--color-primary);">Stories Behind</span> <span style="color: #3895c8;">The Smiles</span>
      </div>
      <div class="section-subtitle text-center" style="margin-bottom:4rem;">Featured moments from our incredible community.</div>
      
      <div class="feature-card">
        <div style="flex:1; min-height:300px;">
          <img src="assets/images/magic_show_party_1790842468826.jpg" style="width:100%; height:100%; object-fit:cover;">
        </div>
        <div style="flex:1; padding:3rem; display:flex; flex-direction:column; justify-content:center;">
          <div style="color:var(--color-primary); font-weight:600; text-transform:uppercase; letter-spacing:1px; margin-bottom:1rem;">Featured Event</div>
          <h3 style="font-size:2rem; margin-bottom:1rem; font-family:var(--font-magic);">The Incredible Magic Show</h3>
          <p style="color:var(--color-text-light); line-height:1.7; margin-bottom:1.5rem; font-style:italic;">
            "We were blown away by the level of engagement! The magician had every single child completely focused and laughing for an entire hour. It made our son's birthday truly unforgettable."
          </p>
          <div style="color:#888; font-size:0.9rem;">- Shared by The Anderson Family</div>
        </div>
      </div>
    </div>
  </section>

  <!-- 06. The Entertainer Spotlight -->
  <section id="spotlight" style="padding: 6rem 0; background: var(--color-bg);">
    <div class="container">
      <div class="section-title text-center" style="font-family: var(--font-magic);">
        <span style="color: var(--color-primary);">Entertainer</span> <span style="color: #3895c8;">Spotlight</span>
      </div>
      <div style="text-align:center; max-width:600px; margin:0 auto 3rem; color:var(--color-text-light);">
        Discover the talented professionals making these moments possible. Browse memories by your favorite entertainer.
      </div>
      <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
        <a href="packages.html" class="btn btn-outline" style="border-radius:50px;">The Great Magic Show</a>
        <a href="packages.html" class="btn btn-outline" style="border-radius:50px;">Royal Princess</a>
        <a href="packages.html" class="btn btn-outline" style="border-radius:50px;">Ultimate Hero</a>
        <a href="packages.html" class="btn btn-outline" style="border-radius:50px;">Silly Clowns</a>
      </div>
    </div>
  </section>

  <!-- 08. Your Memories, Our Inspiration -->
  <section style="padding: 6rem 0; background: var(--color-surface); text-align:center;">
    <div class="container" style="max-width:800px;">
      <h2 style="font-family: var(--font-magic); font-size:2.5rem; margin-bottom: 2rem;">
        <span style="color: var(--color-primary);">Your Memories,</span> <span style="color: #3895c8;">Our Inspiration</span>
      </h2>
      <p style="font-size: 1.25rem; color: var(--color-text-light); line-height: 1.8; font-style:italic;">
        "Seeing the joy and wonder in these shared moments is what drives us. Thank you to every family and community member who allows us to be a part of their special celebrations."
      </p>
      <div style="margin-top: 2rem; color: var(--color-text); font-weight:bold;">- The Magiqo Team</div>
    </div>
  </section>

  <!-- 09. Before You Share (Guidelines) -->
  <section id="guidelines" style="padding: 6rem 0; background: var(--color-bg);">
    <div class="container" style="max-width:800px;">
      <h3 style="font-size:1.75rem; color:var(--color-primary); margin-bottom:2rem; font-family:var(--font-magic);">Upload Guidelines & Privacy</h3>
      <div style="background:var(--color-surface); padding:2.5rem; border-radius:var(--radius-md); border-left:4px solid var(--color-primary);">
        <ul style="color:var(--color-text-light); line-height:1.8; padding-left:1.5rem; margin:0;">
          <li><strong>File Formats:</strong> JPG, PNG, MP4 accepted. Max size 20MB per file.</li>
          <li><strong>Content Moderation:</strong> All submissions are reviewed by our team before publishing to ensure community safety.</li>
          <li><strong>Consent is Key:</strong> Ensure you have explicit permission from anyone clearly visible in your photos/videos before sharing.</li>
          <li><strong>Privacy First:</strong> We will never sell your photos or use them for external marketing without separate written consent.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- 10. CTA -->
  <section style="padding: 6rem 0; text-align:center; background: linear-gradient(135deg, rgba(183, 36, 92, 0.1), rgba(56, 149, 200, 0.1));">
    <div class="container">
      <h2 style="font-family: var(--font-magic); font-size:3rem; margin-bottom:1.5rem;">
        <span style="color: var(--color-primary);">Let's Make</span> <span style="color: #3895c8;">More Memories</span>
      </h2>
      <p style="color:var(--color-text-light); font-size:1.1rem; margin-bottom:2rem;">Ready to create unforgettable moments?</p>
      <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
        <a href="#upload-form" class="btn btn-primary" style="padding:1rem 2rem;">Upload a Memory</a>
        <a href="packages.html" class="btn btn-outline" style="padding:1rem 2rem;">Book an Entertainer</a>
      </div>
    </div>
  </section>

  <!-- 07. Lightbox Modal -->
  <div id="lightbox" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:9999; align-items:center; justify-content:center; padding:20px; backdrop-filter: blur(8px);">
    <div style="background:var(--color-surface); border-radius:var(--radius-lg); overflow:hidden; display:flex; flex-wrap:wrap; max-width:900px; width:100%; position:relative; box-shadow: 0 25px 50px rgba(0,0,0,0.5);">
      <button onclick="document.getElementById('lightbox').style.display='none'" style="position:absolute; top:15px; right:20px; background:rgba(255,255,255,0.8); border:none; font-size:1.5rem; color:#111; cursor:pointer; width:40px; height:40px; border-radius:50%; z-index:10; display:flex; align-items:center; justify-content:center;">&times;</button>
      <div style="flex:1; min-width:300px;">
        <img id="lightboxImg" src="" alt="Moment" style="width:100%; height:100%; object-fit:cover; display:block; min-height:300px; max-height: 70vh;">
      </div>
      <div style="flex:1; padding:3rem; display:flex; flex-direction:column; justify-content:center; min-width:300px;">
        <h3 style="font-family:var(--font-magic); font-size:2.5rem; color:var(--color-primary); margin-bottom:1rem;">Community Memory</h3>
        <p id="lightboxDesc" style="color:var(--color-text-light); font-size:1.1rem; line-height:1.6; font-style:italic;">""</p>
      </div>
    </div>
  </div>

  <script>
    function openLightbox(imgUrl, desc) {
      document.getElementById('lightboxImg').src = imgUrl;
      document.getElementById('lightboxDesc').innerText = '"' + desc + '"';
      document.getElementById('lightbox').style.display = 'flex';
    }
  </script>

  <script src="js/components.js"></script>

</body>
</html>
"""

with open('c:/Users/vigas/Desktop/magiqo/upload.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("done")
