# profile_page.py
from flask import url_for

def register_routes(app, render_page_func):
    @app.route("/")
    @app.route("/profile")
    def profile():
        # Note: me_image_url is injected by render_page_func in app.py when rendering this string
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
        return render_page_func(profile_html, active="profile")
