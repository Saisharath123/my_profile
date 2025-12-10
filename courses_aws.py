# courses_aws.py
# AWS Solution Architect module (Advanced UI)
# Exposes:
#   - render() -> HTML string (main AWS page)
#   - render_service(service) -> HTML string (service detail pages)

from backend_aws import AWS_MODULES, get_module

def _service_card_modern(module, idx=0):
    """
    Renders a single service card (Category) with glassmorphism and hover effects.
    """
    sid = module['id']
    label = module['title']
    icon_url = module['image']
    
    # Get top 4 inner services for the preview list
    inner_list = module.get('services', [])
    topics_html = "".join([f"<li>{s['name']}</li>" for s in inner_list[:4]])
    if len(inner_list) > 4:
        topics_html += "<li>+ more...</li>"

    delay = f"{idx * 0.05}s"
    href = f"/course/aws/{sid}"
    
    return f"""
    <a href="{href}" class="aws-card-modern" style="animation-delay: {delay};">
        <div class="aws-card-icon">
            <img src="{icon_url}" alt="{label}">
        </div>
        <div class="aws-card-content">
            <h3 class="aws-card-title">{label}</h3>
            <ul class="aws-topic-list">
                {topics_html}
            </ul>
            <div class="aws-card-arrow">→</div>
        </div>
    </a>
    """

