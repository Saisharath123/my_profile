from flask import url_for
import json

# --- DYNAMIC SVG ARCHITECTURES (DevOps) ---
# Featuring "Marching Ants" CSS animation for visible flow

SVG_STYLE = """
<style>
    .flow-line {
        stroke-dasharray: 10;
        animation: flowAnimation 1s linear infinite;
    }
    @keyframes flowAnimation {
        from { stroke-dashoffset: 20; }
        to { stroke-dashoffset: 0; }
    }
    .particle {
        filter: drop-shadow(0 0 4px rgba(255, 255, 255, 0.8));
    }
</style>
"""

SVG_GITOPS = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Repos -->
    <g transform="translate(50, 50)">
        <rect width="80" height="80" rx="8" fill="#333"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-weight="bold">App Repo</text>
    </g>
    <g transform="translate(50, 170)">
        <rect width="80" height="80" rx="8" fill="#5c2d91"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-weight="bold">Config Repo</text>
    </g>

    <!-- CI -->
    <g transform="translate(200, 50)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#2088ff"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-weight="bold">Actions</text>
    </g>
    
    <!-- Registry -->
    <g transform="translate(350, 50)">
        <rect width="60" height="80" rx="4" fill="#FF9900"/>
        <text x="30" y="45" text-anchor="middle" fill="white">ECR</text>
    </g>

    <!-- Argo -->
    <g transform="translate(350, 170)">
        <path d="M40,0 L80,20 L80,70 L40,90 L0,70 L0,20 Z" fill="#ef4444"/>
        <text x="40" y="50" text-anchor="middle" fill="white" font-weight="bold">Argo CD</text>
    </g>

    <!-- Cluster -->
    <rect x="480" y="100" width="100" height="100" rx="10" fill="#3b82f6"/>
    <text x="530" y="155" text-anchor="middle" fill="white" font-weight="bold">EKS</text>

    <!-- Flows -->
    <path id="ciPath" d="M130,90 L200,90 L280,90 L350,90" stroke="#333" stroke-width="3" class="flow-line"/>
    <circle r="6" fill="#2088ff" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" href="#ciPath"/></circle>

    <path id="gitUpdate" d="M240,90 L240,140 L90,140 L90,170" stroke="#5c2d91" stroke-width="3" fill="none" class="flow-line"/>
    <circle r="6" fill="#5c2d91" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#gitUpdate"/></circle>

    <path id="syncPath" d="M130,210 L350,210" stroke="#ef4444" stroke-width="3" class="flow-line"/>
    <circle r="6" fill="#ef4444" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" href="#syncPath"/></circle>

    <path id="deployPath" d="M420,210 L530,210 L530,200" stroke="#ef4444" stroke-width="3" fill="none" class="flow-line"/>
    <circle r="6" fill="#fff" class="particle"><animateMotion repeatCount="indefinite" dur="1s" href="#deployPath"/></circle>
</svg>
"""

SVG_PIPELINE = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Code -->
    <circle cx="50" cy="150" r="30" fill="#333"/>
    <text x="50" y="155" text-anchor="middle" fill="white" font-weight="bold">Code</text>

    <!-- Pipeline Steps -->
    <rect x="150" y="120" width="80" height="60" rx="4" fill="#2088ff"/><text x="190" y="155" text-anchor="middle" fill="white">Build</text>
    <rect x="270" y="120" width="80" height="60" rx="4" fill="#2088ff"/><text x="310" y="155" text-anchor="middle" fill="white">Test</text>
    
    <!-- Artifact -->
    <rect x="400" y="110" width="60" height="80" rx="4" fill="#FF9900"/><text x="430" y="155" text-anchor="middle" fill="white">ECR</text>

    <!-- Deploy -->
    <rect x="500" y="100" width="80" height="100" rx="8" fill="#3b82f6"/>
    <text x="540" y="155" text-anchor="middle" fill="white" font-weight="bold">EKS</text>

    <!-- Main Pipe -->
    <path id="pipe" d="M80,150 L150,150 M230,150 L270,150 M350,150 L400,150 M460,150 L500,150" stroke="#333" stroke-width="4" class="flow-line"/>
    <circle r="6" fill="#22c55e" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#pipe"/></circle>
</svg>
"""

