import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Linux Foundation Logo
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Linux_Foundation_logo.svg/1200px-Linux_Foundation_logo.svg.png" 
# Alternative: "https://www.linuxfoundation.org/wp-content/uploads/2020/01/linux-foundation-logo-color.png" (official usually better)
url_lf = "https://www.linuxfoundation.org/wp-content/uploads/2020/01/linux-foundation-logo-color.png"

# I need to ensure Red Hat is good too, earlier I copied fallback.
# Let's try to get a real Red Hat one if possible, but I'll stick to LF for now.
# LPI and CompTIA are already there from previous steps (unless I deleted them? No, I only reverted code, images persist).

images = {
    "lf_logo.png": url_lf
}

headers = {'User-Agent': 'Mozilla/5.0'}
save_dir = r"c:/Users/HP/Desktop/my_profile/images/"

for name, url in images.items():
    print(f"Downloading {name} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx) as response:
            data = response.read()
            with open(os.path.join(save_dir, name), 'wb') as out_file:
                out_file.write(data)
        print(f"Success: {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
