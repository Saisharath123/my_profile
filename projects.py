# projects.py
# Projects module logic with Folder Metaphor
# Exposes: render(project_images) -> HTML string

from flask import url_for

# Rich metadata for known projects
PROJECT_CATALOG = {
    "aws_migration": {
        "title": "AWS Lift & Shift Migration",
        "tags": ["AWS", "DMS", "EC2"],
        "desc": "Zero-downtime migration of a monolithic app to AWS.",
        "category": "cloud"
    },
    "k8s_cluster": {
        "title": "EKS Cluster Automation",
        "tags": ["Kubernetes", "Terraform", "Helm"],
        "desc": "Fully automated EKS provisioning with Observability.",
        "category": "devops"
    },
    "ci_cd_pipeline": {
        "title": "Jenkins CI/CD Pipeline",
        "tags": ["Jenkins", "Docker", "Groovy"],
        "desc": "End-to-end pipeline for Docker build & deploy.",
        "category": "devops"
    },
    "serverless_api": {
        "title": "Serverless REST API",
        "tags": ["Lambda", "API Gateway", "DynamoDB"],
        "desc": "High-scale serverless backend.",
        "category": "cloud"
    },
    "portfolio_site": {
        "title": "Personal Portfolio",
        "tags": ["Flask", "HTML/CSS", "Python"],
        "desc": "The dynamic website you are looking at right now.",
        "category": "web"
    },
    # Fallback / Generic
    "project1": {"title": "Cloud Infra Demo", "tags": ["Cloud"], "desc": "Infrastructure demo.", "category": "cloud"},
    "project2": {"title": "DevOps Workflow", "tags": ["DevOps"], "desc": "Automation workflow snapshot.", "category": "devops"},
    "project3": {"title": "Web Dashboard", "tags": ["Web", "React"], "desc": "Analytics dashboard UI.", "category": "web"}
}

