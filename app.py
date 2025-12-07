# Single-file Flask site "Cloud with Sai"
# - Active module button highlight (blue)
# - / (root) renders profile
# - Cloud logo sky-blue; subtitle continuously types
# - Four modules only: Profile, Courses, Projects, Contact (contact icon set to mobile 📱)
import os
import json
from datetime import datetime, timezone
from flask import Flask, request, render_template_string, redirect, url_for, flash, send_from_directory, abort

# Email imports
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "replace_this_with_a_random_secret_for_prod"

# Email configuration (you will replace the password locally)
EMAIL_ADDRESS = "multiclouddevops4u@gmail.com"
EMAIL_PASSWORD = "mpvbvlovezpjlgmq"
TO_EMAIL = "multiclouddevops4u@gmail.com"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
CLOUD_FILENAME = "cloud.webp"
ME_FILENAME = "me.png"

def list_images(subfolder=""):
    folder = os.path.join(IMAGES_DIR, subfolder) if subfolder else IMAGES_DIR
    if not os.path.isdir(folder):
        return []
    files = []
    for f in sorted(os.listdir(folder)):
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")):
            files.append(f)
    return files

@app.route("/images/<path:filename>")
def image_file(filename):
    # secure serve from images dir
    filename = filename.lstrip("/\\")
    full_path = os.path.normpath(os.path.join(IMAGES_DIR, filename))
    images_dir_norm = os.path.normpath(IMAGES_DIR)
    if not (full_path.startswith(images_dir_norm + os.sep) or full_path == images_dir_norm):
        abort(404)
    if not os.path.exists(full_path) or not os.path.isfile(full_path):
        abort(404)
    rel_dir = os.path.dirname(os.path.relpath(full_path, IMAGES_DIR))
    if rel_dir == ".":
        rel_dir = ""
    directory = os.path.join(IMAGES_DIR, rel_dir) if rel_dir else IMAGES_DIR
    return send_from_directory(directory, os.path.basename(full_path))

# Email configuration transferred to contact_page.py


