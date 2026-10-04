import os

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Why Choose MAGIQO -->'
end_marker = '<!-- Magical Party Experiences -->'

if start_marker in content and end_marker in content:
    pre_content = content.split(start_marker)[0]
    post_content = content.split(end_marker)[1]
    
    new_sections = """<!-- Why Choose MAGIQO -->
  <section id="why-choose" style="padding: 6rem 0; background: linear-gradient(135deg, #f8f6ff 0%, #fff9fc 100%); position: relative; overflow: hidden;">
    <!-- Abstract background shapes -->
    <div style="position: absolute; top: -100px; left: -100px; width: 300px; height: 300px; background: rgba(241, 123, 172, 0.1); filter: blur(50px); border-radius: 50%;"></div>
    <div style="position: absolute; bottom: -100px; right: -100px; width: 400px; height: 400px; background: rgba(117, 191, 242, 0.1); filter: blur(60px); border-radius: 50%;"></div>
    
    <div class="container" style="position: relative; z-index: 1;">
      <div class="section-title text-center" style="font-family: var(--font-magic); margin-bottom: 1rem;">
        <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Why Choose</span> 
        <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">MAGIQO</span>
      </div>
      <div class="section-subtitle text-center" style="margin-bottom: 4rem; color: #625b70;">Safety, professional entertainers, personalized experiences, and trusted service.</div>
      
      <style>
        .why-card { 
          background: rgba(255, 255, 255, 0.7);
          backdrop-filter: blur(10px);
          border: 1px solid rgba(255, 255, 255, 0.5);
          border-radius: 20px;
          padding: 2.5rem 1.5rem;
          transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
          box-shadow: 0 10px 30px rgba(0,0,0,0.03);
          position: relative;
          overflow: hidden;
        }
        .why-card::before {
          content: '';
          position: absolute;
          top: 0; left: 0; right: 0; height: 4px;
          background: linear-gradient(90deg, var(--color-primary), #3895c8);
          transform: scaleX(0);
          transform-origin: left;
          transition: transform 0.4s ease;
        }
        .why-card:hover { 
          transform: translateY(-15px); 
          box-shadow: 0 20px 40px rgba(210, 75, 118, 0.15); 
          border-color: rgba(210, 75, 118, 0.3);
        }
        .why-card:hover::before {
          transform: scaleX(1);
        }
        .why-icon-wrap {
          width: 80px; height: 80px;
          margin: 0 auto 1.5rem;
          border-radius: 50%;
          display: flex; align-items: center; justify-content: center;
          background: linear-gradient(135deg, #fff0f7, #edf8ff);
          position: relative;
          transition: transform 0.4s ease;
        }
        .why-card:hover .why-icon-wrap {
          transform: rotateY(180deg);
        }
        .why-icon-inner {
          transition: transform 0.4s ease;
        }
        .why-card:hover .why-icon-inner {
          transform: rotateY(-180deg);
        }
      </style>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2.5rem;">
        <!-- Card 1 -->
        <div class="text-center why-card">
          <div class="why-icon-wrap">
            <div class="why-icon-inner"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#d95791" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
          </div>
          <h3 style="font-size: 1.4rem; margin-bottom: 1rem; color: #302344; font-weight: 700;">Safety First</h3>
          <p style="color: #777185; line-height: 1.6; font-size: 0.95rem;">All entertainers are fully vetted, background-checked, and insured for your peace of mind.</p>
        </div>
        <!-- Card 2 -->
        <div class="text-center why-card">
          <div class="why-icon-wrap">
            <div class="why-icon-inner"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></div>
          </div>
          <h3 style="font-size: 1.4rem; margin-bottom: 1rem; color: #302344; font-weight: 700;">Professional Talent</h3>
          <p style="color: #777185; line-height: 1.6; font-size: 0.95rem;">Only the best, highly-rated magicians, clowns, and characters make it to Magiqo.</p>
        </div>
        <!-- Card 3 -->
        <div class="text-center why-card">
          <div class="why-icon-wrap">
            <div class="why-icon-inner"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#d95791" stroke-width="2"><path d="M12 2l3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/></svg></div>
          </div>
          <h3 style="font-size: 1.4rem; margin-bottom: 1rem; color: #302344; font-weight: 700;">Personalized Magic</h3>
          <p style="color: #777185; line-height: 1.6; font-size: 0.95rem;">Experiences tailored specifically to your child's age, interests, and party theme.</p>
        </div>
        <!-- Card 4 -->
        <div class="text-center why-card">
          <div class="why-icon-wrap">
            <div class="why-icon-inner"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg></div>
          </div>
          <h3 style="font-size: 1.4rem; margin-bottom: 1rem; color: #302344; font-weight: 700;">Easy Booking</h3>
          <p style="color: #777185; line-height: 1.6; font-size: 0.95rem;">Seamless, transparent booking process with instant confirmations and no hidden fees.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Party Packages -->
  <section id="packages" style="padding: 7rem 0; background: var(--color-surface); position: relative;">
    <div class="container">
      <div class="section-title text-center" style="font-family: var(--font-magic); margin-bottom: 1rem;">
        <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Popular</span> 
        <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Packages</span>
      </div>
      <div class="section-subtitle text-center" style="margin-bottom: 4rem; color: #625b70;">Choose the perfect level of magic for your celebration.</div>
      
      <style>
        .pkg-card {
          background: #ffffff;
          border-radius: 24px;
          padding: 3rem 2.5rem;
          transition: all 0.4s ease;
          border: 1px solid rgba(0,0,0,0.05);
          position: relative;
          display: flex; flex-direction: column;
        }
        .pkg-card:hover {
          transform: translateY(-10px);
          box-shadow: 0 25px 50px rgba(0,0,0,0.08);
        }
        .pkg-btn {
          margin-top: auto;
          padding: 1rem;
          border-radius: 12px;
          font-weight: 700;
          text-transform: uppercase;
          letter-spacing: 1px;
          transition: all 0.3s ease;
          display: block; width: 100%;
          text-decoration: none;
        }
        .pkg-btn-outline {
          background: transparent;
          border: 2px solid #e0e0e0;
          color: #302344;
        }
        .pkg-btn-outline:hover {
          border-color: var(--color-primary);
          color: var(--color-primary);
        }
        .pkg-btn-solid {
          background: linear-gradient(135deg, var(--color-primary), #d95791);
          color: white;
          border: none;
          box-shadow: 0 10px 20px rgba(210, 75, 118, 0.3);
        }
        .pkg-btn-solid:hover {
          transform: translateY(-3px);
          box-shadow: 0 15px 25px rgba(210, 75, 118, 0.4);
          color: white;
        }
        .pkg-popular {
          background: linear-gradient(145deg, #180D20, #302344);
          color: white;
          transform: scale(1.05);
          z-index: 2;
          box-shadow: 0 30px 60px rgba(48, 35, 68, 0.25);
          border: none;
        }
        .pkg-popular:hover {
          transform: scale(1.05) translateY(-10px);
          box-shadow: 0 40px 70px rgba(48, 35, 68, 0.35);
        }
        .badge-popular {
          position: absolute;
          top: -15px; left: 50%; transform: translateX(-50%);
          background: linear-gradient(135deg, #f29ac0, #80c5f4);
          color: white;
          padding: 0.5rem 1.5rem;
          border-radius: 20px;
          font-weight: 800;
          font-size: 0.85rem;
          letter-spacing: 1.5px;
          text-transform: uppercase;
          box-shadow: 0 8px 15px rgba(242, 154, 192, 0.4);
          white-space: nowrap;
        }
      </style>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; align-items: center;">
        
        <!-- Standard -->
        <div class="text-center pkg-card">
          <h3 style="font-family: var(--font-magic); font-size: 2.2rem; margin-bottom: 0.5rem; color: #302344;">The Sparkle</h3>
          <p style="color: #777185; margin-bottom: 1.5rem;">60 Minutes of fun</p>
          <div style="font-size: 3.5rem; font-weight: 800; color: #302344; margin-bottom: 2rem; display: flex; justify-content: center; align-items: baseline;">
            <span style="font-size: 1.5rem; vertical-align: top;">$</span>150
          </div>
          <ul style="list-style: none; padding: 0; margin-bottom: 2.5rem; text-align: left;">
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #625b70;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 1 Character or Magician</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #625b70;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Basic Magic Show</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #625b70;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Balloon Animals</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #cfcfcf;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#cfcfcf" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg> Face Painting</li>
          </ul>
          <a href="packages.html" class="pkg-btn pkg-btn-outline">Select Package</a>
        </div>

        <!-- Premium (Most Popular) -->
        <div class="text-center pkg-card pkg-popular">
          <div class="badge-popular">Most Popular</div>
          <h3 style="font-family: var(--font-magic); font-size: 2.5rem; margin-bottom: 0.5rem; color: #ffffff;">Magic Spell</h3>
          <p style="color: #a9a2b5; margin-bottom: 1.5rem;">90 Minutes of magic</p>
          <div style="font-size: 4rem; font-weight: 800; color: #ffffff; margin-bottom: 2rem; display: flex; justify-content: center; align-items: baseline;">
            <span style="font-size: 1.8rem; vertical-align: top; color: var(--color-primary);">+$</span>250
          </div>
          <ul style="list-style: none; padding: 0; margin-bottom: 2.5rem; text-align: left;">
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #e6e4ea;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 1 Character or Magician</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #e6e4ea;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Grand Magic Show</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #e6e4ea;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Face Painting</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #e6e4ea;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Interactive Games</li>
          </ul>
          <a href="packages.html" class="pkg-btn pkg-btn-solid">Select Package</a>
        </div>

        <!-- Ultimate -->
        <div class="text-center pkg-card">
          <h3 style="font-family: var(--font-magic); font-size: 2.2rem; margin-bottom: 0.5rem; color: #302344;">Grand Illusion</h3>
          <p style="color: #777185; margin-bottom: 1.5rem;">120 Minutes of wonder</p>
          <div style="font-size: 3.5rem; font-weight: 800; color: #302344; margin-bottom: 2rem; display: flex; justify-content: center; align-items: baseline;">
            <span style="font-size: 1.5rem; vertical-align: top;">$</span>399
          </div>
          <ul style="list-style: none; padding: 0; margin-bottom: 2.5rem; text-align: left;">
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #625b70;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 2 Characters/Magicians</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #625b70;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Complete Stage Show</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #625b70;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Custom Party Favors</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 10px; color: #625b70;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#599fdd" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Special Grand Finale</li>
          </ul>
          <a href="packages.html" class="pkg-btn pkg-btn-outline">Select Package</a>
        </div>

      </div>
    </div>
  </section>
  
  <!-- Magical Party Experiences -->"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(pre_content + new_sections + post_content)
