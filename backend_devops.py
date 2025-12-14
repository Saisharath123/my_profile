# backend_devops.py
# Backend content definition for DevOps Modules

# Main text content (Legacy/Fallback)
DEVOPS_CONTENT = {
    "git-github": """
        <h2>Git & GitHub Fundamentals</h2>
        <p class="service-description">
            Version control is the backbone of modern software development. 
            Explore the tools that enable collaboration, history tracking, and code integrity.
        </p>
    """,

    "ci-cd": """
        <h2>CI/CD Pipelines</h2>
        <p class="service-description">
            Continuous Integration and Continuous Deployment allow for rapid, reliable release cycles. 
            Master the leading automation servers and cloud-native pipeline tools.
        </p>
    """,

    "docker": """
        <h2>Docker & Containerization</h2>
        <p class="service-description">
             Build, Ship, and Run any app, anywhere. Docker standardizes the environment 
             to eliminate the "it works on my machine" problem.
        </p>
    """,

    "kubernetes": """
        <h2>Container Orchestration</h2>
        <p class="service-description">
             Kubernetes (K8s) is the industry standard for automating deployment, scaling, 
             and management of containerized applications.
        </p>
    """,

    "iac-terraform": """
        <h2>Infrastructure as Code</h2>
        <p class="service-description">
             Manage and provision your infrastructure through code conventions rather than manual processes.
             Terraform is the tool of choice for platform-agnostic declarative infrastructure.
        </p>
    """,

    "config-ansible": """
        <h2>Configuration Management</h2>
        <p class="service-description">
             Ansible leverages simple YAML to automate configuration, application deployment, 
             and cloud provisioning without agents.
        </p>
    """,

    "monitoring-logging": """
        <h2>Monitoring & Logging</h2>
        <p class="service-description">
             Observability is key. Track performance, visualize metrics, and aggregate logs 
             to detect anomalies before they impact users.
        </p>
    """,

    "devsecops": """
        <h2>DevSecOps</h2>
        <p class="service-description">
             Shift security left. Integrate security checks, vulnerability scanning, 
             and compliance audit automated within the CI/CD pipeline.
        </p>
    """,

    "scripting": """
        <h2>Scripting & Automation</h2>
        <p class="service-description">
              The glue of DevOps. Use Linux shell, Bash scripting, and Python to 
             automate repetitive tasks and bridge tools together.
        </p>
    """,

    "cloud-devops": """
        <h2>Cloud DevOps</h2>
        <p class="service-description">
             leverage the power of major cloud providers (AWS, Azure, GCP) to build 
             scalable, resilient, and globally distributed systems.
        </p>
    """
}

