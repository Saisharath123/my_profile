from PIL import Image
import os

def remove_background(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Change white (and near white) to transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Successfully saved transparent image to {output_path}")
    except Exception as e:
        print(f"Error processing image {input_path}: {e}")

input_file = r"c:\Users\HP\Desktop\my_profile\images\linux.jpg"
output_file = r"c:\Users\HP\Desktop\my_profile\images\linux_transparent.png"

remove_background(input_file, output_file)
