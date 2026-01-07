from flask import url_for
import json

# --- DYNAMIC SVG ARCHITECTURES (GCP THEMED) ---
# Using Google Brand Colors: #4285F4 (Blue), #DB4437 (Red), #F4B400 (Yellow), #0F9D58 (Green)

SVG_GKE = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- User -->
    <circle cx="50" cy="150" r="20" fill="#4285F4"/>
    <text x="50" y="185" text-anchor="middle" font-size="12" fill="#333">User</text>

    <!-- Load Balancer -->
    <rect x="120" y="120" width="60" height="60" rx="8" fill="#4285F4"/>
    <text x="150" y="155" text-anchor="middle" fill="white" font-size="10">GCLB</text>

    <!-- GKE Cluster Box -->
    <rect x="220" y="30" width="350" height="240" rx="10" fill="#f8fafc" stroke="#4285F4" stroke-width="2" stroke-dasharray="5,5"/>
    <text x="240" y="55" font-weight="bold" fill="#4285F4">GKE Cluster (Autopilot)</text>

    <!-- Node Pool -->
    <rect x="250" y="80" width="290" height="160" rx="8" fill="#e6f4ea" stroke="#0F9D58"/>
    
    <!-- Pods -->
    <g transform="translate(270, 100)">
        <polygon points="25,0 50,25 25,50 0,25" fill="#0F9D58"/>
        <text x="25" y="70" text-anchor="middle" font-size="10">Pod A</text>
    </g>
    <g transform="translate(350, 100)">
        <polygon points="25,0 50,25 25,50 0,25" fill="#0F9D58"/>
        <text x="25" y="70" text-anchor="middle" font-size="10">Pod B</text>
    </g>
    <g transform="translate(430, 100)">
        <polygon points="25,0 50,25 25,50 0,25" fill="#0F9D58" opacity="0.6"/>
        <text x="25" y="70" text-anchor="middle" font-size="10">Pod C (Auto)</text>
    </g>

    <!-- Traffic Flow -->
    <path id="gkePath" d="M70,150 L120,150 L270,125" fill="none" stroke="#4285F4" stroke-width="2"/>
    <circle r="4" fill="#DB4437">
        <animateMotion repeatCount="indefinite" dur="2s"> <mpath href="#gkePath"/> </animateMotion>
    </circle>
</svg>
"""

SVG_BIGQUERY = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Source Data -->
    <g transform="translate(50, 120)">
        <rect width="60" height="80" rx="4" fill="#F4B400"/> <!-- Yellow for Storage -->
        <text x="30" y="110" text-anchor="middle" font-size="12">CSV/JSON</text>
    </g>

    <!-- Pipeline -->
    <path id="bqPath" d="M110,160 L200,160" stroke="#4285F4" stroke-width="3" stroke-dasharray="4"/>
    <rect x="200" y="130" width="80" height="60" rx="8" fill="#4285F4"/> <!-- Dataflow -->
    <text x="240" y="165" text-anchor="middle" fill="white">Dataflow</text>

    <!-- BigQuery -->
    <polygon points="350,110 400,190 450,110" fill="#4285F4" opacity="0.1"/>
    <g transform="translate(360, 120)">
        <circle cx="40" cy="40" r="40" fill="#4285F4"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-weight="bold">BigQuery</text>
        <rect x="15" y="35" width="50" height="20" rx="2" fill="white" opacity="0.3"/>
    </g>
    <path id="loadPath" d="M280,160 L360,160" stroke="#4285F4" stroke-width="2"/>

    <!-- Analytics -->
    <rect x="500" y="120" width="60" height="80" rx="4" fill="#0F9D58"/>
    <text x="530" y="165" text-anchor="middle" fill="white">Looker</text>

    <!-- Animation -->
    <circle r="5" fill="#DB4437">
        <animateMotion repeatCount="indefinite" dur="1.5s" begin="0s"> <mpath href="#bqPath"/> </animateMotion>
    </circle>
</svg>
"""

