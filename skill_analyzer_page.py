# skill_analyzer_page.py

def register_routes(app, render_page_func):
    @app.route("/skill-analyzer")
    def skill_analyzer():
        # Import backend content
        try:
            from LiveTest import LIVE_TEST_CONTENT
            from VirtualInterview import VIRTUAL_INTERVIEW_CONTENT
        except ImportError:
            LIVE_TEST_CONTENT = {"title": "Live Test", "description": "Backend missing", "features": [], "action_label": "Error"}
            VIRTUAL_INTERVIEW_CONTENT = {"title": "Virtual Interview", "description": "Backend missing", "features": [], "action_label": "Error"}

        # Define styles and HTML
        html = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
            
            /* --- ANIMATED HEADER --- */
            .sa-header {{
                position: relative;
                background: linear-gradient(-45deg, #1e293b, #0f172a, #334155, #1e293b);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
                padding: 60px 20px;
                border-radius: 24px;
                text-align: center;
                color: #fff;
                overflow: hidden;
                margin-bottom: 40px;
                box-shadow: 0 20px 40px -10px rgba(0,0,0,0.3);
            }}
            
            @keyframes gradientBG {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}

            /* Moving graphical elements */
            .sa-header::before {{
                content: '';
                position: absolute;
                top: -50%; left: -50%;
                width: 200%; height: 200%;
                background: radial-gradient(circle, rgba(255,255,255,0.05) 0%, transparent 60%);
                animation: rotate-overlay 30s linear infinite;
                pointer-events: none;
            }}
            
            @keyframes rotate-overlay {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}

            .sa-title {{
                font-family: 'Outfit', sans-serif;
                font-size: 3rem;
                font-weight: 800;
                margin: 0;
                position: relative;
                z-index: 2;
                letter-spacing: -0.02em;
                background: linear-gradient(to right, #ffffff, #94a3b8);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            
            /* --- MODULES GRID --- */
            .sa-modules-container {{
                display: flex;
                flex-wrap: wrap;
                gap: 30px;
                justify-content: center;
                max-width: 1200px;
                margin: 0 auto;
            }}

            .sa-card {{
                flex: 1;
                min-width: 320px;
                background: #fff;
                border-radius: 20px;
                border: 1px solid #e2e8f0;
                padding: 40px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.05);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
            }}

            .sa-card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                border-color: #3b82f6;
            }}
            
            .sa-icon-circle {{
                width: 80px; height: 80px;
                border-radius: 50%;
                background: #eff6ff;
                display: flex; align-items: center; justify-content: center;
                margin-bottom: 24px;
                font-size: 2rem;
            }}
            
            .sa-card h2 {{
                font-family: 'Outfit', sans-serif;
                color: #1e293b;
                font-size: 1.8rem;
                margin: 0 0 16px 0;
            }}
            
            .sa-card p {{
                color: #64748b;
                font-size: 1.1rem;
                line-height: 1.6;
                margin-bottom: 30px;
                flex-grow: 1;
            }}
            
            .sa-features {{
                list-style: none;
                padding: 0;
                margin: 0 0 30px 0;
                text-align: left;
                width: 100%;
            }}
            .sa-features li {{
                margin-bottom: 10px;
                color: #475569;
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 0.95rem;
            }}
            .sa-features li::before {{
                content: '✓';
                color: #10b981;
                font-weight: bold;
            }}

            .sa-btn {{
                background: #0f172a;
                color: #fff;
                padding: 14px 32px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: 600;
                transition: background 0.2s;
                width: 100%;
                box-sizing: border-box;
            }}
            .sa-btn:hover {{
                background: #334155;
            }}

        </style>

        <div style="font-family: 'Inter', sans-serif; padding: 20px;">
            
            <!-- Animated Header -->
            <div class="sa-header">
                <h1 class="sa-title">Single Platform to Analyze Your Skills</h1>
            </div>

            <!-- Modules -->
            <div class="sa-modules-container">
                
                <!-- Live Test Module -->
                <div class="sa-card">
                    <div class="sa-icon-circle" style="background: #e0f2fe; color: #0284c7;">📝</div>
                    <h2>{LIVE_TEST_CONTENT['title']}</h2>
                    <p>{LIVE_TEST_CONTENT['description']}</p>
                    <ul class="sa-features">
                        {''.join([f'<li>{f}</li>' for f in LIVE_TEST_CONTENT['features']])}
                    </ul>
                    <a href="/contact" class="sa-btn">{LIVE_TEST_CONTENT['action_label']}</a>
                </div>

                <!-- Virtual Interview Module -->
                <div class="sa-card">
                    <div class="sa-icon-circle" style="background: #fdf2f8; color: #db2777;">🎙️</div>
                    <h2>{VIRTUAL_INTERVIEW_CONTENT['title']}</h2>
                    <p>{VIRTUAL_INTERVIEW_CONTENT['description']}</p>
                    <ul class="sa-features">
                        {''.join([f'<li>{f}</li>' for f in VIRTUAL_INTERVIEW_CONTENT['features']])}
                    </ul>
                    <a href="/contact" class="sa-btn">{VIRTUAL_INTERVIEW_CONTENT['action_label']}</a>
                </div>

            </div>
        </div>
        """
        return render_page_func(html, active="skill-analyzer")