def render():
    """Main AWS page with Tabbed UI and Modern styling."""
    
    # Generate cards from AWS_MODULES
    cards_html = "".join([_service_card_modern(m, i) for i, m in enumerate(AWS_MODULES)])

    return f"""
    <style>
        /* --- Shared Animations --- */
        @keyframes slideInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        /* --- Layout --- */
        .aws-wrapper {{
            font-family: 'Inter', sans-serif;
            color: #232f3e;
            max-width: 1200px;
            margin: 0 auto;
        }}

        /* --- Hero Section --- */
        .aws-hero {{
            background: linear-gradient(135deg, #232f3e 0%, #37475a 100%);
            border-radius: 20px;
            padding: 40px;
            color: #fff;
            position: relative;
            overflow: hidden;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(35, 47, 62, 0.2);
        }}

        .aws-hero-content {{ display: flex; align-items: center; gap: 30px; position: relative; z-index: 2; }}

        .aws-logo-img {{
            width: 110px; height: 110px; object-fit: contain;
            filter: drop-shadow(0 0 15px rgba(255, 153, 0, 0.3));
            animation: floatLogo 4s ease-in-out infinite;
        }}

        .aws-hero after {{
            content: '';
            position: absolute;
            top: 0; right: 0; bottom: 0; left: 0;
            background-image: radial-gradient(circle at 80% 20%, rgba(255, 153, 0, 0.15) 0%, transparent 40%);
            pointer-events: none;
        }}

        .aws-hero h1 {{
            font-size: 2.8rem;
            font-weight: 800;
            margin: 0 0 12px 0;
            background: linear-gradient(to right, #ff9900, #ffc470, #ffd59e, #ff9900);
            background-size: 300% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textShine 4s linear infinite;
        }}

        .aws-hero p {{
            font-size: 1.15rem;
            color: #d1d5db;
            max-width: 700px;
            line-height: 1.6;
        }}

        @keyframes textShine {{ to {{ background-position: 200% center; }} }}
        @keyframes floatLogo {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-8px); }} }}

        /* --- Tabs --- */
        .aws-tabs {{
            display: flex;
            gap: 16px;
            margin-bottom: 32px;
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 2px;
        }}

        .aws-tab-btn {{
            background: transparent;
            border: none;
            padding: 12px 20px;
            font-size: 1rem;
            font-weight: 600;
            color: #4b5563;
            cursor: pointer;
            position: relative;
            transition: color 0.2s;
        }}

        .aws-tab-btn:hover {{ color: #ff9900; }}
        .aws-tab-btn.active {{ color: #ec7211; }}
        
        .aws-tab-btn.active::after {{
            content: '';
            position: absolute;
            bottom: -3px; left: 0; right: 0;
            height: 3px;
            background: #ff9900;
            border-radius: 3px 3px 0 0;
        }}

        .aws-tab-content {{ display: none; animation: fadeIn 0.4s ease-out; }}
        .aws-tab-content.active {{ display: block; }}

        /* --- Services Grid --- */
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }}

        .aws-card-modern {{
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 24px;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            gap: 16px;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            position: relative;
            animation: slideInUp 0.5s ease-out backwards;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }}

        .aws-card-modern:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border-color: #ff9900;
        }}

        .aws-card-icon {{
            width: 56px; height: 56px;
            background: #fdfaf5;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
            box-sizing: border-box;
        }}
        .aws-card-icon img {{ width: 100%; height: 100%; object-fit: contain; }}

        .aws-card-title {{
            margin: 0;
            font-size: 1.15rem;
            font-weight: 700;
            color: #232f3e;
        }}

        .aws-topic-list {{
            margin: 0;
            padding-left: 18px;
            font-size: 0.9rem;
            color: #6b7280;
            line-height: 1.5;
        }}

        .aws-card-arrow {{
            margin-top: auto;
            align-self: flex-end;
            color: #ff9900;
            font-weight: bold;
            opacity: 0;
            transform: translateX(-10px);
            transition: all 0.3s ease;
        }}
        .aws-card-modern:hover .aws-card-arrow {{
            opacity: 1;
            transform: translateX(0);
        }}

        /* --- Roadmap (Timeline) --- */
        .roadmap-container {{
            position: relative;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px 0;
        }}
        .roadmap-container::before {{
            content: '';
            position: absolute;
            left: 20px; top: 0; bottom: 0;
            width: 4px;
            background: #e5e7eb;
            border-radius: 2px;
        }}
        .roadmap-item {{
            position: relative;
            padding-left: 60px;
            margin-bottom: 40px;
        }}
        .roadmap-marker {{
            position: absolute;
            left: 10px; top: 0;
            width: 24px; height: 24px;
            background: #232f3e;
            border: 4px solid #fff;
            box-shadow: 0 0 0 4px #ff9900;
            border-radius: 50%;
            z-index: 2;
        }}
        .roadmap-content {{
            background: #fff;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #f3f4f6;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }}
        .roadmap-week {{
            font-size: 0.85rem;
            color: #d97706;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
            display: block;
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .aws-hero h1 {{ font-size: 2rem; }}
            .roadmap-container::before {{ left: 16px; }}
            .roadmap-item {{ padding-left: 50px; }}
            .roadmap-marker {{ left: 6px; }}
        }}
    </style>

    <div class="aws-wrapper">
        <div class="aws-hero">
            <div class="aws-hero-content">
                <img src="/images/AWS.png" alt="AWS" class="aws-logo-img">
                <div>
                    <h1>AWS Solution Architect</h1>
                    <p>
                        Master the world's leading cloud platform. Designed for aspiring architects to build 
                        scalable, highly available, and fault-tolerant systems on the AWS Cloud.
                    </p>
                </div>
            </div>
        </div>

        <div class="aws-tabs">
            <button class="aws-tab-btn active" onclick="openAwsTab('services')">Services Explorer</button>
            <button class="aws-tab-btn" onclick="openAwsTab('roadmap')">Certification Path</button>
        </div>

        <!-- Tab 1: Services Explorer -->
        <div id="services" class="aws-tab-content active">
            <div class="services-grid">
                {cards_html}
            </div>
        </div>

        <!-- Tab 2: Roadmap -->
        <div id="roadmap" class="aws-tab-content">
            <div class="roadmap-container">
                <div class="roadmap-item">
                    <div class="roadmap-marker"></div>
                    <div class="roadmap-content">
                        <span class="roadmap-week">Weeks 1-2</span>
                        <h3 style="margin:0 0 8px 0;">Cloud Foundations & IAM</h3>
                        <p style="margin:0;color:#4b5563;">
                            Understand the AWS Global Infrastructure (regions, AZs). Deep dive into Identity and Access Management (IAM) to secure your environment from Day 1.
                        </p>
                    </div>
                </div>
                <div class="roadmap-item">
                    <div class="roadmap-marker"></div>
                    <div class="roadmap-content">
                        <span class="roadmap-week">Weeks 3-4</span>
                        <h3 style="margin:0 0 8px 0;">Core Services: Compute & Networking</h3>
                        <p style="margin:0;color:#4b5563;">
                            Launch EC2 instances, configure VPCs, Subnets, and Route Tables. Master Security Groups and NACLs effectively.
                        </p>
                    </div>
                </div>
                <div class="roadmap-item">
                    <div class="roadmap-marker"></div>
                    <div class="roadmap-content">
                        <span class="roadmap-week">Weeks 5-6</span>
                        <h3 style="margin:0 0 8px 0;">Storage & Databases</h3>
                        <p style="margin:0;color:#4b5563;">
                            Deep dive into S3 storage classes and lifecycle policies. Provision RDS and DynamoDB databases for varied use-cases.
                        </p>
                    </div>
                </div>
                <div class="roadmap-item">
                    <div class="roadmap-marker"></div>
                    <div class="roadmap-content">
                        <span class="roadmap-week">Weeks 7-8</span>
                        <h3 style="margin:0 0 8px 0;">High Availability & Architecture</h3>
                        <p style="margin:0;color:#4b5563;">
                            Implement Load Balancers, Auto Scaling Groups, and Route53. Design decoupled architectures using SQS and SNS.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div style="margin-top:40px; text-align:center;">
             <a href="/courses" style="color:#3b82f6; text-decoration:none; font-weight:700; font-size:0.95rem;">⬅ Back to All Courses</a>
        </div>
    </div>

    <script>
        function openAwsTab(tabName) {{
            var i;
            var x = document.getElementsByClassName("aws-tab-content");
            for (i = 0; i < x.length; i++) {{
                x[i].style.display = "none";
                x[i].classList.remove("active");
            }}
            document.getElementById(tabName).style.display = "block";
            
            var btns = document.getElementsByClassName("aws-tab-btn");
            for (i = 0; i < btns.length; i++) {{
                btns[i].classList.remove("active");
            }}
            event.currentTarget.classList.add("active");
        }}
    </script>
    """

