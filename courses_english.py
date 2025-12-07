# courses_english.py
# Spoken English & Corporate Etiquette module (Premium UI)
# Exposes: render() -> HTML string

import random

CURRICULUM = {
    "foundations": {
        "title": "Linguistic Foundations",
        "icon": "🗣️",
        "desc": "Master the nuances of pronunciation, phonetics, and grammar to speak with clarity and authority.",
        "topics": ["Neutralizing Mother Tongue Influence", "Advanced Vocabulary & Idioms", "Sentence Stress & Intonation"]
    },
    "corporate": {
        "title": "Corporate Communication",
        "icon": "🤝",
        "desc": "Navigate the professional world with etiquette-driven communication for emails, meetings, and chats.",
        "topics": ["Professional Email Writing", "Effective Meeting Participation", "Cross-Cultural Communication"]
    },
    "presentation": {
        "title": "Public Speaking & Demos",
        "icon": "🎤",
        "desc": "Deliver compelling presentations and technical demos that capture stakeholder attention.",
        "topics": ["Storytelling for Tech Demos", "Body Language & Voice Modulation", "Handling Q&A Sessions"]
    },
    "career": {
        "title": "Career Acceleration",
        "icon": "🚀",
        "desc": "Ace interviews and negotiations with confidence and strategic communication skills.",
        "topics": ["Mock Interview Drills", "Salary Negotiation scripts", "Networking & LinkedIn Brand"]
    }
}

LABS = [
    "<strong>Elevator Pitch:</strong> Record a 60-second professional intro.",
    "<strong>Email Audit:</strong> Rewrite 3 real-world emails for clarity and tone.",
    "<strong>Mock Interview:</strong> 1:1 simulation with real-time feedback.",
    "<strong>Tech Demo:</strong> Present a 5-min technical concept to a non-tech audience."
]

def _section_card(key, info, idx):
    delay = f"{idx * 0.15}s"
    topics_html = "".join([f"<li>{t}</li>" for t in info['topics']])
    
    return f"""
    <div class="english-card" style="animation-delay:{delay};">
        <div class="card-icon">{info['icon']}</div>
        <div class="card-content">
            <h3 class="card-title">{info['title']}</h3>
            <p class="card-desc">{info['desc']}</p>
            <ul class="topic-list">
                {topics_html}
            </ul>
        </div>
    </div>
    """

def render():
    cards_html = "".join([_section_card(k, v, i) for i, (k, v) in enumerate(CURRICULUM.items())])
    labs_list_html = "".join([f"<li>{item}</li>" for item in LABS])

    return f"""
    <style>
        @keyframes fadeUp {{
            from {{ opacity: 0; transform: translateY(15px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .english-container {{
            font-family: 'Inter', sans-serif;
            color: #064e3b;
        }}

        .english-header {{
            background: linear-gradient(120deg, #ecfdf5 0%, #d1fae5 100%);
            border-radius: 16px;
            padding: 36px;
            margin-bottom: 32px;
            border: 1px solid #a7f3d0;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.05);
        }}

        .english-header h1 {{
            margin: 0 0 12px 0;
            font-size: 2.4rem;
            background: linear-gradient(to right, #059669, #047857);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }}

        .english-header p {{
            font-size: 1.15rem;
            color: #374151;
            max-width: 700px;
            line-height: 1.6;
        }}

        .grid-english {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
        }}

        .english-card {{
            background: #ffffff;
            border-radius: 14px;
            padding: 24px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            animation: fadeUp 0.6s ease-out backwards;
            display: flex;
            gap: 16px;
        }}

        .english-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 20px -5px rgba(5, 150, 105, 0.08);
            border-color: #6ee7b7;
        }}

        .card-icon {{
            font-size: 2.2rem;
            background: #ecfdf5;
            width: 56px;
            height: 56px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }}

        .card-content {{ flex: 1; }}

        .card-title {{
            margin: 0 0 6px 0;
            font-size: 1.2rem;
            color: #065f46;
            font-weight: 700;
        }}

        .card-desc {{
            margin: 0 0 12px 0;
            color: #4b5563;
            font-size: 0.95rem;
            line-height: 1.4;
        }}

        .topic-list {{
            margin: 0;
            padding-left: 18px;
            color: #374151;
            font-size: 0.9rem;
            line-height: 1.5;
        }}

        .lab-section {{
            margin-top: 40px;
            background: #fff;
            border-radius: 16px;
            padding: 28px;
            border: 1px dashed #10b981;
            background-image: radial-gradient(#d1fae5 1px, transparent 1px);
            background-size: 20px 20px;
        }}

        .action-row {{
            margin-top: 32px;
            display: flex;
            justify-content: center;
        }}

        .btn-green {{
            background: linear-gradient(90deg, #34d399, #10b981);
            color: #064e3b;
            padding: 12px 32px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 800;
            font-size: 16px;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
            transition: transform 0.2s;
        }}
        .btn-green:hover {{ transform: scale(1.04); }}
    </style>

    <div class="english-container">
        <div class="english-header">
            <h1>Communicate with Impact</h1>
            <p>
                In the global tech landscape, technical skills get you the job, but communication skills get you promoted.
                Refine your presence, master corporate etiquette, and speak with confidence.
            </p>
        </div>

        <div class="grid-english">
            {cards_html}
        </div>

        <div class="lab-section">
            <h2 style="margin-top:0; color:#065f46;">🧪 Practical Labs & Drills</h2>
            <ul style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:12px; font-size:1rem; color:#1f2937;">
                {labs_list_html}
            </ul>
        </div>

        <div class="action-row">
            <a class="btn-green" href="/contact">Join the Next Cohort</a>
        </div>
        
        <p style="text-align:center; margin-top:24px;">
            <a href="/courses" style="text-decoration:none; color:#059669; font-weight:700;">⬅ Back to Courses</a>
        </p>
    </div>
    """
