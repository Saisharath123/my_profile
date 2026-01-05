from PIL import Image
import os

images = [
    "module_icon_profile.png",
    "module_icon_courses.png",
    "module_icon_projects.png",
    "module_icon_skill_analyzer.png",
    "module_icon_contact.png"
]
base_dir = r"c:\Users\HP\Desktop\my_profile\images"

def clean_image(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename}")
        return

    print(f"Processing {filename}...")
    try:
        img = Image.open(path).convert("RGBA")
    except:
        return

    datas = img.getdata()
    new_data = []
    
    # Simple threshold
    # Since these are computer generated on pure white, a high threshold is fine.
    # But shadows might be grey.
    for item in datas:
        # Check if white-ish (near 255,255,255)
        if item[0] > 220 and item[1] > 220 and item[2] > 220:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(path)

for i in images:
    clean_image(i)
