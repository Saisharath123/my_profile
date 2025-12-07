# courses_sdlc.py
# SDLC & Release Management module (Premium UI)
# Exposes: render() -> HTML string

import random

# Use a vibrant placeholder or the existing one if valid. 
# We'll use a local variable for the image to be safe.
HEADER_IMG = "/mnt/data/51BC2F46-B035-4EC2-8054-C3A2697D6723.jpeg"

PHASES = {
    "planning": {
        "title": "Planning & Requirements",
        "icon": "📋",
        "desc": "Define scope, gather requirements, and analyze feasibility. The foundation of successful delivery.",
        "labs": ["Create a Product Backlog", "Draft User Stories", "Feasibility Analysis Matrix"]
    },
    "design": {
        "title": "System Design",
        "icon": "📐",
        "desc": "Architectural blueprints, database schema design, and technical specifications.",
        "labs": ["Draw C4 Model Diagrams", "Database Schema Normalization", "API Contract Design (Swagger)"]
    },
    "development": {
        "title": "Development",
        "icon": "💻",
        "desc": "Coding, code reviews, and version control. Adhering to Clean Code principles.",
        "labs": ["Setup Git Workflow", "Implement Feature Branching", "Static Code Analysis Setup"]
    },
    "testing": {
        "title": "Testing & QA",
        "icon": "🧪",
        "desc": "Unit, Integration, and E2E testing to ensure reliability and bug-free releases.",
        "labs": ["Write Unit Tests (PyTest/Jest)", "Setup Selenium/Cypress", "Automate Regression Suite"]
    },
    "deployment": {
        "title": "Deployment & Release",
        "icon": "🚀",
        "desc": "CI/CD pipelines, containerization, and orchestration (K8s) for production delivery.",
        "labs": ["Build Docker Images", "Configure Jenkins/GitHub Actions", "Blue-Green Deployment Demo"]
    },
    "maintenance": {
        "title": "Maintenance & Ops",
        "icon": "🔧",
        "desc": "Monitoring, logging, patching, and incident management (SRE practices).",
        "labs": ["Setup ELK Stack", "Configure Prometheus Alerts", "Incident Post-Mortem Template"]
    }
}

def _phase_card(key, info, idx):
    delay = f"{idx * 0.1}s"
    # Card styling with glassmorphism and hover lift
    labs_html = "".join([f"<li style='margin-bottom:4px;'>{lab}</li>" for lab in info['labs']])
    
    return f"""
    <div class="sdlc-card" style="animation-delay:{delay};">
        <div class="card-icon">{info['icon']}</div>
        <div class="card-content">
            <h3 class="card-title">{info['title']}</h3>
            <p class="card-desc">{info['desc']}</p>
            <div class="card-labs">
                <strong>Hands-on Labs:</strong>
                <ul>{labs_html}</ul>
            </div>
        </div>
    </div>
    """

def render():
    cards_html = "".join([_phase_card(k, v, i) for i, (k, v) in enumerate(PHASES.items())])

    return f"""
    <style>
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .sdlc-container {{
            font-family: 'Inter', sans-serif;
            color: #0b1620;
        }}

        .sdlc-header {{
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 32px;
            display: flex;
            align-items: center;
            gap: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            border: 1px solid #bae6fd;
        }}

        .header-content h1 {{
            margin: 0 0 12px 0;
            font-size: 2.2rem;
            background: linear-gradient(90deg, #0284c7, #2563eb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }}

        .header-content p {{
            margin: 0;
            font-size: 1.1rem;
            color: #475569;
            line-height: 1.6;
            font-weight: 500;
        }}

        .methodologies-bar {{
            display: flex;
            gap: 12px;
            margin-top: 16px;
            flex-wrap: wrap;
        }}

        .pill {{
            background: #fff;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            color: #0369a1;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border: 1px solid #e0f2fe;
        }}

        .sdlc-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
        }}

        .sdlc-card {{
            background: #ffffff;
            border-radius: 16px;
            padding: 24px;
            border: 1px solid #f1f5f9;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.03);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            animation: fadeInUp 0.6s ease-out backwards;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .sdlc-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border-color: #bfdbfe;
        }}

        .card-icon {{
            font-size: 2.5rem;
            background: #f0f9ff;
            width: 64px;
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            margin-bottom: 8px;
        }}

        .card-title {{
            margin: 0 0 8px 0;
            font-size: 1.25rem;
            color: #1e293b;
            font-weight: 700;
        }}

        .card-desc {{
            margin: 0 0 16px 0;
            color: #64748b;
            font-size: 0.95rem;
            line-height: 1.5;
        }}

        .card-labs {{
            background: #f8fafc;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            margin-top: auto; /* Push to bottom */
        }}

        .card-labs strong {{
            display: block;
            margin-bottom: 8px;
            color: #334155;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .card-labs ul {{
            margin: 0;
            padding-left: 20px;
            font-size: 0.9rem;
            color: #475569;
        }}

        .action-area {{
            margin-top: 40px;
            text-align: center;
            padding: 32px;
            background: #eff6ff;
            border-radius: 16px;
            border: 1px dashed #60a5fa;
        }}
    </style>

    <div class="sdlc-container">
        
        <!-- Header Section -->
        <div class="sdlc-header">
            <div class="header-content">
                <h1>Mastering the SDLC</h1>
                <p>
                    Navigate the complexities of modern software delivery. From initial concept to production deployment, 
                    learn the industry-standard practices that drive efficient, high-quality engineering teams.
                </p>
                <div class="methodologies-bar">
                    <span class="pill">Agile</span>
                    <span class="pill">Scrum</span>
                    <span class="pill">DevOps</span>
                    <span class="pill">CI/CD</span>
                    <span class="pill">SRE</span>
                </div>
            </div>
             <!-- Optional: Header Image if you want one side-by-side on large screens -->
             <!-- <img src="{HEADER_IMG}" style="width:120px; height:120px; object-fit:cover; border-radius:12px; display:none;"> -->
        </div>

        <!-- Cards Grid -->
        <div class="sdlc-grid">
            {cards_html}
        </div>

        <!-- Action / Enrollment -->
        <div class="action-area">
            <h2 style="margin:0 0 12px 0; color:#1e3a8a;">Ready to transform your delivery pipeline?</h2>
            <p style="color:#475569; margin-bottom:24px;">Join the comprehensive workshop and build a real-world release pipeline from scratch.</p>
            <a class="btn" href="/contact" style="font-size:1.1rem; padding:12px 32px;">Enroll Now</a>
        </div>

        <p style="margin-top:32px;">
            <a href="/courses" style="text-decoration:none; display:inline-flex; align-items:center; gap:6px; color:#2563eb; font-weight:700;">
                <span>⬅</span> Back to Courses
            </a>
        </p>

    </div>
    """
