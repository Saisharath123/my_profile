from flask import url_for
import json

# --- DYNAMIC SVG ARCHITECTURES (MULTI-CLOUD THEMED) ---
# Terraform Purple: #7B42BC, Neutral Grays

SVG_TF_MULTI = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Terraform Core -->
    <g transform="translate(250, 20)">
        <polygon points="50,0 95,25 95,75 50,100 5,75 5,25" fill="#7B42BC"/>
        <text x="50" y="55" text-anchor="middle" fill="white" font-weight="bold">TF</text>
        <text x="50" y="80" text-anchor="middle" fill="white" font-size="10">State</text>
    </g>

    <!-- AWS Side -->
    <rect x="50" y="150" width="200" height="130" rx="8" fill="#fff7ed" stroke="#FF9900" stroke-width="2"/>
    <text x="150" y="140" text-anchor="middle" fill="#FF9900" font-weight="bold">AWS (us-east-1)</text>
    <rect x="70" y="170" width="60" height="60" rx="4" fill="#FF9900" opacity="0.8"/>
    <text x="100" y="205" text-anchor="middle" fill="white" font-size="12">EC2</text>
    <rect x="150" y="170" width="60" height="60" rx="4" fill="#FF9900" opacity="0.6"/>
    <text x="180" y="205" text-anchor="middle" fill="white" font-size="12">S3</text>

    <!-- Azure Side -->
    <rect x="350" y="150" width="200" height="130" rx="8" fill="#f0f9ff" stroke="#0078D4" stroke-width="2"/>
    <text x="450" y="140" text-anchor="middle" fill="#0078D4" font-weight="bold">Azure (West EU)</text>
    <rect x="370" y="170" width="60" height="60" rx="4" fill="#0078D4" opacity="0.8"/>
    <text x="400" y="205" text-anchor="middle" fill="white" font-size="12">VM</text>
    <rect x="450" y="170" width="60" height="60" rx="4" fill="#0078D4" opacity="0.6"/>
    <text x="480" y="205" text-anchor="middle" fill="white" font-size="12">Blob</text>

    <!-- Action Arrows -->
    <path id="pathAws" d="M260,110 L150,150" stroke="#7B42BC" stroke-width="3" stroke-dasharray="4"/>
    <path id="pathAz" d="M340,110 L450,150" stroke="#7B42BC" stroke-width="3" stroke-dasharray="4"/>

    <!-- Animation -->
    <circle r="6" fill="#7B42BC">
        <animateMotion repeatCount="indefinite" dur="1s"> <mpath href="#pathAws"/> </animateMotion>
    </circle>
    <circle r="6" fill="#7B42BC">
        <animateMotion repeatCount="indefinite" dur="1s" begin="0.5s"> <mpath href="#pathAz"/> </animateMotion>
    </circle>
</svg>
"""

SVG_MIGRATE = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Source -->
    <rect x="50" y="80" width="150" height="140" rx="8" fill="#fff7ed" stroke="#FF9900"/>
    <g transform="translate(90, 110)">
        <path d="M10,0 L70,0 L60,80 L20,80 Z" fill="#FF9900"/>
        <text x="40" y="50" text-anchor="middle" fill="white">S3 Data</text>
    </g>

    <!-- Dest -->
    <rect x="400" y="80" width="150" height="140" rx="8" fill="#f0f9ff" stroke="#0078D4"/>
    <g transform="translate(440, 110)">
        <path d="M0,10 C0,5 20,0 40,0 C60,0 80,5 80,10 L80,70 L0,70 Z" fill="#0078D4"/>
        <text x="40" y="50" text-anchor="middle" fill="white">Blob</text>
    </g>

    <!-- Middleware/Script -->
    <rect x="250" y="110" width="100" height="80" rx="8" fill="#333"/>
    <text x="300" y="150" text-anchor="middle" fill="white" font-family="monospace">rclone</text>

    <!-- Flow -->
    <path id="migPath" d="M200,150 L250,150 M350,150 L400,150" stroke="#333" stroke-width="2"/>
    <circle r="5" fill="#22c55e">
        <animateMotion repeatCount="indefinite" dur="1.5s" path="M150,150 L450,150"/>
    </circle>
</svg>
"""

