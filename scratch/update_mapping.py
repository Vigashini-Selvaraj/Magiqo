import re

file_path = 'c:/Users/vigas/Desktop/magiqo/service_detail.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_map = """const serviceToEntertainerMap = {
          "Grand Stage Magician": { name: "Elias", id: "elias" },
          "Friendly Mascots": { name: "Rex", id: "rex" },
          "Royal Princess Visit": { name: "Lily", id: "lily" },
          "Action Superhero": { name: "Captain Ray", id: "captain_ray" },
          "Classic Clown": { name: "Barnaby", id: "barnaby" },
          "Face Painting Pro": { name: "Sarah", id: "sarah" },
          "Close-Up Magician": { name: "David", id: "david" },
          "Balloon Twisting": { name: "Giggles", id: "giggles" },
          "Interactive Puppet Show": { name: "Tommy", id: "tommy" },
          "High-Energy Party Host": { name: "Steve", id: "steve" },
          "Magic Workshop": { name: "Emma", id: "emma" },
          "Enchanted Storyteller": { name: "Aurora", id: "aurora" },
          "Master Illusionist": { name: "Arthur", id: "arthur" },
          "Fairy Godmother": { name: "Bella", id: "bella" },
          "Comedy Juggler": { name: "Jojo", id: "jojo" },
          "Glitter Tattoos": { name: "Chloe", id: "chloe" },
          "Giant Bubble Show": { name: "Elena", id: "elena" },
          "Kids Party DJ": { name: "DJ Spark", id: "dj_spark" },
          "Space Warrior Training": { name: "Captain Ray", id: "captain_ray" },
          "Animal Encounters": { name: "Steve", id: "steve" }
        };"""

content = re.sub(r'const serviceToEntertainerMap = \{[^}]+\};', new_map, content, flags=re.MULTILINE|re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mapping updated successfully!")
