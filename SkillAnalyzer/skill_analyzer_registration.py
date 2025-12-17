from flask import Blueprint, render_template, render_template_string, request, flash, redirect, url_for
import json
import os
from datetime import datetime

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
            <!-- <h1 class="sr-title">Register Now</h1> -->
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

        <form method="POST" action="/skill-analyzer">
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

    @app.route('/skill-analyzer', methods=['GET', 'POST'])
    def skill_analyzer():
        if request.method == 'POST':
            name = request.form.get('name')
            institution = request.form.get('institution')
            mobile = request.form.get('mobile')
            email = request.form.get('email')

            if not name or not mobile or not email:
                flash("Please fill in all required fields.", "error")
            else:
                registration_data = {
                    "name": name,
                    "institution": institution,
                    "mobile": mobile,
                    "email": email
                }
                
                if save_registration_to_json(registration_data):
                    flash(f"Success! Redirecting you to the assessment...", "success")
                    return redirect(url_for('skill_selection'))
                else:
                    flash("An error occurred. Please try again.", "error")

        if render_page_callback:
            return render_page_callback(REGISTRATION_HTML.replace('action="/skill-registration"', 'action="/skill-analyzer"'), active="skill-analyzer")
        
        return render_template_string(REGISTRATION_HTML.replace('action="/skill-registration"', 'action="/skill-analyzer"'))