def render_service(service_id: str):
    """
    Detailed Service View with upgraded visuals consistent with the main module.
    Dynamically renders inner modules (services) from backend data.
    """
    sid = (service_id or "").lower().strip()
    module = get_module(sid)
    
    if not module:
        return f"<div style='padding:40px;text-align:center;'><h2>Service Not Found</h2><a href='/course/aws'>Back to AWS Module</a></div>"
    
    label = module['title']
    icon = module['image']
    description = module.get('description', '')
    
    # Generate Inner Services Grid
    services_html = ""
    
    # We need a way to store content safely.
    import html
    
    for i, svc in enumerate(module.get('services', [])):
        # Create a unique key for js
        key = f"svc-{i}"
        
        # Safe content for injection
        raw_content = svc.get('content', '')
        if not raw_content:
             raw_content = f"<p><em>No detailed content available for {svc['name']} yet.</em></p>"
        
        safe_content = html.escape(raw_content)
        
        # Staggered animation delay
        delay = i * 0.25  # 250ms delay per card for a clear "one by one" sequence
        
        services_html += f"""
        <div class="inner-service-card" style="animation-delay: {delay}s;" onclick="openAwsModal('{key}', '{html.escape(svc['name'])}')">
            <div class="inner-service-icon">
                <img src="{svc['image']}" alt="{svc['name']}">
            </div>
            <div class="inner-service-info">
                <h4>{svc['name']}</h4>
                <p>{svc['description']}</p>
            </div>
            <!-- Hidden Content -->
            <div id="content-{key}" style="display:none;">{safe_content}</div>
        </div>
        """

    return f"""
    <style>
        /* Animation Keyframes */
        @keyframes fallIn {{
            0% {{
                opacity: 0;
                transform: translateY(-80px) scale(0.95);
            }}
            60% {{
                transform: translateY(10px) scale(1.02);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0) scale(1);
            }}
        }}
    
        .service-detail-wrap {{
            max-width: 1000px;
            margin: 20px auto;
            font-family: 'Inter', sans-serif;
            color: #1f2937;
        }}
        .service-header {{
            display: flex;
            align-items: center;
            gap: 24px;
            background: #fff;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-bottom: 30px;
            border: 1px solid #f3f4f6;
            animation: fadeIn 0.6s ease-out;
        }}
        .service-icon {{
            width: 100px; height: 100px;
            flex-shrink: 0;
            padding: 10px;
            background: #fff7ed;
            border-radius: 16px;
            display: flex; align-items: center; justify-content: center;
        }}
        .service-icon img {{ width:80%; height:80%; object-fit:contain; }}
        
        .service-intro {{
            margin-bottom: 40px;
            line-height: 1.6;
            color: #4b5563;
            font-size: 1.1rem;
            animation: fadeIn 0.8s ease-out;
        }}

        .inner-services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}

        .inner-service-card {{
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            
            /* Animation Properties */
            opacity: 0; /* start invisible */
            animation: fallIn 1s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }}
        .inner-service-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.08);
            border-color: #ff9900;
        }}
        
        .inner-service-icon {{
            width: 100%; height: 100px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .inner-service-icon img {{
            max-width: 100%; height: 100%; object-fit: contain;
            display: block; 
        }}

        .inner-service-info h4 {{
            margin: 0 0 6px 0;
            font-size: 1rem;
            color: #111827;
        }}
        .inner-service-info p {{
            margin: 0;
            font-size: 0.85rem;
            color: #6b7280;
            line-height: 1.4;
        }}

        .btn-enroll {{
            display: inline-block;
            background: #ff9900;
            color: #fff;
            padding: 12px 30px;
            font-weight: 700;
            border-radius: 8px;
            text-decoration: none;
            margin-top: 20px;
            transition: background 0.2s;
        }}
        .btn-enroll:hover {{ background: #ec7211; }}

        /* Modal Styles */
        .aws-overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(15,23,42,0.85); z-index: 2000; display: none; align-items: center; justify-content: center; padding: 20px; backdrop-filter: blur(5px); }}
        .aws-modal {{ background: #fff; width: 100%; max-width: 800px; max-height: 90vh; border-radius: 20px; display: flex; flex-direction: column; box-shadow: 0 25px 70px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); }}
        
        .aws-modal-header {{ 
            padding: 24px 30px; 
            border-bottom: 1px solid #f1f5f9; 
            display: flex; justify-content: space-between; align-items: center; 
            background: linear-gradient(to right, #ffffff, #fff7ed); 
            border-radius: 20px 20px 0 0; 
        }}
        #aws-modal-title {{ font-weight: 800; font-size: 1.4rem; background: linear-gradient(90deg, #232f3e, #d97706); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

        .aws-modal-body {{ padding: 40px; overflow-y: auto; line-height: 1.7; color: #334155; font-size: 1.05rem; }}
        
        /* Enhanced Typography */
        .aws-modal-body h3 {{
            font-size: 1.6rem;
            margin: 20px 0 15px 0;
            color: #0f172a;
            position: relative;
            padding-bottom: 8px;
            border-bottom: 2px solid #fdba74;
            display: inline-block;
        }}
        
        /* Graphical List Points */
        .aws-modal-body ul {{
            list-style: none;
            padding: 0;
            margin: 25px 0;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
        }}
        .aws-modal-body li {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 16px 20px;
            border-radius: 12px;
            border-left: 5px solid #ff9900;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);
            transition: all 0.2s ease;
            position: relative;
        }}
        .aws-modal-body li:hover {{
            transform: translateY(-3px) scale(1.01);
            box-shadow: 0 10px 20px -5px rgba(255, 153, 0, 0.2);
            border-color: #fdba74;
            border-left-color: #ea580c;
        }}
        .aws-modal-body li strong {{ color: #ea580c; font-weight: 700; }}

        /* Code Blocks */
        .code-block {{ 
            background: #1e293b; 
            padding: 20px; 
            border-radius: 12px; 
            margin: 25px 0; 
            box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);
            border: 1px solid #334155;
            position: relative;
        }}
        .code-block::before {{
            content: 'CODE';
            position: absolute;
            top: 0; right: 0;
            background: #334155;
            color: #94a3b8;
            font-size: 0.7rem;
            padding: 4px 10px;
            border-radius: 0 12px 0 12px;
            font-weight: bold;
        }}
        .aws-modal-body pre {{ 
            background: transparent; 
            color: #e2e8f0; 
            padding: 0; 
            margin: 0; 
            font-family: 'Fira Code', 'Consolas', monospace; 
            font-size: 0.9rem;
            overflow-x: auto;
        }}
    </style>

    <div class="service-detail-wrap">
        <div class="service-header">
            <div class="service-icon">
                <img src="{icon}" alt="{label}">
            </div>
            <div>
                <h1 style="margin:0; font-size:2rem; color:#232f3e;">{label}</h1>
                <p style="margin:8px 0 0 0; color:#6b7280; font-weight:500;">AWS Solution Architect Module</p>
            </div>
        </div>

        <div class="service-body">
            <div class="service-intro">
                <p>{description}</p>
            </div>
            
            <h3 style="border-bottom: 2px solid #f3f4f6; padding-bottom: 10px; margin-bottom: 20px;">Included Services</h3>
            <div class="inner-services-grid">
                {services_html}
            </div>
            
            <div style="margin-top:40px; border-top:1px solid #f3f4f6; padding-top:20px;">
                <a href="/contact" class="btn-enroll">Enroll / Request Demo</a>
                <a href="/course/aws" style="margin-left:20px; color:#4b5563; text-decoration:none; font-weight:600;">⬅ Back to Services</a>
            </div>
        </div>
    </div>

    <!-- MODAL -->
    <div id="aws-modal" class="aws-overlay" onclick="closeAwsModal(event)">
        <div class="aws-modal">
            <div class="aws-modal-header">
                <div style="font-weight:800; font-size:1.2rem;" id="aws-modal-title">Service Details</div>
                <button onclick="closeAwsModal(null)" style="border:none; background:none; font-size:1.5rem; cursor:pointer;">×</button>
            </div>
            <div class="aws-modal-body" id="aws-modal-content"></div>
        </div>
    </div>

    <script>
        function openAwsModal(key, title) {{
            const contentDiv = document.getElementById('content-' + key);
            if (!contentDiv) return;
            
            // Decode HTML entities
            const txt = document.createElement("textarea");
            txt.innerHTML = contentDiv.innerHTML;
            
            document.getElementById('aws-modal-title').innerText = title; 
            document.getElementById('aws-modal-content').innerHTML = txt.value;
            document.getElementById('aws-modal').style.display = 'flex';
        }}
        
        function closeAwsModal(e) {{
            if (e && !e.target.classList.contains('aws-overlay')) return;
            document.getElementById('aws-modal').style.display = 'none';
        }}
    </script>
    """