SVG_PUBSUB = """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Publisher -->
    <rect x="30" y="130" width="80" height="60" rx="5" fill="#333"/>
    <text x="70" y="165" text-anchor="middle" fill="white">Publisher</text>

    <!-- Topic -->
    <circle cx="200" cy="160" r="40" fill="#4285F4" opacity="0.2"/>
    <circle cx="200" cy="160" r="30" fill="none" stroke="#4285F4" stroke-width="3"/>
    <text x="200" y="165" text-anchor="middle" font-weight="bold" fill="#4285F4">TOPIC</text>

    <!-- Subs -->
    <path d="M240,160 L320,100" stroke="#666" stroke-width="2"/>
    <path d="M240,160 L320,220" stroke="#666" stroke-width="2"/>

    <rect x="320" y="80" width="100" height="50" rx="8" fill="#0F9D58"/>
    <text x="370" y="110" text-anchor="middle" fill="white">Sub A (Email)</text>

    <rect x="320" y="200" width="100" height="50" rx="8" fill="#DB4437"/>
    <text x="370" y="230" text-anchor="middle" fill="white">Sub B (Log)</text>

    <!-- Message Animation -->
    <circle r="6" fill="#F4B400">
        <animateMotion repeatCount="indefinite" dur="2s" path="M110,160 L160,160"/>
    </circle>
</svg>
"""

