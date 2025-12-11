# courses_devops.py
# DevOps module (uses images from your images/devops_images folder)
# Exposes:
#   - render() -> HTML string (main DevOps page)
#   - render_service(service) -> HTML string (service/tool detail pages)
#   - get_course_html() -> alias for render()

from flask import url_for

# Header image served from your images/ directory
LOCAL_DEVOPS_IMG = "/images/devops.png"

# Service/tool definitions: id -> (label, served_image_url)
# These are the MAIN categories.
SERVICES = {
    "git-github": (
        "Version Control System",
        "/images/devops_images/Git Hub.png"
    ),
    "ci-cd": (
        "CI/CD",
        "/images/devops_images/CI CD.png"
    ),
    "docker": (
        "Docker & Containerization",
        "/images/devops_images/docker.png"
    ),
    "kubernetes": (
        "Container Orchestration",
        "/images/devops_images/k8.png"
    ),
    "iac-terraform": (
        "Infrastructure as Code",
        "/images/devops_images/terraform.png"
    ),
    "config-ansible": (
        "Configuration Management",
        "/images/devops_images/ansible.webp"
    ),
    "monitoring-logging": (
        "Monitoring & Logging",
        "/images/devops_images/Monitoring.png"
    ),
    "devsecops": (
        "DevSecOps",
        "/images/devops_images/DevSecOps.png"
    ),
    "scripting": (
        "Scripting",
        "/images/devops_images/LINUX.png"
    ),
    "cloud-devops": (
        "Cloud DevOps",
        "/images/devops_images/cloud.png"
    ),
}

def _card_html(href, label, icon_url, is_submodule=False):
    """
    Reusable card component.
    """
    # Cover IDs for main modules that need 'cover' fit style
    cover_ids = {"monitoring-logging", "devsecops", "cloud-devops"} 
    # For submodules, we mostly want 'contain' to show the tool logo clearly.
    
    # Heuristic: if valid URL specific logic needed
    img_class = "devops-card-img-contain"
    if any(x in label for x in ["Monitoring", "DevSecOps", "Cloud DevOps"]) and not is_submodule:
         img_class = "devops-card-img-cover"

    card_class = "devops-module-card"
    if is_submodule:
        card_class += " submodule-card"

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
    """
    Renders the Top Level DevOps Modules.
    """
    # Create cards for main services
    cards_html = ""
    for sid, (label, url) in SERVICES.items():
        href = f"/course/devops/{sid}"
        cards_html += _card_html(href, label, url, is_submodule=False)

    return _wrap_in_page("DevOps Mastery 2025", "Future-proof your career with next-gen infrastructure automation and CI/CD pipelines.", cards_html)

def render_service(service_id):
    """
    Renders the Second Level (Sub-modules) or Content for a specific module.
    """
    # 1. Get the submodules from backend
    try:
        from backend_devops import DEVOPS_CONTENT, DEVOPS_SUBMODULES
    except ImportError:
        DEVOPS_CONTENT = {}
        DEVOPS_SUBMODULES = {}

    label, icon = SERVICES.get(service_id, (f"{service_id}", ""))
    
    # Check if we have submodules defined
    submodules = DEVOPS_SUBMODULES.get(service_id, [])

    if submodules:
        # Render a grid of submodules
        cards_html = ""
        for item in submodules:
            # item = {'id': 'git', 'label': 'Git', 'image': '...'}
            # For now, sub-items are not clickable or loop back to same page or placeholder
            # The user asked for "each tool having its own details", implying 3rd level.
            # But currently we don't have routes for 3rd level. 
            # We'll make it visual for now.
            sub_href = "#"  
            cards_html += _card_html(sub_href, item['label'], item['image'], is_submodule=True)
        
        description = "Explore the essential tools and technologies in this category."
        return _wrap_in_page(label, description, cards_html, back_link="/course/devops")

    else:
        # Fallback to text content if no submodules
        content = DEVOPS_CONTENT.get(service_id, "<p>Coming soon...</p>")
        return _wrap_content(label, content, icon)


