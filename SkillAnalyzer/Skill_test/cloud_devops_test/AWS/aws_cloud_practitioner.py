
# aws_cloud_practitioner.py
# Backend Content & Interface for AWS Certified Cloud Practitioner (CLF-C01) Practice Test

from flask import url_for
import json

EXAM_INFO = {
    "title": "AWS Certified Cloud Practitioner",
    "code": "CLF-C01",
    "description": "Validate your overall understanding of the AWS Cloud platform.",
    "duration_minutes": 90,
    "questions": [
        {"id": 1, "question": "Which AWS service is used to deploy and manage applications in the cloud without worrying about the infrastructure?", "options": ["Amazon EC2", "AWS Elastic Beanstalk", "AWS Lambda", "Amazon RDS"], "correct": 1, "explanation": "Elastic Beanstalk handles deployment details automatically."},
        {"id": 2, "question": "What is the primary benefit of using AWS Regions?", "options": ["Reduce cost", "Data security", "Global replication", "Lower latency for end-users"], "correct": 3, "explanation": "Regions allow deploying closer to users to reduce latency."},
        {"id": 3, "question": "Which service monitors AWS resources health and performance?", "options": ["AWS CloudTrail", "Amazon CloudWatch", "AWS Config", "Amazon Inspector"], "correct": 1, "explanation": "CloudWatch provides metrics, logs, and alarms for monitoring."},
        {"id": 4, "question": "Durable storage for static web content?", "options": ["EBS", "S3", "EFS", "Glacier"], "correct": 1, "explanation": "S3 is ideal for static content like images/videos."},
        {"id": 5, "question": "Pricing model with no long-term commitment?", "options": ["Reserved", "Spot", "On-Demand", "Savings Plans"], "correct": 2, "explanation": "On-Demand is pay-as-you-go with no commitment."},
        {"id": 6, "question": "Which AWS service enables you to create and manage virtual private networks?", "options": ["Amazon VPC", "AWS Direct Connect", "Amazon Route 53", "AWS VPN"], "correct": 0, "explanation": "Amazon VPC lets you provision a logically isolated section of the AWS Cloud."},
        {"id": 7, "question": "Which service is best for querying data directly in S3 using SQL?", "options": ["Amazon Redshift", "Amazon Athena", "Amazon Aurora", "Amazon DynamoDB"], "correct": 1, "explanation": "Athena is an interactive query service to analyze data in S3 using standard SQL."},
        {"id": 8, "question": "Which AWS support plan includes access to a Technical Account Manager (TAM)?", "options": ["Basic", "Developer", "Business", "Enterprise"], "correct": 3, "explanation": "Only the Enterprise Support plan includes a designated TAM."},
        {"id": 9, "question": "Who is responsible for security 'OF' the cloud?", "options": ["AWS", "Customer", "Third-party audit", "Government"], "correct": 0, "explanation": "AWS is responsible for security OF the cloud (physical, network, hypervisor)."},
        {"id": 10, "question": "Which service provides creating and rotating encryption keys?", "options": ["AWS Secrets Manager", "AWS KMS", "AWS Shield", "Amazon Macie"], "correct": 1, "explanation": "AWS Key Management Service (KMS) creates and manages cryptographic keys."},
        {"id": 11, "question": "Which pillar of the Well-Architected Framework focuses on recovery from failure?", "options": ["Reliability", "Performance Efficiency", "Security", "Cost Optimization"], "correct": 0, "explanation": "Reliability focuses on specific best practices for recovering from failures."},
        {"id": 12, "question": "Which service is a serverless compute service?", "options": ["EC2", "Lambda", "LightSail", "Fargate"], "correct": 1, "explanation": "AWS Lambda is a serverless compute service that runs code in response to events."},
        {"id": 13, "question": "Which storage class is best for archival data accessed once a year?", "options": ["S3 Standard", "S3 Intelligent-Tiering", "S3 Glacier Deep Archive", "S3 One Zone-IA"], "correct": 2, "explanation": "Glacier Deep Archive is the lowest-cost storage class for long-term retention."},
        {"id": 14, "question": "Which service helps protect against DDoS attacks?", "options": ["AWS WAF", "AWS Shield", "Amazon GuardDuty", "AWS Inspector"], "correct": 1, "explanation": "AWS Shield provides protection against Distributed Denial of Service (DDoS) attacks."},
        {"id": 15, "question": "What is the AWS database service that is a NoSQL database?", "options": ["RDS", "Aurora", "DynamoDB", "Redshift"], "correct": 2, "explanation": "DynamoDB is a key-value and document database (NoSQL)."},
        {"id": 16, "question": "Which service sends email notifications?", "options": ["SQS", "SNS", "SES", "Pinpoint"], "correct": 2, "explanation": "Amazon SES (Simple Email Service) is used for sending emails."},
        {"id": 17, "question": "How can you grant a user access to a specific bucket?", "options": ["IAM Group", "IAM Role", "Bucket Policy", "Security Group"], "correct": 2, "explanation": "Bucket Policies are resource-based policies used to grant access to S3 buckets."},
        {"id": 18, "question": "Which pricing tool allows you to estimate costs before using services?", "options": ["Cost Explorer", "AWS Pricing Calculator", "AWS Budgets", "Cost and Usage Report"], "correct": 1, "explanation": "AWS Pricing Calculator lets you estimate the cost for your architecture solution."},
        {"id": 19, "question": "Which service provides a dedicated network connection from premises to AWS?", "options": ["VPN", "Internet Gateway", "Direct Connect", "VPC Peering"], "correct": 2, "explanation": "AWS Direct Connect links your internal network to an AWS Direct Connect location."},
        {"id": 20, "question": "Which service is used for Infrastructure as Code?", "options": ["CloudFormation", "CodeBuild", "OpsWorks", "Config"], "correct": 0, "explanation": "AWS CloudFormation allows you to model infrastructure using code (JSON/YAML)."},
        {"id": 21, "question": "Which EC2 purchasing option is best for short-term, spiky workloads that can be interrupted?", "options": ["On-Demand", "Reserved", "Spot", "Dedicated Hosts"], "correct": 2, "explanation": "Spot Instances offer unused capacity at a discount but can be interrupted."},
        {"id": 22, "question": "Which service is a content delivery network (CDN)?", "options": ["Route 53", "CloudFront", "Global Accelerator", "Direct Connect"], "correct": 1, "explanation": "Amazon CloudFront is a global CDN service."},
        {"id": 23, "question": "What does IAM stand for?", "options": ["Internal Access Management", "Identity and Access Management", "Internet Access Method", "Integrated Account Module"], "correct": 1, "explanation": "Identity and Access Management."},
        {"id": 24, "question": "Which service is used to manage Docker containers?", "options": ["ECS", "EC2", "Lambda", "S3"], "correct": 0, "explanation": "Amazon Elastic Container Service (ECS) is a container orchestration service."},
        {"id": 25, "question": "Which component is required to connect a VPC to the Internet?", "options": ["NAT Gateway", "Internet Gateway", "VPN Gateway", "Egress-Only Internet Gateway"], "correct": 1, "explanation": "An Internet Gateway (IGW) enables traffic between your VPC and the internet."},
        {"id": 26, "question": "Which service provides managed DDoS protection?", "options": ["Shield", "WAF", "Firewall Manager", "GuardDuty"], "correct": 0, "explanation": "AWS Shield Standard is automatically enabled; Advanced offers paid protection."},
        {"id": 27, "question": "Which AWS Service is a fully managed graph database?", "options": ["DynamoDB", "Neptune", "ElastiCache", "RDS"], "correct": 1, "explanation": "Amazon Neptune is a fast, reliable, fully managed graph database service."},
        {"id": 28, "question": "Which service alerts you when your costs exceed a threshold?", "options": ["Cost Explorer", "AWS Budgets", "Trusted Advisor", "CloudTrail"], "correct": 1, "explanation": "AWS Budgets allows you to set custom budgets and alerting."},
        {"id": 29, "question": "Who is responsible for patching the Guest OS in EC2?", "options": ["AWS", "The Customer", "AWS Support", "Managed Services"], "correct": 1, "explanation": "Under the Shared Responsibility Model, the customer updates the Guest OS."},
        {"id": 30, "question": "Which service is used for DNS management?", "options": ["CloudFront", "Route 53", "VPC", "Direct Connect"], "correct": 1, "explanation": "Amazon Route 53 is a scalable cloud Domain Name System (DNS) web service."},
        {"id": 31, "question": "Which service provides automated security assessments?", "options": ["Amazon Inspector", "GuardDuty", "Shield", "Macie"], "correct": 0, "explanation": "Amazon Inspector tests network accessibility ensuring security."},
        {"id": 32, "question": "Which service can identify sensitive data (PII) in S3?", "options": ["GuardDuty", "Macie", "Shield", "Inspector"], "correct": 1, "explanation": "Amazon Macie uses ML to discover and protect sensitive data in S3."},
        {"id": 33, "question": "What is the global infrastructure component that contains multiple Availability Zones?", "options": ["Edge Location", "Region", "Data Center", "Zone"], "correct": 1, "explanation": "A Region is a physical location around the world which clusters data centers (AZs)."},
        {"id": 34, "question": "Which service allows you to run code without provisioning servers?", "options": ["EC2", "Lambda", "EBS", "RDS"], "correct": 1, "explanation": "AWS Lambda is the serverless compute service."},
        {"id": 35, "question": "Which database engine is NOT compatible with RDS?", "options": ["MySQL", "PostgreSQL", "Oracle", "MongoDB"], "correct": 3, "explanation": "MongoDB is not supported by RDS (DocumentDB is the mongo-compatible service)."},
        {"id": 36, "question": "Which service is a fully managed in-memory data store?", "options": ["ElastiCache", "DynamoDB", "S3", "RDS"], "correct": 0, "explanation": "Amazon ElastiCache offers Redis or Memcached."},
        {"id": 37, "question": "Which tool provides real-time guidance to provision resources following best practices?", "options": ["Trusted Advisor", "Inspector", "Config", "CloudTrail"], "correct": 0, "explanation": "AWS Trusted Advisor provides recommendations for cost, performance, and security."},
        {"id": 38, "question": "Which service records API calls for your account?", "options": ["CloudWatch", "CloudTrail", "Config", "X-Ray"], "correct": 1, "explanation": "AWS CloudTrail tracks user activity and API usage."},
        {"id": 39, "question": "Which service allows you to decouple components of a microservices application?", "options": ["SQS", "S3", "EC2", "IAM"], "correct": 0, "explanation": "Simple Queue Service (SQS) decouples distributed systems."},
        {"id": 40, "question": "Which S3 storage class is for data that is recreated if lost?", "options": ["S3 Standard", "S3 One Zone-IA", "S3 Glacier", "S3 Intelligent-Tiering"], "correct": 1, "explanation": "S3 One Zone-IA stores data in a single AZ, risking loss if that AZ fails."},
        {"id": 41, "question": "What service handles user sign-up and sign-in for mobile apps?", "options": ["IAM", "Cognito", "Directory Service", "SSO"], "correct": 1, "explanation": "Amazon Cognito enables user authentication for apps."},
        {"id": 42, "question": "Which architecture principle suggests replacing fixed servers with ephemeral resources?", "options": ["Loose Coupling", "Disposable Resources", "Automation", "Caching"], "correct": 1, "explanation": "Treat servers as disposable resources."},
        {"id": 43, "question": "What is the benefit of edge locations?", "options": ["Lower cost", "Lower latency for content delivery", "Higher security", "More compute power"], "correct": 1, "explanation": "Edge locations cache content closer to users via CloudFront."},
        {"id": 44, "question": "Which service provides a shared file system for Linux EC2 instances?", "options": ["S3", "EBS", "EFS", "FSx"], "correct": 2, "explanation": "Elastic File System (EFS) provides scalable file storage."},
        {"id": 45, "question": "Which service automates software deployments to EC2 or on-premise?", "options": ["CodeBuild", "CodeDeploy", "CodeCommit", "CodePipeline"], "correct": 1, "explanation": "AWS CodeDeploy automates code deployments."},
        {"id": 46, "question": "Which service provides machine learning capabilities?", "options": ["SageMaker", "Athena", "Glue", "EMR"], "correct": 0, "explanation": "Amazon SageMaker helps build, train, and deploy ML models."},
        {"id": 47, "question": "Which service manages SSL/TLS certificates?", "options": ["ACM", "IAM", "KMS", "WAF"], "correct": 0, "explanation": "AWS Certificate Manager (ACM) provisions SSL/TLS certificates."},
        {"id": 48, "question": "Which plan provides response times of < 15 minutes for business-critical system down?", "options": ["Developer", "Business", "Enterprise", "Basic"], "correct": 3, "explanation": "Enterprise Support offers < 15 min response for business-critical down events."},
        {"id": 49, "question": "Which service helps you migrate databases to AWS?", "options": ["DMS", "SMS", "Snowball", "Direct Connect"], "correct": 0, "explanation": "Database Migration Service (DMS)."},
        {"id": 50, "question": "Which specialized service is for data warehousing?", "options": ["RDS", "Redshift", "DynamoDB", "Athena"], "correct": 1, "explanation": "Amazon Redshift is a data warehouse service."},
        {"id": 51, "question": "Which service is used for configuration management using Chef/Puppet?", "options": ["OpsWorks", "Beanstalk", "CloudFormation", "Systems Manager"], "correct": 0, "explanation": "AWS OpsWorks uses Chef and Puppet."},
        {"id": 52, "question": "Which service provides demand-based scaling for EC2?", "options": ["Auto Scaling", "Load Balancing", "CloudWatch", "Lambda"], "correct": 0, "explanation": "EC2 Auto Scaling adjusts capacity based on demand."},
        {"id": 53, "question": "What is the text-to-speech service?", "options": ["Polly", "Transcribe", "Lex", "Rekognition"], "correct": 0, "explanation": "Amazon Polly turns text into lifelike speech."},
        {"id": 54, "question": "Which service is for analyzing streaming data?", "options": ["Kinesis", "Glue", "EMR", "Athena"], "correct": 0, "explanation": "Amazon Kinesis enables processing of streaming data."},
        {"id": 55, "question": "Which service provides a simple way to send notifications?", "options": ["SNS", "SQS", "SES", "Connect"], "correct": 0, "explanation": "Simple Notification Service (SNS) uses pub/sub."},
        {"id": 56, "question": "Which service detects objects locally using Deep Learning?", "options": ["DeepLens", "DeepRacer", "DeepComposer", "SageMaker"], "correct": 0, "explanation": "AWS DeepLens (legacy/device) or Rekognition (Cloud)."},
        {"id": 57, "question": "Which service allows private connection between 2 VPCs?", "options": ["VPC Peering", "VPN", "Direct Connect", "Gateway Endpoint"], "correct": 0, "explanation": "VPC Peering connects two VPCs."},
        {"id": 58, "question": "Which service allows transferring exabytes of data to AWS physically?", "options": ["Snowmobile", "Snowball", "Direct Connect", "S3 Transfer Acceleration"], "correct": 0, "explanation": "Snowmobile is the truck for exabyte-scale data."},
        {"id": 59, "question": "Which service is a managed Hadoop framework?", "options": ["EMR", "Glue", "Athena", "Redshift"], "correct": 0, "explanation": "Elastic MapReduce (EMR) runs big data frameworks like Hadoop/Spark."},
        {"id": 60, "question": "Which service provides a virtual desktop?", "options": ["WorkSpaces", "AppStream", "Connect", "Chime"], "correct": 0, "explanation": "Amazon WorkSpaces is a DaaS (Desktop as a Service)."},
        {"id": 61, "question": "What is the primary interactive query service?", "options": ["Athena", "Redshift", "Glue", "EMR"], "correct": 0, "explanation": "Athena queries S3 data using SQL."},
        {"id": 62, "question": "Which service provides threat detection?", "options": ["GuardDuty", "Inspector", "Macie", "WAF"], "correct": 0, "explanation": "GuardDuty is a threat detection service."},
        {"id": 63, "question": "Which service manages API gateways?", "options": ["API Gateway", "Route 53", "Direct Connect", "CloudFront"], "correct": 0, "explanation": "Amazon API Gateway."},
        {"id": 64, "question": "Which service is for business intelligence (BI)?", "options": ["QuickSight", "Athena", "Redshift", "Kinesis"], "correct": 0, "explanation": "Amazon QuickSight is the BI service."},
        {"id": 65, "question": "Which support plan offers architectural guidance for your specific use cases?", "options": ["Business", "Developer", "Basic", "Free"], "correct": 0, "explanation": "Business Support offers context-aware architectural guidance."}
    ]
}