# Sub-module definitions: The tools inside each category
DEVOPS_SUBMODULES = {
    "git-github": [
        {"id": "git", "label": "Git", "image": "/images/devops_images/git.png"},
        {"id": "github", "label": "GitHub", "image": "/images/devops_images/Git Hub.png"},
        {"id": "bitbucket", "label": "Bitbucket", "image": "/images/devops_images/bitbucket.png"}
    ],
    "ci-cd": [
        {"id": "jenkins", "label": "Jenkins", "image": "/images/devops_images/jenkins.png"},
        {"id": "github-actions", "label": "GitHub Actions", "image": "/images/devops_images/github_actions.png"},
        {"id": "gitlab-ci", "label": "GitLab CI", "image": "/images/devops_images/gitlab_ci.png"},
        {"id": "argo-cd", "label": "Argo CD", "image": "/images/devops_images/argo_cd.png"}
    ],
    "docker": [
        {"id": "docker-tool", "label": "Docker", "image": "/images/devops_images/docker.png"}
    ],
    "kubernetes": [
        {"id": "k8s", "label": "Kubernetes", "image": "/images/devops_images/k8.png"},
        {"id": "eks", "label": "Amazon EKS", "image": "/images/devops_images/eks.jpg"},
        {"id": "aks", "label": "Azure AKS", "image": "/images/devops_images/azure.png"},
        {"id": "gke", "label": "Google GKE", "image": "/images/devops_images/gke.png"},
        {"id": "anthos", "label": "Google Anthos", "image": "/images/devops_images/google_anthos.png"}
    ],
    "iac-terraform": [
        {"id": "terraform", "label": "Terraform", "image": "/images/devops_images/terraform.png"}
    ],
    "config-ansible": [
        {"id": "ansible", "label": "Ansible", "image": "/images/devops_images/ansible.webp"}
    ],
    "monitoring-logging": [
        {"id": "prometheus", "label": "Prometheus", "image": "/images/devops_images/prometheus.png"},
        {"id": "grafana", "label": "Grafana", "image": "/images/devops_images/grafana.png"},
        {"id": "aws-cloudwatch", "label": "AWS CloudWatch", "image": "/images/devops_images/aws_cloudwatch.png"},
        {"id": "aws-cloudtrail", "label": "AWS CloudTrail", "image": "/images/devops_images/aws_cloudtrail.jpg"}
    ],
    "devsecops": [
        # Based on user description, this might be a conceptual module or have specific tools.
        # If no specific tools mentioned other than "Security in...", we can put a placeholder or generic.
        # User prompt: "DevSecOps -> Security in CI/CD pipelines"
        # I will add a generic 'Security' item if no specific tool is requested, or just leave text.
        # But user pattern implies cards. I'll use the main image as a 'Concept' card if needed.
        {"id": "pipeline-security", "label": "Pipeline Security", "image": "/images/devops_images/DevSecOps.png"}
    ],
    "scripting": [
        {"id": "bash", "label": "Bash", "image": "/images/devops_images/bash.png"},
        {"id": "python", "label": "Python", "image": "/images/devops_images/python.png"}
    ],
    "cloud-devops": [
        {"id": "aws", "label": "AWS", "image": "/images/AWS.png"}, # Using main AWS image
        {"id": "azure", "label": "Azure", "image": "/images/devops_images/azure.png"},
        {"id": "gcp", "label": "GCP", "image": "/images/devops_images/gcp.png"}
    ]
}

