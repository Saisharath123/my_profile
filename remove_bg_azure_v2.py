from PIL import Image
import os

def remove_background_flood(image_path):
    print(f"Processing {image_path}...")
    try:
        img = Image.open(image_path).convert("RGBA")
        datas = img.getdata()
        
        # Get the background color from the top-left pixel
        bg_color = img.getpixel((0, 0))
        print(f"Detected background color: {bg_color}")
        
        newData = []
        
        # Tolerance for color matching (to handle compression artifacts)
        tolerance = 50 
        
        for item in datas:
            # Calculate distance between current pixel and background color
            # Simple Euclidean-like distance in RGB space
            diff = sum([abs(item[i] - bg_color[i]) for i in range(3)])
            
            if diff < tolerance:
                 # Make transparent
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        
        img.putdata(newData)
        img.save(image_path, "PNG")
        print(f"Successfully processed {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

images = [
    r"c:\Users\HP\Desktop\my_profile\images\azure_devops_engineer_expert.png",
    r"c:\Users\HP\Desktop\my_profile\images\azure_administrator_associate.png"
]

for img_path in images:
    if os.path.exists(img_path):
        remove_background_flood(img_path)
    else:
        print(f"File not found: {img_path}")
