# courses_devops.py
# DevOps Module (Advanced UI with Sub-Modules and Falling Animation)

import html

# Main Header Image
LOCAL_DEVOPS_IMG = "/images/devops.png"

# --- DATA STRUCTURE ---
# Define the hierarchy: Category -> Inner Services
DEVOPS_MODULES = [
    {
        "id": "version-control",
        "title": "Version Control System",
        "image": "/images/devops_images/Git Hub.png",
        "description": "Master the art of tracking code changes and collaborating.",
        "services": [
            {"name": "Git", "image": "/images/devops_images/git.png", "description": "Distributed version control system."},
            {"name": "GitHub", "image": "/images/devops_images/Git Hub.png", "description": "Cloud hosting for Git repositories."},
            {"name": "Bitbucket", "image": "/images/devops_images/bitbucket.png", "description": "Git solution for professional teams."}
        ]
    },
    {
        "id": "ci-cd",
        "title": "CI/CD Pipelines",
        "image": "/images/devops_images/CI CD.png",
        "description": "Automate your software delivery process.",
        "services": [
            {"name": "Jenkins", "image": "/images/devops_images/jenkins.png", "description": "Open source automation server."},
            {"name": "GitHub Actions", "image": "/images/devops_images/github_actions.png", "description": "CI/CD built into GitHub."},
            {"name": "GitLab CI", "image": "/images/devops_images/gitlab_ci.png", "description": "Continuous Integration built into GitLab."},
            {"name": "Argo CD", "image": "/images/devops_images/argo_cd.png", "description": "Declarative GitOps continuous delivery for Kubernetes."}
        ]
    },
    {
        "id": "docker",
        "title": "Docker & Containerization",
        "image": "/images/devops_images/docker.png",
        "description": "Build, ship, and run any app, anywhere.",
        "services": [
            {"name": "Docker Engine", "image": "/images/devops_images/docker.png", "description": "The industry standard for containers."},
            {"name": "Docker Compose", "image": "/images/devops_images/docker.png", "description": "Define and run multi-container Docker applications."}
        ]
    },
    {
        "id": "kubernetes",
        "title": "Container Orchestration",
        "image": "/images/devops_images/k8.png",
        "description": "Automate container deployment, scaling, and management.",
        "services": [
            {"name": "Kubernetes (K8s)", "image": "/images/devops_images/k8.png", "description": "Production-grade container orchestration."}
        ]
    },
    {
        "id": "iac-terraform",
        "title": "Infrastructure as Code",
        "image": "/images/devops_images/terraform.png",
        "description": "Provision and manage infrastructure using code.",
        "services": [
            {"name": "Terraform", "image": "/images/devops_images/terraform.png", "description": "Infrastructure as Code tool."}
        ]
    },
    {
        "id": "config-ansible",
        "title": "Configuration Management",
        "image": "/images/devops_images/ansible.webp",
        "description": "Automate IT configuration and management.",
        "services": [
            {"name": "Ansible", "image": "/images/devops_images/ansible.webp", "description": "Simple, agentless IT automation."}
        ]
    },
    {
        "id": "monitoring-logging",
        "title": "Monitoring & Logging",
        "image": "/images/devops_images/Monitoring.png",
        "description": "Gain insight into your applications and infrastructure.",
        "services": [
            {"name": "Prometheus", "image": "/images/devops_images/prometheus.png", "description": "Monitoring system and time series database."},
            {"name": "Grafana", "image": "/images/devops_images/grafana.png", "description": "Visualization and analytics platform."},
            {"name": "AWS CloudWatch", "image": "/images/devops_images/aws_cloudwatch.png", "description": "Monitoring for AWS resources."},
            {"name": "AWS CloudTrail", "image": "/images/devops_images/aws_cloudtrail.png", "description": "Track user activity and API usage."}
        ]
    },
    {
        "id": "devsecops",
        "title": "DevSecOps",
        "image": "/images/devops_images/DevSecOps.png",
        "description": "Integrating security practices within the DevOps process.",
        "services": [
             {"name": "Security Scanning", "image": "/images/devops_images/DevSecOps.png", "description": "SCA, SAST, and DAST tools."}
        ]
    },
    {
        "id": "scripting",
        "title": "Scripting",
        "image": "/images/devops_images/LINUX.png",
        "description": "Automate tasks using scripting languages.",
        "services": [
            {"name": "Bash", "image": "/images/devops_images/LINUX.png", "description": "Unix shell and command language."},
            {"name": "Python", "image": "/images/devops_images/LINUX.png", "description": "High-level programming language."}
        ]
    },
    {
        "id": "cloud-devops",
        "title": "Cloud DevOps",
        "image": "/images/devops_images/cloud.png",
        "description": "DevOps on major cloud providers.",
        "services": [
            {"name": "AWS", "image": "/images/devops_images/cloud.png", "description": "Amazon Web Services."},
            {"name": "Azure", "image": "/images/devops_images/cloud.png", "description": "Microsoft Azure."},
            {"name": "GCP", "image": "/images/devops_images/cloud.png", "description": "Google Cloud Platform."}
        ]
    }
]

