import os

filepath = 'c:/Users/vigas/Desktop/magiqo/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Party Packages -->'
end_marker = '<!-- Magical Party Experiences -->'

if start_marker in content and end_marker in content:
    pre_content = content.split(start_marker)[0]
    post_content = content.split(end_marker)[1]
    
    new_sections = """<!-- Party Packages -->
  <section id="packages" style="padding: 8rem 0; background: linear-gradient(135deg, #090a10 0%, #151125 100%); position: relative;">
    
    <!-- Royal decorative elements -->
    <div style="position: absolute; top: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.5), transparent);"></div>
    <div style="position: absolute; top: -150px; left: 50%; transform: translateX(-50%); width: 600px; height: 600px; background: radial-gradient(circle, rgba(212,175,55,0.05) 0%, transparent 70%); pointer-events: none;"></div>

    <div class="container" style="position: relative; z-index: 1;">
      <div class="section-title text-center" style="font-family: 'Playfair Display', serif; margin-bottom: 1rem;">
        <span style="color: #ffffff;">Royal</span> 
        <span style="color: #d4af37;">Packages</span>
      </div>
      <div class="section-subtitle text-center" style="margin-bottom: 5rem; color: #a9a2b5; font-size: 1.1rem; letter-spacing: 1px;">Experience the pinnacle of magical entertainment.</div>
      
      <style>
        .pkg-royal-card {
          background: rgba(255, 255, 255, 0.03);
          border-radius: 20px;
          padding: 3rem 2.5rem;
          transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
          border: 1px solid rgba(212, 175, 55, 0.15);
          position: relative;
          display: flex; flex-direction: column;
          backdrop-filter: blur(10px);
        }
        .pkg-royal-card:hover {
          transform: translateY(-10px);
          border-color: rgba(212, 175, 55, 0.4);
          box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 20px rgba(212, 175, 55, 0.1);
        }
        
        .pkg-btn-royal-outline {
          background: transparent;
          border: 1px solid #d4af37;
          color: #d4af37;
          margin-top: auto;
          padding: 1rem;
          border-radius: 8px;
          font-weight: 600;
          text-transform: uppercase;
          letter-spacing: 2px;
          transition: all 0.3s ease;
          display: block; width: 100%;
          text-decoration: none;
        }
        .pkg-btn-royal-outline:hover {
          background: rgba(212, 175, 55, 0.1);
          color: #fff;
          box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
        }
        
        .pkg-royal-popular {
          background: linear-gradient(160deg, #2b1147 0%, #150824 100%);
          border: 1px solid #d4af37;
          transform: scale(1.05);
          z-index: 2;
          box-shadow: 0 30px 60px rgba(0,0,0,0.6), inset 0 0 0 1px rgba(255,255,255,0.1);
        }
        .pkg-royal-popular:hover {
          transform: scale(1.05) translateY(-10px);
          box-shadow: 0 40px 70px rgba(0,0,0,0.7), 0 0 30px rgba(212, 175, 55, 0.15), inset 0 0 0 1px rgba(255,255,255,0.2);
        }
        
        .pkg-btn-royal-solid {
          background: linear-gradient(135deg, #d4af37, #f3e5ab, #d4af37);
          color: #111;
          border: none;
          margin-top: auto;
          padding: 1rem;
          border-radius: 8px;
          font-weight: 700;
          text-transform: uppercase;
          letter-spacing: 2px;
          transition: all 0.3s ease;
          display: block; width: 100%;
          text-decoration: none;
          background-size: 200% auto;
        }
        .pkg-btn-royal-solid:hover {
          background-position: right center;
          transform: translateY(-3px);
          box-shadow: 0 15px 25px rgba(212, 175, 55, 0.3);
          color: #000;
        }
        
        .badge-royal {
          position: absolute;
          top: -16px; left: 50%; transform: translateX(-50%);
          background: linear-gradient(135deg, #d4af37, #b8860b);
          color: #111;
          padding: 0.5rem 2rem;
          border-radius: 30px;
          font-weight: 800;
          font-size: 0.8rem;
          letter-spacing: 2px;
          text-transform: uppercase;
          box-shadow: 0 5px 15px rgba(0,0,0,0.3);
          white-space: nowrap;
          border: 1px solid #f3e5ab;
        }
        
        .royal-price {
          font-family: 'Playfair Display', serif;
          font-size: 4rem; 
          font-weight: 700; 
          background: linear-gradient(135deg, #f3e5ab, #d4af37, #b8860b);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          margin-bottom: 2rem; 
          display: flex; justify-content: center; align-items: baseline;
        }
      </style>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; align-items: center;">
        
        <!-- Standard -->
        <div class="text-center pkg-royal-card">
          <h3 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; margin-bottom: 0.5rem; color: #ffffff;">The Sparkle</h3>
          <p style="color: #a9a2b5; margin-bottom: 1.5rem; letter-spacing: 1px; font-size: 0.9rem; text-transform: uppercase;">60 Minutes of magic</p>
          <div class="royal-price">
            <span style="font-size: 1.5rem; vertical-align: top; -webkit-text-fill-color: #d4af37;">$</span>150
          </div>
          <ul style="list-style: none; padding: 0; margin-bottom: 2.5rem; text-align: left;">
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #d1cdd8;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 1 Character or Magician</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #d1cdd8;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Basic Magic Show</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #d1cdd8;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Balloon Animals</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #5a5468;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#5a5468" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg> Face Painting</li>
          </ul>
          <a href="packages.html" class="pkg-btn-royal-outline">Select Package</a>
        </div>

        <!-- Premium (Most Popular) -->
        <div class="text-center pkg-royal-card pkg-royal-popular">
          <div class="badge-royal">Most Popular</div>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 2.8rem; margin-bottom: 0.5rem; color: #ffffff;">Magic Spell</h3>
          <p style="color: #d4af37; margin-bottom: 1.5rem; letter-spacing: 1px; font-size: 0.9rem; text-transform: uppercase; font-weight: 600;">90 Minutes of magic</p>
          <div class="royal-price" style="font-size: 4.5rem; text-shadow: 0 4px 15px rgba(212,175,55,0.2);">
            <span style="font-size: 1.8rem; vertical-align: top; -webkit-text-fill-color: #d4af37;">$</span>250
          </div>
          <ul style="list-style: none; padding: 0; margin-bottom: 2.5rem; text-align: left;">
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #ffffff;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> 1 Character or Magician</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #ffffff;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Grand Magic Show</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #ffffff;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Face Painting</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #ffffff;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Interactive Games</li>
          </ul>
          <a href="packages.html" class="pkg-btn-royal-solid">Select Package</a>
        </div>

        <!-- Ultimate -->
        <div class="text-center pkg-royal-card">
          <h3 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; margin-bottom: 0.5rem; color: #ffffff;">Grand Illusion</h3>
          <p style="color: #a9a2b5; margin-bottom: 1.5rem; letter-spacing: 1px; font-size: 0.9rem; text-transform: uppercase;">120 Minutes of wonder</p>
          <div class="royal-price">
            <span style="font-size: 1.5rem; vertical-align: top; -webkit-text-fill-color: #d4af37;">$</span>399
          </div>
          <ul style="list-style: none; padding: 0; margin-bottom: 2.5rem; text-align: left;">
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #d1cdd8;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 2 Characters/Magicians</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #d1cdd8;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Complete Stage Show</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #d1cdd8;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Custom Party Favors</li>
            <li style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 12px; color: #d1cdd8;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Special Grand Finale</li>
          </ul>
          <a href="packages.html" class="pkg-btn-royal-outline">Select Package</a>
        </div>

      </div>
    </div>
  </section>
  
  <!-- Magical Party Experiences -->"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(pre_content + new_sections + post_content)
