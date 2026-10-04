from PIL import Image

def remove_white_bg(img_path, out_path, threshold=235):
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Check if the pixel is near-white
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            # Change near-white to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, "PNG")

remove_white_bg("assets/images/magic_hat_logo.jpg", "assets/images/magic_hat_logo.png")
