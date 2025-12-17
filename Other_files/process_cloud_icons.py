
from PIL import Image
import os

def remove_background(input_path, output_path):
    print(f"Processing {input_path}...")
    try:
        if not os.path.exists(input_path):
            print(f"Error: File not found - {input_path}")
            return

        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Change all white (also shades of whites) to transparent
            # Adjusted threshold slightly to be safe
            if item[0] > 230 and item[1] > 230 and item[2] > 230:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        
        # Resize to fit module size better (e.g., 200x200 max)
        img.thumbnail((256, 256), Image.Resampling.LANCZOS)
        
        img.save(output_path, "PNG")
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Paths
brain_dir = "C:/Users/HP/.gemini/antigravity/brain/50652d80-0ace-4b85-8050-ab395fa77515/"
images_dir = "c:/Users/HP/Desktop/my_profile/images/"

# 1. AWS (Generated)
aws_source = os.path.join(brain_dir, "aws_icon_1765962751235.png")
remove_background(aws_source, os.path.join(images_dir, "aws_icon.png"))

# 2. Azure (User Uploaded)
# User uploaded image ID: uploaded_image_1765962931117.png
azure_source = os.path.join(brain_dir, "uploaded_image_1765962931117.png")
remove_background(azure_source, os.path.join(images_dir, "azure_icon.png"))

# 3. GCP (Generated)
gcp_source = os.path.join(brain_dir, "gcp_icon_1765962994516.png")
remove_background(gcp_source, os.path.join(images_dir, "gcp_icon.png"))
