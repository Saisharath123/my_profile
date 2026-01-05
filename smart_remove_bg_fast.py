from PIL import Image
import os
import sys

# List of icons to process
images = [
    "module_icon_profile.png",
    "module_icon_courses.png",
    "module_icon_projects.png",
    "module_icon_skill_analyzer.png",
    "module_icon_contact.png"
]
base_dir = r"c:\Users\HP\Desktop\my_profile\images"
# Using a fixed stack (DFS) or deque is faster than list.pop(0) which is O(n)
# Also using ImageDraw geometry might be faster but simple pixel access is ok for small icons.
# This version uses deque for BFS.

from collections import deque

def flood_fill_remove_bg(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        return

    print(f"Processing {filename}...")
    try:
        img = Image.open(path).convert("RGBA")
    except:
        return

    width, height = img.size
    pixels = img.load()
    
    threshold = 50 
    target_bg = (255, 255, 255)

    def is_similar_val(c):
        # Optimization: inline logic
        return abs(c[0]-255) < threshold and abs(c[1]-255) < threshold and abs(c[2]-255) < threshold

    queue = deque()
    visited = set()

    corners = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    for cx, cy in corners:
        if is_similar_val(pixels[cx, cy]):
            queue.append((cx, cy))
            visited.add((cx, cy))
    
    while queue:
        x, y = queue.popleft()
        pixels[x, y] = (0, 0, 0, 0)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                # To save memory, we can check pixel value first before adding to visited set
                if (nx, ny) not in visited:
                    if is_similar_val(pixels[nx, ny]):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
    
    img.save(path)
    print(f"Saved {filename}")

if __name__ == "__main__":
    for img_name in images:
        flood_fill_remove_bg(img_name)
