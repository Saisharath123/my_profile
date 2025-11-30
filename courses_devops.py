# courses_devops_enhanced.py
# DevOps module (uses images from your images/devops_images folder)
# Exposes:
#   - render() -> HTML string (main DevOps page)
#   - render_service(service) -> HTML string (service/tool detail pages)
#   - get_course_html() -> alias for render()

# Header image served from your images/ directory
LOCAL_DEVOPS_IMG = "/images/devops.png"

# Service/tool definitions: id -> (label, served_image_url)
SERVICES = {
    "git-github": (
        "Git & GitHub Fundamentals",
        "/images/devops_images/Git Hub.png"
    ),
    "ci-cd": (
        "CI/CD (Jenkins / GitHub Actions)",
        "/images/devops_images/CI CD.png"
    ),
    "docker": (
        "Docker & Containerization",
        "/images/devops_images/docker.png"
    ),
    "kubernetes": (
        "Kubernetes (K8s)",
        "/images/devops_images/k8.png"
    ),
    "iac-terraform": (
        "Infrastructure as Code (Terraform)",
        "/images/devops_images/terraform.png"
    ),
    "config-ansible": (
        "Configuration Management (Ansible)",
        "/images/devops_images/ansible.webp"
    ),
    "monitoring-logging": (
        "Monitoring & Logging (Prometheus / Grafana / ELK)",
        "/images/devops_images/Monitoring.png"
    ),
    "devsecops": (
        "DevSecOps & Security in Pipelines",
        "/images/devops_images/DevSecOps.png"
    ),
    "scripting": (
        "Scripting (Linux / Bash / Python)",
        "/images/devops_images/LINUX.png"
    ),
    "cloud-devops": (
        "Cloud DevOps (AWS / Azure / GCP)",
        "/images/devops_images/cloud.png"
    ),
}


def _service_card_html(sid, label, icon_url):
    """
    Small clickable card for each DevOps module.
    Enhanced with clean, class-based styling for modularity.
    """
    href = f"/course/devops/{sid}"

    # IDs that should use "cover" style (fill the card, no empty space)
    cover_ids = {"monitoring-logging", "devsecops", "cloud-devops"}
    is_cover = sid in cover_ids
    
    # Use CSS classes to handle the different image styles
    img_class = "devops-card-img-cover" if is_cover else "devops-card-img-contain"
    card_class = "devops-module-card"
    if is_cover:
        card_class += " devops-module-card-cover"

    return f"""
      <a href="{href}" class="devops-module-link" style="text-decoration:none;color:inherit;">
        <div class="{card_class}" tabindex="0">
          <div class="devops-module-card-inner">
            <img src="{icon_url}" alt="{label}" class="{img_class}">
          </div>
          <div class="devops-card-label">
            {label}
          </div>
        </div>
      </a>
    """


