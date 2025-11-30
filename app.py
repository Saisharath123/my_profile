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

# ---------- Email helper (uses EMAIL_PASSWORD variable) ----------
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
ADMIN_EMAIL = EMAIL_ADDRESS

def send_contact_email(name: str, sender_email: str, message_body: str) -> None:
    """
    Send message to TO_EMAIL using Gmail SMTP.
    Requires EMAIL_PASSWORD to be set (replace the placeholder locally).
    Raises RuntimeError on missing password or smtplib.SMTPException on send failure.
    """
    password = EMAIL_PASSWORD
    if not password or password == "<PUT_PASSWORD_HERE>":
        raise RuntimeError("EMAIL_PASSWORD not configured in app (replace placeholder)")

    msg = EmailMessage()
    # Use the sender's name and email in From header so you can reply
    msg["From"] = f"{name} <{sender_email}>"
    msg["To"] = TO_EMAIL
    msg["Subject"] = f"Website contact: message from {name}"
    body = f"You have received a new message from the website contact form.\n\nName: {name}\nEmail: {sender_email}\n\nMessage:\n{message_body}\n\n--\nSent by Cloud with Sai website"
    msg.set_content(body)

    # Connect and send using STARTTLS
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(ADMIN_EMAIL, password)
        smtp.send_message(msg)

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
@app.route("/")
def root():
    return profile()

@app.route("/profile")
def profile():
    profile_html = """
      <div class="profile">
        <div class="avatar">
          {% if me_image_url %}
            <img src="{{ me_image_url }}" alt="photo">
          {% else %}
            <svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
              <rect width="100%" height="100%" rx="110" ry="110" fill="#ffffff"/>
              <text x="50%" y="50%" fill="#0b1620" font-size="28" text-anchor="middle" dominant-baseline="middle">Profile</text>
            </svg>
          {% endif %}
        </div>

        <div class="profile-text">
          <div class="intro">
            I am Sai — a cloud enthusiast and instructor committed to hands-on learning with real-time labs and projects. I bring 10+ years of IT experience, with 5 years specializing in cloud and DevOps, and I also provide freelance services.
          </div>

          <div style="margin-top:12px;">
            <h3 style="margin-top:12px">Certifications</h3>
            <ul style="color:#374151;font-weight:700;">
              <li>AWS Solution Architect – Associate</li>
              <li>Google Cloud: Associate Cloud Engineer</li>
            </ul>

            <h3 style="margin-top:12px">Teaching Areas</h3>
            <p style="color:#374151;font-weight:700;">
              AWS · Linux · DevOps · MLOps · Multi-cloud DevOps (incl. GCP)
            </p>

            <h3 style="margin-top:12px">Academic Work & Batches</h3>
            <p style="color:#374151;font-weight:700;">
              Completed Master's thesis on <em>resource allocation in cloud computing</em>. I have completed <strong>4 batches</strong> so far with hands-on demos and practical labs.
            </p>

            <div class="contact-row">
              <div class="contact-item">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M3 6.5A2.5 2.5 0 0 1 5.5 4h13A2.5 2.5 0 0 1 21 6.5v11A2.5 2.5 0 0 1 18.5 20h-13A2.5 2.5 0 0 1 3 17.5v-11zM5.5 6L12 10.2 18.5 6" fill="#0b1620" /></svg>
                <a href="mailto:multiclouddevops4u@gmail.com">multiclouddevops4u@gmail.com</a>
              </div>

              <div class="contact-item">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M6.6 10.2a15.05 15.05 0 0 0 7.2 7.2l1.9-1.9a1 1 0 0 1 1.0-.2c1.1.4 2.4.7 3.7.7a1 1 0 0 1 1 1v3.0a1 1 0 0 1-1 1C10.7 21 3 13.3 3 3.5A1 1 0 0 1 4 2.5h3.0a1 1 0 0 1 1 1c0 1.3.3 2.6.7 3.7a1 1 0 0 1-.2 1.0l-1.9 1.9z" fill="#0b1620"/></svg>
                <a href="tel:+919666562012">+91 96665 62012</a>
              </div>
            </div>

          </div>
        </div>
      </div>
    """
    return render_page(profile_html, active="profile")

