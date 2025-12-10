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
    "version-control": (
        "Version Control System (Git / GitHub / Bitbucket)",
        "/images/devops_images/Git Hub.png"
    ),
    "bitbucket": (
        "Bitbucket",
        "/images/devops_images/bitbucket.png"
    ),
    "ci-cd": (
        "CI/CD (Jenkins / GitHub Actions)",
        "/images/devops_images/CI CD.png"
    ),
    "gitlab-ci": (
        "GitLab CI",
        "/images/devops_images/gitlab_ci.png"
    ),
    "argo-cd": (
        "Argo CD",
        "/images/devops_images/argo_cd.png"
    ),
    "docker": (
        "Docker & Containerization",
        "/images/devops_images/docker.png"
    ),
    "kubernetes": (
        "Container Orchestration (Kubernetes)",
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
    "monitoring-prometheus": (
        "Monitoring (Prometheus / Grafana)",
        "/images/devops_images/Monitoring.png"
    ),
    "aws-cloudwatch": (
        "AWS CloudWatch",
        "/images/devops_images/aws_cloudwatch.png"
    ),
    "aws-cloudtrail": (
        "AWS CloudTrail",
        "/images/devops_images/aws_cloudtrail.png"
    ),
    "devsecops": (
        "DevSecOps (Security in CI/CD)",
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
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');

      .devops-page-shell {
        position:relative;
        padding:40px;
        border-radius:32px;
        background: #ffffff; /* White background requested */
        border:1px solid #e2e8f0;
        box-shadow:0 25px 50px rgba(0,0,0,0.1);
        overflow:hidden;
        font-family: 'Outfit', sans-serif;
        color: #1e293b; /* Dark text */
        max-width: 1400px; /* Increase max width to accommodate 5 columns */
        margin: 0 auto;
      }

      /* --- DYNAMIC BACKGROUND (Subtle light mode) --- */
      .devops-page-shell::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.05), transparent 50%),
                    radial-gradient(circle at 10% 20%, rgba(139, 92, 246, 0.05), transparent 40%);
        animation: rotate-bg 20s linear infinite;
        z-index: 0;
      }
      
      @keyframes rotate-bg {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }

      /* --- HERO SECTION --- */
      .devops-wrapper {
        position:relative;
        z-index:1;
        display:flex;
        flex-direction:column;
        gap:40px;
      }

      .devops-hero-row {
        display:flex;
        gap:30px;
        align-items:center;
        justify-content: center;
        text-align: center;
        flex-wrap:wrap;
        padding-bottom:30px;
        border-bottom:1px solid #e2e8f0;
      }

      .devops-hero-img-col img {
        width:140px;
        height:140px;
        object-fit:contain; /* Fit properly */
        border-radius:50%;
        box-shadow:0 10px 30px rgba(56, 189, 248, 0.2);
        border: 4px solid #fff;
        background: #f8fafc; /* Slight bg to ensure circle shape if image is transparent */
        animation: rotate-hero 20s linear infinite; /* Slow rotation */
      }
      
      @keyframes rotate-hero {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }

      .devops-hero-text-col h1 {
        margin:0 0 12px 0;
        font-size:3rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%); /* Dark gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.02em;
      }

      .devops-hero-text-col p {
        color: #64748b; /* Slate 500 */
        font-size:1.25rem;
        max-width: 600px;
        margin: 0 auto;
        font-weight: 300;
      }

      /* --- GRID LAYOUT (5 Columns) --- */
      .devops-grid {
        display:grid;
        /* Force 5 columns, min 180px each */
        grid-template-columns: repeat(5, 1fr); 
        gap: 20px;
        padding: 20px;
      }
      
      /* Responsive fallback for smaller screens */
      @media (max-width: 1200px) {
        .devops-grid {
           grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        }
      }

      /* --- EXTREME CARD STYLES --- */
      .devops-module-card {
        cursor:pointer;
        position:relative;
        transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        z-index: 1;
        /* Ensure card takes full height of grid cell */
        height: 100%;
      }

      .devops-module-card-inner {
        height: auto; /* Let content dictate height */
        min-height: 150px; /* Reduced minimum height */
        border-radius: 20px;
        background: #fff; /* White cards */
        border: 1px solid #e2e8f0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 15px 10px; /* Reduced padding */
        gap: 10px; /* Reduced gap */
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.05);
        transition: all 0.4s ease;
        overflow: hidden;
        position: relative;
      }

      /* Image styling - CONTAINED */
      .devops-card-img-contain, .devops-card-img-cover {
        position: relative;
        width: 110px; /* Increased from 80px */
        height: 110px;
        object-fit: contain;
        transition: transform 0.4s ease, filter 0.4s ease;
        z-index: 0;
      }
      
      /* Label styling - BELOW IMAGE */
      .devops-card-label {
        font-size: 0.95rem; /* Slightly smaller text */
        font-weight: 700;
        text-align: center;
        color: #1e293b;
        position: relative;
        width: 100%;
        padding: 0;
        z-index: 2;
        text-shadow: none;
        transition: transform 0.3s ease, color 0.3s ease;
        line-height: 1.2;
      }

      /* --- HOVER EFFECTS (MAGNIFY + GLOW) --- */
      .devops-module-card:hover {
        transform: scale(1.1) translateY(-5px);
        z-index: 10;
      }

      .devops-module-card:hover .devops-module-card-inner {
        border-color: #38bdf8;
        box-shadow: 
            0 0 0 2px rgba(56, 189, 248, 0.2),
            0 25px 50px -12px rgba(56, 189, 248, 0.25);
      }

      .devops-module-card:hover .devops-card-img-contain, 
      .devops-module-card:hover .devops-card-img-cover {
        transform: scale(1.1) rotate(5deg);
        filter: brightness(1.05);
      }
      
      .devops-module-card:hover .devops-card-label {
        color: #0284c7; /* Blue text on hover */
      }
      
    </style>
    """

    page_html = f"""
    <div class="devops-page-shell">
      <div class="devops-wrapper">
        <div class="devops-hero-row">
          <div class="devops-hero-img-col">
            <img src="{LOCAL_DEVOPS_IMG}" alt="DevOps Course" />
          </div>
          <div class="devops-hero-text-col">
            <h1>DevOps Mastery 2025</h1>
            <p>Future-proof your career with next-gen infrastructure automation and CI/CD pipelines.</p>
          </div>
        </div>

        <div class="devops-grid">
          {cards}
        </div>
      </div>
    """
    return page_style + page_html


def render_service(service):
    sid = service
    label, icon = SERVICES.get(sid, (f"Unknown Service: {sid}", ""))

    # Import content from backend
    try:
        from backend_devops import DEVOPS_CONTENT
    except ImportError:
        DEVOPS_CONTENT = {}

    content = DEVOPS_CONTENT.get(
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
