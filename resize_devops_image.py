from PIL import Image

path = r"c:\Users\HP\Desktop\my_profile\images\azure_devops_engineer_expert.png"
target_height = 500

try:
    img = Image.open(path).convert("RGBA")
    
    # 1. Crop to content
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        print(f"Cropped to {img.size}")
    
    # 2. Resize to target height
    ratio = target_height / img.height
    new_width = int(img.width * ratio)
    img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
    
    print(f"Resized to {img.size}")
    img.save(path, "PNG")
    print("Success")
except Exception as e:
    print(e)
