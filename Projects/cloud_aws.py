from flask import url_for
import json

# --- DYNAMIC SVG ARCHITECTURES ---
# Updated with CSS-based 'Marching Ants' animation for highly visible flow.

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

SVG_S3_CRR = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#64748b" /></marker></defs>
    <rect x="50" y="50" width="200" height="200" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="5,5"/>
    <text x="70" y="80" font-weight="bold" fill="#64748b">Region A</text>
    <g transform="translate(100, 120)">
        <path d="M10,0 L90,0 L80,100 L20,100 Z" fill="#FF9900"/>
        <text x="50" y="130" text-anchor="middle" font-weight="bold">Source</text>
    </g>
    <rect x="350" y="50" width="200" height="200" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="5,5"/>
    <text x="370" y="80" font-weight="bold" fill="#64748b">Region B</text>
    <g transform="translate(400, 120)">
        <path d="M10,0 L90,0 L80,100 L20,100 Z" fill="#22c55e"/>
        <text x="50" y="130" text-anchor="middle" font-weight="bold">Dest</text>
    </g>
    <!-- Flowing Line -->
    <path id="replPath" d="M190,170 C250,170 350,170 410,170" fill="none" stroke="#3b82f6" stroke-width="4" marker-end="url(#arrow)" class="flow-line"/>
    <!-- Particle -->
    <circle r="6" fill="#2563eb" class="particle"><animateMotion repeatCount="indefinite" dur="2s" keyPoints="0;1" keyTimes="0;1"><mpath href="#replPath"/></animateMotion></circle>
</svg>
"""

SVG_EFS = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <g transform="translate(250, 100)">
        <rect x="0" y="0" width="100" height="80" rx="8" fill="#4ade80"/>
        <text x="50" y="45" text-anchor="middle" fill="white" font-weight="bold">EFS</text>
    </g>
    <rect x="50" y="50" width="150" height="200" rx="8" fill="none" stroke="#94a3b8" stroke-dasharray="4"/>
    <text x="60" y="70" font-size="12" fill="#64748b">AZ 1</text>
    <rect x="75" y="150" width="100" height="60" rx="4" fill="#FF9900"/>
    <text x="125" y="185" text-anchor="middle" fill="white" font-size="12">EC2 A</text>
    <rect x="400" y="50" width="150" height="200" rx="8" fill="none" stroke="#94a3b8" stroke-dasharray="4"/>
    <text x="410" y="70" font-size="12" fill="#64748b">AZ 2</text>
    <rect x="425" y="150" width="100" height="60" rx="4" fill="#FF9900"/>
    <text x="475" y="185" text-anchor="middle" fill="white" font-size="12">EC2 B</text>
    <!-- Flowing Mount Paths -->
    <path id="mount1" d="M175,180 C210,180 230,140 250,140" fill="none" stroke="#64748b" stroke-width="3" class="flow-line"/>
    <path id="mount2" d="M425,180 C390,180 370,140 350,140" fill="none" stroke="#64748b" stroke-width="3" class="flow-line"/>
    <circle r="6" fill="#0f172a" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s"><mpath href="#mount1"/></animateMotion></circle>
    <circle r="6" fill="#0f172a" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s"><mpath href="#mount2"/></animateMotion></circle>
</svg>
"""

