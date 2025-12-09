# virtual_lab.py
# Advanced Virtual Linux Terminal Backend
# Encapsulates a JS-based mock kernel and filesystem for a realistic experience.

def render_lab():
    """
    Returns the complete HTML/JS/CSS structure for the Virtual Lab.
    """
    return """
    <style>
        .terminal-container {
            width: 100%;
            height: 600px;
            background-color: #0c0c0c;
            color: #cccccc;
            font-family: 'Fira Code', 'Consolas', monospace;
            font-size: 14px;
            line-height: 1.5;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            border: 1px solid #333;
        }

        .term-header {
            background: #1f1f1f;
            padding: 8px 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #333;
            user-select: none;
        }

        .term-controls { display: flex; gap: 8px; }
        .term-btn { width: 12px; height: 12px; border-radius: 50%; display: inline-block; }
        .term-close { background-color: #ff5f56; }
        .term-min { background-color: #ffbd2e; }
        .term-max { background-color: #27c93f; }
        .term-title { color: #888; font-size: 12px; font-weight: 500; }

        .term-window {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            cursor: text;
        }
        
        .term-content {
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        .term-input-line {
            display: flex;
            margin-top: 5px;
        }

        .term-prompt {
            color: #4ade80; /* User green */
            margin-right: 8px;
            font-weight: bold;
        }
        .term-prompt.root {
            color: #ff5f56; /* Root red */
        }
        .term-path {
            color: #60a5fa; /* Blue path */
            font-weight: bold;
        }

        #term-cmd-input {
            background: transparent;
            border: none;
            color: #fff;
            flex: 1;
            font-family: inherit;
            font-size: inherit;
            outline: none;
            padding: 0;
            margin: 0;
            caret-color: #fff;
        }

        .command-output { color: #d4d4d4; margin-bottom: 8px; }
        .error-msg { color: #ff5555; }
        .dir-color { color: #60a5fa; font-weight: bold; }
        .exec-color { color: #4ade80; }
    </style>

    <div class="terminal-container" onclick="document.getElementById('term-cmd-input').focus()">
        <div class="term-header">
            <div class="term-controls">
                <span class="term-btn term-close"></span>
                <span class="term-btn term-min"></span>
                <span class="term-btn term-max"></span>
            </div>
            <div class="term-title">student@linux-vm: ~ (bash)</div>
            <div style="width: 50px;"></div>
        </div>
        <div class="term-window" id="term-window">
            <div class="term-content" id="term-history">
                <div>Welcome to Cloud-with-Sai Linux Lab v2.0</div>
                <div style="color:#666; margin-bottom:10px;">Type 'help' to see available commands. This is a fully interactive simulation.</div>
            </div>
            <div class="term-input-line" id="term-input-line">
                <span id="term-prompt-span">
                    <span class="term-prompt">student@linux-vm:</span><span class="term-path">~</span>$
                </span>
                <input type="text" id="term-cmd-input" autocomplete="off" spellcheck="false" onkeydown="handleLabKey(event)">
            </div>
        </div>
    </div>

    <script>
    /**
     * VIRTUAL KERNEL SIMULATION
     * Implements a Mock Filesystem, Path Resolution, and Command Execution.
     */
    
    (function() {
        // --- FILESYSTEM STATE ---
        const fs = {
            "/": { type: "dir", children: {
                "home": { type: "dir", children: {
                    "student": { type: "dir", children: {
                        "Documents": { type: "dir", children: {
                            "project.txt": { type: "file", content: "Linux project deadline: Friday." }
                        }},
                        "Downloads": { type: "dir", children: {} },
                        "scripts": { type: "dir", children: {
                            "deploy.sh": { type: "file", content: "#!/bin/bash\\necho 'Deploying...'" }
                        }},
                        "hello.txt": { type: "file", content: "Hello World! Linux is awesome." }
                    }}
                }},
                "etc": { type: "dir", children: {
                    "passwd": { type: "file", content: "root:x:0:0:root:/root:/bin/bash\\nstudent:x:1000:1000:student:/home/student:/bin/bash" },
                    "hostname": { type: "file", content: "linux-vm" }
                }},
                "var": { type: "dir", children: {
                    "log": { type: "dir", children: {
                        "syslog": { type: "file", content: "Dec 9 10:00:00 linux-vm systemd[1]: Started Session 1 of user student." }
                    }}
                }},
                "bin": { type: "dir", children: {} } // Mock bin
            }}
        };

        // --- SESSION STATE ---
        let state = {
            user: "student",
            hostname: "linux-vm",
            cwd: "/home/student", // Current working directory (absolute)
            history: [],
            historyIdx: -1
        };

        // --- CORE UTILS ---
        
        // Resolve path to a node in the FS object
        // Returns { node, name, parent } or null if not found
        function resolve(pathStr) {
            // Handle ~
            if (pathStr === '~') pathStr = "/home/student";
            if (pathStr.startsWith("~/")) pathStr = "/home/student" + pathStr.substring(1);

            // Absolute vs Relative
            let currentPathParts = (pathStr.startsWith('/')) ? [] : state.cwd.split('/').filter(p => p);
            let targetParts = pathStr.split('/').filter(p => p);
            
            let stack = [...currentPathParts];
            
            for (let part of targetParts) {
                if (part === '.') continue;
                if (part === '..') {
                    if (stack.length > 0) stack.pop();
                } else {
                    stack.push(part);
                }
            }

            // Traverse fs
            let currNode = fs["/"];
            let parentNode = null;
            let lastPart = "";

            if (stack.length === 0) return { node: fs["/"], name: "/", parent: null, absPath: "/" };

            for (let i = 0; i < stack.length; i++) {
                let p = stack[i];
                if (currNode.type !== 'dir') return null; // Can't traverse file
                if (!currNode.children[p]) return null; // Not found
                parentNode = currNode;
                currNode = currNode.children[p];
                lastPart = p;
            }
            
            return { node: currNode, name: lastPart, parent: parentNode, absPath: "/" + stack.join('/') };
        }

        // Get Display Path (replace /home/student with ~)
        function getDisplayPath() {
            let path = state.cwd;
            if (path.startsWith("/home/student")) {
                return "~" + path.substring(13);
            }
            return path;
        }

        // --- COMMANDS ---
        const commands = {
            help: {
                desc: "List available commands",
                exe: () => "Available commands: <br>Core: ls, cd, pwd, mkdir, rm, touch, cat, echo, cp, mv <br>Sys: whoami, hostname, date, clear, history, sudo, reboot"
            },
            ls: {
                desc: "List directory contents",
                exe: (args) => {
                    let targetPath = args[0] || ".";
                    let res = resolve(targetPath);
                    if (!res || res.node.type !== 'dir') return `<span class='error-msg'>ls: cannot access '${targetPath}': No such file or directory</span>`;
                    
                    let out = [];
                    for (let child in res.node.children) {
                        let isDir = res.node.children[child].type === 'dir';
                        out.push(`<span class='${isDir ? "dir-color" : ""}'>${child}</span>`);
                    }
                    return out.join("  ");
                }
            },
            pwd: {
                desc: "Print working directory",
                exe: () => state.cwd
            },
            cd: {
                desc: "Change directory",
                exe: (args) => {
                    let target = args[0] || "~";
                    let res = resolve(target);
                    if (!res) return `<span class='error-msg'>bash: cd: ${target}: No such file or directory</span>`;
                    if (res.node.type !== 'dir') return `<span class='error-msg'>bash: cd: ${target}: Not a directory</span>`;
                    state.cwd = res.absPath;
                    updatePrompt();
                    return "";
                }
            },
            cat: {
                desc: "Concatenate and print files",
                exe: (args) => {
                    if (!args[0]) return "<span class='error-msg'>Usage: cat filename</span>";
                    let res = resolve(args[0]);
                    if (!res) return `<span class='error-msg'>cat: ${args[0]}: No such file or directory</span>`;
                    if (res.node.type === 'dir') return `<span class='error-msg'>cat: ${args[0]}: Is a directory</span>`;
                    return res.node.content || "";
                }
            },
            touch: {
                desc: "Create empty file",
                exe: (args) => {
                    if (!args[0]) return "<span class='error-msg'>Usage: touch filename</span>";
                    // Only simple creation in current dir for now for simplicity, or full path
                    // Let's resolve parent
                    let pathStr = args[0];
                    let parts = pathStr.split('/');
                    let fileName = parts.pop();
                    let parentPath = parts.length > 0 ? parts.join('/') : ".";
                    
                    let parentRes = resolve(parentPath);
                    if (!parentRes || parentRes.node.type !== 'dir') return `<span class='error-msg'>touch: cannot touch '${pathStr}': No such file or directory</span>`;
                    
                    if (!parentRes.node.children[fileName]) {
                        parentRes.node.children[fileName] = { type: 'file', content: "" };
                    }
                    return "";
                }
            },
            mkdir: {
                desc: "Make directory",
                exe: (args) => {
                    if (!args[0]) return "<span class='error-msg'>Usage: mkdir dirname</span>";
                    let pathStr = args[0];
                    let parts = pathStr.split('/');
                    let dirName = parts.pop();
                    let parentPath = parts.length > 0 ? parts.join('/') : ".";
                    
                    let parentRes = resolve(parentPath);
                    if (!parentRes || parentRes.node.type !== 'dir') return `<span class='error-msg'>mkdir: cannot create directory '${pathStr}': No such file or directory</span>`;
                    
                    if (parentRes.node.children[dirName]) return `<span class='error-msg'>mkdir: cannot create directory '${dirName}': File exists</span>`;
                    
                    parentRes.node.children[dirName] = { type: 'dir', children: {} };
                    return "";
                }
            },
            rm: {
                desc: "Remove file or directory",
                exe: (args) => {
                     // simplified rm -rf logic
                     if (!args[0]) return "<span class='error-msg'>Usage: rm filename</span>";
                     let res = resolve(args[0]);
                     if (!res) return `<span class='error-msg'>rm: cannot remove '${args[0]}': No such file or directory</span>`;
                     
                     // Root protection
                     if (res.absPath === "/") return "<span class='error-msg'>rm: cannot remove root directory</span>";
                     
                     // Hacky parent removal
                     // We need to find the parent object to delete the key.
                     // Re-resolve parent
                     let lastSlash = res.absPath.lastIndexOf('/');
                     let parentPath = res.absPath.substring(0, lastSlash) || "/";
                     let name = res.absPath.substring(lastSlash + 1);
                     
                     let parentRes = resolve(parentPath);
                     delete parentRes.node.children[name];
                     return "";
                }
            },
            echo: {
                desc: "Display text",
                exe: (args) => args.join(' ')
            },
            whoami: {
                exe: () => state.user
            },
            hostname: {
                exe: () => state.hostname
            },
            date: {
                exe: () => new Date().toString()
            },
            clear: {
                exe: () => {
                    document.getElementById('term-history').innerHTML = "";
                    return "";
                }
            },
            history: {
                exe: () => state.history.map((c, i) => `${i + 1}  ${c}`).join('<br>')
            },
            sudo: {
                exe: (args) => {
                   if (args.length === 0) return "usage: sudo command...";
                   // Simulation of root access (only changes prompt color in this mock)
                   if (args[0] === 'su' || args[0] === '-i') {
                       state.user = 'root';
                       updatePrompt();
                       return "";
                   }
                   return executeCommand(args.join(' ')); // just run it
                }
            },
            reboot: {
                exe: () => { window.location.reload(); return "Rebooting..."; }
            }
        };

        // --- EXECUTION ENGINE ---
        function executeCommand(fullCmd) {
            fullCmd = fullCmd.trim();
            if (!fullCmd) return "";
            
            state.history.push(fullCmd);
            state.historyIdx = state.history.length;
            
            const tokens = fullCmd.split(' ').filter(x => x);
            const cmdName = tokens[0];
            const args = tokens.slice(1);
            
            const cmdObj = commands[cmdName];
            if (cmdObj) {
                try {
                    return cmdObj.exe(args);
                } catch (e) {
                    console.error(e);
                    return `<span class='error-msg'>bash: error executing ${cmdName}</span>`;
                }
            } else {
                return `<span class='error-msg'>bash: ${cmdName}: command not found</span>`;
            }
        }

        // --- UI INTERACTION ---
        function updatePrompt() {
            const promptSpan = document.getElementById('term-prompt-span');
            const isRoot = state.user === 'root';
            const char = isRoot ? '#' : '$';
            promptSpan.innerHTML = `
                <span class="term-prompt ${isRoot ? 'root' : ''}">${state.user}@${state.hostname}:</span><span class="term-path">${getDisplayPath()}</span>${char}
            `;
        }

        window.handleLabKey = function(e) {
            if (e.key === 'Enter') {
                const input = document.getElementById('term-cmd-input');
                const val = input.value;
                const historyDiv = document.getElementById('term-history');
                
                // Echo the command
                const promptHTML = document.getElementById('term-prompt-span').innerHTML;
                const cmdLine = document.createElement('div');
                cmdLine.innerHTML = promptHTML + " " + val;
                historyDiv.appendChild(cmdLine);
                
                // Execute
                const output = executeCommand(val);
                if (output) {
                    const outDiv = document.createElement('div');
                    outDiv.className = 'command-output';
                    outDiv.innerHTML = output;
                    historyDiv.appendChild(outDiv);
                }
                
                // Reset
                input.value = "";
                
                // Scroll to bottom
                const win = document.getElementById('term-window');
                win.scrollTop = win.scrollHeight;
            }
            // Simple History Navigation
            else if (e.key === 'ArrowUp') {
                 e.preventDefault();
                 if (state.historyIdx > 0) {
                     state.historyIdx--;
                     document.getElementById('term-cmd-input').value = state.history[state.historyIdx];
                 }
            }
            else if (e.key === 'ArrowDown') {
                 e.preventDefault();
                 if (state.historyIdx < state.history.length - 1) {
                     state.historyIdx++;
                     document.getElementById('term-cmd-input').value = state.history[state.historyIdx];
                 } else {
                     state.historyIdx = state.history.length;
                     document.getElementById('term-cmd-input').value = "";
                 }
            }
        }
        
    })();
    </script>
    """
