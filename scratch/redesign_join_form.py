import re

def redesign_join_page():
    file_path = r'c:\Users\vigas\Desktop\magiqo\join.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Google Fonts if missing
    google_fonts = '''  <!-- Core Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">'''

    if 'family=Outfit' not in content:
        content = content.replace('<link rel="stylesheet" href="css/style.css">', google_fonts + '\n  <link rel="stylesheet" href="css/style.css">')

    # 2. Replace CSS for .apply-section, .apply-form-container, .form-control, etc.
    old_form_css = re.compile(
        r'/\* Form Section \*/\s*\.apply-section\s*\{.*?\.form-control::placeholder\s*\{[^}]*\}',
        re.DOTALL
    )

    new_form_css = '''/* Form Section - Redesigned to match Magiqo Light & Dark theme */
    .apply-section {
      background: radial-gradient(circle at 10% 20%, rgba(201, 42, 88, 0.05) 0%, transparent 45%),
                  radial-gradient(circle at 90% 80%, rgba(56, 149, 200, 0.06) 0%, transparent 45%),
                  var(--color-bg);
      position: relative;
      padding: 100px 20px;
    }
    .apply-form-container {
      position: relative;
      z-index: 2;
      max-width: 760px;
      margin: 0 auto;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 28px;
      padding: clamp(35px, 5vw, 60px);
      box-shadow: 0 20px 50px var(--color-shadow);
      transition: background 0.3s ease, border-color 0.3s ease;
    }
    .apply-form-title {
      font-family: var(--font-magic);
      font-size: clamp(2.3rem, 4vw, 3.2rem);
      font-weight: 800;
      text-align: center;
      margin-bottom: 12px;
      line-height: 1.2;
    }
    .apply-form-subtitle {
      text-align: center;
      color: var(--color-text-light);
      font-size: 1.1rem;
      margin-bottom: 40px;
      line-height: 1.6;
    }
    .form-group {
      margin-bottom: 22px;
    }
    .form-group label {
      display: block;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--color-text);
      margin-bottom: 8px;
    }
    .form-control {
      width: 100%;
      padding: 15px 20px;
      border-radius: var(--radius-md);
      background: var(--color-bg);
      border: 1.5px solid var(--color-border);
      color: var(--color-text);
      font-family: var(--font-body);
      font-size: 1rem;
      transition: all 0.25s ease;
      box-sizing: border-box;
    }
    .form-control:focus {
      border-color: var(--color-primary);
      outline: none;
      background: var(--color-surface);
      box-shadow: 0 0 0 4px rgba(201, 42, 88, 0.12);
    }
    .form-control::placeholder {
      color: var(--color-text-light);
      opacity: 0.7;
    }
    select.form-control {
      cursor: pointer;
      appearance: none;
      background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23C92A58' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
      background-repeat: no-repeat;
      background-position: right 18px center;
      background-size: 16px;
    }
    select.form-control option {
      background: var(--color-surface);
      color: var(--color-text);
      padding: 10px;
    }
    .file-upload-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 20px;
      background: var(--color-bg);
      border: 2px dashed var(--color-border);
      border-radius: var(--radius-md);
      cursor: pointer;
      color: var(--color-text);
      transition: all 0.3s ease;
      text-align: center;
      gap: 6px;
      width: 100%;
      box-sizing: border-box;
    }
    .file-upload-box:hover {
      border-color: var(--color-primary);
      background: rgba(201, 42, 88, 0.04);
      color: var(--color-primary);
    }
    .file-upload-box i {
      font-size: 1.8rem;
      color: var(--color-primary);
      margin-bottom: 4px;
    }
    .file-upload-box span {
      font-weight: 700;
      font-size: 0.95rem;
    }
    .file-upload-box small {
      color: var(--color-text-light);
      font-size: 0.85rem;
    }'''

    content = old_form_css.sub(new_form_css, content)

    # 3. Replace HTML for section 6. APPLICATION FORM
    old_form_html = re.compile(
        r'<!-- 6\. APPLICATION FORM -->\s*<section id="apply-form" class="apply-section reveal">.*?</section>',
        re.DOTALL
    )

    new_form_html = '''<!-- 6. APPLICATION FORM -->
  <section id="apply-form" class="apply-section reveal">
    <div class="apply-form-container">
      <h2 class="apply-form-title"><span class="text-pink">Submit Your</span> <span class="text-blue">Application</span></h2>
      <p class="apply-form-subtitle">Tell us about yourself and why you'd be a perfect fit for the Magiqo family.</p>
      
      <form onsubmit="event.preventDefault(); this.innerHTML='<div style=\\'text-align:center; padding: 50px 20px;\\'><div style=\\'width: 75px; height: 75px; margin: 0 auto 20px; background: rgba(16, 185, 129, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #10B981; font-size: 2.5rem;\\'><i class=\\'fa-solid fa-circle-check\\'></i></div><h3 style=\\'font-family: var(--font-magic); font-size: 2.2rem; color: var(--color-text); margin-bottom: 12px;\\'>Application Received!</h3><p style=\\'color: var(--color-text-light); font-size: 1.1rem; max-width: 500px; margin: 0 auto; line-height: 1.6;\\'>Thank you for applying. Our talent curation team will carefully review your details and reach out within 3 business days.</p></div>';">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
          <div class="form-group">
            <label>First Name</label>
            <input type="text" class="form-control" placeholder="e.g. Alexander" required>
          </div>
          <div class="form-group">
            <label>Last Name</label>
            <input type="text" class="form-control" placeholder="e.g. Wright" required>
          </div>
        </div>
        <div class="form-group">
          <label>Email Address</label>
          <input type="email" class="form-control" placeholder="name@example.com" required>
        </div>
        <div class="form-group">
          <label>Role Applied For</label>
          <select class="form-control" required>
            <option value="" disabled selected>Select Role you are applying for</option>
            <option value="entertainer">Entertainer / Master Magician</option>
            <option value="character">Character Performer (Princess / Superhero)</option>
            <option value="activity">Activity Specialist (Face Painter / Balloon Artist)</option>
            <option value="planner">Event Coordinator & Planner</option>
            <option value="photo">Event Photographer</option>
            <option value="other">Other Creative Talent</option>
          </select>
        </div>
        <div class="form-group">
          <label>Portfolio / Showreel URL (Optional)</label>
          <input type="url" class="form-control" placeholder="https://instagram.com/yourhandle or portfolio link">
        </div>
        <div class="form-group">
          <label>Why do you want to join Magiqo?</label>
          <textarea class="form-control" rows="4" placeholder="Briefly describe your experience, performance style, and what makes your work magical..." required></textarea>
        </div>
        <div class="form-group">
          <label>Resume / CV</label>
          <label class="file-upload-box">
            <i class="fa-solid fa-cloud-arrow-up"></i>
            <span>Upload Resume (PDF, DOC, DOCX)</span>
            <small>Drag & drop or click to browse (Max 15MB)</small>
            <input type="file" style="display: none;" accept=".pdf,.doc,.docx" onchange="this.previousElementSibling.textContent = this.files[0] ? this.files[0].name : 'Upload Resume (PDF, DOC, DOCX)'">
          </label>
        </div>
        <button type="submit" class="btn btn-primary btn-full btn-lg" style="margin-top: 15px; cursor: pointer; padding: 16px; font-weight: 800; font-size: 1.05rem;">
          Submit Application <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i>
        </button>
      </form>
    </div>
  </section>'''

    content = old_form_html.sub(new_form_html, content)

    # 4. Replace Unsplash image in Life at Magiqo
    content = content.replace(
        'https://images.unsplash.com/photo-1608889476561-6242cfdbf622?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
        'assets/images/interactive_party_show.jpg'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully redesigned 'Submit Your Application' form in join.html to match light & dark theme seamlessly!")

if __name__ == '__main__':
    redesign_join_page()