def render():
    cards = "".join([_service_card_html(sid, label, url) for sid, (label, url) in SERVICES.items()])

    page_style = """
    <style>
      /* --- BASE STYLES & UTILITIES --- */
      .devops-page-shell {
        position:relative;
        padding:30px; /* More padding */
        border-radius:30px;
        background:
          linear-gradient(135deg, #f0f9ff 0%, #e0f7ff 100%); /* Lighter, cleaner background */
        border:1px solid #cceeff;
        box-shadow:0 25px 50px rgba(15,23,42,0.15); /* Deeper shadow */
        overflow:hidden;
      }

      /* --- BACKGROUND ORBS (More subtle) --- */
      .devops-bg-orb {
        position:absolute;
        border-radius:999px;
        filter:blur(40px);
        opacity:0.6;
        pointer-events:none;
        mix-blend-mode:multiply; /* More dramatic blend */
        animation:devops-orb-drift 20s ease-in-out infinite alternate;
      }

      .devops-bg-orb-1 {
        width:300px;
        height:300px;
        top:-100px;
        right:-80px;
        background:radial-gradient(circle, rgba(0,123,255,0.6), transparent 70%);
      }

      .devops-bg-orb-2 {
        width:250px;
        height:250px;
        bottom:-90px;
        left:-60px;
        background:radial-gradient(circle, rgba(40,167,69,0.5), transparent 70%);
        animation-delay:-7s;
      }

      .devops-bg-orb-3 {
        width:220px;
        height:220px;
        top:30%;
        left:50%;
        background:radial-gradient(circle, rgba(255,193,7,0.5), transparent 70%);
        animation-delay:-12s;
      }

      @keyframes devops-orb-drift {
        0%   { transform:translate3d(0,0,0) scale(1); }
        100% { transform:translate3d(40px,-30px,0) scale(1.05); }
      }

      /* --- MAIN CONTENT WRAPPER --- */
      .devops-wrapper {
        position:relative;
        z-index:1;
        display:flex;
        flex-direction:column;
        gap:30px;
      }

      /* --- HERO SECTION --- */
      .devops-hero-row {
        display:flex;
        gap:30px;
        align-items:center;
        flex-wrap:wrap;
        padding-bottom:15px;
        border-bottom:2px solid #e9ecef; /* Thicker separator */
      }

      .devops-hero-img-col {
        flex:0 0 150px;
      }

      .devops-hero-img-col img {
        width:130px;
        height:130px;
        object-fit:cover;
        border-radius:50%; /* Circular image */
        box-shadow:0 15px 35px rgba(0,0,0,0.15);
        display:block;
        border: 6px solid #ffffff; /* White border for pop */
      }

      .devops-hero-text-col {
        flex:1;
        min-width:250px;
      }

      .devops-hero-text-col h1 {
        margin:0;
        font-size:2.5rem; /* Larger heading */
        color:#007bff; /* Primary blue color */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
      }

      .devops-hero-text-col p {
        color:#495057;
        font-weight:500;
        margin:8px 0 0 0;
        font-size:1.2rem;
      }

      /* --- MODULE GRID --- */
      .devops-grid {
        display:flex;
        flex-wrap:wrap;
        gap:25px;
        justify-content:center;
      }

      /* --- CARD STYLES (MODULAR) --- */
      .devops-module-card {
        cursor:pointer;
        position:relative;
        display:flex;
        flex-direction:column;
        align-items:center;
        gap:10px;
        width:220px; /* Slightly wider card */
        padding:0;
        
        /* FALLING FROM AIR ON LOAD */
        opacity:0;
        transform:translateY(-60px) scale(0.9);
        animation:devops-fall-in 0.8s cubic-bezier(0.22, 0.8, 0.3, 1.1) forwards;
        transition:
          transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55), /* Rocket launch curve */
          box-shadow 0.4s ease;
      }

      /* Staggered delays for animation */
      .devops-grid a:nth-child(1)  .devops-module-card { animation-delay:0.00s; }
      .devops-grid a:nth-child(2)  .devops-module-card { animation-delay:0.08s; }
      .devops-grid a:nth-child(3)  .devops-module-card { animation-delay:0.16s; }
      .devops-grid a:nth-child(4)  .devops-module-card { animation-delay:0.24s; }
      .devops-grid a:nth-child(5)  .devops-module-card { animation-delay:0.32s; }
      .devops-grid a:nth-child(6)  .devops-module-card { animation-delay:0.40s; }
      .devops-grid a:nth-child(7)  .devops-module-card { animation-delay:0.48s; }
      .devops-grid a:nth-child(8)  .devops-module-card { animation-delay:0.56s; }
      .devops-grid a:nth-child(9)  .devops-module-card { animation-delay:0.64s; }
      .devops-grid a:nth-child(10) .devops-module-card { animation-delay:0.72s; }

      @keyframes devops-fall-in {
        0%   { opacity:0; transform:translateY(-60px) scale(0.9); }
        70%  { opacity:1; transform:translateY(5px) scale(1.02); }
        100% { opacity:1; transform:translateY(0) scale(1.0); }
      }

      .devops-module-card-inner {
        width:100%;
        height:140px; /* Slightly taller */
        border-radius:18px; /* More rounded */
        padding:10px;
        display:flex;
        align-items:center;
        justify-content:center;
        overflow:hidden;
        
        /* Glassmorphism/Neumorphism base look */
        background:rgba(255, 255, 255, 0.8);
        border:1px solid rgba(255, 255, 255, 0.4);
        box-shadow:0 10px 30px rgba(0,0,0,0.08), inset 0 0 0 1px rgba(255,255,255,0.5);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        transition:
          box-shadow 0.4s ease,
          background 0.4s ease,
          transform 0.4s ease;
      }
      
      /* Specific style for 'cover' cards */
      .devops-module-card-cover .devops-module-card-inner {
          height:160px;
          padding:0;
      }

      /* Image styles */
      .devops-card-img-contain {
          max-width:90%;
          max-height:90%;
          height:auto;
          display:block;
          object-fit:contain;
      }
      
      .devops-card-img-cover {
          width:100%;
          height:100%;
          display:block;
          object-fit:cover;
          border-radius:18px;
      }

      .devops-card-label {
        font-weight:800;
        color:#212529;
        text-align:center;
        font-size:15px;
        line-height:1.4;
        padding: 0 4px;
      }

      /* --- ROCKET HOVER EFFECT --- */
      .devops-module-card:hover {
        /* ROCKET LIFT-OFF */
        transform:translateY(-30px) scale(1.1) rotateZ(-1deg); /* Lift, scale, and slight wobble */
        z-index: 10; /* Bring to front */
      }

      .devops-module-card:hover .devops-module-card-inner {
        /* ENGINE FIRE GLOW */
        background:rgba(255, 255, 255, 0.95);
        box-shadow:
          0 0 5px rgba(255, 165, 0, 0.8), /* Orange glow */
          0 0 20px rgba(255, 69, 0, 0.6), /* Red glow */
          0 25px 50px rgba(0,0,0,0.25); /* Deep shadow */
        border-color: #ffc107; /* Yellow border */
      }
      
      /* --- SERVICE DETAIL PAGE STYLES (MODULAR) --- */
      .service-detail-container {
          display:flex;
          gap:40px;
          flex-wrap:wrap;
          align-items:flex-start;
      }
      
      .service-icon-col {
          flex:0 0 200px; /* Wider column */
          display:flex;
          align-items:flex-start;
          justify-content:center;
      }
      
      .service-icon-wrapper {
          width:200px;
          height:200px;
          border-radius:50%; /* Circular icon */
          background:linear-gradient(145deg, #ffffff, #f0f0f0);
          border:4px solid #007bff; /* Primary color border */
          box-shadow: 0 15px 35px rgba(0,0,0,0.15);
          display:flex;
          align-items:center;
          justify-content:center;
          padding:15px;
      }
      
      .service-icon-wrapper img {
          max-width:90%;
          max-height:90%;
          height:auto;
          display:block;
          object-fit:contain;
      }
      
      .service-content-col {
          flex:1;
          min-width:350px;
      }
      
      .service-content-col h2 {
          font-size:2.5rem;
          color:#007bff;
          margin-top:0;
          border-bottom: 3px solid #e9ecef;
          padding-bottom: 10px;
          margin-bottom: 20px;
      }
      
      .service-content-col h3 {
          font-size:1.6rem;
          color:#28a745; /* Secondary green color for subheadings */
          margin-top:30px;
          margin-bottom:12px;
      }
      
      .service-content-col p {
          color:#495057;
          font-weight:400;
          font-size:1.15rem;
          line-height:1.7;
      }
      
      .service-content-col ol {
          color:#495057;
          font-weight:600;
          font-size:1.05rem;
          line-height:2;
          padding-left: 25px;
          list-style-type: decimal-leading-zero; /* Advanced list style */
      }
      
      .service-content-col li {
          margin-bottom: 8px;
      }
      
      /* Button Style (More prominent) */
      .btn-primary {
          display: inline-block;
          padding: 12px 25px;
          background-color: #007bff;
          color: white;
          text-decoration: none;
          border-radius: 50px; /* Pill shape */
          font-weight: 700;
          font-size: 1.1rem;
          letter-spacing: 0.5px;
          transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
          box-shadow: 0 8px 20px rgba(0, 123, 255, 0.4);
      }
      
      .btn-primary:hover {
          background-color: #0056b3;
          transform: translateY(-3px);
          box-shadow: 0 12px 25px rgba(0, 123, 255, 0.6);
      }
      
      .btn-primary:active {
          transform: translateY(-1px);
          box-shadow: 0 4px 10px rgba(0, 123, 255, 0.4);
      }
      
      /* Back Link */
      .back-link {
          display: inline-block;
          margin-top:20px;
          font-weight:700;
          color:#6c757d;
          text-decoration:none;
          transition: color 0.2s ease;
      }
      
      .back-link:hover {
          color:#007bff;
          text-decoration:underline;
      }
      
    </style>
    """

    page_html = f"""
    <div class="devops-page-shell">
      <div class="devops-bg-orb devops-bg-orb-1"></div>
      <div class="devops-bg-orb devops-bg-orb-2"></div>
      <div class="devops-bg-orb devops-bg-orb-3"></div>

      <div class="devops-wrapper">
        <div class="devops-hero-row">
          <div class="devops-hero-img-col">
            <img src="{LOCAL_DEVOPS_IMG}" alt="DevOps Course" />
          </div>
          <div class="devops-hero-text-col">
            <h1>The Complete DevOps Course</h1>
            <p>Master the tools and practices for modern software delivery and infrastructure automation.</p>
          </div>
        </div>

        <div class="devops-grid">
          {cards}
        </div>
      </div>
    </div>
    """
    return page_style + page_html


