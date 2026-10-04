import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Elias - Master Magician | Magiqo</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="Book Elias the Master Magician for your next children's party. Highly rated interactive magic shows, illusions, and unforgettable party experiences.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
  
  <!-- Core Styles -->
  <link rel="stylesheet" href="css/style.css">
  
  <style>
    /* 1. Entertainer Hero Section */
    .ent-detail-hero {
      position: relative;
      min-height: 85vh;
      display: flex;
      align-items: center;
      background: linear-gradient(135deg, var(--color-bg) 0%, var(--color-bg) 40%, var(--color-surface) 40%, var(--color-surface) 100%);
      padding-top: 150px;
      padding-bottom: 5rem;
      overflow: hidden;
    }
    
    .profile-layout {
      display: flex;
      align-items: center;
      gap: 4rem;
      position: relative;
      z-index: 2;
    }
    
    .profile-image-wrap {
      flex: 1;
      display: flex;
      justify-content: center;
      position: relative;
    }
    
    .profile-image-wrap img {
      width: 100%;
      max-width: 500px;
      border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
      box-shadow: 0 20px 50px rgba(0,0,0,0.15);
      border: 10px solid white;
      object-fit: cover;
      height: 500px;
      animation: floatProfile 6s ease-in-out infinite;
    }

    @keyframes floatProfile {
      0%, 100% { transform: translateY(0) scale(1); border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; }
      50% { transform: translateY(-15px) scale(1.02); border-radius: 40% 60% 50% 50% / 40% 40% 60% 60%; }
    }
    
    .profile-info {
      flex: 1;
    }
    
    .profile-info h1 {
      font-family: var(--font-magic);
      font-size: clamp(3.5rem, 5vw, 5rem);
      color: #3895c8;
      margin-bottom: 0.5rem;
      line-height: 1.1;
    }
    
    .profile-specialty {
      font-size: 1.75rem;
      color: var(--color-primary);
      font-weight: bold;
      font-family: var(--font-heading);
      margin-bottom: 1.5rem;
    }
    
    .profile-rating {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: white;
      padding: 0.5rem 1.5rem;
      border-radius: var(--radius-pill);
      box-shadow: 0 5px 15px rgba(0,0,0,0.05);
      font-weight: bold;
      color: #ff9800;
      font-size: 1.25rem;
      margin-bottom: 2rem;
    }

    /* 2. Content Sections */
    .detail-section {
      padding: 6rem 0;
    }

    .detail-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4rem;
      align-items: center;
    }

    /* Redesigned Signature Performances */
    .sig-list {
      display: flex;
      flex-direction: column;
      gap: 2rem;
      margin-top: 3rem;
    }
    .sig-item {
      display: flex;
      align-items: center;
      gap: 1.5rem;
      background: white;
      padding: 2rem;
      border-radius: var(--radius-lg);
      box-shadow: 0 10px 30px rgba(0,0,0,0.05);
      border-left: 5px solid var(--color-primary);
      transition: transform 0.3s;
    }
    .sig-item:hover {
      transform: translateX(10px);
    }
    .sig-icon {
      width: 60px; height: 60px;
      background: #e0f7fa;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
    }
    .sig-icon svg { width: 30px; height: 30px; fill: #3895c8; }
    .sig-text h3 { font-family: var(--font-heading); color: #3895c8; margin-bottom: 0.5rem; font-size: 1.5rem; }
    .sig-text p { color: var(--color-text-light); margin: 0; line-height: 1.5; }

    /* Redesigned Stats Banner */
    .new-stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
    }
    .new-stat-card {
      background: white;
      padding: 3rem 2rem;
      text-align: center;
      border-radius: var(--radius-xl);
      box-shadow: 0 15px 40px rgba(0,0,0,0.05);
      border-bottom: 4px solid #3895c8;
      transition: transform 0.3s;
    }
    .new-stat-card:hover { transform: translateY(-10px); }
    .new-stat-card h3 {
      font-size: 4rem;
      font-family: var(--font-magic);
      color: var(--color-primary);
      margin-bottom: 0.5rem;
      line-height: 1;
    }
    .new-stat-card p {
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--color-text);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin: 0;
    }

    /* SVG wrapper for list */
    .icon-wrapper {
      width: 50px; height: 50px;
      background: #f0f8ff;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
    }
    .icon-wrapper svg { width: 24px; height: 24px; fill: #3895c8; }

    /* Media queries */
    @media (max-width: 992px) {
      .profile-layout { flex-direction: column; text-align: center; }
      .detail-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Dynamic Header -->
  <div id="navbar"></div>

  <!-- 1. Entertainer Hero -->
  <section class="ent-detail-hero">
    <div class="container profile-layout">
      <div class="profile-image-wrap">
        <img src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias the Magician">
      </div>
      <div class="profile-info">
        <h1>Elias</h1>
        <div class="profile-specialty">Master Magician & Illusionist</div>
        <div class="profile-rating">
          <svg viewBox="0 0 24 24" style="width:20px;height:20px;fill:#ff9800;"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg> 
          Rating: 5.0/5 (120+ Reviews)
        </div>
        <p style="font-size: 1.2rem; color: var(--color-text-light); line-height: 1.6; margin-bottom: 2rem;">
          Bring the wonder of true magic to your child's special day. Elias blends mind-bending illusions, hilarious comedy, and fully interactive stage shows that will leave kids and parents alike speechless.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
           <a href="#book-now" class="btn btn-animated" style="background: var(--color-primary); color: white; padding: 1.25rem 2.5rem; font-size: 1.1rem; border-radius: var(--radius-pill); box-shadow: 0 10px 20px rgba(218, 47, 95, 0.3);">Book Elias Now</a>
           <a href="#watch" class="btn btn-animated" style="background: white; color: #3895c8; border: 2px solid #3895c8; padding: 1.25rem 2.5rem; font-size: 1.1rem; border-radius: var(--radius-pill);">Watch Video</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. Meet Your Entertainer -->
  <section class="detail-section" style="background: white;">
    <div class="container detail-grid">
      <div>
        <div class="sec-title" style="text-align: left;">
          <h2><span style="color: #3895c8;">Meet</span> <span style="color: var(--color-primary);">Elias</span></h2>
        </div>
        <p style="font-size: 1.15rem; color: var(--color-text-light); line-height: 1.7; margin-bottom: 1.5rem;">
          With over 10 years of professional performing experience, Elias isn't just a magician—he's a master storyteller. His passion for magic began when he was just 8 years old, and he has spent his life perfecting routines designed specifically to captivate young minds.
        </p>
        <p style="font-size: 1.15rem; color: var(--color-text-light); line-height: 1.7;">
          Elias believes that the best magic happens when the children become part of the show. His performances are highly interactive, ensuring the birthday child always feels like the true star of the day.
        </p>
      </div>
      <div>
        <img src="assets/images/about_art_of_magic.jpg" alt="Elias Performing" style="width: 100%; border-radius: var(--radius-xl); box-shadow: 0 15px 40px rgba(0,0,0,0.1);">
      </div>
    </div>
  </section>

  <!-- 3. Redesigned Experience & Expertise -->
  <section class="detail-section" style="background: var(--color-bg);">
    <div class="container">
      <div class="sec-title text-center">
        <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Experience &</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Expertise</span></h2>
        <p>A proven track record of bringing joy to hundreds of events.</p>
      </div>
      <div class="new-stats-grid">
        <div class="new-stat-card">
          <h3>10+</h3>
          <p>Years Experience</p>
        </div>
        <div class="new-stat-card" style="border-color: var(--color-primary);">
          <h3 style="color: #3895c8;">500+</h3>
          <p>Parties Performed</p>
        </div>
        <div class="new-stat-card">
          <h3>5.0</h3>
          <p>Average Rating</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. Signature Performances (Redesigned) -->
  <section class="detail-section" style="background: white;">
    <div class="container">
      <div class="sec-title text-center">
        <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Signature</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Performances</span></h2>
        <p>What to expect when Elias takes the stage.</p>
      </div>
      <div class="sig-list" style="max-width: 800px; margin: 3rem auto 0;">
        <div class="sig-item">
          <div class="sig-icon">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
          </div>
          <div class="sig-text">
            <h3>The Floating Child</h3>
            <p>Elias's signature grand illusion where the birthday child safely levitates in mid-air, creating a photo moment you'll never forget.</p>
          </div>
        </div>
        <div class="sig-item">
          <div class="sig-icon" style="background: #fff0f5;">
            <svg viewBox="0 0 24 24" style="fill: var(--color-primary);"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6C7.8 12.16 7 10.63 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>
          </div>
          <div class="sig-text">
            <h3 style="color: var(--color-primary);">Comedy Mind Reading</h3>
            <p>Hilarious and baffling mind-reading tricks tailored for kids, guaranteed to get the entire audience laughing out loud.</p>
          </div>
        </div>
        <div class="sig-item">
          <div class="sig-icon">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/></svg>
          </div>
          <div class="sig-text">
            <h3>Live Animal Magic</h3>
            <p>Watch as doves appear from thin air and a real, friendly bunny is magically produced for the kids to pet after the show.</p>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- 5. Watch the Magic & Perfect For Your Party -->
  <section id="watch" class="detail-section" style="background: var(--color-surface);">
    <div class="container detail-grid">
      <div>
        <!-- Video Placeholder -->
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: var(--radius-xl); box-shadow: 0 20px 50px rgba(0,0,0,0.15);">
          <img src="assets/images/magic_show_party_1790842468826.jpg" alt="Video Thumbnail" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
          <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80px; height: 80px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 0 0 10px rgba(255,255,255,0.2);">
            <div style="width: 0; height: 0; border-top: 15px solid transparent; border-bottom: 15px solid transparent; border-left: 25px solid var(--color-primary); margin-left: 5px;"></div>
          </div>
        </div>
      </div>
      <div>
        <div class="sec-title" style="text-align: left;">
          <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Perfect for</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Your Party</span></h2>
        </div>
        <ul style="list-style: none; padding: 0; margin-top: 2rem;">
          <li style="margin-bottom: 1.5rem; display: flex; gap: 1rem; align-items: flex-start;">
            <div class="icon-wrapper">
              <svg viewBox="0 0 24 24"><path d="M12 6c1.11 0 2-.9 2-2 0-.38-.1-.73-.29-1.03L12 0l-1.71 2.97c-.19.3-.29.65-.29 1.03 0 1.1.9 2 2 2zm4.6 9.99l-1.07-1.07-1.08 1.07c-1.3 1.3-3.58 1.31-4.89 0l-1.07-1.07-1.09 1.07C6.75 16.64 5.88 17 4.96 17c-.73 0-1.4-.23-1.96-.61V21c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-4.61c-.56.38-1.23.61-1.96.61-.92 0-1.79-.36-2.44-1.01zM18 9h-5V7h-2v2H6c-1.66 0-3 1.34-3 3v1.54c0 1.08.88 1.96 1.96 1.96.52 0 1.02-.2 1.38-.57l2.14-2.13 2.13 2.13c.74.74 2.03.74 2.77 0l2.14-2.13 2.13 2.13c.37.37.86.57 1.38.57 1.08 0 1.96-.88 1.96-1.96V12c0-1.66-1.34-3-3-3z"/></svg>
            </div>
            <div><h4 style="font-size: 1.2rem; margin-bottom: 0.25rem;">Ideal Age Group</h4><p style="color: var(--color-text-light); margin: 0;">Ages 4 to 12 years old</p></div>
          </li>
          <li style="margin-bottom: 1.5rem; display: flex; gap: 1rem; align-items: flex-start;">
            <div class="icon-wrapper" style="background: #fff0f5;">
              <svg viewBox="0 0 24 24" style="fill: var(--color-primary);"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
            </div>
            <div><h4 style="font-size: 1.2rem; margin-bottom: 0.25rem;">Party Size</h4><p style="color: var(--color-text-light); margin: 0;">Great for 10 to 50+ kids</p></div>
          </li>
          <li style="margin-bottom: 1.5rem; display: flex; gap: 1rem; align-items: flex-start;">
            <div class="icon-wrapper">
              <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
            </div>
            <div><h4 style="font-size: 1.2rem; margin-bottom: 0.25rem;">Venues</h4><p style="color: var(--color-text-light); margin: 0;">Living rooms, backyards, halls, and parks</p></div>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- 6. Packages & Special Add-ons -->
  <section class="detail-section" style="background: white;">
    <div class="container detail-grid">
      <div>
        <div class="sec-title" style="text-align: left;">
          <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Packages &</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Pricing</span></h2>
        </div>
        <p style="font-size: 1.1rem; color: var(--color-text-light); line-height: 1.6; margin-bottom: 2rem;">
          Elias offers 3 customizable magic packages designed to fit any party size and budget. From our 45-minute "Magic Teaser" to the 90-minute "VIP Extravaganza," you can find the perfect magical experience for your event.
        </p>
        <a href="packages.html?entertainer=elias" class="btn btn-animated" style="background: var(--color-primary); color: white; padding: 1rem 2rem; font-size: 1.1rem; border-radius: var(--radius-pill);">View Packages & Pricing</a>
      </div>
      <div>
        <div style="background: var(--color-bg); padding: 3rem; border-radius: var(--radius-xl); box-shadow: 0 15px 40px rgba(0,0,0,0.05); text-align: center;">
          <h3 style="font-family: var(--font-heading); color: #3895c8; font-size: 1.8rem; margin-bottom: 2rem;">Special Add-ons Available</h3>
          <div style="display: flex; gap: 1rem; align-items: center; justify-content: center; margin-bottom: 1.5rem; background: white; padding: 1rem; border-radius: var(--radius-md);">
             <svg viewBox="0 0 24 24" style="width:30px;height:30px;fill:var(--color-primary);"><path d="M11 2v20c-5.07-.5-9-4.79-9-10s3.93-9.5 9-10zm2 0v20c5.07-.5 9-4.79 9-10s-3.93-9.5-9-10z"/></svg>
             <div style="text-align: left;"><strong style="display: block;">Balloon Twisting</strong><span style="color: var(--color-text-light); font-size: 0.9rem;">30 extra minutes</span></div>
          </div>
          <div style="display: flex; gap: 1rem; align-items: center; justify-content: center; background: white; padding: 1rem; border-radius: var(--radius-md);">
             <svg viewBox="0 0 24 24" style="width:30px;height:30px;fill:#3895c8;"><path d="M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z"/></svg>
             <div style="text-align: left;"><strong style="display: block;">Magic Trick Favors</strong><span style="color: var(--color-text-light); font-size: 0.9rem;">Goodie bags for kids</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 7. Check Availability & Book -->
  <section class="detail-section" style="background: linear-gradient(135deg, #f9f9f9, #e0f7fa);">
    <div class="container">
      <div style="background: white; border-radius: var(--radius-xl); padding: 5rem 3rem; box-shadow: 0 20px 60px rgba(0,0,0,0.08); max-width: 900px; margin: 0 auto; border-top: 10px solid var(--color-primary);">
        <div class="sec-title text-center" style="margin-bottom: 3rem;">
          <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Book</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Elias</span></h2>
          <p>Check availability for your date to proceed with booking.</p>
        </div>
        
        <div id="booking-form-area">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
            <div>
              <label style="display: block; font-weight: bold; margin-bottom: 0.5rem; color: var(--color-text);">Party Date</label>
              <input type="date" id="b_date" style="width: 100%; padding: 1rem; border: 2px solid var(--color-border); border-radius: var(--radius-md); font-size: 1rem; outline: none;">
            </div>
            <div>
              <label style="display: block; font-weight: bold; margin-bottom: 0.5rem; color: var(--color-text);">Event Start Time</label>
              <input type="time" style="width: 100%; padding: 1rem; border: 2px solid var(--color-border); border-radius: var(--radius-md); font-size: 1rem; outline: none;">
            </div>
            <div>
              <label style="display: block; font-weight: bold; margin-bottom: 0.5rem; color: var(--color-text);">Zip Code</label>
              <input type="text" placeholder="e.g. 90210" style="width: 100%; padding: 1rem; border: 2px solid var(--color-border); border-radius: var(--radius-md); font-size: 1rem; outline: none;">
            </div>
            <div>
              <label style="display: block; font-weight: bold; margin-bottom: 0.5rem; color: var(--color-text);">Estimated Number of Kids</label>
              <select style="width: 100%; padding: 1rem; border: 2px solid var(--color-border); border-radius: var(--radius-md); font-size: 1rem; outline: none;">
                <option>Under 10</option>
                <option>10 - 20</option>
                <option>20 - 30</option>
                <option>30+</option>
              </select>
            </div>
            
            <div style="grid-column: 1 / -1; margin-top: 1rem;">
              <button type="button" onclick="checkEntAvailability()" class="btn btn-animated" style="width: 100%; background: var(--color-primary); color: white; padding: 1.25rem; font-size: 1.25rem; font-weight: bold; border-radius: var(--radius-pill); border: none; cursor: pointer; box-shadow: 0 10px 20px rgba(218, 47, 95, 0.3);">Check Availability</button>
            </div>
          </div>
        </div>

        <div id="booking-success" style="display: none; text-align: center; padding: 2rem; border: 2px dashed #3895c8; border-radius: var(--radius-lg); background: #e0f7fa;">
          <h3 style="color: #3895c8; font-size: 2rem; margin-bottom: 1rem; font-family: var(--font-heading);">Good News! Elias is Available!</h3>
          <p style="font-size: 1.2rem; color: var(--color-text-light); margin-bottom: 2rem;">We have held your date. Please proceed to select your performance package to complete the booking.</p>
          <a href="packages.html?entertainer=elias" class="btn btn-animated" style="background: var(--color-primary); color: white; padding: 1.25rem 3rem; font-size: 1.25rem; border-radius: var(--radius-pill); text-decoration: none; display: inline-block;">Select Package</a>
        </div>

        <div id="already-booked" style="display: none; text-align: center; padding: 3rem; border: 2px dashed #4caf50; border-radius: var(--radius-lg); background: #e8f5e9;">
          <svg viewBox="0 0 24 24" style="width: 80px; height: 80px; fill: #4caf50; margin-bottom: 1.5rem;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
          <h3 style="color: #2e7d32; font-size: 2.5rem; margin-bottom: 1rem; font-family: var(--font-heading);">Successfully Booked!</h3>
          <p style="font-size: 1.2rem; color: var(--color-text-light); margin-bottom: 0;">You have successfully secured Elias the Magician. We will email you the confirmation details shortly.</p>
        </div>

      </div>
    </div>
  </section>

  <!-- Dynamic Footer -->
  <div id="footer"></div>

  <!-- Scripts -->
  <script src="js/theme.js"></script>
  <script src="js/rtl.js"></script>
  <script src="js/components.js"></script>
  <script src="js/main.js"></script>
  <script>
    function checkEntAvailability() {
        if(!document.getElementById('b_date').value) {
            alert('Please select a party date first.');
            return;
        }
        document.getElementById('booking-form-area').style.display = 'none';
        document.getElementById('booking-success').style.display = 'block';
    }
    
    // Check if user returned from successful payment/booking
    document.addEventListener('DOMContentLoaded', () => {
        if(window.location.search.includes('booked=true')) {
            document.getElementById('booking-form-area').style.display = 'none';
            document.getElementById('booking-success').style.display = 'none';
            document.getElementById('already-booked').style.display = 'block';
            
            // Scroll to booked message
            setTimeout(() => {
                document.getElementById('already-booked').scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 500);
        }
    });
  </script>
</body>
</html>
"""

with open('c:/Users/vigas/Desktop/magiqo/entertainer_detail.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
