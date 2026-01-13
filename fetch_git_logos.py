import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

images = {
    "redhat_logo.png": "https://raw.githubusercontent.com/redhat-developer-demos/rhd-tutorial-common/master/images/redhat-logo.png",
    "lf_logo.png": "https://w7.pngwing.com/pngs/361/528/png-transparent-linux-foundation-membership-organization-non-profit-organisation-software-foundation-miscellaneous-text-logo.png"
}
# Backup LF: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Linux_Foundation_logo.svg/1200px-Linux_Foundation_logo.svg.png (Blocked usually)
# Provide a simpler source if possible.
# Actually, let's try a different LF one if pngwing fails (blocks bots sometimes).
# Let's try: https://avatars.githubusercontent.com/u/4515128?s=280&v=4 (Linux Foundation GitHub Avatar)
images["lf_logo.png"] = "https://avatars.githubusercontent.com/u/4515128?s=280&v=4"

# Add GitHub Logo
# images["github_logo.png"] = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"


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
