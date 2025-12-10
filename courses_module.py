# courses_module.py
import os
import importlib
from flask import url_for
from markupsafe import Markup

# Literal path to the uploaded image file (left as a file path string per your request).
# Your environment/tooling will transform this to a served URL if needed.
UPLOADED_CLOUD_FALLBACK = "/mnt/data/51BC2F46-B035-4EC2-8054-C3A2697D6723.jpeg"

def register_routes(app, render_page_func, images_dir, cloud_filename):
    """
    Registers /courses and /course/<slug> routes on the provided Flask `app`.
    Keeps UI and behavior unchanged; only integrates dynamic delegation to
    separate per-course python files when available.
    """

    @app.route("/courses")
    def courses():
        course_items = [
            {"slug":"aws","title":"AWS Solution Architect","desc":"Foundations, hands-on labs, IAM, EC2, S3, VPC.","level":"Beginner","duration":"4 weeks","img":"AWS.png","type":"rect","scale":0.54},
            {"slug":"linux","title":"Linux Administration","desc":"System basics, shells, users, permissions, networking.","level":"Beginner","duration":"3 weeks","img":"linux.jpg","type":"rect","scale":0.95},
            {"slug":"devops","title":"Multi-Cloud DevOps","desc":"CI/CD, containers, automation, infra as code across clouds.","level":"Intermediate","duration":"4 weeks","img":"devops.png","type":"rect","scale":1.0},
            {"slug":"spoken-english","title":"Spoken English & Corporate Etiquette","desc":"Improve communication, interviews and workplace etiquette.","level":"All levels","duration":"6 weeks","img":"37527b78-62d1-49a2-adad-0ae6d46cf44a.png","type":"square"},
            {"slug":"sdlc","title":"SDLC & Release Management","desc":"Software development lifecycle, release pipelines, QA.","level":"Intermediate","duration":"2 weeks","img":"SDLC.jpg","type":"square"}
        ]

        html = """
        <h2>Courses & Workshops</h2>

        <style>
          .courses-top { display:flex; gap:14px; margin-top:14px; align-items:stretch; }

          /* course-card is explicitly positioned to host absolutely-positioned elements */
          .courses-top .course-card {
            position: relative;
            flex:1 1 0; min-width:220px; max-width:360px;
            display:flex; flex-direction:column;
            border-radius:12px; overflow:hidden;
            box-shadow:0 8px 28px rgba(2,6,23,0.04);
            border:1px solid rgba(10,20,30,0.04);
            background:#fff;
            transition: transform 220ms ease, box-shadow 220ms ease, background 220ms ease, color 220ms ease;
          }

          .courses-top .course-card:hover,
          .courses-bottom .course-card:hover {
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 20px 48px rgba(2,6,23,0.12);
            background: linear-gradient(90deg,#60A5FA,#3B82F6);
            color: #02203a;
          }

          .courses-bottom {
            display:flex; justify-content:center; gap:16px; margin-top:16px;
          }

          .courses-bottom .course-card {
            position: relative;
            width:224px;
            border-radius:12px; overflow:hidden;
            box-shadow:0 8px 28px rgba(2,6,23,0.04);
            border:1px solid rgba(10,20,30,0.04);
            background:#fff;
            transition: transform 220ms ease, box-shadow 220ms ease, background 220ms ease, color 220ms ease;
          }

          .hero-wrap {
            width:100%; height:170px; overflow:hidden; display:block; background:#fff;
            position: relative; /* ensure hero-wrap creates stacking context for image */
          }

          .hero-wrap.square {
            height:auto; padding-top:100%; position:relative;
          }

          /* make sure hero images sit at z-index:0 (below badge) */
          .course-hero {
            width:100%; height:100%; object-fit:cover;
            display:block; transform-origin:center center;
            transition: transform 220ms ease;
            position: relative;
            z-index: 0;
          }

          .course-hero.contain {
            object-fit:contain; width:100%; height:100%;
          }

          .course-body {
            padding:12px 14px; display:flex; flex-direction:column; gap:8px;
          }

          .course-title {
            font-weight:800; font-size:16px; margin:0 0 4px 0; color:inherit;
          }

          .course-desc { font-size:13px; margin:0; line-height:1.25; color:inherit; }

          .course-meta {
            display:flex; gap:8px; align-items:center; font-size:12px; color:inherit;
          }

          .badge {
            background:#f1f5f9; border-radius:6px; padding:4px 8px; font-size:11px; color:#0f172a;
          }

          .course-actions { margin-top:8px; display:flex; gap:8px; align-items:center; }

          .btn {
            background:linear-gradient(90deg,#60A5FA,#6EE7B7);
            color:#02203a; padding:8px 12px; border-radius:8px;
            text-decoration:none; font-weight:700; font-size:13px;
          }

          .link-secondary { font-size:13px; color:#374151; text-decoration:underline; }

          /* offer-badge must be on top of everything inside the card */
          .offer-badge {
            position:absolute;
            top:12px;
            right:12px;
            z-index:9999 !important; /* force above images */
            padding:6px 12px;
            font-weight:900;
            font-size:13px;
            color:#7c2d12;
            background:linear-gradient(90deg,#fff7ed,#fff3e0);
            border-radius:999px;
            box-shadow:0 8px 18px rgba(124,45,18,0.12);
            border:1px solid rgba(124,45,18,0.08);
            animation: offer-blink 1.8s ease-in-out infinite;
            pointer-events:none;
          }

          @keyframes offer-blink {
            0% { transform:scale(1); opacity:0.98; }
            50% { transform:scale(1.03); opacity:1; }
            100% { transform:scale(1); opacity:0.98; }
          }

          /* default square-image scale (Spoken English kept at 1.10; SDLC overridden in HTML) */
          .hero-wrap.square .course-hero {
            transform: scale(1.10);
            position:absolute; left:0; top:0;
            width:100%; height:100%;
            z-index:0;
          }

          @media (max-width:980px){
            .courses-top { flex-direction:column; }
            .courses-bottom { flex-direction:column; align-items:center; }
            .courses-bottom .course-card { width:92%; }
            .hero-wrap { height:140px; }
            .hero-wrap.square { padding-top:66%; }
          }
        </style>

        <div class="courses-top">
        """

        # Top row
        for c in course_items[:3]:
            img = c['img']
            candidate = os.path.join(images_dir, img)
            if os.path.exists(candidate):
                thumb = url_for('image_file', filename=img)
            else:
                # fallback: use cloud_filename if present in images_dir; otherwise use uploaded file path literal
                candidate_cloud = os.path.join(images_dir, cloud_filename)
                if os.path.exists(candidate_cloud):
                    thumb = url_for('image_file', filename=cloud_filename)
                else:
                    # literal local path as requested; your tooling will transform this to a served URL
                    thumb = UPLOADED_CLOUD_FALLBACK

            offer_html = ""
            if c['slug'] == "devops":
                # Offer badge injected inside the card; CSS ensures it's on top (high z-index)
                offer_html = "<div class='offer-badge'>Offer: Multi-Cloud DevOps – Rs 20,000</div>"

            html += f"""
            <a class='course-link' href='{url_for('course_detail', slug=c['slug'])}' style='text-decoration:none;color:inherit;'>
              <div class="course-card">
                {offer_html}
                <div class='hero-wrap'>
                  <img class='course-hero' src="{thumb}" alt="{c['title']}" style="transform: scale({c['scale']});">
                </div>
                <div class="course-body">
                  <div class="course-title">{c['title']}</div>
                  <div class="course-desc">{c['desc']}</div>
                  <div class="course-meta">
                    <span class="badge">{c['level']}</span>
                    <span>•</span>
                    <span>{c['duration']}</span>
                  </div>
                  <div class="course-actions">
                    <a class="btn" href="{url_for('contact')}">Enroll / Contact</a>
                  </div>
                </div>
              </div>
            </a>
            """

        html += "</div>\n\n<div class='courses-bottom'>\n"

        # Bottom row (Spoken English — unchanged, SDLC — scale adjusted)
        for c in course_items[3:]:
            img = c['img']
            candidate = os.path.join(images_dir, img)
            if os.path.exists(candidate):
                thumb = url_for('image_file', filename=img)
            else:
                candidate_cloud = os.path.join(images_dir, cloud_filename)
                if os.path.exists(candidate_cloud):
                    thumb = url_for('image_file', filename=cloud_filename)
                else:
                    thumb = UPLOADED_CLOUD_FALLBACK

            # Spoken English → keep scale 1.10  
            # SDLC → reduce scale to 1.00 (zoomed out)
            scale_override = "1.10"
            if c['slug'] == "sdlc":
                scale_override = "1.00"

            html += f"""
            <a class='course-link' href='{url_for('course_detail', slug=c['slug'])}' style='text-decoration:none;color:inherit;'>
              <div class="course-card">
                <div class='hero-wrap square'>
                  <img class='course-hero contain' src="{thumb}" alt="{c['title']}" style="transform: scale({scale_override});">
                </div>
                <div class="course-body">
                  <div class="course-title">{c['title']}</div>
                  <div class="course-desc">{c['desc']}</div>
                  <div class="course-meta">
                    <span class="badge">{c['level']}</span>
                    <span>•</span>
                    <span>{c['duration']}</span>
                  </div>
                  <div class="course-actions">
                    <a class="btn" href="{url_for('contact')}">Enroll / Contact</a>
                  </div>
                </div>
              </div>
            </a>
            """

        return render_page_func(Markup(html), active="courses")


    @app.route("/course/<slug>")
    def course_detail(slug):
        mapping = {
            'aws': { 'title': 'AWS Solution Architect', 'img': 'AWS.png', 'module': 'courses_aws' },
            'devops': { 'title': 'Multi-Cloud DevOps', 'img': 'devops.png', 'module': 'courses_devops' },
            'linux': { 'title': 'Linux Administration', 'img': 'linux.jpg', 'module': 'courses_linux' },
            'sdlc': { 'title': 'SDLC & Release Management', 'img': 'SDLC.jpg', 'module': 'courses_sdlc' },
            'spoken-english': { 'title': 'Spoken English & Corporate Etiquette', 'img': '37527b78-62d1-49a2-adad-0ae6d46cf44a.png', 'module': 'courses_english' }
        }

        info = mapping.get(slug)
        if not info:
            return render_page_func("<h2>Course not found</h2><p>No such course.</p>", active="courses")

        # Attempt to delegate to an external module's render() function if present.
        module_name = info.get('module')
        if module_name:
            try:
                course_mod = importlib.import_module(module_name)
                if hasattr(course_mod, "render") and callable(getattr(course_mod, "render")):
                    try:
                        # call the module's render() and if it returns HTML, use it
                        mod_html = course_mod.render()
                        if isinstance(mod_html, str):
                            return render_page_func(Markup(mod_html), active="courses")
                    except Exception:
                        # If module's render() raises, we silently fall back to default detail page below
                        pass
            except Exception:
                # import failed — fall back to default detail page
                pass

        # existing default detail_html (unchanged UI)
        img = info['img']
        candidate = os.path.join(images_dir, img)
        if os.path.exists(candidate):
            img_url = url_for('image_file', filename=img)
        else:
            candidate_cloud = os.path.join(images_dir, cloud_filename)
            if os.path.exists(candidate_cloud):
                img_url = url_for('image_file', filename=cloud_filename)
            else:
                img_url = UPLOADED_CLOUD_FALLBACK

        detail_html = f"""
        <div style='display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start;'>
          <div style='flex:0 0 420px; max-width:100%;'>
            <img src='{img_url}' alt='{info['title']}' style='width:100%;height:340px;object-fit:cover;border-radius:12px;box-shadow:0 12px 36px rgba(2,6,23,0.06);'>
          </div>
          <div style='flex:1;min-width:260px;'>
            <h2 style='margin-top:0'>{info['title']}</h2>
            <p style='color:#6b7280;font-weight:700;'>This is a placeholder. More details coming soon.</p>
            <div style='margin-top:12px;'>
              <a class='btn' href='{url_for('contact')}'>Enroll / Contact</a>
            </div>
          </div>
        </div>
        """


    @app.route("/course/aws/<service_id>")
    def aws_service_detail(service_id):
        """
        Specific route for AWS sub-modules (Compute, Storage, etc.)
        Delegates to courses_aws.render_service(service_id).
        """
        try:
            import courses_aws
            if hasattr(courses_aws, "render_service"):
                html = courses_aws.render_service(service_id)
                return render_page_func(Markup(html), active="courses")
        except Exception as e:
            pass # Fallthrough or error handling

        return render_page_func(f"<h2>Service not found</h2><p>Could not load service detail for {service_id}</p>", active="courses")

