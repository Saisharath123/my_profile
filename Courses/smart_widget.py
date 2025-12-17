# smart_widget.py
# Backend Content & Logic for Smart Command Explainer Widget

# Comprehensive Command Dictionary
# Categorized for better UI discoverability
COMMAND_DATA = {
    "File Operations": {
        "ls": "List directory contents. Usage: `ls -lah` (list all, human-readable).",
        "cd": "Change directory. Usage: `cd /var/log`.",
        "pwd": "Print Working Directory. Shows your current path.",
        "cp": "Copy files/directories. Usage: `cp -r source dest`.",
        "mv": "Move or rename files. Usage: `mv old.txt new.txt`.",
        "rm": "Remove files. Usage: `rm -rf folder` (Be careful!).",
        "mkdir": "Make Directory. Usage: `mkdir -p /path/to/new`.",
        "touch": "Create empty file or update timestamp. Usage: `touch file`.",
        "cat": "Concatenate and display file content.",
        "head": "Output the first part of files (default 10 lines).",
        "tail": "Output the last part of files. Usage: `tail -f log.txt` (follow).",
        "tar": "Archive utility. Usage: `tar -czvf archive.tar.gz /folder`.",
        "find": "Search for files. Usage: `find / -name '*.log'`.",
        "grep": "Search text using regex. Usage: `grep 'error' log.txt`.",
        "chmod": "Change file modes/permissions. Usage: `chmod 755 file`.",
        "chown": "Change file owner/group. Usage: `chown user:group file`.",
        "ln": "Make links between files. Usage: `ln -s target link` (symbolic).",
        "du": "Estimate file space usage. Usage: `du -sh folder`.",
        "df": "Report file system disk space usage. Usage: `df -h`."
    },
    "System Information": {
        "uname": "Print system information. Usage: `uname -a`.",
        "top": "Display Linux processes. Usage: `top`.",
        "htop": "Interactive process viewer (better than top).",
        "ps": "Report a snapshot of current processes. Usage: `ps aux`.",
        "kill": "Terminate a process. Usage: `kill -9 PID`.",
        "free": "Display memory usage. Usage: `free -m`.",
        "lscpu": "Display information about the CPU architecture.",
        "lsblk": "List block devices (disks).",
        "uptime": "Tell how long the system has been running.",
        "whoami": "Print effective userid.",
        "history": "Show command history.",
        "dmesg": "Print or control the kernel ring buffer.",
        "journalctl": "Query the systemd journal. Usage: `journalctl -xe`."
    },
    "Networking": {
        "ip": "Show/manipulate routing, devices, interfaces. Usage: `ip a`.",
        "ifconfig": "Configure a network interface (legacy).",
        "ping": "Send ICMP ECHO_REQUEST to network hosts.",
        "curl": "Transfer data from or to a server. Usage: `curl google.com`.",
        "wget": "Non-interactive network downloader.",
        "ssh": "OpenSSH remote login client. Usage: `ssh user@host`.",
        "scp": "Secure copy (remote file copy). Usage: `scp file user@host:/path`.",
        "netstat": "Print network connections, routing tables.",
        "ss": "Dump socket statistics (modern replacement for netstat).",
        "nc": "Netcat - arbitrary TCP and UDP connections and listens.",
        "traceroute": "Print the route packets trace to network host.",
        "nslookup": "Query Internet name servers interactively.",
        "dig": "DNS lookup utility. Usage: `dig domain.com`."
    },
    "OS Management (Ubuntu/Debian)": {
        "apt": "Package manager. Usage: `apt update && apt install pkg`.",
        "apt-get": "Legacy text-based package handling utility.",
        "dpkg": "Debian package manager (low level). Usage: `dpkg -i file.deb`.",
        "ufw": "Uncomplicated Firewall. Usage: `ufw allow 22`.",
        "systemctl": "Control the systemd system and service manager."
    },
    "OS Management (RHEL/CentOS)": {
        "yum": "Package manager (Yellowdog Updater Modified).",
        "dnf": "Dandified YUM - next-gen package manager.",
        "rpm": "RPM Package Manager. Usage: `rpm -ivh file.rpm`.",
        "firewall-cmd": "Firewalld command line client.",
        "sestatus": "SELinux status tool."
    },
    "Advanced/Misc": {
        "sudo": "Execute a command as another user (superuser).",
        "su": "Change user ID or become superuser.",
        "watch": "Execute a program periodically. Usage: `watch -n 1 'ls'`.",
        "alias": "Create a shortcut for a command.",
        "man": "An interface to the system reference manuals. Usage: `man ls`.",
        "echo": "Display a line of text.",
        "date": "Print or set the system date and time."
    }
}

