import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# UrbanPro Logo
url = "https://s3-ap-southeast-1.amazonaws.com/urbanpro-seo-images-bucket/seo-images/urbanpro-logo.png"
save_path = r"c:/Users/HP/Desktop/my_profile/images/urbanpro_logo.png"

headers = {'User-Agent': 'Mozilla/5.0'}

print(f"Downloading urbanpro_logo.png from {url}...")
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as response:
        data = response.read()
        with open(save_path, 'wb') as out_file:
            out_file.write(data)
    print("Success: urbanpro_logo.png")
except Exception as e:
    print(f"Failed urbanpro_logo.png: {e}")