GCP_PROJECTS = {
    "gke_autopilot": {
        "title": "Scalable Microservices with GKE Autopilot",
        "tags": ["GCP", "Kubernetes", "GKE", "DevOps"],
        "desc": "Deploy production-grade microservices on Google Kubernetes Engine (GKE) Autopilot mode for hands-off cluster management and security best practices.",
        "category": "cloud",
        "diagram": SVG_GKE,
        "problem": "Managing raw Kubernetes clusters is complex. Upgrading control planes, managing node pools, and securing the cluster require significant expertise and time, distracting developers from writing code.",
        "use_cases": [
            "E-Commerce: Handling variable traffic without manual node scaling.",
            "SaaS Platforms: Isolating tenant workloads securely.",
            "CI/CD: Spinning up ephemeral build agents on demand."
        ],
        "architecture": [
            "GKE Autopilot Cluster: Fully managed control plane + worker nodes.",
            "Cloud Load Balancing: Global HTTP(S) load balancing distributing traffic to pods.",
            "Artifact Registry: Secure storage for Docker container images.",
            "Cloud SQL: Managed PostgreSQL database for persistent storage.",
            "Workload Identity: Securely linking K8s ServiceAccounts to IAM roles."
        ],
        "steps": [
            "Step 1: Enable GKE API. `gcloud services enable container.googleapis.com`.",
            "Step 2: Create Cluster. `gcloud container clusters create-auto my-cluster --region us-central1`.",
            "Step 3: Build Docker image for your app and push to Artifact Registry.",
            "Step 4: Create `deployment.yaml` defining your replicas and resource limits.",
            "Step 5: Apply manifest. `kubectl apply -f deployment.yaml`.",
            "Step 6: Expose service via creating an Ingress resource (GCLB).",
            "Step 7: Verify pods are running and accessible via the external IP."
        ]
    },
    "bigquery_dw": {
        "title": "Serverless Data Warehouse with BigQuery",
        "tags": ["GCP", "BigQuery", "Data", "Analytics"],
        "desc": "Build a modern data warehouse pipeline that ingests data from Cloud Storage, processes it, and enables real-time SQL analytics using BigQuery.",
        "category": "cloud",
        "diagram": SVG_BIGQUERY,
        "problem": "Traditional data warehouses are expensive, hard to scale, and require constant maintenance. Businesses have siloes of data in CSVs/Logs that cannot be queried together effectively.",
        "use_cases": [
            "Marketing Analytics: Aggregating ad spend data from multiple sources.",
            "IoT Logs: Processing millions of sensor events per second.",
            "Business Intelligence: Connecting Looker/Tableau for dashboards."
        ],
        "architecture": [
            "Cloud Storage (GCS): Landing zone for raw files (CSV, JSON, Avro).",
            "Cloud Dataflow (Optional): Apache Beam pipelines for ETL transformations.",
            "BigQuery Dataset: The core container for tables and views.",
            "BigQuery Table: Partitioned and Clustered tables for performance.",
            "IAM: Fine-grained access control to datasets."
        ],
        "steps": [
            "Step 1: Create a GCS bucket and upload sample sales data (CSV).",
            "Step 2: Go to BigQuery Console -> Create Dataset `sales_data`.",
            "Step 3: Create Table -> Source: Google Cloud Storage -> Select your CSV.",
            "Step 4: Schema: 'Auto-detect'. Partitioning: By 'Date' column (Vital for cost).",
            "Step 5: Run a query: `SELECT product, SUM(amount) FROM sales_data GROUP BY product`.",
            "Step 6: Visualize results directly in Looker Studio with one click."
        ]
    },
    "pubsub_event": {
        "title": "Event-Driven Architecture with Pub/Sub",
        "tags": ["GCP", "Pub/Sub", "Cloud Functions", "Serverless"],
        "desc": "Decouple application components using asynchronous messaging with Google Cloud Pub/Sub and trigger serverless Cloud Functions.",
        "category": "cloud",
        "diagram": SVG_PUBSUB,
        "problem": "Tightly coupled applications fail together. If an order processing service goes down, the checkout service shouldn't also fail. Synchronous API calls create bottlenecks.",
        "use_cases": [
            "Order Processing: Checkout -> Pub/Sub -> Inventory/Email/Shipping services.",
            "Video Transcoding: Upload Event -> Pub/Sub -> Transcode Jobs.",
            "Log Aggregation: multiple services -> Pub/Sub -> BigQuery."
        ],
        "architecture": [
            "Pub/Sub Topic: The channel where messages are sent.",
            "Pub/Sub Subscription: The queue that retains messages for consumers.",
            "Cloud Scheduler: Cron job to trigger periodic events.",
            "Cloud Functions (2nd Gen): The consumer processing logic.",
            "Dead Letter Queue: Capturing failed messages for debugging."
        ],
        "steps": [
            "Step 1: Create a Pub/Sub Topic `order-created`.",
            "Step 2: Create a Subscription `email-service-sub` attached to the topic.",
            "Step 3: Write a Cloud Function (Python) that prints the message content.",
            "Step 4: Deploy Function with `--trigger-topic order-created`.",
            "Step 5: Publish a test message to the topic via Console or gcloud.",
            "Step 6: Check Cloud Function logs to see the message received instantly."
        ]
    },
    "cloud_run_micro": {
        "title": "Serverless Containers with Cloud Run",
        "tags": ["GCP", "Cloud Run", "Docker", "Serverless"],
        "desc": "Deploy stateless containers that scale to zero instantly, paying only for the request time processed.",
        "category": "cloud",
        "diagram": """<svg viewBox="0 0 400 200" class="arch-svg"><rect x="150" y="50" width="100" height="100" fill="#4285F4"/><text x="200" y="110" text-anchor="middle" fill="white">Container</text><path d="M50,100 L150,100" stroke="#333" stroke-dasharray="4"/><text x="100" y="90" text-anchor="middle">HTTPS</text></svg>""",
        "problem": "Managing servers for simple APIs is wasteful. Kubernetes is too complex for a single microservice. Developers just want to deploy a docker image and have a URL.",
        "use_cases": ["REST APIs", "Webhooks", "Lightweight Web Apps"],
        "architecture": ["Cloud Run Service", "Container Registry", "Traffic Splitting (Canary)"],
        "steps": ["Step 1: Write Dockerfile.", "Step 2: `gcloud run deploy --source .`", "Step 3: Access public URL."]
    }
}