# Flattened map for quick lookups
COMMAND_MAP = {}
for category, cmds in COMMAND_DATA.items():
    for cmd, desc in cmds.items():
        COMMAND_MAP[cmd] = {"desc": desc, "category": category}

def render_widget():
    """
    Returns the HTML component for the Smart Widget to be embedded in the main page.
    Includes its own CSS/JS constraints for modularity.
    """
    
    # Generate categories HTML
    cats_html = ""
    for cat in COMMAND_DATA.keys():
        slug = cat.replace(" ", "").replace("/", "").replace("(", "").replace(")", "")
        cats_html += f'<button class="sw-cat-btn" onclick="filterCmds(\'{cat}\')">{cat}</button>'

    # Generate all commands list for initial/fallback view (hidden or searchable)
    # We will pass the full data to JS to handle client-side searching/filtering
    
    import json
    data_js = json.dumps(COMMAND_DATA)

    return f"""
    <style>
        /* Modernized Styles for Smart Widget */
        .sw-container {{
            background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
            border-radius: 24px;
            padding: 32px;
            color: #f1f5f9;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(148, 163, 184, 0.1);
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            overflow: hidden;
            font-family: 'Inter', system-ui, sans-serif;
        }}
        
        /* CRITICAL FIX: Prevent search bar overflow */
        .sw-container * {{
            box-sizing: border-box; 
        }}

        .sw-header {{
            text-align: center;
            margin-bottom: 35px;
            position: relative;
            z-index: 2;
        }}
        .sw-header h2 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            background: linear-gradient(135deg, #60a5fa 0%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 10px 0;
            font-size: 2.4rem;
            letter-spacing: -0.02em;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
        }}
        .sw-header p {{
            font-size: 1.05rem;
            color: #94a3b8;
            margin: 0;
            opacity: 0.9;
        }}

        .sw-search-box {{
            position: relative;
            margin-bottom: 30px;
            z-index: 2;
        }}
        /* Search input styling */
        .sw-input {{
            width: 100%; /* Now respects padding due to box-sizing: border-box */
            padding: 18px 24px;
            padding-left: 56px;
            border-radius: 16px;
            border: 2px solid #334155;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(8px);
            color: #fff;
            font-size: 1.15rem;
            font-family: 'Fira Code', monospace;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
        }}
        .sw-input:focus {{
            outline: none;
            border-color: #60a5fa;
            background: rgba(15, 23, 42, 0.9);
            box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.2), inset 0 2px 4px rgba(0,0,0,0.2);
            transform: translateY(-1px);
        }}
        
        .sw-search-icon {{
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            color: #64748b;
            font-size: 1.3rem;
            pointer-events: none;
            transition: color 0.3s;
        }}
        .sw-input:focus ~ .sw-search-icon {{
            color: #60a5fa; 
        }}

        .sw-filters {{
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding: 4px 4px 16px 4px;
            margin-bottom: 20px;
            scrollbar-width: thin;
            scrollbar-color: #475569 transparent;
        }}
        .sw-filters::-webkit-scrollbar {{ height: 6px; }}
        .sw-filters::-webkit-scrollbar-track {{ background: transparent; }}
        .sw-filters::-webkit-scrollbar-thumb {{ background-color: #475569; border-radius: 20px; }}

        .sw-cat-btn {{
            background: #1e293b;
            border: 1px solid #334155;
            color: #94a3b8;
            padding: 10px 20px;
            border-radius: 99px;
            cursor: pointer;
            white-space: nowrap;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.2s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .sw-cat-btn:hover {{
            background: #334155;
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        .sw-cat-btn.active {{
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            border-color: transparent;
            color: #fff;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
            transform: translateY(-2px);
        }}

        .sw-results-area {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
            gap: 16px;
            max-height: 440px;
            overflow-y: auto;
            padding: 4px;
            padding-right: 8px;
        }}
        
        .sw-results-area::-webkit-scrollbar {{ width: 8px; }}
        .sw-results-area::-webkit-scrollbar-track {{ background: rgba(15, 23, 42, 0.5); border-radius: 4px; }}
        .sw-results-area::-webkit-scrollbar-thumb {{ background-color: #475569; border-radius: 4px; border: 2px solid transparent; background-clip: content-box; }}

        .sw-cmd-card {{
            background: rgba(51, 65, 85, 0.4); 
            padding: 20px 16px;
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: center;
            border: 1px solid rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        .sw-cmd-card:hover {{
            background: #334155;
            transform: translateY(-4px) scale(1.02);
            border-color: #60a5fa;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        }}

        .sw-cmd-name {{
            font-family: 'Fira Code', monospace;
            font-weight: 700;
            color: #38bdf8;
            font-size: 1.2rem;
            margin-bottom: 8px;
            background: rgba(56, 189, 248, 0.12);
            padding: 6px 10px;
            border-radius: 8px;
            transition: background 0.2s;
        }}
        .sw-cmd-card:hover .sw-cmd-name {{
            background: rgba(56, 189, 248, 0.25);
            color: #7dd3fc;
        }}

        .sw-cmd-desc-short {{
            font-size: 0.85rem;
            color: #cbd5e1;
            line-height: 1.5;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            opacity: 0.8;
        }}

        /* Detail Panel with sophisticated look */
        .sw-detail-panel {{
            margin-top: 35px;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid #3b82f6;
            border-radius: 20px;
            padding: 32px;
            display: none; 
            animation: slideUpFade 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            box-shadow: 0 20px 50px -10px rgba(0,0,0,0.6);
        }}
        @keyframes slideUpFade {{ 
            from {{ opacity:0; transform:translateY(20px); }} 
            to {{ opacity:1; transform:translateY(0); }} 
        }}
    </style>

    <div class="sw-container">
        <div class="sw-header">
            <h2>Linux Knowledge Base</h2>
            <p style="color:#94a3b8;">Search or browse categorized commands.</p>
        </div>

        <div class="sw-search-box">
            <span class="sw-search-icon">🔍</span>
            <input type="text" id="sw-input" class="sw-input" placeholder="Type a command (e.g. tar, top) or keyword..." oninput="swSearch(this.value)">
        </div>

        <div class="sw-filters">
            <button class="sw-cat-btn active" onclick="filterCmds('ALL')">All</button>
            {cats_html}
        </div>

        <div id="sw-results" class="sw-results-area">
            <!-- Results injected by JS -->
        </div>

        <div id="sw-detail" class="sw-detail-panel">
            <h3 id="sw-detail-title" style="margin-top:0; color:#38bdf8; font-family:monospace; font-size:1.5rem;"></h3>
            <span id="sw-detail-cat" style="background:#334155; color:#cbd5e1; padding:2px 8px; border-radius:4px; font-size:0.75rem; text-transform:uppercase;"></span>
            <p id="sw-detail-desc" style="font-size:1.1rem; line-height:1.6; color:#e2e8f0; margin-top:15px;"></p>
        </div>
    </div>

    <script>
        const SW_DATA = {data_js};
        let currentCat = 'ALL';

        function initWidget() {{
            renderGrid('ALL');
        }}

        function filterCmds(cat) {{
            currentCat = cat;
            // Update active btn
            document.querySelectorAll('.sw-cat-btn').forEach(btn => {{
                btn.classList.toggle('active', btn.innerText === (cat === 'ALL' ? 'All' : cat));
            }});
            renderGrid(cat);
        }}

        function swSearch(query) {{
            query = query.toLowerCase();
            renderGrid(currentCat, query);
        }}

        function renderGrid(category, query='') {{
            const container = document.getElementById('sw-results');
            container.innerHTML = '';
            
            // Loop through data
            for (const [catName, cmds] of Object.entries(SW_DATA)) {{
                // If specific category selected, skip others
                if (category !== 'ALL' && category !== catName) continue;

                for (const [cmd, desc] of Object.entries(cmds)) {{
                    // Search filter
                    if (query && !cmd.includes(query) && !desc.toLowerCase().includes(query)) continue;

                    const card = document.createElement('div');
                    card.className = 'sw-cmd-card';
                    card.onclick = () => showDetail(cmd, desc, catName);
                    card.innerHTML = `
                        <div class="sw-cmd-name">${{cmd}}</div>
                        <div class="sw-cmd-desc-short">${{desc}}</div>
                    `;
                    container.appendChild(card);
                }}
            }}
            
            if (container.children.length === 0) {{
                container.innerHTML = '<div style="grid-column:1/-1; text-align:center; color:#64748b; padding:20px;">No matching commands found.</div>';
            }}
        }}

        function showDetail(cmd, desc, cat) {{
            const panel = document.getElementById('sw-detail');
            panel.style.display = 'block';
            document.getElementById('sw-detail-title').innerText = cmd;
            document.getElementById('sw-detail-cat').innerText = cat;
            document.getElementById('sw-detail-desc').innerHTML = desc.replace(/`(.*?)`/g, '<code style="background:#1e293b; padding:2px 6px; border-radius:4px; border:1px solid #475569; color:#facc15;">$1</code>');
            
            // Smooth scroll to detail
            panel.scrollIntoView({{behavior: 'smooth', block: 'nearest'}});
        }}

        // Initialize immediately
        initWidget();
    </script>
    """
