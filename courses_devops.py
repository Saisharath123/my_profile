# courses_devops.py
# DevOps Module (Hierarchical Structure with Inner Modules)

import html

# Header image
LOCAL_DEVOPS_IMG = "/images/devops.png"

# --- DEVOPS MODULES DATA STRUCTURE ---
# Level 1: Categories (e.g., Version Control, CI/CD)
# Level 2: Inner Tools (e.g., Git, Jenkins)
DEVOPS_MODULES = [
    {
        "id": "version-control",
        "title": "Version Control System",
        "image": "/images/devops_images/Git Hub.png",  # Main category icon
        "description": "Manage code history and collaboration.",
        "tools": [
            {
                "id": "git",
                "name": "Git",
                "image": "/images/devops_images/git.png",
                "desc": "Distributed version control system."
            },
            {
                "id": "github",
                "name": "GitHub",
                "image": "/images/devops_images/Git Hub.png",
                "desc": "Platform for hosting and collaborating on Git repositories."
            },
            {
                "id": "bitbucket",
                "name": "Bitbucket",
                "image": "/images/devops_images/bitbucket.png",
                "desc": "Git solution for professional teams."
            }
        ]
    },
    {
        "id": "ci-cd",
        "title": "CI/CD",
        "image": "/images/devops_images/CI CD.png",
        "description": "Automate build, test, and deployment pipelines.",
        "tools": [
            {
                "id": "jenkins",
                "name": "Jenkins",
                "image": "/images/devops_images/jenkins.png",
                "desc": "Open source automation server."
            },
            {
                "id": "github-actions",
                "name": "GitHub Actions",
                "image": "/images/devops_images/github_actions.png",
                "desc": "CI/CD workflows directly in GitHub."
            },
            {
                "id": "gitlab-ci",
                "name": "GitLab CI",
                "image": "/images/devops_images/gitlab_ci.png",
                "desc": "Continuous Integration built into GitLab."
            },
            {
                "id": "argo-cd",
                "name": "Argo CD",
                "image": "/images/devops_images/argo_cd.png",
                "desc": "Declarative GitOps for Kubernetes."
            }
        ]
    },
    {
        "id": "docker",
        "title": "Docker & Containerization",
        "image": "/images/devops_images/docker.png",
        "description": "Containerize applications for consistency.",
        "tools": [
            {
                "id": "docker-tool",
                "name": "Docker",
                "image": "/images/devops_images/docker.png",
                "desc": "Build, ship, and run any app, anywhere."
            }
        ]
    },
    {
        "id": "kubernetes",
        "title": "Container Orchestration",
        "image": "/images/devops_images/k8.png",
        "description": "Manage containerized applications at scale.",
        "tools": [
            {
                "id": "k8s-tool",
                "name": "Kubernetes (K8s)",
                "image": "/images/devops_images/k8.png",
                "desc": "Automated container deployment, scaling, and management."
            }
        ]
    },
    {
        "id": "iac",
        "title": "Infrastructure as Code",
        "image": "/images/devops_images/terraform.png",
        "description": "Provision infrastructure through code.",
        "tools": [
            {
                "id": "terraform",
                "name": "Terraform",
                "image": "/images/devops_images/terraform.png",
                "desc": "Infrastructure as Code software tool."
            }
        ]
    },
    {
        "id": "config-mgmt",
        "title": "Configuration Management",
        "image": "/images/devops_images/ansible.webp",
        "description": "Automate IT configuration.",
        "tools": [
            {
                "id": "ansible",
                "name": "Ansible",
                "image": "/images/devops_images/ansible.webp",
                "desc": "Simple IT automation."
            }
        ]
    },
    {
        "id": "monitoring",
        "title": "Monitoring & Logging",
        "image": "/images/devops_images/Monitoring.png",
        "description": "Observability for your stack.",
        "tools": [
            {
                "id": "prometheus",
                "name": "Prometheus",
                "image": "/images/devops_images/prometheus.png",
                "desc": "Monitoring system & time series DB."
            },
            {
                "id": "grafana",
                "name": "Grafana",
                "image": "/images/devops_images/grafana.png",
                "desc": "Analytics and interactive visualization."
            },
            {
                "id": "aws-cloudwatch",
                "name": "AWS CloudWatch",
                "image": "/images/devops_images/aws_cloudwatch.png",
                "desc": "Monitoring for AWS resources."
            },
            {
                "id": "aws-cloudtrail",
                "name": "AWS CloudTrail",
                "image": "/images/devops_images/aws_cloudtrail.png",
                "desc": "User activity and API usage tracking."
            }
        ]
    },
    {
        "id": "devsecops",
        "title": "DevSecOps",
        "image": "/images/devops_images/DevSecOps.png",
        "description": "Security in CI/CD pipelines.",
        "tools": [
            {
                "id": "sec-pipeline",
                "name": "Security in CI/CD",
                "image": "/images/devops_images/DevSecOps.png",
                "desc": "Shift-left security practices."
            }
        ]
    },
    {
        "id": "scripting",
        "title": "Scripting",
        "image": "/images/devops_images/LINUX.png",
        "description": "Automate tasks using scripts.",
        "tools": [
            {
                "id": "linux-script",
                "name": "Linux",
                "image": "/images/devops_images/LINUX.png",
                "desc": "Operating system and CLI."
            },
            {
                "id": "bash-script",
                "name": "Bash",
                "image": "/images/devops_images/bash.png",
                "desc": "Unix shell and command language."
            },
            {
                "id": "python-script",
                "name": "Python",
                "image": "/images/devops_images/python.png",
                "desc": "High-level programming language."
            }
        ]
    },
    {
        "id": "cloud-devops",
        "title": "Cloud DevOps",
        "image": "/images/devops_images/cloud.png",
        "description": "AWS, Azure, and GCP.",
        "tools": [
            {
                "id": "aws-cloud",
                "name": "AWS",
                "image": "/images/devops_images/cloud.png",
                "desc": "Amazon Web Services."
            },
            {
                "id": "azure-cloud",
                "name": "Azure",
                "image": "/images/devops_images/azure.png",
                "desc": "Microsoft Azure."
            },
            {
                "id": "gcp-cloud",
                "name": "GCP",
                "image": "/images/devops_images/gcp.png",
                "desc": "Google Cloud Platform."
            }
        ]
    }
]

