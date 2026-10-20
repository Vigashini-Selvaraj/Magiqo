import re

def fix_blog():
    file_path = r'c:\Users\vigas\Desktop\magiqo\blog.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Featured Story link
    content = content.replace(
        '<a href="blog_detail.html" class="read-more">Read Article <i class="fa-solid fa-arrow-right"></i></a>',
        '<a href="blog_detail.html?title=The%20Ultimate%20Guide%20to%20Hosting%20a%20Magic-Themed%20Birthday&cat=Themes&img=assets/images/pro_classic_magic.jpg" class="read-more">Read Article <i class="fa-solid fa-arrow-right"></i></a>'
    )

    # 2. Update all blog cards in grid to have local images and parameterized detail links
    # Card 1: 10 reasons to hire a professional magician (Entertainers)
    content = re.sub(
        r'<div class="blog-card" data-category="Entertainers" data-title="10 reasons to hire a professional magician">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Entertainers" data-title="10 reasons to hire a professional magician">
          <img src="assets/images/pro_magician_2.jpg" alt="10 Reasons to Hire a Professional Magician" class="blog-img" onclick="location.href='blog_detail.html?title=10%20Reasons%20to%20Hire%20a%20Professional%20Magician&cat=Entertainers&img=assets/images/pro_magician_2.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Entertainers</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=10%20Reasons%20to%20Hire%20a%20Professional%20Magician&cat=Entertainers&img=assets/images/pro_magician_2.jpg'">10 Reasons to Hire a Professional Magician</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Oct 1, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 5 min</span>
            </div>
            <a href="blog_detail.html?title=10%20Reasons%20to%20Hire%20a%20Professional%20Magician&cat=Entertainers&img=assets/images/pro_magician_2.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 2: Superhero obstacle course (Kids)
    content = re.sub(
        r'<div class="blog-card" data-category="Kids" data-title="how to build a superhero obstacle course">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Kids" data-title="how to build a superhero obstacle course">
          <img src="assets/images/superhero_party_1790842695325.jpg" alt="How to Build a Superhero Obstacle Course" class="blog-img" onclick="location.href='blog_detail.html?title=How%20to%20Build%20a%20Superhero%20Obstacle%20Course&cat=Kids&img=assets/images/superhero_party_1790842695325.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Kids</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=How%20to%20Build%20a%20Superhero%20Obstacle%20Course&cat=Kids&img=assets/images/superhero_party_1790842695325.jpg'">How to Build a Superhero Obstacle Course</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Sep 28, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 4 min</span>
            </div>
            <a href="blog_detail.html?title=How%20to%20Build%20a%20Superhero%20Obstacle%20Course&cat=Kids&img=assets/images/superhero_party_1790842695325.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 3: DIY Princess Crowns (Themes)
    content = re.sub(
        r'<div class="blog-card" data-category="Themes" data-title="diy princess crowns for the royal court">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Themes" data-title="diy princess crowns for the royal court">
          <img src="assets/images/pro_princess.jpg" alt="DIY Princess Crowns for the Royal Court" class="blog-img" onclick="location.href='blog_detail.html?title=DIY%20Princess%20Crowns%20for%20the%20Royal%20Court&cat=Themes&img=assets/images/pro_princess.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Themes</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=DIY%20Princess%20Crowns%20for%20the%20Royal%20Court&cat=Themes&img=assets/images/pro_princess.jpg'">DIY Princess Crowns for the Royal Court</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Sep 25, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 6 min</span>
            </div>
            <a href="blog_detail.html?title=DIY%20Princess%20Crowns%20for%20the%20Royal%20Court&cat=Themes&img=assets/images/pro_princess.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 4: Balloon Arch Decorations (Decor)
    content = re.sub(
        r'<div class="blog-card" data-category="Decor" data-title="the ultimate guide to balloon arch decorations">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Decor" data-title="the ultimate guide to balloon arch decorations">
          <img src="assets/images/service_balloon_twisting.jpg" alt="The Ultimate Guide to Balloon Arch Decorations" class="blog-img" onclick="location.href='blog_detail.html?title=The%20Ultimate%20Guide%20to%20Balloon%20Arch%20Decorations&cat=Decor&img=assets/images/service_balloon_twisting.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Decor</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=The%20Ultimate%20Guide%20to%20Balloon%20Arch%20Decorations&cat=Decor&img=assets/images/service_balloon_twisting.jpg'">The Ultimate Guide to Balloon Arch Decorations</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Sep 22, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 7 min</span>
            </div>
            <a href="blog_detail.html?title=The%20Ultimate%20Guide%20to%20Balloon%20Arch%20Decorations&cat=Decor&img=assets/images/service_balloon_twisting.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 5: 5 Tips from Event Experts to Reduce Stress (Planning - user specifically called out Planning!)
    content = re.sub(
        r'<div class="blog-card" data-category="Planning" data-title="5 tips from event experts to reduce stress">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Planning" data-title="5 tips from event experts to reduce stress">
          <img src="assets/images/about_kids_birthday.jpg" alt="5 Tips from Event Experts to Reduce Stress" class="blog-img" onclick="location.href='blog_detail.html?title=5%20Tips%20from%20Event%20Experts%20to%20Reduce%20Stress&cat=Planning&img=assets/images/about_kids_birthday.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Planning</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=5%20Tips%20from%20Event%20Experts%20to%20Reduce%20Stress&cat=Planning&img=assets/images/about_kids_birthday.jpg'">5 Tips from Event Experts to Reduce Stress</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Sep 20, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 5 min</span>
            </div>
            <a href="blog_detail.html?title=5%20Tips%20from%20Event%20Experts%20to%20Reduce%20Stress&cat=Planning&img=assets/images/about_kids_birthday.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 6: Halloween Party Ideas (Themes)
    content = re.sub(
        r'<div class="blog-card" data-category="Themes" data-title="halloween party ideas that are spooky not scary">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Themes" data-title="halloween party ideas that are spooky not scary">
          <img src="assets/images/spooky_illusions.jpg" alt="Halloween Party Ideas That Are Spooky Not Scary" class="blog-img" onclick="location.href='blog_detail.html?title=Halloween%20Party%20Ideas%20That%20Are%20Spooky%20Not%20Scary&cat=Themes&img=assets/images/spooky_illusions.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Themes</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=Halloween%20Party%20Ideas%20That%20Are%20Spooky%20Not%20Scary&cat=Themes&img=assets/images/spooky_illusions.jpg'">Halloween Party Ideas That Are Spooky Not Scary</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Sep 15, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 4 min</span>
            </div>
            <a href="blog_detail.html?title=Halloween%20Party%20Ideas%20That%20Are%20Spooky%20Not%20Scary&cat=Themes&img=assets/images/spooky_illusions.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 7: Choosing the Right Clown for Toddlers (Entertainers)
    content = re.sub(
        r'<div class="blog-card" data-category="Entertainers" data-title="choosing the right clown for toddlers">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Entertainers" data-title="choosing the right clown for toddlers">
          <img src="assets/images/pro_clown_blog.jpg" alt="Choosing the Right Clown for Toddlers" class="blog-img" onclick="location.href='blog_detail.html?title=Choosing%20the%20Right%20Clown%20for%20Toddlers&cat=Entertainers&img=assets/images/pro_clown_blog.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Entertainers</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=Choosing%20the%20Right%20Clown%20for%20Toddlers&cat=Entertainers&img=assets/images/pro_clown_blog.jpg'">Choosing the Right Clown for Toddlers</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Sep 12, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 3 min</span>
            </div>
            <a href="blog_detail.html?title=Choosing%20the%20Right%20Clown%20for%20Toddlers&cat=Entertainers&img=assets/images/pro_clown_blog.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 8: Top 5 Party Favors Kids Actually Keep (Planning)
    content = re.sub(
        r'<div class="blog-card" data-category="Planning" data-title="top 5 party favors kids actually keep">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Planning" data-title="top 5 party favors kids actually keep">
          <img src="assets/images/party_moments_2_1790918669697.jpg" alt="Top 5 Party Favors Kids Actually Keep" class="blog-img" onclick="location.href='blog_detail.html?title=Top%205%20Party%20Favors%20Kids%20Actually%20Keep&cat=Planning&img=assets/images/party_moments_2_1790918669697.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Planning</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=Top%205%20Party%20Favors%20Kids%20Actually%20Keep&cat=Planning&img=assets/images/party_moments_2_1790918669697.jpg'">Top 5 Party Favors Kids Actually Keep</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Sep 10, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 5 min</span>
            </div>
            <a href="blog_detail.html?title=Top%205%20Party%20Favors%20Kids%20Actually%20Keep&cat=Planning&img=assets/images/party_moments_2_1790918669697.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # Card 9: How to Keep Adults Entertained (Planning)
    content = re.sub(
        r'<div class="blog-card" data-category="Planning" data-title="how to keep adults entertained at a kid\'s party">.*?</div>\s*</div>',
        '''<div class="blog-card" data-category="Planning" data-title="how to keep adults entertained at a kid\'s party">
          <img src="assets/images/family_holiday_party.jpg" alt="How to Keep Adults Entertained at a Kid\'s Party" class="blog-img" onclick="location.href='blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained%20at%20a%20Kid%27s%20Party&cat=Planning&img=assets/images/family_holiday_party.jpg'" style="cursor:pointer;">
          <div class="blog-content">
            <span class="category-tag" style="margin-bottom:10px;">Planning</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained%20at%20a%20Kid%27s%20Party&cat=Planning&img=assets/images/family_holiday_party.jpg'">How to Keep Adults Entertained at a Kid\'s Party</h3>
            <div class="blog-meta">
              <span><i class="fa-regular fa-calendar"></i> Jul 15, 2026</span>
              <span><i class="fa-regular fa-clock"></i> 4 min</span>
            </div>
            <a href="blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained%20at%20a%20Kid%27s%20Party&cat=Planning&img=assets/images/family_holiday_party.jpg" class="read-more" style="margin-top:auto;">Read More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>''',
        content,
        flags=re.DOTALL
    )

    # 3. Update Trending Reads with local images and parameterized detail links
    trending_section = '''    <!-- RECENT & TOP 3 ARTICLES -->
    <section class="section-container reveal" style="margin-top: 80px;">
      <h2 class="section-title"><span class="text-pink">Trending</span> <span class="text-blue">Reads</span></h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">
          <img src="assets/images/family_holiday_party.jpg" alt="Adults Entertained" class="blog-img" onclick="location.href='blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained%20at%20a%20Kid%27s%20Party&cat=Planning&img=assets/images/family_holiday_party.jpg'" style="cursor:pointer; border-radius: 20px 20px 0 0;">
          <div class="blog-content">
            <span class="category-tag" style="background: var(--color-primary); color: white;">#1 TOP RATED</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained%20at%20a%20Kid%27s%20Party&cat=Planning&img=assets/images/family_holiday_party.jpg'">How to Keep Adults Entertained at a Kid's Party</h3>
            <p>Our most viewed article this month! Expert advice on balancing fun for all ages.</p>
            <a href="blog_detail.html?title=How%20to%20Keep%20Adults%20Entertained%20at%20a%20Kid%27s%20Party&cat=Planning&img=assets/images/family_holiday_party.jpg" class="read-more">Read Full Article <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
        <div class="blog-card" style="background: rgba(56, 149, 200, 0.05); border: 1px solid rgba(56, 149, 200, 0.2);">
          <img src="assets/images/pro_classic_magic.jpg" alt="Winter Wonderland" class="blog-img" onclick="location.href='blog_detail.html?title=Winter%20Wonderland%20Party%20Ideas&cat=Themes&img=assets/images/pro_classic_magic.jpg'" style="cursor:pointer; border-radius: 20px 20px 0 0;">
          <div class="blog-content">
            <span class="category-tag" style="background: #3895c8; color: white;">#2 TOP RATED</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=Winter%20Wonderland%20Party%20Ideas&cat=Themes&img=assets/images/pro_classic_magic.jpg'">Winter Wonderland Party Ideas</h3>
            <p>Trending now that the season is shifting. Everything you need for a snowy celebration.</p>
            <a href="blog_detail.html?title=Winter%20Wonderland%20Party%20Ideas&cat=Themes&img=assets/images/pro_classic_magic.jpg" class="read-more">Read Full Article <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
        <div class="blog-card" style="background: rgba(210, 75, 118, 0.05); border: 1px solid rgba(210, 75, 118, 0.2);">
          <img src="assets/images/service_balloon_twisting.jpg" alt="Eco-Friendly Party" class="blog-img" onclick="location.href='blog_detail.html?title=Eco-Friendly%20Party%20Decorations&cat=Decor&img=assets/images/service_balloon_twisting.jpg'" style="cursor:pointer; border-radius: 20px 20px 0 0;">
          <div class="blog-content">
            <span class="category-tag" style="background: var(--color-primary); color: white;">JUST ADDED</span>
            <h3 style="cursor:pointer;" onclick="location.href='blog_detail.html?title=Eco-Friendly%20Party%20Decorations&cat=Decor&img=assets/images/service_balloon_twisting.jpg'">Eco-Friendly Party Decorations</h3>
            <p>Hot off the press! Learn how to party responsibly without sacrificing the fun.</p>
            <a href="blog_detail.html?title=Eco-Friendly%20Party%20Decorations&cat=Decor&img=assets/images/service_balloon_twisting.jpg" class="read-more">Read Full Article <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
      </div>
    </section>'''

    content = re.sub(
        r'<!-- RECENT & TOP 3 ARTICLES -->\s*<section class="section-container reveal".*?</section>',
        trending_section,
        content,
        flags=re.DOTALL
    )

    # 4. Update Testimonials with local images
    content = content.replace(
        'https://images.unsplash.com/photo-1508214751196-bfdd4ca401fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
        'assets/images/emily_girl_smile.jpg'
    )
    content = content.replace(
        'https://images.unsplash.com/photo-1464047736614-af63643285bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
        'assets/images/founder_mark.jpg'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated blog.html cards, Planning images, and parameterized links!")

if __name__ == '__main__':
    fix_blog()
