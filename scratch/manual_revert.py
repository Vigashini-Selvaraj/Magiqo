file_path = 'c:/Users/vigas/Desktop/magiqo/entertainer_detail.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
original_css = '''
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
      background: var(--color-surface);
      padding: 0.5rem 1.5rem;
      border-radius: var(--radius-pill);
      box-shadow: 0 5px 15px rgba(0,0,0,0.05);
      font-weight: bold;
      color: #ff9800;
      font-size: 1.25rem;
      margin-bottom: 2rem;
    }
'''

# Find boundaries for CSS
start_css = content.find('/* 1. Entertainer Hero Section (Redesigned) */')
end_css = content.find('/* 2. Content Sections */')
if start_css != -1 and end_css != -1:
    content = content[:start_css] + original_css + '\n\n    ' + content[end_css:]


# Restore HTML
original_html = '''  <!-- 1. Entertainer Hero -->
  <section class="ent-detail-hero">
    <div class="container profile-layout">
      <div class="profile-image-wrap">
        <img id="ent-img" src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias the Magician">
      </div>
      <div class="profile-info">
        <h1 id="ent-name">Elias</h1>
        <div class="profile-specialty" id="ent-title">Master Magician & Illusionist</div>
        <div class="profile-rating">
          <svg viewBox="0 0 24 24" style="width:20px;height:20px;fill:#ff9800;"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg> 
          Rating: 5.0/5 (120+ Reviews)
        </div>
        <p style="font-size: 1.2rem; color: var(--color-text-light); line-height: 1.6; margin-bottom: 2rem;">
          Bring the wonder of true magic to your child's special day. Elias blends mind-bending illusions, hilarious comedy, and fully interactive stage shows that will leave kids and parents alike speechless.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
           <a href="#book-now" class="btn btn-animated" style="background: var(--color-primary); color: white; padding: 1.25rem 2.5rem; font-size: 1.1rem; border-radius: var(--radius-pill); box-shadow: 0 10px 20px rgba(218, 47, 95, 0.3);">Book <span id="ent-book-btn">Elias</span> Now</a>
           <a href="#watch" class="btn btn-animated" style="background: var(--color-surface); color: #3895c8; border: 2px solid #3895c8; padding: 1.25rem 2.5rem; font-size: 1.1rem; border-radius: var(--radius-pill);">Watch Video</a>
        </div>
      </div>
    </div>
  </section>'''

# Find boundaries for HTML
start_html = content.find('<!-- 1. Entertainer Hero -->')
end_html = content.find('<!-- 2. Our Promise -->')
if start_html != -1 and end_html != -1:
    content = content[:start_html] + original_html + '\n\n  ' + content[end_html:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