SVG_K8S_FED = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Control Plane -->
    <rect x="220" y="20" width="160" height="80" rx="8" fill="#326ce5"/>
    <text x="300" y="65" text-anchor="middle" fill="white" font-weight="bold">K8s Federation</text>

    <!-- Cluster 1 AWS -->
    <rect x="50" y="150" width="140" height="100" rx="8" fill="#fff7ed" stroke="#FF9900"/>
    <text x="120" y="200" text-anchor="middle" fill="#FF9900">EKS (East)</text>
    
    <!-- Cluster 2 GCP -->
    <rect x="230" y="150" width="140" height="100" rx="8" fill="#e6f4ea" stroke="#0F9D58"/>
    <text x="300" y="200" text-anchor="middle" fill="#0F9D58">GKE (Central)</text>

    <!-- Cluster 3 Azure -->
    <rect x="410" y="150" width="140" height="100" rx="8" fill="#f0f9ff" stroke="#0078D4"/>
    <text x="480" y="200" text-anchor="middle" fill="#0078D4">AKS (West)</text>

    <!-- Connections -->
    <path d="M300,100 L120,150" stroke="#326ce5" stroke-width="2" stroke-dasharray="4"/>
    <path d="M300,100 L300,150" stroke="#326ce5" stroke-width="2" stroke-dasharray="4"/>
    <path d="M300,100 L480,150" stroke="#326ce5" stroke-width="2" stroke-dasharray="4"/>

    <!-- Pulse -->
    <circle cx="300" cy="100" r="5" fill="white">
        <animate attributeName="r" values="5;10;5" dur="2s" repeatCount="indefinite"/>
    </circle>
