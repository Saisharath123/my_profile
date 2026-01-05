from PIL import Image
import math
import os

images = [
    "module_icon_profile.png",
    "module_icon_courses.png",
    "module_icon_projects.png",
    "module_icon_skill_analyzer.png",
    "module_icon_contact.png"
]
base_dir = r"c:\Users\HP\Desktop\my_profile\images"

def color_dist(c1, c2):
    return math.sqrt(sum((a-b)**2 for a, b in zip(c1[:3], c2[:3])))

def clean_image(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename} - found")
        return

    print(f"Processing {filename}...")
    try:
        img = Image.open(path).convert("RGBA")
    except Exception as e:
        print(f"Error opening {filename}: {e}")
        return

    width, height = img.size
    pixels = img.load()

    # Seed points: corners
    seeds = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    
    visited = set()
    queue = []
    
    target_bg = (255, 255, 255) 
    
    # Only start from corners that are reasonably light
    for sx, sy in seeds:
        if (sx, sy) not in visited:
            c = pixels[sx, sy]
            if color_dist(c, target_bg) < 150: 
                queue.append((sx, sy))
                visited.add((sx, sy))

    # BFS Flood Fill with high tolerance to eat shadows
    # Shadows on white can be light grey. Distance between (255,255,255) and (200,200,200) is sqrt(55^2*3) ~= 95
    tolerance = 90  
    
    while queue:
        x, y = queue.pop(0)
        pixels[x, y] = (0, 0, 0, 0) # Make transparent

        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    color = pixels[nx, ny]
                    if color_dist(color, target_bg) < tolerance:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
    
    img.save(path)

for i in images:
    clean_image(i)