def render_service(service):
    sid = service
    label, icon = SERVICES.get(sid, (f"Unknown Service: {sid}", ""))

    # The original content is preserved but wrapped in new classes for styling
    topic_content = {
        "git-github": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Learn distributed version control, branching strategies, pull requests, and collaborative workflows.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Initialize a Git repository and perform basic commits</li>
          <li>Master branching, merging, and resolving conflicts</li>
          <li>Set up a GitHub repository and manage pull requests</li>
        </ol>
        """,

        "ci-cd": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Automate your build, test, and deployment processes using industry-leading CI/CD tools.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Create a Jenkins pipeline for a simple application</li>
          <li>Configure GitHub Actions for continuous integration</li>
          <li>Implement automated deployment to a staging environment</li>
        </ol>
        """,

        "docker": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Package applications into portable containers, manage images, and orchestrate multi-container apps with Docker Compose.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Write a Dockerfile to containerize a web application</li>
          <li>Manage images and push them to a container registry</li>
          <li>Use Docker Compose to run a multi-service application locally</li>
        </ol>
        """,

        "kubernetes": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Orchestrate containers with Kubernetes: deployments, services, ingress, and scaling strategies.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Deploy a containerized app to a Kubernetes cluster</li>
          <li>Expose the app using Services and Ingress</li>
          <li>Scale deployments and roll out zero-downtime updates</li>
        </ol>
        """,

        "iac-terraform": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Provision cloud resources declaratively using Terraform modules, state management, and workspaces.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Create a Terraform configuration to deploy a VPC and EC2 instance</li>
          <li>Use variables, outputs, and remote state backends</li>
          <li>Refactor into reusable modules and manage environments</li>
        </ol>
        """,

        "config-ansible": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Automate server configuration using Ansible playbooks, roles, and inventories for idempotent setups.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Write an Ansible playbook to configure a web server</li>
          <li>Create roles and organize group/host inventories</li>
          <li>Run playbooks against multiple servers in parallel</li>
        </ol>
        """,

        "monitoring-logging": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Collect metrics and logs to detect issues early and visualize system health and performance.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Install Prometheus and Grafana, add basic dashboards</li>
          <li>Ship application logs to an ELK or OpenSearch stack</li>
          <li>Create alerts for error spikes and high latency</li>
        </ol>
        """,

        "devsecops": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Integrate security into CI/CD pipelines using code scanning, dependency checks, and container security.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Enable static code analysis in a CI pipeline</li>
          <li>Scan container images for vulnerabilities</li>
          <li>Add dependency and secret scanning to GitHub Actions</li>
        </ol>
        """,

        "scripting": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Use shell and Python scripts to automate repetitive DevOps tasks on servers and in pipelines.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Write Bash scripts to automate log collection and backups</li>
          <li>Use Python to call cloud APIs and manage resources</li>
          <li>Integrate scripts into CI/CD jobs for automation</li>
        </ol>
        """,

        "cloud-devops": f"""
        <h2>{label}</h2>
        <p class="service-description">
          Apply DevOps practices to cloud platforms, focusing on automation, scalability, and cost optimization.
        </p>
        <h3>Hands-on labs</h3>
        <ol class="service-labs">
          <li>Deploy a simple app with IaC to your preferred cloud</li>
          <li>Set up a CI/CD pipeline targeting cloud resources</li>
          <li>Implement autoscaling and basic cost monitoring</li>
        </ol>
        """,
    }

    content = topic_content.get(
        sid,
        f"<h2>{label}</h2><p class='service-description'>No detailed content prepared yet.</p>",
    )

    return f"""
      <div class="service-detail-container">
        <div class="service-icon-col">
          <div class="service-icon-wrapper">
            <img src="{icon}" alt="{label}">
          </div>
        </div>

        <div class="service-content-col">
          {content}
          <div style="margin-top:30px;">
            <a class="btn-primary" href="/contact">Contact / Enroll</a>
          </div>
          <p>
            <a href="/course/devops" class="back-link">⬅ Back to DevOps</a>
          </p>
        </div>
      </div>
    """

def get_course_html():
    return render()