</svg>
"""

MULTI_PROJECTS = {
    "tf_multicloud": {
        "title": "Multi-Cloud IaC with Terraform",
        "tags": ["Terraform", "AWS", "Azure", "IaC"],
        "desc": "Provision a unified infrastructure stack spanning AWS EC2 and Azure Virtual Machines using a single Terraform state and module structure.",
        "category": "cloud",
        "diagram": SVG_TF_MULTI,
        "problem": "Enterprises often avoid vendor lock-in by using multiple clouds, but managing separate deployment scripts (CloudFormation for AWS, ARM Templates for Azure) creates operational silos and inconsistency.",
        "use_cases": [
            "Disaster Recovery: Active in AWS, Passive Backup in Azure.",
            "Best of Breed: Google AI services + AWS Compute.",
            "Cost Optimization: Spot instances arbitration."
        ],
        "architecture": [
            "Terraform Core: Single binary to manage all clouds.",
            "Provider Blocks: `provider 'aws'` and `provider 'azurerm'` defined in `main.tf`.",
            "Remote State: Stored in Terraform Cloud or S3 with dynamoDB locking.",
            "Modules: Abstracting common logic (e.g., 'linux-server') for reusability."
        ],
        "steps": [
            "Step 1: Install Terraform/OpenTofu.",
            "Step 2: Configure credentials (~/.aws/credentials and `az login`).",
            "Step 3: Define providers in `versions.tf`.",
            "Step 4: Create resource 'aws_instance' 'web' { ... }.",
            "Step 5: Create resource 'azurerm_linux_virtual_machine' 'db' { ... }.",
            "Step 6: Run `terraform plan` to see resources created in BOTH clouds simultaneously.",
            "Step 7: `terraform apply`."
        ]
    },
    "k8s_fed": {
        "title": "Kubernetes Federation (EKS + GKE + AKS)",
        "tags": ["K8s", "Multi-Cloud", "DevOps"],
        "desc": "Manage a fleet of Kubernetes clusters across AWS, Google Cloud, and Azure from a single control plane using Federation v2 concepts or tools like Anthos/Rancher.",
        "category": "cloud",
        "diagram": SVG_K8S_FED,
        "problem": "Managing individual clusters involves duplicate config files, scattered monitoring, and inconsistent security policies. Users want 'write once, deploy everywhere'.",
        "use_cases": [
            "Geo-Redundancy: Apps running in US-East (AWS) and EU-West (Azure).",
            "Hybrid Cloud: On-prem data center + Public Cloud bursting.",
            "Compliance: Keeping specific data in specific regulated clouds."
        ],
        "architecture": [
            "Host Cluster: Management plane (e.g., Rancher or Anthos Config Management).",
            "Member Clusters: Downstream clusters (EKS, AKS, GKE).",
            "GitOps Repo: Single source of truth for YAML manifests.",
            "ArgoCD: Sync engine pulling from Git to all clusters."
        ],
        "steps": [
            "Step 1: Provision EKS, GKE, and AKS clusters.",
            "Step 2: Install a federation manager (e.g., Karmada or register with Fleet).",
            "Step 3: Join member clusters to the host plane.",
            "Step 4: Create a `PropagationPolicy` to define which apps go where.",
            "Step 5: Deploy a sample Nginx app to the Host.",
            "Step 6: Verify Nginx pods are running on all 3 clouds."
        ]
    },
    "data_migration": {
        "title": "Cloud-to-Cloud Data Migration Pipeline",
        "tags": ["Migration", "Storage", "Python"],
        "desc": "Automate the transfer of terabytes of object storage data from Amazon S3 to Azure Blob Storage using serverless synchronization tools.",
        "category": "cloud",
        "diagram": SVG_MIGRATE,
        "problem": "Moving clouds is hard because data has gravity. Manually downloading and uploading petabytes is impossible due to bandwidth and time constraints.",
        "use_cases": [
            "Mergers & Acquisitions: Consolidating IT assets.",
            "Cost Arbitrage: Moving interactions to a cheaper storage tier.",
            "Backup Strategy: Copying critical data to a competitor cloud."
        ],
        "architecture": [
            "Source: Amazon S3 Bucket.",
            "Destination: Azure Blob Container.",
            "Tooling: Rclone (self-hosted) or Azure Data Factory.",
            "Identity: AWS Access Keys & Azure SAS Tokens.",
            "Optimization: Multipart uploads and checksum verification."
        ],
        "steps": [
            "Step 1: Set up EC2/VM as the transfer agent.",
            "Step 2: Install `rclone` (open source cloud sync tool).",
            "Step 3: `rclone config` -> Add AWS S3 remote ('src').",
            "Step 4: `rclone config` -> Add Azure Blob remote ('dst').",
            "Step 5: Run `rclone sync src:mybucket dst:mycontainer --progress`.",
            "Step 6: Verify data integrity using MD5 hashes."
        ]
    }
}

def render():
    multi_img = url_for('image_file', filename='cloud.webp')
    projects_json = json.dumps(MULTI_PROJECTS)
    
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
            border-color: rgba(123, 66, 188, 0.5); /* Purple Border */
            background: rgba(255, 255, 255, 0.95);
            z-index: 10;
        }}

        .project-card::before {{
            content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 6px;
            background: linear-gradient(90deg, #7B42BC, #6366f1, #3b82f6); /* Multi-Cloud Gradient */
            border-radius: 4px 0 0 4px;
        }}

        .project-card::after {{
            content: ''; position: absolute; bottom: -50px; right: -50px; width: 120px; height: 120px;
            background: radial-gradient(circle, rgba(123, 66, 188, 0.08) 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%; pointer-events: none; transition: transform 0.5s ease;
        }}
        .project-card:hover::after {{ transform: scale(1.8); }}

        .card-header {{ display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 25px; }}

        .project-title {{
            font-size: 1.5rem; font-weight: 800; color: #0f172a; line-height: 1.3; margin: 0; padding-right: 15px;
        }}

        .project-icon {{
            width: 52px; height: 52px; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
            transition: transform 0.3s ease; flex-shrink: 0;
        }}
        .project-card:hover .project-icon {{ transform: rotate(15deg); }}

        .project-tags {{ display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 25px; }}

        .tag {{
            background: #f3e8ff; color: #6b21a8; padding: 8px 16px; border-radius: 12px;
            font-size: 0.75rem; font-weight: 700; border: 1px solid #e9d5ff;
            text-transform: uppercase; letter-spacing: 0.05em; box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}

        .project-desc {{
            color: #475569; font-size: 1.05rem; line-height: 1.6; margin-bottom: 30px; flex-grow: 1; font-weight: 500;
        }}
        
        .view-btn {{
            align-self: flex-start; padding: 12px 24px;
            background: linear-gradient(135deg, #7B42BC 0%, #4c1d95 100%);
            color: white; border-radius: 99px; font-size: 0.9rem; font-weight: 800;
            text-transform: uppercase; letter-spacing: 1px;
            box-shadow: 0 4px 6px -1px rgba(123, 66, 188, 0.3);
            display: flex; align-items: center; gap: 10px; transition: all 0.3s ease;
        }}
        .project-card:hover .view-btn {{
            transform: translateX(5px); box-shadow: 0 10px 15px -3px rgba(123, 66, 188, 0.4); padding-right: 28px;
        }}
        .view-btn::after {{
            content: '→'; font-size: 1.25em; line-height: 1; transition: transform 0.2s ease;
        }}
        .project-card:hover .view-btn::after {{ transform: translateX(3px); }}

        .back-link {{
            display: inline-flex; align-items: center; margin: 50px; color: #0f172a;
            font-weight: 800; text-decoration: none; background: white; padding: 16px 32px;
            border-radius: 9999px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            transition: all 0.3s; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.9rem;
        }}
        .back-link:hover {{
            transform: translateY(-3px); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.15); color: #7B42BC;
        }}

        /* MODAL */
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
            background: linear-gradient(135deg, #7B42BC 0%, #3b82f6 100%);
            padding: 30px 40px; color: white; flex-shrink: 0; display: flex; justify-content: space-between;
        }}
        .modal-title-group {{ flex: 1; }}
        .modal-title {{ font-size: 2.25rem; font-weight: 800; margin-bottom: 12px; }}
        .modal-tags {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .modal-tag {{ background: rgba(255,255,255,0.25); padding: 6px 14px; border-radius: 20px; }}
        .close-btn {{ background: rgba(255,255,255,0.2); border: none; color: white; width: 44px; height: 44px; border-radius: 50%; cursor: pointer; }}
        .close-btn:hover {{ background: white; color: #7B42BC; }}

        .modal-body {{ padding: 40px; overflow-y: auto; color: #334155; }}
        .diagram-container {{ background: white; border-radius: 16px; padding: 20px; border: 1px solid #e2e8f0; margin-bottom: 40px; display: flex; justify-content: center; }}
        .arch-svg {{ width: 100%; max-height: 350px; }}
        
        .modal-section {{ margin-bottom: 40px; background: white; padding: 30px; border-radius: 16px; border: 1px solid #e2e8f0; }}
        .modal-section h3 {{ color: #0f172a; margin-top: 0; margin-bottom: 20px; font-weight: 800; }}
        
        .problem-box {{ background: #f3e8ff; border-left: 6px solid #7B42BC; padding: 20px; color: #581c87; }}
        .use-case-list {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }}
        .use-case-card {{ background: #faf5ff; padding: 15px; border: 1px solid #e9d5ff; color: #6b21a8; }}

        .step-list {{ list-style: none; padding: 0; counter-reset: counter; }}
        .step-list li {{ position: relative; padding-left: 50px; margin-bottom: 20px; }}
        .step-list li::before {{
            counter-increment: counter; content: counter(counter); position: absolute; left: 0; width: 32px; height: 32px;
            background: linear-gradient(135deg, #7B42BC, #3b82f6); color: white; border-radius: 50%; text-align: center; line-height: 32px;
        }}
        .step-list li strong {{ display: block; color: #0f172a; }}
        ul.arch-list li {{ background: #f8fafc; padding: 12px; margin-bottom: 10px; border: 1px solid #e2e8f0; display: flex; align-items: center; }}
        ul.arch-list li::before {{ content: '⚙️'; margin-right: 15px; }}
    </style>
    

    <div class="project-grid">
    """
    
    for key, proj in MULTI_PROJECTS.items():
        tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in proj.get("tags", [])])
        html += f"""
        <div class="project-card" onclick="openModal('{key}')">
            <div class="card-header">
                <div class="project-title">{proj['title']}</div>
                <img src="{multi_img}" alt="Multi-Cloud" class="project-icon">
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
        const multiProjects = {projects_json};

        function openModal(key) {{
            const proj = multiProjects[key];
            if (!proj) return;

            document.getElementById('mTitle').innerText = proj.title;
            document.getElementById('mProblem').innerText = proj.problem;
            document.getElementById('mDiagram').innerHTML = proj.diagram || 'Diagram coming soon...';
            
            const tC = document.getElementById('mTags'); tC.innerHTML='';
            proj.tags.forEach(t => {{
                let s = document.createElement('span'); s.className='modal-tag'; s.innerText=t; tC.appendChild(s);
            }});

            const uC = document.getElementById('mUseCases'); uC.innerHTML='';
            if(proj.use_cases) proj.use_cases.forEach(u => {{
                let d = document.createElement('div'); d.className='use-case-card'; d.innerText=u; uC.appendChild(d);
            }});

            const aC = document.getElementById('mArch'); aC.innerHTML='';
            proj.architecture.forEach(a => {{
                let l = document.createElement('li'); l.innerText=a; aC.appendChild(l);
            }});

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