SVG_MULTI_ENV = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <g transform="translate(50, 110)">
        <path d="M40,0 L80,20 L80,70 L40,90 L0,70 L0,20 Z" fill="#ef4444"/>
        <text x="40" y="50" text-anchor="middle" fill="white" font-weight="bold">Argo CD</text>
    </g>
    <g transform="translate(250, 20)">
        <rect width="120" height="70" rx="6" fill="#86efac"/>
        <text x="60" y="45" text-anchor="middle" fill="#14532d" font-weight="bold">DEV</text>
    </g>
    <g transform="translate(250, 110)">
        <rect width="120" height="70" rx="6" fill="#93c5fd"/>
        <text x="60" y="45" text-anchor="middle" fill="#1e3a8a" font-weight="bold">STAGE</text>
    </g>
    <g transform="translate(250, 200)">
        <rect width="120" height="70" rx="6" fill="#fca5a5"/>
        <text x="60" y="45" text-anchor="middle" fill="#7f1d1d" font-weight="bold">PROD</text>
    </g>
    <!-- Branch Lines -->
    <path id="devPath" d="M130,150 L180,150 L180,55 L250,55" stroke="#ef4444" stroke-width="3" fill="none" class="flow-line"/>
    <path id="stagePath" d="M130,150 L250,150" stroke="#ef4444" stroke-width="3" fill="none" class="flow-line"/>
    <path id="prodPath" d="M130,150 L180,150 L180,235 L250,235" stroke="#ef4444" stroke-width="3" fill="none" class="flow-line"/>

    <circle r="6" fill="#22c55e" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#devPath"/></circle>
    <circle r="6" fill="#3b82f6" class="particle"><animateMotion repeatCount="indefinite" dur="2s" begin="0.5s" href="#stagePath"/></circle>
    <circle r="6" fill="#ef4444" class="particle"><animateMotion repeatCount="indefinite" dur="2s" begin="1s" href="#prodPath"/></circle>
</svg>
"""

SVG_IRSA = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <rect x="20" y="20" width="250" height="260" rx="10" fill="#fff7ed" stroke="#FF9900" stroke-dasharray="4"/>
    <text x="145" y="45" text-anchor="middle" fill="#c2410c" font-weight="bold">EKS Cluster</text>
    
    <g transform="translate(50, 80)">
        <rect width="190" height="60" rx="4" fill="#3b82f6"/>
        <text x="95" y="35" text-anchor="middle" fill="white">Service Account</text>
    </g>
    <g transform="translate(100, 180)">
        <rect width="90" height="80" rx="4" fill="#22c55e"/>
        <text x="45" y="45" text-anchor="middle" fill="white">Pod</text>
    </g>
    <rect x="330" y="20" width="250" height="260" rx="10" fill="#f8fafc" stroke="#334155"/>
    <text x="455" y="45" text-anchor="middle" fill="#334155" font-weight="bold">AWS Cloud</text>
    
    <g transform="translate(380, 80)">
        <polygon points="50,0 100,50 50,100 0,50" fill="#ef4444"/>
        <text x="50" y="55" text-anchor="middle" fill="white" font-size="12">IAM Role</text>
    </g>
    <g transform="translate(410, 200)">
        <rect width="60" height="60" rx="4" fill="#FF9900"/>
        <text x="30" y="35" text-anchor="middle" fill="white">S3</text>
    </g>
    <path id="trustPath" d="M240,110 L380,110" stroke="#3b82f6" stroke-width="3" stroke-dasharray="4" class="flow-line"/>
    <path id="accessPath" d="M190,220 L300,220 L300,130 L380,130 M430,130 L440,200" stroke="#22c55e" stroke-width="3" fill="none" class="flow-line"/>
    <circle r="6" fill="#22c55e" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#accessPath"/></circle>
</svg>
"""

SVG_BLUE_GREEN = SVG_STYLE + """
<svg viewBox="0 0 600 350" class="arch-svg">
    <rect x="40" y="20" width="520" height="310" rx="15" fill="#f8fafc" stroke="#22c55e" stroke-width="2" stroke-dasharray="4"/>
    <text x="80" y="50" font-weight="bold" fill="#22c55e">EKS Cluster</text>

    <!-- Ingress -->
    <g transform="translate(260, 40)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#8b5cf6"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-size="10">ALB</text>
    </g>

    <!-- Blue Stack -->
    <rect x="80" y="150" width="180" height="120" rx="8" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="170" y="175" text-anchor="middle" fill="#1e40af" font-weight="bold">BLUE (v1)</text>
    <text x="170" y="200" text-anchor="middle" font-size="24">🟦</text>
    <text x="170" y="235" text-anchor="middle" fill="#1e40af" font-size="12">Live Traffic</text>

    <!-- Green Stack -->
    <rect x="340" y="150" width="180" height="120" rx="8" fill="#dcfce7" stroke="#22c55e"/>
    <text x="430" y="175" text-anchor="middle" fill="#15803d" font-weight="bold">GREEN (v2)</text>
    <text x="430" y="200" text-anchor="middle" font-size="24">🟩</text>
    <text x="430" y="235" text-anchor="middle" fill="#15803d" font-size="12">Idle / Test</text>

    <!-- Traffic Switch -->
    <path id="trafficBlue" d="M300,80 L170,150" stroke="#3b82f6" stroke-width="4" class="flow-line"/>
    <path id="trafficGreen" d="M300,80 L430,150" stroke="#22c55e" stroke-width="2" stroke-dasharray="4" opacity="0.3"/>
    
    <circle r="7" fill="#3b82f6" class="particle"><animateMotion repeatCount="indefinite" dur="1s" href="#trafficBlue"/></circle>
</svg>
"""

