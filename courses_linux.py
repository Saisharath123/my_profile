# courses_linux.py
# Linux Administration module (SSR Edition - Fixes Blank Page Issue)
# Exposes: render() -> HTML string

def render():
    # --- DATA (Server-Side) ---
    # We define the content here in Python to ensure it renders even if <script> execution is blocked.
    topics = [
        {"k": "intro", "t": "Introduction", "i": "ℹ️", "d": "Linux basics, learning goals, and best practices.", 
         "c": "<h3>Introduction to Linux</h3><p><strong>What is Linux:</strong> A family of open-source, UNIX-like operating systems used on servers, desktops, and embedded devices.</p><p><strong>Learning goals:</strong> Become comfortable with the shell, filesystem hierarchy, basic administration tasks, and troubleshooting workflows.</p><p><strong>Best practices:</strong> use non-root accounts, prefer SSH key-based access, keep systems updated, and automate repeatable tasks.</p>"},
        
        {"k": "fs", "t": "Filesystem Basics", "i": "📂", "d": "Hierarchy standard, navigation, and file types.",
         "c": "<h3>Filesystem Hierarchy Standard (FHS)</h3><p>Understand the standard directories:</p><ul><li><code>/</code> (Root): The start of the filesystem.</li><li><code>/etc</code>: Configuration files.</li><li><code>/var</code>: Variable data (logs, websites).</li><li><code>/home</code>: User directories.</li></ul><p><strong>Navigation:</strong></p><pre>pwd       # Print Working Directory\nls -la    # List all files with details\ncd /tmp   # Change directory</pre>"},
        
        {"k": "users", "t": "Users & Groups", "i": "👥", "d": "User management, /etc/passwd, and sudo access.",
         "c": "<h3>User Management</h3><p>Linux is a multi-user system.</p><ul><li><code>/etc/passwd</code>: User info.</li><li><code>/etc/shadow</code>: Encrypted passwords.</li></ul><p><strong>Commands:</strong></p><pre>useradd -m developer   # Create user with home dir\npasswd developer       # Set password\nusermod -aG sudo developer # Grant admin rights</pre>"},
        
        {"k": "perms", "t": "Permissions", "i": "🔒", "d": "Read/Write/Execute bits, chown, and chmod.",
         "c": "<h3>File Permissions</h3><p>Every file has Owner, Group, and Others permissions.</p><p><strong>Modes:</strong> Read (r=4), Write (w=2), Execute (x=1).</p><pre>chmod 755 script.sh    # rwx for owner, rx for others\nchown user:group file  # Change ownership\numask 022              # Default creation mask</pre>"},
        
        {"k": "proc", "t": "Process Mgmt", "i": "⚙️", "d": "PID, top/htop, killing processes, and priority.",
         "c": "<h3>Process Management</h3><p>Every running program is a process with a Process ID (PID).</p><pre>ps aux | grep nginx    # Find process\ntop                    # Real-time monitor\nkill -9 &lt;PID&gt;          # Force kill\nrenice -n -5 -p &lt;PID&gt;  # Increase priority</pre>"},
        
        {"k": "systemd", "t": "Systemd Services", "i": "🚀", "d": "Start/Stop services, enable on boot, logs.",
         "c": "<h3>Systemd</h3><p>The standard init system for most Linux distros.</p><pre>systemctl status sshd\nsystemctl start sshd\nsystemctl enable sshd   # Start on boot\njournalctl -u sshd -f   # Follow service logs</pre>"},
        
        {"k": "pkg", "t": "Package Mgmt", "i": "📦", "d": "APT, YUM/DNF repositories and software installation.",
         "c": "<h3>Package Managers</h3><p><strong>Debian/Ubuntu (APT):</strong></p><pre>apt update\napt install htop git</pre><p><strong>RHEL/CentOS (YUM/DNF):</strong></p><pre>dnf install httpd</pre>"},
        
        {"k": "net", "t": "Networking", "i": "🌐", "d": "IP addressing, routing, ports, and DNS tools.",
         "c": "<h3>Network Configuration</h3><pre>ip addr show      # info about interfaces\nip route show     # routing table\nss -tulpn         # listening ports</pre><p><strong>DNS:</strong> Check <code>/etc/resolv.conf</code>.</p>"},
        
        {"k": "shell", "t": "Shell Scripting", "i": "🐚", "d": "Bash scripting basics, loops, and variables.",
         "c": "<h3>Bash Scripting</h3><p>Automate tasks with scripts.</p><pre>#!/bin/bash\nNAME='World'\necho \"Hello, $NAME!\"\n\n# Loop example\nfor i in {1..5}; do\n  echo \"Count: $i\"\ndone</pre><p>Make executable: <code>chmod +x script.sh</code></p>"},
        
        {"k": "ssh", "t": "SSH & Remote", "i": "🔑", "d": "Secure Shell keys, config hardening, and scp.",
         "c": "<h3>Secure Shell (SSH)</h3><p>Remote administration standard.</p><pre>ssh user@server_ip\nssh -i key.pem user@host</pre><p><strong>Hardening:</strong> Edit <code>/etc/ssh/sshd_config</code> to disable PasswordAuthentication and PermitRootLogin.</p>"},
        
        {"k": "storage", "t": "Storage & LVM", "i": "💾", "d": "Disks, partitions, mkfs, mount, and LVM.",
         "c": "<h3>Storage Management</h3><pre>lsblk         # List block devices\nfdisk /dev/sdb # Partition disk\nmkfs.ext4 /dev/sdb1 # Format\nmount /dev/sdb1 /mnt # Mount</pre><p><strong>LVM:</strong> Flexible volume management (pvcreate, vgcreate, lvcreate).</p>"},
        
        {"k": "logs", "t": "Logs & Audit", "i": "📜", "d": "System logs, journalctl, and log rotation.",
         "c": "<h3>System Logs</h3><p>Primary log locations:</p><ul><li><code>/var/log/syslog</code> (or messages)</li><li><code>/var/log/auth.log</code> (Security/Auth)</li></ul><pre>journalctl -xe    # Error details\ndmesg | tail      # Kernel ring buffer</pre>"},
        
        {"k": "sec", "t": "Security/FW", "i": "🛡️", "d": "Firewalls (UFW/IPTables) and best practices.",
         "c": "<h3>Firewalls</h3><p><strong>UFW (Uncomplicated Firewall):</strong></p><pre>ufw allow 22/tcp\nufw enable</pre><p><strong>IPTables:</strong> Legacy packet filtering.</p><p><strong>Best Practice:</strong> Least privilege principle.</p>"},
        
        {"k": "text", "t": "Text Processing", "i": "📑", "d": "Grep, Sed, Awk, Cut, and processing pipelines.",
         "c": "<h3>Text Tools</h3><pre>grep 'error' /var/log/syslog\nsed 's/foo/bar/g' file.txt   # Replace text\nawk '{print $1}' file.txt    # Print first column\ncat file.txt | sort | uniq -c # Count uniques</pre>"},
        
        {"k": "archive", "t": "Archives", "i": "📚", "d": "Tar, Gzip, Zip, and Rsync for backups.",
         "c": "<h3>Archiving & Backup</h3><pre># Create compressed archive\ntar -czf backup.tar.gz /home/user\n\n# Extract\ntar -xzf backup.tar.gz\n\n# Sync directories\nrsync -avz /source/ /destination/</pre>"},
        
        {"k": "env", "t": "Environment", "i": "🌳", "d": "Variables, PATH, aliases, and .bashrc.",
         "c": "<h3>Environment Variables</h3><pre>env             # List all vars\necho $PATH      # View executable path\nexport APP_ENV=prod  # Set variable</pre><p>Persist changes in <code>~/.bashrc</code>.</p>"},
        
        {"k": "git", "t": "Git Basics", "i": "🌱", "d": "Version control essentials for admins.",
         "c": "<h3>Git for Admins</h3><p>Manage config files with Git.</p><pre>git init\ngit add .\ngit commit -m 'Initial config'\ngit status</pre>"},
        
        {"k": "trouble", "t": "Troubleshooting", "i": "🔧", "d": "Diagnostic workflows and rescue modes.",
         "c": "<h3>Troubleshooting Steps</h3><ol><li>Check status: <code>systemctl status service</code></li><li>Check logs: <code>journalctl -u service</code></li><li>Check resources: <code>top</code>, <code>df -h</code></li><li>Check network: <code>ping</code>, <code>curl</code></li></ol>"},
        
        {"k": "perf", "t": "Performance", "i": "🏎️", "d": "CPU, Memory, and IO bottleneck analysis.",
         "c": "<h3>Performance Tuning</h3><pre>htop          # Interactive process viewer\niostat 1      # Disk I/O stats\nvmstat 1      # System stats\nfree -h       # Memory usage</pre>"},
        
        {"k": "containers", "t": "Containers", "i": "🐳", "d": "Docker, Podman, and image management.",
         "c": "<h3>Docker Basics</h3><pre>docker ps           # List running containers\ndocker images       # List images\ndocker run -d nginx # Run in background\ndocker exec -it &lt;ID&gt; bash # Enter container</pre>"},
        
        {"k": "http", "t": "HTTP Tools", "i": "🌍", "d": "Curl, Wget, and web server diagnostics.",
         "c": "<h3>Web Diagnostics</h3><pre>curl -I https://example.com  # Check headers\nwget https://file.zip        # Download file\ncurl -v https://api.site.com # Verbose debug</pre>"},
        
        {"k": "dns", "t": "DNS Tools", "i": "📡", "d": "Dig, Nslookup, and resolver configuration.",
         "c": "<h3>DNS Lookup</h3><pre>dig google.com +short\nnslookup google.com\ncat /etc/hosts</pre>"},
        
        {"k": "time", "t": "Time & NTP", "i": "⏰", "d": "Timedatectl, zones, and synchronization.",
         "c": "<h3>Time Management</h3><pre>date\ntimedatectl set-timezone UTC\ntimedatectl status</pre>"},
        
        {"k": "regex", "t": "Regex", "i": "🧩", "d": "Regular expressions for grep and sed.",
         "c": "<h3>Regular Expressions</h3><p>Used in grep, sed, vim, etc.</p><ul><li><code>^</code>: Start of line</li><li><code>$</code>: End of line</li><li><code>.</code>: Any char</li><li><code>[0-9]</code>: Range</li></ul>"},

        {"k": "kernel", "t": "Kernel", "i": "🧠", "d": "Modules (lsmod) and uname info.",
         "c": "<h3>Linux Kernel</h3><pre>uname -r    # Kernel version\nlsmod       # List loaded modules\nmodprobe &lt;mod&gt; # Load module</pre>"},
         
         {"k": "editors", "t": "Editors", "i": "📝", "d": "Vim, Nano, and file editing.",
         "c": "<h3>Vim Basics</h3><ul><li><code>i</code>: Insert mode</li><li><code>Esc</code>: Exit mode</li><li><code>:wq</code>: Save and quit</li><li><code>:q!</code>: Quit without saving</li></ul>"},
         
         {"k": "mac", "t": "SELinux/AppArmor", "i": "👮", "d": "Mandatory Access Control security.",
         "c": "<h3>SELinux</h3><pre>getenforce    # Check mode (Enforcing/Permissive)\nsetenforce 0  # Set to Permissive (temp)</pre>"},
         
         {"k": "tools", "t": "FS Tools", "i": "🛠️", "d": "Fsck, resize2fs, and maintenance.",
         "c": "<h3>Filesystem Checks</h3><pre>fsck /dev/sdb1  # Check and repair (unmount first!)\nresize2fs /dev/sdb1 # Resize ext4 fs</pre>"},
         
         {"k": "sysinfo", "t": "System Info", "i": "ℹ️", "d": "Hardware specs and OS release info.",
         "c": "<h3>System Information</h3><pre>cat /etc/os-release  # Distro info\nlscpu                # CPU info\nlsmem                # Memory info</pre>"}
    ]

    # Generate HTML for grid items (Server-Side)
    modules_html = ""
    for m in topics:
        # We store the detailed content in a data-attribute to be read by JS, 
        # avoiding injection issues while keeping initial render fast.
        # We escape quotes in the content just in case.
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
        .linux-hero h1 {{ margin: 0 0 10px 0; font-size: 2.2rem; background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .linux-hero p {{ color: #94a3b8; font-size: 1.1rem; max-width: 700px; margin: 0; }}

        /* Tabs */
        .linux-tabs {{ display: flex; gap: 8px; margin-bottom: 24px; border-bottom: 2px solid #e2e8f0; }}
        .linux-tab-btn {{
            background: transparent; border: none; padding: 12px 20px; font-weight: 600; color: #64748b;
            cursor: pointer; font-size: 1rem; border-bottom: 3px solid transparent; transition: all 0.2s;
        }}
        .linux-tab-btn:hover {{ color: #0284c7; background: #f8fafc; }}
        .linux-tab-btn.active {{ color: #0f172a; border-bottom-color: #0284c7; }}
        
        .linux-view {{ display: none; animation: fadeIn 0.3s ease-out; }}
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

        /* Smart Widget */
        .widget-wrap {{ background: #0f172a; color: #fff; padding: 40px; border-radius: 16px; text-align: center; margin: 0 auto; max-width: 800px; }}
        .cmd-input {{ width: 100%; padding: 16px; margin-top: 20px; border-radius: 8px; border: 2px solid #334155; background: #1e293b; color: #fff; font-family: monospace; font-size: 1.1rem; }}
        .cmd-result {{ margin-top: 20px; padding: 20px; background: #1e293b; border-radius: 8px; text-align: left; min-height: 80px; border: 1px solid #334155; }}

        /* Virtual Lab */
        .term-window {{ background: #1e1e1e; border-radius: 8px; height: 500px; display: flex; flex-direction: column; font-family: monospace; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }}
        .term-bar {{ background: #333; padding: 8px 12px; display: flex; gap: 8px; }}
        .term-dot {{ width: 12px; height: 12px; border-radius: 50%; }}
        .term-body {{ flex: 1; padding: 16px; overflow-y: auto; color: #d4d4d4; }}
        .term-line {{ margin-bottom: 4px; white-space: pre-wrap; }}
        .term-input {{ background: transparent; border: none; color: transparent; width: 1px; caret-color: transparent; }}

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
            <h1>Linux Administration Masterclass</h1>
            <p>Comprehensive resource for mastering the Command Line Interface (CLI) and System Administration.</p>
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
            <div class="widget-wrap">
                <h2 style="margin-top:0; color:#38bdf8;">Smart Command Explainer</h2>
                <p>Type any Linux command to understand what it does (e.g. <code>tar -cxvf</code>).</p>
                <input type="text" id="smart-input" class="cmd-input" placeholder="Enter command..." onkeyup="explainCommand(this.value)">
                <div id="smart-output" class="cmd-result">
                    <em>Explanation will appear here...</em>
                </div>
            </div>
        </div>

        <!-- TAB 3: VIRTUAL LAB -->
        <div id="view-lab" class="linux-view">
            <div class="term-window" onclick="document.getElementById('term-input').focus()">
                <div class="term-bar">
                    <div class="term-dot" style="background:#ff5f56;"></div>
                    <div class="term-dot" style="background:#ffbd2e;"></div>
                    <div class="term-dot" style="background:#27c93f;"></div>
                    <div style="flex:1; text-align:center; color:#888; font-size:0.8rem;">student@linux-vm</div>
                </div>
                <div class="term-body" id="term-output">
                    <div class="term-line">Cloud-with-Sai Virtual Linux Environment v1.0</div>
                    <div class="term-line" style="color:#888;">Type 'help' for available commands.</div>
                    <br>
                    <div style="display:flex;">
                        <span style="color:#4ade80; font-weight:bold; margin-right:8px;">student@linux-vm:</span>
                        <span id="term-path-disp" style="color:#60a5fa; font-weight:bold;">~</span>
                        <span style="margin-right:8px;">$</span>
                        <span id="term-live-text"></span>
                        <span style="width:8px; background:#ccc; animation:blink 1s infinite;"></span>
                    </div>
                </div>
                <input type="text" id="term-input" class="term-input" autocomplete="off" oninput="updateLiveText(this.value)" onkeydown="handleTermKey(event)">
            </div>
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
            
            // Get title from the card that was clicked (bit hacky but robust enough for SSR)
            // Or just map it. For simplicity, we use a mapping or just Show Content.
            document.getElementById('modal-title').innerText = "Module Content"; 
            document.getElementById('modal-content').innerHTML = txt.value;
            document.getElementById('linux-modal').style.display = 'flex';
        }}
        
        function closeLinuxModal(e) {{
            if (e && !e.target.classList.contains('overlay')) return;
            document.getElementById('linux-modal').style.display = 'none';
        }}

        // --- Smart Widget Logic ---
        function explainCommand(val) {{
            val = val.trim();
            const out = document.getElementById('smart-output');
            if(!val) {{ out.innerHTML = "<em>Explanation will appear here...</em>"; return; }}
            
            const base = val.split(' ')[0];
            const map = {{
                "ls": "List directory contents.",
                "cd": "Change directory.",
                "pwd": "Print Working Directory.",
                "mkdir": "Make Directory.",
                "rm": "Remove files/directories.",
                "tar": "Tape Archiver - used for backups.",
                "grep": "Global Regular Expression Print - search text.",
                "chmod": "Change Mode - file permissions.",
                "chown": "Change Owner.",
                "ssh": "Secure Shell - remote login.",
                "systemctl": "Control systemd services.",
                "ip": "Show/manipulate routing, network devices, interfaces and tunnels.",
                "apt": "Debian/Ubuntu package manager.",
                "yum": "RHEL/CentOS package manager.",
                "docker": "Container management.",
                "cat": "Concatenate and display file content."
            }};
            
            let desc = map[base] || "A generic Linux command. Check the man page (man " + base + ").";
            if(val.includes('-')) desc += " <br><small>Flags detected.</small>";
            
            out.innerHTML = "<h3 style='margin:0 0 10px 0; color:#38bdf8;'>" + base + "</h3>" + desc;
        }}

        // --- Virtual Lab Logic ---
        function updateLiveText(val) {{
            document.getElementById('term-live-text').innerText = val;
        }}
        
        let termPath = ["~"];
        function handleTermKey(e) {{
            if(e.key === 'Enter') {{
                const input = document.getElementById('term-input');
                const output = document.getElementById('term-output');
                const val = input.value.trim();
                
                // Echo
                const div = document.createElement('div');
                div.innerHTML = '<span style="color:#4ade80;">student@linux-vm:</span><span style="color:#60a5fa;">' + termPath.join('/') + '</span>$ ' + val;
                output.insertBefore(div, output.lastElementChild.previousElementSibling);
                
                // Process
                let resp = "";
                const parts = val.split(' ');
                const cmd = parts[0];
                
                if(cmd === 'ls') resp = "Documents  Downloads  scripts  notes.txt";
                else if(cmd === 'pwd') resp = "/home/student/" + termPath.slice(1).join('/');
                else if(cmd === 'whoami') resp = "student";
                else if(cmd === 'clear') {{
                     // clear logic
                }}
                else if(cmd === 'cd') {{
                    if(parts[1] && parts[1] !== '..') termPath.push(parts[1]);
                    else if(parts[1] === '..') termPath.pop();
                    if(termPath.length < 1) termPath = ["~"];
                    document.getElementById('term-path-disp').innerText = termPath.join('/');
                }}
                else if(cmd) resp = "bash: " + cmd + ": command not found";
                
                if(resp) {{
                    const rDiv = document.createElement('div');
                    rDiv.className = 'term-line';
                    rDiv.innerText = resp;
                    output.insertBefore(rDiv, output.lastElementChild.previousElementSibling);
                }}
                
                input.value = "";
                document.getElementById('term-live-text').innerText = "";
                output.scrollTop = output.scrollHeight;
            }}
        }}
    </script>
    """
