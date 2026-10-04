import re

filepath = r'c:\Users\vigas\Desktop\magiqo\join.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Title
old_hero_title = '<h1 class="join-title">Create <span class="text-pink">Magic</span> With Us</h1>'
new_hero_title = '<h1 class="join-title" style="text-transform: capitalize;"><span class="text-pink">Create Magic</span> <span class="text-blue">With Us</span></h1>'
content = content.replace(old_hero_title, new_hero_title)

# 2. Update Why Join Title
old_why_join_title = '<h2 class="section-title">Why Join <span class="text-blue">Magiqo?</span></h2>'
new_why_join_title = '<h2 class="section-title"><span class="text-pink">Why Join</span> <span class="text-blue">Magiqo?</span></h2>'
content = content.replace(old_why_join_title, new_why_join_title)

# 3. Redesign Career Opportunities
# We will replace the entire career opportunities section CSS and HTML.
old_career_css = '''/* Career Opportunities */
    .jobs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; }
    .job-card {
      background: linear-gradient(145deg, var(--color-surface), rgba(0,0,0,0.2));
      border: 1px solid var(--color-border);
      border-radius: 20px;
      padding: 40px;
      position: relative;
      overflow: hidden;
      transition: 0.4s;
    }
    .job-card::before {
      content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%;
      background: linear-gradient(to bottom, var(--color-primary), #3895c8);
    }
    .job-card:hover { transform: translateY(-5px); border-color: rgba(210, 75, 118, 0.5); }
    .job-title { font-size: 1.5rem; margin-bottom: 10px; color: var(--color-text); }
    .job-type { display: inline-block; padding: 5px 15px; background: rgba(56,149,200,0.1); color: #3895c8; border-radius: 50px; font-size: 0.85rem; font-weight: bold; margin-bottom: 20px; }'''

new_career_css = '''/* Career Opportunities Redesign */
    .jobs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; }
    .job-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 16px;
      padding: 35px 30px;
      position: relative;
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      height: 100%;
    }
    .job-card:hover { 
      transform: translateY(-8px); 
      box-shadow: 0 15px 35px rgba(0,0,0,0.2); 
      border-color: var(--color-primary); 
    }
    .job-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
    .job-icon { width: 50px; height: 50px; border-radius: 12px; background: rgba(210, 75, 118, 0.1); color: var(--color-primary); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; }
    .job-type { padding: 6px 14px; background: rgba(56,149,200,0.1); color: #3895c8; border-radius: 30px; font-size: 0.8rem; font-weight: 600; }
    .job-title { font-size: 1.4rem; margin-bottom: 12px; color: var(--color-text); font-family: var(--font-heading); }
    .job-desc { color: var(--color-text-light); font-size: 0.95rem; line-height: 1.6; margin-bottom: 25px; flex-grow: 1; }
    .job-apply-btn { align-self: flex-start; color: var(--color-text); text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; transition: 0.3s; }
    .job-apply-btn:hover { color: var(--color-primary); gap: 12px; }'''
content = content.replace(old_career_css, new_career_css)

# HTML for Career
old_career_html = '''<div class="jobs-grid">
      <div class="job-card">
        <span class="job-type">Full-Time</span>
        <h3 class="job-title">Event Planner</h3>
        <p class="color-light" style="margin-bottom: 20px;">Coordinate and execute magical celebrations. Must have immense attention to detail and vendor management skills.</p>
        <a href="#apply-form" class="btn" style="border: 1px solid var(--color-primary); color: white; padding: 10px 25px; border-radius: 50px;">Apply <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <span class="job-type">Freelance / Gig</span>
        <h3 class="job-title">Professional Entertainer</h3>
        <p class="color-light" style="margin-bottom: 20px;">Magicians, clowns, princesses, and musicians. Bring your unique act to our exclusive client events.</p>
        <a href="#apply-form" class="btn" style="border: 1px solid var(--color-primary); color: white; padding: 10px 25px; border-radius: 50px;">Apply <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <span class="job-type">Contract</span>
        <h3 class="job-title">Event Photographer</h3>
        <p class="color-light" style="margin-bottom: 20px;">Capture the smiles, the cake cutting, and the magic. Requires portfolio and equipment.</p>
        <a href="#apply-form" class="btn" style="border: 1px solid var(--color-primary); color: white; padding: 10px 25px; border-radius: 50px;">Apply <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <span class="job-type">Remote / Full-Time</span>
        <h3 class="job-title">Content Writer & Designer</h3>
        <p class="color-light" style="margin-bottom: 20px;">Write magical blog posts and design stunning social media assets to grow the Magiqo brand.</p>
        <a href="#apply-form" class="btn" style="border: 1px solid var(--color-primary); color: white; padding: 10px 25px; border-radius: 50px;">Apply <i class="fa-solid fa-arrow-right"></i></a>
      </div>
    </div>'''
