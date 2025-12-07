# courses_english.py
# Spoken English & Corporate Etiquette module (Advanced UI)
# Exposes: render() -> HTML string

def render():
    return """
    <style>
        /* --- Animation Keyframes --- */
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes pulse-soft {
            0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
            100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        /* --- Main Container & Typography --- */
        .eng-wrapper {
            font-family: 'Inter', sans-serif;
            color: #1f2937;
            max-width: 1200px;
            margin: 0 auto;
        }

        .eng-h1 {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #047857 0%, #10b981 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 16px 0;
            letter-spacing: -0.02em;
        }

        .eng-sub {
            font-size: 1.2rem;
            color: #4b5563;
            line-height: 1.6;
            max-width: 800px;
        }

        /* --- Hero Section --- */
        .eng-hero {
            position: relative;
            padding: 60px 40px;
            background: radial-gradient(circle at top right, #e2e8f0 0%, #ffffff 40%),
                        linear-gradient(120deg, #ecfdf5 0%, #ffffff 100%);
            border-radius: 24px;
            overflow: hidden;
            box-shadow: 0 20px 40px -10px rgba(6, 78, 59, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.6);
            margin-bottom: 40px;
        }
        
        .eng-hero::before {
            content: "";
            position: absolute;
            top: -50px; right: -50px;
            width: 300px; height: 300px;
            background: linear-gradient(135deg, #a7f3d0 0%, #34d399 100%);
            filter: blur(80px);
            opacity: 0.3;
            border-radius: 50%;
            z-index: 0;
        }

        .eng-hero-content {
            position: relative;
            z-index: 1;
        }

        /* --- Tab Navigation --- */
        .eng-tabs {
            display: flex;
            gap: 12px;
            margin-bottom: 32px;
            flex-wrap: wrap;
            border-bottom: 2px solid #f3f4f6;
            padding-bottom: 2px;
        }

        .eng-tab-btn {
            background: transparent;
            border: none;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 600;
            color: #6b7280;
            cursor: pointer;
            border-radius: 8px 8px 0 0;
            position: relative;
            transition: all 0.3s ease;
        }

        .eng-tab-btn:hover {
            color: #047857;
            background: #ecfdf5;
        }

        .eng-tab-btn.active {
            color: #064e3b;
            background: #fff;
            border-bottom: 3px solid #10b981;
        }

        .eng-tab-content {
            display: none;
            animation: fadeIn 0.4s ease-out;
        }
        
        .eng-tab-content.active {
            display: block;
        }

        /* --- Glassmorphism Cards (Curriculum) --- */
        .eng-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
        }

        .eng-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            padding: 28px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02), 
                        0 10px 15px -3px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), 
                        box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .eng-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 30px -4px rgba(6, 78, 59, 0.1);
            background: rgba(255, 255, 255, 0.9);
            border-color: #a7f3d0;
        }

        .card-icon-box {
            width: 60px; height: 60px;
            background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            color: #059669;
            box-shadow: inset 0 2px 4px rgba(255,255,255,0.8);
        }

        .card-h3 {
            font-size: 1.25rem;
            font-weight: 700;
            color: #064e3b;
            margin: 0;
        }

        .card-topics {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .card-topics li {
            padding-left: 24px;
            position: relative;
            color: #4b5563;
            font-size: 0.95rem;
            line-height: 1.4;
        }

        .card-topics li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #10b981;
            font-weight: bold;
        }

        /* --- Timeline (Journey Tab) --- */
        .timeline-wrapper {
            position: relative;
            padding: 20px 0;
            max-width: 800px;
            margin: 0 auto;
        }

        .timeline-wrapper::before {
            content: "";
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 4px;
            background: #e5e7eb;
            transform: translateX(-50%);
            border-radius: 2px;
        }

        .timeline-item {
            position: relative;
            width: 50%;
            padding: 0 40px;
            box-sizing: border-box;
            margin-bottom: 40px;
        }

        .timeline-item:nth-child(odd) { left: 0; text-align: right; }
        .timeline-item:nth-child(even) { left: 50%; text-align: left; }

        .timeline-dot {
            position: absolute;
            top: 20px;
            width: 20px; height: 20px;
            background: #10b981;
            border-radius: 50%;
            border: 4px solid #fff;
            box-shadow: 0 0 0 4px #a7f3d0;
            z-index: 2;
        }
        
        .timeline-item:nth-child(odd) .timeline-dot { right: -14px; }
        .timeline-item:nth-child(even) .timeline-dot { left: -14px; }

        .timeline-content {
            background: #fff;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            border: 1px solid #f3f4f6;
            transition: transform 0.3s ease;
        }

        .timeline-content:hover { transform: translateY(-4px); }

        .timeline-year {
            font-size: 0.85rem;
            color: #059669;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
            display: block;
        }

        /* --- Labs Grid (Labs Tab) --- */
        .labs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }

        .lab-card {
            background: #fff;
            border-radius: 16px;
            padding: 24px;
            border: 1px solid #e5e7eb;
            position: relative;
            overflow: hidden;
        }

        .lab-card::after {
            content: "LAB";
            position: absolute;
            bottom: -10px; right: -10px;
            font-size: 4rem;
            font-weight: 900;
            color: #f3f4f6;
            z-index: 0;
            transform: rotate(-15deg);
        }

        .lab-card-content { position: relative; z-index: 1; }
        .lab-icon { font-size: 2rem; margin-bottom: 12px; display: block; }
        .lab-title { font-weight: 700; color: #111827; margin-bottom: 8px; font-size: 1.1rem; }
        .lab-desc { color: #6b7280; font-size: 0.95rem; line-height: 1.5; }

        /* --- CTA Section --- */
        .eng-cta {
            background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
            border-radius: 20px;
            padding: 48px;
            text-align: center;
            color: #fff;
            margin-top: 60px;
            position: relative;
            overflow: hidden;
        }

        .eng-cta-btn {
            display: inline-block;
            background: #fff;
            color: #064e3b;
            padding: 16px 48px;
            font-weight: 800;
            border-radius: 12px;
            text-decoration: none;
            margin-top: 24px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .eng-cta-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        }

        /* Mobile tweaks */
        @media (max-width: 768px) {
            .eng-h1 { font-size: 2rem; }
            .timeline-wrapper::before { left: 40px; }
            .timeline-item { width: 100%; padding-left: 80px; padding-right: 0; text-align: left; }
            .timeline-item:nth-child(odd) { text-align: left; }
            .timeline-item:nth-child(odd) .timeline-dot,
            .timeline-item:nth-child(even) .timeline-dot { left: 30px; right: auto; }
        }
    </style>

    <div class="eng-wrapper">
        <!-- Hero -->
        <div class="eng-hero">
            <div class="eng-hero-content">
                <h1 class="eng-h1">Communicate with Executive Presence</h1>
                <p class="eng-sub">
                    Elevate your career with a curriculum designed for the global tech landscape. 
                    Master corporate etiquette, public speaking, and strategic communication.
                </p>
            </div>
        </div>

        <!-- Tabs Navigation -->
        <div class="eng-tabs">
            <button class="eng-tab-btn active" onclick="openEngTab('curriculum')">Curriculum modules</button>
            <button class="eng-tab-btn" onclick="openEngTab('labs')">Practical Labs</button>
            <button class="eng-tab-btn" onclick="openEngTab('journey')">Your Journey</button>
        </div>

        <!-- Curriculum Tab Content -->
        <div id="curriculum" class="eng-tab-content active">
            <div class="eng-grid">
                <div class="eng-card">
                    <div class="card-icon-box">🗣️</div>
                    <div class="card-content">
                        <h3 class="card-h3">Linguistic Foundations</h3>
                        <p style="color:#6b7280; font-size:0.95rem; margin-bottom:12px;">Master pronunciation and clarity.</p>
                        <ul class="card-topics">
                            <li>Neutralizing Mother Tongue Influence</li>
                            <li>Advanced Vocabulary & Idioms</li>
                            <li>Sentence Stress & Intonation</li>
                        </ul>
                    </div>
                </div>
                <div class="eng-card">
                    <div class="card-icon-box">🤝</div>
                    <div class="card-content">
                        <h3 class="card-h3">Corporate Communication</h3>
                        <p style="color:#6b7280; font-size:0.95rem; margin-bottom:12px;">Navigate the professional world.</p>
                        <ul class="card-topics">
                            <li>Professional Email Writing</li>
                            <li>Effective Meeting Participation</li>
                            <li>Cross-Cultural Communication</li>
                        </ul>
                    </div>
                </div>
                <div class="eng-card">
                    <div class="card-icon-box">🎤</div>
                    <div class="card-content">
                        <h3 class="card-h3">Public Speaking & Demos</h3>
                        <p style="color:#6b7280; font-size:0.95rem; margin-bottom:12px;">Deliver compelling presentations.</p>
                        <ul class="card-topics">
                            <li>Storytelling for Tech Demos</li>
                            <li>Body Language & Voice Modulation</li>
                            <li>Handling Q&A Sessions</li>
                        </ul>
                    </div>
                </div>
                <div class="eng-card">
                    <div class="card-icon-box">🚀</div>
                    <div class="card-content">
                        <h3 class="card-h3">Career Acceleration</h3>
                        <p style="color:#6b7280; font-size:0.95rem; margin-bottom:12px;">Ace interviews and negotiations.</p>
                        <ul class="card-topics">
                            <li>Mock Interview Drills</li>
                            <li>Salary Negotiation Scripts</li>
                            <li>Networking & LinkedIn Brand</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Labs Tab Content -->
        <div id="labs" class="eng-tab-content">
            <div class="labs-grid">
                <div class="lab-card">
                    <div class="lab-card-content">
                        <span class="lab-icon">⏱️</span>
                        <div class="lab-title">Elevator Pitch</div>
                        <div class="lab-desc">Record a 60-second professional intro. Receive AI and peer feedback.</div>
                    </div>
                </div>
                <div class="lab-card">
                    <div class="lab-card-content">
                        <span class="lab-icon">📧</span>
                        <div class="lab-title">Email Audit</div>
                        <div class="lab-desc">Rewrite 3 real-world emails for clarity, conciseness, and tone.</div>
                    </div>
                </div>
                <div class="lab-card">
                    <div class="lab-card-content">
                        <span class="lab-icon">👔</span>
                        <div class="lab-title">Mock Interview</div>
                        <div class="lab-desc">1:1 simulation with real-time feedback on answers and body language.</div>
                    </div>
                </div>
                <div class="lab-card">
                    <div class="lab-card-content">
                        <span class="lab-icon">🖥️</span>
                        <div class="lab-title">Tech Demo</div>
                        <div class="lab-desc">Present a 5-min technical concept to a non-technical audience.</div>
                    </div>
                </div>
                <div class="lab-card">
                    <div class="lab-card-content">
                        <span class="lab-icon">💬</span>
                        <div class="lab-title">Group Discussion</div>
                        <div class="lab-desc">Participate in a moderated debate to practice assertiveness.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Journey Tab Content (Timeline) -->
        <div id="journey" class="eng-tab-content">
            <div class="timeline-wrapper">
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <span class="timeline-year">WEEK 1-2</span>
                        <h3 style="margin:0 0 8px 0; color:#1f2937;">Foundation & Diagnostics</h3>
                        <p style="margin:0; color:#6b7280;">Initial assessment of speech patterns. Focus on phonetics and neutralizing accent.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <span class="timeline-year">WEEK 3-4</span>
                        <h3 style="margin:0 0 8px 0; color:#1f2937;">Professional Fluency</h3>
                        <p style="margin:0; color:#6b7280;">Mastering corporate vocabulary. Email etiquette workshops and meeting simulations.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <span class="timeline-year">WEEK 5</span>
                        <h3 style="margin:0 0 8px 0; color:#1f2937;">Presentation Mastery</h3>
                        <p style="margin:0; color:#6b7280;">Drills on body language, voice modulation, and delivering impactful tech demos.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <span class="timeline-year">WEEK 6</span>
                        <h3 style="margin:0 0 8px 0; color:#1f2937;">Career High-Note</h3>
                        <p style="margin:0; color:#6b7280;">Final mock interviews, salary negotiation tactics, and LinkedIn profile optimization.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Bottom CTA -->
        <div class="eng-cta">
            <h2 style="margin:0 0 12px 0; font-size:2rem;">Ready to Transform?</h2>
            <p style="font-size:1.1rem; opacity:0.9;">Join a community of professionals mastering the art of communication.</p>
            <a href="/contact" class="eng-cta-btn">Join the Next Cohort</a>
            
            <div style="margin-top:32px;">
                 <a href="/courses" style="color:#a7f3d0; text-decoration:none; font-weight:600; font-size:0.95rem;">⬅ Back to Courses</a>
            </div>
        </div>
    </div>

    <script>
        function openEngTab(tabName) {
            var i;
            var x = document.getElementsByClassName("eng-tab-content");
            for (i = 0; i < x.length; i++) {
                x[i].style.display = "none";
                x[i].classList.remove("active");
            }
            document.getElementById(tabName).style.display = "block";
            
            var btns = document.getElementsByClassName("eng-tab-btn");
            for (i = 0; i < btns.length; i++) {
                btns[i].classList.remove("active");
            }
            // Simple active state toggle
            event.currentTarget.classList.add("active");
        }
    </script>
    """
