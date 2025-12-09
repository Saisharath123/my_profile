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
        .sw-container {{
            background: #1e293b;
            border-radius: 16px;
            padding: 30px;
            color: #fff;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border: 1px solid #334155;
            max-width: 900px;
            margin: 0 auto;
        }}
        .sw-header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .sw-header h2 {{
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            font-size: 2rem;
        }}
        .sw-search-box {{
            position: relative;
            margin-bottom: 20px;
        }}
        .sw-input {{
            width: 100%;
            padding: 18px 24px;
            padding-left: 50px;
            border-radius: 12px;
            border: 2px solid #475569;
            background: #0f172a;
            color: #fff;
            font-size: 1.1rem;
            font-family: monospace;
            transition: border-color 0.2s;
        }}
        .sw-input:focus {{ outline: none; border-color: #38bdf8; }}
        
        .sw-search-icon {{
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
        }}

        .sw-filters {{
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding-bottom: 10px;
            margin-bottom: 20px;
            scrollbar-width: thin;
        }}
        .sw-cat-btn {{
            background: #334155;
            border: none;
            color: #cbd5e1;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            white-space: nowrap;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .sw-cat-btn:hover, .sw-cat-btn.active {{
            background: #38bdf8;
            color: #0f172a;
            font-weight: 600;
        }}

        .sw-results-area {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
            gap: 12px;
            max-height: 400px;
            overflow-y: auto;
            padding-right: 5px;
        }}
        
        .sw-cmd-card {{
            background: #334155;
            padding: 12px;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.1s, background 0.1s;
            text-align: center;
            border: 1px solid transparent;
        }}
        .sw-cmd-card:hover {{
            background: #475569;
            transform: translateY(-2px);
            border-color: #38bdf8;
        }}
        .sw-cmd-name {{
            font-family: 'Courier New', monospace;
            font-weight: 700;
            color: #38bdf8;
            font-size: 1.1rem;
        }}
        .sw-cmd-desc-short {{
            font-size: 0.75rem;
            color: #94a3b8;
            margin-top: 4px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        .sw-detail-panel {{
            margin-top: 30px;
            background: #0f172a;
            border: 1px solid #38bdf8;
            border-radius: 12px;
            padding: 24px;
            display: none; /* hidden by default */
            animation: slideDown 0.3s ease-out;
        }}
        @keyframes slideDown {{ from {{ opacity:0; transform:translateY(-10px); }} to {{ opacity:1; transform:translateY(0); }} }}

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
