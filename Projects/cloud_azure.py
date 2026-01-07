from flask import url_for
import json

# --- DYNAMIC SVG ARCHITECTURES (AZURE THEMED) ---
# Azure Blue: #0078D4, Dark Blue: #004C8C, Teal: #00B294

SVG_AKS = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- VNet -->
    <rect x="20" y="20" width="560" height="260" rx="10" fill="#f0f9ff" stroke="#0078D4" stroke-width="2" stroke-dasharray="5,5"/>
    <text x="40" y="50" font-weight="bold" fill="#0078D4">Azure Virtual Network</text>

    <!-- App Gateway -->
    <g transform="translate(50, 120)">
        <circle cx="30" cy="30" r="30" fill="#0078D4"/>
        <text x="30" y="35" text-anchor="middle" fill="white" font-size="10">App GW</text>
    </g>

    <!-- AKS Subnet -->
    <rect x="150" y="60" width="400" height="200" rx="8" fill="#e0f2fe" stroke="#00B294"/>
    <text x="170" y="90" fill="#006655" font-size="12">AKS Subnet</text>

    <!-- Nodes -->
    <rect x="180" y="110" width="100" height="120" rx="4" fill="white" stroke="#0078D4"/>
    <text x="230" y="130" text-anchor="middle" font-size="10">Node 1</text>
    <rect x="300" y="110" width="100" height="120" rx="4" fill="white" stroke="#0078D4"/>
    <text x="350" y="130" text-anchor="middle" font-size="10">Node 2</text>
    <rect x="420" y="110" width="100" height="120" rx="4" fill="white" stroke="#0078D4"/>
    <text x="470" y="130" text-anchor="middle" font-size="10">Node 3</text>

    <!-- Pods -->
    <circle cx="230" cy="160" r="15" fill="#00B294"/>
    <circle cx="230" cy="195" r="15" fill="#00B294"/>
    <circle cx="350" cy="160" r="15" fill="#00B294"/>
    <circle cx="470" cy="160" r="15" fill="#00B294"/>

    <!-- Traffic -->
    <path id="aksPath" d="M80,150 L180,150 L230,160" fill="none" stroke="#0078D4" stroke-width="2"/>
    <circle r="4" fill="#004C8C">
        <animateMotion repeatCount="indefinite" dur="1.5s"> <mpath href="#aksPath"/> </animateMotion>
    </circle>
</svg>
"""

SVG_FUNC = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Event Grid -->
    <circle cx="100" cy="150" r="40" fill="#00B294" opacity="0.2"/>
    <path d="M70,150 L130,150 M100,120 L100,180" stroke="#00B294" stroke-width="2"/>
    <text x="100" y="155" text-anchor="middle" font-weight="bold" fill="#0078D4">Event Grid</text>

    <!-- Function App -->
    <g transform="translate(250, 110)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#0078D4"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-weight="bold">⚡</text>
        <text x="40" y="95" text-anchor="middle" font-size="12">Azure Function</text>
    </g>

    <!-- Cosmos DB -->
    <g transform="translate(450, 110)">
        <path d="M0,10 C0,5 20,0 40,0 C60,0 80,5 80,10 L80,70 C80,75 60,80 40,80 C20,80 0,75 0,70 Z" fill="#7FBA00"/>
        <path d="M0,10 C0,15 20,20 40,20 C60,20 80,15 80,10" fill="none" stroke="#609000"/>
        <text x="40" y="45" text-anchor="middle" fill="white">Cosmos DB</text>
    </g>

    <!-- Flow -->
    <path id="funcPath" d="M140,150 L250,150" stroke="#0078D4" stroke-width="2" stroke-dasharray="4"/>
    <path d="M330,150 L450,150" stroke="#0078D4" stroke-width="2"/>

    <circle r="5" fill="#F25022">
        <animateMotion repeatCount="indefinite" dur="1s"> <mpath href="#funcPath"/> </animateMotion>
    </circle>
</svg>
"""

