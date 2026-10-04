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
    :root {
      --color-tertiary: #8E44AD; /* Purple color requested */
    }
  
    /* Specific styles for upload page */
    .hero-upload {
      position: relative;
      padding: 10rem 0 8rem;
      text-align: center;
      background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('assets/images/party_moments_2_1790918669697.jpg') center/cover;
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
    
    .inspiration-card {
      background: linear-gradient(135deg, var(--color-tertiary), var(--color-primary));
      border-radius: var(--radius-xl);
      padding: 4rem;
      color: white;
      box-shadow: 0 20px 40px var(--color-shadow);
      position: relative;
      overflow: hidden;
    }
    .inspiration-card::before {
      content: '"';
      position: absolute;
      top: -20px;
      left: 20px;
      font-size: 15rem;
      color: rgba(255,255,255,0.1);
      font-family: var(--font-magic);
      line-height: 1;
    }
  </style>
</head>

<body>

  <!-- Dynamic Navbar -->
  <div id="navbar"></div>

  <!-- 01. Hero Section -->
  <section class="hero-upload">
    <div class="container" style="position: relative; z-index: 2;">
      <h1 style="font-family: var(--font-magic); font-size: clamp(3rem, 5vw, 5.5rem); margin-bottom: 1rem; color: white;">
        Every Moment <span style="color: var(--color-primary);">Has a Story</span>
      </h1>
      <p style="font-size: 1.25rem; color: rgba(255,255,255,0.9); max-width: 600px; margin: 0 auto 2.5rem; line-height: 1.6;">
        Join our community gallery. Share your magical memories, photos, and videos of celebrations brought to life by Magiqo entertainers.
      </p>
      <a href="#upload-section" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2.5rem;">Share Your Moment</a>
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
        <!-- Added a 6th moment here -->
        <div class="masonry-item" onclick="openLightbox('assets/images/kids_clapping_party_1790917531872.jpg', 'The balloons made the entire party so vibrant! Everyone loved it.')">
          <img src="assets/images/kids_clapping_party_1790917531872.jpg" alt="Kids Clapping">
          <div class="masonry-item-info">
            <h4 style="color:var(--color-primary); font-size:1.1rem; margin-bottom:0.5rem;">Sarah's 5th Birthday</h4>
            <p style="color:var(--color-text-light); font-size:0.9rem; font-style:italic;">"The balloons made the entire party so vibrant! Everyone loved it."</p>
            <div style="margin-top:0.5rem; font-size:0.8rem; color:#888;">Entertainer: Master Balloon Twister</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 03 & 09. Share Your Moment (Upload Form) + Guidelines -->
  <section id="upload-section" style="padding: 6rem 0; background: var(--color-surface);">
    <div class="container" style="max-width: 1000px;">
      
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 3rem;">
        
        <!-- Upload Guidelines -->
        <div style="background:var(--color-bg); padding:2.5rem; border-radius:var(--radius-lg); border-left:4px solid var(--color-primary);">
          <h3 style="font-size:1.75rem; color:var(--color-primary); margin-bottom:1.5rem; font-family:var(--font-magic);">Upload Guidelines</h3>
          <p style="color:var(--color-text-light); margin-bottom:1rem;">Please read before sharing your magical moments:</p>
          <ul style="color:var(--color-text-light); line-height:1.8; padding-left:1.5rem; margin:0;">
            <li><strong>File Formats:</strong> JPG, PNG, MP4 accepted. Max size 20MB per file.</li>
            <li><strong>Content Moderation:</strong> All submissions are reviewed by our team before publishing to ensure community safety.</li>
            <li><strong>Consent is Key:</strong> Ensure you have explicit permission from anyone clearly visible in your photos/videos before sharing.</li>
            <li><strong>Privacy First:</strong> We will never sell your photos or use them for external marketing without separate written consent.</li>
          </ul>
        </div>
        
        <!-- Form -->
        <div id="form-container">
          <div class="section-title" style="font-family: var(--font-magic); margin-bottom:1.5rem;">
            <span style="color: var(--color-primary);">Share Your</span> <span style="color: #3895c8;">Moment</span>
          </div>
          <form id="uploadForm" onsubmit="submitForm(event)">
            <div class="upload-zone" id="uploadZone" onclick="document.getElementById('fileInput').click()">
              <input type="file" id="fileInput" style="display:none;" onchange="fileSelected(event)">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom:1rem;">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="17 8 12 3 7 8"></polyline>
                <line x1="12" y1="3" x2="12" y2="15"></line>
              </svg>
              <h3 id="uploadText" style="color:var(--color-text); font-size:1.5rem; margin-bottom:0.5rem;">Click to Browse Files</h3>
              <p style="color:var(--color-text-light);">or drag & drop here</p>
            </div>
            
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem;">
              <input type="text" class="form-control" placeholder="Event Title" required>
              <input type="text" class="form-control" placeholder="Your Name" required>
            </div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem;">
              <select class="form-control" required>
                <option value="">Select Event Category</option>
                <option>Kids Party</option>
                <option>Toddler Birthdays</option>
                <option>Special Celebration</option>
              </select>
              <input type="text" class="form-control" placeholder="Entertainer Name">
            </div>
            <textarea class="form-control" rows="3" placeholder="Tell us about the magic! Add a caption..." required></textarea>
            
            <div style="margin-bottom: 2rem; display: flex; align-items: flex-start; gap: 0.5rem;">
              <input type="checkbox" id="consent" required style="margin-top: 0.3rem;">
              <label for="consent" style="color:var(--color-text-light); font-size:0.85rem; line-height:1.5;">
                I confirm I have permission to share these files and agree to the guidelines.
              </label>
            </div>
            
            <button type="submit" class="btn btn-primary" style="width: 100%; font-size: 1.125rem; padding: 1rem;">Submit for Review</button>
          </form>
        </div>
        
        <!-- Success Message (Hidden by default) -->
        <div id="success-message" style="display:none; text-align:center; padding: 4rem 2rem; border-radius:var(--radius-lg); background:rgba(46, 204, 113, 0.1); border:2px solid #2ecc71;">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="2" style="margin-bottom:1rem;">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
          </svg>
          <h3 style="color:var(--color-text); font-size:2rem; margin-bottom:1rem; font-family:var(--font-magic);">Moment Submitted!</h3>
          <p style="color:var(--color-text-light); font-size:1.1rem; line-height:1.6;">
            Thank you for sharing your magic with us. Your memory has been submitted for review and will appear in the gallery soon!
          </p>
          <button onclick="resetForm()" class="btn btn-outline" style="margin-top:2rem;">Upload Another</button>
        </div>
        
      </div>
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
          <img src="assets/images/superhero_party_1790842695325.jpg" style="width:100%; height:180px; object-fit:cover;">
          <div style="padding: 1.5rem;">
            <h3 style="color:var(--color-primary); font-family:var(--font-magic); font-size:1.5rem;">Kids' Parties</h3>
          </div>
        </div>
        <div class="category-card">
          <img src="assets/images/clown_party_1790842566084.jpg" style="width:100%; height:180px; object-fit:cover;">
          <div style="padding: 1.5rem;">
            <h3 style="color:var(--color-primary); font-family:var(--font-magic); font-size:1.5rem;">Toddler Birthdays</h3>
          </div>
        </div>
        <div class="category-card">
          <img src="assets/images/party_moments_2_1790918669697.jpg" style="width:100%; height:180px; object-fit:cover;">
          <div style="padding: 1.5rem;">
            <h3 style="color:var(--color-primary); font-family:var(--font-magic); font-size:1.5rem;">Special Celebrations</h3>
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
          <h3 style="font-size:2.5rem; margin-bottom:1rem; font-family:var(--font-magic); color:var(--color-text);">The Incredible Magic Show</h3>
          <p style="color:var(--color-text-light); line-height:1.8; margin-bottom:1.5rem; font-style:italic; font-size: 1.1rem;">
            "We were completely blown away by the level of engagement! The magician had every single child completely focused and laughing for an entire hour. It made our son's 7th birthday truly unforgettable. He actually made a dove appear out of thin air, and the look on the kids' faces was priceless. I highly recommend them to anyone wanting a real, awe-inspiring experience for their child."
          </p>
          <div style="color:var(--color-primary); font-size:1rem; font-weight: bold;">- Shared by The Anderson Family</div>
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
        Discover the talented professionals making these moments possible. Click to learn what they do.
      </div>
      <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
        <button onclick="showEntertainer('Magic Show', 'Prepare to be amazed by classic illusions, card tricks, and mind-bending stage magic that captivates audiences of all ages.')" class="btn btn-outline" style="border-radius:50px; font-size:1.1rem;">The Great Magic Show</button>
        <button onclick="showEntertainer('Royal Princess', 'Our princesses bring fairy tales to life with elegant tea parties, enchanting storytelling, and royal coronation ceremonies.')" class="btn btn-outline" style="border-radius:50px; font-size:1.1rem;">Royal Princess</button>
        <button onclick="showEntertainer('Superhero', 'Action-packed hero training! Our heroes engage kids with dynamic stunt shows, games, and meet-and-greets.')" class="btn btn-outline" style="border-radius:50px; font-size:1.1rem;">Ultimate Hero</button>
        <button onclick="showEntertainer('Silly Clowns', 'Hilarious slapstick comedy, balloon animals, and non-stop laughter perfect for toddlers and young children.')" class="btn btn-outline" style="border-radius:50px; font-size:1.1rem;">Silly Clowns</button>
      </div>
      
      <!-- Inline Entertainer Description -->
      <div id="ent-desc-box" style="display:none; max-width:600px; margin: 3rem auto 0; background:var(--color-surface); padding:2rem; border-radius:var(--radius-md); box-shadow:0 10px 20px var(--color-shadow); text-align:center;">
        <h3 id="ent-title" style="color:var(--color-primary); font-family:var(--font-magic); font-size:2rem; margin-bottom:1rem;">Title</h3>
        <p id="ent-desc" style="color:var(--color-text-light); font-size:1.1rem; line-height:1.6;"></p>
      </div>
    </div>
  </section>

  <!-- 08. Your Memories, Our Inspiration -->
  <section style="padding: 6rem 0; background: var(--color-surface);">
    <div class="container" style="max-width:900px;">
      <div class="inspiration-card text-center">
        <h2 style="font-family: var(--font-magic); font-size:3rem; margin-bottom: 2rem; position:relative; z-index:2;">
          Your Memories, <br>Our Inspiration
        </h2>
        <p style="font-size: 1.25rem; line-height: 1.8; font-style:italic; position:relative; z-index:2; margin-bottom:2rem;">
          "Seeing the joy and wonder in these shared moments is what drives us. Thank you to every family and community member who allows us to be a part of their special celebrations. Your smiles fuel our magic."
        </p>
        <div style="font-weight:bold; font-size:1.1rem; position:relative; z-index:2;">- The Magiqo Team</div>
      </div>
    </div>
  </section>

  <!-- 10. CTA -->
  <section style="padding: 8rem 0; text-align:center; background: var(--color-tertiary);">
    <div class="container">
      <h2 style="font-family: var(--font-magic); font-size:3.5rem; margin-bottom:1.5rem; color: white;">
        Let's Make More Memories
      </h2>
      <p style="color:rgba(255,255,255,0.9); font-size:1.25rem; margin-bottom:3rem;">Ready to create unforgettable moments for your next big celebration?</p>
      <div style="display:flex; justify-content:center; gap:1.5rem; flex-wrap:wrap;">
        <a href="#upload-section" class="btn" style="padding:1rem 2.5rem; font-size: 1.1rem; background:white; color:var(--color-tertiary); font-weight:bold; border-radius:var(--radius-pill);">Upload a Memory</a>
        <a href="packages.html" class="btn btn-outline" style="padding:1rem 2.5rem; font-size: 1.1rem; color:white; border-color:white; border-radius:var(--radius-pill);">Book an Entertainer</a>
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

  <div id="footer"></div>

  <script>
    function openLightbox(imgUrl, desc) {
      document.getElementById('lightboxImg').src = imgUrl;
      document.getElementById('lightboxDesc').innerText = '"' + desc + '"';
      document.getElementById('lightbox').style.display = 'flex';
    }
    
    function fileSelected(e) {
      if(e.target.files.length > 0) {
        document.getElementById('uploadText').innerText = e.target.files[0].name;
      }
    }
    
    function submitForm(e) {
      e.preventDefault();
      document.getElementById('form-container').style.display = 'none';
      document.getElementById('success-message').style.display = 'block';
    }
    
    function resetForm() {
      document.getElementById('uploadForm').reset();
      document.getElementById('uploadText').innerText = 'Click to Browse Files';
      document.getElementById('form-container').style.display = 'block';
      document.getElementById('success-message').style.display = 'none';
    }
    
    function showEntertainer(title, desc) {
      document.getElementById('ent-title').innerText = title;
      document.getElementById('ent-desc').innerText = desc;
      document.getElementById('ent-desc-box').style.display = 'block';
    }
  </script>

  <script src="js/components.js"></script>

</body>
</html>
"""

with open('c:/Users/vigas/Desktop/magiqo/upload.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("done")
