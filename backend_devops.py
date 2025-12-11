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
        {"id": "eks", "label": "Amazon EKS", "image": "/images/AWS.png"},
        {"id": "aks", "label": "Azure AKS", "image": "/images/devops_images/azure.png"},
        {"id": "gke", "label": "Google GKE", "image": "/images/devops_images/gcp.png"},
        {"id": "anthos", "label": "Google Anthos", "image": "/images/devops_images/gcp.png"}
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