SVG_WEBAPP = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- App Service Plan -->
    <rect x="50" y="50" width="200" height="200" rx="8" fill="#f3f4f6" stroke="#666"/>
    <text x="150" y="75" text-anchor="middle" fill="#666">App Service Plan</text>
    
    <!-- Web App -->
    <rect x="70" y="90" width="160" height="140" rx="8" fill="#0078D4"/>
    <text x="150" y="160" text-anchor="middle" fill="white" font-weight="bold" font-size="14">Web App</text>

    <!-- Private Endpoint Connection -->
    <line x1="230" y1="160" x2="350" y2="160" stroke="#333" stroke-width="4"/>
    <rect x="330" y="140" width="40" height="40" rx="4" fill="#333"/>
    <text x="350" y="165" text-anchor="middle" fill="white" font-size="10">PE</text>

    <!-- SQL Database -->
    <path transform="translate(400, 110)" d="M0,10 C0,5 25,0 50,0 C75,0 100,5 100,10 L100,90 C100,95 75,100 50,100 C25,100 0,95 0,90 Z" fill="#0078D4"/>
    <text x="450" y="170" text-anchor="middle" fill="white" font-weight="bold">Azure SQL</text>

    <!-- Lock -->
    <text x="490" y="130" font-size="20">🔒</text>
