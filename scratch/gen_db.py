# Script to generate the comprehensive entertainersDatabase dictionary in JavaScript format
import json

db = {
  "elias": {
    "name": "Elias Thorne",
    "firstName": "Elias",
    "lastName": "Thorne",
    "title": "Master Magician & Grand Illusionist",
    "img": "assets/images/magician_portrait_1790843004983.jpg",
    "secondaryImg": "assets/images/pro_grand_stage.jpg",
    "rating": "4.95",
    "shows": "1,200+",
    "exp": "12 Years Experience",
    "price": "$250 / hr",
    "location": "London & Nationwide",
    "ages": "Ages 4 - 12 Years",
    "bio": "Elias Thorne is Magiqo's premier illusionist, renowned for high-energy sleight of hand, interactive mind reading, and jaw-dropping levitations that leave children gasping in awe and parents thoroughly entertained.",
    "storyP1": "With over 12 years of professional stage and party magic, Elias commands room attention with effortless warmth, spontaneous comedy, and mind-boggling illusions that baffle audiences of all ages.",
    "storyP2": "From the opening spell to the signature birthday child levitation, Elias makes the birthday boy or girl the absolute star of the celebration with their own magic wand and official apprentice certificate.",
    "reviews": [
      { "quote": "Elias the Magician was absolutely phenomenal. The kids were completely mesmerized for the entire hour. Best birthday party ever!", "name": "Sarah Jenkins", "event": "7th Birthday Party • London" },
      { "quote": "Elias held the attention of 25 seven-year-olds without breaking a sweat. The parents were just as amazed as the children!", "name": "Marcus Thornton", "event": "8th Birthday Party • Surrey" },
      { "quote": "Every trick was interactive, funny, and clean. Elias is a true master of his craft. Highly recommend!", "name": "David Miller", "event": "6th Birthday Party • Kent" }
    ],
    "gallery": [
      "assets/images/interactive_party_show.jpg",
      "assets/images/about_art_of_magic.jpg",
      "assets/images/family_holiday_party.jpg"
    ]
  },
  "jojo": {
    "name": "Jojo The Juggler",
    "firstName": "Jojo",
    "lastName": "The Juggler",
    "title": "Circus Juggler, Acrobat & Clown",
    "img": "assets/images/service_circus_juggler.jpg",
    "secondaryImg": "assets/images/clown_party_1790842566084.jpg",
    "rating": "4.8",
    "shows": "920+",
    "exp": "10 Years Experience",
    "price": "$195 / hr",
    "location": "Greater London & South East",
    "ages": "Ages 3 - 10 Years",
    "bio": "Jojo brings dazzling circus flair, hilarious slapstick comedy, and world-class juggling with balls, clubs, and spinning plates. Kids don't just watch—they jump right into the circus ring!",
    "storyP1": "Trained at the international circus academy, Jojo combines jaw-dropping balance acts with nonstop slapstick comedy, turning living rooms and gardens into vibrant big-top arenas.",
    "storyP2": "Every child gets to try spinning their own plates and balancing peacock feathers, concluding with a hilarious coronation where the birthday child leads the circus parade.",
    "reviews": [
      { "quote": "Jojo had 20 kids rolling on the floor laughing within 3 minutes! The plate spinning workshop was an absolute hit.", "name": "Claire Davies", "event": "5th Birthday Party • Essex" },
      { "quote": "So energetic, patient, and delightfully funny. Even the shyest children were up and participating in no time.", "name": "Liam O'Connor", "event": "6th Birthday Party • London" },
      { "quote": "Jojo is simply spectacular. The juggling stunts are top tier and the comedy is wholesome and hilarious.", "name": "Hannah Brooks", "event": "7th Birthday Party • Hertfordshire" }
    ],
    "gallery": [
      "assets/images/service_circus_juggler.jpg",
      "assets/images/clown_party_1790842566084.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "lily": {
    "name": "Princess Lily",
    "firstName": "Princess",
    "lastName": "Lily",
    "title": "Royal Fairytale Singer & Performer",
    "img": "assets/images/princess_portrait_1790843055244.jpg",
    "secondaryImg": "assets/images/princess_party_1790842645232.jpg",
    "rating": "5.0",
    "shows": "850+",
    "exp": "8 Years Experience",
    "price": "$210 / hr",
    "location": "London & Home Counties",
    "ages": "Ages 3 - 8 Years",
    "bio": "Princess Lily turns every celebration into a royal kingdom. Featuring live vocal performances, fairytale storytelling, and a heartfelt royal coronation ceremony for the birthday child.",
    "storyP1": "Trained in musical theatre, Princess Lily arrives in hand-stitched museum-quality royal gowns, singing beloved fairytale anthems that bring pure wonder to young dreamers.",
    "storyP2": "Her signature coronation includes a sparkling tiara crowning, royal decree reading, and princess etiquette lessons filled with laughter and enchanting dances.",
    "reviews": [
      { "quote": "Princess Lily was magical. Her singing voice gave everyone goosebumps, and my daughter cried happy tears when she was crowned!", "name": "Emma Richardson", "event": "4th Birthday Party • London" },
      { "quote": "From her gorgeous costume to her gentle warmth with all the girls and boys, Lily made our daughter's fairytale dream come true.", "name": "Sophie Taylor", "event": "5th Birthday Party • Berkshire" },
      { "quote": "Unbelievably authentic. The kids truly believed she stepped straight out of their favorite movie.", "name": "Jessica White", "event": "6th Birthday Party • Surrey" }
    ],
    "gallery": [
      "assets/images/princess_portrait_1790843055244.jpg",
      "assets/images/princess_party_1790842645232.jpg",
      "assets/images/sparkle_party.jpg"
    ]
  },
  "barnaby": {
    "name": "Barnaby The Clown",
    "firstName": "Barnaby",
    "lastName": "The Clown",
    "title": "Classic Comedy Clown & Slapstick",
    "img": "assets/images/pro_silly_clown.jpg",
    "secondaryImg": "assets/images/clown_party_1790842566084.jpg",
    "rating": "4.8",
    "shows": "620+",
    "exp": "9 Years Experience",
    "price": "$180 / hr",
    "location": "London & South East",
    "ages": "Ages 3 - 9 Years",
    "bio": "Barnaby delivers pure, good-hearted slapstick comedy, balloon animals, and playful games. Gentle, funny, and guaranteed to have toddlers and young kids rolling with laughter.",
    "storyP1": "Barnaby specializes in gentle, charming physical humor that never overwhelms younger children, creating an environment of immediate trust and infectious giggles.",
    "storyP2": "Featuring custom sculpted balloon pets for every single attendee and a grand comedy magic finale starring the birthday host.",
    "reviews": [
      { "quote": "Barnaby was wonderfully gentle with the younger kids and hilarious for the older ones. Truly a classic clown!", "name": "Rachel Adams", "event": "4th Birthday Party • London" },
      { "quote": "The balloon animals were incredible and the magic tricks were so silly the parents were laughing just as hard.", "name": "Peter Green", "event": "5th Birthday Party • Kent" },
      { "quote": "Everyone in the room was in stitches. Barnaby's comic timing is unbeatable.", "name": "Hannah Wright", "event": "5th Birthday • Essex" }
    ],
    "gallery": [
      "assets/images/pro_silly_clown.jpg",
      "assets/images/clown_party_1790842566084.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "sarah": {
    "name": "Sarah Face Art",
    "firstName": "Sarah",
    "lastName": "Face Art",
    "title": "Master Face Painter & Glitter Artist",
    "img": "assets/images/service_face_painting.jpg",
    "secondaryImg": "assets/images/sparkle_party.jpg",
    "rating": "4.9",
    "shows": "740+",
    "exp": "7 Years Experience",
    "price": "$175 / hr",
    "location": "London & Nationwide",
    "ages": "All Ages",
    "bio": "Sarah transforms children into fantastical creatures, superheroes, and shimmering butterflies using certified hypoallergenic, FDA-approved cosmetic face paints and eco-glitter.",
    "storyP1": "A professional makeup artist and illustrator, Sarah paints lightning-fast, museum-grade designs that delight both children and parents.",
    "storyP2": "Includes biodegradable glitter bars, temporary festival tattoos, and custom design requests for any party theme imaginable.",
    "reviews": [
      { "quote": "Sarah's face painting is pure art! Every single child looked like they walked out of a movie set.", "name": "Natalie Cole", "event": "6th Birthday Party • London" },
      { "quote": "Lightning fast and stunningly detailed. She painted 20 kids with time to spare for glitter touch-ups!", "name": "Chloe Bennett", "event": "5th Birthday • Surrey" },
      { "quote": "Hypoallergenic paints that washed off easily before bed with no irritation whatsoever. Highly recommended!", "name": "Mark Roberts", "event": "7th Birthday • Kent" }
    ],
    "gallery": [
      "assets/images/service_face_painting.jpg",
      "assets/images/sparkle_party.jpg",
      "assets/images/family_holiday_party.jpg"
    ]
  },
  "rex": {
    "name": "Rex Character Lead",
    "firstName": "Rex",
    "lastName": "Character Lead",
    "title": "Friendly Mascot & Game Lead",
    "img": "assets/images/service_mascot.jpg",
    "secondaryImg": "assets/images/superhero_party_1790842695325.jpg",
    "rating": "4.9",
    "shows": "510+",
    "exp": "6 Years Experience",
    "price": "$190 / hr",
    "location": "London & Home Counties",
    "ages": "Ages 2 - 7 Years",
    "bio": "Rex brings beloved mascot personalities to life with energetic dance games, warm high-fives, and unforgettable photo sessions that young children adore.",
    "storyP1": "Accompanied by a dedicated party coordinator, Rex guides children through fun parachute games, bubble dances, and gentle warm hugs.",
    "storyP2": "Ensures every child gets quality 1-on-1 time with their favorite character for timeless photos.",
    "reviews": [
      { "quote": "Our 3-year-old was thrilled beyond words! The mascot costume was immaculate and the host was fantastic.", "name": "Gemma Harris", "event": "3rd Birthday Party • London" },
      { "quote": "Rex brought so much joy and energy. The parachute games had all the little ones laughing nonstop.", "name": "Daniel Cooper", "event": "4th Birthday • Hertfordshire" },
      { "quote": "Brilliant handler and character performer. The photo moments will be cherished forever.", "name": "Samantha Green", "event": "3rd Birthday • Essex" }
    ],
    "gallery": [
      "assets/images/service_mascot.jpg",
      "assets/images/superhero_party_1790842695325.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "david": {
    "name": "David The Illusionist",
    "firstName": "David",
    "lastName": "The Illusionist",
    "title": "Grand Stage Illusionist & Mentalist",
    "img": "assets/images/pro_grand_stage.jpg",
    "secondaryImg": "assets/images/about_art_of_magic.jpg",
    "rating": "5.0",
    "shows": "980+",
    "exp": "14 Years Experience",
    "price": "$260 / hr",
    "location": "Nationwide UK",
    "ages": "Ages 5 - 14 Years",
    "bio": "David delivers theater-caliber stage illusions, mind reading, and clean psychological mysteries that captivate older children, tweens, and family gatherings alike.",
    "storyP1": "David brings grand theatrical props, impossible escapes, and modern mind reading that makes adults question reality.",
    "storyP2": "Includes an exclusive junior magician mini-workshop where guests learn a jaw-dropping trick to keep forever.",
    "reviews": [
      { "quote": "David blew everyone's minds—including the adults! Simply world-class entertainment.", "name": "Mark Henderson", "event": "10th Birthday Party • London" },
      { "quote": "A true stage show in our local hall. The levitation illusion left all the children speechless.", "name": "Claire Vance", "event": "9th Birthday • Surrey" },
      { "quote": "David is sophisticated, witty, and exceptionally talented. Our guests are still talking about it.", "name": "Robert Shaw", "event": "11th Birthday • London" }
    ],
    "gallery": [
      "assets/images/pro_grand_stage.jpg",
      "assets/images/about_art_of_magic.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "max": {
    "name": "Captain Leo",
    "firstName": "Captain",
    "lastName": "Leo",
    "title": "Action Hero Training & Stunts",
    "img": "assets/images/performer_superhero.jpg",
    "secondaryImg": "assets/images/superhero_party_1790842695325.jpg",
    "rating": "4.95",
    "shows": "880+",
    "exp": "8 Years Experience",
    "price": "$220 / hr",
    "location": "London & Nationwide",
    "ages": "Ages 4 - 10 Years",
    "bio": "Captain Leo takes children through an action-packed superhero bootcamp with obstacle courses, agility drills, teamwork games, and heroic oath ceremonies.",
    "storyP1": "Trained martial artist and stunt performer, Captain Leo enters with explosive energy and guides kids through certified hero training.",
    "storyP2": "Concludes with an official graduation ceremony where every child is awarded their superhero badge and cape certificate.",
    "reviews": [
      { "quote": "The kids were completely engaged running through the obstacle courses. Captain Leo is an incredible role model!", "name": "Tom Bradley", "event": "6th Birthday Party • London" },
      { "quote": "The hero academy games were perfectly paced and every child felt powerful and celebrated.", "name": "Karen Price", "event": "7th Birthday • Berkshire" },
      { "quote": "Best superhero performer we have ever booked. Top energy from start to finish!", "name": "James Sullivan", "event": "5th Birthday • London" }
    ],
    "gallery": [
      "assets/images/performer_superhero.jpg",
      "assets/images/superhero_party_1790842695325.jpg",
      "assets/images/family_holiday_party.jpg"
    ]
  },
  "captain_ray": {
    "name": "Captain Ray",
    "firstName": "Captain",
    "lastName": "Ray",
    "title": "Hero Academy Coach & Stunts",
    "img": "assets/images/performer_superhero.jpg",
    "secondaryImg": "assets/images/superhero_party_1790842695325.jpg",
    "rating": "4.9",
    "shows": "880+",
    "exp": "8 Years Experience",
    "price": "$220 / hr",
    "location": "London & Nationwide",
    "ages": "Ages 4 - 10 Years",
    "bio": "Captain Ray delivers action-packed superhero training courses, superhero games, and high-energy interactive fun for all brave young heroes.",
    "storyP1": "A full theatrical hero experience with agility drills, villain-stopping games, and teamwork missions.",
    "storyP2": "Finishes with an authentic hero graduation ceremony and memorable photo ops.",
    "reviews": [
      { "quote": "Captain Ray brought so much enthusiasm! The kids talked about hero training for weeks.", "name": "Laura Palmer", "event": "7th Birthday Party • London" },
      { "quote": "Every child got a superhero medal and felt like an absolute champion. Spectacular party!", "name": "Simon Cox", "event": "6th Birthday • Surrey" },
      { "quote": "Fantastic discipline and hilarious comedy mixed together. All the parents were thrilled.", "name": "Angela Reed", "event": "8th Birthday • Kent" }
    ],
    "gallery": [
      "assets/images/performer_superhero.jpg",
      "assets/images/superhero_party_1790842695325.jpg",
      "assets/images/family_holiday_party.jpg"
    ]
  },
  "emma": {
    "name": "Emma The Puppeteer",
    "firstName": "Emma",
    "lastName": "The Puppeteer",
    "title": "Master Puppeteer & Interactive Storyteller",
    "img": "assets/images/service_puppet_show.jpg",
    "secondaryImg": "assets/images/about_kids_birthday.jpg",
    "rating": "4.8",
    "shows": "610+",
    "exp": "8 Years Experience",
    "price": "$190 / hr",
    "location": "London & Home Counties",
    "ages": "Ages 2 - 8 Years",
    "bio": "Emma brings a vibrant cast of puppet friends to life in interactive musical adventures that have toddlers and young children fully spellbound.",
    "storyP1": "Featuring a custom tabletop puppet theater, hand-crafted fuzzy characters, and catchy interactive songs.",
    "storyP2": "Children get to meet the puppets up close and participate in funny puppet voice conversations.",
    "reviews": [
      { "quote": "Emma's puppet show had every single toddler giggling in complete harmony. Truly gifted performer.", "name": "Helen Martin", "event": "3rd Birthday Party • London" },
      { "quote": "The puppet characters were so vibrant and witty! Perfect for our 4-year-old's party.", "name": "Lucy Davis", "event": "4th Birthday • Essex" },
      { "quote": "Emma engaged every child effortlessly. Her warmth and vocal versatility are amazing.", "name": "Paul Foster", "event": "3rd Birthday • Surrey" }
    ],
    "gallery": [
      "assets/images/service_puppet_show.jpg",
      "assets/images/about_kids_birthday.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "chloe": {
    "name": "Chloe Balloon Sculptor",
    "firstName": "Chloe",
    "lastName": "Balloon Sculptor",
    "title": "Master Balloon Sculptor & Entertainer",
    "img": "assets/images/service_balloon_twisting.jpg",
    "secondaryImg": "assets/images/family_holiday_party.jpg",
    "rating": "4.9",
    "shows": "790+",
    "exp": "7 Years Experience",
    "price": "$185 / hr",
    "location": "London & South East",
    "ages": "All Ages",
    "bio": "Chloe twists wearable balloon hats, life-sized superheroes, magical unicorn wands, and playful balloon animals at lightning speed.",
    "storyP1": "A master balloon artist who combines lively interactive comedy with jaw-dropping sculptural skill.",
    "storyP2": "Guarantees every child receives multiple custom balloon creations to take home.",
    "reviews": [
      { "quote": "Chloe created balloon sculptures I didn't even know were possible! The kids were ecstatic.", "name": "Benjamin Scott", "event": "6th Birthday Party • London" },
      { "quote": "Unbelievable speed and creativity. The giant balloon crowns were the hit of the day!", "name": "Olivia Moore", "event": "5th Birthday • Kent" },
      { "quote": "Chloe was friendly, super energetic, and kept all 25 kids thoroughly delighted.", "name": "Jonathan Hall", "event": "7th Birthday • London" }
    ],
    "gallery": [
      "assets/images/service_balloon_twisting.jpg",
      "assets/images/family_holiday_party.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "arthur": {
    "name": "Arthur The Mind Reader",
    "firstName": "Arthur",
    "lastName": "The Mind Reader",
    "title": "Junior Mind Reader & Mentalist",
    "img": "assets/images/about_art_of_magic.jpg",
    "secondaryImg": "assets/images/pro_classic_magic.jpg",
    "rating": "5.0",
    "shows": "460+",
    "exp": "6 Years Experience",
    "price": "$210 / hr",
    "location": "London & Home Counties",
    "ages": "Ages 6 - 13 Years",
    "bio": "Arthur astounds young minds with intuitive mind reading, prediction tricks, and clever psychological mysteries designed especially for sharp, curious kids.",
    "storyP1": "Arthur turns audience members into mind readers, having them accurately guess secretly chosen numbers, colors, and mystery cards.",
    "storyP2": "Combines lighthearted mystery with intelligent humor that makes older kids and tweens feel respected and amazed.",
    "reviews": [
      { "quote": "Arthur had 15 eight-year-olds completely stumped and leaning forward in disbelief. Brilliant performer!", "name": "Clara Evans", "event": "8th Birthday Party • London" },
      { "quote": "Not a corny trick in the whole routine. Sophisticated, hilarious, and genuinely mystifying.", "name": "George Turner", "event": "9th Birthday • Surrey" },
      { "quote": "Our son wants to become a mentalist now! Arthur was courteous, punctual, and extraordinarily talented.", "name": "Victoria King", "event": "10th Birthday • Kent" }
    ],
    "gallery": [
      "assets/images/about_art_of_magic.jpg",
      "assets/images/pro_classic_magic.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "bella": {
    "name": "Bella Fairy Godmother",
    "firstName": "Bella",
    "lastName": "Fairy Godmother",
    "title": "Fairy Godmother & Enchanted Storyteller",
    "img": "assets/images/performer_fairy.jpg",
    "secondaryImg": "assets/images/sparkle_party.jpg",
    "rating": "4.9",
    "shows": "670+",
    "exp": "7 Years Experience",
    "price": "$205 / hr",
    "location": "London & South East",
    "ages": "Ages 3 - 8 Years",
    "bio": "Bella sprinkles enchanted fairy dust, leads sparkling wishing ceremonies, and guides children on mystical woodland adventures with illuminated fairy wings.",
    "storyP1": "Arriving with illuminated fairy wings and a crystal wand, Bella creates an atmosphere of pure warmth, kindness, and gentle wonder.",
    "storyP2": "Every child crafts their own enchanted wishing stone and joins the woodland fairy circle dance.",
    "reviews": [
      { "quote": "Bella was like a real angel in our garden. The wishing ceremony made my daughter feel so cherished.", "name": "Emily Watson", "event": "4th Birthday Party • Surrey" },
      { "quote": "Gentle, radiant, and wonderful with shy children. The fairy wings lit up our living room!", "name": "Rachel Morris", "event": "5th Birthday • London" },
      { "quote": "A completely magical experience. Every girl and boy was enchanted from start to finish.", "name": "Anthony Clark", "event": "4th Birthday • Essex" }
    ],
    "gallery": [
      "assets/images/performer_fairy.jpg",
      "assets/images/sparkle_party.jpg",
      "assets/images/family_holiday_party.jpg"
    ]
  },
  "tommy": {
    "name": "Tommy Slapstick Humorist",
    "firstName": "Tommy",
    "lastName": "Slapstick Humorist",
    "title": "Slapstick Comedy & Party Games Lead",
    "img": "assets/images/clown_party_1790842566084.jpg",
    "secondaryImg": "assets/images/pro_silly_clown.jpg",
    "rating": "4.7",
    "shows": "540+",
    "exp": "7 Years Experience",
    "price": "$175 / hr",
    "location": "London & Home Counties",
    "ages": "Ages 4 - 10 Years",
    "bio": "Tommy brings non-stop belly laughs with runaway props, classic banana-peel comedy, silly dance-offs, and high-energy party games.",
    "storyP1": "Tommy knows exactly how to get a whole room of children laughing out loud together within sixty seconds.",
    "storyP2": "Features hilarious tug-of-war challenges, musical freeze dancing, and Tommy's famous runaway pie trick.",
    "reviews": [
      { "quote": "Tommy had the entire room in stitches! The parents were laughing just as hard as the kids.", "name": "Gary Mitchell", "event": "6th Birthday Party • London" },
      { "quote": "Pure, unadulterated fun. Tommy's energy never flagged for a single minute.", "name": "Fiona Adams", "event": "7th Birthday • Kent" },
      { "quote": "Best party host we have had. The kids had an absolute blast running through his silly games.", "name": "David Lloyd", "event": "5th Birthday • Surrey" }
    ],
    "gallery": [
      "assets/images/clown_party_1790842566084.jpg",
      "assets/images/pro_silly_clown.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "dj_spark": {
    "name": "DJ Spark",
    "firstName": "DJ",
    "lastName": "Spark",
    "title": "Kids Party DJ & High-Energy MC",
    "img": "assets/images/theme_music.jpg",
    "secondaryImg": "assets/images/interactive_party_show.jpg",
    "rating": "4.8",
    "shows": "810+",
    "exp": "9 Years Experience",
    "price": "$225 / hr",
    "location": "London & Nationwide",
    "ages": "Ages 5 - 13 Years",
    "bio": "DJ Spark transforms your venue into an electrifying kids dance club with professional lighting rigs, bubble machines, and chart-topping dance choreography.",
    "storyP1": "Equipped with club-grade LED lighting, wireless microphones, and kid-safe hit playlists, Spark turns any party into a festival.",
    "storyP2": "Hosts glow-stick limbo competitions, crowd karaoke, and thrilling dance battles with prizes for all.",
    "reviews": [
      { "quote": "DJ Spark had 30 nine-year-olds bouncing and singing along for two solid hours. Absolutely stellar!", "name": "Melanie Carter", "event": "9th Birthday Party • London" },
      { "quote": "The lighting setup and sound were festival quality. Spark is a master MC who kept everyone hyped.", "name": "Craig Hughes", "event": "10th Birthday • Essex" },
      { "quote": "Our daughter said it was the best day of her life. DJ Spark is worth every penny!", "name": "Beatrice Young", "event": "8th Birthday • Surrey" }
    ],
    "gallery": [
      "assets/images/theme_music.jpg",
      "assets/images/interactive_party_show.jpg",
      "assets/images/family_holiday_party.jpg"
    ]
  },
  "elena": {
    "name": "Elena Magical Storyteller",
    "firstName": "Elena",
    "lastName": "Magical Storyteller",
    "title": "Magical Storyteller & Folk Musician",
    "img": "assets/images/about_kids_birthday.jpg",
    "secondaryImg": "assets/images/princess_party_1790842645232.jpg",
    "rating": "4.9",
    "shows": "730+",
    "exp": "8 Years Experience",
    "price": "$185 / hr",
    "location": "London & South East",
    "ages": "Ages 2 - 7 Years",
    "bio": "Elena weaves captivating folk tales with acoustic folk instruments, gentle puppetry, and interactive story journeys that spark deep childhood imagination.",
    "storyP1": "Elena brings along sensory story props, bell chimes, and soft velvet tapestries that envelop children in a tranquil fairy world.",
    "storyP2": "Kids actively participate as story characters, creating wind sounds, animal calls, and finding the hidden magical treasure.",
    "reviews": [
      { "quote": "Elena has a soothing, enchanting presence. Even our rowdiest toddler was sitting quietly, eyes wide in wonder.", "name": "Joanne Bailey", "event": "3rd Birthday Party • London" },
      { "quote": "Beautiful acoustic singing and gentle stories. A welcome, calm breath of fresh air for our celebration.", "name": "Michael Bennett", "event": "4th Birthday • Kent" },
      { "quote": "Truly wholesome entertainment. Elena is a genuine storyteller of the highest order.", "name": "Sarah Collins", "event": "5th Birthday • Berkshire" }
    ],
    "gallery": [
      "assets/images/about_kids_birthday.jpg",
      "assets/images/princess_party_1790842645232.jpg",
      "assets/images/sparkle_party.jpg"
    ]
  },
  "giggles": {
    "name": "Giggles Face Painting Clown",
    "firstName": "Giggles",
    "lastName": "Face Painting Clown",
    "title": "Face Painting Clown & Balloon Modeler",
    "img": "assets/images/pro_clown_blog.jpg",
    "secondaryImg": "assets/images/service_face_painting.jpg",
    "rating": "5.0",
    "shows": "690+",
    "exp": "8 Years Experience",
    "price": "$190 / hr",
    "location": "London & Home Counties",
    "ages": "Ages 3 - 9 Years",
    "bio": "Giggles combines gentle comedy, lightning-fast balloon twisting, and sparkling face painting for an all-in-one entertainment feast that toddlers and kids adore.",
    "storyP1": "A brightly dressed, smile-inducing performer who gently warms up children with silly feather duster tricks before painting masterpieces.",
    "storyP2": "Every child gets custom face art and a wearable balloon sculpture created right before their eyes.",
    "reviews": [
      { "quote": "Giggles was an absolute delight! The face painting was gorgeous and the balloon animals were so sturdy.", "name": "Claire Richardson", "event": "5th Birthday Party • London" },
      { "quote": "So warm and gentle. None of the younger kids were scared of the clown makeup at all—they loved her!", "name": "Trevor Scott", "event": "4th Birthday • Surrey" },
      { "quote": "Two hours of nonstop joy. Giggles managed everything with a warm smile and great professionalism.", "name": "Linda Edwards", "event": "6th Birthday • Essex" }
    ],
    "gallery": [
      "assets/images/pro_clown_blog.jpg",
      "assets/images/service_face_painting.jpg",
      "assets/images/clown_party_1790842566084.jpg"
    ]
  },
  "steve": {
    "name": "Steve Action Games Host",
    "firstName": "Steve",
    "lastName": "Action Games Host",
    "title": "Hero Bootcamp & Action Games Coach",
    "img": "assets/images/superhero_party_1790842695325.jpg",
    "secondaryImg": "assets/images/performer_superhero.jpg",
    "rating": "4.9",
    "shows": "580+",
    "exp": "6 Years Experience",
    "price": "$195 / hr",
    "location": "London & Nationwide",
    "ages": "Ages 5 - 12 Years",
    "bio": "Coach Steve leads high-octane sports obstacle relays, dodgeball tournaments, nerf tag battles, and collaborative field day games with boundless enthusiasm.",
    "storyP1": "Former youth sports instructor Steve brings pop-up obstacle courses, cones, parachutes, and whistles to get everyone moving.",
    "storyP2": "Emphasizes sportsmanship, high energy teamwork, and ensures every single child crosses the finish line a winner.",
    "reviews": [
      { "quote": "Coach Steve tire out 20 energetic boys and girls while keeping everyone smiling and safe. Phenomenal party!", "name": "Paul Harrison", "event": "8th Birthday Party • London" },
      { "quote": "The obstacle course was brilliantly designed and the team relay races were a riot. Highly recommend Steve!", "name": "Rebecca Ward", "event": "7th Birthday • Surrey" },
      { "quote": "Steve was fantastic at including children of all athletic abilities. Truly top-class host.", "name": "Jason Phillips", "event": "9th Birthday • Kent" }
    ],
    "gallery": [
      "assets/images/superhero_party_1790842695325.jpg",
      "assets/images/performer_superhero.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "mia": {
    "name": "Mia Bubble Specialist",
    "firstName": "Mia",
    "lastName": "Bubble Specialist",
    "title": "Giant Bubble Specialist & Wonder Artist",
    "img": "assets/images/service_bubble_show.jpg",
    "secondaryImg": "assets/images/family_holiday_party.jpg",
    "rating": "4.9",
    "shows": "640+",
    "exp": "7 Years Experience",
    "price": "$195 / hr",
    "location": "London & Home Counties",
    "ages": "All Ages",
    "bio": "Mia creates jaw-dropping giant smoke-filled bubbles, rainbow bubble sculptures, and puts children inside real life-sized bubbles for the ultimate photo moment.",
    "storyP1": "Using secret eco-friendly bubble formulas, Mia constructs shimmering bubbles larger than cars that gently float through gardens and halls.",
    "storyP2": "The grand finale features the famous 'Child Inside a Bubble' stunt, where every guest steps inside an iridescent bubble column.",
    "reviews": [
      { "quote": "Standing inside a real giant bubble was something my daughter will never forget! Mia is fantastic.", "name": "Jessica Wright", "event": "5th Birthday Party • London" },
      { "quote": "The bubble tricks with smoke and fire-safe foam were mesmerizing. Parents were just as enthralled as kids.", "name": "Brian Cox", "event": "6th Birthday • Berkshire" },
      { "quote": "So clean, beautiful, and visually spectacular. The outdoor lawn was filled with hundreds of giant bubbles!", "name": "Caroline Lewis", "event": "4th Birthday • Surrey" }
    ],
    "gallery": [
      "assets/images/service_bubble_show.jpg",
      "assets/images/family_holiday_party.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "the_great_z": {
    "name": "The Great Z",
    "firstName": "The Great",
    "lastName": "Z",
    "title": "Close-up Card Conjurer & Sleight of Hand",
    "img": "assets/images/pro_classic_magic.jpg",
    "secondaryImg": "assets/images/pro_grand_stage.jpg",
    "rating": "4.9",
    "shows": "820+",
    "exp": "11 Years Experience",
    "price": "$230 / hr",
    "location": "London & South East",
    "ages": "Ages 6 - 14 Years",
    "bio": "The Great Z performs impossible close-up card miracles, coin vanishings right in children's open palms, and mind-boggling rope restorations.",
    "storyP1": "An award-winning close-up magician of the Magic Circle, The Great Z performs inches away from spectators with zero smoke or mirrors.",
    "storyP2": "Includes a private masterclass where the birthday child learns an impossible card secret to amaze their friends at school.",
    "reviews": [
      { "quote": "The Great Z did tricks right in my son's hands that defied all logic. An absolute genius!", "name": "Stuart Barnes", "event": "9th Birthday Party • London" },
      { "quote": "Unbelievable close-up technique and charismatic showmanship. Adults and kids were totally spellbound.", "name": "Patricia King", "event": "11th Birthday • Kent" },
      { "quote": "Classy, witty, and astonishing. The Great Z elevated our family party into a premier event.", "name": "Howard Bell", "event": "10th Birthday • London" }
    ],
    "gallery": [
      "assets/images/pro_classic_magic.jpg",
      "assets/images/pro_grand_stage.jpg",
      "assets/images/interactive_party_show.jpg"
    ]
  },
  "aurora": {
    "name": "Princess Aurora",
    "firstName": "Princess",
    "lastName": "Aurora",
    "title": "Snow & Frost Princess Storyteller",
    "img": "assets/images/sparkle_party.jpg",
    "secondaryImg": "assets/images/princess_portrait_1790843055244.jpg",
    "rating": "5.0",
    "shows": "950+",
    "exp": "9 Years Experience",
    "price": "$215 / hr",
    "location": "London & Home Counties",
    "ages": "Ages 3 - 9 Years",
    "bio": "Princess Aurora brings winter magic and fairytale elegance to life with live vocal performances, snowflake dances, and an enchanting royal coronation ceremony.",
    "storyP1": "Dressed in an illuminated shimmering winter gown, Aurora sings iconic fairytale anthems and leads gentle royal etiquette lessons.",
    "storyP2": "Every child receives a sparkling snowflake tiara and takes part in the magical coronation circle.",
    "reviews": [
      { "quote": "Princess Aurora made our little girl's winter wonderland dreams come true! Her live vocals are stunning.", "name": "Catherine Price", "event": "5th Birthday Party • London" },
      { "quote": "The coronation was so emotional and sweet. Aurora has the voice and grace of a true fairytale princess.", "name": "Darren Walker", "event": "6th Birthday • Surrey" },
      { "quote": "Every single child was spellbound. Aurora is the gold standard for princess entertainment.", "name": "Natalie Foster", "event": "4th Birthday • Essex" }
    ],
    "gallery": [
      "assets/images/sparkle_party.jpg",
      "assets/images/princess_portrait_1790843055244.jpg",
      "assets/images/family_holiday_party.jpg"
    ]
  }
}

print(f"Total performers created: {len(db)}")
with open('scratch/full_entertainers_db.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2)
print("Saved to scratch/full_entertainers_db.json")
