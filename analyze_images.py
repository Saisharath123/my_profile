from PIL import Image
import os

images = [
    r"c:\Users\HP\Desktop\my_profile\images\azure_fundamentals.png",
    r"c:\Users\HP\Desktop\my_profile\images\azure_administrator_associate.png",
    r"c:\Users\HP\Desktop\my_profile\images\azure_solutions_architect_expert.png",
    r"c:\Users\HP\Desktop\my_profile\images\azure_devops_engineer_expert.png"
]

for img_path in images:
    if os.path.exists(img_path):
        img = Image.open(img_path)
        print(f"{os.path.basename(img_path)}: {img.size}")
        # Get bounding box of non-zero regions to see if there is padding
        bbox = img.getbbox()
        if bbox:
            print(f"  Content bbox: {bbox} (width: {bbox[2]-bbox[0]}, height: {bbox[3]-bbox[1]})")
        else:
            print("  Empty image")
