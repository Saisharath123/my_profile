
CLOUD_DEVOPS_TEST_CONTENT = {
    "title": "Cloud & DevOps",
    "description": "Master Cloud Computing (AWS, Azure, GCP) and DevOps practices (CI/CD, IaC, Kubernetes).",
    "features": [
        "Cloud Architecture Scenarios",
        "CI/CD Pipeline Troubleshooting",
        "Infrastructure as Code & Containers"
    ],
    "action_label": "Explore Assessments",
    "route": "/skill-analyzer/cloud-devops-test",
    # Using a combined image concept or fallback to cloud image for now
    "image": "cloud_logo_new.png" 
}

from .cloud_Devops_backend import CLOUD_DEVOPS_BACKEND

# Separate content dictionaries for individual module access if needed
AWS_CONTENT = CLOUD_DEVOPS_BACKEND['aws']
AWS_CONTENT['action_label'] = "Start AWS Assessment"
AWS_CONTENT['route'] = "/skill-analyzer/cloud-devops-test/aws"
AWS_CONTENT['features'] = ["EC2, S3, RDS mastery", "IAM & Security policies", "Serverless (Lambda) scenarios"]

AZURE_CONTENT = CLOUD_DEVOPS_BACKEND['azure']
AZURE_CONTENT['action_label'] = "Start Azure Assessment"
AZURE_CONTENT['route'] = "/skill-analyzer/cloud-devops-test/azure"
AZURE_CONTENT['features'] = ["Azure VMs & VNets", "Azure Active Directory", "App Services & Functions"]

GCP_CONTENT = CLOUD_DEVOPS_BACKEND['gcp']
GCP_CONTENT['action_label'] = "Start GCP Assessment"
GCP_CONTENT['route'] = "/skill-analyzer/cloud-devops-test/gcp"
GCP_CONTENT['features'] = ["GCE & GKE Fundamentals", "BigQuery & Dataflow", "Google Cloud Storage classes"]

DEVOPS_CONTENT_SUB = CLOUD_DEVOPS_BACKEND['devops']
DEVOPS_CONTENT_SUB['title'] = "Cloud & DevOps"
DEVOPS_CONTENT_SUB['description'] = "Evaluate your proficiency in CI/CD, Containerization, and IaC."
DEVOPS_CONTENT_SUB['features'] = [
    "Pipeline troubleshooting",
    "Docker & Kubernetes labs",
    "Infrastructure automation"
]
DEVOPS_CONTENT_SUB['action_label'] = "Start DevOps Assessment"
DEVOPS_CONTENT_SUB['route'] = "/skill-analyzer/cloud-devops-test/devops"
DEVOPS_CONTENT_SUB['image'] = "cloud_devops_transparent.png"
