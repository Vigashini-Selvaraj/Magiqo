import re

filepath = r'c:\Users\vigas\Desktop\magiqo\packages.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Change all btn-secondary for Choose Package to btn-primary
# The user wants "Choose package" buttons to be pink always and hover to sky blue.
# Currently they use `btn-secondary` (which I changed to blue earlier) or `btn-primary`.
# I will change all instances of "class="btn btn-secondary" style="width: 100%;"" to btn-primary
content = content.replace('class="btn btn-secondary" style="width: 100%;">Choose Package</a>', 'class="btn btn-primary" style="width: 100%;">Choose Package</a>')
content = content.replace('class="btn btn-primary" style="width: 100%;">Choose Package</a>', 'class="btn btn-primary choose-package-btn" style="width: 100%;">Choose Package</a>')

# Add custom hover style for choose-package-btn
custom_css = '''
    .choose-package-btn:hover {
      background: #3895c8 !important;
      color: white !important;
      transform: translateY(-3px);
    }
'''
content = content.replace('/* Custom Packages Styles using strict Magiqo variables */', '/* Custom Packages Styles using strict Magiqo variables */' + custom_css)

# Redesign the comparison table
table_pattern = re.compile(r'<div class="compare-table-wrapper reveal">.*?</div>', re.DOTALL)