SVG_ALB = SVG_STYLE + """
<svg viewBox="0 0 600 350" class="arch-svg">
    <circle cx="50" cy="175" r="20" fill="#3b82f6"/>
    <text x="50" y="210" text-anchor="middle" font-size="12">User</text>
    <g transform="translate(150, 135)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#8b5cf6"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-size="10">ALB</text>
    </g>
    <rect x="300" y="20" width="250" height="310" rx="10" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="425" y="45" text-anchor="middle" font-size="14" fill="#c2410c" font-weight="bold">Auto Scaling Group</text>
    <rect x="350" y="70" width="150" height="50" rx="4" fill="#FF9900"/><text x="425" y="100" text-anchor="middle" fill="white">Instance 1</text>
    <rect x="350" y="150" width="150" height="50" rx="4" fill="#FF9900"/><text x="425" y="180" text-anchor="middle" fill="white">Instance 2</text>
    <!-- Traffic Flows -->
    <path id="path1" d="M70,175 L150,175" stroke="#3b82f6" stroke-width="3" class="flow-line"/>
    <path id="path2" d="M230,175 C290,175 290,95 350,95" fill="none" stroke="#8b5cf6" stroke-width="3" class="flow-line"/>
    <path id="path3" d="M230,175 C290,175 290,175 350,175" fill="none" stroke="#8b5cf6" stroke-width="3" class="flow-line"/>
    <circle r="6" fill="#3b82f6" class="particle"><animateMotion repeatCount="indefinite" dur="1s"><mpath href="#path1"/></animateMotion></circle>
    <circle r="6" fill="#8b5cf6" class="particle"><animateMotion repeatCount="indefinite" dur="1s" begin="0.5s"><mpath href="#path2"/></animateMotion></circle>
</svg>
"""

SVG_VPC_SEC = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <rect x="10" y="10" width="580" height="280" rx="10" fill="none" stroke="#22c55e" stroke-width="3"/>
    <text x="50" y="40" font-weight="bold" fill="#22c55e">VPC</text>
    <rect x="250" y="0" width="100" height="40" rx="5" fill="#334155"/>
    <text x="300" y="25" text-anchor="middle" fill="white" font-size="12">IGW</text>
    <rect x="50" y="80" width="220" height="180" rx="8" fill="#ecfdf5" stroke="#22c55e" stroke-dasharray="4"/>
    <text x="160" y="100" text-anchor="middle" fill="#15803d">Public Subnet</text>
    <rect x="85" y="130" width="150" height="80" rx="4" fill="#FF9900"/><text x="160" y="175" text-anchor="middle" fill="white">Web Server</text>
    <rect x="330" y="80" width="220" height="180" rx="8" fill="#f1f5f9" stroke="#64748b" stroke-dasharray="4"/>
    <text x="440" y="100" text-anchor="middle" fill="#475569">Private Subnet</text>
    <rect x="365" y="130" width="150" height="80" rx="4" fill="#3b82f6"/><text x="440" y="175" text-anchor="middle" fill="white">Database</text>
    <!-- Secure Flow -->
    <path id="vpcPath" d="M300,40 L300,80 L160,80 L160,130" fill="none" stroke="#22c55e" stroke-width="3" class="flow-line"/>
    <circle r="7" fill="#22c55e" class="particle"><animateMotion repeatCount="indefinite" dur="2s"><mpath href="#vpcPath"/></animateMotion></circle>
    <text x="440" y="290" text-anchor="middle" font-size="20">🔒</text>
</svg>
"""

SVG_IAM_FLOW = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <circle cx="50" cy="150" r="30" fill="#fca5a5"/>
    <text x="50" y="155" text-anchor="middle" fill="white" font-weight="bold">User</text>
    <g transform="translate(150, 110)">
        <rect width="100" height="80" rx="4" fill="#f8fafc" stroke="#333"/>
        <text x="50" y="30" text-anchor="middle" font-size="10">IAM Policy</text>
        <rect x="20" y="40" width="60" height="10" fill="#22c55e"/><text x="50" y="50" text-anchor="middle" font-size="8" fill="white">Allow S3</text>
        <rect x="20" y="55" width="60" height="10" fill="#ef4444"/><text x="50" y="65" text-anchor="middle" font-size="8" fill="white">Deny EC2</text>
    </g>
    <g transform="translate(450, 50)">
        <rect width="80" height="80" rx="4" fill="#FF9900"/>
        <text x="40" y="45" text-anchor="middle" fill="white">S3</text>
    </g>
    <g transform="translate(450, 170)">
        <rect width="80" height="80" rx="4" fill="#FF9900" opacity="0.5"/>
        <text x="40" y="45" text-anchor="middle" fill="white">EC2</text>
        <text x="40" y="25" text-anchor="middle" font-size="20">🚫</text>
    </g>
    <!-- Policy Flow -->
    <path id="allowPath" d="M80,150 L150,150 M250,150 L350,150 L350,90 L450,90" stroke="#22c55e" stroke-width="3" fill="none" class="flow-line"/>
    <circle r="6" fill="#22c55e" class="particle"><animateMotion repeatCount="indefinite" dur="2s" href="#allowPath"/></circle>
</svg>
"""

