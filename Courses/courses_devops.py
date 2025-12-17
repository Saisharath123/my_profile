# courses_devops.py
# DevOps module (uses images from your images/devops_images folder)
# Exposes:
#   - render() -> HTML string (main DevOps page)
#   - render_service(service) -> HTML string (service/tool detail pages)
#   - get_course_html() -> alias for render()

from flask import url_for

# Header image served from your images/ directory
LOCAL_DEVOPS_IMG = "/images/devops_images/k8.png"

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

def _card_html(href, label, icon_url, is_submodule=False, attributes=""):
    """
    Reusable card component. 
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

    # Add special class for Kubernetes (Container Orchestration)
    if "Container Orchestration" in label:
        img_class += " k8s-spin-target"

    card_class = "devops-module-card"
    if is_submodule: 
        card_class += " submodule-card"

    return f"""
      <a href="{href}" {attributes} class="devops-module-link" style="text-decoration:none;color:inherit;">
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

    return _wrap_in_page("DevOps Mastery 2025", "Future-proof your career with next-gen infrastructure automation and CI/CD pipelines.", cards_html, hero_image=LOCAL_DEVOPS_IMG, back_link="/courses")

def render_service(service_id):
    """
    Renders the Second Level (Sub-modules) or Content for a specific module.
    """
    # 1. Get the submodules from backend
    try:
        from .backend_devops import DEVOPS_CONTENT, DEVOPS_SUBMODULES, DEVOPS_TOOL_DETAILS
    except ImportError:
        DEVOPS_CONTENT = {}
        DEVOPS_SUBMODULES = {}
        DEVOPS_TOOL_DETAILS = {}

    label, icon = SERVICES.get(service_id, (f"{service_id}", ""))
    
    # Check if we have submodules defined
    submodules = DEVOPS_SUBMODULES.get(service_id, [])

    if submodules:
        # Prepare content for JS
        import json
        
        # Helper to safely serialize content
        tool_data_json = json.dumps(DEVOPS_TOOL_DETAILS)

        # Render a grid of submodules
        cards_html = ""
        for item in submodules:
            tool_id = item.get('id')
            # Use onclick to open modal
            # We revert _card_html to standard and wrap in a clickable div or adjust _card_html
            # But simpler: _card_html returns an anchor. We can make href="javascript:void(0)" and onclick.
            
            click_attr = f'onclick="openModal(\'{tool_id}\')"'
            cards_html += _card_html("javascript:void(0)", item['label'], item['image'], is_submodule=True, attributes=click_attr)
        
        description = "Explore the essential tools and technologies in this category."
        
        # Add Modal HTML and Script
        modal_html = f"""
        <!-- MODAL OVERLAY -->
        <div id="devops-modal-overlay" class="devops-modal-overlay" onclick="closeModal(event)">
            <div class="devops-modal-container">
                <button class="devops-modal-close" onclick="closeModal(event)">×</button>
                <div id="devops-modal-content" class="devops-modal-content">
                    <!-- Content injected via JS -->
                </div>
            </div>
        </div>

        <script>
            const TOOL_DATA = {tool_data_json};

            function openModal(toolId) {{
                const content = TOOL_DATA[toolId];
                if (!content) return;
                
                const overlay = document.getElementById('devops-modal-overlay');
                const contentDiv = document.getElementById('devops-modal-content');
                
                contentDiv.innerHTML = content;
                overlay.classList.add('active');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
            }}

            function closeModal(e) {{
                // Close if clicked on overlay (outside container) or close button
                if (e.target === e.currentTarget || e.target.classList.contains('devops-modal-close')) {{
                    const overlay = document.getElementById('devops-modal-overlay');
                    overlay.classList.remove('active');
                    document.body.style.overflow = '';
                }}
            }}
        </script>
        """

        return _wrap_in_page(label, description, cards_html + modal_html, back_link="/course/devops", hero_image=icon)

    else:
        # Fallback to text content if no submodules
        content = DEVOPS_CONTENT.get(service_id, "<p>Coming soon...</p>")
        return _wrap_content(label, content, icon)


