from flask import url_for

def register_routes(app, render_page_func):
    @app.route("/skill-selection")
    def skill_selection():
        # Parent Page: Shows "Live Test" and "Virtual Interview"
        try:
            from .LiveTest import LIVE_TEST_CONTENT
            from .VirtualInterview import VIRTUAL_INTERVIEW_CONTENT
            
            # Update Live Test route to point to our new hub
            LIVE_TEST_CONTENT['route'] = url_for('live_test_hub')
            
            # Ensure features are present for the main cards
            if 'features' not in LIVE_TEST_CONTENT: LIVE_TEST_CONTENT['features'] = []
            if 'features' not in VIRTUAL_INTERVIEW_CONTENT: VIRTUAL_INTERVIEW_CONTENT['features'] = []

            modules = [LIVE_TEST_CONTENT, VIRTUAL_INTERVIEW_CONTENT]
        except ImportError:
            modules = []

        # HTML for Parent Page
        html = """
        {% raw %}
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
            
            /* --- ANIMATED HEADER --- */
            .sa-header {
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
            }
            
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .sa-title {
                font-family: 'Outfit', sans-serif;
                font-size: 3rem;
                font-weight: 800;
                margin: 0;
                background: linear-gradient(to right, #ffffff, #94a3b8);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            /* --- MODULES GRID --- */
            .sa-modules-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 30px;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }

            .sa-card {
                background: #fff;
                border-radius: 20px;
                border: 1px solid #e2e8f0;
                padding: 30px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.05);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                height: 100%;
            }

            .sa-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                border-color: #3b82f6;
            }
            
            .sa-icon-box {
                width: 80px; height: 80px;
                border-radius: 50%;
                background: #f8fafc;
                display: flex; align-items: center; justify-content: center;
                margin-bottom: 20px;
                overflow: hidden;
                border: 1px solid #f1f5f9;
                font-size: 2.5rem;
            }
            
            .sa-icon-box img {
                width: 85%;
                height: 85%;
                object-fit: contain;
            }
            
            .sa-card h2 {
                font-family: 'Outfit', sans-serif;
                color: #1e293b;
                font-size: 1.5rem;
                margin: 0 0 12px 0;
                font-weight: 700;
            }
            
            .sa-card p {
                color: #64748b;
                font-size: 1rem;
                line-height: 1.5;
                margin-bottom: 24px;
                flex-grow: 1;
            }

            .sa-btn {
                background: #0f172a;
                color: #fff;
                padding: 12px 24px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                transition: background 0.2s;
                width: 100%;
                display: block;
                box-sizing: border-box;
                margin-top: auto;
            }
            .sa-btn:hover {
                background: #334155;
            }
            
            .sa-features {
                list-style: none;
                padding: 0;
                margin: 0 0 24px 0;
                text-align: left;
                width: 100%;
            }
            .sa-features li {
                margin-bottom: 8px;
                color: #475569;
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 0.9rem;
            }
            .sa-features li::before {
                content: '✓';
                color: #10b981;
                font-weight: bold;
            }

        </style>
        {% endraw %}

        <div style="font-family: 'Inter', sans-serif; padding-bottom: 40px;">
            
            <!-- Animated Header -->
            <div class="sa-header">
                <h1 class="sa-title">Single Platform to Analyze Your Skills</h1>
            </div>

            <!-- Modules -->
            <div class="sa-modules-container">
                {% for module in modules %}
                <div class="sa-card">
                    <div class="sa-icon-box">
                        <!-- If 'image' is a file path, render it. Else render emoji. -->
                        {% if module.get('image') %}
                            <img src="{{ url_for('image_file', filename=module['image']) }}" alt="{{ module['title'] }}">
                        {% else %}
                           <!-- Fallback icons -->
                           {% if module['title'] == 'Live Test' %}📝{% elif module['title'] == 'Virtual Interview' %}🎙️{% else %}❓{% endif %}
                        {% endif %}
                    </div>
                    <h2>{{ module['title'] }}</h2>
                    <p>{{ module['description'] }}</p>
                    
                    {% if module.get('features') %}
                    <ul class="sa-features">
                        {% for feature in module['features'] %}
                        <li>{{ feature }}</li>
                        {% endfor %}
                    </ul>
                    {% endif %}

                    <a href="{{ module.get('route', '#') }}" class="sa-btn">{{ module['action_label'] }}</a>
                </div>
                {% endfor %}
            </div>
        </div>
        """
        return render_page_func(html, active="skill-analyzer", modules=modules)

    @app.route("/skill-analyzer/live-test")
    def live_test_hub():
        # Child Page: Shows specific tests (Cloud, DevOps, Linux, Others)
        try:
            from .Skill_test.Skill_anlz_test_sujects import (
                CLOUD_TEST_CONTENT, 
                DEVOPS_TEST_CONTENT, 
                LINUX_TEST_CONTENT, 
                OTHERS_TEST_CONTENT
            )
            modules = [CLOUD_TEST_CONTENT, DEVOPS_TEST_CONTENT, LINUX_TEST_CONTENT, OTHERS_TEST_CONTENT]
        except ImportError:
            modules = []

        html = """
        {% raw %}
        <style>
             /* Reusing styles from parent page with adjustments for 4-column layout */
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
            
            .sa-header {
                background: linear-gradient(-45deg, #0f172a, #334155); 
                padding: 40px 20px; /* Reduced padding */
                border-radius: 24px;
                text-align: center;
                color: #fff;
                margin-bottom: 30px;
            }
            .sa-title {
                font-family: 'Outfit', sans-serif;
                font-size: 2.2rem; /* Slightly smaller title */
                font-weight: 800;
                background: linear-gradient(to right, #ffffff, #cbd5e1);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .sa-modules-container {
                display: grid;
                /* Force 4 columns on large screens, auto-wrap on smaller */
                grid-template-columns: repeat(4, 1fr); 
                gap: 20px; /* Reduced gap */
                max-width: 1500px; /* Increased width to fit 4 comfortably */
                margin: 0 auto;
                padding: 0 20px;
            }
            @media (max-width: 1200px) {
                .sa-modules-container {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
            @media (max-width: 768px) {
                .sa-modules-container {
                    grid-template-columns: 1fr;
                }
            }

            .sa-card {
                background: #fff;
                border-radius: 16px; /* Slightly smaller radius */
                border: 1px solid #e2e8f0;
                padding: 20px; /* Reduced padding */
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                display: flex; flex-direction: column; align-items: center; text-align: center; height: 100%;
                transition: transform 0.2s;
            }
            .sa-card:hover { transform: translateY(-5px); border-color:#3b82f6; }
            
            .sa-icon-box {
                width: 65px; height: 65px; /* Reduced size */
                border-radius: 50%; background: #f8fafc;
                display: flex; align-items: center; justify-content: center;
                margin-bottom: 15px; overflow: hidden; border: 1px solid #f1f5f9;
            }
            .sa-icon-box img { width: 80%; height: 80%; object-fit: contain; }
            
            .sa-card h2 { 
                font-family: 'Outfit', sans-serif; 
                color: #1e293b; 
                font-size: 1.3rem; /* Smaller heading */
                margin-bottom: 8px; 
                font-weight: 700; 
                line-height: 1.2;
            }
            .sa-card p { 
                color: #64748b; 
                font-size: 0.9rem; 
                margin-bottom: 16px; 
                flex-grow: 1; 
                line-height: 1.4;
            }
            .sa-btn {
                background: #0f172a; color: #fff; padding: 10px 20px; border-radius: 8px;
                text-decoration: none; font-weight: 600; display: block; width: 100%; box-sizing: border-box; margin-top: auto;
                font-size: 0.95rem;
            }
            .sa-btn:hover { background: #334155; }
            
            .sa-features { list-style: none; padding: 0; margin: 0 0 16px 0; text-align: left; width: 100%; }
            .sa-features li { 
                margin-bottom: 6px; 
                color: #475569; 
                display: flex; 
                align-items: center; 
                gap: 8px; 
                font-size: 0.85rem; 
            }
            .sa-features li::before { content: '✓'; color: #10b981; font-weight: bold; }
        </style>
        {% endraw %}
        
        <div style="font-family: 'Inter', sans-serif; padding-bottom: 40px;">
            <div class="sa-header">
                <h1 class="sa-title">Select Assessment Type</h1>
                <div style="margin-top:10px; color:#94a3b8;"><a href="{{ url_for('skill_selection') }}" style="color:#cbd5e1;text-decoration:none;">← Back to Main</a></div>
            </div>

            <div class="sa-modules-container">
                {% for module in modules %}
                <div class="sa-card">
                    <div class="sa-icon-box">
                        <img src="{{ url_for('image_file', filename=module['image']) }}" alt="{{ module['title'] }}">
                    </div>
                    <h2>{{ module['title'] }}</h2>
                    <p>{{ module['description'] }}</p>
                    {% if module.get('features') %}
                    <ul class="sa-features">
                        {% for feature in module['features'] %}
                        <li>{{ feature }}</li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                    <a href="{{ module.get('route', '#') }}" class="sa-btn">{{ module['action_label'] }}</a>
                </div>
                {% endfor %}
            </div>
        </div>
        """
        return render_page_func(html, active="skill-analyzer", modules=modules)

    @app.route("/skill-analyzer/cloud-test")
    def cloud_test_hub():
        # Grandchild Page: Shows AWS, Azure, GCP
        try:
            from .Skill_test.cloud_test.cloud_test import (
                AWS_CONTENT,
                AZURE_CONTENT,
                GCP_CONTENT
            )
            modules = [AWS_CONTENT, AZURE_CONTENT, GCP_CONTENT]
        except ImportError:
            modules = []

        html = """
        {% raw %}
        <style>
             /* Reusing styles from parent page with adjustments for 3-column layout */
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
            
            .sa-header {
                background: linear-gradient(-45deg, #0f172a, #334155); 
                padding: 40px 20px;
                border-radius: 24px;
                text-align: center;
                color: #fff;
                margin-bottom: 30px;
            }
            .sa-title {
                font-family: 'Outfit', sans-serif;
                font-size: 2.2rem;
                font-weight: 800;
                background: linear-gradient(to right, #ffffff, #cbd5e1);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .sa-modules-container {
                display: grid;
                /* Force 3 columns for 3 items */
                grid-template-columns: repeat(3, 1fr); 
                gap: 20px;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }
            @media (max-width: 900px) {
                .sa-modules-container {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
            @media (max-width: 600px) {
                .sa-modules-container {
                    grid-template-columns: 1fr;
                }
            }

            .sa-card {
                background: #fff;
                border-radius: 16px;
                border: 1px solid #e2e8f0;
                padding: 20px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                display: flex; flex-direction: column; align-items: center; text-align: center; height: 100%;
                transition: transform 0.2s;
            }
            .sa-card:hover { transform: translateY(-5px); border-color:#3b82f6; }
            
            .sa-icon-box {
                width: 70px; height: 70px;
                border-radius: 50%; background: #f8fafc;
                display: flex; align-items: center; justify-content: center;
                margin-bottom: 15px; overflow: hidden; border: 1px solid #f1f5f9;
            }
            .sa-icon-box img { width: 85%; height: 85%; object-fit: contain; }
            
            .sa-card h2 { 
                font-family: 'Outfit', sans-serif; 
                color: #1e293b; 
                font-size: 1.3rem;
                margin-bottom: 8px; 
                font-weight: 700; 
                line-height: 1.2;
            }
            .sa-card p { 
                color: #64748b; 
                font-size: 0.9rem; 
                margin-bottom: 16px; 
                flex-grow: 1; 
                line-height: 1.4;
            }
            .sa-btn {
                background: #0f172a; color: #fff; padding: 10px 20px; border-radius: 8px;
                text-decoration: none; font-weight: 600; display: block; width: 100%; box-sizing: border-box; margin-top: auto;
                font-size: 0.95rem;
            }
            .sa-btn:hover { background: #334155; }
            
            .sa-features { list-style: none; padding: 0; margin: 0 0 16px 0; text-align: left; width: 100%; }
            .sa-features li { 
                margin-bottom: 6px; 
                color: #475569; 
                display: flex; 
                align-items: center; 
                gap: 8px; 
                font-size: 0.85rem; 
            }
            .sa-features li::before { content: '✓'; color: #10b981; font-weight: bold; }
        </style>
        {% endraw %}
        
        <div style="font-family: 'Inter', sans-serif; padding-bottom: 40px;">
            <div class="sa-header">
                <h1 class="sa-title">Cloud Assessments</h1>
                 <div style="margin-top:10px; color:#94a3b8;"><a href="{{ url_for('live_test_hub') }}" style="color:#cbd5e1;text-decoration:none;">← Back to Test Hub</a></div>
            </div>

            <div class="sa-modules-container">
                {% for module in modules %}
                <div class="sa-card">
                    <div class="sa-icon-box">
                        <img src="{{ url_for('image_file', filename=module['image']) }}" alt="{{ module['title'] }}">
                    </div>
                    <h2>{{ module['title'] }}</h2>
                    <p>{{ module['description'] }}</p>
                    {% if module.get('features') %}
                    <ul class="sa-features">
                        {% for feature in module['features'] %}
                        <li>{{ feature }}</li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                    <a href="{{ module.get('route', '#') }}" class="sa-btn">{{ module['action_label'] }}</a>
                </div>
                {% endfor %}
            </div>
        </div>
        """
        return render_page_func(html, active="skill-analyzer", modules=modules)
