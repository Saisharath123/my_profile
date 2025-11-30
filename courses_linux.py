# courses_linux.py
# Linux Administration module for integration with courses_module.py
# Exposes:
#   - render() -> str (HTML inner content)
#   - render_service(service_id) -> str (placeholder)
#
# Important: THIS FILE MUST NOT DEFINE @app.route handlers.
# Your courses_module.py should import this and call render().

def render():
    # Return inner HTML only (no <html>/<body> wrapper) so the host app keeps chrome intact.
    return r'''
    <style>
      :root { box-sizing: border-box; }
      *, *::before, *::after { box-sizing: inherit; }

      /* Ensure hero doesn't collide with header - base template defines --nav-height */
      .linux-hero {
        border-radius:18px;
        overflow:hidden;
        color:#fff;
        background:radial-gradient(circle at 12% 0%, rgba(148,163,184,0.45), transparent 55%),
                   linear-gradient(135deg,#020617,#0b3b6f);
        padding:22px;
        margin-top: 6px;
        position: relative;
        z-index: 1;
        border:1px solid rgba(148,163,184,0.32);
        box-shadow:
          0 22px 44px rgba(15,23,42,0.75),
          0 0 0 1px rgba(15,23,42,0.85) inset;
      }
      .linux-hero .hero-inner {
        display:flex;
        gap:18px;
        align-items:flex-start;
        flex-wrap:wrap;
      }
      .linux-hero h1 { font-weight:800; margin:0 0 6px 0; font-size:1.6rem; }
      .linux-hero p.lead { margin:0; color:rgba(255,255,255,0.88); font-weight:700; }

      /* Sticky TOC offset respects header height (default fallback 110px) */
      .toc-sticky { position:sticky; top: calc(var(--nav-height, 110px) + 12px); }

      /* Widget/card visuals (3D base) */
      .widget {
        border-radius:16px;
        border:1px solid rgba(15,23,42,0.55);
        background:
          radial-gradient(circle at 15% 0%, rgba(248,250,252,0.09), transparent 55%),
          linear-gradient(180deg, rgba(15,23,42,0.96), rgba(15,23,42,0.88));
        box-shadow:
          0 20px 40px rgba(15,23,42,0.85),
          0 0 0 1px rgba(15,23,42,0.75),
          0 0 24px rgba(37,99,235,0.32);
        overflow:hidden;
        transform-style: preserve-3d;
      }
      .hero-widget {
        max-width:860px;
        padding:14px;
        border-radius:18px;
        position:relative;
      }
      .hero-widget::before {
        content:"";
        position:absolute;
        inset:0;
        border-radius:18px;
        background: linear-gradient(135deg,rgba(96,165,250,0.5),rgba(56,189,248,0.2),rgba(45,212,191,0.1));
        mix-blend-mode: screen;
        opacity:0.28;
        pointer-events:none;
      }
      .hero-widget .row { display:flex; gap:8px; align-items:center; flex-wrap:wrap; }
      .hero-widget .label { color: #fff; font-weight:800; text-shadow:0 1px 4px rgba(15,23,42,0.9); }
      .hero-widget .desc { color: rgba(226,232,240,0.96); font-weight:600; font-size:0.93rem; }

      /* Input styles (no bootstrap dependency) */
      .input-group { display:flex; gap:8px; margin-top:10px; }
      .input-group .icon {
        display:inline-flex; align-items:center; justify-content:center;
        width:44px; height:44px; border-radius:10px;
        background: radial-gradient(circle at 30% 0%, rgba(248,250,252,0.9), rgba(15,23,42,0.9));
        color:#0b1f3b; font-weight:800;
        box-shadow:
          0 6px 16px rgba(15,23,42,0.85),
          0 0 0 1px rgba(15,23,42,0.8);
      }
      .input-group input[type="text"], .input-group input[type="search"] {
        flex:1; padding:10px 12px; border-radius:10px; border: none;
        background: radial-gradient(circle at 0% 0%, rgba(255,255,255,0.22), rgba(15,23,42,0.95));
        color:#e5e7eb; font-weight:700;
        outline: none; min-width:160px;
        box-shadow: inset 0 0 0 1px rgba(148,163,184,0.45);
      }
      .input-group button {
        padding:10px 14px; border-radius:10px; border:none; cursor:pointer;
        background: linear-gradient(120deg,#22c55e,#22c55e,#38bdf8,#6366f1);
        background-size: 220% 220%;
        color:#020617; font-weight:800;
        box-shadow:
          0 6px 18px rgba(22,163,74,0.85),
          0 0 0 1px rgba(22,163,74,0.85);
        transform:translateZ(0);
        transition: transform 0.14s ease, box-shadow 0.14s ease, background-position 0.3s ease;
      }
      .input-group button:hover {
        transform: translateY(-1px);
        background-position: 100% 0%;
        box-shadow:
          0 10px 26px rgba(22,163,74,0.9),
          0 0 0 1px rgba(22,163,74,0.9);
      }
      .input-group button:active {
        transform: translateY(1px);
        box-shadow:
          0 4px 12px rgba(22,163,74,0.8),
          0 0 0 1px rgba(22,163,74,0.9);
      }

      /* Result box - white so content readable */
      .cmd-result {
        margin-top:12px;
        padding:12px;
        border-radius:10px;
        background: radial-gradient(circle at 0% 0%, #ffffff, #e5e7eb);
        color:#0b1620;
        min-height:92px;
        box-shadow:
          0 14px 30px rgba(15,23,42,0.35),
          0 0 0 1px rgba(148,163,184,0.8);
        overflow:auto;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      }
      .cmd-result .badge {
        display:inline-block; padding:4px 8px; border-radius:999px;
        background:linear-gradient(135deg,#e0f2fe,#e5e7eb);
        font-weight:800; margin-right:8px;
        box-shadow:0 1px 3px rgba(15,23,42,0.35);
      }

      /* Layout grid */
      .linux-grid { display:grid; grid-template-columns: 320px 1fr; gap:22px; align-items:start; margin-top:18px; }
      @media (max-width:980px) { .linux-grid { grid-template-columns: 1fr; } .toc-sticky { position: static; } }

      /* TOC list */
      .list-group { display:flex; flex-direction:column; gap:4px; }
      .list-group a {
        display:block; padding:10px 12px; border-radius:10px; text-decoration:none;
        color:#0b1720; background:linear-gradient(180deg,#f9fafb,#e5e7eb);
        border:1px solid rgba(148,163,184,0.85); font-weight:700;
        transition: transform .14s cubic-bezier(.2,.8,.2,1), box-shadow .14s, background .14s;
        transform-origin: left center;
        will-change: transform, box-shadow;
        box-shadow:
          0 4px 9px rgba(15,23,42,0.25),
          0 0 0 1px rgba(148,163,184,0.65);
      }
      .list-group a:hover, .list-group a:focus {
        transform: translateY(-2px);
        box-shadow:
          0 8px 18px rgba(15,23,42,0.35),
          0 0 0 1px rgba(59,130,246,0.9);
        outline: none;
        background:linear-gradient(180deg,#eff6ff,#dbeafe);
      }
      .list-group a.active {
        background: linear-gradient(120deg,#2563eb,#22c55e);
        color:#f9fafb;
        border-color: rgba(37,99,235,0.95);
        box-shadow:
          0 10px 24px rgba(37,99,235,0.6),
          0 0 0 1px rgba(15,23,42,0.8);
        transform: none;
      }
      @media (prefers-reduced-motion: reduce) {
        .list-group a, .list-group a:hover, .list-group a:focus { transition: none; transform: none; }
      }

      /* Section headers: thicker, 3D blue bar for topic titles */
      .section-card .card-header {
        display:flex;
        align-items:center;
        gap:8px;
        color:#f9fafb;
        background: linear-gradient(135deg,#1d4ed8,#2563eb);
        padding:14px 18px;
        border:none;
        border-radius:14px 14px 0 0;
        box-shadow:
          0 3px 0 rgba(15,23,42,0.55),
          0 10px 18px rgba(15,23,42,0.45),
          0 0 0 1px rgba(15,23,42,0.9);
        letter-spacing:0.03em;
        line-height:1.3;
        overflow:visible;
        text-shadow:0 1px 3px rgba(15,23,42,0.9);
      }

      /* Header blink/pulse animation for section titles */
      @keyframes headlinePulse {
        0%   { filter: none; text-shadow: 0 1px 3px rgba(15,23,42,0.9); }
        50%  { filter: brightness(1.08); text-shadow: 0 1px 6px rgba(191,219,254,1); }
        100% { filter: none; text-shadow: 0 1px 3px rgba(15,23,42,0.9); }
      }
      .pulse-headline {
        animation-name: headlinePulse;
        animation-duration: 0.6s;
        animation-timing-function: ease-in-out;
        animation-iteration-count: 2;
        animation-fill-mode: none;
      }

      /* Typing animation for card-body content: characters are revealed one-by-one */
      .typing-char {
        display:inline-block;
        opacity:0;
        transform: translateY(6px);
        transition: opacity 80ms linear, transform 80ms linear;
        white-space: pre-wrap;
      }
      .typing-char.reveal {
        opacity:1;
        transform: none;
      }
      .section-card pre, .section-card code { white-space: pre-wrap; }

      /* Section cards themselves: 3D modules */
      .section-card {
        border-radius:14px;
        overflow:hidden;
        border:1px solid rgba(15,23,42,0.7);
        background: radial-gradient(circle at 0% 0%, #ffffff, #eef2ff);
        box-shadow:
          0 16px 32px rgba(15,23,42,0.32),
          0 0 0 1px rgba(148,163,184,0.85);
        padding:0;
        transform-style: preserve-3d;
        transform: translateZ(0);
        transition: transform 0.16s ease, box-shadow 0.16s ease;
      }
      .section-card .card-body {
        padding:14px;
        color:#374151;
        font-weight:700;
        line-height:1.45;
      }
      .section-card:hover {
        transform: translateY(-4px);
        box-shadow:
          0 22px 40px rgba(15,23,42,0.45),
          0 0 0 1px rgba(59,130,246,0.9);
      }

      /* small utilities */
      .cmd-chip {
        display:inline-block;
        padding:.2rem .5rem;
        border:1px solid rgba(148,163,184,0.9);
        border-radius:999px;
        font-family: ui-monospace, monospace;
        background:linear-gradient(135deg,#f9fafb,#e5e7eb);
        color:#0b1620;
        font-weight:700;
        margin-right:6px;
        box-shadow:0 2px 4px rgba(15,23,42,0.25);
      }
      pre {
        background:#020617;
        color:#e5e7eb;
        padding:12px;
        border-radius:10px;
        overflow:auto;
        white-space:pre-wrap;
        font-size:0.92rem;
        line-height:1.4;
        border-left:4px solid rgba(59,130,246,0.85);
        box-shadow: inset 0 0 0 1px rgba(15,23,42,0.85);
      }
      .pre-copy {
        position:absolute;
        right:12px; top:12px;
        padding:6px 8px;
        border-radius:999px;
        border:none; cursor:pointer;
        background: radial-gradient(circle at 0% 0%, rgba(248,250,252,0.9), rgba(30,64,175,0.9));
        color:#020617; font-weight:700;
        box-shadow:
          0 4px 10px rgba(15,23,42,0.85),
          0 0 0 1px rgba(15,23,42,0.8);
      }
      .hit { animation: flash 1.4s ease 1; }
      @keyframes flash {
        0%   { box-shadow:0 0 0 0 rgba(59,130,246,0); }
        20%  { box-shadow:0 0 0 8px rgba(37,99,235,.28); }
        100% { box-shadow:0 0 0 0 rgba(37,99,235,0); }
      }

      .linux-hero h1 { font-size:1.75rem; letter-spacing:-0.4px; }
      .section-card .card-header { font-size:1.05rem; }
      .section-card .card-body { font-size:0.98rem; }

      #progressBar {
        position: fixed; left:0; top: calc(var(--nav-height, 72px) + 0px);
        height: 3px; width:0%; background: linear-gradient(90deg,#60A5FA,#6EE7B7);
        z-index: 9999; transition: width 100ms linear;
      }

      :focus { outline: none; }
      a:focus, button:focus, input:focus {
        outline: none;
        box-shadow: 0 0 0 4px rgba(96,165,250,0.18);
        border-radius: 8px;
      }

      @media (prefers-reduced-motion: reduce) {
        .typing-char, .pulse-headline, .list-group a, .section-card {
          animation: none !important;
          transition: none !important;
          transform: none !important;
        }
      }

      /* Rocket Scroll-to-Top Widget (3D rocket) */
      .heli-btn {
        position: fixed;
        bottom: 24px;
        right: 24px;
        border: none;
        padding: 0;
        margin: 0;
        background: transparent;
        cursor: pointer;
        z-index: 9999;
        display: none;
      }
      .heli-btn.show { display: block; }
      .heli-btn:focus { outline: none; }

      .heli-btn::before {
        content:"";
        position:absolute;
        inset:auto 4px 0 4px;
        height:10px;
        border-radius:999px;
        background: radial-gradient(circle at 50% 0%, rgba(15,23,42,0.6), transparent 70%);
        filter: blur(2px);
        opacity:0.95;
        pointer-events:none;
      }

      .heli {
        position: relative;
        width: 50px;
        height: 70px;
        transform-origin: center;
        animation: heli-float 2.4s ease-in-out infinite;
        filter: drop-shadow(0 12px 22px rgba(15,23,42,0.9));
      }

      .heli-body {
        position: absolute;
        bottom: 14px;
        left: 50%;
        transform: translateX(-50%);
        width: 22px;
        height: 42px;
        border-radius: 12px 12px 6px 6px;
        background:
          radial-gradient(circle at 30% 0%, #e0f2fe, #60a5fa),
          linear-gradient(180deg, #60A5FA, #1D4ED8);
        box-shadow:
          0 8px 14px rgba(15,23,42,0.9),
          0 0 0 1px rgba(30,64,175,0.9);
      }

      .heli-body::before {
        content: "";
        position: absolute;
        top: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 11px solid transparent;
        border-right: 11px solid transparent;
        border-bottom: 12px solid #1D4ED8;
        filter: drop-shadow(0 3px 4px rgba(15,23,42,0.9));
      }

      .heli-window {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #ffffff, #dbeafe);
        box-shadow:
          0 0 6px rgba(248,250,252,0.9),
          0 0 0 2px rgba(15,23,42,0.9);
      }

      .heli-tail {
        position: absolute;
        bottom: 14px;
        left: 50%;
        transform: translateX(-50%);
        width: 30px;
        height: 14px;
      }
      .heli-tail::before,
      .heli-tail::after {
        content: "";
        position: absolute;
        bottom: 0;
        width: 14px;
        height: 14px;
        background: linear-gradient(180deg,#F97316,#EA580C);
        box-shadow:
          0 4px 8px rgba(15,23,42,0.9),
          0 0 0 1px rgba(124,45,18,0.95);
      }
      .heli-tail::before {
        right: 50%;
        transform-origin: top right;
        transform: skewX(-20deg);
        border-bottom-left-radius: 10px;
      }
      .heli-tail::after {
        left: 50%;
        transform-origin: top left;
        transform: skewX(20deg);
        border-bottom-right-radius: 10px;
      }

      .heli-tail-rotor {
        position: absolute;
        bottom: 22px;
        left: 50%;
        transform: translateX(-50%);
        width: 4px;
        height: 4px;
        border-radius: 50%;
        background: rgba(15,23,42,0.65);
        box-shadow:0 1px 2px rgba(15,23,42,0.9);
      }

      .heli-rotor {
        position: absolute;
        bottom: -12px;
        left: 50%;
        transform: translateX(-50%);
        height: 18px;
        display: flex;
        justify-content: center;
        align-items: flex-start;
      }

      .heli-rotor-blade {
        width: 12px;
        height: 18px;
        border-radius: 50% 50% 60% 60%;
        background: radial-gradient(circle at 30% 0%, #FEF9C3, #FBBF24, #F97316, #B91C1C);
        box-shadow:
          0 0 7px rgba(251,191,36,1),
          0 0 16px rgba(248,113,113,0.9);
        animation: rotor-spin 0.28s ease-in-out infinite alternate;
        transform-origin: top center;
      }

      .heli-skids { display:none; }

      @keyframes rotor-spin {
        0%   { transform: scaleY(0.8) translateY(1px); opacity: 0.9; }
        50%  { transform: scaleY(1.15) translateY(-2px); opacity: 1; }
        100% { transform: scaleY(0.7) translateY(3px); opacity: 0.75; }
      }
      @keyframes heli-float {
        0%   { transform: translateY(0); }
        50%  { transform: translateY(-5px); }
        100% { transform: translateY(0); }
      }

      .heli-btn:hover .heli {
        transform: translateY(-4px);
      }
    </style>

    <!-- Progress bar element removed so the blue line no longer appears -->

    <div class="linux-hero" role="region" aria-label="Linux hero">
      <div class="hero-inner">
        <div style="flex:1;min-width:180px;">
          <h1>Linux Administration</h1>
          <p class="lead">The Single Platform to Learn Linux Administration • <strong>Smart Command Widget</strong> above • Topics below.</p>
        </div>

        <div style="flex:0 0 420px;">
          <div class="widget hero-widget" role="region" aria-label="Linux command widget">
            <div class="row">
              <div style="flex:1;min-width:180px;">
                <div class="label">Linux Command Knowledge Widget</div>
                <div class="desc">Type a Linux command (or small snippet) and press <strong>Run</strong> — explanation only.</div>
              </div>
            </div>

            <div class="input-group" style="margin-top:10px;">
              <div class="icon" aria-hidden="true">⌘</div>
              <input id="cmdInput" type="search" placeholder="e.g., ls -la /var/log or systemctl status ssh" aria-label="Linux command input">
              <button id="btnRun" type="button" aria-label="Run command">Run ▶</button>
            </div>

            <div style="font-size:0.82rem; color: rgba(255,255,255,0.75); margin-top:8px;">Try commands like <code>ls -la /var/log</code> or <code>systemctl status ssh</code></div>

            <div id="cmdResult" class="cmd-result" role="status" aria-live="polite">
              <div style="color:#6b7280;font-weight:700;">Type a command and press <strong>Run</strong>. This is a safe explain-only sandbox — nothing runs on server.</div>
            </div>

          </div>
        </div>
      </div>
    </div>

    <div class="linux-grid" role="main" aria-label="Linux content grid">
      <aside class="toc-sticky" aria-label="Linux table of contents">
        <nav class="list-group" id="linuxToc">
          <a class="active" href="#intro">Introduction</a>
          <a href="#fs">Filesystem Basics</a>
          <a href="#users">Users & Groups</a>
          <a href="#perms">Permissions & Ownership</a>
          <a href="#proc">Processes & Services</a>
          <a href="#pkg">Package Management</a>
          <a href="#net">Networking</a>
          <a href="#storage">Disks, Partitions & LVM</a>
          <a href="#systemd">Boot & systemd</a>
          <a href="#logs">Logs & Monitoring</a>
          <a href="#shell">Shell Scripting & Cron</a>
          <a href="#sec">Security & Firewalls</a>
          <a href="#mac">SELinux / AppArmor</a>
          <a href="#ssh">SSH & Remote Access</a>
          <a href="#kernel">Kernel & Modules</a>
          <a href="#containers">Containers</a>
          <a href="#trouble">Troubleshooting & Rescue</a>
          <a href="#perf">Performance Tuning</a>
          <a href="#tools">Filesystem Tools</a>
          <a href="#editors">Editors (vim/nano)</a>
          <a href="#archive">Archives & Compression</a>
          <a href="#text">Text Processing</a>
          <a href="#regex">Regular Expressions</a>
          <a href="#env">Environment & Dotfiles</a>
          <a href="#git">Git Basics</a>
          <a href="#sysinfo">System Info & Hardware</a>
          <a href="#time">Time & NTP/chrony</a>
          <a href="#dns">DNS Tools</a>
          <a href="#http">HTTP Tools</a>
        </nav>
      </aside>

      <section>
        <div id="intro" class="section-card" style="margin-bottom:14px;">
          <div class="card-header"><i aria-hidden="true">ℹ️</i> Introduction</div>
          <div class="card-body">
            <p><strong>What is Linux:</strong> A family of open-source, UNIX-like operating systems used on servers, desktops, and embedded devices.</p>
            <p><strong>Learning goals:</strong> Become comfortable with the shell, filesystem hierarchy, basic administration tasks, and troubleshooting workflows.</p>
            <p><strong>Key concepts:</strong> processes, users, permissions, services (systemd), package managers, networking, and storage.</p>
            <p><strong>Best practices:</strong> use non-root accounts, prefer SSH key-based access, keep systems updated, and automate repeatable tasks.</p>
          </div>
        </div>

        <div id="fs" class="section-card" style="margin-bottom:14px;">
          <div class="card-header">Filesystem Basics</div>
          <div class="card-body">
            <p><strong>Filesystem tree:</strong> Understand standard directories (/, /etc, /var, /usr, /home, /tmp) and their purposes.</p>
            <p><strong>Navigation & inspection:</strong> use <code>ls, pwd, cd, tree</code> to explore; learn file metadata via <code>stat</code>.</p>
            <p><strong>Mounts:</strong> difference between device nodes and mount points; check mounts with <code>mount</code> and <code>findmnt</code>.</p>
            <p><strong>Persistence:</strong> fstab entries for persistent mounts and using UUIDs or labels for reliability.</p>
            <pre>ls -la  # list with details
pwd    # print working dir
cd /etc; tree -L 1</pre>
          </div>
        </div>

        <div id="users" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Users & Groups</div>
          <div class="card-body">
            <p><strong>User accounts:</strong> system vs human users; UID ranges; /etc/passwd and /etc/shadow basics.</p>
            <p><strong>Groups:</strong> primary vs supplementary groups; use <code>getent group</code> to inspect.</p>
            <p><strong>Account management:</strong> create users with home dirs, set passwords, lock/unlock accounts, and expire credentials.</p>
            <p><strong>Privileges:</strong> control sudo access and minimize granting full root where possible.</p>
            <pre>id
useradd -m dev; passwd dev
usermod -aG sudo dev
getent group sudo</pre>
          </div>
        </div>

        <div id="perms" class="section-card" style="margin-bottom:14px;">
          <div class="card-header">Permissions & Ownership</div>
          <div class="card-body">
            <p><strong>POSIX permissions:</strong> read/write/execute for user/group/others; numeric and symbolic modes.</p>
            <p><strong>Ownership:</strong> change owner/group with <code>chown</code> and adjust default file creation mask with <code>umask</code>.</p>
            <p><strong>ACLs:</strong> when POSIX bits aren't enough, use <code>setfacl/getfacl</code> for fine-grained access control.</p>
            <p><strong>Sticky bits & special bits:</strong> setgid on directories for shared projects, sticky bit on /tmp.</p>
            <pre>chmod 640 file
chown user:group file
umask 027
setfacl -m u:dev:rwx project</pre>
          </div>
        </div>

        <div id="proc" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Processes & Services</div>
          <div class="card-body">
            <p><strong>Processes:</strong> inspect running processes with <code>ps</code>, monitor with <code>top</code>/<code>htop</code>, and use <code>nice</code>/<code>renice</code> for priority.</p>
            <p><strong>Signals:</strong> use <code>kill</code> and <code>kill -9</code> appropriately; understand common signals (TERM, KILL, HUP).</p>
            <p><strong>Services (systemd):</strong> start/stop/enable services, check status, and read unit files to understand dependencies.</p>
            <p><strong>Background jobs:</strong> job control with <code>&amp;</code>, <code>fg</code>, <code>bg</code>, and <code>jobs</code>.</p>
            <pre>ps aux | head
top
systemctl status nginx
systemctl enable --now nginx</pre>
          </div>
        </div>

        <div id="pkg" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Package Management</div>
          <div class="card-body">
            <p><strong>Distributions & package systems:</strong> apt (Debian/Ubuntu), dnf/yum/rpm (RHEL/CentOS/Fedora), zypper, apk (Alpine).</p>
            <p><strong>Updates & security:</strong> keep systems patched, configure unattended-upgrades or repositories with tested packages for production.</p>
            <p><strong>Local packages:</strong> install from local files, pin versions, rollback where supported, and verify signatures when possible.</p>
            <pre>apt update && apt install -y htop
yum install -y httpd
apt-cache policy nginx</pre>
          </div>
        </div>

        <div id="net" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Networking</div>
          <div class="card-body">
            <p><strong>Interfaces & addresses:</strong> use <code>ip a</code> and <code>ip addr</code> to inspect IPs; understand link vs IP states.</p>
            <p><strong>Routing & connectivity:</strong> check routes with <code>ip r</code>, test with <code>ping</code> and <code>traceroute</code>.</p>
            <p><strong>Listening services:</strong> use <code>ss</code> or <code>netstat</code> to see listening sockets and associated processes.</p>
            <p><strong>Name resolution:</strong> /etc/resolv.conf, /etc/hosts, and debugging with <code>dig</code> / <code>nslookup</code>.</p>
            <pre>ip a
ip r
ss -lntp
ping -c 3 8.8.8.8</pre>
          </div>
        </div>

        <div id="storage" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Disks, Partitions & LVM</div>
          <div class="card-body">
            <p><strong>Device discovery:</strong> list disks with <code>lsblk</code>, partition tables with <code>fdisk -l</code>.</p>
            <p><strong>Filesystems:</strong> format with mkfs variants, consider ext4, xfs, btrfs depending on needs and tooling.</p>
            <p><strong>LVM basics:</strong> pvcreate, vgcreate, lvcreate for flexible volume management and snapshots.</p>
            <p><strong>Mounting & fstab:</strong> ensure correct mount options (rw,noatime), use UUIDs, and test entries before reboot.</p>
            <pre>lsblk
fdisk -l
pvcreate /dev/xvdf; vgcreate vg0 /dev/xvdf; lvcreate -n data -L 10G vg0
mkfs.ext4 /dev/vg0/data && mount /dev/vg0/data /data</pre>
          </div>
        </div>

        <div id="systemd" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Boot & systemd</div>
          <div class="card-body">
            <p><strong>Boot process:</strong> BIOS/UEFI → bootloader (GRUB) → kernel → init/systemd. Know how to recover from boot failures.</p>
            <p><strong>Systemd units:</strong> service, socket, target, timer units — inspect unit files and journal logs for diagnostics.</p>
            <p><strong>Runlevels/targets:</strong> multi-user.target vs graphical.target; change default with <code>systemctl set-default</code>.</p>
            <p><strong>Emergency recovery:</strong> using rescue.target, single-user mode, or initramfs troubleshooting.</p>
            <pre>systemctl list-units --type=service
systemctl get-default
journalctl -b -1</pre>
          </div>
        </div>

        <div id="logs" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Logs & Monitoring</div>
          <div class="card-body">
            <p><strong>System journal:</strong> central logging with <code>journalctl</code> — filter by unit, boot ID, or time range.</p>
            <p><strong>Log files:</strong> classic files under /var/log (syslog, auth.log, kern.log) — rotate logs with logrotate.</p>
            <p><strong>Monitoring basics:</strong> use vmstat, iostat, top, and consider Prometheus/node_exporter for metrics in production.</p>
            <p><strong>Alerting & retention:</strong> set sensible retention and alert thresholds; aggregate logs to a central server where feasible.</p>
            <pre>journalctl -u ssh --since "1 hour ago"
dmesg | tail
vmstat 1</pre>
          </div>
        </div>

        <div id="shell" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Shell Scripting & Cron</div>
          <div class="card-body">
            <p><strong>Scripting fundamentals:</strong> write idempotent scripts, use set -euo pipefail, and comment inputs/outputs for maintainability.</p>
            <p><strong>Common tasks:</strong> parsing files with grep/sed/awk, looping over items, argument parsing with getopts, and using functions.</p>
            <p><strong>Scheduling:</strong> crontab syntax, systemd timers as an alternative, and safe practices for scheduled jobs (logging, locking, retries).</p>
            <p><strong>Testing & deployment:</strong> test scripts locally, run under the service account they'll execute as, and avoid storing secrets in plaintext.</p>
            <pre>crontab -e
for f in *.log; do echo "$f"; done
$(date +%F)</pre>
          </div>
        </div>

        <div id="sec" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Security & Firewalls</div>
          <div class="card-body">
            <p><strong>Principle of least privilege:</strong> grant only the permissions needed, prefer role-based access and minimal sudoers entries.</p>
            <p><strong>Authentication:</strong> prefer SSH keys, disable password authentication for remote access when possible, and use MFA for console access.</p>
            <p><strong>Host-based firewalls:</strong> ufw for simple setups, iptables/nftables for advanced rules, firewalld for dynamic management on RHEL families.</p>
            <p><strong>Hardening:</strong> disable unused services, secure shared directories, remove unnecessary packages, and keep packages patched.</p>
            <p><strong>Intrusion detection:</strong> consider tools like fail2ban, auditd, AIDE for file integrity, and centralize logs to detect anomalies.</p>
            <pre>ufw allow OpenSSH && ufw enable
iptables -L -n
firewall-cmd --add-service=http --permanent && firewall-cmd --reload</pre>
          </div>
        </div>

        <div id="mac" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">SELinux / AppArmor</div>
          <div class="card-body">
            <p><strong>Mandatory access control (MAC):</strong> SELinux (RHEL/Fedora/CentOS) and AppArmor (Ubuntu) provide fine-grained policy enforcement beyond POSIX permissions.</p>
            <p><strong>Modes:</strong> Enforcing (deny & log), Permissive (log only), and Disabled. Use permissive mode for debugging policy issues before enforcing.</p>
            <p><strong>Troubleshooting:</strong> use <code>audit2why</code>, <code>audit2allow</code> (SELinux) and <code>aa-status</code>, <code>aa-complain</code> (AppArmor) to diagnose & adjust policies.</p>
            <p><strong>Best practices:</strong> prefer targeted policies over permissive global rules, test policy changes in staging, and avoid disabling MAC in production unless unavoidable.</p>
            <pre>getenforce
setenforce 0  # temp permissive
aa-status</pre>
          </div>
        </div>

        <div id="ssh" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">SSH & Remote Access</div>
          <div class="card-body">
            <p><strong>Keys over passwords:</strong> generate SSH key pairs, protect private keys with passphrases, and use ssh-agent for convenience.</p>
            <p><strong>Server config:</strong> harden /etc/ssh/sshd_config (disable RootLogin, disable PasswordAuthentication, set AllowUsers/AllowGroups, configure IdleTimeout).</p>
            <p><strong>Port forwarding & jump hosts:</strong> use bastion/jump hosts and ProxyJump for secure administrative access and auditability.</p>
            <p><strong>Secure copy & file transfer:</strong> scp, sftp, and rsync over SSH are common. Prefer rsync for efficient syncs with checksums.</p>
            <pre>ssh -i key.pem user@host
sshd -t
sudo systemctl restart ssh</pre>
          </div>
        </div>

        <div id="kernel" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Kernel & Modules</div>
          <div class="card-body">
            <p><strong>Kernel basics:</strong> understand kernel role, versions, and ABI compatibility. Check with <code>uname -r</code>.</p>
            <p><strong>Modules:</strong> load/unload with <code>modprobe</code>, list with <code>lsmod</code>, and persist module options in /etc/modprobe.d/.</p>
            <p><strong>Tuning:</strong> sysctl key/value pairs modify kernel behavior (networking, vm, fs). Persist changes in /etc/sysctl.conf or /etc/sysctl.d/.</p>
            <p><strong>Upgrades:</strong> kernel upgrades may require reboots; test in staging and coordinate with maintenance windows.</p>
            <pre>uname -a
lsmod | head
modprobe br_netfilter</pre>
          </div>
        </div>

        <div id="containers" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Containers</div>
          <div class="card-body">
            <p><strong>Runtime choices:</strong> Docker, Podman, containerd — choose based on orchestration, rootless needs, and distribution support.</p>
            <p><strong>Images & registries:</strong> build minimal images, sign images, use private registries, and scan images for vulnerabilities before production use.</p>
            <p><strong>Networking & storage:</strong> container networks, bridge vs host mode, persistent volumes, and bind mounts for data persistence.</p>
            <p><strong>Orchestration:</strong> basic kubectl usage, namespaces, and resource requests/limits; use healthchecks and readiness/liveness probes.</p>
            <pre>docker ps
podman ps
docker run -it --rm alpine sh</pre>
          </div>
        </div>

        <div id="trouble" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Troubleshooting & Rescue</div>
          <div class="card-body">
            <p><strong>Gather information:</strong> logs (journalctl, /var/log), resource usage (top, free, iostat), and recent changes (package updates/config edits).</p>
            <p><strong>Reproduce & isolate:</strong> attempt to reproduce the issue in a safe environment, isolate services, and check dependencies (network, DB, disk).</p>
            <p><strong>Rescue modes:</strong> boot into rescue/single-user, use live media or initramfs to repair filesystems or reset root passwords.</p>
            <p><strong>Common fixes:</strong> fix permissions, clear full disks, restart failed services, and revert problematic config changes using versioned backups.</p>
            <pre>journalctl -xe
systemctl --failed
rescue.target</pre>
          </div>
        </div>

        <div id="perf" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Performance Tuning</div>
          <div class="card-body">
            <p><strong>Measure first:</strong> use sar, iostat, vmstat, top, and perf to identify real bottlenecks before changing settings.</p>
            <p><strong>CPU & scheduling:</strong> tune affinity, use cgroups to limit CPU for noisy neighbors, and adjust scheduler parameters only when required.</p>
            <p><strong>Memory & disk:</strong> monitor free/used memory, swap behavior, and tune dirty_ratio, swappiness, and I/O scheduler for workloads.</p>
            <p><strong>Network:</strong> tune TCP buffers, somaxconn, and use ethtool for NIC-level optimizations when high throughput/low latency is needed.</p>
            <pre>top / htop / iostat / sar
sysctl -a | grep net.core.somaxconn</pre>
          </div>
        </div>

        <div id="tools" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Filesystem Tools</div>
          <div class="card-body">
            <p><strong>Partitioning:</strong> fdisk and parted for creating partitions; use gpt for modern systems when appropriate.</p>
            <p><strong>Filesystem creation & checks:</strong> mkfs for format, fsck for repair — avoid running fsck on mounted filesystems unless safe.</p>
            <p><strong>Maintenance:</strong> use tune2fs/xfs_admin for filesystem tuning, resize2fs/xfs_growfs for online resizing where supported.</p>
            <p><strong>Backup & restore:</strong> prefer filesystem-aware backups (rsync, borg, restic) and test restores regularly.</p>
            <pre>fdisk /dev/xvdf
mkfs.ext4 /dev/xvdf1
fsck -f /dev/xvdf1</pre>
          </div>
        </div>

        <div id="editors" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Editors</div>
          <div class="card-body">
            <p><strong>Choosing editors:</strong> nano for quick edits, vim for modal editing power; learn basic commands for both to be productive.</p>
            <p><strong>Vim basics:</strong> navigation (h/j/k/l), insert mode (i/a), saving (:w), quitting (:q), search (/pattern) and simple macros.</p>
            <p><strong>Nano basics:</strong> Ctrl+O to write, Ctrl+X to exit, and helpful prompts at the bottom for common actions.</p>
            <p><strong>Best practice:</strong> keep consistent editor choices across teams, provide .vimrc or editorconfig for shared defaults, and avoid editing binary files with text editors.</p>
            <pre>nano file.txt
vim file.txt</pre>
          </div>
        </div>

        <div id="archive" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Archives & Compression</div>
          <div class="card-body">
            <p><strong>Tar & gzip:</strong> create compressed archives with tar -czf and extract with tar -xzf; preserve permissions with -p when required.</p>
            <p><strong>Zip:</strong> cross-platform friendly archives; include compression level and recursion flags carefully.</p>
            <p><strong>Efficient transfers:</strong> use rsync with --compress for network transfers, and use incremental backups to reduce bandwidth.</p>
            <p><strong>Choosing formats:</strong> use xz/zstd for higher compression ratios at the cost of CPU; choose based on restore speed needs.</p>
            <pre>tar -czf site.tgz /var/www
zip -r site.zip /var/www
rsync -avz src/ dest/</pre>
          </div>
        </div>

        <div id="text" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Text Processing</div>
          <div class="card-body">
            <p><strong>Searching:</strong> grep for searching; ripgrep (rg) when available for speed and usability.</p>
            <p><strong>Line-oriented tools:</strong> sed for stream edits, awk for column processing and reports, cut/sort/uniq for transforms.</p>
            <p><strong>Combining tools:</strong> pipe small utilities together — keep commands simple and readable; avoid overcomplicated one-liners in production scripts.</p>
            <p><strong>Common tasks:</strong> extract fields from /etc/passwd, filter logs, and assemble reports for monitoring or audits.</p>
            <pre>grep -R "pattern" /var/log
sed -n '1,10p' file
awk -F: '{print $1}' /etc/passwd</pre>
          </div>
        </div>

        <div id="regex" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Regular Expressions</div>
          <div class="card-body">
            <p><strong>Basics:</strong> anchors (^,$), character classes ([a-z]), quantifiers (*, +, ?), and groups (()).</p>
            <p><strong>Practical use:</strong> validate interface names, extract IDs from logs, and build safe grep/egrep patterns for alerts.</p>
            <p><strong>Tools:</strong> use grep -E, sed -E or perl for extended regex needs; test expressions with online testers or local echo pipelines.</p>
            <p><strong>Performance:</strong> avoid catastrophic backtracking—prefer simpler, anchored expressions for scanning large files.</p>
            <pre>grep -E "^eth[0-9]+$" <<< "eth0"</pre>
          </div>
        </div>

        <div id="env" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Environment & Dotfiles</div>
          <div class="card-body">
            <p><strong>Dotfiles:</strong> manage ~/.bashrc, ~/.profile, ~/.gitconfig; keep backups and use a dotfiles repo to sync settings across machines.</p>
            <p><strong>PATH & variables:</strong> safely append to PATH, avoid polluting environment with secrets, and use env files with restricted permissions when necessary.</p>
            <p><strong>Shell choice:</strong> bash is common, zsh offers interactive features; scripts should use a defined shebang (#!/usr/bin/env bash).</p>
            <p><strong>Session management:</strong> use tmux or screen for long-lived sessions, and export essential variables in systemd unit files if services need them.</p>
            <pre>echo "export PATH=\"$HOME/bin:$PATH\"" >> ~/.bashrc && source ~/.bashrc
printenv | sort | less</pre>
          </div>
        </div>

        <div id="git" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Git Basics</div>
          <div class="card-body">
            <p><strong>Workflow:</strong> understand clone, branch, commit, merge/rebase, and push; adopt a branching strategy that fits your team (Git Flow, trunk-based).</p>
            <p><strong>Commits:</strong> write clear messages, sign commits when required, and use .gitignore to avoid committing secrets or build artifacts.</p>
            <p><strong>History & recovery:</strong> use git log, reflog, and revert/cherry-pick for safe history fixes; never rewrite shared history without coordination.</p>
            <p><strong>Automation:</strong> use hooks, CI pipelines, and protected branches to enforce tests and code reviews before merging to mainline.</p>
            <pre>git init && git add . && git commit -m "init"
git log --oneline --graph --decorate</pre>
          </div>
        </div>

        <div id="sysinfo" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">System Info & Hardware</div>
          <div class="card-body">
            <p><strong>OS info:</strong> lsb_release or /etc/os-release for distribution details; useful when following distro-specific guides.</p>
            <p><strong>CPU & memory:</strong> lscpu, free -h show capacity; watch for swap usage and memory pressure.</p>
            <p><strong>Storage:</strong> lsblk, df -h, and smartctl for drive health; monitor IO wait and filesystem utilization.</p>
            <p><strong>Inventory:</strong> collect hardware and firmware versions for audits and support tickets.</p>
            <pre>lsb_release -a || cat /etc/os-release
lscpu; free -h; lsblk</pre>
          </div>
        </div>

        <div id="time" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">Time & NTP/chrony</div>
          <div class="card-body">
            <p><strong>Importance of time:</strong> correct time is critical for logs, certificates, cron jobs, and distributed systems coordination.</p>
            <p><strong>Time services:</strong> use chrony or systemd-timesyncd or ntpd depending on distro; prefer chrony on cloud VMs for speed and stability.</p>
            <p><strong>Drift diagnosis:</strong> use timedatectl and chronyc tracking to inspect synchronization status; correct large offsets carefully.</p>
            <p><strong>Best practice:</strong> point servers to internal NTP pool or reliable upstream servers and monitor sync status with alerts.</p>
            <pre>timedatectl
systemctl status chronyd || systemctl status systemd-timesyncd</pre>
          </div>
        </div>

        <div id="dns" class="section-card" style="margin-bottom:14px%;">
          <div class="card-header">DNS Tools</div>
          <div class="card-body">
            <p><strong>Resolution basics:</strong> /etc/resolv.conf and systemd-resolved behavior; know where your system gets DNS from.</p>
            <p><strong>Debugging:</strong> dig, host, and nslookup for querying records; use +trace to see delegation path and troubleshoot propagation.</p>
            <p><strong>Common issues:</strong> TTLs, caching, misconfigured glue records, and firewall blocking UDP/53 can cause resolution failures.</p>
            <p><strong>Testing:</strong> check A, AAAA, MX, TXT, and CNAME records and verify from multiple networks to rule out caching issues.</p>
            <pre>dig +short A example.com
host example.com</pre>
          </div>
        </div>

        <div id="http" class="section-card" style="margin-bottom:28px;">
          <div class="card-header">HTTP Tools</div>
          <div class="card-body">
            <p><strong>Basic checks:</strong> curl and wget to fetch headers and content, verify TLS certs, redirects, and response codes.</p>
            <p><strong>Performance & debugging:</strong> use curl -I for headers, curl --resolve to test DNS/host header combos, and analyze latency with --write-out.</p>
            <p><strong>Load testing:</strong> simple checks with ab or wrk for synthetic load; use caution on production systems and prefer controlled environments.</p>
            <p><strong>Proxies & headers:</strong> inspect request/response headers to find caching, compression, or proxy-related issues; test various user agents and accept-encoding values.</p>
            <pre>curl -I https://example.com
wget -O /dev/null -S https://example.com</pre>
          </div>
        </div>
      </section>
    </div>

    <!-- Rocket Scroll-to-Top Button -->
    <button id="heliTopBtn" class="heli-btn" aria-label="Back to top">
      <div class="heli">
        <div class="heli-rotor">
          <div class="heli-rotor-blade"></div>
        </div>
        <div class="heli-body">
          <div class="heli-window"></div>
        </div>
        <div class="heli-tail">
          <div class="heli-tail-rotor"></div>
        </div>
        <div class="heli-skids"></div>
      </div>
    </button>

    <script>
    (function(){
      const cmdInput = document.getElementById('cmdInput');
      const btnRun = document.getElementById('btnRun');
      const cmdResult = document.getElementById('cmdResult');
      const toc = document.getElementById('linuxToc');
      const progressBar = document.getElementById('progressBar');
      const heliBtn = document.getElementById('heliTopBtn');

      if(!cmdInput || !btnRun || !cmdResult){ console.warn('Linux module: missing widget nodes'); }

      const COMMAND_USECASE = {
        "ls":"List directory contents.","cd":"Change the current working directory.","pwd":"Print the current working directory.",
        "echo":"Print arguments to standard output.","printf":"Format and print data.","clear":"Clear the terminal screen.",
        "cat":"Print file contents to stdout.","less":"View file contents one screen at a time.","head":"Show first lines of files.",
        "tail":"Show last lines of files; -f to follow.","sed":"Stream editor for substitutions/filters.",
        "awk":"Pattern scanning and processing language.","grep":"Search text using regular expressions.",
        "cut":"Select sections from lines.","sort":"Sort lines of text files.","uniq":"Report or filter duplicate lines.",
        "tee":"Copy stdin to stdout and files.","wc":"Count lines, words, bytes.","diff":"Show line differences between files.",
        "touch":"Create empty files or update timestamps.","mkdir":"Create directories.","rmdir":"Remove empty directories.",
        "cp":"Copy files or directories.","mv":"Move or rename files/dirs.","rm":"Remove files or directories.",
        "rsync":"Efficient file sync and transfer.","tar":"Archive files (tarballs).","gzip":"Compress files with gzip.",
        "unzip":"Extract ZIP archives.","chmod":"Change permission bits.","chown":"Change file owner/group.","umask":"Set default permission mask.",
        "id":"Print user/group IDs.","whoami":"Print effective username.","useradd":"Create a new user.","usermod":"Modify a user account.",
        "sudo":"Run a command as another user (root).","ps":"Process snapshot.","top":"Interactive process viewer.","kill":"Send signals to processes.",
        "systemctl":"Control and query systemd.","journalctl":"Query systemd journal logs.",
        "ip":"Show/manipulate network, routes, links.","ss":"Socket statistics (netstat replacement).","ping":"Send ICMP echo requests.",
        "dig":"DNS lookup utility.","curl":"Transfer data to/from URLs.","wget":"Non-interactive network downloader.",
        "ssh":"OpenSSH remote login.","scp":"Secure copy over SSH.","sftp":"Interactive file transfer over SSH.",
        "lsblk":"List block devices.","mount":"Mount a filesystem.","umount":"Unmount a filesystem.","df":"Report filesystem disk space usage.","du":"Estimate file/directory space usage.",
        "mkfs.ext4":"Create an ext4 filesystem.","fsck":"Check/repair a filesystem.","fdisk":"Partition editor.","parted":"Modern partition tool.",
        "pvcreate":"Initialize a physical volume for LVM.","vgcreate":"Create a volume group.","lvcreate":"Create a logical volume.",
        "apt":"APT package manager.","yum":"RPM-based package manager.","dnf":"Modern RPM package manager.","rpm":"RPM package manager.",
        "ufw":"Uncomplicated Firewall frontend.","iptables":"Legacy packet filter and NAT.","firewall-cmd":"firewalld CLI.",
        "getenforce":"Get SELinux status.","setenforce":"Set SELinux mode.",
        "uname":"Print system/kernel info.","lscpu":"Display CPU info.","free":"Show memory usage.",
        "vmstat":"Report performance stats.","dmesg":"Kernel ring buffer messages.","lsmod":"List loaded kernel modules.","modprobe":"Load/unload modules.",
        "nano":"Simple terminal text editor.","vim":"Vi IMproved text editor.","git":"Distributed version control.",
        "docker":"Manage Docker containers/images.","podman":"Daemonless OCI containers.","kubectl":"Control Kubernetes clusters.",
        "aws":"AWS CLI for AWS services.","terraform":"Infrastructure as code."
      };

      const PATTERNS = [
        {re:/^mkfs\.(\w+)/, msg:(m)=>"Create a "+m[1].toUpperCase()+" filesystem on a block device."},
        {re:/^fsck\.(\w+)/, msg:(m)=>"Check/repair a "+m[1].toUpperCase()+" filesystem."},
        {re:/^lv\w+$/, msg:()=> "LVM logical volume management command."},
        {re:/^vg\w+$/, msg:()=> "LVM volume group management command."},
        {re:/^pv\w+$/, msg:()=> "LVM physical volume management command."},
        {re:/^e2\w+$/, msg:()=> "ext2/3/4 filesystem utility."},
        {re:/^(yum|dnf)$/, msg:(m)=> (m[1]==="dnf"?"Modern RPM package manager for Fedora/RHEL.":"RPM-based package manager for RHEL/CentOS/Amazon Linux.")},
        {re:/^(rpm)$/, msg:()=> "Install, query, verify, and manage RPM packages."},
        {re:/^(apt|apt-get|apt-cache)$/, msg:(m)=> ({"apt":"APT high-level package manager.","apt-get":"Low-level APT operations.","apt-cache":"Query APT package metadata."})[m[1]]},
        {re:/^iptables(?:-save|-restore)?$/, msg:()=> "Legacy packet filter/NAT rules (IPv4)."},
        {re:/^ip6tables(?:-save|-restore)?$/, msg:()=> "Legacy packet filter rules (IPv6)."},
        {re:/^nft$/, msg:()=> "Configure nftables firewall rules."},
        {re:/^ssh-\w+$/, msg:()=> "OpenSSH utility (keys/agent/config)."},
        {re:/^(ctr|crictl|nerdctl)$/, msg:()=> "Low-level container runtime tooling."},
        {re:/^(helm|kustomize)$/, msg:(m)=> (m[1]==="helm"?"Kubernetes package manager (Charts).":"Kubernetes manifest customization.")},
        {re:/^(aws|az|gcloud)$/, msg:(m)=> ({"aws":"AWS command-line interface.","az":"Azure command-line interface.","gcloud":"Google Cloud command-line interface."}[m[1]])},
        {re:/^(terraform|ansible|packer|vault)$/, msg:(m)=> ({"terraform":"Infrastructure as Code (provisioning).","ansible":"Agentless automation/configuration.","packer":"Build machine images.","vault":"Secret management & encryption."}[m[1]])}
      ];

      function basename(path){ return (path||'').trim().split('/').filter(Boolean).pop() || path; }
      function extractBaseCommand(raw){
        if(!raw) return '';
        let s = raw.trim();
        if(s.startsWith('sudo ')) s = s.slice(5);
        let tok = s.split(/\s+/)[0];
        tok = basename(tok);
        return tok.toLowerCase().replace(/:$/,'');
      }
      function explain(cmd){
        const base = extractBaseCommand(cmd);
        if(!base) return {title:null, text:'Type a command and press Run.'};
        if(COMMAND_USECASE[base]) return {title:base, text:COMMAND_USECASE[base]};
        for(const p of PATTERNS){
          const m = base.match(p.re);
          if(m) return {title: base, text: (typeof p.msg === 'function') ? p.msg(m) : p.msg};
        }
        return {title:base, text:'Generic UNIX/Linux program. See its manual for details.'};
      }

      function renderCmd(){
        try{
          const raw = cmdInput.value || '';
          const out = explain(raw);
          if(!out.title){
            cmdResult.innerHTML = '<div style="color:#924a4a;font-weight:800;">' + out.text + '</div>';
            return;
          }
          cmdResult.innerHTML = '<div><span class="badge">Command</span> <strong>' + escapeHtml(out.title) + '</strong></div>'
                              + '<div style="margin-top:8px;"><span class="badge">Use case</span> ' + escapeHtml(out.text) + '</div>';
        }catch(e){
          cmdResult.innerHTML = '<div style="color:#924a4a;font-weight:800;">Failed to explain command.</div>';
          console.error(e);
        }
      }

      function escapeHtml(s){
        return String(s).replace(/[&<>"]/g, function(c){
          return { '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;' }[c];
        });
      }

      if(btnRun){
        btnRun.addEventListener('click', function(e){ e.preventDefault(); renderCmd(); });
      }
      if(cmdInput){
        cmdInput.addEventListener('keydown', function(e){
          if(e.key === 'Enter'){
            e.preventDefault();
            renderCmd();
          }
        });
      }

      try{
        if(progressBar){
          const updateProgress = () => {
            const h = document.documentElement;
            const scroll = (h.scrollTop || document.body.scrollTop);
            const height = (h.scrollHeight - h.clientHeight) || 1;
            const percent = Math.min(100, Math.max(0, (scroll/height * 100)));
            progressBar.style.width = percent + '%';
          };
          window.addEventListener('scroll', updateProgress, { passive: true });
          window.addEventListener('resize', updateProgress);
          updateProgress();
        }

        // ✅ FIXED: Robust copy-to-clipboard for all <pre> blocks
        document.querySelectorAll('pre').forEach(pre => {
          try{
            const wrapper = document.createElement('div');
            wrapper.style = 'position:relative; margin-top:0.6rem;';
            pre.parentNode.insertBefore(wrapper, pre);
            wrapper.appendChild(pre);

            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'pre-copy';
            btn.title = 'Copy';
            btn.innerText = 'Copy';
            wrapper.appendChild(btn);

            btn.addEventListener('click', async (ev) => {
              ev.preventDefault();
              ev.stopPropagation();
              const text = pre.innerText || '';

              const fallbackCopy = () => {
                const ta = document.createElement('textarea');
                ta.value = text;
                ta.style.position = 'fixed';
                ta.style.opacity = '0';
                ta.style.left = '-9999px';
                document.body.appendChild(ta);
                ta.focus();
                ta.select();
                const ok = document.execCommand('copy');
                document.body.removeChild(ta);
                if(!ok) throw new Error('execCommand copy failed');
              };

              try {
                if (navigator.clipboard && navigator.clipboard.writeText) {
                  await navigator.clipboard.writeText(text);
                } else {
                  fallbackCopy();
                }
                btn.innerText = 'Copied';
                setTimeout(()=> btn.innerText = 'Copy', 1200);
              } catch(e) {
                try {
                  fallbackCopy();
                  btn.innerText = 'Copied';
                  setTimeout(()=> btn.innerText = 'Copy', 1200);
                } catch(e2) {
                  console.error('Copy failed', e2);
                  btn.innerText = 'Err';
                  setTimeout(()=> btn.innerText='Copy',1200);
                }
              }
            });
          }catch(e){
            // ignore per-pre errors
          }
        });

        if (heliBtn) {
          const toggleHeli = () => {
            if (window.scrollY > 200) {
              heliBtn.classList.add('show');
            } else {
              heliBtn.classList.remove('show');
            }
          };
          window.addEventListener('scroll', toggleHeli, { passive: true });
          window.addEventListener('resize', toggleHeli);
          toggleHeli();

          heliBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
              top: 0,
              behavior: 'smooth'
            });
          });
        }

        const tocLinks = Array.from(document.querySelectorAll('#linuxToc a'));
        let tocIndex = tocLinks.findIndex(a => a.classList.contains('active'));
        if(tocIndex === -1) tocIndex = 0;
        document.addEventListener('keydown', (e) => {
          if(['ArrowDown','ArrowUp'].includes(e.key) && document.activeElement && document.activeElement.closest('#linuxToc')){
            e.preventDefault();
            if(e.key === 'ArrowDown') tocIndex = Math.min(tocIndex + 1, tocLinks.length - 1);
            else tocIndex = Math.max(tocIndex - 1, 0);
            const a = tocLinks[tocIndex]; if(a){ a.focus(); a.click(); }
          }
        });

        const tocEl = document.getElementById('linuxToc');
        function headerForHref(href){
          try{
            const target = document.querySelector(href);
            if(!target) return null;
            return target.querySelector('.card-header') || null;
          }catch(e){
            return null;
          }
        }
        function bodyForHref(href){
          try{
            const target = document.querySelector(href);
            if(!target) return null;
            return target.querySelector('.card-body') || null;
          }catch(e){
            return null;
          }
        }
        function wrapTextNodes(root){
          const SKIP_TAGS = new Set(['PRE','CODE','SCRIPT','STYLE']);
          function walk(node){
            if(!node) return;
            if(node.nodeType === 1 && SKIP_TAGS.has(node.tagName)) return;
            if(node.nodeType === 3){
              const text = node.nodeValue;
              if(!text || /^\s*$/.test(text)) return;
              const frag = document.createDocumentFragment();
              for(const ch of text){
                const span = document.createElement('span');
                span.className = 'typing-char';
                span.textContent = ch;
                frag.appendChild(span);
              }
              node.parentNode.replaceChild(frag, node);
              return;
            }
            const children = Array.from(node.childNodes);
            for(const c of children) walk(c);
          }
          walk(root);
        }
        function restoreOriginal(body){
          if(body && body.dataset && body.dataset.originalHtml){
            body.innerHTML = body.dataset.originalHtml;
          }
        }
        function revealTyping(body, speedMs){
          const chars = Array.from(body.querySelectorAll('.typing-char'));
          if(chars.length === 0) return Promise.resolve();
          if(chars.length > 800){
            chars.forEach(c => c.classList.add('reveal'));
            return Promise.resolve();
          }
          chars.forEach(c => c.classList.remove('reveal'));
          return new Promise(resolve => {
            let i = 0;
            const total = chars.length;
            const timer = setInterval(() => {
              if(i >= total){
                clearInterval(timer);
                resolve();
                return;
              }
              chars[i].classList.add('reveal');
              i++;
            }, speedMs);
          });
        }
        function prepareTyping(body){
          if(!body) return;
          if(!body.dataset.originalHtml) body.dataset.originalHtml = body.innerHTML;
          restoreOriginal(body);
          wrapTextNodes(body);
        }
        async function animateTyped(body, speedMs=10){
          if(!body) return;
          prepareTyping(body);
          await revealTyping(body, speedMs);
        }

        if(tocEl){
          tocEl.addEventListener('click', function(ev){
            if(ev.target && ev.target.tagName === 'A'){
              ev.preventDefault();
              const href = ev.target.getAttribute('href');
              const el = document.querySelector(href);

              Array.from(tocEl.querySelectorAll('a')).forEach(a => a.classList.remove('active'));
              ev.target.classList.add('active');

              const hdr = headerForHref(href);
              if(hdr){
                hdr.classList.remove('pulse-headline');
                void hdr.offsetWidth;
                hdr.classList.add('pulse-headline');
                setTimeout(()=>hdr.classList.remove('pulse-headline'), 1250);
              }

              if(el){
                el.scrollIntoView({ behavior:'smooth', block:'start' });
                el.classList.add('hit');
                setTimeout(()=>el.classList.remove('hit'), 1200);
                const body = bodyForHref(href);
                if(body) animateTyped(body, 10).catch(err => console.warn('typing anim err', err));
              }
            }
          });

          tocEl.addEventListener('mouseover', function(ev){
            const a = ev.target && ev.target.tagName === 'A' ? ev.target : null;
            if(!a) return;
            const href = a.getAttribute('href');
            const hdr = headerForHref(href);
            if(!hdr) return;
            hdr.classList.remove('pulse-headline');
            void hdr.offsetWidth;
            hdr.classList.add('pulse-headline');
            setTimeout(()=>hdr.classList.remove('pulse-headline'), 1250);
          }, true);
        }
      }catch(e){ console.warn('UI enhancement script error', e); }

    })();
    </script>
    '''

def render_service(service_id: str):
    sid = (service_id or "").lower().strip()
    return f"<h2>Linux — {sid}</h2><p>Detailed content for {sid} will be added here.</p>"

