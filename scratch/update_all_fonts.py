import os, glob

def replace_fonts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Imports
    content = content.replace(
        "https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Nunito+Sans:wght@300;400;600;700;800&display=swap",
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap"
    )
    
    # CSS variables and font-families
    content = content.replace("'Nunito Sans', sans-serif", "'Inter', sans-serif")
    content = content.replace("Nunito Sans", "Inter")
    content = content.replace("'Berkshire Swash', cursive", "'Playfair Display', serif")
    content = content.replace("Berkshire Swash", "Playfair Display")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in glob.glob('*.html') + glob.glob('css/*.css'):
    replace_fonts(file)

print("Updated all fonts.")