BASE_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cloud with Sai</title>

  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">

  <style>
    :root{
      --accent-a: #6EE7B7;
      --accent-b: #60A5FA;
      --accent-c: #7C3AED;
      --muted-dark: #0b1620;
      --muted-gray: #6b7280;
      --card-radius: 12px;
      --nav-height: 110px;
      --module-size: 110px;
    }

    html,body{
      height:100%;
      margin:0;
      font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: #ffffff;
      color: #0b1620;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }

    /* Header */
    header.app-header {
      position:sticky;
      top:0;
      z-index:40;
      backdrop-filter: blur(6px);
      background: linear-gradient(180deg, rgba(255,255,255,0.99), rgba(255,255,255,0.97));
      border-bottom: 1px solid rgba(10,20,30,0.06);
      padding: 10px 20px;
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:12px;
      height: var(--nav-height);
    }

    /* brand group: logo + title aligned side-by-side, no wrap */
    .brand {
      display:flex;
      align-items:center;
      gap:12px;
      flex-wrap:nowrap;
      min-width:0;
    }

    /* Cloud logo: no box, larger, aligned to title baseline */
    .cloud-logo {
      height:88px;
      width:auto;
      display:flex;
      align-items:center;
      justify-content:center;
      flex-shrink:0;
      overflow:visible;
      margin:0;
    }
    .cloud-logo img {
      height:84px;
      width:auto;
      object-fit:contain;
      display:block;
      /* stronger sky-blue tint */
      filter: brightness(1.05) saturate(2.6) hue-rotate(200deg);
      vertical-align:middle;
    }

    /* Title block */
    .title-wrap { display:flex; flex-direction:column; justify-content:center; line-height:1; margin:0; padding:0; }
    .title {
      font-weight:900;
      font-size:32px;
      margin:0;
      letter-spacing:-0.6px;
      background: linear-gradient(90deg, var(--accent-c), var(--accent-b), var(--accent-a), var(--accent-b));
      background-size: 300% 100%;
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      animation: slidebg 5.5s linear infinite;
    }
    @keyframes slidebg {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* subtitle (typewriter handled by JS) */
    .title-sub {
      font-size:14px;
      color:var(--muted-gray);
      margin-top:6px;
      text-transform:none;
      font-weight:700;
      display:inline-block;
      position:relative;
      white-space:pre-wrap;
      letter-spacing:0.2px;
      opacity:1;
    }
    .title-sub .ch {
      opacity:0;
      transform: translateY(6px);
      display:inline-block;
      transition: opacity 140ms ease, transform 160ms cubic-bezier(.2,.9,.25,1), text-shadow 220ms ease;
    }
    .title-sub .ch.show {
      opacity:1;
      transform: translateY(0);
      text-shadow: 0 0 12px rgba(96,165,250,0.08);
    }
    .title-sub::after {
      content: "";
      position: absolute;
      left: -30%;
      top: 0;
      height: 100%;
      width: 60%;
      pointer-events: none;
      background: linear-gradient(90deg, rgba(255,255,255,0.0), rgba(255,255,255,0.28), rgba(255,255,255,0.0));
      transform: skewX(-12deg) translateX(-100%);
      opacity: 0.6;
      filter: blur(6px);
      animation: sweep 4s linear infinite;
    }
    @keyframes sweep {
      0% { transform: skewX(-12deg) translateX(-100%); opacity: 0; }
      15% { opacity: 0.3; }
      50% { transform: skewX(-12deg) translateX(40%); opacity: 0.6; }
      85% { opacity: 0.15; }
      100% { transform: skewX(-12deg) translateX(200%); opacity: 0; }
    }

    .subtitle-particles { position:absolute; right: -6px; top: -26px; width:120px; height:36px; pointer-events:none; overflow:visible; }
    .subtitle-particles span {
      position:absolute; display:block; width:10px; height:10px; border-radius:50%;
      background: rgba(96,165,250,0.12); transform: translateY(0);
      animation: floatUp linear infinite;
      filter: blur(0.8px);
    }
    .subtitle-particles span.p1 { left:8px; bottom:0; width:8px; height:8px; animation-duration:2.8s; animation-delay:0.1s; }
    .subtitle-particles span.p2 { left:34px; bottom:8px; width:6px; height:6px; animation-duration:2.2s; animation-delay:0.4s; background: rgba(124,58,237,0.10); }
    .subtitle-particles span.p3 { left:60px; bottom:2px; width:9px; height:9px; animation-duration:3.8s; animation-delay:0.8s; background: rgba(110,231,183,0.08); }
    .subtitle-particles span.p4 { left:88px; bottom:6px; width:6px; height:6px; animation-duration:3.0s; animation-delay:0.3s; background: rgba(96,165,250,0.09); }
    @keyframes floatUp {
      0% { transform: translateY(6px) scale(0.85); opacity:0; }
      10% { opacity:0.45; }
      50% { transform: translateY(-18px) scale(1); opacity:0.85; }
      100% { transform: translateY(-46px) scale(0.9); opacity:0; }
    }

    /* modules */
    nav.modules { display:flex; align-items:center; gap:10px; height:100%; }
    .module {
      width: var(--module-size);
      height: var(--module-size);
      min-width: var(--module-size);
      border-radius: 10px;
      display:flex;
      flex-direction:column;
      align-items:center;
      justify-content:center;
      gap:6px;
      background: #fff;
      border: 1px solid rgba(10,20,30,0.06);
      box-shadow: 0 6px 18px rgba(12,24,36,0.04);
      text-decoration:none;
      color: var(--muted-dark);
      transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease, color 180ms ease;
      cursor:pointer;
      font-weight:700;
    }
    .module .icon { font-size:20px; }
    .module .label { font-weight:700; font-size:13px; }

    .module:hover { transform: translateY(-6px) scale(1.03); box-shadow: 0 16px 36px rgba(12,24,36,0.09); background: linear-gradient(180deg, rgba(246,252,255,1), #ffffff); border-color: rgba(10,20,30,0.09); }

    /* ACTIVE module style (blue highlight) */
    .module.active {
      background: linear-gradient(90deg, var(--accent-b), var(--accent-a));
      color: #02203a;
      border-color: rgba(96,165,250,0.18);
      box-shadow: 0 18px 48px rgba(96,165,250,0.12);
      transform: translateY(-6px) scale(1.03);
    }
    .module.active .label, .module.active .icon { color: #02203a; }

    .container { max-width:1100px; margin:18px auto; padding:20px; }
    .card { background: #ffffff; border-radius: 12px; padding:20px; border: 1px solid rgba(10,20,30,0.05); box-shadow: 0 8px 30px rgba(10,20,30,0.03); }

    /* profile */
    .profile { display:flex; gap:20px; align-items:center; flex-wrap:wrap; }
    .avatar { width:260px; height:260px; border-radius:50%; overflow:hidden; flex-shrink:0; background:transparent; display:flex; align-items:center; justify-content:center; box-shadow: 0 8px 22px rgba(2,6,23,0.06); margin-top:-12px; }
    .avatar img { width:100%; height:100%; object-fit:cover; object-position:50% 18%; display:block; background:transparent; border-radius:0; }

    .profile-text { flex:1; min-width:260px; }
    .intro { font-size:15px; color:#374151; font-weight:700; line-height:1.45; }
    .contact-row { display:flex; gap:16px; align-items:center; margin-top:12px; flex-wrap:wrap; }
    .contact-item { display:flex; gap:8px; align-items:center; color:#374151; font-weight:700; font-size:14px; }
    .contact-item svg { width:18px; height:18px; fill:#0b1620; opacity:0.9; }

    .grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(240px,1fr)); gap:16px; margin-top:14px; }

    @media (max-width:960px){
      header.app-header { padding:8px 12px; height:120px; }
      .title { font-size:24px; }
      .title-sub { font-size:12px; white-space:normal; }
      .subtitle-particles { display:none; }
      .module { width:96px; height:96px; min-width:96px; }
      .avatar { width:160px; height:160px; margin-top:0; }
      .container { padding:12px; margin-top:8px; }
    }
  </style>
</head>
<body>
  <header class="app-header">
    <div class="brand">
      <!-- cloud image kept and served from images/cloud.webp -->
      <div class="cloud-logo" aria-hidden="true">
        {% if cloud_image_url %}
          <img src="{{ cloud_image_url }}" alt="cloud logo">
        {% endif %}
      </div>

      <div class="title-wrap" role="banner">
        <div class="title">Cloud with Sai</div>

        <div style="position:relative; display:inline-block;">
          <div id="titleSub" class="title-sub" data-text=" An AI-Driven Cloud and DevOps Learning Platform "></div>
          <div class="subtitle-particles" aria-hidden="true">
            <span class="p1"></span>
            <span class="p2"></span>
            <span class="p3"></span>
            <span class="p4"></span>
          </div>
        </div>
      </div>
    </div>

    <nav class="modules" role="navigation" aria-label="primary modules">
      <a class="module {% if active=='profile' %}active{% endif %}" href="{{ url_for('profile') }}"><div class="icon">👨‍🏫</div><div class="label">Profile</div></a>
      <a class="module {% if active=='courses' %}active{% endif %}" href="{{ url_for('courses') }}"><div class="icon">📚</div><div class="label">Courses</div></a>
      <a class="module {% if active=='projects' %}active{% endif %}" href="{{ url_for('projects') }}"><div class="icon">💼</div><div class="label">Projects</div></a>
      <a class="module {% if active=='skill-analyzer' %}active{% endif %}" href="{{ url_for('skill_analyzer') }}"><div class="icon">📊</div><div class="label">Skill Analyzer</div></a>
      <a class="module {% if active=='contact' %}active{% endif %}" href="{{ url_for('contact') }}"><div class="icon">📱</div><div class="label">Contact</div></a>
    </nav>
  </header>

  <div class="container">
    <main class="card" role="main">
      {% with messages = get_flashed_messages() %}
        {% if messages %}
          <div style="padding:12px;border-radius:8px;background:#f0fdf4;margin-bottom:12px;color:#065f46;">
            {% for m in messages %}{{ m }}{% endfor %}
          </div>
        {% endif %}
      {% endwith %}

      {{ content|safe }}
    </main>
  </div>

  <script>
    // Continuous looping typewriter-like reveal for subtitle
    (function(){
      const target = document.getElementById('titleSub');
      if(!target) return;
      const full = target.getAttribute('data-text') || '';
      const totalDuration = 1100; // ms per full print cycle
      const len = Math.max(1, full.length);
      const perChar = Math.max(6, Math.floor(totalDuration / len)); // ms per char

      function buildSpans() {
        target.innerHTML = '';
        for(let i=0;i<full.length;i++){
          const ch = full[i];
          const span = document.createElement('span');
          span.className = 'ch';
          span.innerHTML = ch === ' ' ? '&nbsp;' : ch.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
          target.appendChild(span);
        }
      }

      function revealOnce(callback) {
        const chars = Array.from(target.querySelectorAll('.ch'));
        let idx = 0;
        const step = () => {
          if(idx >= chars.length) {
            if(callback) callback();
            return;
          }
          chars[idx].classList.add('show');
          idx++;
          setTimeout(step, perChar);
        };
        step();
      }

      function hideAll(done) {
        const chars = Array.from(target.querySelectorAll('.ch'));
        let completed = 0;
        if(chars.length === 0) { if(done) done(); return; }
        chars.forEach((c, i) => {
          setTimeout(()=> {
            c.classList.remove('show');
            completed++;
            if(completed === chars.length && done) done();
          }, Math.floor(i * 8));
        });
      }

      function loop() {
        buildSpans();
        target.style.filter = 'none';
        revealOnce(()=>{
          const pauseAfter = 600;
          setTimeout(()=>{
            hideAll(()=> {
              const pauseBeforeRestart = 220;
              setTimeout(loop, pauseBeforeRestart);
            });
          }, pauseAfter);
        });
      }

      setTimeout(loop, 240);
    })();
  </script>

  <!-- ANIMATED MASCOT WIDGET (Global) -->
  <div id="mascot-widget">
      <div class="mascot-message-box">
          <span id="mascot-text">Courses available in: English, Telugu, & Hindi</span>
      </div>
      <img src="/images/mascot_tutor.png?v=3" alt="3D Tutor" class="mascot-img">
  </div>

  <style>
    #mascot-widget {
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 9999; /* High z-index to stay on top */
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      pointer-events: none;
      font-family: 'Inter', sans-serif; /* Match site font */
    }
    
    .mascot-img {
      width: 140px; /* Slightly smaller for global non-intrusive feel */
      height: auto;
      filter: drop-shadow(0 10px 10px rgba(0,0,0,0.2));
      animation: mascot-bounce 3s ease-in-out infinite;
      transform-origin: bottom center;
      pointer-events: auto;
      transition: transform 0.3s ease;
    }
    
    .mascot-img:hover {
        transform: scale(1.05) rotate(-2deg);
    }
    
    @keyframes mascot-bounce {
      0%, 100% { transform: translateY(0) rotate(0deg); }
      50% { transform: translateY(-8px) rotate(1deg); }
    }
    
    .mascot-message-box {
      background: #fff;
      padding: 12px 18px;
      border-radius: 18px 18px 0 18px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.15);
      margin-bottom: 8px;
      max-width: 240px;
      text-align: right;
      border: 2px solid #38bdf8;
      font-weight: 600;
      color: #0f172a;
      font-size: 0.9rem;
      opacity: 0;
      transform: translateY(10px);
      animation: bubble-pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
      pointer-events: auto;
      margin-right: 15px;
    }
    
    .mascot-message-box::after {
      content: '';
      position: absolute;
      bottom: -10px;
      right: 20px;
      width: 0;
      height: 0;
      border-left: 10px solid transparent;
      border-right: 0px solid transparent;
      border-top: 10px solid #38bdf8;
    }
    .mascot-message-box::before {
      content: '';
      position: absolute;
      bottom: -7px;
      right: 22px;
      width: 0;
      height: 0;
      border-left: 8px solid transparent;
      border-right: 0px solid transparent;
      border-top: 8px solid #fff;
      z-index: 1;
    }

    @keyframes bubble-pop {
      to { opacity: 1; transform: translateY(0); }
    }
  </style>

  <script>
  (function() {
      const messages = [
          "Courses available in: 🇬🇧 English, 🇮🇳 Telugu, & 🇮🇳 Hindi",
          "Includes Resume & Interview Prep!",
          "Real-time & AI-driven Projects!",
          "For details contact: 📞 9666-562012"
      ];
      
      let msgIndex = 0;
      const msgEl = document.getElementById('mascot-text');
      const bubbleEl = document.querySelector('.mascot-message-box');
      
      if(msgEl && bubbleEl) {
          setInterval(() => {
              msgIndex = (msgIndex + 1) % messages.length;
              // Fade out
              bubbleEl.style.opacity = '0';
              bubbleEl.style.transform = 'translateY(5px)';
              
              setTimeout(() => {
                  msgEl.innerHTML = messages[msgIndex];
                  // Pop in
                  bubbleEl.style.opacity = '1';
                  bubbleEl.style.transform = 'translateY(0)';
              }, 400); 
              
          }, 4000); 
      }
  })();
  </script>
</body>
</html>
"""

def render_page(content_html, **extra):
    cloud_url = None
    me_url = None
    cloud_candidate = os.path.join(IMAGES_DIR, CLOUD_FILENAME)
    me_candidate = os.path.join(IMAGES_DIR, ME_FILENAME)
    if os.path.exists(cloud_candidate) and os.path.isfile(cloud_candidate):
        cloud_url = url_for('image_file', filename=CLOUD_FILENAME)
    if os.path.exists(me_candidate) and os.path.isfile(me_candidate):
        me_url = url_for('image_file', filename=ME_FILENAME)

    ctx = {
        "cloud_image_url": cloud_url,
        "me_image_url": me_url,
        "year": datetime.now(timezone.utc).year,
        **extra,
    }
    rendered_content = render_template_string(content_html, **ctx)
    return render_template_string(BASE_HTML, content=rendered_content, **ctx)

# ---- Wire the courses module here (one-line import + call) ----
# This attaches /courses and /course/<slug> without modifying other app routes.
from courses_module import register_routes
register_routes(app, render_page, IMAGES_DIR, CLOUD_FILENAME)

# Make / (root) show the profile page directly
# Profile Module
import profile_page
profile_page.register_routes(app, render_page)

@app.route("/projects")
def projects():
    # Import locally to use the new projects module
    import projects as projects_module
    
    project_images = list_images("projects")
    html = projects_module.render(project_images)
    return render_page(html, active="projects")

# Skill Analyzer Module
import skill_analyzer_page
skill_analyzer_page.register_routes(app, render_page)

# Contact Module
import contact_page
contact_page.register_routes(app, render_page, BASE_DIR, {
    "password": "mpvbvlovezpjlgmq",
    "to_email": "multiclouddevops4u@gmail.com",
    "admin_email": "multiclouddevops4u@gmail.com"
})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

