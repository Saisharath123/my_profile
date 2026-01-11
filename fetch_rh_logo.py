import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://avatars.githubusercontent.com/u/158763?s=200&v=4"
save_path = r"c:/Users/HP/Desktop/my_profile/images/redhat_logo.png"

headers = {'User-Agent': 'Mozilla/5.0'}

print(f"Downloading redhat_logo.png from {url}...")
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as response:
        data = response.read()
        with open(save_path, 'wb') as out_file:
            out_file.write(data)
    print("Success: redhat_logo.png")
except Exception as e:
    print(f"Failed redhat_logo.png: {e}")
