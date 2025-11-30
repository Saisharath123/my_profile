# courses_aws.py
# AWS Solution Architect module (uses images from your images/aws_images folder)
# Exposes:
#   - render() -> HTML string (main AWS page)
#   - render_service(service) -> HTML string (service detail pages)
#   - get_course_html() -> alias for render()

LOCAL_CLOUD_IMG = "/mnt/data/fdbd7e66-d51d-43e3-b104-eaad8d587981.png"

# Normalized service IDs -> (Label, icon path)
SERVICES = {
    "compute": ("Compute", "/images/aws_images/compute.svg"),
    "storage": ("Storage", "/images/aws_images/storage.svg"),
    "databases": ("Databases", "/images/aws_images/databases.png"),
    "networking-and-content-delivery": ("Networking & Content Delivery", "/images/aws_images/Networking & Content Delivery.webp"),
    "security-identity-and-compliance": ("Security, Identity & Compliance", "/images/aws_images/Security, Identity & Compliance.png"),
    "monitoring": ("Monitoring & Logging", "/images/aws_images/Monitoring & Logging.png"),
    "application-integration": ("Application Integration", "/images/aws_images/Application Integration.png"),
    "deployment-and-management": ("Deployment & Management", "/images/aws_images/Deployment & Management.png"),
    "containers": ("Containers", "/images/aws_images/Containers.svg"),
    "migration": ("Migration", "/images/aws_images/Migration.png"),
    "analytics": ("Analytics", "/images/aws_images/Analytics.svg"),
    "machine-learning": ("Machine Learning", "/images/aws_images/Machine Learning.png"),
    "amazon-q": ("Amazon Q", "/images/aws_images/Amazon Q.jpg"),
    "cloud-automation": ("Cloud Automation", "/images/aws_images/cloud automation.png"),
}

INNER_SERVICES = {
    "compute": ["EC2", "Auto Scaling", "AMI", "Security Groups", "Load Balancers"],
    "storage": ["S3", "EBS", "EFS", "Lifecycle Policies", "Replication"],
    "databases": ["RDS", "DynamoDB", "Aurora", "Redshift"],
    "networking-and-content-delivery": ["VPC", "Subnets", "Route Tables", "NAT Gateway", "CloudFront"],
    "security-identity-and-compliance": ["IAM", "KMS", "Policies", "MFA", "Secrets Manager"],
    "monitoring": ["CloudWatch", "CloudTrail", "Alarms", "Log Insights"],
    "application-integration": ["SNS", "SQS", "EventBridge", "Step Functions"],
    "deployment-and-management": ["CloudFormation", "CodePipeline", "Parameter Store"],
    "containers": ["ECS", "EKS", "Fargate", "Docker"],
    "migration": ["DMS", "Application Migration Service", "Cutover"],
    "analytics": ["Athena", "Kinesis", "Glue", "QuickSight"],
    "machine-learning": ["SageMaker", "Rekognition", "Comprehend"],
    "amazon-q": ["Amazon Q", "Generative AI", "Text / Image APIs"],
    "cloud-automation": ["Terraform", "CDK", "CI/CD", "Automation Scripts"],
}