def get_module_by_id(mid):
    for m in DEVOPS_MODULES:
        if m['id'] == mid:
            return m
    return None

def _render_category_card(module):
    """
    Renders the Main Category Card.
    """
    sid = module['id']
    label = module['title']
    icon_url = module['image']
    href = f"/course/devops/{sid}"
    
    # Preview inner tools in list
    tools_list = [t['name'] for t in module.get('tools', [])]
    preview_html = "".join([f"<li>{t}</li>" for t in tools_list[:3]])
    if len(tools_list) > 3:
        preview_html += "<li>+ more...</li>"

    return f"""
    <a href="{href}" class="devops-card-modern">
        <div class="devops-card-icon">
            <img src="{icon_url}" alt="{label}">
        </div>
        <div class="devops-card-content">
            <h3 class="devops-card-title">{label}</h3>
            <ul class="devops-topic-list">
                {preview_html}
            </ul>
            <div class="devops-card-arrow">→</div>
        </div>
    </a>
    """

def render():
    """Main DevOps page with Grid of Categories"""
    cards_html = "".join([_render_category_card(m) for m in DEVOPS_MODULES])

    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        
        .devops-wrapper {{
            font-family: 'Inter', sans-serif;
            color: #232f3e;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        /* Hero Section */
        .devops-hero {{
            background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
            border-radius: 24px;
            padding: 40px;
            color: #fff;
            position: relative;
            overflow: hidden;
            margin-bottom: 40px;
            display: flex; align-items: center; gap: 30px;
            box-shadow: 0 20px 40px rgba(15, 23, 42, 0.2);
        }}
        .devops-hero-icon img {{
             width: 110px; height: 110px; 
             object-fit: cover; border-radius: 50%; border: 4px solid #fff;
             box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);
             animation: rotateHero 20s linear infinite;
        }}
        @keyframes rotateHero {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}

        .devops-hero-text h1 {{
            font-size: 2.8rem; font-weight: 800; margin: 0 0 10px 0;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .devops-hero-text p {{
            font-size: 1.15rem; color: #cbd5e1; max-width: 600px; line-height: 1.6;
        }}

        /* Grid */
        .devops-grid {{
            display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px;
        }}

        /* Modern Card */
        .devops-card-modern {{
            background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px;
            padding: 24px; text-decoration: none; color: inherit;
            display: flex; flex-direction: column; gap: 16px; position: relative;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }}
        .devops-card-modern:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            border-color: #38bdf8;
        }}
        .devops-card-icon {{
            width: 56px; height: 56px; background: #f0f9ff; border-radius: 12px;
            display: flex; align-items: center; justify-content: center; padding: 8px;
        }}
        .devops-card-icon img {{ width: 100%; height: 100%; object-fit: contain; }}

        .devops-card-title {{ margin: 0; font-size: 1.25rem; font-weight: 700; color: #0f172a; }}
        .devops-topic-list {{ margin: 0; padding-left: 18px; font-size: 0.9rem; color: #64748b; line-height: 1.6; }}
        
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
                <p>Advanced DevOps practices: Version Control, CI/CD, Containers, IaC, and Cloud.</p>
            </div>
        </div>

        <div class="devops-grid">
            {cards_html}
        </div>
    </div>
    """

def render_service(service_id):
    """
    Displays the Inner Tools for a selected Category (e.g. CI/CD -> Jenkins, GitHub Actions...)
    """
    sid = (service_id or "").lower().strip()
    module = get_module_by_id(sid)
    
    if not module:
        return f"<div style='padding:40px;text-align:center;'><h2>Category Not Found</h2><a href='/course/devops'>Back to DevOps</a></div>"

    label = module['title']
    icon = module['image']
    desc = module['description']

    # Generate Inner Tools Cards
    tools_html = ""
    for i, tool in enumerate(module.get('tools', [])):
        # Falling animation delay
        delay = i * 0.2
        key = f"tool-{i}"
        
        # Placeholder content for potential modal (reusing generic description for now)
        safe_content = html.escape(f"<h3>{tool['name']}</h3><p>{tool['desc']}</p>")
        
        tools_html += f"""
        <div class="inner-tool-card" style="animation-delay: {delay}s;" onclick="openToolModal('{key}', '{html.escape(tool['name'])}')">
            <div class="inner-tool-icon">
                <img src="{tool['image']}" alt="{tool['name']}">
            </div>
            <div class="inner-tool-info">
                <h4>{tool['name']}</h4>
                <p>{tool['desc']}</p>
            </div>
            <div id="content-{key}" style="display:none;">{safe_content}</div>
        </div>
        """

    return f"""
    <style>
        .service-detail-wrap {{ max-width: 1000px; margin: 20px auto; font-family: 'Inter', sans-serif; color: #1f2937; }}
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
        
        @keyframes fadeIn {{ from {{ opacity:0; transform:translateY(10px); }} to {{ opacity:1; transform:translateY(0); }} }}

        /* Inner Grid */
        .inner-tools-grid {{
            display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 20px; margin-top: 30px;
        }}

        /* Tool Card with Falling Animation */
        @keyframes fallIn {{
            0% {{ opacity: 0; transform: translateY(-80px) scale(0.95); }}
            60% {{ transform: translateY(10px) scale(1.02); }}
            100% {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}

        .inner-tool-card {{
            background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px;
            padding: 20px; text-align: center; cursor: pointer;
            display: flex; flex-direction: column; align-items: center; gap: 12px;
            
            opacity: 0;
            animation: fallIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .inner-tool-card:hover {{
            transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.08); border-color: #38bdf8;
        }}
        
        .inner-tool-icon {{ width: 100%; height: 80px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; }}
        .inner-tool-icon img {{ max-width: 100%; height: 100%; object-fit: contain; }}

        .inner-tool-info h4 {{ margin: 0 0 6px 0; font-size: 1rem; color: #0f172a; }}
        .inner-tool-info p {{ margin: 0; font-size: 0.85rem; color: #64748b; line-height: 1.4; }}

        /* Modal Styles */
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
                <p style="margin:8px 0 0 0; color:#64748b; font-weight:500;">{desc}</p>
            </div>
        </div>
        
        <h3 style="border-bottom:1px solid #e2e8f0; padding-bottom:10px; margin-top:30px;">Included Tools & Technologies</h3>
        <div class="inner-tools-grid">
            {tools_html}
        </div>
        
        <div style="margin-top:40px; border-top:1px solid #f3f4f6; padding-top:20px;">
             <a href="/course/devops" style="color:#64748b; text-decoration:none; font-weight:600;">⬅ Back to Categories</a>
        </div>
    </div>

    <!-- MODAL -->
    <div id="devops-modal" class="devops-overlay" onclick="closeToolModal(event)">
        <div class="devops-modal">
            <div class="devops-modal-header">
                <div style="font-weight:800; font-size:1.2rem; color:#0f172a;" id="devops-modal-title">Details</div>
                <button onclick="closeToolModal(null)" style="border:none; background:none; font-size:1.5rem; cursor:pointer;">×</button>
            </div>
            <div class="devops-modal-body" id="devops-modal-content"></div>
        </div>
    </div>

    <script>
        function openToolModal(key, title) {{
            const contentDiv = document.getElementById('content-' + key);
            if (!contentDiv) return;
            const txt = document.createElement("textarea");
            txt.innerHTML = contentDiv.innerHTML;
            document.getElementById('devops-modal-title').innerText = title; 
            document.getElementById('devops-modal-content').innerHTML = txt.value;
            document.getElementById('devops-modal').style.display = 'flex';
        }}
        
        function closeToolModal(e) {{
            if (e && !e.target.classList.contains('devops-overlay')) return;
            document.getElementById('devops-modal').style.display = 'none';
        }}
    </script>
    """

def get_course_html():
    return render()