SVG_NAT_GW = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <rect x="50" y="50" width="200" height="200" rx="8" fill="#f1f5f9" stroke="#64748b"/>
    <text x="150" y="75" text-anchor="middle">Private Subnet</text>
    <rect x="100" y="120" width="100" height="80" rx="4" fill="#333"/>
    <text x="150" y="165" text-anchor="middle" fill="white">Server</text>
    <rect x="300" y="50" width="200" height="200" rx="8" fill="#ecfdf5" stroke="#22c55e"/>
    <text x="400" y="75" text-anchor="middle">Public Subnet</text>
    <circle cx="400" cy="160" r="40" fill="#3b82f6"/>
    <text x="400" y="165" text-anchor="middle" fill="white" font-weight="bold">NAT</text>
    <rect x="550" y="140" width="40" height="40" rx="5" fill="#333"/>
    <text x="570" y="165" text-anchor="middle" fill="white" font-size="10">IGW</text>
    <!-- NAT Flow -->
    <path id="natPath" d="M200,160 L360,160 M440,160 L550,160" stroke="#333" stroke-width="3" class="flow-line"/> 
    <circle r="6" fill="#3b82f6" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" href="#natPath"/></circle>
</svg>
"""

SVG_STATIC_SITE = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <circle cx="50" cy="150" r="20" fill="#3b82f6"/>
    <text x="50" y="185" text-anchor="middle">User</text>
    <g transform="translate(200, 110)">
        <rect width="80" height="80" fill="#8b5cf6"/>
        <text x="40" y="45" text-anchor="middle" fill="white">CloudFront</text>
        <text x="40" y="105" text-anchor="middle" font-size="10">Edge Location</text>
    </g>
    <g transform="translate(450, 110)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#FF9900"/>
        <text x="40" y="45" text-anchor="middle" fill="white">S3</text>
        <text x="40" y="105" text-anchor="middle" font-size="10">Origin</text>
    </g>
    <!-- Request Flow -->
    <path id="reqPath" d="M70,150 L200,150" stroke="#3b82f6" stroke-width="3" class="flow-line"/>
    <path id="originPath" d="M280,150 L450,150" stroke="#3b82f6" stroke-width="3" stroke-dasharray="4" class="flow-line"/>
    <circle r="6" fill="#3b82f6" class="particle"><animateMotion repeatCount="indefinite" dur="1s" href="#reqPath"/></circle>
    <circle r="6" fill="#8b5cf6" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" begin="0.5s" href="#originPath"/></circle>
</svg>
"""

SVG_TF_STATE = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <circle cx="50" cy="150" r="20" fill="#333"/><text x="50" y="190" text-anchor="middle" font-size="12">Engineer</text>
    <g transform="translate(150, 110)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#7B42BC"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-weight="bold">TF</text>
    </g>
    <g transform="translate(350, 60)">
        <path d="M10,0 L90,0 L80,100 L20,100 Z" fill="#FF9900"/>
        <text x="50" y="130" text-anchor="middle" font-weight="bold">S3 State</text>
    </g>
    <rect x="350" y="200" width="100" height="80" rx="4" fill="#3b82f6"/><text x="400" y="245" text-anchor="middle" fill="white" font-weight="bold">DynamoDB</text>
    <!-- State Flow -->
    <path id="pushPath" d="M230,150 L350,110" stroke="#7B42BC" stroke-width="3" stroke-dasharray="4" class="flow-line"/>
    <path id="lockPath" d="M230,150 L350,240" stroke="#7B42BC" stroke-width="3" stroke-dasharray="4" class="flow-line"/>
    <circle r="6" fill="#7B42BC" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" href="#pushPath"/></circle>
    <circle r="6" fill="#3b82f6" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" begin="0.5s" href="#lockPath"/></circle>
