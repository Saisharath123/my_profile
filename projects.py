# projects.py
# Projects module logic with Portfolio Catalog
# Exposes: render(project_images) -> HTML string

from flask import url_for

# Rich metadata for known projects. 
# Keys should match filenames (without extension) if possible, 
# or we will fallback to generic display for unknown files.
PROJECT_CATALOG = {
    "aws_migration": {
        "title": "AWS Lift & Shift Migration",
        "tags": ["AWS", "DMS", "EC2"],
        "desc": "Zero-downtime migration of a monolithic app to AWS using Database Migration Service."
    },
    "k8s_cluster": {
        "title": "EKS Cluster Automation",
        "tags": ["Kubernetes", "Terraform", "Helm"],
        "desc": "Fully automated EKS provisioning with Terraform and Helm charts for observability."
    },
    "ci_cd_pipeline": {
        "title": "Jenkins CI/CD Pipeline",
        "tags": ["Jenkins", "Docker", "Groovy"],
        "desc": "End-to-end pipeline for building Docker images and deploying to staging/prod environments."
    },
    "serverless_api": {
        "title": "Serverless REST API",
        "tags": ["Lambda", "API Gateway", "DynamoDB"],
        "desc": "High-scale serverless backend handling 10k+ requests/sec with auto-scaling."
    },
    # Fallbacks for common demo names
    "project1": {"title": "Cloud Infrastructure Demo", "tags": ["Cloud", "Demo"], "desc": "Demonstration of core cloud infrastructure concepts."},
    "project2": {"title": "DevOps Workflow", "tags": ["DevOps"], "desc": "Snapshot of a modern DevOps workflow implementation."},
    "project3": {"title": "Monitoring Dashboard", "tags": ["Grafana", "Prometheus"], "desc": "Real-time metrics and alerting dashboard."}
}

def render(project_images):
    """
    Render the projects page HTML with rich cards.
    """
    html = """
    <style>
        .projects-header {
            margin-bottom: 32px;
            text-align: center;
        }
        .projects-header h2 {
            margin: 0 0 12px 0;
            font-size: 2.2rem;
            background: linear-gradient(90deg, #1f2937, #4b5563);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }
        .projects-header p {
            color: #6b7280;
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto;
        }

        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 28px;
        }

        .project-card {
            background: #fff;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid #f3f4f6;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.03);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
            position: relative;
        }

        .project-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            border-color: #e5e7eb;
        }

        .p-img-wrap {
            width: 100%;
            height: 200px;
            background: #f9fafb;
            overflow: hidden;
            border-bottom: 1px solid #f3f4f6;
        }
        
        .p-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .project-card:hover .p-img-wrap img {
            transform: scale(1.08);
        }

        .p-body {
            padding: 20px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .p-tags {
            display: flex;
            gap: 8px;
            margin-bottom: 12px;
            flex-wrap: wrap;
        }

        .p-tag {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 20px;
            background: #eff6ff;
            color: #1d4ed8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .p-title {
            font-weight: 800;
            font-size: 1.25rem;
            color: #111827;
            margin-bottom: 8px;
            line-height: 1.3;
        }

        .p-desc {
            font-size: 0.95rem;
            color: #6b7280;
            line-height: 1.6;
        }
        
        .empty-state {
            padding: 60px;
            text-align: center;
            background: #f9fafb;
            border-radius: 16px;
            border: 2px dashed #e5e7eb;
            color: #9ca3af;
        }
    </style>

    <div class="projects-wrapper">
        <div class="projects-header">
            <h2>Portfolio & Case Studies</h2>
            <p>Highlights from real-world implementations, demonstrating cloud architecture, DevOps automation, and scalable design.</p>
        </div>
    """

    if project_images:
        html += '<div class="project-grid">'
        for p in project_images:
            img_url = url_for("image_file", filename=f"projects/{p}")
            
            # Normalize filename to key (remove extension)
            key = p.rpartition('.')[0].lower()
            
            # Lookup metadata
            info = PROJECT_CATALOG.get(key)
            if not info:
                # Fallback: pretty print filename
                clean_title = p.rpartition('.')[0].replace('_', ' ').replace('-', ' ').title()
                info = {
                    "title": clean_title,
                    "tags": ["Project"],
                    "desc": "Hands-on implementation details available upon request."
                }
            
            tags_html = "".join([f'<span class="p-tag">{t}</span>' for t in info['tags']])

            html += f"""
            <div class="project-card">
                <div class="p-img-wrap">
                    <img src="{img_url}" alt="{info['title']}" loading="lazy">
                </div>
                <div class="p-body">
                    <div class="p-tags">{tags_html}</div>
                    <div class="p-title">{info['title']}</div>
                    <div class="p-desc">{info['desc']}</div>
                </div>
            </div>
            """
        html += "</div>"
    else:
        html += """
        <div class="empty-state">
            <h3>Portfolio Gallery Empty</h3>
            <p>Upload project screenshots to <code>images/projects/</code> to populate this grid.</p>
        </div>
        """

    html += "</div>"
    return html
