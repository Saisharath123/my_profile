from flask import url_for
from .cloud_aws import AWS_PROJECTS
from .cloud_gcp import GCP_PROJECTS
from .cloud_azure import AZURE_PROJECTS
from .cloud_multi import MULTI_PROJECTS

CLOUD_PROJECTS = {}
CLOUD_PROJECTS.update(AWS_PROJECTS)
CLOUD_PROJECTS.update(GCP_PROJECTS)
CLOUD_PROJECTS.update(AZURE_PROJECTS)
CLOUD_PROJECTS.update(MULTI_PROJECTS)

def render_cloud_page():
    """
    Render the Cloud Projects detailed view with 4 folders: AWS, GCP, Azure, Multi-Cloud.
    Uses the same folder metaphor as the main projects page.
    """
    aws_img = url_for('image_file', filename='aws_icon.png')
    gcp_img = url_for('image_file', filename='gcp_icon.png')
    azure_img = url_for('image_file', filename='azure_icon.png')
    multi_img = url_for('image_file', filename='cloud.webp') # Using cloud.webp for Multi-Cloud
    
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

        /* Reusing the Folder styles */
        .projects-wrapper {{
            padding: 40px 20px;
            perspective: 800px;
            margin-top: 20px;
        }}

        .folders-row {{
            display: flex;
            justify-content: center;
            gap: 48px;
            flex-wrap: wrap;
            margin: 20px 0;
        }}

        .folder {{
            width: 220px;
            height: 160px;
            position: relative;
            cursor: pointer;
            transition: transform 0.3s ease;
            transform-style: preserve-3d;
        }}

        .folder:hover {{
            transform: translateY(-10px) rotateX(5deg);
        }}

        .folder-back {{
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(to bottom, #d4a76a, #bf9052);
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }}
        .folder-back::after {{
            content: '';
            position: absolute;
            top: -14px; left: 0;
            width: 90px; height: 14px;
            background: #d4a76a;
            border-radius: 8px 8px 0 0;
        }}

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

        .folder-front {{
            position: absolute;
            top: 20px; left: 0;
            width: 100%; height: 140px;
            background: linear-gradient(135deg, #e6b97b 0%, #d4a76a 100%);
            border-radius: 0 0 8px 8px;
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
            transform: rotateX(-25deg);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }}

        .folder-icon {{
            width: 64px;
            height: 64px;
            object-fit: contain;
            margin-bottom: 8px;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
            transform: translateZ(20px);
            backface-visibility: hidden;
        }}
        
        .folder-label {{
            font-weight: 800;
            color: #3f2e18;
            font-size: 1.1rem;
            text-shadow: 0 1px 0 rgba(255,255,255,0.3);
            transform: translateZ(20px);
        }}
    </style>

    <div class="projects-wrapper">
        <div class="folders-row">
            
            <!-- AWS Folder -->
            <a href="/projects/cloud/aws" style="text-decoration: none; color: inherit;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{aws_img}" alt="AWS" class="folder-icon">
                        <div class="folder-label">AWS</div>
                    </div>
                </div>
            </a>

            <!-- GCP Folder -->
            <a href="/projects/cloud/gcp" style="text-decoration: none; color: inherit;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{gcp_img}" alt="GCP" class="folder-icon">
                        <div class="folder-label">Google Cloud</div>
                    </div>
                </div>
            </a>

            <!-- Azure Folder -->
            <a href="/projects/cloud/azure" style="text-decoration: none; color: inherit;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{azure_img}" alt="Azure" class="folder-icon">
                        <div class="folder-label">Azure</div>
                    </div>
                </div>
            </a>

            <!-- Multi-Cloud Folder -->
            <a href="/projects/cloud/multi" style="text-decoration: none; color: inherit;">
                <div class="folder">
                    <div class="folder-back"></div>
                    <div class="folder-paper"></div>
                    <div class="folder-front">
                        <img src="{multi_img}" alt="Multi-Cloud" class="folder-icon">
                        <div class="folder-label">Multi-Cloud</div>
                    </div>
                </div>
            </a>
            
        </div>
    </div>
    """
    return html
