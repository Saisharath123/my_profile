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

              <form method="post" action="{{ url_for('contact') }}" novalidate>

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

              <!-- CONTACT INFO -->
              <div class="right-contact-info">
                  <div class="email-row">
                      <svg width="18" height="18" viewBox="0 0 24 24"><path d="M3 6.5A2.5 2.5 0 0 1 5.5 4h13A2.5 2.5 0 0 1 21 6.5v11A2.5 2.5 0 0 1 18.5 20h-13A2.5 2.5 0 0 1 3 17.5v-11zM5.5 6L12 10.2 18.5 6" fill="#0b1620"/></svg>
                      <a href="mailto:multiclouddevops4u@gmail.com" style="text-decoration:none;"><span class="email-text">multiclouddevops4u@gmail.com</span></a>
                  </div>
                  <div style="height:8px;"></div>
                  <div class="phone-row">
                      <svg width="18" height="18" viewBox="0 0 24 24"><path d="M6.6 10.2a15.05 15.05 0 0 0 7.2 7.2l1.9-1.9a1 1 0 0 1 1.0-.2c1.1.4 2.4.7 3.7.7a1 1 0 0 1 1 1v3.0a1 1 0 0 1-1 1C10.7 21 3 13.3 3 3.5A1 1 0 0 1 4 2.5h3.0a1 1 0 0 1 1 1c0 1.3.3 2.6.7 3.7a1 1 0 0 1-.2 1.0l-1.9 1.9z" fill="#0b1620"/></svg>
                      <a href="tel:+919666562012" style="text-decoration:none;"><span class="phone-text">+91 96665 62012</span></a>
                  </div>
              </div>
            </div>

          </div>
        """
        return render_page_func(form_html, active="contact")