def render(project_images):
    """
    Render the projects page with Folder metaphor.
    """
    
    # Images for the folders
    cloud_img = url_for('image_file', filename='cloud.webp')
    devops_img = url_for('image_file', filename='devops.png')
    
    html = f"""
    <script>
        function filterProjects(category) {{
            const cards = document.querySelectorAll('.project-card');
            const folders = document.querySelectorAll('.folder');
            
            // Visual feedback on folders
            folders.forEach(f => {{
                f.style.opacity = '0.6';
                f.style.transform = 'scale(0.95)';
                f.style.border = '1px solid #cbd5e1';
                
                // Check if this folder is the selected category
                // We check the onclick attribute content or use a data attribute if we had it.
                // Simple check:
                if(f.getAttribute('onclick').includes("'" + category + "'")) {{
                    f.style.opacity = '1';
                    f.style.transform = 'scale(1.05) translateY(-5px)';
                    f.style.border = '2px solid #3b82f6';
                }}
            }});
            
            // Reset for 'all'
            if(category === 'all') {{
                folders.forEach(f => {{
                    f.style.opacity = '1';
                    f.style.transform = 'none';
                    f.style.border = '1px solid #cbd5e1';
                }});
            }}

            // Filter cards
            cards.forEach(card => {{
                const cat = card.getAttribute('data-category');
                if (category === 'all' || cat === category) {{
                    card.style.display = 'flex';
                    // Trigger simple fade in
                    card.style.animation = 'none';
                    card.offsetHeight; /* trigger reflow */
                    card.style.animation = 'fadeIn 0.5s ease forwards';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
    <style>
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .projects-header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        .projects-header h2 {{
             margin: 0 0 10px 0;
             font-size: 2.4rem;
             color: #1e293b;
             font-weight: 800;
        }}
        .projects-header p {{
            color: #64748b;
            font-size: 1.1rem;
        }}

        /* FOLDER CONTAINER */
        .folders-row {{
            display: flex;
            justify-content: center;
            gap: 32px;
            flex-wrap: wrap;
            margin-bottom: 48px;
        }}

        .folder {{
            width: 220px;
            height: 160px;
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            border-radius: 0 12px 12px 12px;
            position: relative;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border: 1px solid #cbd5e1;
            user-select: none;
        }}

        /* The tab styling */
        .folder::after {{
            content: '';
            position: absolute;
            top: -14px;
            left: 0;
            width: 90px;
            height: 14px;
            background: inherit; /* Match folder bg */
            border-radius: 8px 8px 0 0;
            border-top: 1px solid #cbd5e1;
            border-left: 1px solid #cbd5e1;
            border-right: 1px solid #cbd5e1;
            border-bottom: none; /* Seamless merge */
        }}

        .folder:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 30px rgba(0,0,0,0.1);
            background: linear-gradient(135deg, #fff 0%, #f1f5f9 100%);
        }}

        .folder-icon {{
            width: 64px;
            height: 64px;
            object-fit: contain;
            margin-bottom: 12px;
            z-index: 2;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
        }}
        
        .folder-label {{
            font-weight: 800;
            color: #334155;
            font-size: 1.1rem;
            z-index: 2;
        }}

        /* PROJECT GRID (Below folders) */
        .project-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 24px;
        }}

        .project-card {{
            background: #fff;
            border-radius: 12px;
            padding: 16px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            display: flex;
            gap: 12px;
            align-items: start;
            transition: transform 0.2s;
        }}
        
        .project-card:hover {{
            transform: translateY(-4px);
            border-color: #93c5fd;
        }}

        .project-thumb {{
            width: 80px;
            height: 80px;
            border-radius: 8px;
            object-fit: cover;
            background: #f1f5f9;
        }}

        .p-info h4 {{ margin: 0 0 4px 0; font-size: 1rem; color: #0f172a; }}
        .p-info p {{ margin: 0; font-size: 0.85rem; color: #64748b; line-height: 1.4; }}
        
        .p-tags {{ margin-top: 8px; display: flex; gap: 6px; flex-wrap: wrap; }}
        .p-tag {{ font-size: 0.7rem; background: #eff6ff; color: #2563eb; padding: 2px 8px; border-radius: 12px; font-weight: 600; }}

    </style>

    <div class="projects-wrapper">
        <div class="projects-header">
            <h2>Project Repository</h2>
            <p>Select a category to browse detailed case studies.</p>
            <button onclick="filterProjects('all')" style="margin-top:10px; padding:6px 12px; background:transparent; border:1px solid #cbd5e1; border-radius:20px; cursor:pointer; color:#64748b; font-size:0.9rem;">Show All</button>
        </div>

        <div class="folders-row">
            <!-- Cloud Folder -->
            <div class="folder" onclick="filterProjects('cloud')">
                <img src="{cloud_img}" alt="Cloud" class="folder-icon">
                <div class="folder-label">Cloud Projects</div>
            </div>

            <!-- DevOps Folder -->
            <div class="folder" onclick="filterProjects('devops')">
                <img src="{devops_img}" alt="DevOps" class="folder-icon">
                <div class="folder-label">DevOps Projects</div>
            </div>

            <!-- Web Folder -->
            <div class="folder" onclick="filterProjects('web')">
                <!-- Using inline SVG for Web if no image found, or generic web icon -->
                <svg class="folder-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="2" y="3" width="20" height="14" rx="2" stroke="#3b82f6" stroke-width="2"/>
                    <path d="M8 21h8" stroke="#3b82f6" stroke-width="2" stroke-linecap="round"/>
                    <path d="M12 17v4" stroke="#3b82f6" stroke-width="2" stroke-linecap="round"/>
                </svg>
                <div class="folder-label">Web Apps</div>
            </div>
        </div>
        
        <h3 style="margin-left:4px; margin-bottom:16px; color:#334155;">Latest Deployments</h3>
        
        <div class="project-grid">
    """
    
    # Render cards below folders
    if project_images:
        for p in project_images:
            img_url = url_for("image_file", filename=f"projects/{p}")
            key = p.rpartition('.')[0].lower()
            info = PROJECT_CATALOG.get(key)
            if not info:
                title = p.rpartition('.')[0].replace('_', ' ').replace('-', ' ').title()
                info = {"title": title, "desc": "Project implementation.", "tags": [], "category": "other"}
            
            tags_html = "".join([f'<span class="p-tag">{t}</span>' for t in info.get('tags',[])])
            category = info.get('category', 'other')
            
            html += f"""
            <div class="project-card" data-category="{category}">
                <img src="{img_url}" class="project-thumb" loading="lazy">
                <div class="p-info">
                    <h4>{info['title']}</h4>
                    <p>{info['desc']}</p>
                    <div class="p-tags">{tags_html}</div>
                </div>
            </div>
            """
    else:
        html += "<p style='color:#64748b; margin-left:8px;'>No specific project screenshots found.</p>"

    html += """
        </div>
    </div>
    """
    return html