SVG_TF_GITOPS = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Engineer -->
    <circle cx="40" cy="150" r="20" fill="#333"/>
    <text x="40" y="185" text-anchor="middle" font-size="10">Dev</text>

    <!-- Git -->
    <rect x="100" y="120" width="60" height="60" rx="4" fill="#333"/>
    <text x="130" y="155" text-anchor="middle" fill="white">Git</text>

    <!-- Actions -->
    <g transform="translate(200, 110)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#2088ff"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-size="10">Action</text>
    </g>

    <!-- Terraform -->
    <g transform="translate(300, 50)">
        <polygon points="30,0 60,30 30,60 0,30" fill="#7B42BC"/>
        <text x="30" y="35" text-anchor="middle" fill="white" font-size="10">TF</text>
    </g>

    <!-- Infra Creation -->
    <path id="infraPath" d="M360,80 L450,150" stroke="#7B42BC" stroke-width="3" stroke-dasharray="4" class="flow-line"/>

    <!-- Cluster -->
    <rect x="420" y="130" width="140" height="100" rx="8" fill="#3b82f6" opacity="0.9"/>
    <text x="490" y="160" text-anchor="middle" fill="white" font-weight="bold">EKS Cluster</text>
    <text x="490" y="190" text-anchor="middle" fill="white" font-size="20">🏗️</text>

    <!-- Argo Deployment -->
    <g transform="translate(300, 180)">
        <path d="M30,0 L60,15 L60,45 L30,60 L0,45 L0,15 Z" fill="#ef4444"/>
        <text x="30" y="35" text-anchor="middle" fill="white" font-size="8">Argo</text>
    </g>
    <path id="argoPath" d="M360,210 L420,200" stroke="#ef4444" stroke-width="3" class="flow-line"/>

    <!-- Flow -->
    <path id="gitFlow" d="M60,150 L100,150 M160,150 L200,150 M280,150 L300,80" stroke="#333" stroke-width="2" fill="none" class="flow-line"/>
    <circle r="5" fill="#2088ff" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#gitFlow"/></circle>
    <circle r="5" fill="#7B42BC" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" begin="1s" href="#infraPath"/></circle>
</svg>
"""

SVG_MONOREPO = SVG_STYLE + """
<svg viewBox="0 0 600 320" class="arch-svg">
    <!-- Monorepo -->
    <rect x="20" y="50" width="100" height="220" rx="8" fill="#f1f5f9" stroke="#64748b"/>
    <text x="70" y="80" text-anchor="middle" font-weight="bold">Monorepo</text>
    <rect x="35" y="100" width="70" height="40" rx="4" fill="#e0f2fe"/><text x="70" y="125" text-anchor="middle" font-size="10">Service A</text>
    <rect x="35" y="160" width="70" height="40" rx="4" fill="#dcfce7"/><text x="70" y="185" text-anchor="middle" font-size="10">Service B</text>
    <rect x="35" y="220" width="70" height="40" rx="4" fill="#fce7f3"/><text x="70" y="245" text-anchor="middle" font-size="10">Service C</text>

    <!-- Argo Applications -->
    <g transform="translate(250, 100)">
        <path d="M30,0 L60,15 L60,45 L30,60 L0,45 L0,15 Z" fill="#ef4444"/>
        <text x="30" y="35" text-anchor="middle" fill="white" font-size="8">App A</text>
    </g>
    <g transform="translate(250, 160)">
        <path d="M30,0 L60,15 L60,45 L30,60 L0,45 L0,15 Z" fill="#ef4444"/>
        <text x="30" y="35" text-anchor="middle" fill="white" font-size="8">App B</text>
    </g>
    <g transform="translate(250, 220)">
        <path d="M30,0 L60,15 L60,45 L30,60 L0,45 L0,15 Z" fill="#ef4444"/>
        <text x="30" y="35" text-anchor="middle" fill="white" font-size="8">App C</text>
    </g>
    
    <!-- K8s -->
    <rect x="450" y="50" width="120" height="220" rx="8" fill="#e0f7fa" stroke="#00bcd4"/>
    <text x="510" y="80" text-anchor="middle" fill="#006064" font-weight="bold">Cluster</text>
    <circle cx="510" cy="130" r="15" fill="#3b82f6"/>
    <circle cx="510" cy="190" r="15" fill="#22c55e"/>
    <circle cx="510" cy="250" r="15" fill="#ec4899"/>

    <!-- selective Sync flow -->
    <path id="syncA" d="M105,120 L250,130 M310,130 L495,130" stroke="#ef4444" stroke-width="2" fill="none" class="flow-line"/>
    <circle r="4" fill="#ef4444" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#syncA"/></circle>