def render():
    """
    Renders the Timer-based MCQ Interface.
    """
    exam_json = json.dumps(EXAM_INFO)
    
    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        :root {{
            --primary: #FF9900; /* AWS Orange */
            --primary-dark: #FF9900; 
            --bg-glass: rgba(255, 255, 255, 0.95);
            --text-dark: #232F3E; /* AWS Dark Blue */
            --text-light: #5d6c7b;
            --success: #10b981;
            --error: #ef4444;
        }}

        .test-interface-wrapper {{
            font-family: 'Outfit', sans-serif;
            max-width: 1000px;
            margin: 40px auto;
            color: var(--text-dark);
            position: relative;
        }}

        /* --- Header / Timer Bar --- */
        .test-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #232F3E;
            color: #fff;
            padding: 15px 30px;
            border-radius: 16px 16px 0 0;
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.3);
            position: sticky;
            top: 20px;
            z-index: 50;
        }}
        
        .test-title h2 {{ margin: 0; font-size: 1.2rem; font-weight: 600; letter-spacing: 0.5px; }}
        .test-title span {{ font-size: 0.9rem; opacity: 0.8; font-weight: 400; }}

        .timer-box {{
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(255,255,255,0.1);
            padding: 8px 16px;
            border-radius: 8px;
            font-variant-numeric: tabular-nums;
            font-weight: 700;
            font-size: 1.1rem;
            color: #FF9900;
            border: 1px solid rgba(255, 153, 0, 0.3);
        }}
        
        /* --- Main Content Area --- */
        .test-body {{
            background: #fff;
            border: 1px solid #e2e8f0;
            border-top: none;
            border-radius: 0 0 16px 16px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
            min-height: 400px;
            position: relative;
        }}

        /* Progress Bar */
        .progress-container {{
            margin-bottom: 30px;
        }}
        .progress-labels {{
            display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-light); margin-bottom: 8px;
        }}
        .progress-track {{
            height: 8px;
            background: #f1f5f9;
            border-radius: 4px;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #FF9900, #F58536);
            width: 0%;
            transition: width 0.4s ease;
        }}

        /* Question Card */
        .question-card {{
            animation: fadeIn 0.4s ease;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .q-header {{
            font-size: 1.1rem;
            color: var(--text-light);
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .q-text {{
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 30px;
            line-height: 1.4;
            color: #1a202c;
        }}

        /* Options */
        .options-grid {{
            display: grid;
            gap: 15px;
        }}

        .option-btn {{
            display: flex;
            align-items: center;
            padding: 18px 25px;
            background: #f8fafc;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 1.05rem;
            color: #475569;
            text-align: left;
            position: relative;
        }}

        .option-btn:hover {{
            border-color: #cbd5e1;
            background: #f1f5f9;
        }}

        .option-btn.selected {{
            border-color: #FF9900;
            background: #fff7ed; /* light orange tint */
            color: #c2410c;
        }}
        
        .option-marker {{
            width: 24px;
            height: 24px;
            border: 2px solid #cbd5e1;
            border-radius: 50%;
            margin-right: 15px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .option-btn.selected .option-marker {{
            border-color: #FF9900;
            background: #FF9900;
        }}
        
        .option-btn.selected .option-marker::after {{
            content: '';
            width: 8px;
            height: 8px;
            background: #fff;
            border-radius: 50%;
        }}

        /* Footer / Navigation */
        .test-footer {{
            margin-top: 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #f1f5f9;
            padding-top: 30px;
        }}

        .btn {{
            padding: 12px 30px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s;
            border: none;
        }}
        
        .btn-secondary {{
            background: #f1f5f9;
            color: #64748b;
        }}
        .btn-secondary:hover {{ background: #e2e8f0; }}

        .btn-primary {{
            background: #232F3E;
            color: #fff;
        }}
        .btn-primary:hover {{
            background: #374151;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        
        /* Results Modal */
        .modal-overlay {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(5px);
            display: flex; justify-content: center; align-items: center;
            z-index: 1000;
            opacity: 0; visibility: hidden;
            transition: all 0.3s;
        }}
        .modal-overlay.active {{ opacity: 1; visibility: visible; }}
        
        .result-card {{
            background: #fff;
            padding: 50px;
            border-radius: 24px;
            text-align: center;
            max-width: 500px;
            width: 90%;
            transform: scale(0.95);
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}
        .modal-overlay.active .result-card {{ transform: scale(1); }}
        
        .score-circle {{
            width: 120px; height: 120px;
            border-radius: 50%;
            background: conic-gradient(var(--primary) 0%, #e2e8f0 0%);
            margin: 0 auto 30px;
            display: flex; align-items: center; justify-content: center;
            position: relative;
        }}
        .score-circle::before {{
            content: '';
            position: absolute; width: 100px; height: 100px;
            background: #fff; border-radius: 50%;
        }}
        .score-val {{
            position: relative; font-size: 2.5rem; font-weight: 800; color: #1e293b;
        }}
        .score-label {{ position: relative; font-size: 0.9rem; color: #64748b; margin-top:-5px;}}

    </style>

    <div class="test-interface-wrapper">
        <!-- Header -->
        <div class="test-header">
            <div class="test-title">
                <h2>AWS Certified Cloud Practitioner</h2>
                <span>CLF-C01 | Practice Exam</span>
            </div>
            <div class="timer-box">
                <span id="timer-display">90:00</span>
            </div>
        </div>

        <!-- Body -->
        <div class="test-body">
            
            <!-- Progress -->
            <div class="progress-container">
                <div class="progress-labels">
                    <span id="q-counter">Question 1 of 5</span>
                    <span>Progress</span>
                </div>
                <div class="progress-track">
                    <div id="progress-bar" class="progress-fill" style="width: 20%"></div>
                </div>
            </div>

            <!-- Question Container -->
            <div id="question-container" class="question-card">
                <!-- Injected via JS -->
            </div>

            <!-- Footer -->
            <div class="test-footer">
                <button class="btn btn-secondary" onclick="prevQuestion()" id="btn-prev" disabled>Previous</button>
                <button class="btn btn-primary" onclick="nextQuestion()" id="btn-next">Next Question</button>
            </div>
        </div>
    </div>

    <!-- Result Modal -->
    <div class="modal-overlay" id="result-modal">
        <div class="result-card">
            <h2 style="margin-top:0; color:#1e293b;">Exam Completed!</h2>
            <p style="color:#64748b;">Here is your performance summary.</p>
            
            <div class="score-circle" id="score-circle">
                <div style="display:flex; flex-direction:column;">
                    <span class="score-val" id="score-val">0%</span>
                </div>
            </div>
            
            <div id="score-msg" style="font-weight:600; font-size:1.2rem; margin-bottom:30px;">
                <!-- Pass/Fail msg -->
            </div>
            
            <button class="btn btn-primary" onclick="window.location.reload()" style="width:100%">Retake Exam</button>
            <button class="btn btn-success" onclick="downloadExamPaper()" style="width:100%; margin-top:10px; background-color:#10b981; border:none; color:white; font-weight:600;">Download Report 📄</button>
            <button class="btn btn-secondary" onclick="window.history.back()" style="width:100%; margin-top:10px;">Exit</button>
        </div>
    </div>

    <script>
        const EXAM_DATA = {exam_json};
        let currentQ = 0;
        let answers = new Array(EXAM_DATA.questions.length).fill(null);
        let timeLeft = EXAM_DATA.duration_minutes * 60; // in seconds

        // Timer Logic
        function startTimer() {{
            const display = document.getElementById('timer-display');
            const timer = setInterval(() => {{
                if (timeLeft <= 0) {{
                    clearInterval(timer);
                    submitExam();
                    return;
                }}
                timeLeft--;
                const m = Math.floor(timeLeft / 60);
                const s = timeLeft % 60;
                display.textContent = `${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
            }}, 1000);
        }}

        function renderQuestion(idx) {{
            const q = EXAM_DATA.questions[idx];
            const container = document.getElementById('question-container');
            
            // Build Options HTML
            let optionsHtml = '<div class="options-grid">';
            q.options.forEach((opt, i) => {{
                const isSelected = answers[idx] === i ? 'selected' : '';
                optionsHtml += `
                    <div class="option-btn ${{isSelected}}" onclick="selectOption(${{i}})">
                        <div class="option-marker"></div>
                        <span>${{opt}}</span>
                    </div>
                `;
            }});
            optionsHtml += '</div>';

            container.innerHTML = `
                <div class="q-header">Question ${{idx + 1}}</div>
                <div class="q-text">${{q.question}}</div>
                ${{optionsHtml}}
            `;

            // Update UI state
            document.getElementById('q-counter').textContent = `Question ${{idx + 1}} of ${{EXAM_DATA.questions.length}}`;
            document.getElementById('progress-bar').style.width = `${{((idx + 1) / EXAM_DATA.questions.length) * 100}}%`;
            
            document.getElementById('btn-prev').disabled = idx === 0;
            document.getElementById('btn-next').textContent = idx === EXAM_DATA.questions.length - 1 ? 'Finish & Submit' : 'Next Question';
        }}

        function selectOption(optIdx) {{
            answers[currentQ] = optIdx;
            renderQuestion(currentQ); // Re-render to update selected style
        }}

        function nextQuestion() {{
            if (currentQ < EXAM_DATA.questions.length - 1) {{
                currentQ++;
                renderQuestion(currentQ);
            }} else {{
                submitExam();
            }}
        }}

        function prevQuestion() {{
            if (currentQ > 0) {{
                currentQ--;
                renderQuestion(currentQ);
            }}
        }}

        function submitExam() {{
            // Calculate Score
            let correct = 0;
            EXAM_DATA.questions.forEach((q, i) => {{
                if (answers[i] === q.correct) correct++;
            }});
            
            const scorePct = Math.round((correct / EXAM_DATA.questions.length) * 100);
            
            // Show Result
            document.getElementById('result-modal').classList.add('active');
            document.getElementById('score-val').textContent = `${{scorePct}}%`;
            
            const msg = document.getElementById('score-msg');
            const circle = document.getElementById('score-circle');
            
            // Update Circle Gradient
            circle.style.background = `conic-gradient(${{scorePct >= 70 ? '#10b981' : '#ef4444'}} ${{scorePct}}%, #e2e8f0 ${{scorePct}}%)`;
            
            if (scorePct >= 70) {{
                msg.textContent = "Congratulations! You Passed.";
                msg.style.color = "#10b981";
            }} else {{
                msg.textContent = "Keep practicing. You got this!";
                msg.style.color = "#ef4444";
            }}
        }}

        function downloadExamPaper() {{
            let correct = 0;
            const questionData = EXAM_DATA.questions.map((q, i) => {{
                if (answers[i] === q.correct) correct++;
                return {{
                    question: q.question,
                    options: q.options,
                    user_idx: answers[i],
                    correct_idx: q.correct,
                    explanation: q.explanation
                }};
            }});
            const scorePct = Math.round((correct / EXAM_DATA.questions.length) * 100);

            const payload = {{
                user_name: "Candidate",
                exam_title: EXAM_DATA.title,
                score: scorePct,
                passed: scorePct >= 70,
                questions: questionData
            }};

            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/skill-analyzer/download-result';
            
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'exam_data';
            input.value = JSON.stringify(payload);
            
            form.appendChild(input);
            document.body.appendChild(form);
            form.submit();
        }}

        // Init
        renderQuestion(0);
        startTimer();

    </script>
    """