def render():
    gcp_img = url_for('image_file', filename='gcp_icon.png')
    projects_json = json.dumps(GCP_PROJECTS)
    
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
            border-color: rgba(66, 133, 244, 0.5); /* Google Blue Border */
            background: rgba(255, 255, 255, 0.95);
            z-index: 10;
        }}

        .project-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 6px;
            background: linear-gradient(90deg, #4285F4, #DB4437, #F4B400, #0F9D58); /* Google Colors */
            border-radius: 4px 0 0 4px;
        }}

        .project-card::after {{
            content: '';
            position: absolute;
            bottom: -50px;
            right: -50px;
            width: 120px;
            height: 120px;
            background: radial-gradient(circle, rgba(66, 133, 244, 0.08) 0%, rgba(255,255,255,0) 70%);
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
            background: #eff6ff; 
            color: #1e40af;
            padding: 8px 16px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 700;
            border: 1px solid #dbeafe;
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
            background: linear-gradient(135deg, #4285F4 0%, #1a73e8 100%);
            color: white;
            border-radius: 99px;
            font-size: 0.9rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 6px -1px rgba(66, 133, 244, 0.3);
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
        }}
        .project-card:hover .view-btn {{
            transform: translateX(5px);
            box-shadow: 0 10px 15px -3px rgba(66, 133, 244, 0.4);
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
            color: #4285F4;
        }}

        /* MODAL STYLES (Identical structure, different colors) */
        .modal-overlay {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .modal-overlay.active {{
            opacity: 1;
            visibility: visible;
        }}
        
        .modal-content {{
            background: #ffffff;
            width: 1000px;
            max-width: 95vw;
            height: 90vh;
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            overflow: hidden;
            transform: scale(0.95) translateY(20px);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            display: flex;
            flex-direction: column;
        }}
        .modal-overlay.active .modal-content {{
            transform: scale(1) translateY(0);
        }}

        .modal-header {{
            background: linear-gradient(135deg, #4285F4 0%, #34A853 100%); /* Blue to Green Gradient */
            padding: 30px 40px;
            color: white;
            flex-shrink: 0;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }}
        .modal-title-group {{ flex: 1; }}
        .modal-title {{
            font-size: 2.25rem; font-weight: 800; line-height: 1.1; margin-bottom: 12px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .modal-tags {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .modal-tag {{
            background: rgba(255, 255, 255, 0.25);
            padding: 6px 14px; border-radius: 9999px;
            font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em;
            backdrop-filter: blur(4px);
        }}
        .close-btn {{
            background: rgba(255,255,255,0.2); border: none; color: white;
            width: 44px; height: 44px; border-radius: 50%; font-size: 24px;
            cursor: pointer; display: flex; align-items: center; justify-content: center;
            transition: all 0.2s; margin-left: 20px;
        }}
        .close-btn:hover {{ background: white; color: #4285F4; transform: rotate(90deg); }}

        .modal-body {{ padding: 40px; overflow-y: auto; color: #334155; background: #f8fafc; }}

        .diagram-container {{
            background: white; border-radius: 16px; padding: 20px;
            margin-bottom: 40px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid #e2e8f0; display: flex; justify-content: center;
        }}
        .arch-svg {{ width: 100%; height: auto; max-height: 350px; }}

        .modal-section {{
            margin-bottom: 40px; background: white; padding: 30px;
            border-radius: 16px; border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        }}
        .modal-section h3 {{
            font-size: 1.5rem; color: #0f172a; margin-top: 0; margin-bottom: 20px;
            display: flex; align-items: center; gap: 12px; font-weight: 800; letter-spacing: -0.025em;
        }}
        
        .problem-box {{
            background: #eff6ff; border-left: 6px solid #4285F4; /* Blue Theme */
            padding: 20px 25px; border-radius: 8px; font-size: 1.05rem;
            color: #1e3a8a; line-height: 1.7;
        }}

        .use-case-list {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;
        }}
        .use-case-card {{
            background: #f0fdf4; padding: 15px 20px; border-radius: 10px;
            border: 1px solid #bbf7d0; color: #15803d; font-weight: 600; /* Green Accents */
        }}

        .step-list {{ list-style: none; padding: 0; counter-reset: step-counter; }}
        .step-list li {{ position: relative; padding-left: 60px; margin-bottom: 25px; font-size: 1.05rem; line-height: 1.6; }}
        .step-list li:last-child {{ margin-bottom: 0; }}
        .step-list li::before {{
            counter-increment: step-counter; content: counter(step-counter);
            position: absolute; left: 0; top: -2px; width: 36px; height: 36px;
            background: linear-gradient(135deg, #4285F4 0%, #34A853 100%);
            color: white; border-radius: 50%; text-align: center;
            line-height: 36px; font-weight: bold; font-size: 1rem;
            box-shadow: 0 4px 6px -1px rgba(66, 133, 244, 0.3);
        }}
        .step-list li strong {{ display: block; color: #0f172a; font-weight: 700; margin-bottom: 4px; font-size: 1.1rem; }}

        ul.arch-list {{
            list-style-type: none; padding: 0; display: grid; grid-template-columns: 1fr; gap: 12px;
        }}
        ul.arch-list li {{
            background: #f8fafc; padding: 16px 20px; border-radius: 10px;
            border: 1px solid #e2e8f0; display: flex; align-items: center;
            font-weight: 500; color: #334155;
        }}
        ul.arch-list li::before {{ content: '⚙️'; margin-right: 15px; font-size: 1.2rem; }}

    </style>
    

    <div class="project-grid">
    """
    
    for key, proj in GCP_PROJECTS.items():
        tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in proj.get("tags", [])])
        html += f"""
        <div class="project-card" onclick="openModal('{key}')">
            <div class="card-header">
                <div class="project-title">{proj['title']}</div>
                <img src="{gcp_img}" alt="GCP" class="project-icon">
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

    <!-- MODAL COMPONENT (Reused Logic) -->
    <div class="modal-overlay" id="projectModal" onclick="closeModal(event)">
        <div class="modal-content">
            <div class="modal-header">
                <div class="modal-title-group">
                    <div class="modal-title" id="mTitle">Project Title</div>
                    <div class="modal-tags" id="mTags"></div>
                </div>
                <button class="close-btn" onclick="closeModal(event)">&times;</button>
            </div>
            <div class="modal-body">
                
                <div class="modal-section" style="background: transparent; border: none; box-shadow: none; padding: 0;">
                    <h3 style="margin-bottom: 15px; color: #1e293b;">Architecture:</h3>
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
        const gcpProjects = {projects_json};

        function openModal(key) {{
            const proj = gcpProjects[key];
            if (!proj) return;

            document.getElementById('mTitle').innerText = proj.title;
            document.getElementById('mProblem').innerText = proj.problem;
            document.getElementById('mDiagram').innerHTML = proj.diagram || '<div style="padding:20px;">Diagram coming soon...</div>';

            const tagsContainer = document.getElementById('mTags');
            tagsContainer.innerHTML = '';
            proj.tags.forEach(tag => {{
                const span = document.createElement('span');
                span.className = 'modal-tag';
                span.innerText = tag;
                tagsContainer.appendChild(span);
            }});

            const ucContainer = document.getElementById('mUseCases');
            ucContainer.innerHTML = '';
            if (proj.use_cases) {{
                 proj.use_cases.forEach(uc => {{
                    const div = document.createElement('div');
                    div.className = 'use-case-card';
                    div.innerText = uc;
                    ucContainer.appendChild(div);
                }});
            }}

            const archContainer = document.getElementById('mArch');
            archContainer.innerHTML = '';
            proj.architecture.forEach(item => {{
                const li = document.createElement('li');
                li.innerText = item;
                archContainer.appendChild(li);
            }});

            const stepsContainer = document.getElementById('mSteps');
            stepsContainer.innerHTML = '';
            proj.steps.forEach(step => {{
                const li = document.createElement('li');
                li.innerHTML = step;
                stepsContainer.appendChild(li);
            }});

            document.getElementById('projectModal').classList.add('active');
            document.body.style.overflow = 'hidden'; 
        }}

        function closeModal(event) {{
            if (event.target.classList.contains('modal-overlay') || event.target.classList.contains('close-btn') || event.target.closest('.close-btn')) {{
                document.getElementById('projectModal').classList.remove('active');
                document.body.style.overflow = 'auto';
            }}
        }}
    </script>
    """
    return html