# Detailed content for the "Back" of the module cards or detailed views
DEVOPS_TOOL_DETAILS = {
    # 1. Git
    "git": """
        <h3>Git – INTERNALS, DESIGN & REALITY</h3>
        <h4>Distributed Architecture</h4>
        <p>Git is not a file tracker, it is a directed acyclic graph (DAG) of commits.</p>
        <ul>
            <li><strong>Each commit:</strong>
                <ul>
                    <li>Has a SHA-1/SHA-256 hash</li>
                    <li>Points to a parent commit</li>
                    <li>Represents a full snapshot, not a diff</li>
                </ul>
            </li>
            <li><strong>This enables:</strong> Fast branching, Cheap merges, Offline work, Strong data integrity.</li>
        </ul>
        <h4>Internals</h4>
        <ul>
            <li><strong>Blob:</strong> file content</li>
            <li><strong>Tree:</strong> directory structure</li>
            <li><strong>Commit:</strong> snapshot + metadata</li>
            <li><strong>Ref:</strong> pointer (branch, tag)</li>
        </ul>
        <h4>Advanced Concepts</h4>
        <ul>
            <li>Detached HEAD</li>
            <li>Reflog for disaster recovery</li>
            <li>Shallow clones</li>
            <li>Submodules vs Subtrees</li>
            <li>Monorepo vs Multirepo strategies</li>
        </ul>
        <h4>Enterprise Use Cases</h4>
        <ul>
            <li>Terraform & Kubernetes Git history</li>
            <li>GitOps pipelines</li>
            <li>Audit trails for compliance</li>
            <li>Rollback of broken infra releases</li>
        </ul>
    """,

    # 2. GitHub / Bitbucket
    "github": """
        <h3>GitHub – PLATFORM DEEP DIVE</h3>
        <h4>Beyond Code Hosting</h4>
        <p>Modern Git platforms are software delivery control planes covering Code, Pipelines, Security, Collaboration, and Governance.</p>
        <h4>Pull Requests (PRs)</h4>
        <ul>
            <li>Mandatory reviews</li>
            <li>Branch protection rules</li>
            <li>Required checks</li>
            <li>Signed commits</li>
        </ul>
        <h4>Security Layer</h4>
        <ul>
            <li>Secret scanning</li>
            <li>Dependency graph</li>
            <li>Vulnerability alerts</li>
            <li>Access tokens & scopes</li>
        </ul>
        <h4>Enterprise Reality</h4>
        <p>GitHub Enterprise with SSO, Compliance (SOC2, ISO).</p>
    """,
    "bitbucket": """
        <h3>Bitbucket – PLATFORM DEEP DIVE</h3>
        <h4>Beyond Code Hosting</h4>
        <p>Modern Git platforms are software delivery control planes.</p>
        <h4>Pull Requests (PRs)</h4>
        <ul>
            <li>Mandatory reviews and Branch protection</li>
            <li>Integration with Jira workflows</li>
        </ul>
        <h4>Enterprise Reality</h4>
        <p>Bitbucket + Jira workflows, Compliance (SOC2, ISO).</p>
    """,

    # 3. CI/CD Tools
    "jenkins": """
        <h3>Jenkins – ENGINEERING VIEW</h3>
        <h4>Architecture</h4>
        <ul>
            <li>Master-agent architecture</li>
            <li>Groovy DSL for pipelines</li>
        </ul>
        <h4>Pros & Cons</h4>
        <ul>
            <li><strong>Plugin dependency hell:</strong> Needs strong maintenance.</li>
            <li><strong>Used when:</strong> Legacy environments, Heavy customization, On-prem data centers.</li>
        </ul>
        <h4>What Really Happens in CI</h4>
        <p>Code commit → Webhook → Runner picks job → Environment provisioned → Build artifacts → Tests executed → Artifacts stored → Notifications.</p>
    """,
    "github-actions": """
        <h3>GitHub Actions</h3>
        <ul>
            <li>Event-driven model</li>
            <li>Ephemeral runners</li>
            <li>YAML declarative pipelines</li>
            <li>Tight GitHub ecosystem</li>
        </ul>
        <p><strong>Best for:</strong> Cloud-native teams, Faster setup, Lower ops overhead.</p>
    """,
    "gitlab-ci": """
        <h3>GitLab CI</h3>
        <ul>
            <li>Single DevOps platform</li>
            <li>Built-in registry, security</li>
            <li>Strong Kubernetes integration</li>
        </ul>
    """,
    "argo-cd": """
        <h3>Argo CD – GITOPS CORE</h3>
        <ul>
            <li>Declarative desired state</li>
            <li>Continuous reconciliation</li>
            <li>Drift detection</li>
            <li>Pull-based deployment (secure)</li>
        </ul>
        <p><strong>Used in:</strong> Kubernetes production clusters, Regulated environments, Multi-team deployments.</p>
    """,

    # 4. Docker
    "docker-tool": """
        <h3>Docker – CONTAINER DEEP DIVE</h3>
        <h4>What Docker Actually Solves</h4>
        <p>Docker does not virtualize hardware, it uses Linux namespaces, cgroups, and shares the host kernel.</p>
        <h4>Dockerfile Best Practices</h4>
        <ul>
            <li>Multi-stage builds</li>
            <li>Minimal base images (distroless, alpine)</li>
            <li>Layer caching and Security hardening</li>
        </ul>
        <h4>Container Lifecycle</h4>
        <p>Image build → Registry push → Container runtime execution → Logs & metrics → Termination</p>
        <h4>Production Use</h4>
        <p>CI artifact packaging, Microservices, Immutable infrastructure.</p>
    """,

    # 5. Kubernetes
    "k8s": """
        <h3>Kubernetes – SYSTEMS ENGINEERING VIEW</h3>
        <h4>Control Plane Components</h4>
        <ul>
            <li>API Server, Scheduler, Controller Manager, eta (critical)</li>
        </ul>
        <h4>Core Objects</h4>
        <ul>
            <li><strong>Pod:</strong> smallest unit</li>
            <li><strong>Deployment:</strong> desired state</li>
            <li><strong>ReplicaSet:</strong> scaling</li>
            <li><strong>Service:</strong> network abstraction</li>
            <li><strong>Ingress:</strong> L7 routing</li>
        </ul>
        <h4>Networking Reality</h4>
        <p>CNI plugins, Pod-to-pod networking, Service mesh (Istio, Linkerd).</p>
        <h4>Production Use</h4>
        <p>High availability, Rolling deployments, Canary releases, Auto-scaling.</p>
    """,
    "eks": """
        <h3>Amazon EKS – Managed Kubernetes</h3>
        <p>Managed Control Plane. Worker node scaling. IAM / RBAC integration.</p>
        <p>Part of the Kubernetes ecosystem for High availability and Auto-scaling.</p>
    """,
    "aks": """
        <h3>Azure AKS – Managed Kubernetes</h3>
        <p>Managed Control Plane. Worker node scaling. IAM / RBAC integration.</p>
    """,
    "gke": """
        <h3>Google GKE – Managed Kubernetes</h3>
        <p>Managed Control Plane. Worker node scaling. IAM / RBAC integration.</p>
    """,
    "anthos": """
        <h3>Google Anthos</h3>
        <p>Hybrid and Multi-cloud Kubernetes platform.</p>
    """,

    # 6. Terraform
    "terraform": """
        <h3>Terraform – INFRASTRUCTURE ENGINEERING</h3>
        <h4>Core Concepts</h4>
        <ul>
            <li>Declarative state</li>
            <li>Dependency graph</li>
            <li>Execution plan</li>
            <li>State locking</li>
        </ul>
        <h4>State File Reality</h4>
        <ul>
            <li>Single source of truth (Needs protection)</li>
            <li>Remote backends (S3, Terraform Cloud)</li>
        </ul>
        <h4>Modules</h4>
        <p>Reusable infra components, Versioned, Team-scalable.</p>
        <h4>Enterprise Use</h4>
        <p>Multi-account AWS, DR environments, CI-driven infra changes.</p>
    """,

    # 7. Ansible
    "ansible": """
        <h3>Ansible – CONFIGURATION AT SCALE</h3>
        <h4>Agentless Architecture</h4>
        <ul>
            <li>Uses SSH, YAML based, Idempotent operations.</li>
        </ul>
        <h4>Roles & Playbooks</h4>
        <ul>
            <li>Reusable automation</li>
            <li>Environment-specific vars</li>
            <li>Secrets via vault</li>
        </ul>
        <h4>Real Use</h4>
        <p>OS hardening, Patch automation, App deployment on VMs.</p>
    """,

    # 8. Monitoring & Logging
    "prometheus": """
        <h3>Prometheus</h3>
        <ul>
            <li>Pull-based metrics</li>
            <li>Time-series DB</li>
            <li>Label-based querying (PromQL)</li>
        </ul>
    """,
    "grafana": """
        <h3>Grafana</h3>
        <ul>
            <li>Visualization layer</li>
            <li>Alerts</li>
            <li>Multi-source dashboards</li>
        </ul>
    """,
    "aws-cloudwatch": """
        <h3>CloudWatch</h3>
        <ul>
            <li>Native AWS telemetry</li>
            <li>Application logs</li>
            <li>Metrics & alarms</li>
        </ul>
    """,
    "aws-cloudtrail": """
        <h3>CloudTrail</h3>
        <ul>
            <li>API audit logs</li>
            <li>Security investigations</li>
            <li>Compliance evidence</li>
        </ul>
    """,

    # 9. DevSecOps
    "pipeline-security": """
        <h3>DevSecOps – SECURITY ENGINEERING</h3>
        <h4>Security Shift-Left</h4>
        <p>Security integrated at: Code commit, Build stage, Image creation, Deployment, Runtime.</p>
        <h4>What Gets Secured</h4>
        <ul>
            <li>Secrets, Dependencies, Containers, Infrastructure, Network policies.</li>
        </ul>
        <h4>Enterprise Outcome</h4>
        <p>Reduced breaches, Faster compliance, Secure pipelines.</p>
    """,

    # 10. Scripting
    "bash": """
        <h3>Bash</h3>
        <p>System automation, Log parsing, OS scripting.</p>
    """,
    "python": """
        <h3>Python</h3>
        <p>Cloud automation (Boto3), API orchestration, CI/CD tooling.</p>
    """,

    # Cloud DevOps
    "aws": """
        <h3>AWS</h3>
        <p>Broad service ecosystem, Production stability, Global scale.</p>
    """,
    "azure": """
        <h3>Azure</h3>
        <p>Enterprise adoption, Microsoft stack integration.</p>
    """,
    "gcp": """
        <h3>GCP</h3>
        <p>Kubernetes leadership, Data & AI.</p>
    """
}
