from PIL import Image

def crop_transparent(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Get bounding box of non-transparent pixels
    bbox = img.getbbox()
    
    if bbox:
        # Crop the image to the bounding box
        cropped_img = img.crop(bbox)
        cropped_img.save(output_path, "PNG")
        print(f"Cropped to {bbox}")
    else:
        print("Image is fully transparent or no bounding box found.")

crop_transparent("public/logo_transparent.png", "public/logo_cropped.png")
