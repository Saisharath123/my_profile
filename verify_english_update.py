
import sys
import os

sys.path.append(r"c:\Users\HP\Desktop\my_profile")

try:
    import courses_english
    html = courses_english.render()
    print("SUCCESS: Rendered HTML length:", len(html))
    if "Communicate with Impact" in html and "english-card" in html:
         print("VERIFIED: Core content and styles found.")
    else:
         print("WARNING: Expected content missing.")
except Exception as e:
    print("ERROR:", e)