</svg>
"""

AZURE_PROJECTS = {
    "aks_secure": {
        "title": "Secure AKS Cluster Implementation",
        "tags": ["Azure", "AKS", "Kubernetes", "Privacy"],
        "desc": "Deploy an enterprise-grade Azure Kubernetes Service (AKS) cluster with private networking, Azure Active Directory integration, and Azure Policy.",
        "category": "cloud",
        "diagram": SVG_AKS,
        "problem": "Default K8s clusters often expose API servers to the internet. Enterprise security demands that control planes and nodes are isolated within a private virtual network and that access is governed by corporate identities (AD).",
        "use_cases": [
            "FinTech Apps: hosting payments in a PCI-DSS compliant environment.",
            "Healthcare: processing PHI data with strict network isolation.",
            "Internal Tooling: Apps only accessible via VPN."
        ],
        "architecture": [
            "Azure VNet: Private network address space.",
            "AKS (Managed K8s): Private cluster mode (API server has internal IP).",
            "Azure CNI: Advanced networking allowing pods to have VNet IPs.",
            "Azure AD Integration: Developers use corporate credentials to `kubectl`.",
            "Azure Application Gateway: Ingress Controller for secure web traffic."
        ],
        "steps": [
            "Step 1: Create Resource Group & VNet with a dedicated subnet for AKS.",
            "Step 2: Create AKS Cluster with `--enable-private-cluster` flag.",
            "Step 3: Enable Azure CNI networking to allow pod-to-vnet communication.",
            "Step 4: Enable Azure AD RBAC for secure login.",
            "Step 5: Deploy an internal application (e.g., Nginx).",
            "Step 6: Configure Application Gateway Ingress Controller (AGIC) to expose app securely."
        ]
    },
    "serverless_funcs": {
        "title": "Event-Driven Processing with Azure Functions",
        "tags": ["Azure", "Serverless", "Functions", "Python"],
        "desc": "Build a scalable image processing pipeline that triggers automatically when files are uploaded to Blob Storage.",
        "category": "cloud",
        "diagram": SVG_FUNC,
        "problem": "Provisioning virtual machines that sit idle 90% of the time is costly. Event-driven tasks (like resizing user-uploaded images or parsing logs) should only incur costs when they actually run.",
        "use_cases": [
            "Image Resizing: User uploads photo -> Function generates thumbnail.",
            "Data Sanitation: CSV upload triggers cleaning script.",
            "Real-time Alerts: IoT message triggers push notification."
        ],
        "architecture": [
            "Blob Storage (Container): Stores uploaded files.",
            "Event Grid: Detects 'Blob Created' event and notifies Function.",
            "Azure Function (Consumption Plan): Python code to process file.",
            "Cosmos DB: Metadata storage for processed results."
        ],
        "steps": [
            "Step 1: Create Storage Account and 'images' container.",
            "Step 2: Create Azure Function App (Python runtime).",
            "Step 3: Write code: trigger on Blob Event, resize using Pillow library.",
            "Step 4: Configure Event Grid subscription to send events from Storage to Function.",
            "Step 5: Upload an image to the container.",
            "Step 6: Verify the Function fired via 'Monitor' tab and check output container."
        ]
    },
    "webapp_sql": {
        "title": "PaaS Web App with Private SQL",
        "tags": ["Azure", "Web App", "SQL", "PaaS"],
        "desc": "Host a scalable Python web application using Azure App Service connected securely to Azure SQL Database via Private Endpoint.",
        "category": "cloud",
        "diagram": SVG_WEBAPP,
        "problem": "Managing OS patches for web servers and database servers is overhead. Exposing database ports to the internet for connectivity is a major security risk.",
        "use_cases": [
            "Corporate Portal: Employee HR system.",
            "E-Commerce: Storefront with secure customer data.",
            "API Backend: For mobile applications."
        ],
        "architecture": [
            "App Service Plan: Defines compute power (e.g., P1v2).",
            "Web App for Containers: Runs the Dockerized app.",
            "Azure SQL Database: Manged relational DB.",
            "Private Endpoint: Network interface that connects Web App to SQL privately.",
            "VNet Integration: Allows Web App to talk to the Private Endpoint."
        ],
        "steps": [
            "Step 1: Provision Azure SQL Server (disable public access).",
            "Step 2: Create VNet and 'integration' subnet.",
            "Step 3: Create App Service and enable 'VNet Integration'.",
            "Step 4: Create Private Endpoint for SQL in the VNet.",
            "Step 5: Update App Service connection string to use SQL's private IP.",
            "Step 6: Deploy code via GitHub Actions."
        ]
    }
}

def render():
    azure_img = url_for('image_file', filename='azure_icon.png')
    projects_json = json.dumps(AZURE_PROJECTS)
    
    html = f"""
    <style>
        /* Override global main container styles */
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

        .project-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 40px;
            padding: 60px 40px;
            max-width: 1600px;
            margin: 0 auto;
            align-items: stretch;
        }}

        .project-card {{
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 20px;
            padding: 35px;
            box-shadow: 
                0 4px 6px -1px rgba(0, 0, 0, 0.05),
                0 10px 15px -3px rgba(0, 0, 0, 0.05),
                inset 0 0 0 1px rgba(255, 255, 255, 0.6);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: auto;
            min-height: 400px;
            cursor: pointer;
            z-index: 1;
        }}

        .project-card:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: 
                0 20px 25px -5px rgba(0, 0, 0, 0.1), 
                0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border-color: rgba(0, 120, 212, 0.5); /* Azure Blue Border */
            background: rgba(255, 255, 255, 0.95);
            z-index: 10;
        }}

        /* Azure Header Bar */
        .project-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 6px;
            background: linear-gradient(90deg, #0078D4, #00B294, #004C8C); 
            border-radius: 4px 0 0 4px;
        }}

        /* Azure Circle Decor */
        .project-card::after {{
            content: '';
            position: absolute;
            bottom: -50px;
            right: -50px;
            width: 120px;
            height: 120px;
            background: radial-gradient(circle, rgba(0, 120, 212, 0.08) 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%;
            pointer-events: none;
            transition: transform 0.5s ease;
        }}
        .project-card:hover::after {{
            transform: scale(1.8);
        }}

        .card-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 25px;
        }}

        .project-title {{
            font-size: 1.5rem;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.3;
            margin: 0;
            letter-spacing: -0.025em;
            padding-right: 15px;
        }}

        .project-icon {{
            width: 52px;
            height: 52px;
            object-fit: contain;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
            transition: transform 0.3s ease;
            flex-shrink: 0;
        }}
        .project-card:hover .project-icon {{
            transform: rotate(15deg);
        }}

        .project-tags {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 25px;
        }}

        .tag {{
            background: #f0f9ff; 
            color: #0369a1;
            padding: 8px 16px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 700;
            border: 1px solid #bae6fd;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}

        .project-desc {{
            color: #475569;
            font-size: 1.05rem;
            line-height: 1.6;
            margin-bottom: 30px;
            flex-grow: 1;
            font-weight: 500;
        }}
        
        .view-btn {{
            align-self: flex-start;
            padding: 12px 24px;
            background: linear-gradient(135deg, #0078D4 0%, #005a9e 100%);
            color: white;
            border-radius: 99px;
            font-size: 0.9rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 6px -1px rgba(0, 120, 212, 0.3);
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
        }}
        .project-card:hover .view-btn {{
            transform: translateX(5px);
            box-shadow: 0 10px 15px -3px rgba(0, 120, 212, 0.4);
            padding-right: 28px;
        }}
        .view-btn::after {{
            content: '→';
            font-size: 1.25em;
            line-height: 1;
            transition: transform 0.2s ease;
        }}
        .project-card:hover .view-btn::after {{
            transform: translateX(3px);
        }}

        .back-link {{
            display: inline-flex;
            align-items: center;
            margin: 50px;
            color: #0f172a;
            font-weight: 800;
            text-decoration: none;
            background: white;
            padding: 16px 32px;
            border-radius: 9999px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-size: 0.9rem;
        }}
        .back-link:hover {{
            transform: translateY(-3px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.15);
            color: #0078D4;
        }}

        /* MODAL (Azure Colors) */
        .modal-overlay {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px);
            opacity: 0; visibility: hidden; transition: all 0.3s;
            z-index: 9999; display: flex; align-items: center; justify-content: center;
        }}
        .modal-overlay.active {{ opacity: 1; visibility: visible; }}
        
        .modal-content {{
            background: #ffffff; width: 1000px; max-width: 95vw; height: 90vh;
            border-radius: 24px; display: flex; flex-direction: column;
            transform: scale(0.95) translateY(20px); transition: all 0.3s;
        }}
        .modal-overlay.active .modal-content {{ transform: scale(1) translateY(0); }}

        .modal-header {{
            background: linear-gradient(135deg, #0078D4 0%, #00B294 100%); /* Azure Gradient */
            padding: 30px 40px; color: white; flex-shrink: 0; display: flex; justify-content: space-between;
        }}
        .modal-title-group {{ flex: 1; }}
        .modal-title {{ font-size: 2.25rem; font-weight: 800; margin-bottom: 12px; }}
        .modal-tags {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .modal-tag {{ background: rgba(255,255,255,0.25); padding: 6px 14px; border-radius: 20px; }}
        .close-btn {{ background: rgba(255,255,255,0.2); border: none; color: white; width: 40px; height: 40px; border-radius: 50%; cursor: pointer; }}
        .close-btn:hover {{ background: white; color: #0078D4; }}

        .modal-body {{ padding: 40px; overflow-y: auto; color: #334155; }}
        .diagram-container {{ background: white; border-radius: 16px; padding: 20px; border: 1px solid #e2e8f0; margin-bottom: 40px; display: flex; justify-content: center; }}
        .arch-svg {{ width: 100%; max-height: 350px; }}
        
        .modal-section {{ margin-bottom: 40px; background: white; padding: 30px; border-radius: 16px; border: 1px solid #e2e8f0; }}
        .modal-section h3 {{ color: #0f172a; margin-top: 0; margin-bottom: 20px; font-weight: 800; }}
        
        .problem-box {{ background: #eff6ff; border-left: 6px solid #0078D4; padding: 20px; color: #1e3a8a; }}

        .use-case-list {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }}
        .use-case-card {{ background: #f0fdfa; padding: 15px; border: 1px solid #99f6e4; color: #0f766e; }}

        .step-list {{ list-style: none; padding: 0; counter-reset: counter; }}
        .step-list li {{ position: relative; padding-left: 50px; margin-bottom: 20px; }}
        .step-list li::before {{
            counter-increment: counter; content: counter(counter); position: absolute; left: 0; width: 32px; height: 32px;
            background: linear-gradient(135deg, #0078D4, #00B294); color: white; border-radius: 50%; text-align: center; line-height: 32px;
        }}
        .step-list li strong {{ display: block; color: #0f172a; }}

        ul.arch-list li {{ background: #f8fafc; padding: 12px; margin-bottom: 10px; border: 1px solid #e2e8f0; display: flex; align-items: center; }}
        ul.arch-list li::before {{ content: '⚙️'; margin-right: 15px; }}
    </style>
    

    <div class="project-grid">
    """
    
    for key, proj in AZURE_PROJECTS.items():
        tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in proj.get("tags", [])])
        html += f"""
        <div class="project-card" onclick="openModal('{key}')">
            <div class="card-header">
                <div class="project-title">{proj['title']}</div>
                <img src="{azure_img}" alt="Azure" class="project-icon">
            </div>
            <div class="project-tags">{tags_html}</div>
            <div class="project-desc">{proj['desc']}</div>
            <div class="view-btn">View Details</div>
        </div>
        """
        
    html += f"""
    </div>
    <div style="text-align: center; margin-bottom: 40px;">
        <a href="/projects/cloud" class="back-link">← Back to Cloud Projects</a>
    </div>

    <!-- MODAL JS -->
    <div class="modal-overlay" id="projectModal" onclick="closeModal(event)">
        <div class="modal-content">
            <div class="modal-header">
                <div class="modal-title-group">
                    <div class="modal-title" id="mTitle"></div>
                    <div class="modal-tags" id="mTags"></div>
                </div>
                <button class="close-btn" onclick="closeModal(event)">&times;</button>
            </div>
            <div class="modal-body">
                <div class="modal-section" style="border:none; padding:0;">
                    <h3 style="margin-bottom:15px;">Architecture:</h3>
                    <div class="diagram-container" id="mDiagram"></div>
                </div>
                <div class="modal-section">
                    <h3>⚠️ Problem Statement</h3>
                    <div class="problem-box" id="mProblem"></div>
                </div>
                <div class="modal-section">
                    <h3>🎯 Use Cases</h3>
                    <div class="use-case-list" id="mUseCases"></div>
                </div>
                <div class="modal-section">
                    <h3>🏗️ Solution Components</h3>
                    <ul class="arch-list" id="mArch"></ul>
                </div>
                <div class="modal-section">
                    <h3>Implementation Steps:</h3>
                    <ul class="step-list" id="mSteps"></ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        const azureProjects = {projects_json};

        function openModal(key) {{
            const proj = azureProjects[key];
            if (!proj) return;

            document.getElementById('mTitle').innerText = proj.title;
            document.getElementById('mProblem').innerText = proj.problem;
            document.getElementById('mDiagram').innerHTML = proj.diagram || 'Diagram coming soon...';

            // Tags
            const tC = document.getElementById('mTags'); tC.innerHTML='';
            proj.tags.forEach(t => {{
                let s = document.createElement('span'); s.className='modal-tag'; s.innerText=t; tC.appendChild(s);
            }});

            // Use Cases
            const uC = document.getElementById('mUseCases'); uC.innerHTML='';
            if(proj.use_cases) proj.use_cases.forEach(u => {{
                let d = document.createElement('div'); d.className='use-case-card'; d.innerText=u; uC.appendChild(d);
            }});

            // Arch
            const aC = document.getElementById('mArch'); aC.innerHTML='';
            proj.architecture.forEach(a => {{
                let l = document.createElement('li'); l.innerText=a; aC.appendChild(l);
            }});

            // Steps
            const sC = document.getElementById('mSteps'); sC.innerHTML='';
            proj.steps.forEach(s => {{
                let l = document.createElement('li'); l.innerHTML=s; sC.appendChild(l);
            }});

            document.getElementById('projectModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeModal(event) {{
            if (event.target.classList.contains('modal-overlay') || event.target.closest('.close-btn')) {{
                document.getElementById('projectModal').classList.remove('active');
                document.body.style.overflow = 'auto';
            }}
        }}
    </script>
    """
    return html