def _service_card_html(sid, label, icon_url, idx=0):
    """
    Build card HTML. 'sid' is normalized. Adds tabindex so keyboard navigation works.
    """
    href = f"/course/aws/{sid}"
    inner_list = INNER_SERVICES.get(sid, [])
    inner_html = "".join([
        f"<li style='margin:3px 0;font-size:11px;font-weight:700;line-height:1.15;'>{item}</li>"
        for item in inner_list
    ])

    # Slightly smaller icons for long labels so the label fits
    long_label_sids = {"deployment-and-management", "networking-and-content-delivery", "security-identity-and-compliance"}
    if sid in long_label_sids:
        img_style = "width:76px;height:76px;object-fit:contain;"
        label_style = "font-weight:800;color:#0b1620;text-align:center;font-size:12px;white-space:normal;word-break:break-word;margin:0;padding:0;"
    else:
        img_style = "width:96px;height:96px;object-fit:contain;"
        label_style = "font-weight:800;color:#0b1620;text-align:center;font-size:14px;margin:0;padding:0;"

    delay = f"{idx * 0.12:.2f}s"

    return f"""
      <a href="{href}" class="aws-card-link" tabindex="0" aria-label="{label}" style="text-decoration:none;color:inherit;display:inline-block;">
        <div class="flip-card"
             style="width:180px;border-radius:10px;padding:12px;background:#fff;
                    border:1px solid rgba(10,20,30,0.06);
                    box-shadow:0 10px 28px rgba(2,6,23,0.04);
                    display:flex;flex-direction:column;align-items:center;gap:8px;
                    margin:8px;animation:fallIn 900ms cubic-bezier(.2,.8,.2,1) both;
                    animation-delay:{delay};transition:transform 200ms ease, box-shadow 200ms ease;transform-origin:center center;">
          <div class="flip-inner" style="position:relative;width:100%;height:100%;transform-style:preserve-3d;transition:transform 520ms cubic-bezier(.2,.9,.2,1);min-height:120px;overflow:hidden;display:flex;align-items:center;justify-content:center;flex-direction:column;">
            <div class="flip-front" style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;backface-visibility:hidden;-webkit-backface-visibility:hidden;padding:0 6px;">
              <img src="{icon_url}" alt="{label}" style="{img_style}">
              <div class="card-label" style="{label_style}">{label}</div>
            </div>
            <div class="flip-back" style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:flex-start;justify-content:flex-start;backface-visibility:hidden;-webkit-backface-visibility:hidden;transform:rotateY(180deg);padding:8px 10px;text-align:left;background:linear-gradient(180deg,#f7fbff,#ffffff);border-radius:10px;width:100%;height:100%;overflow:auto;box-sizing:border-box;">
              <div style="font-weight:800;margin-bottom:4px;font-size:12px;">{label} — contents</div>
              <ul style="padding-left:14px;margin:0;list-style:disc;">{inner_html}</ul>
            </div>
          </div>
        </div>
      </a>
    """

def render():
    """Main AWS page (used by /course/aws)."""
    cards = "".join([_service_card_html(sid, label, url, idx=i) for i, (sid, (label, url)) in enumerate(SERVICES.items())])

    # Key changes: scale increased to 1.28, z-index lift while hovered/focused so card is visually above neighbors,
    # transform-origin set to center so it grows from center.
    html = f"""
    <style>
      @keyframes fallIn {{
        0%   {{ opacity:0; transform: translateY(-50px) rotateX(8deg) scale(0.98); }}
        60%  {{ opacity:1; transform: translateY(8px) rotateX(0deg) scale(1.02); }}
        100% {{ opacity:1; transform: translateY(0) rotateX(0deg) scale(1); }}
      }}

      /* Stronger selection: bigger scale, raise above siblings */
      .aws-card-link:focus .flip-card,
      .aws-card-link:hover .flip-card {{
        transform: scale(1.28) !important; /* visibly larger */
        z-index: 40;                         /* bring forward so it is not clipped */
        box-shadow: 0 26px 64px rgba(11,94,215,0.20);
      }}

      /* apply blue tint to front face when selected */
      .aws-card-link:focus .flip-front,
      .aws-card-link:hover .flip-front {{
        background: linear-gradient(180deg, rgba(11,94,215,0.09), rgba(11,94,215,0.04));
        border-radius:8px;
      }}

      /* visible focus for keyboard users */
      .aws-card-link:focus {{
        outline: 3px solid rgba(11,94,215,0.16);
        outline-offset: 4px;
        border-radius: 10px;
      }}

      /* flip to back face preserved */
      .aws-card-link:hover .flip-inner, .aws-card-link:focus .flip-inner {{
        transform: rotateY(180deg);
      }}

      /* ensure transitions are smooth and override inline conflict if any */
      .flip-card {{ transition: transform 200ms cubic-bezier(.2,.8,.2,1) !important; will-change:transform; }}

      /* responsive fallback */
      @media (max-width:520px) {{
        .flip-card {{ width:48% !important; }}
      }}
    </style>

    <script>
      (function() {{
        function qsAll(selector) {{ return Array.prototype.slice.call(document.querySelectorAll(selector)); }}

        function init() {{
          var cards = qsAll('.aws-card-link');
          if (!cards || !cards.length) return;

          cards.forEach(function(card, idx) {{
            card.addEventListener('keydown', function(e) {{
              var k = e.key || e.keyCode;
              if (k === 'ArrowRight' || k === 'ArrowDown' || k === 39 || k === 40) {{
                e.preventDefault();
                var next = cards[(idx + 1) % cards.length];
                if (next) next.focus();
              }} else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 37 || k === 38) {{
                e.preventDefault();
                var prev = cards[(idx - 1 + cards.length) % cards.length];
                if (prev) prev.focus();
              }} else if (k === 'Enter' || k === ' ' || k === 13 || k === 32) {{
                e.preventDefault();
                card.click();
              }}
            }});

            // Focus on mouseenter so hover and keyboard styles match and selection is visible
            card.addEventListener('mouseenter', function() {{
              try {{ card.focus({{preventScroll:true}}); }} catch (err) {{ card.focus(); }}
            }});

            // Remove focus when leaving (so keyboard outlines don't stick after mouseout)
            card.addEventListener('mouseleave', function() {{
              try {{ card.blur(); }} catch (err) {{ }}
            }});
          }});
        }}

        if (document.readyState === 'loading') {{
          document.addEventListener('DOMContentLoaded', init);
        }} else {{
          setTimeout(init, 10);
        }}
      }})();
    </script>

    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap;">
        <div style="flex:0 0 140px;display:flex;align-items:center;justify-content:center;">
          <img src="{LOCAL_CLOUD_IMG}" alt="cloud" style="width:80px;height:80px;object-fit:contain;border-radius:8px;box-shadow:0 8px 22px rgba(2,6,23,0.06);">
        </div>
        <div style="flex:1;min-width:220px;">
          <h1 style="margin:0">AWS Solution Architect – Services</h1>
          <p style="color:#6b7280;font-weight:700;">Click any service below to see focused content and labs for that service.</p>
        </div>
      </div>

      <hr style="border:none;border-top:1px solid #e6eef8;">

      <div class="aws-cards-container" style="display:flex;flex-wrap:wrap;gap:12px;">
        {cards}
      </div>

      <p style="margin-top:12px;">
        <a href="/courses" style="text-decoration:underline;color:#0b5ed7;font-weight:800;">⬅ Back to Courses</a>
      </p>
    </div>
    """
    return html