</svg>
"""

SVG_HA_WEB = SVG_STYLE + """
<svg viewBox="0 0 600 350" class="arch-svg">
    <rect x="20" y="20" width="560" height="310" rx="15" fill="#f8fafc" stroke="#22c55e" stroke-width="2" stroke-dasharray="4"/>
    <text x="60" y="50" font-weight="bold" fill="#22c55e">VPC</text>
    <g transform="translate(260, 40)">
        <polygon points="40,0 80,40 40,80 0,40" fill="#8b5cf6"/>
        <text x="40" y="45" text-anchor="middle" fill="white" font-size="10">ALB</text>
    </g>
    <rect x="50" y="130" width="220" height="180" rx="8" fill="#e0f2fe" stroke="#3b82f6"/>
    <text x="160" y="150" text-anchor="middle" fill="#1e40af">AZ 1</text>
    <rect x="80" y="170" width="60" height="60" rx="4" fill="#FF9900"/><text x="110" y="205" text-anchor="middle" fill="white">EC2</text>
    <rect x="180" y="170" width="60" height="60" rx="4" fill="#3b82f6"/><text x="210" y="205" text-anchor="middle" fill="white">RDS (P)</text>
    <rect x="330" y="130" width="220" height="180" rx="8" fill="#e0f2fe" stroke="#3b82f6"/>
    <text x="440" y="150" text-anchor="middle" fill="#1e40af">AZ 2</text>
    <rect x="360" y="170" width="60" height="60" rx="4" fill="#FF9900"/><text x="390" y="205" text-anchor="middle" fill="white">EC2</text>
    <rect x="460" y="170" width="60" height="60" rx="4" fill="#94a3b8"/><text x="490" y="205" text-anchor="middle" fill="white">RDS (S)</text>
    <path d="M240,200 L460,200" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4" class="flow-line"/>
    <!-- Load Balancing Flow -->
    <path id="trafficLeft" d="M260,80 L80,170" stroke="#3b82f6" stroke-width="3" class="flow-line"/>
    <path id="trafficRight" d="M340,80 L360,170" stroke="#3b82f6" stroke-width="3" class="flow-line"/>
    <circle r="6" fill="#22c55e" class="particle"> <animateMotion repeatCount="indefinite" dur="1s" href="#trafficLeft"/> </circle>
    <circle r="6" fill="#22c55e" class="particle"> <animateMotion repeatCount="indefinite" dur="1s" begin="0.5s" href="#trafficRight"/> </circle>
