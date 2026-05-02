from PIL import Image

def remove_background(input_path, output_path, bg_color_hex):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    
    # hex to rgb
    bg_color = tuple(int(bg_color_hex[i:i+2], 16) for i in (0, 2, 4))
    
    new_data = []
    for item in data:
        # Check if color is close to background color
        if abs(item[0] - bg_color[0]) < 20 and abs(item[1] - bg_color[1]) < 20 and abs(item[2] - bg_color[2]) < 20:
            new_data.append((255, 255, 255, 0)) # Transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

remove_background("public/logo1.png", "public/logo_transparent.png", "0F2C3E")
