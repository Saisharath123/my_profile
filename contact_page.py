# contact_page.py
import os
import smtplib
from email.message import EmailMessage
from flask import request, redirect, url_for, flash

# Email Configuration Defaults
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

def send_contact_email(name, sender_email, message_body, email_config):
    """
    Send message using Gmail SMTP.
    email_config must contain: 'password', 'to_email', 'admin_email'
    """
    password = email_config.get('password')
    to_email = email_config.get('to_email')
    admin_email = email_config.get('admin_email')

    if not password or password == "<PUT_PASSWORD_HERE>":
        raise RuntimeError("EMAIL_PASSWORD not configured")

    msg = EmailMessage()
    msg["From"] = f"{name} <{sender_email}>"
    msg["To"] = to_email
    msg["Subject"] = f"Website contact: message from {name}"
    body = f"You have received a new message from the website contact form.\n\nName: {name}\nEmail: {sender_email}\n\nMessage:\n{message_body}\n\n--\nSent by Cloud with Sai website"
    msg.set_content(body)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(admin_email, password)
        smtp.send_message(msg)

def register_routes(app, render_page_func, base_dir, email_config):
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
                with open(os.path.join(base_dir, "contacts.txt"), "a", encoding="utf-8") as fh:
                    fh.write(safe_line)
            except Exception:
                flash("Failed to save message (server error).")
                return redirect(url_for("contact"))

            try:
                full_message = f"{message}\n\nMobile: {mobile}"
                send_contact_email(name, email, full_message, email_config)
                flash("Thanks — message received and emailed. I'll get back to you.")
            except RuntimeError:
                flash("Thanks — message received. Email sending is not configured on this server.")
            except Exception:
                flash("Thanks — message received. Email could not be sent due to a server error.")

            return redirect(url_for("contact"))

        # GET request - render form
        form_html = """
          <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700;800&display=swap');
            
            @keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
            
            /* Override global app.py container to be transparent */
            .card {
              background: transparent !important;
              box-shadow: none !important;
              border: none !important;
              padding: 0 !important;
            }
            .container {
              max-width: 100% !important;
              padding: 0 !important;
              margin: 0 !important;
              width: 100% !important;
            }

            .contact-wrap { 
              display: flex; 
              gap: 30px; 
              flex-wrap: wrap; 
              animation: fadeIn 0.6s ease-out;
              max-width: 1100px;
              margin: 0 auto;
              padding: 20px;
              font-family: 'Outfit', sans-serif; /* Global font for contact section */
            }

            .contact-panel {
              flex: 1.4; 
              min-width: 340px;
              border-radius: 24px; 
              padding: 40px;
              background: rgba(255, 255, 255, 0.25);
              backdrop-filter: blur(24px);
              -webkit-backdrop-filter: blur(24px);
              border: 1px solid rgba(255, 255, 255, 0.4);
              box-shadow: 0 20px 50px -12px rgba(0,0,0,0.1);
              transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .contact-panel:hover {
              transform: translateY(-2px);
              box-shadow: 0 30px 60px -12px rgba(0,0,0,0.15);
            }

            h2.contact-title { 
              margin: 0 0 10px 0; 
              font-size: 36px; 
              font-weight: 800;
              color: #0F172A; 
              letter-spacing: -1px;
              background: linear-gradient(to right, #0f172a, #334155);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
            }
            p.contact-sub { 
              margin: 0 0 32px 0; 
              color: #334155; 
              font-size: 16px; 
              line-height: 1.6;
              font-weight: 500;
            }

            .form-row { display: flex; gap: 20px; margin-bottom: 24px; }
            .form-row .field { flex: 1; }
            
            label {
                display: flex;
                align-items: center;
                gap: 6px;
                font-size: 11px;
                text-transform: uppercase;
                letter-spacing: 1px;
                font-weight: 800;
                color: #1e293b;
                margin-bottom: 10px;
                margin-left: 4px;
            }

            /* Enhanced "Filling Things" (Inputs) */
            .field input, .field textarea {
              width: 100%;
              padding: 16px 20px;
              border-radius: 16px;
              border: 2px solid rgba(255, 255, 255, 0.3);
              background: rgba(255, 255, 255, 0.15);
              backdrop-filter: blur(10px);
              color: #0F172A;
              font-weight: 600;
              font-size: 16px;
              font-family: 'Outfit', sans-serif;
              transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
              box-sizing: border-box;
              box-shadow: inset 0 2px 4px rgba(0,0,0,0.03);
            }
            .field input::placeholder, .field textarea::placeholder {
                color: #64748b;
                font-weight: 500;
                opacity: 0.8;
            }
            .field input:focus, .field textarea:focus {
              outline: none;
              border-color: #60A5FA;
              background: rgba(255, 255, 255, 0.85);
              box-shadow: 0 10px 25px -5px rgba(96, 165, 250, 0.3), inset 0 2px 4px rgba(0,0,0,0.02);
              transform: translateY(-2px);
            }
            .field textarea { resize: vertical; min-height: 160px; }

            .message-wrap { display: flex; gap: 24px; flex-wrap: wrap; }
            .message-container { flex: 1; min-width: 300px; }
            
            .btn-send {
              margin-top: 12px;
              background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%);
              border: none; 
              padding: 18px 32px;
              border-radius: 16px; 
              color: white;
              font-weight: 800; 
              font-size: 16px;
              cursor: pointer;
              transition: all 0.3s ease;
              width: 100%;
              box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.4);
              text-transform: uppercase;
              letter-spacing: 0.5px;
            }
            .btn-send:hover {
              filter: brightness(110%);
              transform: translateY(-2px);
              box-shadow: 0 15px 35px -5px rgba(37, 99, 235, 0.5);
            }
            .btn-send:active {
                transform: translateY(0);
            }

            .contact-side {
              flex: 1;
              width: 320px; 
              min-width: 280px;
              border-radius: 24px; 
              padding: 36px;
              background: rgba(255, 255, 255, 0.25);
              backdrop-filter: blur(24px);
              -webkit-backdrop-filter: blur(24px);
              border: 1px solid rgba(255, 255, 255, 0.3);
              height: fit-content;
            }
            
            /* Graphical Header on Right Side */
            .contact-side h3 {
                margin: 0 0 12px 0; 
                color: #0f172a; 
                font-size: 24px; /* Increased size */
                font-weight: 800;
                background: linear-gradient(135deg, #1e293b 0%, #3b82f6 100%); /* Blue-dark gradient */
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .contact-side p {
                margin: 0 0 24px 0; 
                color: #334155; 
                font-size: 15px; 
                line-height: 1.6;
                font-weight: 500;
            }

            .side-cards { 
                display: grid; 
                grid-template-columns: 1fr 1fr; 
                gap: 16px; 
                margin-top: 24px; 
            }
            .side-card {
              background: rgba(255, 255, 255, 0.4); 
              padding: 20px 16px; 
              border-radius: 16px;
              box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
              text-align: center; 
              font-weight: 700;
              font-size: 14px;
              color: #1e293b;
              border: 1px solid rgba(255, 255, 255, 0.3);
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 10px;
              transition: all 0.2s ease;
            }
            .side-card:hover {
                transform: translateY(-4px);
                border-color: #60A5FA;
                background: rgba(255, 255, 255, 0.7);
                box-shadow: 0 10px 20px -5px rgba(96, 165, 250, 0.2);
            }
            .side-card span { font-size: 24px; display: block; margin-bottom: 4px; }

            .right-contact-info {
              margin-top: 32px; 
              padding-top: 24px;
              border-top: 2px solid rgba(255,255,255,0.2);
            }
            .contact-link-row {
              display: flex;
              align-items: center;
              gap: 16px;
              padding: 12px 16px;
              background: rgba(255,255,255,0.2);
              border-radius: 12px;
              margin-bottom: 12px;
              color: #0f172a;
              text-decoration: none;
              transition: all 0.2s;
              border: 1px solid transparent;
              font-weight: 600;
            }
            .contact-link-row:hover {
                transform: translateX(4px);
                background: rgba(255,255,255,0.5);
                border-color: #93c5fd;
                color: #0284c7;
            }
            .contact-link-row span { font-size: 14px; }

            @media (max-width: 850px){
              .contact-wrap { flex-direction: column; }
              .contact-side { width: 100%; box-sizing: border-box; }
              .message-container { width: 100%; }
              .form-row { flex-direction: column; gap: 16px; }
            }
          </style>

          <div class="contact-wrap">

            <!-- LEFT FORM PANEL -->
            <div class="contact-panel">
              <h2 class="contact-title">Get in Touch</h2>
              <p class="contact-sub">Have a question or want to collaborate? Drop me a message below.</p>

              <form method="post" action="{{ url_for('contact') }}" novalidate>

                <div class="form-row">
                  <div class="field">
                    <label>Name</label>
                    <input name="name" type="text" placeholder="John Doe" required>
                  </div>
                  <div class="field">
                    <label>Email</label>
                    <input name="email" type="email" placeholder="john@example.com" required>
                  </div>
                </div>

                <div class="form-row">
                  <div class="field">
                    <label>Mobile</label>
                    <input name="mobile" type="tel" placeholder="+91 98765 43210" required>
                  </div>
                </div>

                <div class="field">
                   <label>Message</label>
                   <textarea name="message" placeholder="Tell me about your project or enquiry..." required></textarea>
                </div>

                <button class="btn-send" type="submit">
                    Send Message
                </button>

              </form>
            </div>

            <!-- RIGHT INFO PANEL -->
            <div class="contact-side">
              <h3 style="margin:0 0 8px 0; color:#0f172a; font-size: 18px;">Why reach out?</h3>
              <p style="margin:0 0 16px 0; color:#64748b; font-size: 14px; line-height: 1.5;">
                Whether you need a demo, course details, or technical mentorship — I'm here to help.
              </p>

              <div class="side-cards">
                <div class="side-card"><span>🧪</span>Live Labs</div>
                <div class="side-card"><span>🚀</span>Project Demos</div>
                <div class="side-card"><span>👨‍💻</span>Mentorship</div>
                <div class="side-card"><span>🏆</span>Cert Prep</div>
              </div>

              <!-- CONTACT INFO -->
              <div class="right-contact-info">
                  <a href="mailto:multiclouddevops4u@gmail.com" class="contact-link-row">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                      <span>multiclouddevops4u@gmail.com</span>
                  </a>
                  <a href="tel:+919666562012" class="contact-link-row">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                      <span>+91 96665 62012</span>
                  </a>
              </div>
            </div>

          </div>
        """
        return render_page_func(form_html, active="contact")