new_career_html = '''<div class="jobs-grid">
      <div class="job-card">
        <div class="job-header">
          <div class="job-icon"><i class="fa-solid fa-calendar-check"></i></div>
          <span class="job-type">Full-Time</span>
        </div>
        <h3 class="job-title">Event Planner</h3>
        <p class="job-desc">Coordinate and execute magical celebrations. Bring your immense attention to detail and vendor management skills to our dynamic team.</p>
        <a href="#apply-form" class="job-apply-btn">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <div class="job-header">
          <div class="job-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
          <span class="job-type">Freelance / Gig</span>
        </div>
        <h3 class="job-title">Professional Entertainer</h3>
        <p class="job-desc">Magicians, clowns, princesses, and musicians! Bring your unique acts to our exclusive client events and parties.</p>
        <a href="#apply-form" class="job-apply-btn">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <div class="job-header">
          <div class="job-icon"><i class="fa-solid fa-camera"></i></div>
          <span class="job-type">Contract</span>
        </div>
        <h3 class="job-title">Event Photographer</h3>
        <p class="job-desc">Capture the smiles, the cake cutting, and the magic. Help our clients freeze their unforgettable moments in time.</p>
        <a href="#apply-form" class="job-apply-btn">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <div class="job-header">
          <div class="job-icon"><i class="fa-solid fa-pen-nib"></i></div>
          <span class="job-type">Remote</span>
        </div>
        <h3 class="job-title">Content Writer & Designer</h3>
        <p class="job-desc">Write magical blog posts and design stunning social media assets to grow the Magiqo brand across digital platforms.</p>
        <a href="#apply-form" class="job-apply-btn">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <div class="job-header">
          <div class="job-icon"><i class="fa-solid fa-utensils"></i></div>
          <span class="job-type">Part-Time</span>
        </div>
        <h3 class="job-title">Catering & Hospitality</h3>
        <p class="job-desc">Provide top-tier service and delicious experiences at our VIP events. Ensure every guest leaves happy and full.</p>
        <a href="#apply-form" class="job-apply-btn">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div class="job-card">
        <div class="job-header">
          <div class="job-icon"><i class="fa-solid fa-bullhorn"></i></div>
          <span class="job-type">Full-Time</span>
        </div>
        <h3 class="job-title">Marketing Manager</h3>
        <p class="job-desc">Lead our promotional campaigns and manage our public relations to help Magiqo reach new audiences globally.</p>
        <a href="#apply-form" class="job-apply-btn">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
      </div>
    </div>'''
content = content.replace(old_career_html, new_career_html)


# 4. Redesign Application Process
old_process_css = '''/* Process Flow */
    .process-container { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 30px; position: relative; }
    .process-step { flex: 1; min-width: 200px; text-align: center; position: relative; z-index: 2; }
    .step-circle {
      width: 80px; height: 80px; border-radius: 50%;
      background: var(--color-surface); border: 2px solid var(--color-primary);
      display: flex; align-items: center; justify-content: center;
      font-size: 2rem; color: var(--color-primary); margin: 0 auto 20px;
      box-shadow: 0 10px 30px rgba(210, 75, 118, 0.2);
    }
    .process-step h4 { font-size: 1.2rem; margin-bottom: 10px; }'''

