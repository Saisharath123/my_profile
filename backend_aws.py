# backup_AWS.py
# Backend content definition for AWS Solution Architect Modules

AWS_CONTENT = {
    "compute": """
        <h3>Core Concepts</h3>
        <p>Compute services are the backbone of your AWS infrastructure. You will master the deployment, management, and scaling of virtual servers and serverless compute resources.</p>
        
        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon EC2:</strong> Scalable virtual servers. Learn distinct Instance families (General Purpose, Compute Optimized, Memory Optimized).</li>
            <li><strong>Auto Scaling:</strong> Automatically adjust capacity to maintain steady, predictable performance at the lowest possible cost.</li>
            <li><strong>Elastic Load Balancing (ELB):</strong> Distribute incoming application traffic across multiple targets.</li>
            <li><strong>AWS Lambda:</strong> Run code without provisioning or managing servers (Serverless).</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Launch and Configure a Linux EC2 Instance with User Data.</li>
                <li>Create an Application Load Balancer (ALB) with Target Groups.</li>
                <li>Configure Auto Scaling Policies based on CPU utilization.</li>
            </ul>
        </div>
    """,

    "storage": """
        <h3>Core Concepts</h3>
        <p>AWS offers a complete range of services for you to store, access, govern, and analyze your data to reduce costs, increase agility, and accelerate innovation.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon S3:</strong> Object storage built to retrieve any amount of data from anywhere. Master Storage Classes (Standard, Intelligent-Tiering, Glacier).</li>
            <li><strong>Amazon EBS:</strong> Block storage volumes for use with EC2 instances.</li>
            <li><strong>Amazon EFS:</strong> Serverless, fully elastic file storage.</li>
            <li><strong>AWS Storage Gateway:</strong> Hybrid cloud storage service.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Host a Static Website on Amazon S3 with Custom Domain.</li>
                <li>Configure S3 Lifecycle Policies and Cross-Region Replication (CRR).</li>
                <li>Mount an EFS File System to Multiple EC2 Instances.</li>
            </ul>
        </div>
    """,

    "databases": """
        <h3>Core Concepts</h3>
        <p>Choose the right database for the right job. AWS offers the broadest selection of purpose-built databases for all your application needs.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon RDS:</strong> Managed Relational Database Service (MySQL, PostgreSQL, Oracle, SQL Server).</li>
            <li><strong>Amazon Aurora:</strong> High-performance managed relational database compatible with MySQL and PostgreSQL.</li>
            <li><strong>Amazon DynamoDB:</strong> Key-value and document database that delivers single-digit millisecond performance at any scale.</li>
            <li><strong>Amazon Redshift:</strong> Fast, simple, cost-effective data warehousing.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Launch an Multi-AZ RDS MySQL Database.</li>
                <li>Create and Query a DynamoDB Table.</li>
                <li>Implement Read Replicas for improved read performance.</li>
            </ul>
        </div>
    """,

    "networking-and-content-delivery": """
        <h3>Core Concepts</h3>
        <p>Networking is the foundation of the cloud. Learn to isolate your cloud infrastructure and deliver content with low latency.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon VPC:</strong> Logically isolated virtual network. Master Subnets, Route Tables, and Internet Gateways.</li>
            <li><strong>Amazon Route 53:</strong> Scalable Domain Name System (DNS).</li>
            <li><strong>Amazon CloudFront:</strong> Content Delivery Network (CDN) for fast distribution.</li>
            <li><strong>AWS Transit Gateway:</strong> Connect VPCs and on-premises networks.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Build a Custom VPC with Public and Private Subnets.</li>
                <li>Configure a NAT Gateway for private subnet internet access.</li>
                <li>Set up VPC Peering between two different VPCs.</li>
            </ul>
        </div>
    """,

    "security-identity-and-compliance": """
        <h3>Core Concepts</h3>
        <p>Security is Job Zero at AWS. Learn to secure your workloads and manage identities effectively.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>AWS IAM:</strong> Manage access to AWS services and resources securely.</li>
            <li><strong>AWS KMS:</strong> Create and manage keys to encrypt your data.</li>
            <li><strong>AWS WAF:</strong> Protect your web applications from common web exploits.</li>
            <li><strong>AWS Shield:</strong> Managed DDoS protection.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Create IAM Users, Groups, and Roles with least privilege policies.</li>
                <li>Enable Multi-Factor Authentication (MFA).</li>
                <li>Encrypt an S3 Bucket using KMS Keys.</li>
            </ul>
        </div>
    """,

    "monitoring": """
        <h3>Core Concepts</h3>
        <p>Visibility into your AWS resources and applications is crucial for operational excellence.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon CloudWatch:</strong> Observability of your AWS resources and applications.</li>
            <li><strong>AWS CloudTrail:</strong> Track user activity and API usage.</li>
            <li><strong>AWS Config:</strong> Audit and evaluate the configurations of your AWS resources.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Create CloudWatch Dashboards and Alarms.</li>
                <li>Analyze CloudTrail logs for security auditing.</li>
                <li>Set up Config Rules to enforce compliance.</li>
            </ul>
        </div>
    """,

    "application-integration": """
        <h3>Core Concepts</h3>
        <p>Decouple your microservices and distributed systems.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon SQS:</strong> Fully managed message queuing service.</li>
            <li><strong>Amazon SNS:</strong> Fully managed Pub/Sub messaging.</li>
            <li><strong>Amazon EventBridge:</strong> Serverless event bus.</li>
            <li><strong>AWS Step Functions:</strong> Visual workflow orchestration.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Build a Fan-out architecture using SNS and SQS.</li>
                <li>Orchestrate a serverless workflow with Step Functions.</li>
            </ul>
        </div>
    """,

    "deployment-and-management": """
        <h3>Core Concepts</h3>
        <p>Automate resource provisioning and manage your infrastructure as code.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>AWS CloudFormation:</strong> Model and provision all your cloud infrastructure resources.</li>
            <li><strong>AWS Systems Manager:</strong> Unified user interface to view & control operational data.</li>
            <li><strong>AWS Elastic Beanstalk:</strong> Easy-to-use service for deploying and scaling web applications.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Deploy a LAMP stack using a CloudFormation Template.</li>
                <li>Patch EC2 instances using Systems Manager.</li>
            </ul>
        </div>
    """,

    "containers": """
        <h3>Core Concepts</h3>
        <p>Run containerized applications on AWS using managed services.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon ECS:</strong> Highly scalable, high-performance container orchestration service.</li>
            <li><strong>Amazon EKS:</strong> Managed Kubernetes service.</li>
            <li><strong>AWS Fargate:</strong> Serverless compute engine for containers.</li>
            <li><strong>Amazon ECR:</strong> Fully managed Docker container registry.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Deploy a Docker container to ECS Fargate.</li>
                <li>Push a Docker image to ECR.</li>
            </ul>
        </div>
    """,

    "migration": """
        <h3>Core Concepts</h3>
        <p>Move data and applications to AWS quickly and securely.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>AWS Database Migration Service (DMS):</strong> Migrate databases to AWS easily and securely.</li>
            <li><strong>AWS Application Migration Service:</strong> Lift-and-shift migration.</li>
            <li><strong>AWS Snow Family:</strong> Physical devices to migrate data into and out of AWS.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Migrate an on-premise application to EC2.</li>
                <li>Perform a homogeneous database migration with DMS.</li>
            </ul>
        </div>
    """,

    "analytics": """
        <h3>Core Concepts</h3>
        <p>Derive insights from your data with the broadest and deepest set of analytics services.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon Athena:</strong> Query data in S3 using SQL.</li>
            <li><strong>Amazon Kinesis:</strong> Build streaming applications.</li>
            <li><strong>Amazon Glue:</strong> Serverless data integration (ETL).</li>
            <li><strong>Amazon QuickSight:</strong> Business intelligence service.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Query S3 logs using Athena.</li>
                <li>Create a Kinesis Data Stream.</li>
            </ul>
        </div>
    """,

    "machine-learning": """
        <h3>Core Concepts</h3>
        <p>Build, train, and deploy machine learning models for any use case with fully managed infrastructure.</p>

        <h4>Key Services Covered:</h4>
        <ul class="aws-feature-list">
            <li><strong>Amazon SageMaker:</strong> Build, train, and deploy ML models.</li>
            <li><strong>Amazon Rekognition:</strong> Automate image and video analysis.</li>
            <li><strong>Amazon Polly:</strong> Turn text into lifelike speech.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Detect labels in an image using Rekognition.</li>
                <li>Deploy a simple ML model with SageMaker.</li>
            </ul>
        </div>
    """,
    "amazon-q": """
        <h3>Core Concepts</h3>
        <p>Your Generative AI assistant designed for work.</p>

        <h4>Key Features:</h4>
        <ul class="aws-feature-list">
            <li><strong>Conversational Q&A:</strong> Ask questions about your business data.</li>
            <li><strong>Code Transformation:</strong> Upgrade and transform code.</li>
            <li><strong>Troubleshooting:</strong> Diagnose errors in the console.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Set up Amazon Q to index your S3 documentation.</li>
                <li>Ask Q to explain a piece of code.</li>
            </ul>
        </div>
    """,
    "cloud-automation": """
        <h3>Core Concepts</h3>
        <p>Modern cloud operations rely on heavy automation and Infrastructure as Code (IaC).</p>

        <h4>Key Tools:</h4>
        <ul class="aws-feature-list">
            <li><strong>Terraform:</strong> Open-source IaC tool.</li>
            <li><strong>AWS CDK:</strong> Define cloud infrastructure using familiar programming languages.</li>
            <li><strong>CI/CD Pipelines:</strong> Automate your release process.</li>
        </ul>

        <div style="background:#f3f4f6; padding:20px; border-radius:12px; margin-top:20px;">
            <h4 style="margin-top:0;">🧪 Hands-on Labs</h4>
            <ul style="margin-bottom:0; padding-left:20px;">
                <li>Provision a VPC using Terraform.</li>
                <li>Build a Jenkins Pipeline to deploy to AWS.</li>
            </ul>
        </div>
    """
}
