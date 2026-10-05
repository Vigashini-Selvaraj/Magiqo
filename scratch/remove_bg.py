from PIL import Image

def make_transparent(input_path, output_path, bg_color=None, tolerance=15):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    
    # If bg_color is not provided, pick the top-left pixel
    if bg_color is None:
        bg_color = data[0]

    new_data = []
    for item in data:
        # Check if pixel is within tolerance of background color
        if all(abs(item[i] - bg_color[i]) <= tolerance for i in range(3)):
            # It's background, make it fully transparent
            new_data.append((255, 255, 255, 0))
        else:
            # Not background, but we might want to do partial transparency for anti-aliasing
            # For simplicity, keep it opaque
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    make_transparent('assets/full logo.png', 'assets/full logo.png', tolerance=25)
    make_transparent('assets/logoooo.png', 'assets/logoooo.png', tolerance=25)
    print("Background removed from logos.")
