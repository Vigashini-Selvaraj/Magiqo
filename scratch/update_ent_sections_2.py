import re

file_path = 'c:/Users/vigas/Desktop/magiqo/entertainers.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Redesign "Choose Your Performance Style" Quiz
new_quiz_html = '''
  <!-- 6. Choose Your Performance Style (Redesigned Again) -->
  <section class="section-pad" style="background: var(--color-bg); position: relative;">
    <div class="container">
      <div class="sec-title text-center">
        <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Find Your</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Perfect Match</span></h2>
        <p style="font-size: 1.2rem; margin-top: 1rem; color: var(--color-text-light);">Answer a few quick questions to find the ideal entertainer for your event.</p>
      </div>
      
      <div class="interactive-finder" style="background: var(--color-surface); border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); border: 1px solid var(--color-border); max-width: 800px; margin: 0 auto; overflow: hidden;">
        
        <div style="padding: 3rem; position: relative;">
            <div id="quizContainer">
               <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; border-bottom: 2px solid var(--color-border); padding-bottom: 1rem;">
                 <span style="font-weight: bold; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;">Question <span id="qNum">1</span> of 4</span>
                 <div style="height: 6px; width: 100px; background: var(--color-bg); border-radius: 3px; overflow: hidden;">
                   <div id="qProgress" style="height: 100%; width: 25%; background: var(--color-primary); transition: width 0.3s;"></div>
                 </div>
               </div>
               
               <h4 id="questionText" style="font-size: 1.8rem; margin-bottom: 2.5rem; color: var(--color-text); font-family: var(--font-heading);">What is the age of the birthday child?</h4>
               
               <div id="answersContainer" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                  <button class="btn style-btn-modern" onclick="nextQuestion(1)">1-4 years</button>
                  <button class="btn style-btn-modern" onclick="nextQuestion(2)">5-7 years</button>
                  <button class="btn style-btn-modern" onclick="nextQuestion(3)">8-10 years</button>
                  <button class="btn style-btn-modern" onclick="nextQuestion(4)">11+ years</button>
               </div>
            </div>
            
            <div id="talentSuggestion" style="display: none; text-align: center; animation: fadeIn 0.5s ease-out;">
               <div style="width: 120px; height: 120px; margin: 0 auto 1.5rem; border-radius: 50%; overflow: hidden; border: 4px solid var(--color-primary);">
                 <img src="assets/images/magician_portrait_1790843004983.jpg" alt="Elias" style="width: 100%; height: 100%; object-fit: cover;">
               </div>
               <h3 style="color: var(--color-text); font-size: 2rem; margin-bottom: 0.5rem; font-family: var(--font-heading);">Elias the Magician</h3>
               <p id="sugDesc" style="font-size: 1.1rem; color: var(--color-text-light); margin-bottom: 2rem; line-height: 1.6; max-width: 500px; margin-left: auto; margin-right: auto;"></p>
               <a href="entertainer_detail.html?id=elias" class="btn btn-primary" style="background: var(--color-primary); font-size: 1.1rem; padding: 1rem 2.5rem; border-radius: var(--radius-pill); width: 100%; max-width: 300px;">View Full Profile</a>
            </div>
        </div>
      </div>
      
      <style>
        .style-btn-modern { background: transparent; border: 2px solid var(--color-border); color: var(--color-text); padding: 1.25rem 1.5rem; border-radius: 12px; font-size: 1.1rem; font-weight: 600; transition: all 0.2s; cursor: pointer; text-align: left; }
        .style-btn-modern:hover { border-color: var(--color-primary); color: var(--color-primary); background: rgba(218, 47, 95, 0.05); transform: translateY(-2px); }
      </style>
      <script>
        const questions = [
            { q: "What is the age of the birthday child?", a: ["1-4 years", "5-7 years", "8-10 years", "11+ years"] },
            { q: "How active is your group?", a: ["Super Active", "Moderate", "Quiet & Focused", "Mixed Group"] },
            { q: "What's the party setting?", a: ["Living Room", "Large Hall", "Outdoor Park", "Backyard"] },
            { q: "What vibe are you going for?", a: ["Laughs & Silliness", "Magic & Wonder", "Action & Games", "Story & Creativity"] }
        ];
        let currentQ = 0;
        
        function nextQuestion(ans) {
            currentQ++;
            if(currentQ < questions.length) {
                document.getElementById('qNum').innerText = currentQ + 1;
                document.getElementById('qProgress').style.width = ((currentQ + 1) / questions.length * 100) + '%';
                document.getElementById('questionText').innerText = questions[currentQ].q;
                let html = '';
                questions[currentQ].a.forEach((ans, i) => {
                    html += '<button class="btn style-btn-modern" onclick="nextQuestion(' + i + ')">' + ans + '</button>';
                });
                document.getElementById('answersContainer').innerHTML = html;
            } else {
                document.getElementById('quizContainer').style.display = 'none';
                
                const box = document.getElementById('talentSuggestion');
                box.style.display = 'block';
                document.getElementById('sugDesc').innerText = 'Based on your answers, Elias brings the perfect mix of wonder, interaction, and magic for your specific group size and location!';
            }
        }
      </script>
    </div>
  </section>
'''

content = re.sub(r'<!-- 6\. Choose Your Performance Style.*?.*?</section>', new_quiz_html, content, flags=re.DOTALL)


