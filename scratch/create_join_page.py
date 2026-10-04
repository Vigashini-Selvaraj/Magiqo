import os

filepath = r'c:\Users\vigas\Desktop\magiqo\join.html'

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Join Our Team | Magiqo</title>

  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* Hero Section */
    .join-hero {
      padding: 180px 20px 100px;
      text-align: center;
      background: radial-gradient(circle at 50% 50%, rgba(210, 75, 118, 0.15) 0%, var(--color-bg) 60%);
      position: relative;
      overflow: hidden;
    }
    .join-title {
      font-family: var(--font-magic);
      font-size: clamp(3rem, 5vw, 5rem);
      margin-bottom: 20px;
      color: var(--color-text);
      line-height: 1.2;
    }
    .join-subtitle {
      font-size: 1.25rem;
      color: var(--color-text-light);
      max-width: 700px;
      margin: 0 auto 40px;
      line-height: 1.6;
    }

    /* Section Global */
    .section-container { max-width: 1200px; margin: 0 auto 100px; padding: 0 20px; }
    .section-title { font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 50px; color: var(--color-text); }
    .text-pink { color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); }
    .text-blue { color: #3895c8; -webkit-text-fill-color: #3895c8; }

    /* Why Join Us */
    .benefits-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
    .benefit-card {
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 20px;
      padding: 40px 30px;
      text-align: center;
      transition: transform 0.4s, box-shadow 0.4s;
    }
    .benefit-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 20px 40px rgba(56, 149, 200, 0.15);
      border-color: #3895c8;
    }
    .benefit-icon { font-size: 3rem; color: var(--color-primary); margin-bottom: 20px; transition: 0.3s; }
    .benefit-card:hover .benefit-icon { transform: scale(1.1); color: #3895c8; }
    .benefit-card h3 { margin-bottom: 15px; font-size: 1.3rem; }
    
    /* Career Opportunities */
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
    .job-type { display: inline-block; padding: 5px 15px; background: rgba(56,149,200,0.1); color: #3895c8; border-radius: 50px; font-size: 0.85rem; font-weight: bold; margin-bottom: 20px; }
    
    /* Process Flow */
    .process-container { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 30px; position: relative; }
    .process-step { flex: 1; min-width: 200px; text-align: center; position: relative; z-index: 2; }
    .step-circle {
      width: 80px; height: 80px; border-radius: 50%;
      background: var(--color-surface); border: 2px solid var(--color-primary);
      display: flex; align-items: center; justify-content: center;
      font-size: 2rem; color: var(--color-primary); margin: 0 auto 20px;
      box-shadow: 0 10px 30px rgba(210, 75, 118, 0.2);
    }
    .process-step h4 { font-size: 1.2rem; margin-bottom: 10px; }

    /* Form Section */
    .apply-section {
      background: url('assets/images/magic_show_party_1790842468826.jpg') center/cover fixed;
      position: relative;
      padding: 100px 20px;
    }
    .apply-section::before { content: ''; position: absolute; inset: 0; background: rgba(0,0,0,0.85); }
    .apply-form-container {
      position: relative; z-index: 2;
      max-width: 700px; margin: 0 auto;
      background: rgba(255,255,255,0.05); backdrop-filter: blur(15px);
      border: 1px solid rgba(255,255,255,0.1); border-radius: 24px;
      padding: 50px; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    .form-group { margin-bottom: 25px; }
    .form-control {
      width: 100%; padding: 15px 20px; border-radius: 12px;
      background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.2);
      color: white; font-size: 1rem; transition: 0.3s;
    }
    .form-control:focus { border-color: var(--color-primary); outline: none; background: rgba(0,0,0,0.7); }
    .form-control::placeholder { color: rgba(255,255,255,0.5); }
    
    /* Team & Life */
    .team-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }
    .team-card { text-align: center; }
    .team-img { width: 150px; height: 150px; border-radius: 50%; object-fit: cover; border: 4px solid var(--color-surface); box-shadow: 0 15px 30px rgba(0,0,0,0.3); margin-bottom: 20px; transition: 0.4s; }
    .team-card:hover .team-img { transform: scale(1.1) rotate(5deg); border-color: var(--color-primary); }
    
    .gallery-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
    .gallery-item { height: 250px; border-radius: 16px; overflow: hidden; cursor: pointer; }
    .gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: 0.5s; filter: grayscale(50%); }
    .gallery-item:hover img { transform: scale(1.05); filter: grayscale(0%); }

    /* FAQ */
    .faq-container details { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; margin-bottom: 15px; overflow: hidden; }
    .faq-container summary { padding: 20px; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; }
    .faq-container summary::-webkit-details-marker { display: none; }
    .faq-container summary::after { content: '+'; font-size: 1.5rem; color: var(--color-primary); }
    .faq-container details[open] summary::after { content: '-'; }
    .faq-container .faq-content { padding: 0 20px 20px; color: var(--color-text-light); line-height: 1.6; }
    
    /* CTA */
    .cta-section { background: var(--color-primary); padding: 100px 20px; text-align: center; }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <div id="navbar"></div>

  <!-- 1. HERO SECTION -->
  <section class="join-hero reveal">
    <h1 class="join-title">Create <span class="text-pink">Magic</span> With Us</h1>
    <p class="join-subtitle">Are you passionate about making people smile? We are always looking for creative, energetic, and dedicated individuals to join the Magiqo family. Turn your passion into a career.</p>
    <a href="#apply-form" class="btn btn-primary" style="padding: 15px 40px; font-size: 1.2rem; border-radius: 50px;">Apply Now <i class="fa-solid fa-arrow-down" style="margin-left: 10px;"></i></a>
  </section>

  <!-- 2. WHY JOIN MAGIQO -->
  <section class="section-container reveal">
    <h2 class="section-title">Why Join <span class="text-blue">Magiqo?</span></h2>
    <div class="benefits-grid">
      <div class="benefit-card">
        <i class="fa-solid fa-face-smile-beam benefit-icon"></i>
        <h3>Creative Freedom</h3>
        <p class="color-light">We encourage out-of-the-box thinking. Bring your wildest entertainment ideas to life.</p>
      </div>
      <div class="benefit-card">
        <i class="fa-solid fa-calendar-check benefit-icon"></i>
        <h3>Flexible Schedule</h3>
        <p class="color-light">Choose events that fit your availability. Perfect for freelancers and part-time magicians.</p>
      </div>
      <div class="benefit-card">
        <i class="fa-solid fa-users benefit-icon"></i>
        <h3>Amazing Team Culture</h3>
        <p class="color-light">Work alongside passionate planners, designers, and entertainers in a highly supportive environment.</p>
      </div>
    </div>
  </section>

  <!-- 3. CAREER OPPORTUNITIES -->
  <section class="section-container reveal">
    <h2 class="section-title"><span class="text-pink">Career</span> Opportunities</h2>
    <div class="jobs-grid">
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
    </div>
  </section>

  <!-- 4. WHAT WE LOOK FOR & 5. HOW TO JOIN -->
  <section class="section-container reveal">
    <h2 class="section-title">The <span class="text-blue">Application</span> Process</h2>
    <div class="process-container">
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
    </div>
  </section>

  <!-- 6. APPLICATION FORM -->
  <section id="apply-form" class="apply-section reveal">
    <div class="apply-form-container">
      <h2 style="font-family: var(--font-magic); font-size: 2.5rem; text-align: center; margin-bottom: 10px; color: white;">Submit Your Application</h2>
      <p style="text-align: center; color: rgba(255,255,255,0.7); margin-bottom: 40px;">Tell us about yourself and why you'd be a perfect fit.</p>
      
      <form onsubmit="event.preventDefault(); this.innerHTML='<div style=\\'text-align:center; padding: 50px 0;\\'><i class=\\'fa-solid fa-circle-check\\' style=\\'font-size:4rem; color:var(--color-primary); margin-bottom:20px;\\'></i><h3 style=\\'font-size:2rem; color:white;\\'>Application Received!</h3><p style=\\'color:#ccc;\\'>Thank you for applying. Our hiring team will review your details and get back to you soon.</p></div>';">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
          <div class="form-group">
            <input type="text" class="form-control" placeholder="First Name" required>
          </div>
          <div class="form-group">
            <input type="text" class="form-control" placeholder="Last Name" required>
          </div>
        </div>
        <div class="form-group">
          <input type="email" class="form-control" placeholder="Email Address" required>
        </div>
        <div class="form-group">
          <select class="form-control" required style="color: white;">
            <option value="" disabled selected>Select Role you are applying for</option>
            <option value="planner" style="color: black;">Event Planner</option>
            <option value="entertainer" style="color: black;">Entertainer / Performer</option>
            <option value="photo" style="color: black;">Photographer</option>
            <option value="design" style="color: black;">Designer / Developer</option>
            <option value="other" style="color: black;">Other</option>
          </select>
        </div>
        <div class="form-group">
          <input type="url" class="form-control" placeholder="Portfolio / Website URL (Optional)">
        </div>
        <div class="form-group">
          <textarea class="form-control" rows="4" placeholder="Why do you want to join Magiqo? Briefly describe your skills and motivation." required></textarea>
        </div>
        <div class="form-group" style="text-align: center;">
          <label style="display: inline-block; padding: 15px 30px; background: rgba(255,255,255,0.1); border: 1px dashed rgba(255,255,255,0.3); border-radius: 12px; cursor: pointer; color: white; width: 100%;">
            <i class="fa-solid fa-cloud-arrow-up" style="margin-right: 10px;"></i> Upload Resume (PDF/DOC)
            <input type="file" style="display: none;" accept=".pdf,.doc,.docx">
          </label>
        </div>
        <button type="submit" class="btn btn-primary" style="width: 100%; padding: 15px; font-size: 1.1rem; border-radius: 12px; margin-top: 10px; border: none; font-weight: bold; cursor: pointer;">Submit Application</button>
      </form>
    </div>
  </section>

  <!-- 7. MEET OUR TEAM -->
  <section class="section-container reveal" style="margin-top: 100px;">
    <h2 class="section-title">Meet The <span class="text-pink">Magic</span> Makers</h2>
    <div class="team-grid">
      <div class="team-card">
        <img src="assets/images/james_boy_smile.jpg" alt="CEO" class="team-img">
        <h3>Michael Vance</h3>
        <p class="text-blue" style="margin-bottom: 10px;">Founder & CEO</p>
        <p class="color-light" style="font-size: 0.9rem;">Former stage illusionist turned event mastermind.</p>
      </div>
      <div class="team-card">
        <img src="assets/images/cute_kids_clapping_1790833571210.jpg" alt="Head Planner" class="team-img">
        <h3>Sarah Jenkins</h3>
        <p class="text-pink" style="margin-bottom: 10px;">Head of Event Planning</p>
        <p class="color-light" style="font-size: 0.9rem;">Organizes chaos into breathtaking celebrations.</p>
      </div>
      <div class="team-card">
        <img src="assets/images/about_kids_birthday.jpg" alt="Lead Entertainer" class="team-img">
        <h3>David 'Zappo' Lee</h3>
        <p class="text-blue" style="margin-bottom: 10px;">Lead Entertainer</p>
        <p class="color-light" style="font-size: 0.9rem;">Specializes in interactive comedy and grand illusions.</p>
      </div>
    </div>
  </section>

  <!-- 8. LIFE AT MAGIQO -->
  <section class="section-container reveal">
    <h2 class="section-title">Life at <span class="text-blue">Magiqo</span></h2>
    <p style="text-align: center; color: var(--color-text-light); margin-bottom: 40px; max-width: 600px; margin-left: auto; margin-right: auto;">We work hard to create unforgettable experiences, but we always make sure to celebrate our own team's wins too!</p>
    <div class="gallery-grid">
      <div class="gallery-item"><img src="assets/images/superhero_party_1790842695325.jpg" alt="Life 1"></div>
      <div class="gallery-item"><img src="assets/images/princess_party_1790842645232.jpg" alt="Life 2"></div>
      <div class="gallery-item"><img src="assets/images/magic_show_party_1790842468826.jpg" alt="Life 3"></div>
    </div>
  </section>

  <!-- 9. FAQs -->
  <section class="section-container reveal">
    <h2 class="section-title">Career <span class="text-pink">FAQs</span></h2>
    <div class="faq-container" style="max-width: 800px; margin: 0 auto;">
      <details>
        <summary>Do you hire freelancers for events?</summary>
        <div class="faq-content">Yes! The majority of our entertainers, photographers, and caterers operate on a gig/freelance basis. You can pick up events that match your schedule.</div>
      </details>
      <details>
        <summary>Are there internship opportunities?</summary>
        <div class="faq-content">Absolutely. We offer paid summer internships for event management and marketing students looking to get hands-on experience in the entertainment industry.</div>
      </details>
      <details>
        <summary>What is the audition process like for entertainers?</summary>
        <div class="faq-content">If your resume/portfolio is shortlisted, we'll invite you for a 15-minute live or virtual audition where you can perform your best routine for our panel.</div>
      </details>
      <details>
        <summary>Where is Magiqo located?</summary>
        <div class="faq-content">Our core planning team works hybrid in our downtown office, but our entertainers operate throughout the entire tri-state area.</div>
      </details>
    </div>
  </section>

  <!-- 10. FINAL CTA -->
  <section class="cta-section reveal">
    <div class="container text-center" style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
      <h2 style="font-family: var(--font-magic); font-size: 3rem; margin-bottom: 20px; color: white;">Ready to start your journey?</h2>
      <p style="font-size: 1.25rem; max-width: 600px; margin: 0 auto 40px; line-height: 1.6; color: rgba(255,255,255,0.9);">
        Don't miss the chance to do what you love while making people smile.
      </p>
      <a href="#apply-form" class="btn" style="background: white; color: var(--color-primary); padding: 1.25rem 3.5rem; font-size: 1.2rem; border-radius: 50px; font-weight: bold; text-decoration: none; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">Apply Now</a>
    </div>
  </section>

  <!-- 11. FOOTER -->
  <div id="footer"></div>

  <script src="js/components.js"></script>
  <script src="js/theme.js"></script>
  <script>
    // Reveal animations logic is assumed to be in components.js or theme.js, 
    // but we can add a simple observer here to ensure .reveal classes animate
    const observerOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(30px)';
      el.style.transition = 'all 0.8s ease-out';
      observer.observe(el);
    });
  </script>
</body>
</html>
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_content)