def get_module(module_id):
    """Helper to find a module by ID"""
    for m in DEVOPS_MODULES:
        if m['id'] == module_id:
            return m
    return None

def _service_card_html(module):
    """
    Main Category Card (similar to AWS modern card)
    """
    sid = module['id']
    label = module['title']
    icon_url = module['image']
    href = f"/course/devops/{sid}"
    
    # Preview of inner services
    inner_list = module.get('services', [])
    topics_html = "".join([f"<li>{s['name']}</li>" for s in inner_list[:4]])
    if len(inner_list) > 4:
        topics_html += "<li>+ more...</li>"

    return f"""
    <a href="{href}" class="devops-card-modern">
        <div class="devops-card-icon">
            <img src="{icon_url}" alt="{label}">
        </div>
        <div class="devops-card-content">
            <h3 class="devops-card-title">{label}</h3>
            <ul class="devops-topic-list">
                {topics_html}
            </ul>
            <div class="devops-card-arrow">→</div>
        </div>
    </a>
    """

def render():
    """Main DevOps page"""
    cards_html = "".join([_service_card_html(m) for m in DEVOPS_MODULES])

    return f"""
    <style>
        /* --- Shared Animations (reused from AWS for consistency) --- */
        @keyframes slideInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes rotateHero {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}

        .devops-wrapper {{
            font-family: 'Inter', sans-serif;
            color: #232f3e;
            max-width: 1200px;
            margin: 0 auto;
        }}

        /* --- Hero Section --- */
        .devops-hero {{
            background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
            border-radius: 24px;
            padding: 40px;
            color: #fff;
            position: relative;
            overflow: hidden;
            margin-bottom: 40px;
            box-shadow: 0 20px 40px rgba(15, 23, 42, 0.2);
            display: flex;
            align-items: center;
            gap: 30px;
        }}
        
        .devops-hero-icon img {{
             width: 110px; height: 110px; 
             object-fit: cover;
             border-radius: 50%;
             border: 4px solid #fff;
             box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);
             animation: rotateHero 20s linear infinite;
        }}

        .devops-hero-text h1 {{
            font-size: 2.8rem;
            font-weight: 800;
            margin: 0 0 10px 0;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .devops-hero-text p {{
            font-size: 1.15rem;
            color: #cbd5e1;
            max-width: 600px;
            line-height: 1.6;
        }}

        /* --- Grid --- */
        .devops-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 24px;
        }}

        /* --- Modern Card --- */
        .devops-card-modern {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 24px;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            gap: 16px;
            transition: all 0.3s ease;
            position: relative;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            animation: slideInUp 0.5s ease-out backwards;
        }}
        .devops-card-modern:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            border-color: #38bdf8;
        }}
        
        .devops-card-icon {{
            width: 56px; height: 56px;
            background: #f0f9ff;
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            padding: 8px;
        }}
        .devops-card-icon img {{ width: 100%; height: 100%; object-fit: contain; }}

        .devops-card-title {{
            margin: 0; font-size: 1.25rem; font-weight: 700; color: #0f172a;
        }}
        
        .devops-topic-list {{
            margin: 0; padding-left: 18px; font-size: 0.9rem; color: #64748b; line-height: 1.6;
        }}
        
        .devops-card-arrow {{
            margin-top: auto; align-self: flex-end; color: #38bdf8; font-weight: bold;
            opacity: 0; transform: translateX(-10px); transition: all 0.3s ease;
        }}
        .devops-card-modern:hover .devops-card-arrow {{ opacity: 1; transform: translateX(0); }}

    </style>

    <div class="devops-wrapper">
        <div class="devops-hero">
            <div class="devops-hero-icon">
                <img src="{LOCAL_DEVOPS_IMG}" alt="DevOps">
            </div>
            <div class="devops-hero-text">
                <h1>DevOps Mastery</h1>
                <p>Master the end-to-end software delivery lifecycle with industry-standard tools and practices.</p>
            </div>
        </div>

        <div class="devops-grid">
            {cards_html}
        </div>
    </div>
    """