def get_course_html():
    return render()

def render_service(service_id: str):
    """
    Return HTML for a specific AWS service (service_id is normalized id segment).
    """
    sid = (service_id or "").lower().strip()
    if sid not in SERVICES:
        return f"<h2>Service not found</h2><p>No content available for '{service_id}'.</p><p><a href='/course/aws'>⬅ Back to AWS</a></p>"

    label, icon = SERVICES[sid]

    # Per-service concise content (labels unchanged)
    if sid == "compute":
        content = """
        <h2>Compute</h2>
        <p style='color:#374151;font-weight:700;'>
          EC2 provides resizable compute. Focus: instance types, AMIs, security groups, Auto Scaling and placement.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Launch EC2 & SSH into instance</li>
          <li>Create AMI and launch from AMI</li>
          <li>Setup Auto Scaling Group with a launch template</li>
        </ol>
        """
    elif sid == "storage":
        content = """
        <h2>Storage</h2>
        <p style='color:#374151;font-weight:700;'>
          S3 for objects, EBS for block storage, EFS for shared file systems. Learn lifecycle policies & backups.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Create S3 bucket with versioning & lifecycle rules</li>
          <li>Attach EBS volume to EC2 and snapshot</li>
          <li>Mount EFS from two EC2 instances</li>
        </ol>
        """
    elif sid == "databases":
        content = """
        <h2>Databases</h2>
        <p style='color:#374151;font-weight:700;'>
          Managed relational and NoSQL options. Focus on backups, scaling, read replicas and performance.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Launch RDS and connect from EC2</li>
          <li>Configure read replicas and automated backups</li>
          <li>Design a DynamoDB table with appropriate keys</li>
        </ol>
        """
    elif sid == "networking-and-content-delivery":
        content = """
        <h2>Networking & Content Delivery</h2>
        <p style='color:#374151;font-weight:700;'>
          Design secure VPCs, route tables, NAT, peering and CDN strategies for global delivery.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Create VPC with public & private subnets</li>
          <li>Configure NAT Gateway and route tables</li>
          <li>Set up CloudFront with an S3 origin</li>
        </ol>
        """
    elif sid == "security-identity-and-compliance":
        content = """
        <h2>Security, Identity & Compliance</h2>
        <p style='color:#374151;font-weight:700;'>
          Implement least privilege, roles, policies, KMS encryption and audit-ready configurations.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Create IAM users, groups and policies</li>
          <li>Enable MFA and rotate access keys</li>
          <li>Use KMS to encrypt data at rest</li>
        </ol>
        """
    elif sid == "monitoring":
        content = """
        <h2>Monitoring & Logging</h2>
        <p style='color:#374151;font-weight:700;'>
          Collect metrics and logs, create alarms and dashboards, and enable audit trails.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Create CloudWatch metric alarm and dashboard</li>
          <li>Enable CloudTrail and query events</li>
          <li>Use Log Insights to search application logs</li>
        </ol>
        """
    elif sid == "application-integration":
        content = """
        <h2>Application Integration</h2>
        <p style='color:#374151;font-weight:700;'>
          Event-driven design, messaging, pub/sub and state orchestration using Step Functions.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Create an SNS topic and subscribe an endpoint</li>
          <li>Build an SQS queue and process messages from EC2</li>
          <li>Create EventBridge rule to route events to Lambda</li>
        </ol>
        """
    elif sid == "deployment-and-management":
        content = """
        <h2>Deployment & Management</h2>
        <p style='color:#374151;font-weight:700;'>
          Automate infra deployments and CI/CD pipelines for repeatable delivery and governance.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Author a CloudFormation stack and deploy it</li>
          <li>Create a CodePipeline to build and deploy an app</li>
          <li>Use Parameter Store / Secrets Manager for config</li>
        </ol>
        """
    elif sid == "containers":
        content = """
        <h2>Containers</h2>
        <p style='color:#374151;font-weight:700;'>
          Container orchestration patterns, cluster design and serverless containers (Fargate).
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Deploy a Docker app to ECS with Fargate</li>
          <li>Provision an EKS cluster and deploy a sample app</li>
          <li>Use service autoscaling and horizontal pod autoscaler</li>
        </ol>
        """
    elif sid == "migration":
        content = """
        <h2>Migration</h2>
        <p style='color:#374151;font-weight:700;'>
          Plan and execute migrations for databases and servers with minimal downtime.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Use DMS to migrate a sample database to RDS</li>
          <li>Perform a lift-and-shift using Application Migration Service</li>
          <li>Validate data integrity and cutover procedures</li>
        </ol>
        """
    elif sid == "analytics":
        content = """
        <h2>Analytics</h2>
        <p style='color:#374151;font-weight:700;'>
          Query and process large datasets, streaming ingestion and ETL pipelines.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Run SQL queries on S3 using Athena</li>
          <li>Stream sample data with Kinesis and consume it</li>
          <li>Create Glue jobs to transform datasets</li>
        </ol>
        """
    elif sid == "machine-learning":
        content = """
        <h2>Machine Learning</h2>
        <p style='color:#374151;font-weight:700;'>
          Build, train and deploy models with SageMaker and leverage AI services for common tasks.
        </p>
        <h3>Hands-on labs</h3>
        <ol style='font-weight:700;color:#374151;'>
          <li>Train a simple model in SageMaker and deploy endpoint</li>
          <li>Use Rekognition for image recognition demo</li>
          <li>Use Comprehend for basic NLP tasks</li>
        </ol>
        """
    elif sid == "amazon-q":
        content = """
        <h2>Amazon Q</h2>
        <p style='color:#374151;font-weight:700;'>
          Amazon's AI services and generative APIs overview.
        </p>
        """
    elif sid == "cloud-automation":
        content = """
        <h2>Cloud Automation</h2>
        <p style='color:#374151;font-weight:700;'>
          Infrastructure-as-code, CI/CD and automation tooling.
        </p>
        """
    else:
        content = f"<h2>{label}</h2><p>No detailed content prepared yet.</p>"

    return f"""
      <div style="display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start;">
        <div style="flex:0 0 120px;">
          <img src="{icon}" alt="{label}" style="width:120px;height:120px;object-fit:contain;border-radius:8px;">
        </div>
        <div style="flex:1;min-width:240px;">
          {content}
          <div style="margin-top:12px;">
            <a class="btn" href="/contact">Contact / Enroll</a>
          </div>
          <p style="margin-top:12px;">
            <a href="/course/aws" style="text-decoration:underline;color:#0b5ed7;font-weight:800;">⬅ Back to AWS</a>
          </p>
        </div>
      </div>
    """

