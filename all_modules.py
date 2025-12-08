# all_modules.py
# Backend content for Linux Modules

LINUX_TOPICS = [
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
     "c": "<h3>Regular Expressions</h3><p>Used in grep, sed, vim, etc.</p><ul><li><code>^</code>: Start of line</li><li><code>$</code>: End of line</li><li><code>.</code>: Any char</li><li><code>[0-9]</code>: Range</li><li><code>*</code>: Zero or more</li></ul>"},

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