def _wrap_in_page(title, subtitle, grid_content, back_link=None):
    """
    Wraps the grid content in the standard page shell.
    """
    
    back_html = ""
    if back_link:
        back_html = f"""
        <div style="margin-bottom: 20px;">
            <a href="{back_link}" style="display:inline-flex;align-items:center;gap:6px;font-weight:700;color:#64748b;text-decoration:none;">
                <span>⬅ Back</span>
            </a>
        </div>
        """

    page_style = """
    <style>
      /* --- BASE STYLES & UTILITIES --- */
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');

      .devops-page-shell {
        position:relative;
        padding:40px;
        border-radius:32px;
        background: #ffffff;
        border:1px solid #e2e8f0;
        box-shadow:0 25px 50px rgba(0,0,0,0.1);
        overflow:hidden;
        font-family: 'Outfit', sans-serif;
        color: #1e293b;
        max-width: 1400px;
        margin: 0 auto;
      }

      /* --- DYNAMIC BACKGROUND --- */
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
        gap:30px;
      }

      .devops-hero-row {
        display:flex;
        flex-direction:column;
        align-items:center;
        text-align: center;
        padding-bottom:10px;
      }

      .devops-hero-text-col h1 {
        margin:0 0 12px 0;
        font-size:3rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.02em;
      }

      .devops-hero-text-col p {
        color: #64748b;
        font-size:1.2rem;
        max-width: 600px;
        margin: 0 auto;
        font-weight: 300;
      }

      /* --- GRID LAYOUT (5 Columns) --- */
      .devops-grid {
        display:grid;
        grid-template-columns: repeat(5, 1fr); 
        gap: 24px;
        padding: 10px 0;
      }
      
      @media (max-width: 1200px) {
        .devops-grid { grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }
      }

      /* --- CARD STYLES --- */
      .devops-module-card {
        cursor:pointer;
        height: 100%;
        perspective: 1000px;
      }

      .devops-module-card-inner {
        height: auto;
        min-height: 160px;
        border-radius: 20px;
        background: #fff;
        border: 1px solid #e2e8f0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px 10px;
        gap: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
      }

      .devops-card-img-contain, .devops-card-img-cover {
        width: 90px;
        height: 90px;
        object-fit: contain;
        transition: transform 0.4s ease;
      }

      .devops-card-label {
        font-size: 1rem;
        font-weight: 700;
        text-align: center;
        color: #334155;
      }

      /* Hover Effects */
      .devops-module-card:hover .devops-module-card-inner {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        border-color: #38bdf8;
      }
      
      .devops-module-card:hover .devops-card-img-contain {
        transform: scale(1.1) rotate(5deg);
      }
    </style>
    """

    page_html = f"""
    <div class="devops-page-shell">
      {back_html}
      <div class="devops-wrapper">
        <div class="devops-hero-row">
          <div class="devops-hero-text-col">
            <h1>{title}</h1>
            <p>{subtitle}</p>
          </div>
        </div>

        <div class="devops-grid">
          {grid_content}
        </div>
      </div>
    </div>
    """
    return page_style + page_html

def _wrap_content(title, content_html, icon_url):
    """
    Wraps text content for fallback.
    """
    return f"""
      <style>
        .devops-content-shell {{
            padding: 40px; background: #fff; border-radius: 24px; max-width: 1000px; margin: 0 auto;
            border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        }}
        .back-link {{ display: inline-block; margin-bottom: 20px; font-weight: bold; color: #64748b; text-decoration: none; }}
      </style>
      <div class="devops-content-shell">
         <a href="/course/devops" class="back-link">⬅ Back to DevOps</a>
         <div style="display:flex; align-items:center; gap: 20px; margin-bottom: 30px;">
            <img src="{icon_url}" style="width: 80px; height: 80px; object-fit: contain;">
            <h1 style="margin:0; font-size: 2.5rem; color: #0f172a;">{title}</h1>
         </div>
         <div style="font-size: 1.1rem; line-height: 1.7; color: #334155;">
            {content_html}
         </div>
      </div>
    """

def get_course_html():
    return render()
