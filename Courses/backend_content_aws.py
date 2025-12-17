# backend_content_aws.py
# Detailed HTML content for AWS Services
# Mapped by exact Service Name as defined in backend_aws.py

AWS_CONTENT = {
    # --- COMPUTE ---
    "Amazon EC2": """
        <h3>Amazon EC2 (Elastic Compute Cloud)</h3>
        <p><strong>Definition:</strong> Virtual servers in the cloud with resizable compute capacity.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li><strong>Instance Types:</strong> General purpose, compute/memory/storage optimized, accelerated computing.</li>
            <li><strong>Pricing Models:</strong> On-Demand, Reserved Instances, Savings Plans, Spot Instances.</li>
            <li><strong>AMIs (Amazon Machine Images):</strong> Pre-configured templates for instances.</li>
            <li><strong>Key Pairs:</strong> SSH authentication for Linux instances.</li>
            <li><strong>Security Groups:</strong> Virtual firewalls for instances.</li>
            <li><strong>Placement Groups:</strong> Control instance placement for low latency/high throughput.</li>
        </ul>
        <p><strong>Use Cases:</strong> Web servers, application servers, batch processing, gaming servers.</p>
    """,
    "EC2 Auto Scaling": """
        <h3>EC2 Auto Scaling</h3>
        <p><strong>Definition:</strong> Automatically adds/removes EC2 instances based on demand.</p>
        <p><strong>Components:</strong></p>
        <ul>
            <li><strong>Launch Configuration/Template:</strong> Instance configuration blueprint.</li>
            <li><strong>Auto Scaling Group:</strong> Logical grouping of instances.</li>
            <li><strong>Scaling Policies:</strong> Target tracking, step scaling, simple scaling.</li>
            <li><strong>Health Checks:</strong> EC2 and ELB health checks.</li>
        </ul>
        <p><strong>Use Cases:</strong> Handling traffic spikes, ensuring application availability.</p>
    """,
    "Elastic Load Balancing": """
        <h3>Elastic Load Balancing</h3>
        <p><strong>Definition:</strong> Distributes incoming traffic across multiple targets.</p>
        <p><strong>Types:</strong></p>
        <ul>
            <li><strong>Application Load Balancer (ALB):</strong> Layer 7, HTTP/HTTPS.</li>
            <li><strong>Network Load Balancer (NLB):</strong> Layer 4, TCP/UDP, extreme performance.</li>
            <li><strong>Gateway Load Balancer (GWLB):</strong> For 3rd-party virtual appliances.</li>
            <li><strong>Classic Load Balancer (CLB):</strong> Legacy (avoid for new deployments).</li>
        </ul>
        <p><strong>Features:</strong> SSL termination, sticky sessions, health checks.</p>
    """,
    "AWS Lambda": """
        <h3>AWS Lambda</h3>
        <p><strong>Definition:</strong> Serverless compute service running code in response to events.</p>
        <p><strong>Key Concepts:</strong></p>
        <ul>
            <li><strong>Function:</strong> Code packaged with dependencies.</li>
            <li><strong>Runtime:</strong> Supports multiple languages (Python, Node.js, Java, etc.).</li>
            <li><strong>Trigger:</strong> Event sources (S3, DynamoDB, API Gateway, etc.).</li>
            <li><strong>Execution Role:</strong> IAM role granting permissions.</li>
            <li><strong>Layers:</strong> Shared code and data across functions.</li>
            <li><strong>Concurrency:</strong> Simultaneous executions (provisioned/reserved).</li>
        </ul>
        <p><strong>Use Cases:</strong> Real-time file processing, data transformation, microservices.</p>
    """,
    "AWS Elastic Beanstalk": """
        <h3>AWS Elastic Beanstalk</h3>
        <p><strong>Definition:</strong> Platform-as-a-Service (PaaS) for deploying web applications.</p>
        <p><strong>Components:</strong></p>
        <ul>
            <li><strong>Application:</strong> Logical collection of Elastic Beanstalk components.</li>
            <li><strong>Application Version:</strong> Specific labeled iteration of deployable code.</li>
            <li><strong>Environment:</strong> Version deployed on AWS resources.</li>
        </ul>
        <p><strong>Supported Platforms:</strong> Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker.</p>
        <p><strong>Features:</strong> Automatic scaling, load balancing, health monitoring.</p>
    """,
    "Amazon Lightsail": """
        <h3>Amazon Lightsail</h3>
        <p><strong>Definition:</strong> Simplified virtual private server (VPS) solution.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Pre-configured instances (WordPress, LAMP stack, etc.).</li>
            <li>Fixed monthly pricing.</li>
            <li>Includes SSD storage, DNS management, static IP.</li>
        </ul>
        <p><strong>Use Cases:</strong> Simple web applications, blogs, development environments.</p>
    """,
    "Amazon ECS": """
        <h3>Amazon ECS (Elastic Container Service)</h3>
        <p><strong>Definition:</strong> Fully managed container orchestration service.</p>
        <p><strong>Launch Types:</strong></p>
        <ul>
            <li><strong>EC2 Launch Type:</strong> Manage your own EC2 instances.</li>
            <li><strong>Fargate Launch Type:</strong> Serverless containers.</li>
        </ul>
        <p><strong>Components:</strong></p>
        <ul>
            <li><strong>Task Definition:</strong> Blueprint for containers (JSON).</li>
            <li><strong>Task:</strong> Running instance of a task definition.</li>
            <li><strong>Service:</strong> Maintains specified number of tasks.</li>
            <li><strong>Cluster:</strong> Logical grouping of tasks/services.</li>
        </ul>
        <p><strong>Use Cases:</strong> Microservices, batch processing, machine learning.</p>
    """,
    "AWS Fargate": """
        <h3>AWS Fargate</h3>
        <p><strong>Definition:</strong> Serverless compute engine for containers.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>No infrastructure management.</li>
            <li>Pay per vCPU and memory used.</li>
            <li>Works with ECS and EKS.</li>
        </ul>
        <p><strong>Use Cases:</strong> Microservices, CI/CD pipelines, batch jobs.</p>
    """,
    "Amazon EKS": """
        <h3>Amazon EKS (Elastic Kubernetes Service)</h3>
        <p><strong>Definition:</strong> Managed Kubernetes service.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Runs upstream Kubernetes.</li>
            <li>Integrates with IAM for authentication.</li>
            <li>Managed control plane.</li>
            <li>Supports Fargate for serverless pods.</li>
        </ul>
        <p><strong>Use Cases:</strong> Enterprise container orchestration, hybrid deployments.</p>
    """,

    # --- STORAGE ---
    "Amazon S3": """
        <h3>Amazon S3 (Simple Storage Service)</h3>
        <p><strong>Definition:</strong> Object storage service with industry-leading scalability, data availability, security, and performance.</p>
        <p><strong>Storage Classes:</strong></p>
        <ul>
            <li><strong>S3 Standard:</strong> Frequently accessed data.</li>
            <li><strong>S3 Intelligent-Tiering:</strong> Unknown/changing access patterns.</li>
            <li><strong>S3 Standard-IA:</strong> Infrequently accessed.</li>
            <li><strong>S3 One Zone-IA:</strong> Infrequently accessed, single AZ.</li>
            <li><strong>S3 Glacier:</strong> Archive storage (minutes retrieval).</li>
            <li><strong>S3 Glacier Deep Archive:</strong> Lowest cost (hours retrieval).</li>
        </ul>
        <p><strong>Features:</strong> Versioning, Encryption, Lifecycle policies, Cross-region replication, Presigned URLs, Static website hosting.</p>
    """,
    "Amazon EBS": """
        <h3>Amazon EBS (Elastic Block Store)</h3>
        <p><strong>Definition:</strong> Persistent block storage volumes for EC2 instances.</p>
        <p><strong>Volume Types:</strong></p>
        <ul>
            <li><strong>SSD (gp2/gp3):</strong> General purpose.</li>
            <li><strong>SSD (io1/io2):</strong> Provisioned IOPS (performance).</li>
            <li><strong>HDD (st1):</strong> Throughput optimized.</li>
            <li><strong>HDD (sc1):</strong> Cold HDD (lowest cost).</li>
        </ul>
        <p><strong>Features:</strong> Snapshots, encryption, multi-attach (io1/io2).</p>
    """,
    "Amazon EFS": """
        <h3>Amazon EFS (Elastic File System)</h3>
        <p><strong>Definition:</strong> Serverless, scalable file storage for Linux.</p>
        <p><strong>Performance Modes:</strong></p>
        <ul>
            <li><strong>General Purpose:</strong> Default for web servers, CMS.</li>
            <li><strong>Max I/O:</strong> Higher throughput, higher latency.</li>
        </ul>
        <p><strong>Throughput Modes:</strong> Bursting (based on size), Provisioned (set throughput independent of size).</p>
        <p><strong>Use Cases:</strong> Content management, web serving, data sharing.</p>
    """,
    "Amazon S3 Glacier": """
        <h3>Amazon S3 Glacier</h3>
        <p><strong>Definition:</strong> Secure, durable, low-cost storage for archiving.</p>
        <p><strong>Retrieval Options:</strong></p>
        <ul>
            <li><strong>Expedited:</strong> 1-5 minutes.</li>
            <li><strong>Standard:</strong> 3-5 hours.</li>
            <li><strong>Bulk:</strong> 5-12 hours (lowest cost).</li>
        </ul>
        <p><strong>Features:</strong> Vault Lock (WORM compliance).</p>
    """,
    "AWS Backup": """
        <h3>AWS Backup</h3>
        <p><strong>Definition:</strong> Centralized backup service across AWS services.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Policy-based backup plans.</li>
            <li>Cross-account/cross-region backup.</li>
            <li>Backup monitoring and reporting.</li>
        </ul>
        <p><strong>Supported Services:</strong> EBS, EFS, RDS, DynamoDB, Storage Gateway, FSx.</p>
    """,
    "Amazon FSx": """
        <h3>Amazon FSx</h3>
        <p><strong>Definition:</strong> Managed file systems.</p>
        <p><strong>Types:</strong></p>
        <ul>
            <li><strong>FSx for Windows:</strong> Native Windows file server (SMB).</li>
            <li><strong>FSx for Lustre:</strong> High-performance computing.</li>
            <li><strong>FSx for NetApp ONTAP:</strong> Enterprise NAS.</li>
            <li><strong>FSx for OpenZFS:</strong> ZFS file system.</li>
        </ul>
        <p><strong>Use Cases:</strong> Windows applications, machine learning, analytics.</p>
    """,

    # --- DATABASES ---
    "Amazon RDS": """
        <h3>Amazon RDS (Relational Database Service)</h3>
        <p><strong>Definition:</strong> Managed relational database service.</p>
        <p><strong>Engines:</strong> MySQL, PostgreSQL, MariaDB, Oracle, SQL Server.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Multi-AZ deployments for high availability.</li>
            <li>Read replicas (for scaling).</li>
            <li>Automated backups and patching.</li>
            <li>Storage auto-scaling.</li>
        </ul>
        <p><strong>Use Cases:</strong> Traditional applications, e-commerce, CRM.</p>
    """,
    "Amazon Aurora": """
        <h3>Amazon Aurora</h3>
        <p><strong>Definition:</strong> MySQL and PostgreSQL compatible relational database.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Up to 5x faster than standard MySQL.</li>
            <li>Up to 3x faster than standard PostgreSQL.</li>
            <li>15 read replicas (vs. 5 for RDS).</li>
            <li>Aurora Serverless (auto-scaling).</li>
            <li>Global Database (cross-region replication).</li>
        </ul>
    """,
    "Amazon DynamoDB": """
        <h3>Amazon DynamoDB</h3>
        <p><strong>Definition:</strong> Fully managed NoSQL database.</p>
        <p><strong>Key Concepts:</strong> Tables, Items, Attributes.</p>
        <p><strong>Capacity Modes:</strong></p>
        <ul>
            <li><strong>Provisioned:</strong> Set RCU/WCU.</li>
            <li><strong>On-Demand:</strong> Pay per request.</li>
        </ul>
        <p><strong>Features:</strong> Global Tables, DAX (in-memory cache), Streams, TTL.</p>
    """,
    "Amazon ElastiCache": """
        <h3>Amazon ElastiCache</h3>
        <p><strong>Definition:</strong> Managed Redis or Memcached in-memory data store.</p>
        <p><strong>Use Cases:</strong> Database caching, session stores, real-time analytics, gaming leaderboards.</p>
    """,
    "Amazon Redshift": """
        <h3>Amazon Redshift</h3>
        <p><strong>Definition:</strong> Petabyte-scale data warehouse.</p>
        <p><strong>Architecture:</strong></p>
        <ul>
            <li><strong>Leader Node:</strong> Query planning and coordination.</li>
            <li><strong>Compute Nodes:</strong> Execute queries and store data.</li>
            <li><strong>Columnar Storage:</strong> Optimized for analytics.</li>
        </ul>
        <p><strong>Features:</strong> Spectrum (query S3 directly), Concurrency Scaling.</p>
    """,
    "Amazon DocumentDB": """
        <h3>Amazon DocumentDB</h3>
        <p><strong>Definition:</strong> MongoDB compatible document database.</p>
        <p><strong>Features:</strong> 3x throughput of MongoDB, automatic scaling, replication across 3 AZs.</p>
    """,

    # --- NETWORKING & CONTENT DELIVERY ---
    "Amazon VPC": """
        <h3>Amazon VPC (Virtual Private Cloud)</h3>
        <p><strong>Definition:</strong> Isolated virtual network in AWS.</p>
        <p><strong>Components:</strong></p>
        <ul>
            <li><strong>Subnets:</strong> Public/Private segments of IP range.</li>
            <li><strong>Route Tables:</strong> Control traffic routing.</li>
            <li><strong>Internet Gateway:</strong> Connects VPC to internet.</li>
            <li><strong>NAT Gateway:</strong> Internet across for private subnets.</li>
            <li><strong>VPC Peering:</strong> Connect two VPCs.</li>
            <li><strong>Endpoints:</strong> Private connection to AWS services.</li>
            <li><strong>Flow Logs:</strong> Capture IP traffic.</li>
        </ul>
    """,
    "Internet Gateway": """
        <h3>Internet Gateway</h3>
        <p><strong>Definition:</strong> Horizontally scaled, redundant VPC component for internet connectivity.</p>
    """,
    "NAT Gateway": """
        <h3>NAT Gateway</h3>
        <p><strong>Definition:</strong> Network Address Translation for private subnets to access internet.</p>
        <p><strong>Types:</strong> Public (in public subnet), Private (for cross-VPC routing).</p>
    """,
    "VPC Peering": """
        <h3>VPC Peering</h3>
        <p><strong>Definition:</strong> Connect two VPCs using private IP addresses.</p>
        <p><strong>Limitations:</strong> No transitive peering, overlapping CIDRs not allowed.</p>
    """,
    "Security Groups": """
        <h3>Security Groups</h3>
        <p><strong>Definition:</strong> Stateful virtual firewall for EC2 instances.</p>
        <ul>
            <li>Allow rules only.</li>
            <li>Reference other security groups.</li>
            <li>Applied at instance level.</li>
        </ul>
    """,
    "AWS Transit Gateway": """
        <h3>AWS Transit Gateway</h3>
        <p><strong>Definition:</strong> Network transit hub connecting VPCs and on-premises networks.</p>
        <p><strong>Features:</strong> Hub-and-spoke architecture, cross-region peering, route tables.</p>
    """,
    "AWS Site-to-Site VPN": """
        <h3>AWS Site-to-Site VPN</h3>
        <p><strong>Definition:</strong> IPSec VPN connection between VPC and on-premises network.</p>
        <p><strong>Components:</strong> Virtual Private Gateway, Customer Gateway, VPN Connection.</p>
    """,
    "AWS Direct Connect": """
        <h3>AWS Direct Connect</h3>
        <p><strong>Definition:</strong> Dedicated network connection from on-premises to AWS.</p>
        <p><strong>Types:</strong> Dedicated (1/10/100 Gbps), Hosted (50Mbps-10Gbps).</p>
    """,
    "Amazon Route 53": """
        <h3>Amazon Route 53</h3>
        <p><strong>Definition:</strong> Scalable DNS and domain registration.</p>
        <p><strong>Routing Policies:</strong> Simple, Weighted, Latency-based, Failover, Geolocation, Geoproximity, Multivalue Answer.</p>
        <p><strong>Features:</strong> Health Checks.</p>
    """,
    "Amazon CloudFront": """
        <h3>Amazon CloudFront</h3>
        <p><strong>Definition:</strong> Global Content Delivery Network (CDN).</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Edge Locations (300+ globally).</li>
            <li>Origin Shield (secondary cache).</li>
            <li>Field-Level Encryption.</li>
            <li>Lambda@Edge (run code at edge).</li>
        </ul>
        <p><strong>Use Cases:</strong> Static/dynamic content delivery, video streaming, security.</p>
    """,

    # --- SECURITY, IDENTITY & COMPLIANCE ---
    "AWS IAM": """
        <h3>AWS IAM (Identity and Access Management)</h3>
        <p><strong>Definition:</strong> Manage access to AWS services and resources.</p>
        <p><strong>Components:</strong></p>
        <ul>
            <li><strong>Users:</strong> End users.</li>
            <li><strong>Groups:</strong> Collection of users.</li>
            <li><strong>Roles:</strong> Temporary credentials for AWS services/EC2.</li>
            <li><strong>Policies:</strong> JSON permission documents.</li>
        </ul>
        <p><strong>Best Practices:</strong> Least privilege, MFA, password policies, use roles.</p>
    """,
    "AWS IAM Identity Center (SSO)": """
        <h3>AWS IAM Identity Center (formerly SSO)</h3>
        <p><strong>Definition:</strong> Centralized access management for multiple AWS accounts and business applications.</p>
        <p><strong>Features:</strong> Centralized user management, MFA, attribute-based access control.</p>
    """,
    "AWS Organizations": """
        <h3>AWS Organizations</h3>
        <p><strong>Definition:</strong> Manage multiple AWS accounts.</p>
        <p><strong>Features:</strong> Consolidated billing, Service Control Policies (SCPs), Organizational Units (OUs).</p>
    """,
    "AWS KMS": """
        <h3>AWS KMS (Key Management Service)</h3>
        <p><strong>Definition:</strong> Managed encryption key service.</p>
        <p><strong>Key Types:</strong> AWS Managed Keys, Customer Managed Keys (CMK), AWS Owned Keys.</p>
        <p><strong>Features:</strong> Key rotation, key policies, audit via CloudTrail.</p>
    """,
    "AWS Secrets Manager": """
        <h3>AWS Secrets Manager</h3>
        <p><strong>Definition:</strong> Store and rotate secrets (database credentials, API keys).</p>
        <p><strong>Features:</strong> Automatic rotation, cross-region replication, integration with RDS.</p>
    """,
    "AWS Certificate Manager (ACM)": """
        <h3>AWS Certificate Manager (ACM)</h3>
        <p><strong>Definition:</strong> Provision, manage, and deploy SSL/TLS certificates.</p>
        <p><strong>Features:</strong> Free public certificates, automatic renewal, integration with ELB/CloudFront.</p>
    """,
    "AWS WAF": """
        <h3>AWS WAF (Web Application Firewall)</h3>
        <p><strong>Definition:</strong> Protect web applications from common exploits.</p>
        <p><strong>Features:</strong> Web ACLs (allow/block rules), Rate-based rules (DDoS), Managed rule sets.</p>
    """,
    "AWS Shield": """
        <h3>AWS Shield</h3>
        <p><strong>Definition:</strong> DDoS protection service.</p>
        <p><strong>Types:</strong> Standard (Free), Advanced (24/7 response team).</p>
    """,
    "Amazon GuardDuty": """
        <h3>Amazon GuardDuty</h3>
        <p><strong>Definition:</strong> Threat detection service using ML.</p>
        <p><strong>Data Sources:</strong> VPC Flow Logs, DNS Logs, CloudTrail Events.</p>
        <p><strong>Findings:</strong> Unauthorized deployments, cryptocurrency mining, compromised instances.</p>
    """,
    "AWS Security Hub": """
        <h3>AWS Security Hub</h3>
        <p><strong>Definition:</strong> Centralized security view across AWS accounts.</p>
        <p><strong>Features:</strong> Aggregates findings from GuardDuty, Inspector, Macie, etc.</p>
    """,
    "AWS Config": """
        <h3>AWS Config</h3>
        <p><strong>Definition:</strong> Track resource configuration and compliance.</p>
        <p><strong>Features:</strong> Configuration history, configuration snapshots, rules.</p>
    """,

    # --- MONITORING & LOGGING ---
    "Amazon CloudWatch": """
        <h3>Amazon CloudWatch</h3>
        <p><strong>Definition:</strong> Monitoring and observability service.</p>
        <p><strong>Components:</strong> Metrics, Alarms, Logs, Events (EventBridge), Dashboards.</p>
        <p><strong>Use Cases:</strong> Infrastructure monitoring, application performance, log analysis.</p>
    """,
    "AWS CloudTrail": """
        <h3>AWS CloudTrail</h3>
        <p><strong>Definition:</strong> Governance, compliance, and audit trail of AWS account activity.</p>
        <p><strong>Event Types:</strong> Management Events, Data Events, Insights Events.</p>
    """,
    "AWS X-Ray": """
        <h3>AWS X-Ray</h3>
        <p><strong>Definition:</strong> Analyze and debug distributed applications.</p>
        <p><strong>Components:</strong> Segments, Subsegments, Traces, Service Map.</p>
    """,
    "AWS Trusted Advisor": """
        <h3>AWS Trusted Advisor</h3>
        <p><strong>Definition:</strong> Recommendations to reduce cost, increase performance, improve security.</p>
        <p><strong>Categories:</strong> Cost Optimization, Performance, Security, Fault Tolerance, Service Limits.</p>
    """,

    # --- APPLICATION INTEGRATION ---
    "Amazon SNS": """
        <h3>Amazon SNS (Simple Notification Service)</h3>
        <p><strong>Definition:</strong> Pub/sub messaging service.</p>
        <p><strong>Components:</strong> Topics, Subscriptions (SQS, Lambda, HTTP/S, Email, SMS), Publishers.</p>
    """,
    "Amazon SQS": """
        <h3>Amazon SQS (Simple Queue Service)</h3>
        <p><strong>Definition:</strong> Message queue service.</p>
        <p><strong>Types:</strong> Standard Queue, FIFO Queue.</p>
        <p><strong>Features:</strong> Visibility timeout, dead-letter queues, delay queues.</p>
    """,
    "Amazon EventBridge": """
        <h3>Amazon EventBridge</h3>
        <p><strong>Definition:</strong> Serverless event bus connecting applications with data.</p>
        <p><strong>Key Concepts:</strong> Rules (route events), Schema Registry.</p>
    """,
    "AWS Step Functions": """
        <h3>AWS Step Functions</h3>
        <p><strong>Definition:</strong> Coordinate components of distributed applications as visual workflows.</p>
        <p><strong>Workflow Types:</strong> Standard (Long-running), Express (High-volume).</p>
    """,
    "Amazon MQ": """
        <h3>Amazon MQ</h3>
        <p><strong>Definition:</strong> Managed message broker for Apache ActiveMQ and RabbitMQ.</p>
        <p><strong>Use Case:</strong> Migrate existing messaging systems to cloud.</p>
    """,
    "AWS AppSync": """
        <h3>AWS AppSync</h3>
        <p><strong>Definition:</strong> Managed GraphQL service with real-time data synchronization.</p>
        <p><strong>Features:</strong> Offline data access, data sources (DynamoDB, Lambda), fine-grained security.</p>
    """,

    # --- DEPLOYMENT & MANAGEMENT ---
    "AWS CloudFormation": """
        <h3>AWS CloudFormation</h3>
        <p><strong>Definition:</strong> Infrastructure as Code (IaC) service.</p>
        <p><strong>Components:</strong> Templates (JSON/YAML), Stacks, Change Sets, StackSets.</p>
        <p><strong>Features:</strong> Drift detection, nested stacks.</p>
    """,
    "AWS CDK": """
        <h3>AWS CDK (Cloud Development Kit)</h3>
        <p><strong>Definition:</strong> Define cloud infrastructure using programming languages.</p>
        <p><strong>Supported Languages:</strong> TypeScript, JavaScript, Python, Java, C#, Go.</p>
    """,
    "AWS Systems Manager": """
        <h3>AWS Systems Manager</h3>
        <p><strong>Definition:</strong> Operational insights and actions on AWS resources.</p>
        <p><strong>Capabilities:</strong> Parameter Store, Run Command, Session Manager, Patch Manager, Automation.</p>
    """,
    "AWS CodeCommit": """
        <h3>AWS CodeCommit</h3>
        <p><strong>Definition:</strong> Private Git repositories.</p>
        <p><strong>Features:</strong> Encryption at rest/in-transit, integration with IAM, pull request workflows.</p>
    """,
    "AWS CodeBuild": """
        <h3>AWS CodeBuild</h3>
        <p><strong>Definition:</strong> Fully managed build service.</p>
        <p><strong>Features:</strong> Pay per minute, custom environments, buildspec.yml configuration.</p>
    """,
    "AWS CodeDeploy": """
        <h3>AWS CodeDeploy</h3>
        <p><strong>Definition:</strong> Automate code deployments.</p>
        <p><strong>Deployment Types:</strong> In-place, Blue/Green.</p>
        <p><strong>Supported Platforms:</strong> EC2, Lambda, ECS, on-premises servers.</p>
    """,
    "AWS CodePipeline": """
        <h3>AWS CodePipeline</h3>
        <p><strong>Definition:</strong> Continuous delivery service.</p>
        <p><strong>Components:</strong> Stages → Actions → Artifacts.</p>
        <p><strong>Integrations:</strong> CodeBuild, CodeDeploy, Elastic Beanstalk, third-party tools.</p>
    """,

    # --- CONTAINERS (EXTRA) ---
    "Amazon ECR": """
        <h3>Amazon ECR (Elastic Container Registry)</h3>
        <p><strong>Definition:</strong> Fully managed Docker container registry.</p>
        <p><strong>Features:</strong> Image scanning, lifecycle policies, cross-region replication.</p>
    """,
    "AWS App Runner": """
        <h3>AWS App Runner</h3>
        <p><strong>Definition:</strong> Fully managed container application service.</p>
        <p><strong>Features:</strong> Auto-scaling, load balancing, automatic deployments from source code.</p>
    """,

    # --- MIGRATION ---
    "AWS MGN": """
        <h3>AWS MGN (Application Migration Service)</h3>
        <p><strong>Definition:</strong> Lift-and-shift migration service.</p>
        <p><strong>Features:</strong> Minimal downtime, test migrations, automated replication.</p>
    """,
    "AWS DMS": """
        <h3>AWS DMS (Database Migration Service)</h3>
        <p><strong>Definition:</strong> Migrate databases to AWS.</p>
        <p><strong>Types:</strong> Homogeneous, Heterogeneous.</p>
        <p><strong>Features:</strong> Continuous replication, schema conversion.</p>
    """,
    "AWS DataSync": """
        <h3>AWS DataSync</h3>
        <p><strong>Definition:</strong> Automated data transfer service.</p>
        <p><strong>Use Cases:</strong> Migrate data to AWS, replicate data between storage systems.</p>
    """,
    "AWS Transfer Family": """
        <h3>AWS Transfer Family</h3>
        <p><strong>Definition:</strong> Fully managed SFTP, FTPS, FTP service.</p>
        <p><strong>Features:</strong> Identity integration (AD, IAM), encryption, logging.</p>
    """,
    "AWS Snowball": """
        <h3>AWS Snowball</h3>
        <p><strong>Definition:</strong> Physical device for petabyte-scale data transfer.</p>
        <p><strong>Types:</strong> Snowball Edge (compute/storage), Snowcone.</p>
    """,

    # --- ANALYTICS ---
    "Amazon Athena": """
        <h3>Amazon Athena</h3>
        <p><strong>Definition:</strong> Serverless interactive query service for S3.</p>
        <p><strong>Features:</strong> Standard SQL, supports JSON/CSV/Parquet, pay per query.</p>
    """,
    "AWS Glue": """
        <h3>AWS Glue</h3>
        <p><strong>Definition:</strong> Serverless ETL service.</p>
        <p><strong>Components:</strong> Data Catalog, ETL Jobs, Crawlers, Studio.</p>
    """,
    "Amazon Kinesis": """
        <h3>Amazon Kinesis</h3>
        <p><strong>Definition:</strong> Real-time data streaming.</p>
        <p><strong>Services:</strong> Data Streams, Firehose, Data Analytics, Video Streams.</p>
    """,
    "Amazon QuickSight": """
        <h3>Amazon QuickSight</h3>
        <p><strong>Definition:</strong> Business intelligence service.</p>
        <p><strong>Features:</strong> SPICE engine, ML insights, embedded analytics.</p>
    """,
    "Amazon OpenSearch Service": """
        <h3>Amazon OpenSearch Service</h3>
        <p><strong>Definition:</strong> Managed OpenSearch (formerly Elasticsearch) service.</p>
        <p><strong>Use Cases:</strong> Log analytics, real-time application monitoring, search.</p>
    """,

    # --- MACHINE LEARNING ---
    "Amazon SageMaker": """
        <h3>Amazon SageMaker</h3>
        <p><strong>Definition:</strong> End-to-end ML platform.</p>
        <p><strong>Components:</strong> Ground Truth, Notebooks, Training, Hyperparameter Tuning, Hosting, Studio.</p>
    """,
    "Amazon Rekognition": """
        <h3>Amazon Rekognition</h3>
        <p><strong>Definition:</strong> Image and video analysis.</p>
        <p><strong>Features:</strong> Object detection, facial analysis, text detection, content moderation.</p>
    """,
    "Amazon Textract": """
        <h3>Amazon Textract</h3>
        <p><strong>Definition:</strong> Extract text and data from documents.</p>
        <p><strong>Features:</strong> Handwriting recognition, forms/tables extraction.</p>
    """,
    "Amazon Comprehend": """
        <h3>Amazon Comprehend</h3>
        <p><strong>Definition:</strong> Natural language processing (NLP).</p>
        <p><strong>Features:</strong> Sentiment analysis, entity recognition, topic modeling.</p>
    """,
    "Amazon Lex": """
        <h3>Amazon Lex</h3>
        <p><strong>Definition:</strong> Build conversational interfaces.</p>
        <p><strong>Features:</strong> Automatic speech recognition, powered by Alexa technology.</p>
    """,
    "Amazon Polly": """
        <h3>Amazon Polly</h3>
        <p><strong>Definition:</strong> Text-to-speech service.</p>
        <p><strong>Features:</strong> Neural text-to-speech, multiple languages/voices.</p>
    """,
    "Amazon Bedrock": """
        <h3>Amazon Bedrock</h3>
        <p><strong>Definition:</strong> Foundational models service.</p>
        <p><strong>Features:</strong> Access to models from AI21 Labs, Anthropic, Stability AI, and Amazon.</p>
    """,

    # --- AMAZON Q & AI ---
    "Amazon Q": """
        <h3>Amazon Q</h3>
        <p><strong>Definition:</strong> AI-powered assistant for AWS.</p>
        <p><strong>Capabilities:</strong> Code generation, debugging, troubleshooting (Q Developer).</p>
    """,
    "Amazon Q Business": """
        <h3>Amazon Q Business</h3>
        <p><strong>Definition:</strong> Secure, generative AI-powered assistant for business.</p>
        <p><strong>Features:</strong> Connects to enterprise data sources, provides relevant answers with citations.</p>
    """,

    # --- CLOUD AUTOMATION ---
    "AWS Systems Manager Automation": """
        <h3>AWS Systems Manager Automation</h3>
        <p><strong>Definition:</strong> Automate common maintenance and deployment tasks for AWS resources.</p>
        <p><strong>Key Capabilities:</strong></p>
        <ul>
            <li><strong>Runbooks:</strong> Define automation workflows using documents.</li>
            <li><strong>Patching:</strong> Automate OS patching across fleets.</li>
            <li><strong>AMI Management:</strong> Streamline image creation and updates.</li>
            <li><strong>Remediation:</strong> Automatically fix non-compliant config rules.</li>
        </ul>
        <p><strong>Use Cases:</strong> Server maintenance, disaster recovery drills, state management.</p>
    """,
    "AWS Control Tower": """
        <h3>AWS Control Tower</h3>
        <p><strong>Definition:</strong> Set up and govern secure, compliant multi-account environments.</p>
        <p><strong>Features:</strong> Landing zone automation, guardrails, centralized dashboard.</p>
    """
}