# 2. Redesign The Magiqo Standard
new_standard_html = '''
  <!-- NEW SECTION 1: The Magiqo Standard -->
  <section class="section-pad" style="background: var(--color-bg);">
    <div class="container">
      <div class="sec-title text-center">
        <h2><span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">The Magiqo</span> <span style="color: var(--color-primary); -webkit-text-fill-color: var(--color-primary);">Standard</span></h2>
        <p style="color: var(--color-text-light);">Your child's safety, happiness, and engagement are our top priorities.</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        
        <div style="background: var(--color-surface); padding: 3rem 2rem; border-radius: 16px; border: 1px solid var(--color-border); text-align: center; transition: transform 0.3s; box-shadow: 0 5px 15px rgba(0,0,0,0.02);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
          <div style="width: 70px; height: 70px; background: rgba(56, 149, 200, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
            <svg viewBox="0 0 24 24" style="width: 35px; height: 35px; fill: #3895c8;"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
          </div>
          <h3 style="color: var(--color-text); font-family: var(--font-heading); font-size: 1.5rem; margin-bottom: 1rem;">Background Checked</h3>
          <p style="color: var(--color-text-light); line-height: 1.6;">Every single entertainer undergoes a comprehensive nationwide background check and reference verification.</p>
        </div>
        
        <div style="background: var(--color-surface); padding: 3rem 2rem; border-radius: 16px; border: 1px solid var(--color-border); text-align: center; transition: transform 0.3s; box-shadow: 0 5px 15px rgba(0,0,0,0.02);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
          <div style="width: 70px; height: 70px; background: rgba(218, 47, 95, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
            <svg viewBox="0 0 24 24" style="width: 35px; height: 35px; fill: var(--color-primary);"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"/></svg>
          </div>
          <h3 style="color: var(--color-text); font-family: var(--font-heading); font-size: 1.5rem; margin-bottom: 1rem;">Professionally Trained</h3>
          <p style="color: var(--color-text-light); line-height: 1.6;">Our talent attends rigorous Magiqo Workshops to master crowd control and the art of highly-engaging performance.</p>
        </div>
        
        <div style="background: var(--color-surface); padding: 3rem 2rem; border-radius: 16px; border: 1px solid var(--color-border); text-align: center; transition: transform 0.3s; box-shadow: 0 5px 15px rgba(0,0,0,0.02);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
          <div style="width: 70px; height: 70px; background: rgba(255, 152, 0, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
            <svg viewBox="0 0 24 24" style="width: 35px; height: 35px; fill: #ff9800;"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 12h-4v-4h4v4zm0-6h-4V5h4v4zm6 6h-4v-4h4v4zm0-6h-4V5h4v4z"/></svg>
          </div>
          <h3 style="color: var(--color-text); font-family: var(--font-heading); font-size: 1.5rem; margin-bottom: 1rem;">Fully Insured</h3>
          <p style="color: var(--color-text-light); line-height: 1.6;">We are fully licensed and hold robust liability insurance, giving parents complete peace of mind.</p>
        </div>
        
      </div>
    </div>
  </section>
'''

content = re.sub(r'<!-- NEW SECTION 1: The Magiqo Standard -->.*?</section>', new_standard_html, content, flags=re.DOTALL)


# 3. Remove Book Your Star
content = re.sub(r'<!-- 9\. Availability & Booking -->.*?</section>', '', content, flags=re.DOTALL)
# Also remove the modal
content = re.sub(r'<div class="modal-availability".*?</div>\s*</div>', '', content, flags=re.DOTALL)

# 4. Remove Let the Magic Begin CTA and use "Have a talent for magic?" as CTA
content = re.sub(r'<!-- 10\. Find Your Party Star \(CTA\) -->.*?</section>', '', content, flags=re.DOTALL)

# 5. Make Join the Team section act as the CTA section (which it already is, I just need to make sure the HTML is clean)
new_join_html = '''
  <!-- NEW SECTION 3: Join the Team (CTA) -->
  <section class="cta-section" style="background: var(--color-secondary); padding: 6rem 0; text-align: center; position: relative; overflow: hidden;">
    <div class="container" style="position: relative; z-index: 2;">
        <h2 style="font-family: var(--font-magic); font-size: 3.5rem; margin-bottom: 1rem; color: white !important; -webkit-text-fill-color: white !important; background: none !important;">
           Have a <span style="color: #3895c8; -webkit-text-fill-color: #3895c8;">Talent for Magic?</span>
        </h2>
        <p style="font-size: 1.25rem; color: rgba(255,255,255,0.9); max-width: 700px; margin: 0 auto 3rem; line-height: 1.6;">
           We are always looking for passionate, high-energy individuals to join our growing roster of premium entertainers. If you love making kids smile, we'd love to meet you.
        </p>
        <a href="join.html" class="btn btn-animated" style="background: var(--color-primary); color: white; padding: 1.25rem 4rem; font-size: 1.25rem; font-weight: bold; border-radius: var(--radius-pill); box-shadow: 0 10px 20px rgba(218, 47, 95, 0.4); text-decoration: none; display: inline-block; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Apply to Join</a>
    </div>
  </section>
'''

content = re.sub(r'<!-- NEW SECTION 3: Join the Team -->.*?</section>', new_join_html, content, flags=re.DOTALL)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Redesigns completed")