new_process_css = '''/* Process Timeline Redesign */
    .process-container { 
      display: grid; 
      grid-template-columns: repeat(4, 1fr); 
      gap: 20px; 
      position: relative; 
      margin-top: 40px;
    }
    @media(max-width: 900px) { .process-container { grid-template-columns: repeat(2, 1fr); gap: 40px; } }
    @media(max-width: 500px) { .process-container { grid-template-columns: 1fr; gap: 40px; } }
    
    .process-step { 
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 20px;
      padding: 40px 25px;
      text-align: center;
      position: relative;
      transition: 0.3s;
    }
    .process-step:hover {
      transform: translateY(-5px);
      border-color: #3895c8;
      box-shadow: 0 10px 30px rgba(56, 149, 200, 0.15);
    }
    .step-number {
      position: absolute;
      top: -20px;
      left: 50%;
      transform: translateX(-50%);
      width: 40px;
      height: 40px;
      background: var(--color-primary);
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      font-size: 1.2rem;
      box-shadow: 0 5px 15px rgba(210, 75, 118, 0.4);
    }
    .process-step i { font-size: 2.5rem; color: #3895c8; margin-bottom: 20px; }
    .process-step h4 { font-size: 1.3rem; margin-bottom: 12px; color: var(--color-text); }
    .process-step p { color: var(--color-text-light); font-size: 0.95rem; line-height: 1.5; }'''
content = content.replace(old_process_css, new_process_css)

old_process_html = '''<div class="process-container">
      <div class="process-step">
        <div class="step-circle"><i class="fa-solid fa-file-signature"></i></div>
        <h4>1. Apply Online</h4>
        <p class="color-light">Submit your resume and portfolio using the form below.</p>
      </div>
      <div class="process-step">
        <div class="step-circle"><i class="fa-solid fa-magnifying-glass"></i></div>
        <h4>2. We Review</h4>
        <p class="color-light">Our team evaluates your skills, passion, and experience.</p>
      </div>
      <div class="process-step">
        <div class="step-circle"><i class="fa-solid fa-video"></i></div>
        <h4>3. Interview / Audition</h4>
        <p class="color-light">Chat with us or perform a quick audition (for entertainers).</p>
      </div>
      <div class="process-step">
        <div class="step-circle"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
        <h4>4. Welcome!</h4>
        <p class="color-light">Join the crew and start making magic happen.</p>
      </div>
    </div>'''
new_process_html = '''<div class="process-container">
      <div class="process-step">
        <div class="step-number">1</div>
        <i class="fa-solid fa-laptop-file"></i>
        <h4>Online Apply</h4>
        <p>Submit your resume and portfolio directly through our magic application form.</p>
      </div>
      <div class="process-step">
        <div class="step-number">2</div>
        <i class="fa-solid fa-user-check"></i>
        <h4>We Review</h4>
        <p>Our dedicated hiring team carefully evaluates your skills, passion, and experience.</p>
      </div>
      <div class="process-step">
        <div class="step-number">3</div>
        <i class="fa-solid fa-microphone-lines"></i>
        <h4>Interview & Audition</h4>
        <p>Have a chat with us, or perform a quick virtual audition if you're an entertainer.</p>
      </div>
      <div class="process-step">
        <div class="step-number">4</div>
        <i class="fa-solid fa-champagne-glasses"></i>
        <h4>Welcome!</h4>
        <p>Congratulations! You join the Magiqo family and start bringing joy to events.</p>
      </div>
    </div>'''
content = content.replace(old_process_html, new_process_html)


# 5. Remove Meet the Magic Makers
team_regex = r'<!-- 7\. MEET OUR TEAM -->.*?<!-- 8\. LIFE AT MAGIQO -->'
content = re.sub(team_regex, '<!-- 8. LIFE AT MAGIQO -->', content, flags=re.DOTALL)


# 6. Final CTA Text to White
cta_regex = r'<h2 style="font-family: var\(--font-magic\); font-size: 3rem; margin-bottom: 20px; color: white;">Ready to start your journey\?</h2>'
new_cta = '<h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 20px; color: white !important;">Ready to start your journey?</h2>'
content = content.replace(cta_regex, new_cta)
# Just to be absolutely sure the text is white (it already had color: white, but the user explicitly requested it, maybe there's an override)
cta_h2_regex = r'<h2[^>]*>Ready to start your journey\?</h2>'
content = re.sub(cta_h2_regex, '<h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 20px; color: #ffffff !important;">Ready to start your journey?</h2>', content)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
