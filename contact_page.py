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
            @keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
            
            .contact-wrap { 
              display: flex; 
              gap: 24px; 
              flex-wrap: wrap; 
              animation: fadeIn 0.6s ease-out;
            }

            .contact-panel {
              flex: 1; 
              min-width: 320px;
              border-radius: 20px; 
              padding: 32px;
              background: #ffffff;
              box-shadow: 0 20px 40px -12px rgba(0,0,0,0.05);
              border: 1px solid rgba(0,0,0,0.04);
              transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .contact-panel:hover {
              transform: translateY(-2px);
              box-shadow: 0 25px 50px -12px rgba(0,0,0,0.08);
            }

            h2.contact-title { 
              margin: 0 0 8px 0; 
              font-size: 28px; 
              color: #111827; 
              letter-spacing: -0.5px;
            }
            p.contact-sub { 
              margin: 0 0 24px 0; 
              color: #6B7280; 
              font-size: 15px; 
              line-height: 1.5;
            }

            .form-row { display: flex; gap: 16px; margin-bottom: 16px; }
            .form-row .field { flex: 1; }
            
            label {
                display: block;
                font-size: 13px;
                font-weight: 600;
                color: #374151;
                margin-bottom: 6px;
                margin-left: 2px;
            }

            .field input, .field textarea {
              width: 100%;
              padding: 14px 16px;
              border-radius: 12px;
              border: 1px solid #E5E7EB;
              background: #F9FAFB;
              color: #111827;
              font-weight: 500;
              font-size: 15px;
              transition: all 0.2s ease;
              box-sizing: border-box;
              font-family: inherit;
            }
            .field input:focus, .field textarea:focus {
              outline: none;
              border-color: #60A5FA;
              background: #ffffff;
              box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.1);
            }
            .field textarea { resize: vertical; min-height: 150px; }

            .message-wrap { display: flex; gap: 24px; flex-wrap: wrap; }
            .message-container { flex: 1; min-width: 300px; }
            
            .btn-send {
              margin-top: 8px;
              background: linear-gradient(135deg, #3B82F6 0%, #10B981 100%);
              border: none; 
              padding: 14px 28px;
              border-radius: 12px; 
              color: white;
              font-weight: 700; 
              font-size: 16px;
              cursor: pointer;
              transition: filter 0.2s ease, transform 0.1s ease;
              width: 100%;
              box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            }
            .btn-send:hover {
              filter: brightness(110%);
              transform: translateY(-1px);
            }
            .btn-send:active {
                transform: translateY(0);
            }

            .contact-side {
              width: 320px; 
              min-width: 280px;
              border-radius: 20px; 
              padding: 28px;
              background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
              border: 1px solid rgba(186, 230, 253, 0.4);
              height: fit-content;
            }

            .side-cards { 
                display: grid; 
                grid-template-columns: 1fr 1fr; 
                gap: 12px; 
                margin-top: 20px; 
            }
            .side-card {
              background: #ffffff; 
              padding: 16px 12px; 
              border-radius: 12px;
              box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
              text-align: center; 
              font-weight: 600;
              font-size: 13px;
              color: #0F172A;
              border: 1px solid #E2E8F0;
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 8px;
              transition: transform 0.2s;
            }
            .side-card:hover {
                transform: translateY(-2px);
                border-color: #BAE6FD;
            }
            .side-card span { font-size: 20px; }

            .right-contact-info {
              margin-top: 24px; 
              padding-top: 20px;
              border-top: 1px solid rgba(0,0,0,0.06);
            }
            .contact-link-row {
              display: flex;
              align-items: center;
              gap: 12px;
              padding: 10px 0;
              color: #334155;
              text-decoration: none;
              transition: transform 0.2s;
            }
            .contact-link-row:hover {
                transform: translateX(4px);
                color: #0284c7;
            }
            .contact-link-row span { font-weight: 600; font-size: 15px; }

            @media (max-width: 768px){
              .contact-wrap { flex-direction: column; }
              .contact-side { width: 100%; box-sizing: border-box; }
              .message-container { width: 100%; }
              .form-row { flex-direction: column; gap: 12px; }
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