modern_compare_html = '''
      <style>
        .modern-compare-container {
          overflow-x: auto;
          padding-bottom: 2rem;
          margin-top: 3rem;
        }
        .modern-compare-grid {
          display: flex;
          gap: 1.5rem;
          min-width: 900px; /* Ensure horizontal scroll on small screens */
        }
        .compare-column {
          flex: 1;
          background: var(--color-surface);
          border-radius: 20px;
          overflow: hidden;
          box-shadow: 0 10px 30px rgba(0,0,0,0.05);
          display: flex;
          flex-direction: column;
          border-top: 4px solid var(--color-primary);
          transition: transform 0.3s, box-shadow 0.3s;
        }
        .compare-column:hover {
          transform: translateY(-10px);
          box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        .compare-img {
          width: 100%;
          height: 120px;
          object-fit: cover;
        }
        .compare-header {
          padding: 1.5rem 1rem;
          text-align: center;
          border-bottom: 1px solid rgba(0,0,0,0.05);
        }
        .compare-header h3 {
          font-family: var(--font-magic);
          font-size: 1.4rem;
          color: #3895c8;
          margin-bottom: 0.5rem;
        }
        .compare-price {
          font-size: 1.5rem;
          font-weight: bold;
          color: var(--color-primary);
        }
        .compare-features {
          list-style: none;
          padding: 0;
          margin: 0;
          flex-grow: 1;
        }
        .compare-features li {
          padding: 1rem;
          text-align: center;
          border-bottom: 1px solid rgba(0,0,0,0.03);
          font-size: 0.9rem;
          color: var(--color-text);
          display: flex;
          flex-direction: column;
          gap: 5px;
          align-items: center;
        }
        .compare-features li:last-child {
          border-bottom: none;
        }
        .compare-features li span {
          color: var(--color-text-light);
          font-size: 0.75rem;
          text-transform: uppercase;
          letter-spacing: 1px;
        }
        .check-icon { color: var(--color-primary); font-size: 1.1rem; }
        .x-icon { color: rgba(0,0,0,0.15); font-size: 1.1rem; }
      </style>

      <div class="modern-compare-container reveal">
        <div class="modern-compare-grid">
          <!-- Sparkle Party -->
          <div class="compare-column">
            <img src="assets/images/magic_show_party_1790842468826.jpg" class="compare-img" alt="Sparkle Party">
            <div class="compare-header">
              <h3>Sparkle Party</h3>
              <div class="compare-price">$99</div>
            </div>
            <ul class="compare-features">
              <li><span>Duration</span> 1 hour</li>
              <li><span>Entertainers</span> 1</li>
              <li><span>Interactive games</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Live performance</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Themed activities</span> <i class="fa-solid fa-xmark x-icon"></i></li>
              <li><span>Meet & Greet</span> <i class="fa-solid fa-xmark x-icon"></i></li>
            </ul>
          </div>
          
          <!-- Magic Adventure -->
          <div class="compare-column" style="border-top-color: #3895c8; transform: scale(1.03); box-shadow: 0 15px 35px rgba(56,149,200,0.15);">
            <img src="assets/images/superhero_party_1790842695325.jpg" class="compare-img" alt="Magic Adventure">
            <div class="compare-header">
              <h3 style="color: var(--color-primary);">Magic Adventure</h3>
              <div class="compare-price" style="color: #3895c8;">$149</div>
            </div>
            <ul class="compare-features">
              <li><span>Duration</span> 1.5 hours</li>
              <li><span>Entertainers</span> 1</li>
              <li><span>Interactive games</span> <i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></li>
              <li><span>Live performance</span> <i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></li>
              <li><span>Themed activities</span> <i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></li>
              <li><span>Meet & Greet</span> <i class="fa-solid fa-check check-icon" style="color:#3895c8;"></i></li>
            </ul>
          </div>
          
          <!-- Fantasy World -->
          <div class="compare-column">
            <img src="assets/images/princess_party_1790842645232.jpg" class="compare-img" alt="Fantasy World">
            <div class="compare-header">
              <h3>Fantasy World</h3>
              <div class="compare-price">$199</div>
            </div>
            <ul class="compare-features">
              <li><span>Duration</span> 2 hours</li>
              <li><span>Entertainers</span> 1-2</li>
              <li><span>Interactive games</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Live performance</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Themed activities</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Meet & Greet</span> <i class="fa-solid fa-check check-icon"></i></li>
            </ul>
          </div>
          
          <!-- Little Explorers -->
          <div class="compare-column">
            <img src="assets/images/about_kids_birthday.jpg" class="compare-img" alt="Little Explorers">
            <div class="compare-header">
              <h3>Little Explorers</h3>
              <div class="compare-price">$249</div>
            </div>
            <ul class="compare-features">
              <li><span>Duration</span> 2.5 hours</li>
              <li><span>Entertainers</span> 2</li>
              <li><span>Interactive games</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Live performance</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Themed activities</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Meet & Greet</span> <i class="fa-solid fa-check check-icon"></i></li>
            </ul>
          </div>
          
          <!-- Joyful Moments -->
          <div class="compare-column">
            <img src="assets/images/james_boy_smile.jpg" class="compare-img" alt="Joyful Moments">
            <div class="compare-header">
              <h3>Joyful Moments</h3>
              <div class="compare-price">$129</div>
            </div>
            <ul class="compare-features">
              <li><span>Duration</span> 1 hour</li>
              <li><span>Entertainers</span> 1</li>
              <li><span>Interactive games</span> <i class="fa-solid fa-xmark x-icon"></i></li>
              <li><span>Live performance</span> <i class="fa-solid fa-check check-icon"></i></li>
              <li><span>Themed activities</span> <i class="fa-solid fa-xmark x-icon"></i></li>
              <li><span>Meet & Greet</span> <i class="fa-solid fa-check check-icon"></i></li>
            </ul>
          </div>
          
          <!-- Ultimate Celebration -->
          <div class="compare-column" style="border-top-color: #f5a623;">
            <img src="assets/images/hero_magician_1790831867453.jpg" class="compare-img" alt="Ultimate Celebration">
            <div class="compare-header">
              <h3 style="color: #f5a623;">Ultimate Celeb</h3>
              <div class="compare-price">$349</div>
            </div>
            <ul class="compare-features">
              <li><span>Duration</span> 3 hours</li>
              <li><span>Entertainers</span> 3</li>
              <li><span>Interactive games</span> <i class="fa-solid fa-check check-icon" style="color:#f5a623;"></i></li>
              <li><span>Live performance</span> <i class="fa-solid fa-check check-icon" style="color:#f5a623;"></i></li>
              <li><span>Themed activities</span> <i class="fa-solid fa-check check-icon" style="color:#f5a623;"></i></li>
              <li><span>Meet & Greet</span> <i class="fa-solid fa-check check-icon" style="color:#f5a623;"></i></li>
            </ul>
          </div>
          
        </div>
      </div>
'''

content = table_pattern.sub(modern_compare_html, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