</svg>
"""

SVG_DR_GITOPS = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <circle cx="50" cy="150" r="20" fill="#3b82f6"/>
    <text x="50" y="185" text-anchor="middle" font-size="10">User</text>

    <!-- Route53 -->
    <rect x="120" y="120" width="80" height="60" rx="4" fill="#FF9900"/>
    <text x="160" y="155" text-anchor="middle" fill="white" font-weight="bold">R53</text>

    <!-- Region 1 -->
    <rect x="250" y="50" width="120" height="100" rx="8" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="310" y="80" text-anchor="middle" fill="#1e40af">Primary (US)</text>
    <text x="310" y="110" text-anchor="middle" font-size="20">✅</text>

    <!-- Region 2 -->
    <rect x="420" y="150" width="120" height="100" rx="8" fill="#fce7f3" stroke="#be185d"/>
    <text x="480" y="180" text-anchor="middle" fill="#831843">DR (EU)</text>
    <text x="480" y="210" text-anchor="middle" font-size="20">💤</text>
    
    <!-- Git Repo -->
    <g transform="translate(330, 250)">
        <rect width="60" height="40" rx="4" fill="#333"/>
        <text x="30" y="25" text-anchor="middle" fill="white" font-size="10">Git Config</text>
    </g>

    <!-- Traffic -->
    <path id="pathPrimary" d="M70,150 L120,150 L250,100" stroke="#22c55e" stroke-width="3" fill="none" class="flow-line"/>
    <path id="pathDR" d="M200,150 L420,200" stroke="#be185d" stroke-width="2" stroke-dasharray="4" fill="none" opacity="0.3"/>
    
    <!-- Git Sync -->
    <path id="sync1" d="M360,250 L310,150" stroke="#333" stroke-width="2" stroke-dasharray="4" class="flow-line"/>
    <path id="sync2" d="M390,250 L480,250 L480,250" stroke="#333" stroke-width="2" stroke-dasharray="4" class="flow-line"/>

    <circle r="5" fill="#22c55e" class="particle"><animateMotion repeatCount="indefinite" dur="1s" href="#pathPrimary"/></circle>
</svg>
"""

SVG_OBSERVABILITY = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- EKS Pods -->
    <rect x="50" y="100" width="150" height="150" rx="8" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="125" y="130" text-anchor="middle" fill="#1e40af" font-weight="bold">EKS Cluster</text>
    <rect x="70" y="150" width="40" height="40" rx="4" fill="#22c55e"/>
    <rect x="130" y="150" width="40" height="40" rx="4" fill="#ef4444"/> <!-- Failed Pod -->

    <!-- CloudWatch -->
    <rect x="300" y="80" width="100" height="80" rx="8" fill="#d946ef"/>
    <text x="350" y="125" text-anchor="middle" fill="white" font-weight="bold">CloudWatch</text>

    <!-- SNS -->
    <circle cx="480" cy="120" r="30" fill="#FF9900"/>
    <text x="480" y="125" text-anchor="middle" fill="white" font-weight="bold">SNS</text>

    <!-- Slack/Email -->
    <rect x="530" y="180" width="60" height="60" rx="8" fill="#333"/>
    <text x="560" y="215" text-anchor="middle" fill="white" font-size="10">Alert</text>

    <!-- Log Flow -->
    <path id="logPath" d="M200,170 L300,120" stroke="#d946ef" stroke-width="3" class="flow-line"/>
    <path id="alertPath" d="M400,120 L450,120" stroke="#FF9900" stroke-width="3" class="flow-line"/>
    <path id="notifyPath" d="M480,150 L560,180" stroke="#333" stroke-width="2" stroke-dasharray="4" class="flow-line"/>

    <circle r="5" fill="#d946ef" class="particle"><animateMotion repeatCount="indefinite" dur="1s" href="#logPath"/></circle>
    <circle r="5" fill="#FF9900" class="particle"><animateMotion repeatCount="indefinite" dur="1s" begin="0.5s" href="#alertPath"/></circle>
