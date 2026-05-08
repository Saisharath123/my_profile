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
              margin-bottom: 12px;
              display: flex;
              align-items: center;
              gap: 8px;
            }
            .cert-grid {
              display: grid;
              grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
              gap: 12px;
            }
            .cert-card {
              background: #fff;
              border: 1px solid #E2E8F0;
              border-radius: 12px;
              padding: 12px;
              display: flex;
              flex-direction: column;
              align-items: center;
              text-align: center;
              gap: 8px;
              transition: transform 0.2s, box-shadow 0.2s;
            }
            .cert-card:hover {
              transform: translateY(-4px);
              box-shadow: 0 8px 20px -6px rgba(0,0,0,0.1);
              border-color: #CBD5E1;
            }
            .cert-img {
              width: 50px;
              height: 50px;
              object-fit: contain;
            }
            .cert-name {
              font-size: 11px;
              font-weight: 700;
              color: #334155;
              line-height: 1.3;
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
            
            .graphical-label {
              font-size: 22px; 
              font-weight: 900;
              text-transform: uppercase;
              letter-spacing: -0.5px;
              margin-bottom: 16px;
              background: linear-gradient(135deg, #0F172A 0%, #3b82f6 100%);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
              position: relative;
              display: inline-block;
              padding-bottom: 6px;
            }
            .graphical-label::after {
              content: '';
              position: absolute;
              bottom: 0;
              left: 0;
              width: 40px;
              height: 4px;
              background: linear-gradient(90deg, #3b82f6, #06b6d4);
              border-radius: 4px;
            }
            .info-content {
              font-size: 15px;
              font-weight: 600;
              color: #334155;
              line-height: 1.6;
            }
            

            .tech-grid {
              display: grid;
              grid-template-columns: repeat(3, 1fr);
              gap: 12px;
              margin-top: 10px;
            }
            .tech-item {
              display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: flex-start;
              padding: 0;
              background: #f1f5f9;
              border-radius: 12px;
              overflow: hidden;
              font-size: 11px;
              font-weight: 700;
              color: #334155;
              transition: transform 0.2s, background 0.2s;
              text-align: center;
              height: 100%;
            }
            .tech-item:hover { transform: translateY(-3px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
            .tech-item img { 
              width: 100%; 
              height: 85px; 
              object-fit: cover; 
              display: block;
            }
            .tech-item span {
              width: 100%;
              padding: 8px 4px;
              background: #f1f5f9;
              display: flex;
              align-items: center;
              justify-content: center;
              flex-grow: 1;
            }
            .tech-item:hover span { background: #e2e8f0; }

            .lang-row {
              display: flex;
              gap: 16px;
              margin-top: 12px;
              align-items: center;
              flex-wrap: wrap;
            }
            .lang-item {
              display: flex;
              align-items: center;
              gap: 8px;
              font-size: 13px;
              font-weight: 600;
              color: #475569;
              background: #fff;
              padding: 6px 10px;
              border-radius: 20px;
              border: 1px solid #e2e8f0;
            }
            .flag-icon { 
              width: 20px; 
              height: 15px; 
              border-radius: 2px; 
              object-fit: cover; 
              box-shadow: 0 1px 2px rgba(0,0,0,0.1); 
              display: block;
            }
            
            .academic-row {
              display: flex;
              align-items: flex-start;
              gap: 16px;
              margin-bottom: 20px;
              padding: 12px;
              border-radius: 12px;
              background: #fff;
              border: 1px solid #f1f5f9;
              transition: transform 0.2s, box-shadow 0.2s;
            }
            .academic-row:last-child { margin-bottom: 0; }
            .academic-row:hover {
              transform: translateX(6px);
              box-shadow: 0 4px 12px rgba(0,0,0,0.05);
              border-color: #e2e8f0;
            }
            .academic-icon {
              width: 48px;
              height: 48px;
              object-fit: contain;
              flex-shrink: 0;
            }
            .academic-text {
              font-size: 14px;
              color: #475569;
              line-height: 1.5;
            }
            .academic-text strong { color: #0f172a; font-weight: 700; }
            
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
                <a href="{{ url_for('contact') }}" class="contact-link">
                  <img src="{{ url_for('image_file', filename='gmail.png') }}" alt="Gmail" style="width:20px;height:20px;object-fit:contain;">
                  <span>multiclouddevops4u@gmail.com</span>
                </a>
                <a href="{{ url_for('contact') }}" class="contact-link">
                  <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                  <span>+91 96665 62012</span>
                </a>
                <a href="https://www.linkedin.com/in/sai-s-n" target="_blank" class="contact-link">
                  <img src="{{ url_for('image_file', filename='linkedin.png') }}" alt="LinkedIn" style="width:20px;height:20px;object-fit:contain;">
                  <span>www.linkedin.com/in/sai-s-n</span>
                </a>
                <a href="https://github.com/Saisharath123" target="_blank" class="contact-link">
                  <img src="/images/devops_images/Git Hub.png" alt="GitHub" style="width:20px;height:20px;object-fit:contain;">
                  <span>github.com/Saisharath123</span>
                </a>
                <a href="https://hub.docker.com/u/saisarath14" target="_blank" class="contact-link">
                  <img src="/images/devops_images/docker.png" alt="DockerHub" style="width:20px;height:20px;object-fit:contain;">
                  <span>Docker Hub: saisarath14</span>
                </a>
                <a href="https://www.urbanpro.com/hyderabad/sai-n-aws-devops-trainer-with-10-years-of-it-experience-and-5-years-in-real-time-cloud-projects" target="_blank" class="contact-link">
                  <img src="{{ url_for('image_file', filename='urbanpro_logo.jpg') }}" alt="UrbanPro" style="width:20px;height:20px;object-fit:contain;">
                  <span>UrbanPro Profile</span>
                </a>
              </div>
            </div>

            <!-- Main Content -->
            <div class="profile-main">
              
              <!-- Bio -->
              <div class="bio-card">
                <div class="bio-header">Hello, I am Sai.</div>
                <div class="bio-text">
                  A cloud enthusiast and instructor committed to hands-on learning through real-time labs and industry-grade projects. I bring <strong>10+ years of IT experience</strong>, with over 5 years specializing in <strong>Cloud and DevOps technologies</strong>. I completed my Master’s thesis on resource allocation in cloud computing, gaining strong expertise in optimization, scalability, and performance-driven architectures. Additionally, I provide freelance consulting services to help businesses scale, optimize, and modernize their cloud infrastructure.
                </div>
              </div>

              <!-- Info Grid -->
              <div class="info-grid">
                <div class="info-card">
                  <div class="graphical-label">Teaching Areas</div>
                  <div class="tech-grid">
                    <a href="{{ url_for('course_detail', slug='aws') }}" class="tech-item" style="text-decoration:none;">
                      <img src="{{ url_for('image_file', filename='AWS.png') }}" alt="AWS" style="object-fit:contain; padding:6px;">
                      <span>AWS-SA</span>
                    </a>
                    <a href="{{ url_for('course_detail', slug='linux') }}" class="tech-item" style="text-decoration:none;">
                      <img src="{{ url_for('image_file', filename='linux.jpg') }}" alt="Linux" style="mix-blend-mode:multiply;">
                      <span>Linux</span>
                    </a>
                    <a href="{{ url_for('course_detail', slug='devops') }}" class="tech-item" style="text-decoration:none;">
                      <img src="{{ url_for('image_file', filename='devops.png') }}" alt="DevOps" style="object-fit:contain; padding:2px;">
                      <span>Multi-Cloud DevOps</span>
                    </a>
                    <a href="{{ url_for('course_detail', slug='spoken-english') }}" class="tech-item" style="text-decoration:none;">
                      <img src="{{ url_for('image_file', filename='37527b78-62d1-49a2-adad-0ae6d46cf44a.png') }}" alt="English">
                      <span>Spoken English</span>
                    </a>
                    <a href="{{ url_for('course_detail', slug='sdlc') }}" class="tech-item" style="text-decoration:none;">
                      <img src="{{ url_for('image_file', filename='SDLC.jpg') }}" alt="SDLC" style="mix-blend-mode:multiply; object-fit:contain; padding:2px;">
                      <span>SDLC</span>
                    </a>
                    <a href="{{ url_for('course_detail', slug='vibe-coding') }}" class="tech-item" style="text-decoration:none;">
                      <img src="{{ url_for('image_file', filename='vibe_coding.png') }}" alt="Vibe Coding">
                      <span>Vibe Coding</span>
                    </a>
                  </div>

                  <div class="info-label" style="margin-top:24px;">Available In</div>
                  <div class="lang-row">
                    <div class="lang-item">
                      <img src="{{ url_for('image_file', filename='flags/us.png') }}" class="flag-icon" alt="US">
                      <span>English</span>
                    </div>
                    <div class="lang-item">
                      <img src="{{ url_for('image_file', filename='flags/in.png') }}" class="flag-icon" alt="IN">
                      <span>Telugu</span>
                    </div>
                    <div class="lang-item">
                      <img src="{{ url_for('image_file', filename='flags/in.png') }}" class="flag-icon" alt="IN">
                      <span>Hindi</span>
                    </div>
                  </div>
                </div>
                <div class="info-card">
                  <div class="graphical-label">Services</div>
                  
                  <style>
                    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

                    .services-inner {
                       display: flex;
                       flex-direction: column;
                       justify-content: space-between; /* Distribute items to fill height */
                       height: 100%;
                       min-height: 320px; /* Ensure it takes up vertical space */
                       padding: 10px 0;
                    }

                    .handwriting-list {
                      list-style: none;
                      padding: 0;
                      margin: 0;
                      font-family: 'Patrick Hand', cursive;
                      font-size: 22px; /* Larger text */
                      color: #1e3a8a;
                      line-height: 1.6;
                      flex-grow: 1;
                      display: flex;
                      flex-direction: column;
                      justify-content: space-around; /* Distribute list items evenly */
                    }
                    .handwriting-list li {
                      margin-bottom: 12px;
                      display: flex;
                      align-items: center;
                      flex-wrap: wrap; /* Allow text to wrap if very long */
                      min-height: 40px;
                    }
                    
                    /* The writing hand cursor */
                    .pencil-cursor {
                      display: inline-block;
                      width: 50px; /* Much larger */
                      height: 50px;
                      margin-left: -5px;
                      margin-top: -15px; /* Adjust alignment to look like tip is on line */
                      /* Hand holding pencil SVG */
                      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3C!-- Hand --%3E%3Cpath d='M60 50 Q75 40 85 55 T80 80 Q60 90 50 70' fill='%23ffccaa' stroke='%23d4a373' stroke-width='2'/%3E%3C!-- Fingers wrapping --%3E%3Ccircle cx='70' cy='60' r='8' fill='%23ffccaa' stroke='%23d4a373' stroke-width='1'/%3E%3Ccircle cx='65' cy='68' r='8' fill='%23ffccaa' stroke='%23d4a373' stroke-width='1'/%3E%3C!-- Pencil Body --%3E%3Cpath d='M20 90 L50 60 L65 75 L35 105 Z' fill='%23fbbf24' stroke='%23b45309' stroke-width='2' transformation='rotate(-45 50 50)'/%3E%3C!-- Pencil Tip --%3E%3Cpath d='M20 90 L10 100 L35 105 Z' fill='%23fde047'/%3E%3Cpath d='M10 100 L15 95 L20 100 Z' fill='%231e3a8a'/%3E%3C!-- Eraser --%3E%3Cpath d='M50 60 L60 50 L75 65 L65 75 Z' fill='%23f472b6' stroke='%23be185d' stroke-width='1'/%3E%3C/svg%3E");
                      /* Better detailed SVG of hand holding pencil */
                      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cg transform='translate(5,5)'%3E%3C!-- Pencil --%3E%3Cpath d='M38.5 12.5 L46.5 20.5 L18 49 L10 41 Z' fill='%23FBBF24' stroke='%23B45309' stroke-width='1'/%3E%3Cpath d='M10 41 L5 54 L18 49' fill='%23FDE68A' stroke='%23B45309' stroke-width='1'/%3E%3Cpath d='M5 54 L8 46 L13 51 Z' fill='%23333'/%3E%3Cpath d='M38.5 12.5 L42.5 8.5 L50.5 16.5 L46.5 20.5 Z' fill='%239CA3AF' stroke='%234B5563' stroke-width='1'/%3E%3Cpath d='M42.5 8.5 L46.5 4.5 Q50.5 0.5 54.5 4.5 L58.5 8.5 Q62.5 12.5 58.5 16.5 L54.5 20.5 L50.5 16.5 Z' fill='%23F472B6' stroke='%23BE185D' stroke-width='1'/%3E%3C!-- Hand --%3E%3Cpath d='M40 30 Q50 25 55 35 Q60 45 45 50 Q35 52 30 40' fill='%23FFDCBC' stroke='%23E0A070' stroke-width='1.5'/%3E%3Cellipse cx='42' cy='32' rx='6' ry='8' fill='%23FFDCBC' stroke='%23E0A070' stroke-width='1' transform='rotate(-20)'/%3E%3Cellipse cx='36' cy='38' rx='6' ry='8' fill='%23FFDCBC' stroke='%23E0A070' stroke-width='1' transform='rotate(-10)'/%3E%3C/g%3E%3C/svg%3E");
                      
                      background-size: contain;
                      background-repeat: no-repeat;
                      transition: transform 0.05s;
                      z-index: 10;
                      position: relative;
                    }
                    
                    .writing-active .pencil-cursor {
                      animation: complexWrite 0.4s infinite alternate;
                    }
                    
                    @keyframes complexWrite {
                       0% { transform: translate(0, 0) rotate(0deg); }
                       25% { transform: translate(1px, -2px) rotate(2deg); }
                       50% { transform: translate(-1px, 1px) rotate(-1deg); }
                       75% { transform: translate(2px, -1px) rotate(1deg); }
                       100% { transform: translate(0, 0) rotate(0deg); }
                    }

                    /* Green tick written styling */
                    .check-mark {
                        color: #16a34a;
                        font-weight: 900;
                        margin-right: 8px;
                        font-size: 24px;
                    }
                  </style>

                  <div class="services-container">
                    <div class="services-inner">
                        <ul id="dynamic-services" class="handwriting-list">
                          <!-- JS will populate this -->
                        </ul>
                    </div>
                  </div>

                  <script>
                    (function() {
                      const services = [
                        "Online and Offline Classes Available (Hyderabad only)",
                        "Course Material",
                        "Resume Preparation",
                        "Online Profile Building",
                        "Mock Interviews",
                        "Complimentary Spoken English Classes"
                      ];
                      
                      const container = document.getElementById('dynamic-services');
                      
                      async function typeService(text) {
                        const li = document.createElement('li');
                        
                        // Text span (will contain the Checkmark + Text)
                        const textSpan = document.createElement('span');
                        li.appendChild(textSpan);
                        
                        // Pencil
                        const pencil = document.createElement('span');
                        pencil.className = 'pencil-cursor';
                        li.appendChild(pencil);
                        
                        container.appendChild(li);
                        
                        li.classList.add('writing-active');
                        
                        const fullText = "✔ " + text;
                        
                        // Type logic
                        for (let i = 0; i < fullText.length; i++) {
                           const char = fullText[i];
                           
                           if (i === 0) {
                               // Styling the checkmark
                               const checkSpan = document.createElement('span');
                               checkSpan.className = 'check-mark';
                               checkSpan.textContent = char;
                               textSpan.appendChild(checkSpan);
                           } else {
                               // Regular text
                               textSpan.appendChild(document.createTextNode(char));
                           }

                           // small random delay for realistic writing speed
                           // slightly faster to ensure it doesn't take forever to fill list
                           await new Promise(r => setTimeout(r, 20 + Math.random() * 20)); 
                        }
                        
                        li.classList.remove('writing-active');
                        pencil.remove(); 
                      }

                      async function runAnimationLoop() {
                        while (true) {
                          container.innerHTML = '';
                          for (const service of services) {
                            await typeService(service);
                            // Brief pause between lines
                            await new Promise(r => setTimeout(r, 100)); 
                          }
                          // Wait before clearing and restarting
                          await new Promise(r => setTimeout(r, 4000));
                        }
                      }

                      // Start if visible
                      runAnimationLoop();
                    })();
                  </script>

                </div>
              </div>

              <!-- Certifications -->
              <div>
                <div class="section-title">
                  <img src="{{ url_for('image_file', filename='cert_header_logo.png') }}" style="width:28px;height:auto;" alt="Cert Icon">
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
                  <!-- Adobe Photoshop -->
                  <div class="cert-card">
                    <img class="cert-img" src="{{ url_for('image_file', filename='photoshop.svg') }}" alt="Adobe Photoshop">
                    <div class="cert-name">Adobe Photoshop</div>
                  </div>
                  <!-- IELTS -->
                  <div class="cert-card">
                    <img class="cert-img" src="{{ url_for('image_file', filename='ielts_v2_transparent.png') }}" alt="IELTS">
                    <div class="cert-name">IELTS</div>
                  </div>
                  <!-- CELPIP -->
                  <div class="cert-card">
                    <img class="cert-img" src="{{ url_for('image_file', filename='celpip_logo.png') }}" alt="CELPIP">
                    <div class="cert-name">CELPIP</div>
                  </div>
                  <!-- Duolingo -->
                  <div class="cert-card">
                    <img class="cert-img" src="{{ url_for('image_file', filename='duolingo.svg') }}" alt="Duolingo">
                    <div class="cert-name">Duolingo</div>
                  </div>
                </div>
              </div>
          </div>
        """
        return render_page_func(profile_html, active="profile")
