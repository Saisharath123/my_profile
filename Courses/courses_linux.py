# courses_linux.py
# Linux Administration module (SSR Edition - Fixes Blank Page Issue)
# Exposes: render() -> HTML string

import json

def render():
    # --- DATA IMPORT ---
    # --- DATA IMPORT ---
    # --- DATA IMPORT ---
    try:
        from .all_modules import LINUX_TOPICS
    except ImportError:
        # Fallback for dev safety
        LINUX_TOPICS = []

    # Generate HTML for grid items (Server-Side)
    modules_html = ""
    for m in LINUX_TOPICS:
        # We store the detailed content in a data-attribute to be read by JS, 
        # avoiding injection issues while keeping initial render fast.
        import html
        safe_content = html.escape(m["c"])
        modules_html += f"""
        <div class="module-card" onclick="openLinuxModal('{m['k']}')">
            <div class="mc-header">
                <div class="mc-icon">{m['i']}</div>
                <div class="mc-title">{m['t']}</div>
            </div>
            <div class="mc-desc">{m['d']}</div>
            <div class="mc-footer">Start Module</div>
            <!-- Hidden content storage for this module -->
            <div id="content-{m['k']}" style="display:none;">{safe_content}</div>
        </div>
        """

    # Generate Widget HTML
    try:
        from .smart_widget import render_widget
        widget_html = render_widget()
    except ImportError:
        widget_html = "<div style='color:white'>Error loading widget.</div>"

    # Generate Lab HTML
    try:
        from .virtual_lab import render_lab
        lab_html = render_lab()
    except ImportError:
        lab_html = "<div style='color:white'>Error loading Virtual Lab.</div>"

    return f"""
    <style>
        /* --- CSS STYLES --- */
        .linux-wrapper {{ font-family: 'Inter', system-ui, sans-serif; color: #1e293b; max-width: 1200px; margin: 0 auto; }}
        
        /* Hero */
        .linux-hero {{
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border-radius: 20px; padding: 40px; color: #fff; margin-bottom: 24px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2); position: relative; overflow: hidden;
        }}
        
        .linux-hero-content {{ display: flex; align-items: center; gap: 30px; position: relative; z-index: 2; }}

        .linux-logo-img {{
            width: 110px; height: 110px; object-fit: cover;
            border-radius: 12px;
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.25);
            animation: floatLogo 4s ease-in-out infinite;
        }}

        .linux-hero h1 {{ 
            margin: 0 0 10px 0; font-size: 2.5rem; font-weight: 800; 
            background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc, #38bdf8);
            background-size: 300% auto;
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            animation: textShine 4s linear infinite;
        }}
        .linux-hero p {{ color: #94a3b8; font-size: 1.1rem; max-width: 700px; margin: 0; line-height: 1.5; }}

        @keyframes textShine {{ to {{ background-position: 200% center; }} }}
        @keyframes floatLogo {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-8px); }} }}

        /* Tabs */
        .linux-tabs {{ display: flex; gap: 8px; margin-bottom: 24px; border-bottom: 2px solid #e2e8f0; }}
        .linux-tab-btn {{
            background: transparent; border: none; padding: 12px 20px; font-weight: 600; color: #64748b;
            cursor: pointer; font-size: 1rem; border-bottom: 3px solid transparent; transition: all 0.2s;
        }}
        .linux-tab-btn:hover {{ color: #0284c7; background: #f8fafc; }}
        .linux-tab-btn.active {{ color: #0f172a; border-bottom-color: #0284c7; }}
        
        .linux-view {{ display: none; margin-top: 20px; animation: fadeIn 0.3s ease-out; }}
        .linux-view.active {{ display: block; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(5px); }} to {{ opacity: 1; transform: translateY(0); }} }}

        /* Grid */
        .modules-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }}
        .module-card {{
            background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;
            cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; display: flex; flex-direction: column;
        }}
        .module-card:hover {{ transform: translateY(-4px); box-shadow: 0 10px 20px -5px rgba(0,0,0,0.1); border-color: #38bdf8; }}
        .mc-header {{ display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }}
        .mc-icon {{ width: 42px; height: 42px; background: #f0f9ff; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; }}
        .mc-title {{ font-weight: 700; color: #0f172a; font-size: 1.05rem; }}
        .mc-desc {{ font-size: 0.9rem; color: #64748b; margin-bottom: 16px; flex-grow: 1; line-height: 1.5; }}
        .mc-footer {{ border-top: 1px solid #f1f5f9; padding-top: 12px; font-size: 0.8rem; font-weight: 700; color: #3b82f6; text-transform: uppercase; }}

        /* Modal */
        .overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(15,23,42,0.8); z-index: 2000; display: none; align-items: center; justify-content: center; padding: 20px; }}
        .modal {{ background: #fff; width: 100%; max-width: 700px; max-height: 85vh; border-radius: 12px; display: flex; flex-direction: column; box-shadow: 0 25px 50px rgba(0,0,0,0.5); }}
        .modal-header {{ padding: 20px; border-bottom: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; border-radius: 12px 12px 0 0; }}
        .modal-body {{ padding: 30px; overflow-y: auto; line-height: 1.6; color: #334155; }}
        .modal-body pre {{ background: #1e293b; color: #e2e8f0; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 15px 0; font-family: 'Consolas', monospace; }}
    </style>

    <div class="linux-wrapper">
        <!-- Hero -->
        <div class="linux-hero">
            <div class="linux-hero-content">
                <img src="/images/linux.jpg" alt="Linux" class="linux-logo-img">
                <div>
                    <h1>Linux Administration Masterclass</h1>
                    <p>Comprehensive resource for mastering the Command Line Interface (CLI) and System Administration.</p>
                </div>
            </div>
        </div>

        <!-- Navigation -->
        <div class="linux-tabs">
            <button class="linux-tab-btn active" onclick="switchTab('modules', this)">📚 All Modules</button>
            <button class="linux-tab-btn" onclick="switchTab('widget', this)">🧠 Smart Widget</button>
            <button class="linux-tab-btn" onclick="switchTab('lab', this)">💻 Virtual Lab</button>
        </div>

        <!-- TAB 1: MODULES GRID -->
        <div id="view-modules" class="linux-view active">
            <div class="modules-grid">
                {modules_html}
            </div>
        </div>

        <!-- TAB 2: SMART WIDGET -->
        <div id="view-widget" class="linux-view">
            {widget_html}
        </div>

        <!-- TAB 3: VIRTUAL LAB -->
        <div id="view-lab" class="linux-view">
            {lab_html}
        </div>
    </div>

    <!-- MODAL -->
    <div id="linux-modal" class="overlay" onclick="closeLinuxModal(event)">
        <div class="modal">
            <div class="modal-header">
                <div style="font-weight:800; font-size:1.2rem;" id="modal-title">Module</div>
                <button onclick="closeLinuxModal(null)" style="border:none; background:none; font-size:1.5rem; cursor:pointer;">×</button>
            </div>
            <div class="modal-body" id="modal-content"></div>
        </div>
    </div>

    <!-- SCRIPTS -->
    <script>
        // --- Tab Logic ---
        function switchTab(viewId, btn) {{
            document.querySelectorAll('.linux-view').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.linux-tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById('view-' + viewId).classList.add('active');
            btn.classList.add('active');
        }}

        // --- Modal Logic ---
        function openLinuxModal(key) {{
            const contentDiv = document.getElementById('content-' + key);
            if (!contentDiv) return;
            
            // Decode HTML entities
            const txt = document.createElement("textarea");
            txt.innerHTML = contentDiv.innerHTML;
            
            document.getElementById('modal-title').innerText = "Module Content"; 
            document.getElementById('modal-content').innerHTML = txt.value;
            document.getElementById('linux-modal').style.display = 'flex';
        }}
        
        function closeLinuxModal(e) {{
            if (e && !e.target.classList.contains('overlay')) return;
            document.getElementById('linux-modal').style.display = 'none';
        }}
    </script>
    """