@app.route("/projects")
def projects():
    project_images = list_images("projects")
    html = "<h2>Projects</h2><p style='color:var(--muted-gray)'>A few highlights and demo screenshots.</p>"
    if project_images:
        html += "<div class='grid' style='margin-top:12px;'>"
        for p in project_images:
          img_url = url_for("image_file", filename=f"projects/{p}")
          html += f"<div class='project-card card'><img src='{img_url}' alt='{p}' style='width:100%;height:160px;object-fit:cover;border-radius:8px;display:block;'><div style='padding:8px;'><strong style='color:#0b1620'>{p}</strong><div style='color:var(--muted-gray);font-size:13px;margin-top:6px'>Short description or tech tags here</div></div></div>"
        html += "</div>"
    else:
        html += "<div style='margin-top:12px;color:var(--muted-gray)'>No project images found in <code>images/projects/</code>. Drop screenshots there and refresh.</div>"
    return render_page(html, active="projects")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        mobile = request.form.get("mobile", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not mobile or not message:
            flash("Please fill all fields before submitting.")
            return redirect(url_for("contact"))

        safe_line = f"---\nName: {name}\nEmail: {email}\nMobile: {mobile}\nMessage: {message}\n"
        try:
            with open(os.path.join(BASE_DIR, "contacts.txt"), "a", encoding="utf-8") as fh:
                fh.write(safe_line)
        except Exception:
            flash("Failed to save message (server error).")
            return redirect(url_for("contact"))

        try:
            full_message = f"{message}\n\nMobile: {mobile}"
            send_contact_email(name, email, full_message)
            flash("Thanks — message received and emailed. I'll get back to you.")
        except RuntimeError:
            flash("Thanks — message received. Email sending is not configured on this server.")
        except Exception:
            flash("Thanks — message received. Email could not be sent due to a server error.")

        return redirect(url_for("contact"))

    form_html = """
      <style>
        .contact-wrap { display:flex; gap:18px; flex-wrap:wrap; }

        .contact-panel {
          flex:1; min-width:300px;
          border-radius:14px; padding:18px;
          background:linear-gradient(180deg,#ffffff,#fbfdff);
          box-shadow:0 20px 50px rgba(2,6,23,0.06);
          border:1px solid rgba(10,20,30,0.04);
        }

        h2.contact-title { margin:0 0 6px 0; font-size:22px; color:#02203a; }
        p.contact-sub { margin:0 0 14px 0; color:var(--muted-gray); font-weight:700; }

        .form-row { display:flex; gap:10px; margin-bottom:10px; }
        .form-row .field { flex:1; }

        .field input, .field textarea {
          padding:12px 14px;
          border-radius:10px;
          border:1px solid rgba(10,20,30,0.06);
          background:#fff;
          font-weight:700;
          font-size:15px;
        }

        /* Message box — width 50%, height normal */
        .message-wrap { display:flex; gap:12px; }
        .message-container { width:50%; min-width:240px; }
        .message-container textarea {
          width:100%;
          min-height:220px;
          resize:vertical;
        }

        .send-row { margin-top:8px; }
        .btn-send {
          background:linear-gradient(90deg,#60A5FA,#6EE7B7);
          border:none; padding:10px 16px;
          border-radius:10px; color:#02203a;
          font-weight:800; cursor:pointer;
        }

        /* RIGHT SIDE PANEL */
        .contact-side {
          width:320px; min-width:240px;
          border-radius:14px; padding:16px;
          background:linear-gradient(180deg,#f8fbff,#fff);
          box-shadow:0 16px 44px rgba(2,6,23,0.04);
          border:1px solid rgba(10,20,30,0.04);
        }

        .side-cards { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:12px; }
        .side-cards .card {
          background:#fff; padding:10px; border-radius:10px;
          box-shadow:0 8px 20px rgba(10,20,30,0.03);
          text-align:center; font-weight:700;
        }

        /* Contact info moved to RIGHT & kept INLINE */
        .right-contact-info {
          margin-top:18px; padding-top:10px;
          border-top:1px solid rgba(10,20,30,0.06);
        }
        .email-row, .phone-row {
          display:flex;
          align-items:center;
          gap:8px;
          white-space:nowrap;
        }
        .email-row span.email-text { font-size:15px; font-weight:900; color:#02203a; }
        .phone-row span.phone-text { font-size:17px; font-weight:900; color:#02203a; }

        @media (max-width:900px){
          .contact-wrap { flex-direction:column; }
          .contact-side { width:100%; }
          .message-container { width:100%; }
        }
      </style>

      <div class="contact-wrap">

        <!-- LEFT FORM PANEL -->
        <div class="contact-panel">
          <h2 class="contact-title">Contact</h2>
          <p class="contact-sub">Send a quick message — for course enquiries, demos, or project collaboration.</p>

          <form method="post" action="{{ action_url }}" novalidate>

            <div class="form-row">
              <div class="field"><input name="name" type="text" placeholder="Your name" required></div>
              <div class="field"><input name="email" type="email" placeholder="Your email" required></div>
            </div>

            <div class="form-row">
              <div class="field"><input name="mobile" type="tel" placeholder="Your mobile number" required></div>
            </div>

            <div class="message-wrap">
              <div class="message-container">
                <div class="field">
                  <textarea name="message" rows="8" placeholder="Your message" required></textarea>
                </div>

                <div class="send-row">
                  <button class="btn-send" type="submit">Send Message</button>
                </div>
              </div>
              <div style="flex:1"></div>
            </div>

          </form>
        </div>

        <!-- RIGHT INFO PANEL -->
        <div class="contact-side">
          <h3 style="margin:0 0 6px 0;color:#02203a;">Why reach out?</h3>
          <p style="margin:0 0 12px 0;color:var(--muted-gray);font-weight:700;">
            For demos, course details, or project collaboration — I reply as soon as possible.
          </p>

          <div class="side-cards">
            <div class="card">Live Labs</div>
            <div class="card">Project Demos</div>
            <div class="card">Mentorship</div>
            <div class="card">Cert Prep</div>
          </div>

          <!-- CONTACT INFO (INLINE EMOJIS) -->
          <div class="right-contact-info">
            <div class="email-row">
              <span style="font-size:20px;">📧</span>
              <span class="email-text">multiclouddevops4u@gmail.com</span>
            </div>

            <div class="phone-row" style="margin-top:6px;">
              <span style="font-size:20px;">📞</span>
              <span class="phone-text">+91 96665 62012</span>
            </div>
          </div>

        </div>

      </div>
    """

    return render_page(form_html, active="contact", action_url=url_for('contact'))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