</svg>
"""

SVG_CANARY = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <!-- Traffic Source -->
    <rect x="20" y="120" width="60" height="60" rx="4" fill="#333"/>
    <text x="50" y="155" text-anchor="middle" fill="white">Users</text>
    
    <!-- Rollout Controller -->
    <g transform="translate(150, 50)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#0ea5e9"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-size="10">Argo</text>
    </g>

    <!-- Stable -->
    <rect x="350" y="50" width="150" height="80" rx="8" fill="#dcdfce" stroke="#4d7c0f"/>
    <text x="425" y="80" text-anchor="middle" font-weight="bold" fill="#365314">Stable (v1)</text>
    <text x="425" y="110" text-anchor="middle">90% Traffic</text>

    <!-- Canary -->
    <rect x="350" y="180" width="150" height="80" rx="8" fill="#fef08a" stroke="#ca8a04"/>
    <text x="425" y="210" text-anchor="middle" font-weight="bold" fill="#854d0e">Canary (v2)</text>
    <text x="425" y="240" text-anchor="middle">10% Traffic</text>

    <!-- Split Flow -->
    <path id="majorPath" d="M80,150 L350,90" stroke="#4d7c0f" stroke-width="4" class="flow-line"/>
    <path id="minorPath" d="M80,150 L350,220" stroke="#ca8a04" stroke-width="2" stroke-dasharray="4" class="flow-line"/>

    <circle r="6" fill="#4d7c0f" class="particle"><animateMotion repeatCount="indefinite" dur="0.8s" href="#majorPath"/></circle>
    <circle r="4" fill="#ca8a04" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#minorPath"/></circle>
</svg>
"""