</svg>
"""

SVG_ECS = SVG_STYLE + """
<svg viewBox="0 0 600 300" class="arch-svg">
    <g transform="translate(50, 100)">
        <rect width="60" height="80" rx="4" fill="#FF9900"/>
        <text x="30" y="45" text-anchor="middle" fill="white">ECR</text>
    </g>
    <rect x="180" y="50" width="240" height="200" rx="10" fill="#fff7ed" stroke="#FF9900" stroke-width="2"/>
    <text x="300" y="80" text-anchor="middle" font-weight="bold" fill="#c2410c">ECS Fargate</text>
    <rect x="200" y="100" width="200" height="60" rx="4" fill="#22c55e" opacity="0.1"/>
    <rect x="210" y="110" width="40" height="40" rx="4" fill="#22c55e"/><rect x="260" y="110" width="40" height="40" rx="4" fill="#22c55e"/>
    <g transform="translate(480, 100)">
        <rect width="60" height="60" rx="4" fill="#d946ef"/>
        <text x="30" y="35" text-anchor="middle" fill="white" font-size="10">Logs</text>
    </g>
    <!-- Deployment Flow -->
    <path id="pullPath" d="M110,130 L180,130" stroke="#FF9900" stroke-width="3" class="flow-line"/>
    <path id="logPath" d="M420,130 L480,130" stroke="#d946ef" stroke-width="3" stroke-dasharray="4" class="flow-line"/>
    <circle r="6" fill="#FF9900" class="particle"><animateMotion repeatCount="indefinite" dur="1.5s" href="#pullPath"/></circle>
    <circle r="6" fill="#d946ef" class="particle"><animateMotion repeatCount="indefinite" dur="1s" href="#logPath"/></circle>
