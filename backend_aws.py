# backend_aws.py
# Backend content definition for AWS Solution Architect Modules
# Structured as a list of dictionaries for easier iteration and rendering.

# Base URL for icons (using a reliable source for official AWS icons)
# We will use specific URLs for better accuracy, but this variable helps if we need to switch CDNs.
ICON_BASE = "https://icon.icepanel.io/AWS/svg" 

# Local Image Path Helper
def local_img(filename):
    return f"/images/aws_images/{filename}"

AWS_MODULES = [
    {
        "id": "compute",
        "title": "Compute",
        # REVERTED TO LOCAL IMAGE
        "image": local_img("compute.svg"), 
        "description": "Compute services are the backbone of your AWS infrastructure. Master virtual servers, serverless, and scaling.",
        "services": [
            {
                "name": "Amazon EC2",
                "image": f"{ICON_BASE}/Compute/EC2.svg",
                "description": "Scalable virtual servers in the cloud."
            },
            {
                "name": "Auto Scaling",
                "image": f"{ICON_BASE}/Compute/EC2-Auto-Scaling.svg",
                "description": "Maintains application availability and capacity."
            },
            {
                "name": "Elastic Load Balancing",
                "image": f"{ICON_BASE}/Networking-Content-Delivery/Elastic-Load-Balancing.svg",
                "description": "Distributes incoming traffic across targets."
            },
            {
                "name": "AWS Lambda",
                "image": f"{ICON_BASE}/Compute/Lambda.svg",
                "description": "Run code without provisioning servers."
            },
            {
                "name": "Amazon Lightsail",
                "image": f"{ICON_BASE}/Compute/Lightsail.svg",
                "description": "Easy-to-use cloud platform."
            }
        ]
    },
    {
        "id": "storage",
        "title": "Storage",
        "image": local_img("storage.svg"),
        "description": "Durable, scalable, and secure storage solutions for any data type.",
        "services": [
            {
                "name": "Amazon S3",
                "image": f"{ICON_BASE}/Storage/Simple-Storage-Service.svg",
                "description": "Object storage built to store and retrieve data."
            },
            {
                "name": "Amazon EBS",
                "image": f"{ICON_BASE}/Storage/Elastic-Block-Store.svg",
                "description": "Block storage for EC2 instances."
            },
            {
                "name": "Amazon EFS",
                "image": f"{ICON_BASE}/Storage/Elastic-File-System.svg",
                "description": "Serverless, fully elastic file storage."
            },
            {
                "name": "AWS Storage Gateway",
                "image": f"{ICON_BASE}/Storage/Storage-Gateway.svg",
                "description": "Hybrid cloud storage service."
            },
             {
                "name": "Amazon S3 Glacier",
                "image": f"{ICON_BASE}/Storage/S3-Glacier.svg",
                "description": "Low-cost archival storage."
            }
        ]
    },
    {
        "id": "databases",
        "title": "Databases",
        "image": local_img("databases.png"),
        "description": "Purpose-built databases for all your application needs.",
        "services": [
            {
                "name": "Amazon RDS",
                "image": f"{ICON_BASE}/Database/RDS.svg",
                "description": "Managed relational database service."
            },
            {
                "name": "Amazon DynamoDB",
                "image": f"{ICON_BASE}/Database/DynamoDB.svg",
                "description": "Fast, flexible NoSQL database service."
            },
            {
                "name": "Amazon Aurora",
                "image": f"{ICON_BASE}/Database/Aurora.svg",
                "description": "High-performance API compatible DB."
            },
            {
                "name": "Amazon Redshift",
                "image": f"{ICON_BASE}/Database/Redshift.svg",
                "description": "Fast, simple, cost-effective data warehousing."
            },
            {
                "name": "Amazon ElastiCache",
                "image": f"{ICON_BASE}/Database/ElastiCache.svg",
                "description": "In-memory data store and cache."
            }
        ]
    },
    {
        "id": "networking-and-content-delivery",
        "title": "Networking & Content Delivery",
        "image": local_img("Networking & Content Delivery.webp"),
        "description": "Isolate your cloud infrastructure and deliver content with low latency.",
        "services": [
            {
                "name": "Amazon VPC",
                "image": f"{ICON_BASE}/Networking-Content-Delivery/VPC.svg",
                "description": "Logically isolated virtual network."
            },
            {
                "name": "Amazon Route 53",
                "image": f"{ICON_BASE}/Networking-Content-Delivery/Route-53.svg",
                "description": "Scalable Domain Name System (DNS)."
            },
            {
                "name": "Amazon CloudFront",
                "image": f"{ICON_BASE}/Networking-Content-Delivery/CloudFront.svg",
                "description": "Fast Content Delivery Network (CDN)."
            },
            {
                "name": "AWS Transit Gateway",
                "image": f"{ICON_BASE}/Networking-Content-Delivery/Transit-Gateway.svg",
                "description": "Connect VPCs and on-premises networks."
            },
             {
                "name": "AWS Direct Connect",
                "image": f"{ICON_BASE}/Networking-Content-Delivery/Direct-Connect.svg",
                "description": "Dedicated network connection to AWS."
            }
        ]
    },
    {
        "id": "security-identity-and-compliance",
        "title": "Security, Identity & Compliance",
        "image": local_img("Security, Identity & Compliance.png"),
        "description": "Secure your workloads and manage identities effectively.",
        "services": [
            {
                "name": "AWS IAM",
                "image": f"{ICON_BASE}/Security-Identity-Compliance/Identity-Access-Management.svg",
                "description": "Manage access to AWS resources."
            },
            {
                "name": "AWS KMS",
                "image": f"{ICON_BASE}/Security-Identity-Compliance/Key-Management-Service.svg",
                "description": "Create and control encryption keys."
            },
            {
                "name": "AWS WAF",
                "image": f"{ICON_BASE}/Security-Identity-Compliance/WAF.svg",
                "description": "Protect web apps from common exploits."
            },
            {
                "name": "AWS Shield",
                "image": f"{ICON_BASE}/Security-Identity-Compliance/Shield.svg",
                "description": "DDoS protection service."
            },
            {
                "name": "AWS Secrets Manager",
                "image": f"{ICON_BASE}/Security-Identity-Compliance/Secrets-Manager.svg",
                "description": "Rotate, manage, and retrieve secrets."
            }
        ]
    },
    {
        "id": "monitoring",
        "title": "Monitoring & Logging",
        "image": local_img("Monitoring & Logging.png"),
        "description": "Visibility into your AWS resources and applications.",
        "services": [
            {
                "name": "Amazon CloudWatch",
                "image": f"{ICON_BASE}/Management-Governance/CloudWatch.svg",
                "description": "Observability for resources and apps."
            },
            {
                "name": "AWS CloudTrail",
                "image": f"{ICON_BASE}/Management-Governance/CloudTrail.svg",
                "description": "Track user activity and API usage."
            },
            {
                "name": "AWS Config",
                "image": f"{ICON_BASE}/Management-Governance/Config.svg",
                "description": "Assess, audit, and evaluate configurations."
            },
             {
                "name": "AWS Health",
                "image": f"{ICON_BASE}/Management-Governance/Personal-Health-Dashboard.svg",
                "description": "Visibility into resource performance."
            }
        ]
    },
    {
        "id": "application-integration",
        "title": "Application Integration",
        "image": local_img("Application Integration.png"),
        "description": "Decouple microservices and distributed systems.",
        "services": [
            {
                "name": "Amazon SQS",
                "image": f"{ICON_BASE}/Application-Integration/Simple-Queue-Service.svg",
                "description": "Fully managed message queuing."
            },
            {
                "name": "Amazon SNS",
                "image": f"{ICON_BASE}/Application-Integration/Simple-Notification-Service.svg",
                "description": "Pub/Sub messaging service."
            },
            {
                "name": "Amazon EventBridge",
                "image": f"{ICON_BASE}/Application-Integration/EventBridge.svg",
                "description": "Serverless event bus."
            },
            {
                "name": "AWS Step Functions",
                "image": f"{ICON_BASE}/Application-Integration/Step-Functions.svg",
                "description": "Visual workflow orchestration."
            },
             {
                "name": "Amazon AppFlow",
                "image": f"{ICON_BASE}/Application-Integration/AppFlow.svg",
                "description": "No-code integration for SaaS apps."
            }
        ]
    },
    {
        "id": "deployment-and-management",
        "title": "Deployment Management",
        "image": local_img("Deployment & Management.png"),
        "description": "Automate resource provisioning and infrastructure management.",
        "services": [
            {
                "name": "AWS CloudFormation",
                "image": f"{ICON_BASE}/Management-Governance/CloudFormation.svg",
                "description": "Infrastructure as Code (IaC)."
            },
            {
                "name": "AWS Systems Manager",
                "image": f"{ICON_BASE}/Management-Governance/Systems-Manager.svg",
                "description": "Unified UI for operational data."
            },
            {
                "name": "AWS Elastic Beanstalk",
                "image": f"{ICON_BASE}/Compute/Elastic-Beanstalk.svg",
                "description": "Deploy web apps effortlessly."
            },
            {
                "name": "AWS OpsWorks",
                "image": f"{ICON_BASE}/Management-Governance/OpsWorks.svg",
                "description": "Configuration management service."
            }
        ]
    },
    {
        "id": "containers",
        "title": "Containers",
        "image": local_img("Containers.svg"),
        "description": "Run containerized applications utilizing managed services.",
        "services": [
            {
                "name": "Amazon ECS",
                "image": f"{ICON_BASE}/Containers/Elastic-Container-Service.svg",
                "description": "Container orchestration service."
            },
            {
                "name": "Amazon EKS",
                "image": f"{ICON_BASE}/Containers/Elastic-Kubernetes-Service.svg",
                "description": "Managed Kubernetes service."
            },
            {
                "name": "AWS Fargate",
                "image": f"{ICON_BASE}/Containers/Fargate.svg",
                "description": "Serverless compute for containers."
            },
            {
                "name": "Amazon ECR",
                "image": f"{ICON_BASE}/Containers/Elastic-Container-Registry.svg",
                "description": "Docker container registry."
            }
        ]
    },
    {
        "id": "migration",
        "title": "Migration",
        "image": local_img("Migration.png"),
        "description": "Move data and applications to AWS quickly and securely.",
        "services": [
            {
                "name": "AWS DMS",
                "image": f"{ICON_BASE}/Migration-Transfer/Database-Migration-Service.svg",
                "description": "Migrate databases easily."
            },
            {
                "name": "AWS MGN",
                "image": f"{ICON_BASE}/Migration-Transfer/Application-Migration-Service.svg",
                "description": "Application Migration Service."
            },
            {
                "name": "AWS Snow Family",
                "image": f"{ICON_BASE}/Migration-Transfer/Snowball.svg",
                "description": "Physical migration devices."
            },
            {
                "name": "AWS DataSync",
                "image": f"{ICON_BASE}/Migration-Transfer/DataSync.svg",
                "description": "Automated data transfer."
            }
        ]
    },
    {
        "id": "analytics",
        "title": "Analytics",
        "image": local_img("Analytics.svg"),
        "description": "Derive insights with the broadest set of analytics services.",
        "services": [
            {
                "name": "Amazon Athena",
                "image": f"{ICON_BASE}/Analytics/Athena.svg",
                "description": "Query data in S3 using SQL."
            },
            {
                "name": "Amazon Kinesis",
                "image": f"{ICON_BASE}/Analytics/Kinesis.svg",
                "description": "Process streaming data."
            },
            {
                "name": "Amazon Glue",
                "image": f"{ICON_BASE}/Analytics/Glue.svg",
                "description": "Serverless data integration."
            },
            {
                "name": "Amazon QuickSight",
                "image": f"{ICON_BASE}/Analytics/QuickSight.svg",
                "description": "Business intelligence service."
            },
            {
                "name": "Amazon EMR",
                "image": f"{ICON_BASE}/Analytics/EMR.svg",
                "description": "Big data platform."
            }
        ]
    },
    {
        "id": "machine-learning",
        "title": "Machine Learning",
        "image": local_img("Machine Learning.png"),
        "description": "Build, train, and deploy ML models for any use case.",
        "services": [
            {
                "name": "Amazon SageMaker",
                "image": f"{ICON_BASE}/Machine-Learning/SageMaker.svg",
                "description": "Build, train, and deploy models."
            },
            {
                "name": "Amazon Rekognition",
                "image": f"{ICON_BASE}/Machine-Learning/Rekognition.svg",
                "description": "Image and video analysis."
            },
            {
                "name": "Amazon Polly",
                "image": f"{ICON_BASE}/Machine-Learning/Polly.svg",
                "description": "Turn text into lifelike speech."
            },
            {
                "name": "Amazon Comprehend",
                "image": f"{ICON_BASE}/Machine-Learning/Comprehend.svg",
                "description": "NLP and text analytics."
            }
        ]
    },
    {
        "id": "amazon-q",
        "title": "Amazon Q",
        "image": local_img("Amazon Q.jpg"),
        "description": "Your Generative AI assistant designed for work.",
        "services": [
            {
                "name": "Amazon Q Business",
                "image": f"{ICON_BASE}/General/Internet-of-Things.svg", # Placeholder or generic
                "description": "AI assistant for business data."
            },
            {
                "name": "Amazon Q Developer",
                "image": f"{ICON_BASE}/Developer-Tools/Developer-Tools.svg",
                "description": "AI-powered coding assistant."
            }
        ]
    },
    {
        "id": "cloud-automation",
        "title": "Cloud Automation",
        "image": local_img("cloud automation.png"),
        "description": "Modern cloud operations rely on heavy automation and IaC.",
        "services": [
            {
                "name": "Terraform",
                "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/terraform/terraform-original.svg",
                "description": "Open-source IaC tool."
            },
            {
                "name": "AWS CDK",
                "image": f"{ICON_BASE}/Developer-Tools/Cloud-Development-Kit.svg",
                "description": "Define infrastructure in code."
            },
            {
                "name": "CI/CD Pipelines",
                "image": f"{ICON_BASE}/Developer-Tools/CodePipeline.svg",
                "description": "Automate release pipelines."
            },
            {
                "name": "Automation Scripts",
                "image": f"{ICON_BASE}/Developer-Tools/CloudShell.svg",
                "description": "Scripting for operations."
            }
        ]
    }
]

# Helper to look up module by ID
def get_module(module_id):
    for m in AWS_MODULES:
        if m['id'] == module_id:
            return m
    return None