DEVOPS_PROJECTS = {
    "gitops_eks": {
        "title": "GitOps Deployment on EKS with Argo CD",
        "tags": ["Kubernetes", "Argo CD", "EKS", "GitHub Actions"],
        "desc": "Implement a full GitOps workflow where infrastructure updates are triggered by git commits.",
        "category": "devops",
        "diagram": SVG_GITOPS,
        "problem": "Manual deployments via `kubectl` are error-prone and lack audit trails.",
        "use_cases": ["Self-Healing Infrastructure", "Audit & Compliance", "Automated Rollbacks"],
        "architecture": ["GitHub (App & Config Repos)", "GitHub Actions (CI)", "Amazon ECR", "Argo CD (GitOps Controller)", "EKS Cluster"],
        "steps": [
            "Step 1: Set up EKS Cluster and install Argo CD.",
            "Step 2: Create GitHub Actions workflow to build Docker image and push to ECR.",
            "Step 3: Update K8s manifests in the Config Repo with the new image tag automatically.",
            "Step 4: Argo CD detects the change in git and syncs the cluster state."
        ]
    },
    "cicd_end_to_end": {
        "title": "End-to-End CI/CD Pipeline on AWS",
        "tags": ["CI/CD", "GitHub Actions", "ECR", "EKS"],
        "desc": "A production-grade pipeline handling code build, test, security scan, and deployment.",
        "category": "devops",
        "diagram": SVG_PIPELINE,
        "problem": "Software release cycles are slow and buggy without automated testing and deployment.",
        "use_cases": ["Rapid Prototyping", "Zero-Downtime Deployment", "Quality Assurance"],
        "architecture": ["Source Code (Git)", "Build Server (Actions)", "Test Suite (PyTest/Jest)", "Container Registry (ECR)", "Orchestrator (EKS)"],
        "steps": [
            "Step 1: Push code to main branch.",
            "Step 2: Trigger GitHub Actions: Lint -> Test -> Build.",
            "Step 3: Authenticate with AWS & push image to ECR.",
            "Step 4: Commit new version tag to the infrastructure repo.",
            "Step 5: Verify deployment rollout on EKS."
        ]
    },
    "multi_env_gitops": {
        "title": "Multi-Environment GitOps Strategy",
        "tags": ["Argo CD", "Kustomize", "Strategy"],
        "desc": "Manage Dev, Staging, and Production environments using Kustomize overlays and Argo CD Applications.",
        "category": "devops",
        "diagram": SVG_MULTI_ENV,
        "problem": "Managing configuration drift across multiple environments is a nightmare.",
        "use_cases": ["Blue/Green Deployment Preparation", "Environment Isolation", "Feature Testing"],
        "architecture": ["Kustomize Overlays (base, dev, prod)", "Argo CD ApplicationSet", "Namespaces/Clusters Isolation"],
        "steps": [
            "Step 1: Structure git repo with `base/` and `overlays/dev`, `overlays/prod`.",
            "Step 2: Configure Argo CD to track branches or folders.",
            "Step 3: Push change to Dev branch -> Auto-sync to Dev namespace.",
            "Step 4: Create PR to Prod branch -> Manual Approval -> Sync to Prod."
        ]
    },
    "irsa_security": {
        "title": "Secure Pipelines with IRSA (IAM Roles)",
        "tags": ["Security", "IAM", "EKS", "OIDC"],
        "desc": "Eliminate long-lived AWS keys in Kubernetes by using OIDC and IAM Roles for Service Accounts.",
        "category": "devops",
        "diagram": SVG_IRSA,
        "problem": "Hardcoding AWS Access Keys in K8s Secrets is a major security risk.",
        "use_cases": ["S3 Access from Pods", "Least Privilege Security", "Compliant Banking Apps"],
        "architecture": ["EKS OIDC Provider", "AWS IAM Role with Trust Policy", "K8s Service Account", "Pod Identity"],
        "steps": [
            "Step 1: Create an OIDC provider for the EKS cluster.",
            "Step 2: Create an IAM Policy (e.g. S3ReadOnly).",
            "Step 3: Create an IAM Role trusting the OIDC provider.",
            "Step 4: Annotate the K8s Service Account with the Role ARN.",
            "Step 5: Deploy Pod using that Service Account."
        ]
    },
    "blue_green_eks": {
        "title": "Blue-Green Deployment on EKS",
        "tags": ["EKS", "ALB", "Argo CD", "Strategy"],
        "desc": "Implement zero-downtime releases by running two versions (Blue & Green) and switching traffic via ALB.",
        "category": "devops",
        "diagram": SVG_BLUE_GREEN,
        "problem": "Standard rolling updates can fail mid-way, leaving the application in a mixed state.",
        "use_cases": ["Critical Banking Apps", "Instant Rollback availability"],
        "architecture": ["AWS ALB Ingress Controller", "Blue ReplicaSet (Active)", "Green ReplicaSet (Idle)", "Argo Rollouts"],
        "steps": [
            "Step 1: Install Argo Rollouts controller.",
            "Step 2: Define Rollout resource with BlueGreen strategy.",
            "Step 3: Deploy v1 (Blue).",
            "Step 4: Deploy v2 (Green). Rollouts creates a Preview service.",
            "Step 5: Promote v2. ALB switches Active Service to Green pods."
        ]
    },
    "terraform_gitops": {
        "title": "Infra Deployment: Terraform + GitOps",
        "tags": ["Terraform", "GitHub Actions", "Argo CD"],
        "desc": "A complete workflow: Terraform provisions the EKS cluster, and Argo CD immediately fills it with workloads.",
        "category": "devops",
        "diagram": SVG_TF_GITOPS,
        "problem": "Infrastructure and Application layers are frequent silos. Changes in one break the other.",
        "use_cases": ["Platform Engineering", "Bootstrap New Clusters", "Disaster Recovery"],
        "architecture": ["Terraform (EKS, VPC, IAM)", "S3 Backend (State)", "Argo CD (Bootstrap)", "GitHub Actions"],
        "steps": [
            "Step 1: Terraform creates VPC and EKS.",
            "Step 2: Terraform Helm Provider installs Argo CD.",
            "Step 3: Terraform configures Argo CD to watch the App Repo.",
            "Step 4: Cluster boots up pre-loaded with applications."
        ]
    },
    "monorepo_cicd": {
        "title": "Monorepo CI/CD with Argo CD",
        "tags": ["Monorepo", "Microservices", "Argo CD"],
        "desc": "Manage multiple microservices in a single repo with selective build triggers and independent deployments.",
        "category": "devops",
        "diagram": SVG_MONOREPO,
        "problem": "Rebuilding all 50 services when only 1 changes is inefficient and slow.",
        "use_cases": ["Microservices Backend", "Unified Frontend/Backend Repo"],
        "architecture": ["GitHub Actions 'paths' filter", "Argo CD Multi-Source", "Helm umbrella charts"],
        "steps": [
            "Step 1: Organize Monorepo (`services/cart`, `services/user`).",
            "Step 2: Configure CI path filters to only build changed folders.",
            "Step 3: Create separate Argo CD Applications for each service.",
            "Step 4: Verify that changing 'User' service only redeploys 'User'."
        ]
    },
    "dr_gitops": {
        "title": "Disaster Recovery GitOps (Multi-Region)",
        "tags": ["DR", "Route53", "Multi-Region"],
        "desc": "Achieve high availability by replicating state to a DR region using GitOps for rapid recovery.",
        "category": "devops",
        "diagram": SVG_DR_GITOPS,
        "problem": "If `us-east-1` goes down, the entire business halts.",
        "use_cases": ["Business Continuity", "Global Latency Reduction"],
        "architecture": ["Primary Cluster (US)", "DR Cluster (EU)", "Route53 DNS Failover", "Git Config Source of Truth"],
        "steps": [
            "Step 1: Spin up standby cluster in secondary region.",
            "Step 2: Point Argo CD in DR cluster to the SAME git repo.",
            "Step 3: Configure Route53 Health Checks.",
            "Step 4: Simulate outage; Route53 shifts traffic to DR."
        ]
    },
    "observability_gitops": {
        "title": "GitOps Pipeline with Observability",
        "tags": ["CloudWatch", "Observability", "SNS"],
        "desc": "Integrate monitoring into the deployment pipeline to auto-alert on failed deployments.",
        "category": "devops",
        "diagram": SVG_OBSERVABILITY,
        "problem": "Silent failures in automated pipelines lead to outages.",
        "use_cases": ["Proactive Incident Response", "SLA Monitoring"],
        "architecture": ["Amazon CloudWatch Container Insights", "Argo CD Notifications", "AWS SNS", "Slack Webhook"],
        "steps": [
            "Step 1: Enable Container Insights on EKS.",
            "Step 2: Configure CloudWatch Alarms (CPU/Error Rate).",
            "Step 3: Connect Argo CD to SNS/Slack for sync status.",
            "Step 4: Receive alert upon deployment failure."
        ]
    },
    "zero_downtime_canary": {
        "title": "Zero-Downtime Canary Deployment",
        "tags": ["Argo Rollouts", "Canary", "Strategy"],
        "desc": "Progressive delivery: Release new version to 10% of users, analyze metrics, then roll out fully.",
        "category": "devops",
        "diagram": SVG_CANARY,
        "problem": "Big Bang deployments risk affecting 100% of users with a bug.",
        "use_cases": ["A/B Testing", "Risk Mitigation"],
        "architecture": ["Argo Rollouts", "Ingress Controller (ALB/Nginx)", "AnalysisTemplate (Metrics)"],
        "steps": [
            "Step 1: Define Rollout with `setWeight: 10`.",
            "Step 2: Deploy new image tag.",
            "Step 3: Argo routes 10% traffic to canary.",
            "Step 4: Wait/Analyze. If success, increase to 100%. If fail, auto-rollback."
        ]
    }
}