</svg>
"""

AWS_PROJECTS = {
    "terraform_iac": {
        "title": "Infrastructure as Code with Terraform & S3 State",
        "tags": ["Terraform", "S3", "DynamoDB", "IaC"],
        "desc": "Manage AWS infrastructure reliably using Terraform with remote state storage in S3 and state locking via DynamoDB.",
        "category": "cloud",
        "diagram": SVG_TF_STATE,
        "problem": "Storing Terraform state files locally is risky; if the developer's laptop dies, the state is lost. Furthermore, in teams, two people running 'apply' simultaneously can corrupt the infrastructure.",
        "use_cases": ["Team Collaboration", "CI/CD Integration", "Audit & Rollback"],
        "architecture": ["Terraform Backend (S3)", "S3 Bucket (Versioning)", "DynamoDB (Locking)", "IAM Policy", "Lifecycle Rules"],
        "steps": ["Step 1: Create S3 bucket & DynamoDB table.", "Step 2: Define backend.tf.", "Step 3: terraform init.", "Step 4: terraform apply.", "Step 5: Verify Lock."]
    },
    "ha_webapp": {
        "title": "Highly Available Web App (Multi-AZ)",
        "tags": ["AWS", "EC2", "ALB", "RDS", "Auto Scaling"],
        "desc": "Deploy a fault-tolerant web application spanning multiple Availability Zones with auto-healing capabilities and a managed database.",
        "category": "cloud",
        "diagram": SVG_HA_WEB,
        "problem": "Single-server deployments represent a Single Point of Failure (SPOF).",
        "use_cases": ["Mission Critical Apps", "High Traffic Sites", "Enterprise CMS"],
        "architecture": ["VPC (Multi-AZ)", "ALB", "Auto Scaling Group", "RDS (Multi-AZ)", "Security Groups"],
        "steps": ["Step 1: Create VPC.", "Step 2: Launch RDS Multi-AZ.", "Step 3: Create ALB.", "Step 4: Create ASG.", "Step 5: Test Failover."]
    },
    "ecs_containers": {
        "title": "Containerized Microservices with ECS Fargate",
        "tags": ["AWS", "Docker", "ECS", "Fargate"],
        "desc": "Deploy scalable, serverless containerized applications using Amazon ECS Fargate and ECR.",
        "category": "cloud",
        "diagram": SVG_ECS,
        "problem": "Managing EC2 instances for containers is heavy operational overhead.",
        "use_cases": ["Microservices", "Batch Processing", "Web APIs"],
        "architecture": ["Docker Image", "ECR", "ECS Cluster", "Fargate Task", "CloudWatch"],
        "steps": ["Step 1: Build Docker image.", "Step 2: Push to ECR.", "Step 3: Create Task Def.", "Step 4: Deploy Service.", "Step 5: Check Logs."]
    },
    "s3_crr": {
        "title": "Cross-Region Replication in Amazon S3",
        "tags": ["AWS", "S3", "Disaster Recovery"],
        "desc": "Implement robust disaster recovery by configuring Cross-Region Replication (CRR).",
        "category": "cloud",
        "diagram": SVG_S3_CRR,
        "problem": "Data loss risks due to regional outages.",
        "use_cases": ["Compliance", "Disaster Recovery", "Latency Reduction"],
        "architecture": ["Source Bucket", "Dest Bucket", "IAM Role", "Replication Rules"],
        "steps": ["Step 1: Create Source/Dest Buckets.", "Step 2: Enable Versioning.", "Step 3: Create Replication Rule.", "Step 4: Verify Copy."]
    },
    "efs_ec2": {
        "title": "Scalable Shared Storage with EFS",
        "tags": ["AWS", "EFS", "EC2", "Linux"],
        "desc": "Architect a scalable, shared file storage solution using Amazon EFS mounted on multiple instances.",
        "category": "cloud",
        "diagram": SVG_EFS,
        "problem": "EBS volumes are AZ-locked and not shared.",
        "use_cases": ["CMS (WordPress)", "Shared CI/CD", "Data Science"],
        "architecture": ["EFS File System", "Mount Targets", "Security Groups", "NFS Client"],
        "steps": ["Step 1: Create EFS.", "Step 2: Create Mount Targets.", "Step 3: Mount on EC2.", "Step 4: Write/Read test."]
    },
    "alb_asg": {
        "title": "Load Balancing & Auto Scaling",
        "tags": ["AWS", "ALB", "ASG"],
        "desc": "Design infrastructure that scales automatically with traffic using ALB and ASG.",
        "category": "cloud",
        "diagram": SVG_ALB,
        "problem": "Static provisioning wastes money or crashes under load.",
        "use_cases": ["E-Commerce Spikes", "SaaS Apps"],
        "architecture": ["ALB", "Target Group", "Launch Template", "Auto Scaling Group"],
        "steps": ["Step 1: Create Security Groups.", "Step 2: Create ALB.", "Step 3: Create Launch Template.", "Step 4: Create ASG.", "Step 5: Stress Test."]
    },
    "vpc_security": {
        "title": "Secure VPC Architecture",
        "tags": ["AWS", "VPC", "Security"],
        "desc": "Build a secure network foundation with isolated subnets for backend systems.",
        "category": "cloud",
        "diagram": SVG_VPC_SEC,
        "problem": "Default VPCs lack strict isolation.",
        "use_cases": ["Multi-Tier Apps", "Compliance", "Data Security"],
        "architecture": ["Public Subnet (DMZ)", "Private Subnet (App)", "IGW", "Route Tables"],
        "steps": ["Step 1: Create Custom VPC.", "Step 2: Create Subnets.", "Step 3: Config Routes.", "Step 4: Test Connectivity."]
    },
    "iam_user_mgmt": {
        "title": "IAM Identity & Access Management",
        "tags": ["AWS", "IAM", "Security"],
        "desc": "Implement granular access control using IAM policies, groups, and roles.",
        "category": "cloud",
        "diagram": SVG_IAM_FLOW,
        "problem": "Root access is dangerous; permissions need to be least-privilege.",
        "use_cases": ["Employee Access", "Auditing"],
        "architecture": ["IAM Users", "Groups", "Policies", "MFA"],
        "steps": ["Step 1: Create Groups.", "Step 2: Define Policies.", "Step 3: Create Users.", "Step 4: Enforce MFA."]
    },
    "nat_gateway": {
        "title": "NAT Gateway for Private Subnets",
        "tags": ["AWS", "VPC", "Networking"],
        "desc": "Enable private instances to access the internet securely without incoming exposure.",
        "category": "cloud",
        "diagram": SVG_NAT_GW,
        "problem": "Private servers need updates but should not have Public IPs.",
        "use_cases": ["Patching", "3rd Party APIs"],
        "architecture": ["NAT Gateway", "Public Subnet", "Private Route Table"],
        "steps": ["Step 1: Allocate EIP.", "Step 2: Create NAT GW.", "Step 3: Update Routes."]
    },
    "static_site": {
        "title": "Static Website with CloudFront + S3",
        "tags": ["AWS", "S3", "CloudFront"],
        "desc": "Host a global, low-latency secure website using S3 and CloudFront.",
        "category": "cloud",
        "diagram": SVG_STATIC_SITE,
        "problem": "S3 hosting lacks HTTPS and has high latency globally.",
        "use_cases": ["Portfolios", "React Apps"],
        "architecture": ["S3 Origin", "CloudFront", "OAC", "Route53"],
        "steps": ["Step 1: Upload Content.", "Step 2: Create CloudFront.", "Step 3: Config OAC.", "Step 4: DNS Setup."]
    }
}

def render():
    aws_img = url_for('image_file', filename='aws_icon.png')
    
    # Serialize projects to JSON for JS to use
    projects_json = json.dumps(AWS_PROJECTS)
    
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
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); /* Auto-fill with proper min width */
            gap: 40px; /* Increased gap */
            padding: 60px 40px;
            max-width: 1600px;
            margin: 0 auto;
            align-items: stretch; /* Stretch items to same height */
        }}

        .project-card {{
            background: rgba(255, 255, 255, 0.85); /* Slightly clearer */
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 35px;
            box-shadow: 
                0 4px 6px -1px rgba(0, 0, 0, 0.05),
                0 10px 15px -3px rgba(0, 0, 0, 0.05),
                inset 0 0 0 1px rgba(255, 255, 255, 0.6); /* Inner light border */
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Springy transition */
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: auto;
            min-height: 400px; /* Enforced min height */
            cursor: pointer;
            z-index: 1;
        }}

        .project-card:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: 
                0 20px 25px -5px rgba(0, 0, 0, 0.1), 
                0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border-color: rgba(255, 153, 0, 0.5);
            background: rgba(255, 255, 255, 0.95);
            z-index: 10;
        }}

        .project-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%; /* Top border instead of left side */
            height: 6px;
            background: linear-gradient(90deg, #FF9900, #F58529, #fbbf24); 
        }}

        .project-card::after {{
            content: '';
            position: absolute;
            bottom: -50px;
            right: -50px;
            width: 120px;
            height: 120px;
            background: radial-gradient(circle, rgba(255, 153, 0, 0.08) 0%, rgba(255,255,255,0) 70%);
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
            background: #fff7ed; 
            color: #c2410c;
            padding: 8px 16px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 700;
            border: 1px solid #ffedd5;
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
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            color: white;
            border-radius: 99px;
            font-size: 0.9rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 6px -1px rgba(234, 88, 12, 0.3);
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
        }}
        .project-card:hover .view-btn {{
            transform: translateX(5px);
            box-shadow: 0 10px 15px -3px rgba(234, 88, 12, 0.4);
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
            color: #ea580c;
        }}

        /* MODAL STYLES */
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
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            padding: 30px 40px;
            color: white;
            flex-shrink: 0;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }}
        .modal-title-group {{
            flex: 1;
        }}
        .modal-title {{
            font-size: 2.25rem;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 12px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .modal-tags {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .modal-tag {{
            background: rgba(255, 255, 255, 0.25);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            backdrop-filter: blur(4px);
        }}

        .close-btn {{
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px; height: 44px;
            border-radius: 50%;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            margin-left: 20px;
        }}
        .close-btn:hover {{
            background: white;
            color: #ea580c;
            transform: rotate(90deg);
        }}

        .modal-body {{
            padding: 40px;
            overflow-y: auto;
            color: #334155;
            background: #f8fafc;
        }}

        /* Dynamic Diagram Container */
        .diagram-container {{
            background: white;
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 40px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid #e2e8f0;
            display: flex;
            justify-content: center;
        }}
        .arch-svg {{
            width: 100%;
            height: auto;
            max-height: 350px;
        }}

        .modal-section {{
            margin-bottom: 40px;
            background: white;
            padding: 30px;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        }}
        .modal-section h3 {{
            font-size: 1.5rem;
            color: #0f172a;
            margin-top: 0;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 800;
            letter-spacing: -0.025em;
        }}
        
        .problem-box {{
            background: #fff1f2;
            border-left: 6px solid #e11d48;
            padding: 20px 25px;
            border-radius: 8px;
            font-size: 1.05rem;
            color: #9f1239;
            line-height: 1.7;
        }}

        .use-case-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }}
        .use-case-card {{
            background: #f0f9ff;
            padding: 15px 20px;
            border-radius: 10px;
            border: 1px solid #bae6fd;
            color: #0369a1;
            font-weight: 600;
        }}

        .step-list {{
            list-style: none;
            padding: 0;
            counter-reset: step-counter;
        }}
        .step-list li {{
            position: relative;
            padding-left: 60px;
            margin-bottom: 25px;
            font-size: 1.05rem;
            line-height: 1.6;
        }}
        .step-list li:last-child {{
            margin-bottom: 0;
        }}
        .step-list li::before {{
            counter-increment: step-counter;
            content: counter(step-counter);
            position: absolute;
            left: 0;
            top: -2px;
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            color: white;
            border-radius: 50%;
            text-align: center;
            line-height: 36px;
            font-weight: bold;
            font-size: 1rem;
            box-shadow: 0 4px 6px -1px rgba(249, 115, 22, 0.3);
        }}
        .step-list li strong {{
            display: block;
            color: #0f172a;
            font-weight: 700;
            margin-bottom: 4px;
            font-size: 1.1rem;
        }}

        ul.arch-list {{
            list-style-type: none;
            padding: 0;
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
        }}
        ul.arch-list li {{
            background: #f8fafc;
            padding: 16px 20px;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            font-weight: 500;
            color: #334155;
        }}
        ul.arch-list li::before {{
            content: '⚙️';
            margin-right: 15px;
            font-size: 1.2rem;
        }}

    </style>
    

    <div class="project-grid">
    """
    
    for key, proj in AWS_PROJECTS.items():
        tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in proj.get("tags", [])])
        html += f"""
        <div class="project-card" onclick="openModal('{key}')">
            <div class="card-header">
                <div class="project-title">{proj['title']}</div>
                <img src="{aws_img}" alt="AWS" class="project-icon">
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

    <!-- MODAL COMPONENT -->
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
                
                <!-- Dynamic Diagram Section -->
                <div class="modal-section" style="background: transparent; border: none; box-shadow: none; padding: 0;">
                    <h3 style="margin-bottom: 15px; color: #1e293b;">Architecture:</h3>
                    <div class="diagram-container" id="mDiagram">
                        <!-- SVG injected here -->
                    </div>
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
        const awsProjects = {projects_json};

        function openModal(key) {{
            const proj = awsProjects[key];
            if (!proj) return;

            document.getElementById('mTitle').innerText = proj.title;
            document.getElementById('mProblem').innerText = proj.problem;
            
            // Diagram
            document.getElementById('mDiagram').innerHTML = proj.diagram || '<div style="padding:20px; color:#64748b;">Diagram coming soon...</div>';

            // Tags
            const tagsContainer = document.getElementById('mTags');
            tagsContainer.innerHTML = '';
            proj.tags.forEach(tag => {{
                const span = document.createElement('span');
                span.className = 'modal-tag';
                span.innerText = tag;
                tagsContainer.appendChild(span);
            }});

            // Use Cases
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

            // Architecture
            const archContainer = document.getElementById('mArch');
            archContainer.innerHTML = '';
            proj.architecture.forEach(item => {{
                const li = document.createElement('li');
                li.innerText = item;
                archContainer.appendChild(li);
            }});

            // Steps
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
