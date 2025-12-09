# backend_aws.py
# Backend content definition for AWS Solution Architect Modules
# Structured as a list of dictionaries for easier iteration and rendering.

# Base URL for icons (using a reliable source for official AWS icons)
ICON_BASE = "https://icon.icepanel.io/AWS/svg" 

# Local Image Path Helper
def local_img(filename):
    return f"/images/aws_images/{filename}"

def local_backend_img(filename):
    return f"/images/aws backend modules/{filename}"

AWS_MODULES = [
    {
        "id": "compute",
        "title": "Compute",
        "image": local_img("compute.svg"), 
        "description": "Compute services are the backbone of your AWS infrastructure. Master virtual servers, serverless, and scaling.",
        "services": [
            {"name": "Amazon EC2", "image": f"{ICON_BASE}/Compute/EC2.svg", "description": "Scalable virtual servers in the cloud."},
            {"name": "EC2 Auto Scaling", "image": f"{ICON_BASE}/Compute/EC2-Auto-Scaling.svg", "description": "Maintains application availability and capacity."},
            {"name": "Elastic Load Balancing", "image": f"{ICON_BASE}/Networking-Content-Delivery/Elastic-Load-Balancing.svg", "description": "Distributes incoming traffic across targets."},
            {"name": "AWS Lambda", "image": f"{ICON_BASE}/Compute/Lambda.svg", "description": "Run code without provisioning servers."},
            {"name": "AWS Elastic Beanstalk", "image": f"{ICON_BASE}/Compute/Elastic-Beanstalk.svg", "description": "Deploy web apps effortlessly."},
             {"name": "Amazon Lightsail", "image": f"{ICON_BASE}/Compute/Lightsail.svg", "description": "Easy-to-use cloud platform."},
        ]
    },
    {
        "id": "storage",
        "title": "Storage",
        "image": local_img("storage.svg"),
        "description": "Durable, scalable, and secure storage solutions for any data type.",
        "services": [
            {"name": "Amazon S3", "image": f"{ICON_BASE}/Storage/Simple-Storage-Service.svg", "description": "Object storage built to store and retrieve data."},
            {"name": "Amazon EBS", "image": f"{ICON_BASE}/Storage/Elastic-Block-Store.svg", "description": "Block storage for EC2 instances."},
            {"name": "Amazon EFS", "image": local_backend_img("amazon_efs.png"), "description": "Serverless, fully elastic file storage."},
            {"name": "Amazon S3 Glacier", "image": local_backend_img("amazon glacier.png"), "description": "Low-cost archival storage."},
            {"name": "AWS Backup", "image": f"{ICON_BASE}/Storage/Backup.svg", "description": "Centralized backup service."},
            {"name": "Amazon FSx", "image": f"{ICON_BASE}/Storage/FSx.svg", "description": "File storage for diverse workloads."}
        ]
    },
    {
        "id": "databases",
        "title": "Databases",
        "image": local_img("databases.png"),
        "description": "Purpose-built databases for all your application needs.",
        "services": [
            {"name": "Amazon RDS", "image": f"{ICON_BASE}/Database/RDS.svg", "description": "Managed relational database service."},
            {"name": "Amazon Aurora", "image": f"{ICON_BASE}/Database/Aurora.svg", "description": "High-performance API compatible DB."},
            {"name": "Amazon DynamoDB", "image": f"{ICON_BASE}/Database/DynamoDB.svg", "description": "Fast, flexible NoSQL database service."},
            {"name": "Amazon ElastiCache", "image": f"{ICON_BASE}/Database/ElastiCache.svg", "description": "In-memory data store and cache."},
            {"name": "Amazon Redshift", "image": local_backend_img("amazon_redshirt.png"), "description": "Fast, simple, cost-effective data warehousing."},
             {"name": "Amazon DocumentDB", "image": local_backend_img("Amazon DocumentDB.png"), "description": "Fast, scalable, fully managed MongoDB-compatible database."}
        ]
    },
    {
        "id": "networking-and-content-delivery",
        "title": "Networking & Content Delivery",
        "image": local_img("Networking & Content Delivery.webp"),
        "description": "Isolate your cloud infrastructure and deliver content with low latency.",
        "services": [
            {"name": "Amazon VPC", "image": local_backend_img("Amazon VPC.png"), "description": "Logically isolated virtual network."},
            
            {"name": "Internet Gateway", "image": local_backend_img("Internet Gateway.png"), "description": "Connects VPC to the internet."}, 
            {"name": "NAT Gateway", "image": local_backend_img("NAT Gateway.png"), "description": "Internet across for private subnets."},
            {"name": "VPC Peering", "image": local_backend_img("VPC Peering.png"), "description": "Connect two VPCs."},
            {"name": "Security Groups", "image": f"{ICON_BASE}/Security-Identity-Compliance/Firewall-Manager.svg", "description": "Virtual firewall for EC2 instances."},
             
            {"name": "AWS Transit Gateway", "image": f"{ICON_BASE}/Networking-Content-Delivery/Transit-Gateway.svg", "description": "Connect VPCs and on-premises networks."},
            {"name": "AWS Site-to-Site VPN", "image": f"{ICON_BASE}/Networking-Content-Delivery/Site-to-Site-VPN.svg", "description": "Secure connection to on-premises."},
            {"name": "AWS Direct Connect", "image": f"{ICON_BASE}/Networking-Content-Delivery/Direct-Connect.svg", "description": "Dedicated network connection to AWS."},
            {"name": "Amazon Route 53", "image": f"{ICON_BASE}/Networking-Content-Delivery/Route-53.svg", "description": "Scalable Domain Name System (DNS)."},
            {"name": "Amazon CloudFront", "image": f"{ICON_BASE}/Networking-Content-Delivery/CloudFront.svg", "description": "Fast Content Delivery Network (CDN)."}
        ]
    },
    {
        "id": "security-identity-and-compliance",
        "title": "Security, Identity & Compliance",
        "image": local_img("Security, Identity & Compliance.png"),
        "description": "Secure your workloads and manage identities effectively.",
        "services": [
            {"name": "AWS IAM", "image": local_backend_img("AWS IAM.png"), "description": "Manage access to AWS resources."},
            {"name": "AWS IAM Identity Center (SSO)", "image": f"{ICON_BASE}/Security-Identity-Compliance/IAM-Identity-Center.svg", "description": "Manage workforce access."},
            {"name": "AWS Organizations", "image": f"{ICON_BASE}/Management-Governance/Organizations.svg", "description": "Central governance and management."},
            {"name": "AWS KMS", "image": f"{ICON_BASE}/Security-Identity-Compliance/Key-Management-Service.svg", "description": "Create and control encryption keys."},
            {"name": "AWS Secrets Manager", "image": f"{ICON_BASE}/Security-Identity-Compliance/Secrets-Manager.svg", "description": "Rotate, manage, and retrieve secrets."},
            {"name": "AWS Certificate Manager (ACM)", "image": f"{ICON_BASE}/Security-Identity-Compliance/Certificate-Manager.svg", "description": "Provision, manage, and deploy SSL/TLS certificates."},
            {"name": "AWS WAF", "image": f"{ICON_BASE}/Security-Identity-Compliance/WAF.svg", "description": "Protect web apps from common exploits."},
            {"name": "AWS Shield", "image": f"{ICON_BASE}/Security-Identity-Compliance/Shield.svg", "description": "DDoS protection service."},
            {"name": "Amazon GuardDuty", "image": f"{ICON_BASE}/Security-Identity-Compliance/GuardDuty.svg", "description": "Intelligent threat detection."},
            {"name": "AWS Security Hub", "image": f"{ICON_BASE}/Security-Identity-Compliance/Security-Hub.svg", "description": "Unified security and compliance center."},
            {"name": "AWS Config", "image": f"{ICON_BASE}/Management-Governance/Config.svg", "description": "Assess, audit, and evaluate configurations."}
        ]
    },
    {
        "id": "monitoring",
        "title": "Monitoring & Logging",
        "image": local_img("Monitoring & Logging.png"),
        "description": "Visibility into your AWS resources and applications.",
        "services": [
            {"name": "Amazon CloudWatch", "image": f"{ICON_BASE}/Management-Governance/CloudWatch.svg", "description": "Observability for resources and apps."},
            {"name": "AWS CloudTrail", "image": f"{ICON_BASE}/Management-Governance/CloudTrail.svg", "description": "Track user activity and API usage."},
            {"name": "AWS X-Ray", "image": f"{ICON_BASE}/Developer-Tools/X-Ray.svg", "description": "Analyze and debug distributed applications."},
             {"name": "AWS Trusted Advisor", "image": f"{ICON_BASE}/Management-Governance/Trusted-Advisor.svg", "description": "Reduce costs and improve performance."}
        ]
    },
    {
        "id": "application-integration",
        "title": "Application Integration",
        "image": local_img("Application Integration.png"),
        "description": "Decouple microservices and distributed systems.",
        "services": [
            {"name": "Amazon SNS", "image": local_backend_img("Amazon SNS.png"), "description": "Pub/Sub messaging service."},
            {"name": "Amazon SQS", "image": local_backend_img("Amazon SQS.jpg"), "description": "Fully managed message queuing."},
            {"name": "Amazon EventBridge", "image": local_backend_img("Amazon EventBridge.jpg"), "description": "Serverless event bus."},
            {"name": "AWS Step Functions", "image": local_backend_img("AWS Step Functions.jpg"), "description": "Visual workflow orchestration."},
             {"name": "Amazon MQ", "image": local_backend_img("Amazon MQ.jpg"), "description": "Managed message broker Service."},
             {"name": "AWS AppSync", "image": local_backend_img("AWS AppSync.svg"), "description": "Accelerate app development with GraphQL APIs."}
        ]
    },
    {
        "id": "deployment-and-management",
        "title": "Deployment Management",
        "image": local_img("Deployment & Management.png"),
        "description": "Automate resource provisioning and infrastructure management.",
        "services": [
            {"name": "AWS CloudFormation", "image": f"{ICON_BASE}/Management-Governance/CloudFormation.svg", "description": "Infrastructure as Code (IaC)."},
            {"name": "AWS CDK", "image": f"{ICON_BASE}/Developer-Tools/Cloud-Development-Kit.svg", "description": "Define infrastructure in code."},
            {"name": "AWS Systems Manager", "image": f"{ICON_BASE}/Management-Governance/Systems-Manager.svg", "description": "Unified UI for operational data."},
            {"name": "AWS CodeCommit", "image": f"{ICON_BASE}/Developer-Tools/CodeCommit.svg", "description": "Secure Git-based repositories."},
            {"name": "AWS CodeBuild", "image": f"{ICON_BASE}/Developer-Tools/CodeBuild.svg", "description": "Build and test code."},
            {"name": "AWS CodeDeploy", "image": f"{ICON_BASE}/Developer-Tools/CodeDeploy.svg", "description": "Automate code deployments."},
            {"name": "AWS CodePipeline", "image": f"{ICON_BASE}/Developer-Tools/CodePipeline.svg", "description": "Automate release pipelines."}
        ]
    },
    {
        "id": "containers",
        "title": "Containers",
        "image": local_img("Containers.svg"),
        "description": "Run containerized applications utilizing managed services.",
        "services": [
            {"name": "Amazon ECS", "image": f"{ICON_BASE}/Containers/Elastic-Container-Service.svg", "description": "Container orchestration service."},
            {"name": "Amazon EKS", "image": f"{ICON_BASE}/Containers/Elastic-Kubernetes-Service.svg", "description": "Managed Kubernetes service."},
            {"name": "AWS Fargate", "image": f"{ICON_BASE}/Containers/Fargate.svg", "description": "Serverless compute for containers."},
            {"name": "Amazon ECR", "image": f"{ICON_BASE}/Containers/Elastic-Container-Registry.svg", "description": "Docker container registry."},
             {"name": "AWS App Runner", "image": local_backend_img("AWS AppRunner.png"), "description": "Fully managed container application service."}
        ]
    },
    {
        "id": "migration",
        "title": "Migration",
        "image": local_img("Migration.png"),
        "description": "Move data and applications to AWS quickly and securely.",
        "services": [
            {"name": "AWS MGN", "image": f"{ICON_BASE}/Migration-Transfer/Application-Migration-Service.svg", "description": "Application Migration Service."},
            {"name": "AWS DMS", "image": local_backend_img("AWS DMS.png"), "description": "Migrate databases easily."},
            {"name": "AWS DataSync", "image": f"{ICON_BASE}/Migration-Transfer/DataSync.svg", "description": "Automated data transfer."},
            {"name": "AWS Transfer Family", "image": f"{ICON_BASE}/Migration-Transfer/Transfer-Family.svg", "description": "Fully managed SFTP, FTPS, and FTP support."},
            {"name": "AWS Snowball", "image": local_backend_img("AWS Snowball.png"), "description": "Petabyte-scale data transport."},
        ]
    },
    {
        "id": "analytics",
        "title": "Analytics",
        "image": local_img("Analytics.svg"),
        "description": "Derive insights with the broadest set of analytics services.",
        "services": [
            {"name": "Amazon Athena", "image": f"{ICON_BASE}/Analytics/Athena.svg", "description": "Query data in S3 using SQL."},
             {"name": "AWS Glue", "image": f"{ICON_BASE}/Analytics/Glue.svg", "description": "Serverless data integration."},
            {"name": "Amazon Kinesis", "image": f"{ICON_BASE}/Analytics/Kinesis.svg", "description": "Process streaming data."},
            {"name": "Amazon QuickSight", "image": f"{ICON_BASE}/Analytics/QuickSight.svg", "description": "Business intelligence service."},
            {"name": "Amazon OpenSearch Service", "image": f"{ICON_BASE}/Analytics/OpenSearch-Service.svg", "description": "Search, visualize, and analyze data."},
             {"name": "Amazon Redshift", "image": local_backend_img("amazon_redshirt.png"), "description": "Fast, simple, cost-effective data warehousing."}
        ]
    },
    {
        "id": "machine-learning",
        "title": "Machine Learning",
        "image": local_img("Machine Learning.png"),
        "description": "Build, train, and deploy ML models for any use case.",
        "services": [
            {"name": "Amazon SageMaker", "image": f"{ICON_BASE}/Machine-Learning/SageMaker.svg", "description": "Build, train, and deploy models."},
            {"name": "Amazon Rekognition", "image": f"{ICON_BASE}/Machine-Learning/Rekognition.svg", "description": "Image and video analysis."},
             {"name": "Amazon Textract", "image": f"{ICON_BASE}/Machine-Learning/Textract.svg", "description": "Extract text and data from documents."},
            {"name": "Amazon Comprehend", "image": f"{ICON_BASE}/Machine-Learning/Comprehend.svg", "description": "NLP and text analytics."},
             {"name": "Amazon Lex", "image": f"{ICON_BASE}/Machine-Learning/Lex.svg", "description": "Build conversational interfaces."},
            {"name": "Amazon Polly", "image": f"{ICON_BASE}/Machine-Learning/Polly.svg", "description": "Turn text into lifelike speech."},
             {"name": "Amazon Bedrock", "image": local_backend_img("Amazon Bedrock.webp"), "description": "Build with Foundation Models."}
        ]
    },
    {
        "id": "amazon-q",
        "title": "Amazon Q",
        "image": local_img("Amazon Q.jpg"),
        "description": "Your Generative AI assistant designed for work.",
        "services": [
            {"name": "Amazon Q Business", "image": local_backend_img("Amazon Q Business.png"), "description": "AI assistant for business data."},
        ]
    },
    {
        "id": "cloud-automation",
        "title": "Cloud Automation",
        "image": local_img("cloud automation.png"),
        "description": "Modern cloud operations rely on heavy automation and IaC.",
        "services": [
             {"name": "AWS CloudFormation", "image": f"{ICON_BASE}/Management-Governance/CloudFormation.svg", "description": "Model and provision resources."},
            {"name": "AWS CDK", "image": f"{ICON_BASE}/Developer-Tools/Cloud-Development-Kit.svg", "description": "Define infrastructure in code."},
            {"name": "AWS Step Functions", "image": local_backend_img("AWS Step Functions.jpg"), "description": "Orchestrate workflows."},
            {"name": "AWS Systems Manager Automation", "image": local_backend_img("AWS Systems Manager Automation.jpg"), "description": "Simplify common maintenance tasks."},
            {"name": "AWS Control Tower", "image": f"{ICON_BASE}/Management-Governance/Control-Tower.svg", "description": "Set up and govern a multi-account environment."}
        ]
    }
]

# Helper to look up module by ID
def get_module(module_id):
    for m in AWS_MODULES:
        if m['id'] == module_id:
            return m
    return None
