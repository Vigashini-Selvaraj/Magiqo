import json
import re

with open('scratch/full_entertainers_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Convert DB dictionary to formatted JavaScript object string
js_db_str = json.dumps(db, indent=2)

js_logic = f"""  <!-- Comprehensive Entertainer Profile Resolver -->
  <script>
    const entertainersDatabase = {js_db_str};

    // Aliases registration
    entertainersDatabase["captain_ray"] = entertainersDatabase["captain_ray"];
    entertainersDatabase["captain ray"] = entertainersDatabase["captain_ray"];
    entertainersDatabase["captain_leo"] = entertainersDatabase["max"];
    entertainersDatabase["captain leo"] = entertainersDatabase["max"];
    entertainersDatabase["leo"] = entertainersDatabase["max"];
    entertainersDatabase["dj spark"] = entertainersDatabase["dj_spark"];
    entertainersDatabase["the great z"] = entertainersDatabase["the_great_z"];
    entertainersDatabase["princess lily"] = entertainersDatabase["lily"];
    entertainersDatabase["princess aurora"] = entertainersDatabase["aurora"];
    entertainersDatabase["elias thorne"] = entertainersDatabase["elias"];
    entertainersDatabase["jojo the juggler"] = entertainersDatabase["jojo"];
    entertainersDatabase["bubble_mia"] = entertainersDatabase["mia"];
    entertainersDatabase["bubble mia"] = entertainersDatabase["mia"];

    function resolveEntertainer(rawId) {{
      if (!rawId) return {{ key: "elias", data: entertainersDatabase["elias"] }};
      
      const clean = rawId.toLowerCase().trim();
      if (entertainersDatabase[clean]) {{
        return {{ key: clean, data: entertainersDatabase[clean] }};
      }}
      
      const norm = clean.replace(/[^a-z0-9]/g, "");
      if (entertainersDatabase[norm]) {{
        return {{ key: norm, data: entertainersDatabase[norm] }};
      }}
      
      for (const key in entertainersDatabase) {{
        const knorm = key.replace(/[^a-z0-9]/g, "");
        if (knorm === norm || (knorm.length > 2 && norm.includes(knorm)) || (norm.length > 2 && knorm.includes(norm))) {{
          return {{ key: key, data: entertainersDatabase[key] }};
        }}
      }}
      
      for (const key in entertainersDatabase) {{
        const ent = entertainersDatabase[key];
        const nameNorm = ent.name.toLowerCase().replace(/[^a-z0-9]/g, "");
        if (nameNorm.includes(norm) || norm.includes(nameNorm)) {{
          return {{ key: key, data: ent }};
        }}
      }}
      
      return {{ key: "elias", data: entertainersDatabase["elias"] }};
    }}

    function applyEntertainerProfile() {{
      const params = new URLSearchParams(window.location.search);
      const rawId = params.get("id") || params.get("name") || window.location.hash.replace("#", "") || "elias";
      const resolved = resolveEntertainer(rawId);
      const data = resolved.data;
      const key = resolved.key;

      // Update Page Meta
      document.title = `${{data.name}} - ${{data.title}} | Magiqo`;
      const metaDesc = document.getElementById("page-desc");
      if (metaDesc) metaDesc.content = `Book ${{data.name}}, ${{data.title}} for magical children celebrations with Magiqo.`;
      
      const breadcrumb = document.getElementById("breadcrumb-current");
      if (breadcrumb) breadcrumb.textContent = data.name;

      // Portrait Image
      const imgEl = document.getElementById("ent-img");
      if (imgEl) {{
        imgEl.src = data.img;
        imgEl.alt = `${{data.name}} - ${{data.title}}`;
      }}

      // Rating badge
      const ratingBadge = document.getElementById("ent-rating-badge");
      if (ratingBadge) ratingBadge.textContent = `★ ${{data.rating}} Rating (${{data.shows}} Shows)`;

      // Title & Name with split styling
      const nameEl = document.getElementById("ent-name");
      if (nameEl) {{
        nameEl.innerHTML = `<span class="text-pink">${{data.firstName}}</span> <span class="text-blue">${{data.lastName}}</span>`;
      }}
      
      const titleEl = document.getElementById("ent-title");
      if (titleEl) titleEl.textContent = data.title;

      // Meta row
      const metaRating = document.getElementById("meta-rating");
      if (metaRating) metaRating.textContent = `${{data.rating}} / 5.0 Rating`;
      const metaShows = document.getElementById("meta-shows");
      if (metaShows) metaShows.textContent = `${{data.shows}} Completed Shows`;
      const metaExp = document.getElementById("meta-exp");
      if (metaExp) metaExp.textContent = data.exp;
      const metaPrice = document.getElementById("meta-price");
      if (metaPrice) metaPrice.textContent = data.price;

      // Bio
      const descEl = document.getElementById("ent-description");
      if (descEl) descEl.textContent = data.bio;

      // About Section
      const p1 = document.getElementById("about-story-p1");
      if (p1 && data.storyP1) p1.textContent = data.storyP1;
      const p2 = document.getElementById("about-story-p2");
      if (p2 && data.storyP2) p2.textContent = data.storyP2;
      const agesEl = document.getElementById("spec-ages");
      if (agesEl && data.ages) agesEl.textContent = data.ages;
      const locEl = document.getElementById("spec-location");
      if (locEl && data.location) locEl.textContent = data.location;

      const aboutImg = document.getElementById("about-ent-img");
      if (aboutImg && data.secondaryImg) {{
        aboutImg.src = data.secondaryImg;
        aboutImg.alt = `${{data.name}} Live Performance`;
      }}

      // Reviews
      if (data.reviews && data.reviews.length >= 3) {{
        const q1 = document.getElementById("review-quote-1");
        const q2 = document.getElementById("review-quote-2");
        const q3 = document.getElementById("review-quote-3");
        if (q1) q1.textContent = `"${{data.reviews[0].quote}}"`;
        if (q2) q2.textContent = `"${{data.reviews[1].quote}}"`;
        if (q3) q3.textContent = `"${{data.reviews[2].quote}}"`;
      }}

      // Gallery Images
      if (data.gallery && data.gallery.length >= 3) {{
        const g1 = document.getElementById("gallery-img-1");
        const g2 = document.getElementById("gallery-img-2");
        const g3 = document.getElementById("gallery-img-3");
        if (g1) g1.src = data.gallery[0];
        if (g2) g2.src = data.gallery[1];
        if (g3) g3.src = data.gallery[2];
      }}

      // Booking Links
      const bookingUrl = `booking.html?id=${{encodeURIComponent(key)}}`;
      const heroBookBtn = document.getElementById("hero-book-btn");
      if (heroBookBtn) heroBookBtn.href = bookingUrl;
      const finalCtaBtn = document.getElementById("final-cta-btn");
      if (finalCtaBtn) finalCtaBtn.href = bookingUrl;
      const ctaName = document.getElementById("cta-ent-name");
      if (ctaName) ctaName.textContent = data.name;

      const pkg1 = document.getElementById("pkg-btn-1");
      if (pkg1) pkg1.href = `booking.html?id=${{encodeURIComponent(key)}}&package=spark`;
      const pkg2 = document.getElementById("pkg-btn-2");
      if (pkg2) pkg2.href = `booking.html?id=${{encodeURIComponent(key)}}&package=adventure`;
      const pkg3 = document.getElementById("pkg-btn-3");
      if (pkg3) pkg3.href = `booking.html?id=${{encodeURIComponent(key)}}&package=spectacle`;
    }}

    // Execute immediately so there is zero flash of default content
    applyEntertainerProfile();

    // Also run on DOM ready and window events
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', applyEntertainerProfile);
    }}
    window.addEventListener('load', applyEntertainerProfile);
    window.addEventListener('popstate', applyEntertainerProfile);
  </script>
</body>
</html>"""

with open('entertainer_detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace from '<!-- Comprehensive Entertainer Profile Resolver -->' to '</body>'
pattern = r'<!-- Comprehensive Entertainer Profile Resolver -->.*</body>[\s\r\n]*</html>'
match = re.search(pattern, html, re.DOTALL)
if match:
    new_html = html[:match.start()] + js_logic
    with open('entertainer_detail.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully replaced entertainer_detail.html script with full 21 performers database and instant resolver!")
else:
    print("Could not find script block to replace!")
