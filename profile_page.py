# profile_page.py
from flask import url_for

def register_routes(app, render_page_func):
    @app.route("/")
    @app.route("/profile")
    def profile():
        # Note: me_image_url is injected by render_page_func in app.py when rendering this string
        profile_html = """
          <style>
            @keyframes fadeUp { from { opacity:0; transform:translateY(15px); } to { opacity:1; transform:translateY(0); } }
            
            .profile-container {
              display: grid;
              grid-template-columns: 280px 1fr;
              gap: 32px;
              animation: fadeUp 0.6s ease-out;
            }

            /* Left Sidebar: Photo + Contact */
            .profile-sidebar {
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 20px;
            }

            .avatar-frame {
              width: 240px;
              height: 240px;
              border-radius: 50%;
              padding: 6px;
              background: linear-gradient(135deg, #60A5FA, #34D399);
              box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            }
            .avatar-content {
              width: 100%;
              height: 100%;
              border-radius: 50%;
              overflow: hidden;
              background: #fff;
              display: flex;
              align-items: center;
              justify-content: center;
              border: 4px solid #fff;
              position: relative;
            }
            .avatar-content img {
              width: 100%;
              height: 100%;
              object-fit: cover;
              object-position: top center;
            }
            
            .contact-box {
              width: 100%;
              background: #F8FAFC;
              border-radius: 16px;
              padding: 20px;
              border: 1px solid #E2E8F0;
            }
            .contact-link {
              display: flex;
              align-items: center;
              gap: 12px;
              color: #475569;
              text-decoration: none;
              font-size: 14px;
              font-weight: 600;
              margin-bottom: 12px;
              transition: transform 0.2s, color 0.2s;
            }
            .contact-link:last-child { margin-bottom: 0; }
            .contact-link:hover { transform: translateX(4px); color: #0EA5E9; }
            .contact-link svg { width: 18px; height: 18px; fill: currentColor; }

            /* Right Content: Bio, Stats, Certs */
            .profile-main {
              display: flex;
              flex-direction: column;
              gap: 24px;
            }

            .bio-card {
              background: #fff;
              border-radius: 20px;
              padding: 28px;
              box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
              border: 1px solid #F1F5F9;
            }
            .bio-header {
              font-size: 24px;
              font-weight: 800;
              color: #0F172A;
              margin-bottom: 12px;
              background: linear-gradient(90deg, #0F172A, #334155);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
            }
            .bio-text {
              font-size: 16px;
              line-height: 1.7;
              color: #475569;
            }

            /* Certifications */
            .section-title {
              font-size: 18px;
              font-weight: 700;
              color: #1E293B;
              margin-bottom: 16px;
              display: flex;
              align-items: center;
              gap: 8px;
            }
            .cert-grid {
              display: grid;
              grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
              gap: 16px;
            }
            .cert-card {
              background: #fff;
              border: 1px solid #E2E8F0;
              border-radius: 16px;
              padding: 20px;
              display: flex;
              flex-direction: column;
              align-items: center;
              text-align: center;
              gap: 12px;
              transition: transform 0.2s, box-shadow 0.2s;
            }
            .cert-card:hover {
              transform: translateY(-4px);
              box-shadow: 0 12px 24px -8px rgba(0,0,0,0.1);
              border-color: #CBD5E1;
            }
            .cert-img {
              width: 100px;
              height: 100px;
              object-fit: contain;
            }
            .cert-name {
              font-size: 14px;
              font-weight: 700;
              color: #334155;
              line-height: 1.4;
            }

            /* Info Grid for Teaching/Academic */
            .info-grid {
              display: grid;
              grid-template-columns: 1fr 1fr;
              gap: 20px;
            }
            .info-card {
              background: #F8FAFC;
              border-radius: 16px;
              padding: 24px;
              border: 1px solid #E2E8F0;
            }
            .info-label {
              text-transform: uppercase;
              font-size: 11px;
              font-weight: 800;
              letter-spacing: 0.05em;
              color: #94A3B8;
              margin-bottom: 8px;
            }
            .info-content {
              font-size: 15px;
              font-weight: 600;
              color: #334155;
              line-height: 1.6;
            }
            
            @media (max-width: 800px) {
              .profile-container { grid-template-columns: 1fr; }
              .profile-sidebar { flex-direction: row; flex-wrap: wrap; justify-content: center; }
              .contact-box { width: auto; flex: 1; min-width: 260px; }
              .info-grid { grid-template-columns: 1fr; }
            }
          </style>

          <div class="profile-container">
            
            <!-- Sidebar -->
            <div class="profile-sidebar">
              <div class="avatar-frame">
                <div class="avatar-content">
                  {% if me_image_url %}
                    <img src="{{ me_image_url }}" alt="Sai Profile Photo">
                  {% else %}
                    <div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:#f1f5f9;color:#cbd5e1;font-weight:800;font-size:48px;">SAI</div>
                  {% endif %}
                </div>
              </div>

              <div class="contact-box">
                <a href="mailto:multiclouddevops4u@gmail.com" class="contact-link">
                  <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><path d="m22 6-10 7L2 6"></path></svg>
                  <span>multiclouddevops4u@gmail.com</span>
                </a>
                <a href="tel:+919666562012" class="contact-link">
                  <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                  <span>+91 96665 62012</span>
                </a>
              </div>
            </div>

            <!-- Main Content -->
            <div class="profile-main">
              
              <!-- Bio -->
              <div class="bio-card">
                <div class="bio-header">Hello, I am Sai.</div>
                <div class="bio-text">
                  A cloud enthusiast and instructor committed to hands-on learning with real-time labs and projects. I bring <strong>10+ years of IT experience</strong>, with 5 years specializing in <strong>Cloud & DevOps</strong>. I also provide freelance services to help businesses scale and optimize their infrastructure.
                </div>
              </div>

              <!-- Certifications -->
              <div>
                <div class="section-title">
                  <span style="background:#E0F2FE;color:#0284C7;padding:4px 8px;border-radius:6px;font-size:12px;">VALIDATED</span>
                  Certifications
                </div>
                <div class="cert-grid">
                  <!-- AWS Badge -->
                  <div class="cert-card">
                    <img class="cert-img" src="https://images.credly.com/size/340x340/images/0e284c3f-5164-4b21-8660-0d84737941bc/image.png" alt="AWS Solutions Architect Associate">
                    <div class="cert-name">AWS Certified<br>Solutions Architect Associate</div>
                  </div>
                  <!-- GCP Badge -->
                  <div class="cert-card">
                    <img class="cert-img" src="{{ url_for('image_file', filename='gcp_cloud_engineer.png') }}" alt="GCP Associate Cloud Engineer">
                    <div class="cert-name">Google Cloud<br>Associate Cloud Engineer</div>
                  </div>
                </div>
              </div>

              <!-- Info Grid -->
              <div class="info-grid">
                <div class="info-card">
                  <div class="info-label">Teaching Areas</div>
                  <div class="info-content">
                    AWS · Linux · DevOps<br>
                    MLOps · Multi-cloud (GCP)<br>
                    Infrastructure as Code
                  </div>
                </div>
                <div class="info-card">
                  <div class="info-label">Academic & Mentorship</div>
                  <div class="info-content">
                    Master's Thesis: <em>Resource Allocation in Cloud Computing</em><br><br>
                    <strong>4 Batches</strong> completed with hands-on live labs.
                  </div>
                </div>
              </div>

            </div>
          </div>
        """
        return render_page_func(profile_html, active="profile")