def render():
    devops_img = url_for('image_file', filename='devops.png')
    projects_json = json.dumps(DEVOPS_PROJECTS)
    
    html = f"""
    <style>
        /* Copied styling for consistency with Cloud Projects */
        .card {{ background: transparent !important; box-shadow: none !important; border: none !important; padding: 0 !important; }}
        .container {{ max-width: 100% !important; padding: 0 !important; margin: 0 !important; width: 100% !important; }}

        .project-grid {{
            display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 40px; padding: 60px 40px; max-width: 1600px; margin: 0 auto; align-items: stretch;
        }}
        .project-card {{
            background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border-radius: 20px; padding: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), inset 0 0 0 1px rgba(255,255,255,0.6);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden;
            display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; cursor: pointer; z-index: 1;
        }}
        .project-card:hover {{ transform: translateY(-8px) scale(1.02); background: rgba(255,255,255,0.95); z-index: 10; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); }}
        .project-card::before {{ content: ''; position: absolute; top:0; left:0; width: 100%; height: 6px; background: linear-gradient(90deg, #3b82f6, #8b5cf6); }}
        
        .card-header {{ display: flex; justify-content: space-between; margin-bottom: 25px; }}
        .project-title {{ font-size: 1.5rem; font-weight: 800; color: #0f172a; margin: 0; padding-right: 15px; }}
        
        .project-icon {{ width: 52px; height: 52px; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1)); }}
        
        .project-tags {{ display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 25px; }}
        .tag {{ background: #eff6ff; color: #1e40af; padding: 8px 16px; border-radius: 12px; font-size: 0.75rem; font-weight: 700; border: 1px solid #dbeafe; }}
        .project-desc {{ color: #475569; font-size: 1.05rem; line-height: 1.6; margin-bottom: 30px; flex-grow: 1; font-weight: 500; }}
        
        .view-btn {{ align-self: flex-start; padding: 12px 24px; background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); color: white; border-radius: 99px; font-weight: 800; display: flex; gap: 10px; transition: all 0.3s ease; }}
        .view-btn::after {{ content: '→'; font-size: 1.25em; line-height: 1; }}

        .back-link {{ display: inline-flex; margin: 50px; color: #0f172a; font-weight: 800; text-decoration: none; background: white; padding: 16px 32px; border-radius: 9999px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); transition: all 0.3s; text-transform: uppercase; }}
        .back-link:hover {{ transform: translateY(-3px); color: #2563eb; }}

        /* Modal */
        .modal-overlay {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); opacity: 0; visibility: hidden; transition: all 0.3s; z-index: 9999; display: flex; align-items: center; justify-content: center; padding: 20px; }}
        .modal-overlay.active {{ opacity: 1; visibility: visible; }}
        .modal-content {{ background: #fff; width: 1000px; max-width: 95vw; height: 90vh; border-radius: 24px; display: flex; flex-direction: column; overflow: hidden; transform: scale(0.95); transition: all 0.3s; }}
        .modal-overlay.active .modal-content {{ transform: scale(1); }}
        .modal-header {{ background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 30px 40px; color: white; display: flex; justify-content: space-between; }}
        .modal-title {{ font-size: 2.25rem; font-weight: 800; }}
        .close-btn {{ background: rgba(255,255,255,0.2); border: none; color: white; width: 44px; height: 44px; border-radius: 50%; font-size: 24px; cursor: pointer; }}
        .modal-body {{ padding: 40px; overflow-y: auto; background: #f8fafc; color: #334155; }}
        
        .diagram-container {{ background: white; border-radius: 16px; padding: 20px; margin-bottom: 40px; border: 1px solid #e2e8f0; display: flex; justify-content: center; }}
        .arch-svg {{ width: 100%; height: auto; max-height: 350px; }}
        
        .modal-section {{ margin-bottom: 40px; background: white; padding: 30px; border-radius: 16px; border: 1px solid #e2e8f0; }}
        .modal-section h3 {{ font-size: 1.5rem; color: #0f172a; margin-top: 0; margin-bottom: 20px; font-weight: 800; }}
        
        ul.arch-list, ul.step-list {{ list-style-type: none; padding: 0; }}
        ul.arch-list li {{ background: #f8fafc; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #e2e8f0; font-weight: 600; }}
        ul.step-list li {{ position: relative; padding-left: 20px; margin-bottom: 15px; font-size: 1.05rem; }}
    </style>


    <div class="project-grid">
    """
    
    for key, proj in DEVOPS_PROJECTS.items():
        tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in proj.get("tags", [])])
        html += f"""
        <div class="project-card" onclick="openModal('{key}')">
            <div class="card-header">
                <div class="project-title">{proj['title']}</div>
                <img src="{devops_img}" alt="DevOps" class="project-icon">
            </div>
            <div class="project-tags">{tags_html}</div>
            <div class="project-desc">{proj['desc']}</div>
            <div class="view-btn">View Details</div>
        </div>
        """
        
    html += f"""
    </div>
    <div style="text-align: center; margin-bottom: 40px;">
        <a href="/projects" class="back-link">← Back to Projects</a>
    </div>

    <!-- MODAL -->
    <div class="modal-overlay" id="projectModal" onclick="closeModal(event)">
        <div class="modal-content">
            <div class="modal-header">
                <div class="modal-title" id="mTitle"></div>
                <button class="close-btn" onclick="closeModal(event)">&times;</button>
            </div>
            <div class="modal-body">
                <div class="modal-section">
                    <h3>Architecture:</h3>
                    <div class="diagram-container" id="mDiagram"></div>
                </div>
                <div class="modal-section">
                    <h3>⚠️ Problem</h3>
                    <div id="mProblem" style="font-size: 1.1rem; color: #b91c1c; font-weight: 500;"></div>
                </div>
                <div class="modal-section">
                    <h3>🏗️ Architecture</h3>
                    <ul class="arch-list" id="mArch"></ul>
                </div>
                <div class="modal-section">
                    <h3>Steps:</h3>
                    <ul class="step-list" id="mSteps"></ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        const projects = {projects_json};
        function openModal(key) {{
            const proj = projects[key];
            document.getElementById('mTitle').innerText = proj.title;
            document.getElementById('mDiagram').innerHTML = proj.diagram;
            document.getElementById('mProblem').innerText = proj.problem;
            
            const archList = document.getElementById('mArch');
            archList.innerHTML = '';
            proj.architecture.forEach(item => {{
                const li = document.createElement('li');
                li.innerText = item;
                archList.appendChild(li);
            }});

            const stepList = document.getElementById('mSteps');
            stepList.innerHTML = '';
            proj.steps.forEach(step => {{
                const li = document.createElement('li');
                li.innerText = step;
                stepList.appendChild(li);
            }});

            document.getElementById('projectModal').classList.add('active');
        }}
        function closeModal(e) {{
            if (e.target.classList.contains('modal-overlay') || e.target.closest('.close-btn')) {{
                document.getElementById('projectModal').classList.remove('active');
            }}
        }}
    </script>
    """
    return html
