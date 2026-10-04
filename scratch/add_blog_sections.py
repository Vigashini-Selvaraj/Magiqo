import re

filepath_blog = r'c:\Users\vigas\Desktop\magiqo\blog.html'
filepath_book = r'c:\Users\vigas\Desktop\magiqo\booking.html'

with open(filepath_blog, 'r', encoding='utf-8') as f:
    blog_content = f.read()
    
with open(filepath_book, 'r', encoding='utf-8') as f:
    book_content = f.read()

# 1. Restore section-container CSS
missing_css = '''
    .section-container { max-width: 1200px; margin: 0 auto 80px; padding: 0 20px; }
    .section-title { font-family: var(--font-magic); font-size: 3rem; text-align: center; margin-bottom: 40px; color: var(--color-text); }
    .section-title .text-pink { color: var(--color-primary); -webkit-text-fill-color: var(--color-primary); background: none; }
    .section-title .text-blue { color: #3895c8; -webkit-text-fill-color: #3895c8; background: none; }
    
    /* 3. Explore Categories */
'''
blog_content = blog_content.replace('    /* 3. Explore Categories */\n', missing_css)

# Extract Testimonials, FAQ, and Query from booking.html
test_match = re.search(r'<!-- SECTION 6: TESTIMONIALS -->.*?</section>', book_content, re.DOTALL)
faq_match = re.search(r'<!-- SECTION 7: FAQs -->.*?</section>', book_content, re.DOTALL)
query_match = re.search(r'<!-- SECTION 8: QUERY BOX -->.*?</section>', book_content, re.DOTALL)

test_html = test_match.group(0) if test_match else ''
faq_html = faq_match.group(0) if faq_match else ''
query_html = query_match.group(0) if query_match else ''

# Modify FAQ title to "Blog FAQs" and Query title to "Doubts in Blogs?"
faq_html = faq_html.replace('Booking', 'Blog')
query_html = query_html.replace('Still have questions?', 'Doubts about our blogs?')

# Create Recent / Top 3 Articles section
recent_top3_html = '''
    <!-- RECENT & TOP 3 ARTICLES -->
    <section class="section-container reveal" style="margin-top: 80px;">
      <h2 class="section-title"><span class="text-pink">Trending</span> <span class="text-blue">Reads</span></h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">
          <div class="blog-content">
            <span class="category-tag" style="background: var(--color-primary); color: white;">#1 TOP RATED</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html'">How to Keep Adults Entertained at a Kid's Party</h3>
            <p>Our most viewed article this month! Expert advice on balancing fun for all ages.</p>
            <a href="blog_detail.html" class="read-more">Read Full Article <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
        <div class="blog-card" style="background: rgba(56, 149, 200, 0.05); border: 1px solid rgba(56, 149, 200, 0.2);">
          <div class="blog-content">
            <span class="category-tag" style="background: #3895c8; color: white;">#2 TOP RATED</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html'">Winter Wonderland Party Ideas</h3>
            <p>Trending now that the season is shifting. Everything you need for a snowy celebration.</p>
            <a href="blog_detail.html" class="read-more">Read Full Article <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">
          <div class="blog-content">
            <span class="category-tag" style="background: var(--color-primary); color: white;">JUST ADDED</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html'">Eco-Friendly Party Decorations</h3>
            <p>Hot off the press! Learn how to party responsibly without sacrificing the fun.</p>
            <a href="blog_detail.html" class="read-more">Read Full Article <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
      </div>
    </section>
'''

# Redesign Final CTA
new_cta_html = '''
    <!-- 12. FINAL CTA -->
    <section class="cta-final reveal" style="background: linear-gradient(135deg, var(--color-primary), #3895c8); padding: 100px 20px; text-align: center; border-radius: 40px; max-width: 1200px; margin: 80px auto; color: white; box-shadow: 0 20px 50px rgba(0,0,0,0.3);">
      <h2 style="font-family: var(--font-magic); font-size: 4rem; margin-bottom: 20px; font-weight: 900; line-height: 1.1; text-transform: uppercase; letter-spacing: 2px;">Ready to Make <br>Magic Happen?</h2>
      <p style="font-size: 1.3rem; margin-bottom: 40px; font-weight: 500; max-width: 600px; margin-left: auto; margin-right: auto; opacity: 0.9;">Stop dreaming about the perfect party and let us bring it to life. Book your magical celebration today.</p>
      <a href="booking.html" class="btn" style="background: white; color: var(--color-primary); padding: 20px 50px; font-size: 1.5rem; font-weight: 900; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: transform 0.3s;">Start Booking <i class="fa-solid fa-bolt" style="margin-left: 10px;"></i></a>
    </section>
'''

# Replace old CTA
old_cta_match = re.search(r'<!-- 12\. FINAL CTA -->.*?</section>', blog_content, re.DOTALL)
if old_cta_match:
    blog_content = blog_content.replace(old_cta_match.group(0), new_cta_html)

# Insert the new sections before NEWSLETTER
newsletter_match = re.search(r'<!-- 10\. NEWSLETTER -->', blog_content)
if newsletter_match:
    insert_str = recent_top3_html + '\n' + test_html + '\n' + faq_html + '\n' + query_html + '\n\n    <!-- 10. NEWSLETTER -->'
    blog_content = blog_content.replace('<!-- 10. NEWSLETTER -->', insert_str)

with open(filepath_blog, 'w', encoding='utf-8') as f:
    f.write(blog_content)