def _wrap_in_page(title, subtitle, grid_content, back_link=None, hero_image=None):
    """
    Wraps the grid content in the standard page shell.
    """
    
    back_html = ""
    if back_link:
        back_html = f"""
        <div style="margin-bottom: 20px; position: relative; z-index: 10;">
            <a href="{back_link}" style="display:inline-flex;align-items:center;gap:6px;font-weight:700;color:#64748b;text-decoration:none;">
                <span>⬅ Back</span>
            </a>
        </div>
        """

    # Determine if rotation should be applied (Only for Kubernetes/Container Orchestration)
    extra_cls = ""
    if "Kubernetes" in title or "Container Orchestration" in title or "DevOps Mastery" in title:
        extra_cls = " spin-me"

    img_html = ""
    if hero_image:
        img_html = f"""
        <div class="devops-hero-img-container">
            <img src="{hero_image}" alt="Hero" class="devops-hero-img{extra_cls}">
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

      @keyframes aurora {
        0% { transform: translate(0, 0) rotate(0deg); }
        33% { transform: translate(5%, 5%) rotate(2deg); }
        66% { transform: translate(-5%, 2%) rotate(-2deg); }
        100% { transform: translate(0, 0) rotate(0deg); }
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
        flex-direction: row;
        align-items:center;
        justify-content: center;
        gap: 40px;
        text-align: left;
        padding: 40px;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(241, 245, 249, 0.9) 100%);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 1);
        box-shadow: 
            0 10px 30px -10px rgba(56, 189, 248, 0.2), 
            inset 0 0 0 1px rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
      }
      
      /* Decorative subtle Glow behind text */
      .devops-hero-row::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 70% 30%, rgba(139, 92, 246, 0.08), transparent 40%),
                    radial-gradient(circle at 20% 80%, rgba(56, 189, 248, 0.08), transparent 40%);
        pointer-events: none;
        z-index: 0;
      }
      
      /* Make sure content is above the glow */
      .devops-hero-img-container, .devops-hero-text-col {
        position: relative;
        z-index: 1;
      }

      /* On mobile, stack them */
      @media (max-width: 768px) {
        .devops-hero-row { flex-direction: column; text-align: center; padding: 25px; }
      }

      .devops-hero-img-container {
        width: 140px;
        height: 140px;
        flex-shrink: 0;
        filter: drop-shadow(0 10px 20px rgba(59, 130, 246, 0.3)); /* Glow for the image */
      }
      
      .devops-hero-img {
        width: 100%;
        height: 100%;
        object-fit: contain;
      }

      .devops-hero-img.spin-me {
        animation: rotate-img 20s linear infinite;
      }
      
      @keyframes rotate-img {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }

      .devops-hero-text-col h1 {
        margin:0 0 15px 0;
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 50%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        line-height: 1.1;
        filter: drop-shadow(0 2px 4px rgba(59, 130, 246, 0.1));
      }

      .devops-hero-text-col p {
        color: #475569;
        font-size: 1.35rem;
        max-width: 650px;
        margin: 0;
        font-weight: 500;
        line-height: 1.6;
        opacity: 0.9;
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
        transition: transform 0.3s ease;
      }

      .devops-module-card-inner {
        height: auto;
        min-height: 160px; /* REVERTED TO ORIGINAL HEIGHT */
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
      
      /* Standard hover: Scale only, no rotate */
      .devops-module-card:hover .devops-card-img-contain {
        transform: scale(1.1);
      }
      
      /* Kubernetes specific: Scale + Spin */
      .devops-module-card:hover .devops-card-img-contain.k8s-spin-target {
        animation: spin-icon 4s linear infinite;
      }
      
      @keyframes spin-icon {
        0% { transform: scale(1.1) rotate(0deg); }
        100% { transform: scale(1.1) rotate(360deg); }
      }

      /* --- HIGH-END MODAL STYLES --- */
      .devops-modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s ease, visibility 0.3s ease;
      }

      .devops-modal-overlay.active {
        opacity: 1;
        visibility: visible;
      }

      .devops-modal-container {
        background: #ffffff;
        width: 90%;
        max-width: 800px;
        max-height: 85vh;
        border-radius: 24px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        position: relative;
        transform: scale(0.95);
        transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        overflow: hidden;
        display: flex;
        flex-direction: column;
        border: 1px solid rgba(255, 255, 255, 0.5);
      }

      .devops-modal-overlay.active .devops-modal-container {
        transform: scale(1);
      }

      .devops-modal-close {
        position: absolute;
        top: 15px;
        right: 15px;
        background: #f1f5f9;
        border: none;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        font-size: 1.2rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #64748b;
        transition: all 0.2s;
        z-index: 10;
        font-family: inherit;
      }

      .devops-modal-close:hover {
        background: #e2e8f0;
        color: #0f172a;
        transform: rotate(90deg);
      }

      .devops-modal-content {
        padding: 40px;
        overflow-y: auto;
        color: #334155;
        font-size: 1.05rem;
        line-height: 1.7;
      }

      /* Modal Typography High-End Tweaks */
      .devops-modal-content h3 {
        font-size: 1.8rem;
        background: linear-gradient(135deg, #0f172a 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 0;
        margin-bottom: 20px;
        font-weight: 800;
      }
      
      .devops-modal-content h4 {
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #475569;
        border-left: 4px solid #3b82f6;
        padding-left: 12px;
      }
      
      .devops-modal-content ul {
        background: #f8fafc;
        border-radius: 12px;
        padding: 20px 40px;
        border: 1px solid #f1f5f9;
      }
      
      .devops-modal-content li {
        margin-bottom: 8px;
      }
      
      /* Scrollbar */
      .devops-modal-content::-webkit-scrollbar { width: 8px; }
      .devops-modal-content::-webkit-scrollbar-track { background: transparent; }
      .devops-modal-content::-webkit-scrollbar-thumb { background-color: #cbd5e1; border-radius: 10px; }
    </style>
    """

    page_html = f"""
    <div class="devops-page-shell">
      {back_html}
      <div class="devops-wrapper">
        <div class="devops-hero-row">
          {img_html}
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