def render_service(service_id):
    """
    Detailed View for a Main DevOps Module (e.g. CI/CD)
    Displays inner services (Jenkins, GitLab CI, etc.) falling from top.
    """
    sid = (service_id or "").lower().strip()
    module = get_module(sid)
    
    if not module:
        return f"<div style='padding:40px;text-align:center;'><h2>Module Not Found</h2><a href='/course/devops'>Back to DevOps</a></div>"

    label = module['title']
    icon = module['image']
    description = module.get('description', '')

    # Generate Inner Services Grid with falling animation
    services_html = ""
    for i, svc in enumerate(module.get('services', [])):
        # Staggered animation delay
        delay = i * 0.2  # 200ms sequence
        
        # Simple content placeholder for modal (can be expanded later)
        safe_content = html.escape(f"<h3>{svc['name']}</h3><p>{svc['description']}</p>")
        key = f"svc-{i}"

        services_html += f"""
        <div class="inner-service-card" style="animation-delay: {delay}s;" onclick="openDevOpsModal('{key}', '{html.escape(svc['name'])}')">
            <div class="inner-service-icon">
                <img src="{svc['image']}" alt="{svc['name']}">
            </div>
            <div class="inner-service-info">
                <h4>{svc['name']}</h4>
                <p>{svc['description']}</p>
            </div>
            <div id="content-{key}" style="display:none;">{safe_content}</div>
        </div>
        """

    return f"""
    <style>
        /* Animation Keyframes */
        @keyframes fallIn {{
            0% {{ opacity: 0; transform: translateY(-80px) scale(0.95); }}
            60% {{ transform: translateY(10px) scale(1.02); }}
            100% {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}
    
        .service-detail-wrap {{
            max-width: 1000px; margin: 20px auto; font-family: 'Inter', sans-serif; color: #1f2937;
        }}
        .service-header {{
            display: flex; align-items: center; gap: 24px; background: #fff;
            padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-bottom: 30px; border: 1px solid #f3f4f6; animation: fadeIn 0.6s ease-out;
        }}
        .service-icon {{
            width: 100px; height: 100px; padding: 10px; background: #f0f9ff;
            border-radius: 16px; display: flex; align-items: center; justify-content: center;
        }}
        .service-icon img {{ width:80%; height:80%; object-fit:contain; }}
        
        .inner-services-grid {{
            display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 20px; margin-top: 30px;
        }}

        .inner-service-card {{
            background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px;
            padding: 20px; text-align: center; cursor: pointer;
            display: flex; flex-direction: column; align-items: center; gap: 12px;
            
            /* Animation Properties */
            opacity: 0; 
            animation: fallIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .inner-service-card:hover {{
            transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.08); border-color: #38bdf8;
        }}
        
        .inner-service-icon {{ width: 100%; height: 80px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; }}
        .inner-service-icon img {{ max-width: 100%; height: 100%; object-fit: contain; }}

        .inner-service-info h4 {{ margin: 0 0 6px 0; font-size: 1rem; color: #0f172a; }}
        .inner-service-info p {{ margin: 0; font-size: 0.85rem; color: #64748b; line-height: 1.4; }}
        
        /* Modal Styles (Shared) */
        .devops-overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(15,23,42,0.85); z-index: 2000; display: none; align-items: center; justify-content: center; padding: 20px; backdrop-filter: blur(5px); }}
        .devops-modal {{ background: #fff; width: 100%; max-width: 600px; max-height: 80vh; border-radius: 20px; display: flex; flex-direction: column; box-shadow: 0 25px 70px rgba(0,0,0,0.5); }}
        .devops-modal-header {{ padding: 20px 30px; border-bottom: 1px solid #f1f5f9; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; border-radius: 20px 20px 0 0; }}
        .devops-modal-body {{ padding: 30px; overflow-y: auto; line-height: 1.6; color: #334155; }}

    </style>

    <div class="service-detail-wrap">
        <div class="service-header">
            <div class="service-icon">
                <img src="{icon}" alt="{label}">
            </div>
            <div>
                <h1 style="margin:0; font-size:2rem; color:#0f172a;">{label}</h1>
                <p style="margin:8px 0 0 0; color:#64748b; font-weight:500;">DevOps Module</p>
            </div>
        </div>

        <div class="inner-services-grid">
            {services_html}
        </div>
        
        <div style="margin-top:40px; border-top:1px solid #f3f4f6; padding-top:20px;">
             <a href="/course/devops" style="color:#64748b; text-decoration:none; font-weight:600;">⬅ Back to DevOps Modules</a>
        </div>
    </div>

    <!-- MODAL -->
    <div id="devops-modal" class="devops-overlay" onclick="closeDevOpsModal(event)">
        <div class="devops-modal">
            <div class="devops-modal-header">
                <div style="font-weight:800; font-size:1.2rem; color:#0f172a;" id="devops-modal-title">Details</div>
                <button onclick="closeDevOpsModal(null)" style="border:none; background:none; font-size:1.5rem; cursor:pointer;">×</button>
            </div>
            <div class="devops-modal-body" id="devops-modal-content"></div>
        </div>
    </div>

    <script>
        function openDevOpsModal(key, title) {{
            const contentDiv = document.getElementById('content-' + key);
            if (!contentDiv) return;
            const txt = document.createElement("textarea");
            txt.innerHTML = contentDiv.innerHTML;
            document.getElementById('devops-modal-title').innerText = title; 
            document.getElementById('devops-modal-content').innerHTML = txt.value;
            document.getElementById('devops-modal').style.display = 'flex';
        }}
        
        function closeDevOpsModal(e) {{
            if (e && !e.target.classList.contains('devops-overlay')) return;
            document.getElementById('devops-modal').style.display = 'none';
        }}
    </script>
    """
