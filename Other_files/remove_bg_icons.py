from PIL import Image

def remove_background(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Change white (and near white) to transparent
            if item[0] > 230 and item[1] > 230 and item[2] > 230:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Successfully saved transparent image to {output_path}")
    except Exception as e:
        print(f"Error processing image {input_path}: {e}")

tasks = [
    (r"c:\Users\HP\Desktop\my_profile\images\live_test_icon.png", r"c:\Users\HP\Desktop\my_profile\images\live_test_icon_transparent.png"),
    (r"c:\Users\HP\Desktop\my_profile\images\interview_icon.png", r"c:\Users\HP\Desktop\my_profile\images\interview_icon_transparent.png")
]

for input_file, output_file in tasks:
    remove_background(input_file, output_file)
