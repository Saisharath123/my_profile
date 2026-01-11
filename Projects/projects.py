# projects.py
# Projects module logic with Folder Metaphor
# Exposes: render(project_images) -> HTML string

from flask import url_for

# Import backend content from separate modules
try:
    from .cloud_projects import CLOUD_PROJECTS
    from .devops_projects import DEVOPS_PROJECTS
    from .web_projects import WEB_PROJECTS
    from .other_projects import OTHER_PROJECTS
except ImportError:
    # Fallback if files missing (e.g. during dev)
    CLOUD_PROJECTS = {}
    DEVOPS_PROJECTS = {}
    WEB_PROJECTS = {}
    OTHER_PROJECTS = {}

# Combine all projects into the main catalog
PROJECT_CATALOG = {}
PROJECT_CATALOG.update(CLOUD_PROJECTS)
PROJECT_CATALOG.update(DEVOPS_PROJECTS)
PROJECT_CATALOG.update(WEB_PROJECTS)
PROJECT_CATALOG.update(OTHER_PROJECTS)

def render(project_images):
    """
    Render the projects page with Folder metaphor.
    """
    
    # Images for the folders
    cloud_img = url_for('image_file', filename='cloud.webp')
    devops_img = url_for('image_file', filename='devops.png')
    github_img = url_for('image_file', filename='github_logo.png')
    docker_img = url_for('image_file', filename='docker_logo.png')
    
    html = f"""
    <style>
        /* Override global main container styles for this page only */
        .card {{
            background: transparent !important;
            box-shadow: none !important;
            border: none !important;
            padding: 0 !important;
        }}
        .container {{
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
            width: 100% !important;
        }}

        .projects-wrapper {{
            padding: 40px 20px;
            perspective: 800px; /* Essential for 3D effect */
            margin-top: 20px;
        }}

        .folders-row {{
            display: flex;
            justify-content: center;
            gap: 48px;
            flex-wrap: wrap;
            margin: 20px 0;
        }}

        /* FOLDER CONTAINER */
        .folder {{
            width: 220px;
            height: 160px;
            position: relative;
            cursor: pointer;
            transition: transform 0.3s ease;
            transform-style: preserve-3d; /* Key for 3D children */
        }}

        .folder:hover {{
            transform: translateY(-10px) rotateX(5deg);
        }}

        /* BACK PLATE (The part behind) */
        .folder-back {{
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(to bottom, #d4a76a, #bf9052);
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            /* The tab on the back plate */
        }}
        .folder-back::after {{
            content: '';
            position: absolute;
            top: -14px; left: 0;
            width: 90px; height: 14px;
            background: #d4a76a;
            border-radius: 8px 8px 0 0;
        }}

        /* PAPER (Sheet inside) - Optional "peeking" paper */
        .folder-paper {{
            position: absolute;
            top: 10px; left: 10px;
            width: calc(100% - 20px); height: calc(100% - 15px);
            background: #ffffff;
            border-radius: 4px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            transform-origin: bottom center;
        }}
        .folder:hover .folder-paper {{
            transform: translateY(-8px) scaleY(1.02);
        }}

        /* FRONT PLATE (The cover) */
        .folder-front {{
            position: absolute;
            top: 20px; left: 0; /* Starts slightly lower to show back tab */
            width: 100%; height: 140px; /* Shorter than back to reveal paper/tab */
            background: linear-gradient(135deg, #e6b97b 0%, #d4a76a 100%);
            border-radius: 0 0 8px 8px;
            
            /* 3D Transform for "Slightly Open" look */
            transform-origin: bottom center;
            transform: rotateX(-12deg); 
            transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
            
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            backface-visibility: hidden;
            border-top: 1px solid rgba(255,255,255,0.3);
        }}

        .folder:hover .folder-front {{
            transform: rotateX(-25deg); /* Opens more on hover */
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }}

        /* CONTENT ON FRONT */
        .folder-icon {{
            width: 64px;
            height: 64px;
            object-fit: contain;
            margin-bottom: 8px;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
            transform: translateZ(20px); /* Push icon out slightly */
            backface-visibility: hidden; /* Fix flickering */
        }}
        
        .folder-label {{
            font-weight: 800;
            color: #3f2e18;
            font-size: 1.1rem;
            text-shadow: 0 1px 0 rgba(255,255,255,0.3);
            transform: translateZ(20px);
        }}

        /* Reset SVG strokes for non-image icons */
        .folder-icon path, .folder-icon rect, .folder-icon circle, .folder-icon line {{
            vector-effect: non-scaling-stroke;
        }}
    </style>



    <div class="projects-wrapper">
        <div class="folders-row">
            
            <!-- Cloud Folder -->
            <a href="{url_for('projects_cloud')}" style="text-decoration: none; color: inherit; display: block;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{cloud_img}" alt="Cloud" class="folder-icon">
                        <div class="folder-label">Cloud Projects</div>
                    </div>
                </div>
            </a>

            <!-- DevOps Folder -->
            <a href="{url_for('projects_devops')}" style="text-decoration: none; color: inherit; display: block;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{devops_img}" alt="DevOps" class="folder-icon">
                        <div class="folder-label">DevOps Projects</div>
                    </div>
                </div>
            </a>

            <!-- Web Folder -->
            <div class="folder">
                <div class="folder-back"></div>
                <div class="folder-paper"></div>
                <div class="folder-front">
                    <svg class="folder-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="2" y="3" width="20" height="14" rx="2" stroke="#2563eb" stroke-width="2"/>
                        <path d="M8 21h8" stroke="#2563eb" stroke-width="2" stroke-linecap="round"/>
                        <path d="M12 17v4" stroke="#2563eb" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                    <div class="folder-label">Web Projects</div>
                </div>
            </div>

            <!-- Other Folder -->
            <div class="folder">
                <div class="folder-back"></div>
                <div class="folder-paper"></div>
                <div class="folder-front">
                    <svg class="folder-icon" viewBox="0 0 24 24" fill="none" stroke="#4b5563" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="8" x2="12" y2="16"></line>
                        <line x1="8" y1="12" x2="16" y2="12"></line>
                    </svg>
                    <div class="folder-label">Other Projects</div>
                </div>
            </div>

            <!-- GitHub Folder -->
            <a href="https://github.com/Saisharath123" target="_blank" style="text-decoration: none; color: inherit; display: block;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{github_img}" alt="GitHub" class="folder-icon">
                        <div class="folder-label">GitHub</div>
                    </div>
                </div>
            </a>

            <!-- DockerHub Folder -->
            <a href="https://hub.docker.com/u/saisarath14" target="_blank" style="text-decoration: none; color: inherit; display: block;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{docker_img}" alt="DockerHub" class="folder-icon">
                        <div class="folder-label">DockerHub</div>
                    </div>
                </div>
            </a>

        </div>
        </div>
    </div>
    
    <div style="text-align: center; margin-bottom: 40px;">
        <a href="/" class="back-link" style="
            display: inline-flex; 
            align-items: center; 
            color: #0f172a; 
            font-weight: 800; 
            text-decoration: none; 
            background: rgba(255, 255, 255, 0.9); 
            padding: 12px 24px; 
            border-radius: 9999px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
            transition: all 0.3s; 
            font-size: 0.9rem;
            text-transform: uppercase;
        ">← Back to Home</a>
    </div>
    """
    return html
