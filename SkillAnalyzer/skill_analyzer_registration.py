from flask import Blueprint, render_template, render_template_string, request, flash, redirect, url_for, make_response, session
import json
import os
from datetime import datetime
from fpdf import FPDF
import base64
import tempfile

# ==========================================
#  JSON DATABASE LOGIC
# ==========================================

DATA_FILE = os.path.join(os.path.dirname(__file__), 'registrations.json')

def init_json_db():
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump([], f)
        except Exception as e:
            print(f"Error initializing data file: {e}")

def save_registration_to_json(data):
    try:
        registrations = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                try:
                    registrations = json.load(f)
                except json.JSONDecodeError:
                    registrations = []
        
        data['id'] = len(registrations) + 1
        data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registrations.append(data)
        
        with open(DATA_FILE, 'w') as f:
            json.dump(registrations, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False

# ==========================================
#  PREMIUM UI TEMPLATE
# ==========================================

REGISTRATION_HTML = """
<style>
    /* Override global main container styles for this page only */
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
    
    /* Premium Page Layout */
    .sr-page-container {
        /* Full viewport height to ensure centering */
        min-height: 80vh; /* Adjusted to account for header/nav if needed, but 100% is fine */
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        position: relative;
    }

    /* Ambient Background Glow - Removed entirely to let pure sky shine */
    .sr-glow-bg {
        display: none;
    }

    /* Glassmorphism Card - Wider and more prominent */
    .sr-card {
        position: relative;
        z-index: 10;
        /* Very light dark tint to keep text readable against bright sky */
        background: rgba(15, 15, 20, 0.45); 
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 30px;
        padding: 60px;
        width: 100%;
        /* Increased width to occupy more screen real estate */
        max-width: 700px;
        box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.6);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .sr-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 30px 60px -12px rgba(99, 102, 241, 0.2);
        border-color: rgba(99, 102, 241, 0.3);
    }

    /* Header Styling */
    .sr-header {
        text-align: center;
        margin-bottom: 40px;
    }
    
    .sr-title {
        font-family: 'Outfit', sans-serif; /* Assuming usage of primary font */
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #fff 0%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    
    .sr-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
    }

    /* Form Elements */
    .sr-form-group {
        margin-bottom: 25px;
        position: relative;
    }

    .sr-label {
        display: block;
        margin-bottom: 10px;
        color: #e2e8f0;
        font-weight: 500;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .sr-input {
        width: 100%;
        padding: 16px 20px;
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        color: #fff;
        font-size: 1.1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .sr-input:focus {
        outline: none;
        background: rgba(0, 0, 0, 0.5);
        border-color: #6366f1;
        box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
        transform: scale(1.01);
    }
    
    .sr-input::placeholder {
        color: rgba(255, 255, 255, 0.3);
    }

    /* Submit Button */
    .sr-submit-btn {
        width: 100%;
        padding: 18px;
        margin-top: 20px;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border: none;
        border-radius: 14px;
        font-size: 1.2rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
    }

    .sr-submit-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.6);
        background: linear-gradient(135deg, #818cf8 0%, #6366f1 100%);
    }

    .sr-submit-btn:active {
        transform: translateY(1px);
    }

    /* Flash Messages */
    .sr-flash {
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 25px;
        font-weight: 500;
        text-align: center;
        animation: fadeIn 0.5s ease;
    }
    
    .sr-flash-success {
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #34d399;
    }
    
    .sr-flash-error {
        background: rgba(239, 68, 68, 0.15);
        border: 1px solid rgba(239, 68, 68, 0.3);
        color: #f87171;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>

<div class="sr-page-container">
    <div class="sr-glow-bg"></div>
    
    <div class="sr-card">
        <div class="sr-header">
            <h1 class="sr-title">Register Now</h1>
            <p class="sr-subtitle">Unlock your personalized skill analysis</p>
        </div>
        
        <div class="sr-flash-area">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="sr-flash sr-flash-{{ category }}">{{ message }}</div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
        </div>

        <form method="POST" action="/skill-registration">
            <input type="hidden" name="next" value="NEXT_URL_PLACEHOLDER">
            <div class="sr-form-group">
                <label class="sr-label" for="name">Full Name</label>
                <input class="sr-input" type="text" id="name" name="name" required placeholder="Ex. John Doe">
            </div>
            
            <div class="sr-form-group">
                <label class="sr-label" for="institution">Institution / Organization</label>
                <input class="sr-input" type="text" id="institution" name="institution" placeholder="Ex. University of Tech">
            </div>

            <div class="sr-form-group">
                <label class="sr-label" for="mobile">Mobile Number</label>
                <input class="sr-input" type="tel" id="mobile" name="mobile" required placeholder="+91 98765 43210">
            </div>

            <div class="sr-form-group">
                <label class="sr-label" for="email">Email Address</label>
                <input class="sr-input" type="email" id="email" name="email" required placeholder="john@example.com">
            </div>

            <button type="submit" class="sr-submit-btn">Start Assessment ➔</button>
        </form>
    </div>
</div>
"""


# ==========================================
#  ROUTE REGISTRATION
# ==========================================

def register_routes(app, render_page_callback=None):
    init_json_db()

    # @app.route('/skill-analyzer') removed to fix collision
    @app.route('/skill-registration', methods=['GET', 'POST'], endpoint='skill_registration')
    def skill_analyzer():
        if request.method == 'POST':
            name = request.form.get('name')
            institution = request.form.get('institution')
            mobile = request.form.get('mobile')
            email = request.form.get('email')
            next_url = request.form.get('next')

            # bypass validation to debug
            if False: # if not name or not mobile or not email:
                print("DEBUG: Validation failed - Missing fields")
                flash("Please fill in all required fields.", "error")
            else:
                print(f"DEBUG: Form Data: {request.form}")
                print(f"DEBUG: Registration valid for {name}. Processing...")
                registration_data = {
                    "name": name,
                    "institution": institution,
                    "mobile": mobile,
                    "email": email
                }
                
                # Attempt to save, but don't block exam on failure
                try:
                    save_success = save_registration_to_json(registration_data)
                    if not save_success:
                        print("DEBUG: Save returned False, but proceeding.")
                except Exception as e:
                    print(f"DEBUG: Save crashed {e}")

                # Always redirect if validation passes
                print(f"DEBUG: Redirecting to {next_url or 'Fallback'}")
                flash(f"Success! Redirecting you to the assessment...", "success")
                if next_url:
                    return redirect(next_url)
                # Fallback to default AWS exam if link context is lost
                return redirect('/skill-analyzer/take-test/CLF-C02')

        # GET Handling
        next_url = request.args.get('next', '')
        html = REGISTRATION_HTML # Use native action="/skill-registration"
        html = html.replace('NEXT_URL_PLACEHOLDER', next_url)

        if render_page_callback:
            return render_page_callback(html, active="skill-analyzer")
        
        return render_template_string(html)

    @app.route('/skill-analyzer/download-result', methods=['POST'])
    def download_result():
        try:
            exam_data_str = request.form.get('exam_data')
            if not exam_data_str:
                return "No exam data provided", 400
            
            data = json.loads(exam_data_str)
            
            # --- PDF GENERATION ---
            pdf = FPDF()
            pdf.add_page()
            
            # 1. Header / Certificate Section
            pdf.set_font("Arial", 'B', 24)
            pdf.cell(0, 20, "Skill Analysis Report", 0, 1, 'C')
            
            pdf.set_font("Arial", '', 14)
            pdf.cell(0, 10, f"Candidate: {data.get('user_name', 'Candidate')}", 0, 1)
            pdf.cell(0, 10, f"Exam: {data.get('exam_title', 'Cloud Assessment')}", 0, 1)
            pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", 0, 1)
            
            score = data.get('score', 0)
            passed = data.get('passed', False)
            
            # --- Graph Image ---
            graph_img = data.get('graph_image')
            if graph_img:
                try:
                    # Remove header
                    if ',' in graph_img:
                        graph_img = graph_img.split(',')[1]
                    img_data = base64.b64decode(graph_img)
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_img:
                        tmp_img.write(img_data)
                        tmp_name = tmp_img.name
                    
                    # Add to PDF
                    pdf.image(tmp_name, x=10, y=60, w=100) # Left side
                    os.unlink(tmp_name) # Clean up
                except Exception as e:
                    print(f"Graph error: {e}")

            # --- Summary ---
            summary = data.get('skill_summary', '')
            if summary:
                pdf.set_xy(120, 60) # Right side
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(0, 10, "Skill Analysis:", 0, 1)
                pdf.set_font("Arial", '', 10)
                pdf.set_xy(120, 70)
                pdf.multi_cell(0, 6, summary)
            
            # Move Cursor down for Questions
            pdf.set_y(150)
            

            
            score_color = (16, 185, 129) if passed else (239, 68, 68)
            pdf.set_text_color(*score_color)
            pdf.set_font("Arial", 'B', 20)
            pdf.cell(0, 20, f"Score: {score}% - {'PASSED' if passed else 'FAILED'}", 0, 1, 'C')
            pdf.set_text_color(0, 0, 0)
            
            pdf.ln(10)
            
            # 2. Detailed Questions
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "Detailed Analysis", 0, 1)
            pdf.ln(5)
            
            questions = data.get('questions', [])
            
            for i, q in enumerate(questions, 1):
                pdf.set_font("Arial", 'B', 12)
                # Ensure question text is latin-1 compatible or sanitise
                q_text = q['question'].encode('latin-1', 'replace').decode('latin-1')
                pdf.multi_cell(0, 8, f"Q{i}. {q_text}")
                
                user_idx = q.get('user_idx', -1)
                correct_idx = q.get('correct_idx', -1)
                options = q.get('options', [])
                
                pdf.set_font("Arial", '', 11)
                for opt_i, opt_val in enumerate(options):
                    opt_val = str(opt_val).encode('latin-1', 'replace').decode('latin-1')
                    prefix = "[ ]"
                    if opt_i == user_idx: prefix = "[X] (Your Answer)"
                    if opt_i == correct_idx: prefix = "[V] (Correct)"
                    if opt_i == user_idx and opt_i == correct_idx: prefix = "[X] [V] (Correct & Selected)"
                    
                    pdf.cell(10)
                    pdf.cell(0, 8, f"{prefix} {opt_val}", 0, 1)
                
                pdf.ln(2)
                if q.get('explanation'):
                    pdf.set_font("Arial", 'I', 10)
                    pdf.set_text_color(100, 100, 100)
                    expl = q['explanation'].encode('latin-1', 'replace').decode('latin-1')
                    pdf.multi_cell(0, 6, f"Explanation: {expl}")
                    pdf.set_text_color(0, 0, 0)
                
                pdf.ln(8)
                
            response = make_response(pdf.output(dest='S').encode('latin-1'))
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'attachment; filename=Skill_Analysis_Report.pdf'
            return response

        except Exception as e:
            print(f"Error generating PDF: {e}")
            return f"Error: {str(e)}", 500

    @app.route('/skill-analyzer/download-certificate', methods=['POST'])
    def download_certificate():
        try:
            exam_code = request.form.get('exam_code', 'General')
            score = request.form.get('score', '0')
            
            user_name = session.get('user_info', {}).get('name', 'Candidate')
            
            badges = {
                'CLF-C01': {'title': "AWS Certified Cloud Practitioner", 'image': 'aws_cloud_practitioner.png'},
                'CLF-C02': {'title': "AWS Certified Cloud Practitioner", 'image': 'aws_cloud_practitioner.png'}
            }
            details = badges.get(exam_code, {'title': "Certificate of Completion", 'image': 'aws_icon.png'})
            
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            img_path = os.path.join(base_dir, 'images', details['image'])
            
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()
            
            # Border
            pdf.set_line_width(2)
            pdf.rect(10, 10, 277, 190)
            
            # Badge
            if os.path.exists(img_path):
                pdf.image(img_path, x=130, y=20, w=40)
            
            # Title
            pdf.set_xy(0, 65)
            pdf.set_font("Arial", 'B', 30)
            pdf.cell(0, 20, "CERTIFICATE OF ACHIEVEMENT", 0, 1, 'C')
            
            pdf.set_font("Arial", '', 16)
            pdf.cell(0, 15, "This certificate is proudly presented to", 0, 1, 'C')
            
            pdf.set_font("Arial", 'B', 24)
            pdf.cell(0, 15, user_name, 0, 1, 'C')
            
            pdf.set_font("Arial", '', 16)
            pdf.cell(0, 15, "For successfully passing the examination", 0, 1, 'C')
            
            pdf.set_font("Arial", 'B', 20)
            pdf.cell(0, 15, details['title'], 0, 1, 'C')
            
            pdf.set_font("Arial", 'I', 12)
            pdf.cell(0, 10, f"Score: {score}%", 0, 1, 'C')
            
            pdf.set_xy(60, 160)
            pdf.set_font("Arial", '', 12)
            pdf.cell(60, 10, f"Date: {datetime.now().strftime('%B %d, %Y')}", 'T', 0, 'C')
            
            pdf.set_xy(180, 160)
            pdf.cell(60, 10, "Instructor / Admin", 'T', 0, 'C')
            
            response = make_response(pdf.output(dest='S').encode('latin-1'))
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = f'attachment; filename=Certificate_{exam_code}.pdf'
            return response

        except Exception as e:
            print(f"Error generating certificate: {e}")
            return str(e), 500



