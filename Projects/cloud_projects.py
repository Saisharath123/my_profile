from flask import url_for

CLOUD_PROJECTS = {
    "aws_migration": {
        "title": "AWS Lift & Shift Migration",
        "tags": ["AWS", "DMS", "EC2"],
        "desc": "Zero-downtime migration of a monolithic app to AWS.",
        "category": "cloud"
    },
    "serverless_api": {
        "title": "Serverless REST API",
        "tags": ["Lambda", "API Gateway", "DynamoDB"],
        "desc": "High-scale serverless backend.",
        "category": "cloud"
    },
    "project1": {"title": "Cloud Infra Demo", "tags": ["Cloud"], "desc": "Infrastructure demo.", "category": "cloud"},
}

def render_cloud_page():
    """
    Render the Cloud Projects detailed view with 3 main modules: AWS, GCP, Azure.
    """
    aws_img = url_for('image_file', filename='aws_icon.png')
    gcp_img = url_for('image_file', filename='gcp_icon.png')
    azure_img = url_for('image_file', filename='azure_icon.png')
    
    html = f"""
    <style>
        .cloud-modules-container {{
            padding: 40px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header-section {{
            text-align: center;
            margin-bottom: 50px;
        }}
        
        .header-section h2 {{
            font-size: 2.5rem;
            color: #0f172a;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .header-section p {{
            color: #64748b;
            font-size: 1.1rem;
        }}

        .modules-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            justify-items: center;
        }}
        
        .cloud-module-card {{
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            width: 100%;
            max-width: 350px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            position: relative;
            overflow: hidden;
        }}
        
        .cloud-module-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }}
        
        .cloud-module-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border-color: rgba(14, 165, 233, 0.4);
        }}
        
        .cloud-module-card:hover::before {{
            opacity: 1;
        }}
        
        .logo-container {{
            width: 120px;
            height: 120px;
            margin-bottom: 25px;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.4s ease;
        }}
        
        .cloud-module-card:hover .logo-container {{
            transform: scale(1.1) rotate(5deg);
        }}
        
        .module-logo {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
        }}
        
        .module-title {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 15px;
        }}
        
        .module-desc {{
            color: #64748b;
            font-size: 0.95rem;
            line-height: 1.5;
        }}
        
        .card-decoration {{
            position: absolute;
            bottom: 0;
            right: 0;
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, transparent 50%, rgba(14, 165, 233, 0.05) 50%);
            border-bottom-right-radius: 20px;
            pointer-events: none;
        }}
        
        /* Specific hover colors */
        .cloud-module-card.aws:hover {{ border-color: #FF9900; }}
        .cloud-module-card.gcp:hover {{ border-color: #4285F4; }}
        .cloud-module-card.azure:hover {{ border-color: #0078D4; }}

    </style>

    <div class="cloud-modules-container">
        <div class="header-section">
            <h2>Cloud Platforms</h2>
            <p>Explore projects and resources across major cloud providers</p>
        </div>

        <div class="modules-grid">
            <!-- AWS Module -->
            <div class="cloud-module-card aws" onclick="window.location.href='#'"> <!-- Placeholder link -->
                <div class="logo-container">
                    <img src="{aws_img}" alt="AWS" class="module-logo">
                </div>
                <div class="module-title">AWS</div>
                <div class="module-desc">Amazon Web Services architecture, serverless patterns, and infrastructure as code.</div>
                <div class="card-decoration"></div>
            </div>

            <!-- GCP Module -->
            <div class="cloud-module-card gcp" onclick="window.location.href='#'">
                <div class="logo-container">
                    <img src="{gcp_img}" alt="GCP" class="module-logo">
                </div>
                <div class="module-title">Google Cloud</div>
                <div class="module-desc">GCP native solutions, Kubernetes (GKE), and data analytics pipelines.</div>
                <div class="card-decoration"></div>
            </div>

            <!-- Azure Module -->
            <div class="cloud-module-card azure" onclick="window.location.href='#'">
                <div class="logo-container">
                    <img src="{azure_img}" alt="Azure" class="module-logo">
                </div>
                <div class="module-title">Azure</div>
                <div class="module-desc">Microsoft Azure enterprise solutions, DevOps integration, and hybrid cloud.</div>
                <div class="card-decoration"></div>
            </div>
        </div>
    </div>
    """
    return html
