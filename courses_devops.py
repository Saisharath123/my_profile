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

def _card_html(href, label, icon_url, is_submodule=False, back_content=None):
    """
    Reusable card component. Supports standard link cards and Flip Cards.
    """
    # Cover IDs for main modules that need 'cover' fit style
    cover_ids = {"monitoring-logging", "devsecops", "cloud-devops"} 
    
    img_class = "devops-card-img-contain"
    if any(x in label for x in ["Monitoring", "DevSecOps", "Cloud DevOps"]) and not is_submodule:
         img_class = "devops-card-img-cover"

    # Specific override for GCP image size as requested
    img_style = ""
    if label == "GCP":
        img_style = "width: 130px; height: 130px;"

    # --- FLIP CARD LOGIC (for Submodules) ---
    if back_content:
        return f"""
        <div class="flip-card" tabindex="0">
          <div class="flip-card-inner">
            <!-- FRONT -->
            <div class="flip-card-front">
              <div class="devops-module-card-inner-static">
                 <img src="{icon_url}" alt="{label}" class="{img_class}" style="{img_style}">
                 <div class="devops-card-label">{label}</div>
              </div>
            </div>
            <!-- BACK -->
            <div class="flip-card-back">
               <div class="flip-content-scroll">
                  {back_content}
               </div>
            </div>
          </div>
        </div>
        """
    
    # --- STANDARD LINK CARD (for Main Modules) ---
    card_class = "devops-module-card"
    if is_submodule: 
        card_class += " submodule-card"

    return f"""
      <a href="{href}" class="devops-module-link" style="text-decoration:none;color:inherit;">
        <div class="{card_class}" tabindex="0">
          <div class="devops-module-card-inner">
            <img src="{icon_url}" alt="{label}" class="{img_class}" style="{img_style}">
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
        from backend_devops import DEVOPS_CONTENT, DEVOPS_SUBMODULES, DEVOPS_TOOL_DETAILS
    except ImportError:
        DEVOPS_CONTENT = {}
        DEVOPS_SUBMODULES = {}
        DEVOPS_TOOL_DETAILS = {}

    label, icon = SERVICES.get(service_id, (f"{service_id}", ""))
    
    # Check if we have submodules defined
    submodules = DEVOPS_SUBMODULES.get(service_id, [])

    if submodules:
        # Render a grid of submodules
        cards_html = ""
        for item in submodules:
            # Check for backend details
            tool_id = item.get('id')
            detail_html = DEVOPS_TOOL_DETAILS.get(tool_id, "<p>More details coming soon...</p>")
            
            # Pass detailed content to the card
            cards_html += _card_html("#", item['label'], item['image'], is_submodule=True, back_content=detail_html)
        
        description = "Explore the essential tools and technologies in this category. Hover over a card to see details."
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

      /* --- CARD STYLES (MAIN) --- */
      .devops-module-card {
        cursor:pointer;
        height: 100%;
        perspective: 1000px;
      }

      .devops-module-card-inner, .devops-module-card-inner-static {
        height: auto;
        min-height: 220px; /* Increased height for uniformity */
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
      
      .devops-module-card-inner-static {
        width: 100%; height: 100%; border:none; box-shadow:none; /* For inside flip */
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

      /* Hover Effects (Main Link Cards) */
      .devops-module-card:hover .devops-module-card-inner {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        border-color: #38bdf8;
      }
      
      .devops-module-card:hover .devops-card-img-contain {
        transform: scale(1.1) rotate(5deg);
      }

      /* --- FLIP CARD STYLES (SUBMODULES) --- */
      .flip-card {
        background-color: transparent;
        perspective: 1000px;
        height: 320px; /* Fixed height required for flip */
        cursor: pointer;
      }

      .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
        border-radius: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      }

      .flip-card:hover .flip-card-inner, .flip-card:focus .flip-card-inner {
        transform: rotateY(180deg);
      }

      .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        overflow: hidden;
      }

      .flip-card-front {
        background-color: #fff;
        color: black;
      }
      
      /* Front content needs to mimic the standard card layout */
      .flip-card-front .devops-module-card-inner-static {
         display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;
      }

      .flip-card-back {
        background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
        color: #334155;
        transform: rotateY(180deg);
        text-align: left;
        display: flex; 
        flex-direction: column;
        border-color: #bae6fd;
      }

      .flip-content-scroll {
        padding: 20px;
        overflow-y: auto;
        height: 100%;
        font-size: 0.9rem;
      }
      
      /* Scrollbar styling for back content */
      .flip-content-scroll::-webkit-scrollbar { width: 6px; }
      .flip-content-scroll::-webkit-scrollbar-track { background: transparent; }
      .flip-content-scroll::-webkit-scrollbar-thumb { background-color: #cbd5e1; border-radius: 10px; }

      /* Typography for Back Content */
      .flip-content-scroll h3 { font-size: 1rem; color: #0f172a; margin-top:0; margin-bottom: 8px; border-bottom: 2px solid #38bdf8; display:inline-block; padding-bottom:2px; }
      .flip-content-scroll h4 { font-size: 0.9rem; color: #475569; margin: 12px 0 6px 0; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
      .flip-content-scroll p { margin-bottom: 8px; line-height: 1.4; }
      .flip-content-scroll ul { padding-left: 16px; margin-bottom: 8px; }
      .flip-content-scroll li { margin-bottom: 4px; }
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
