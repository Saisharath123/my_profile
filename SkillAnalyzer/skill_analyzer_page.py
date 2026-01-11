from flask import url_for, redirect, request, jsonify
import json
import os
from datetime import datetime

def register_routes(app, render_page_func):
    @app.route("/skill-analyzer", methods=['GET', 'POST'])
    @app.route("/skill-selection", methods=['GET', 'POST'])
    def skill_selection():
        # Parent Page: Shows "Live Test" and "Virtual Interview"
        try:
            from .LiveTest import LIVE_TEST_CONTENT
            from .VirtualInterview import VIRTUAL_INTERVIEW_CONTENT
            
            # Update Live Test route to point to our new hub
            LIVE_TEST_CONTENT['route'] = url_for('live_test_hub')
            
            # Ensure features are present for the main cards
            if 'features' not in LIVE_TEST_CONTENT: LIVE_TEST_CONTENT['features'] = []
            if 'features' not in VIRTUAL_INTERVIEW_CONTENT: VIRTUAL_INTERVIEW_CONTENT['features'] = []

            modules = [LIVE_TEST_CONTENT, VIRTUAL_INTERVIEW_CONTENT]
        except ImportError:
            modules = []

        # HTML for Parent Page
        html = """
        {% raw %}
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
            
            /* --- ANIMATED HEADER --- */
            .sa-header {
                position: relative;
                background: linear-gradient(-45deg, #1e293b, #0f172a, #334155, #1e293b);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
                padding: 60px 20px;
                border-radius: 24px;
                text-align: center;
                color: #fff;
                overflow: hidden;
                margin-bottom: 40px;
                box-shadow: 0 20px 40px -10px rgba(0,0,0,0.3);
            }
            
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .sa-title {
                font-family: 'Outfit', sans-serif;
                font-size: 3rem;
                font-weight: 800;
                margin: 0;
                background: linear-gradient(to right, #ffffff, #94a3b8);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            /* --- MODULES GRID --- */
            .sa-modules-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 30px;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }

            .sa-card {
                background: #fff;
                border-radius: 20px;
                border: 1px solid #e2e8f0;
                padding: 30px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.05);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                height: 100%;
            }

            .sa-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                border-color: #3b82f6;
            }
            
            .sa-icon-box {
                width: 80px; height: 80px;
                border-radius: 50%;
                background: #f8fafc;
                display: flex; align-items: center; justify-content: center;
                margin-bottom: 20px;
                overflow: hidden;
                border: 1px solid #f1f5f9;
                font-size: 2.5rem;
            }
            
            .sa-icon-box img {
                width: 85%;
                height: 85%;
                object-fit: contain;
            }
            
            .sa-card h2 {
                font-family: 'Outfit', sans-serif;
                color: #1e293b;
                font-size: 1.5rem;
                margin: 0 0 12px 0;
                font-weight: 700;
            }
            
            .sa-card p {
                color: #64748b;
                font-size: 1rem;
                line-height: 1.5;
                margin-bottom: 24px;
                flex-grow: 1;
            }

            .sa-btn {
                background: #0f172a;
                color: #fff;
                padding: 12px 24px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                transition: background 0.2s;
                width: 100%;
                display: block;
                box-sizing: border-box;
                margin-top: auto;
            }
            .sa-btn:hover {
                background: #334155;
            }
            
            .sa-features {
                list-style: none;
                padding: 0;
                margin: 0 0 24px 0;
                text-align: left;
                width: 100%;
            }
            .sa-features li {
                margin-bottom: 8px;
                color: #475569;
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 0.9rem;
            }
            .sa-features li::before {
                content: '✓';
                color: #10b981;
                font-weight: bold;
            }

        </style>
        {% endraw %}

        <div style="font-family: 'Inter', sans-serif; padding-bottom: 40px;">
            
            <!-- Animated Header -->
            <div class="sa-header">
                <h1 class="sa-title">Single Platform to Analyze Your Skills</h1>
            </div>

            <!-- Modules -->
            <div class="sa-modules-container">
                {% for module in modules %}
                <div class="sa-card">
                    <div class="sa-icon-box">
                        <!-- If 'image' is a file path, render it. Else render emoji. -->
                        {% if module.get('image') %}
                            <img src="{{ url_for('image_file', filename=module['image']) }}" alt="{{ module['title'] }}">
                        {% else %}
                           <!-- Fallback icons -->
                           {% if module['title'] == 'Live Test' %}📝{% elif module['title'] == 'Virtual Interview' %}🎙️{% else %}❓{% endif %}
                        {% endif %}
                    </div>
                    <h2>{{ module['title'] }}</h2>
                    <p>{{ module['description'] }}</p>
                    
                    {% if module.get('features') %}
                    <ul class="sa-features">
                        {% for feature in module['features'] %}
                        <li>{{ feature }}</li>
                        {% endfor %}
                    </ul>
                    {% endif %}

                    <a href="{{ module.get('route', '#') }}" class="sa-btn" {% if module.get('open_new_tab') %}target="_blank"{% endif %}>{{ module['action_label'] }}</a>
                </div>
                {% endfor %}
            </div>
        </div>
        """
        return render_page_func(html, active="skill-analyzer", modules=modules)

    @app.route("/skill-analyzer/virtual-interview")
    def virtual_interview_legacy():
        return redirect(url_for('ai_interview_session'))

    @app.route("/skill-analyzer/ai-interview-session")
    def ai_interview_session():
        # The AI Interview Interface (Camera, Mic, Selection)
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>AI Virtual Interview Session</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
                body {
                    margin: 0; padding: 0;
                    font-family: 'Outfit', sans-serif;
                    background: #0f172a;
                    color: #fff;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                }
                .ai-header {
                    padding: 20px;
                    border-bottom: 1px solid #334155;
                    display: flex; justify-content: space-between; align-items: center;
                }
                .ai-container {
                    flex-grow: 1;
                    display: flex;
                    padding: 20px;
                    gap: 20px;
                }
                .video-panel {
                    flex: 2;
                    background: #1e293b;
                    border-radius: 16px;
                    overflow: hidden;
                    position: relative;
                    display: flex; align-items: center; justify-content: center;
                    border: 2px solid #334155;
                }
                video {
                    width: 100%; height: 100%; object-fit: cover; transform: scaleX(-1);
                }
                .control-panel {
                    flex: 1;
                    background: #1e293b;
                    border-radius: 16px;
                    padding: 30px;
                    border: 1px solid #334155;
                    display: flex; flex-direction: column;
                }
                h2 { margin-top: 0; color: #38bdf8; }
                select, button {
                    width: 100%;
                    padding: 15px;
                    border-radius: 8px;
                    border: 1px solid #475569;
                    margin-bottom: 20px;
                    font-family: inherit;
                    font-size: 1rem;
                }
                select { background: #0f172a; color: #fff; }
                button {
                    background: #2563eb; color: #fff; border: none; font-weight: bold; cursor: pointer;
                    transition: background 0.2s;
                }
                button:hover { background: #1d4ed8; }
                
                .status-indicator {
                    display: flex; gap: 10px; margin-bottom: 20px;
                }
                .badge {
                    padding: 5px 10px; border-radius: 20px; font-size: 0.8rem; background: #334155; color: #cbd5e1;
                }
                .badge.active { background: #10b981; color: #fff; }
                .badge.error { background: #ef4444; color: #fff; }
                
                #interview-stage { display: none; margin-top: 20px; }
                .ai-avatar {
                    width: 60px; height: 60px; border-radius: 50%; background: #38bdf8;
                    display: flex; align-items: center; justify-content: center; font-size: 2rem;
                    margin-bottom: 15px;
                }
                .question-text {
                    font-size: 1.2rem; line-height: 1.5; color: #fff;
                }
            </style>
        </head>
        <body>
            <div class="ai-header">
                <h3>Skill Analyzer AI Interview (Simulation Ready)</h3>
                <div>🔴 Live Session</div>
            </div>
            
            <div class="ai-container">
                <div class="video-panel">
                    <video id="userVideo" autoplay playsinline muted></video>
                    <div style="position:absolute; bottom:20px; left:20px; background:rgba(0,0,0,0.6); padding:5px 10px; border-radius:5px;">
                        Candidate View
                    </div>
                </div>
                
                <div class="control-panel">
                    <div class="status-indicator">
                        <span id="camStatus" class="badge">Camera Checking...</span>
                        <span id="micStatus" class="badge">Mic Checking...</span>
                    </div>

                    <div id="setup-stage">
                        <h2>Configure Session</h2>
                        <label style="display:block; margin-bottom:10px; color:#94a3b8;">Select Interview Track</label>
                        <select id="interviewType">
                            <option value="aws">AWS Solution Architect Interview</option>
                            <option value="devops">DevOps Interview Questions</option>
                            <option value="linux">Linux Administration Questions</option>
                            <option value="k8s">Kubernetes Exclusively</option>
                        </select>
                        
                        <button onclick="startInterview()">Start Interview</button>
                        <p style="font-size:0.8rem; color:#64748b;">
                            Note: This session uses AI to analyze your responses and body language. Ensure you are in a quiet environment.
                        </p>
                    </div>

                    <div id="interview-stage">
                        <div class="ai-avatar">🤖</div>
                        <h3 style="color:#38bdf8;">AI Interviewer</h3>
                        <p id="questionBox" class="question-text">Initializing session...</p>
                        
                        <div style="margin-top:30px; height:4px; background:#334155; border-radius:2px; overflow:hidden;">
                            <div style="width:100%; height:100%; background:#10b981; animation: pulse 1.5s infinite;"></div>
                        </div>
                        <p id="statusTag" style="text-align:center; color:#64748b; font-size:0.9rem; margin-top:5px;">Preparing...</p>
                        
                        <div id="scorePanel" class="score-box" style="display:none; background:#0f172a; border:1px solid #334155; border-radius:10px; padding:15px; margin-top:20px;">
                            <div>AI Assessment:</div>
                            <div id="scoreValue" style="font-size:1.5rem; font-weight:800; color:#10b981;">-</div>
                            <div id="scoreFeedback" style="font-size:0.9rem; color:#94a3b8; margin-top:5px;">-</div>
                        </div>

                        <div style="display:flex; gap:10px; margin-top:20px;">
                            <button onclick="manualRepeat()" style="background:#334155;">Repeat Question</button>
                            <button onclick="manualNext()" style="background:#10b981;">Done Speaking / Next ➔</button>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                const videoElement = document.getElementById('userVideo');
                const camStatus = document.getElementById('camStatus');
                const micStatus = document.getElementById('micStatus');
                const qBox = document.getElementById('questionBox');
                
                let recognition;
                let currentQuestion = "";
                let isListening = false;
                
                // 1. Initialize Camera/Mic
                async function initMedia() {
                    try {
                        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                        videoElement.srcObject = stream;
                        camStatus.textContent = "Camera Active";
                        camStatus.classList.add("active");
                        micStatus.textContent = "Mic Active";
                        micStatus.classList.add("active");
                    } catch (err) {
                        console.warn("Media Error:", err);
                        camStatus.textContent = "Camera N/A (Simulation)";
                        camStatus.classList.add("error");
                        micStatus.textContent = "Mic N/A (Simulation)";
                        micStatus.classList.add("error");
                    }
                    
                    // Initialize Speech Recognition
                    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                        recognition = new SpeechRecognition();
                        recognition.continuous = false; // Stop after one sentence to process
                        recognition.interimResults = false;
                        recognition.lang = 'en-US';
                        
                        recognition.onresult = function(event) {
                            const transcript = event.results[0][0].transcript.toLowerCase();
                            console.log("User said:", transcript);
                            processAnswer(transcript);
                        };
                        
                        recognition.onend = function() {
                            if (isListening) recognition.start(); // Restart if still in listening mode
                        };
                        
                        recognition.onerror = function(event) {
                            console.error("Speech Error:", event.error);
                        };
                    } else {
                        alert("Your browser does not support Speech Recognition. Please use Chrome/Edge.");
                    }
                }
                
                window.onload = initMedia;

                // 2. Start Logic
                function startInterview() {
                    const type = document.getElementById('interviewType').value;
                    const setupDiv = document.getElementById('setup-stage');
                    const interviewDiv = document.getElementById('interview-stage');
                    
                    setupDiv.style.display = 'none';
                    interviewDiv.style.display = 'block';
                    
                    // Set initial question
                    if(type === 'aws') currentQuestion = "Welcome. Let's start with AWS. Can you explain the difference between latency-based routing and geolocation routing in Route 53?";
                    else if(type === 'devops') currentQuestion = "Hello. In a DevOps lifecycle, how do you handle rollback strategies during a failed deployment?";
                    else if(type === 'linux') currentQuestion = "Hi. Describe the boot process of a Linux system from BIOS to the login prompt.";
                    else currentQuestion = "Welcome. Explain the purpose of a ReplicaSet vs a Deployment in Kubernetes.";
                    
                    speakAndListen(currentQuestion);
                }
                
                function speakAndListen(text) {
                    qBox.textContent = text;
                    qBox.style.color = "#fff";
                    document.getElementById('scorePanel').style.display = 'none';
                    isListening = false;
                    if(recognition) recognition.stop();
                    
                    if ('speechSynthesis' in window) {
                        const utterance = new SpeechSynthesisUtterance(text);
                        utterance.onend = function() {
                            // Start listening after speaking
                            qBox.innerHTML += "<br><br><span style='color:#10b981'>[Listening...]</span>";
                            isListening = true;
                            if(recognition) recognition.start();
                        };
                        window.speechSynthesis.speak(utterance);
                    }
                }
                
                function manualRepeat() { speakAndListen(currentQuestion); }
                function manualNext() { processAnswer("Manual submission"); }

                function processAnswer(text) {
                    isListening = false;
                    if(recognition) recognition.stop();
                    document.getElementById('statusTag').textContent = "Analyzing Response...";
                    
                    setTimeout(() => {
                        const score = Math.floor(Math.random() * (10 - 7 + 1)) + 7;
                        const feedback = [
                            "Solid explanation of the core concepts.",
                            "Good understanding, but could be more concise.",
                            "Excellent technical depth mentioned.",
                            "Correct. You covered the key aspects well."
                        ];
                        const fb = feedback[Math.floor(Math.random() * feedback.length)];
                        
                        document.getElementById('scoreValue').textContent = score + "/10";
                        document.getElementById('scoreFeedback').textContent = fb;
                        document.getElementById('scorePanel').style.display = 'block';
                        
                        setTimeout(() => {
                            const followUps = [
                                "Interesting. How would you scale that solution?",
                                "What about the security implications?",
                                "Can you give a real-world scenario for this?",
                                "Let's move on. How do you monitor this system?"
                            ];
                            const nextQ = followUps[Math.floor(Math.random() * followUps.length)];
                            currentQuestion = nextQ;
                            speakAndListen(nextQ);
                        }, 4000);
                        
                    }, 1500);
                }
            </script>
            <style>
            @keyframes pulse {
                0% { transform: translateX(-100%); }
                100% { transform: translateX(100%); }
            }
            </style>
        </body>
        </html>
        """
        return html

    @app.route("/skill-analyzer/linux-test")
    def linux_test_legacy():
        return redirect(url_for('cloud_devops_module_detail', module_id='linux'))

    @app.route("/skill-analyzer/live-test")
    def live_test_hub():
        # Child Page: Shows specific tests (Cloud, DevOps, Linux, Others)
        try:
            from .Skill_test.cloud_devops_test.cloud_devops_test import DEVOPS_CONTENT_SUB
            from .Skill_test.Skill_anlz_test_sujects import ( 
                LINUX_TEST_CONTENT, 
                OTHERS_TEST_CONTENT
            )
            modules = [DEVOPS_CONTENT_SUB, LINUX_TEST_CONTENT, OTHERS_TEST_CONTENT]
        except ImportError:
            modules = []

        html = """
        {% raw %}
        <style>
             /* Reusing styles from parent page with adjustments for 4-column layout */
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
            
            .sa-header {
                background: linear-gradient(-45deg, #0f172a, #334155); 
                padding: 40px 20px; /* Reduced padding */
                border-radius: 24px;
                text-align: center;
                color: #fff;
                margin-bottom: 30px;
            }
            .sa-title {
                font-family: 'Outfit', sans-serif;
                font-size: 2.2rem; /* Slightly smaller title */
                font-weight: 800;
                background: linear-gradient(to right, #ffffff, #cbd5e1);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .sa-modules-container {
                display: grid;
                /* Force 4 columns on large screens, auto-wrap on smaller */
                grid-template-columns: repeat(3, 1fr); 
                gap: 20px; /* Reduced gap */
                max-width: 1200px; /* Increased width to fit 4 comfortably */
                margin: 0 auto;
                padding: 0 20px;
            }
            @media (max-width: 1200px) {
                .sa-modules-container {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
            @media (max-width: 768px) {
                .sa-modules-container {
                    grid-template-columns: 1fr;
                }
            }

            .sa-card {
                background: #fff;
                border-radius: 16px; /* Slightly smaller radius */
                border: 1px solid #e2e8f0;
                padding: 20px; /* Reduced padding */
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                display: flex; flex-direction: column; align-items: center; text-align: center; height: 100%;
                transition: transform 0.2s;
            }
            .sa-card:hover { transform: translateY(-5px); border-color:#3b82f6; }
            
            .sa-icon-box {
                width: 65px; height: 65px; /* Reduced size */
                border-radius: 50%; background: #f8fafc;
                display: flex; align-items: center; justify-content: center;
                margin-bottom: 15px; overflow: hidden; border: 1px solid #f1f5f9;
            }
            .sa-icon-box img { width: 80%; height: 80%; object-fit: contain; }
            
            .sa-card h2 { 
                font-family: 'Outfit', sans-serif; 
                color: #1e293b; 
                font-size: 1.3rem; /* Smaller heading */
                margin-bottom: 8px; 
                font-weight: 700; 
                line-height: 1.2;
            }
            .sa-card p { 
                color: #64748b; 
                font-size: 0.9rem; 
                margin-bottom: 16px; 
                flex-grow: 1; 
                line-height: 1.4;
            }
            .sa-btn {
                background: #0f172a; color: #fff; padding: 10px 20px; border-radius: 8px;
                text-decoration: none; font-weight: 600; display: block; width: 100%; box-sizing: border-box; margin-top: auto;
                font-size: 0.95rem;
            }
            .sa-btn:hover { background: #334155; }
            
            .sa-features { list-style: none; padding: 0; margin: 0 0 16px 0; text-align: left; width: 100%; }
            .sa-features li { 
                margin-bottom: 6px; 
                color: #475569; 
                display: flex; 
                align-items: center; 
                gap: 8px; 
                font-size: 0.85rem; 
            }
            .sa-features li::before { content: '✓'; color: #10b981; font-weight: bold; }
        </style>
        {% endraw %}
        
        <div style="font-family: 'Inter', sans-serif; padding-bottom: 40px;">
            <div class="sa-header">
                <h1 class="sa-title">Select Assessment Type</h1>
                <div style="margin-top:10px; color:#94a3b8;"><a href="{{ url_for('skill_selection') }}" style="color:#cbd5e1;text-decoration:none;">← Back to Main</a></div>
            </div>

            <div class="sa-modules-container">
                {% for module in modules %}
                <div class="sa-card">
                    <div class="sa-icon-box">
                        <img src="{{ url_for('image_file', filename=module['image']) }}" alt="{{ module['title'] }}">
                    </div>
                    <h2>{{ module['title'] }}</h2>
                    <p>{{ module['description'] }}</p>
                    {% if module.get('features') %}
                    <ul class="sa-features">
                        {% for feature in module['features'] %}
                        <li>{{ feature }}</li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                    <a href="{{ module.get('route', '#') }}" class="sa-btn">{{ module['action_label'] }}</a>
                </div>
                {% endfor %}
            </div>
        </div>
        """
        return render_page_func(html, active="skill-analyzer", modules=modules)








    @app.route("/skill-analyzer/cloud-devops-test/<module_id>")
    def cloud_devops_module_detail(module_id):
        # Shows details for a specific module (AWS, Azure, GCP, DevOps)
        try:
            from .Skill_test.cloud_devops_test.cloud_devops_test import (
                AWS_CONTENT,
                AZURE_CONTENT,
                GCP_CONTENT,
                DEVOPS_CONTENT_SUB
            )
            from .Skill_test.linux_test.linux_test import LINUX_TEST_CONTENT

            # Find the matching module
            module = None
            if module_id == 'aws': module = AWS_CONTENT
            elif module_id == 'azure': module = AZURE_CONTENT
            elif module_id == 'gcp': module = GCP_CONTENT
            elif module_id == 'devops': module = DEVOPS_CONTENT_SUB
            elif module_id == 'linux': module = LINUX_TEST_CONTENT
            
            if not module:
                 return render_page_func("<h2>Module not found</h2><p>Invalid module ID.</p>", active="skill-analyzer")

        except ImportError:
             return render_page_func("<h2>Error loading modules</h2>", active="skill-analyzer")

        html = """
        {% raw %}
        <style>
             @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');
             
             .cert-container {
                 max-width: 1200px;
                 margin: 0 auto;
                 padding: 40px 20px;
                 font-family: 'Outfit', sans-serif;
             }
             
             .cert-header {
                 text-align: center;
                 margin-bottom: 50px;
             }
             .cert-header h1 {
                 font-size: 2.5rem;
                 color: #1e293b;
                 margin-bottom: 10px;
             }
             
             .category-section {
                 margin-bottom: 60px;
             }
             .category-title {
                 font-size: 1.8rem;
                 font-weight: 700;
                 color: #334155;
                 margin-bottom: 30px;
                 text-align: center; /* Or left aligned if preferred */
                 border-bottom: 2px solid #e2e8f0;
                 padding-bottom: 10px;
                 display: inline-block;
                 width: 100%;
             }
             
             .cert-list {
                 display: flex;
                 flex-wrap: wrap;
                 justify-content: center;
                 gap: 40px;
             }
             
             .cert-card {
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 transition: transform 0.3s ease;
                 cursor: pointer;
                 text-decoration: none; 
             }
             .cert-card:hover {
                 transform: scale(1.08);
             }
             
             .cert-icon {
                 width: 100%;
                 max-width: 180px; /* Reduced from 350px per user request */
                 height: auto;
                 display: flex;
                 align-items: center;
                 justify-content: center;
             }
             
             .cert-icon img {
                 width: 100%;
                 height: auto;
                 object-fit: contain;
                 filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));
             }
             
        </style>
        {% endraw %}
        
        <div class="cert-container">
            <div style="margin-bottom:20px;"><a href="{{ url_for('live_test_hub') }}" style="color:#64748b;text-decoration:none;font-weight:600;">← Back to Assessments</a></div>
            
            <div class="cert-header">
                <h1>{{ module['title'] }}</h1>
                <p style="color:#64748b; font-size:1.1rem;">{{ module['description'] }}</p>
            </div>
            
            {% if module.get('certifications') %}
                {% set current_category = namespace(value=None) %}
                
                {% for cert in module['certifications'] %}
                    {% if current_category.value != cert.get('category' ) %}
                        {% if current_category.value is not none %}
                            </div> <!-- Close previous list -->
                            </div> <!-- Close previous section -->
                        {% endif %}
                        
                        <div class="category-section">
                            <h2 class="category-title">{{ cert.get('category') }}</h2>
                            <div class="cert-list">
                        {% set current_category.value = cert.get('category') %}
                    {% endif %}
                    
                    {% if cert.get('link') %}
                        <a href="{{ cert['link'] }}" target="_blank" class="cert-card" title="Open {{ cert['name'] }}">
                    {% else %}
                        <a href="{{ url_for('skill_registration', next=url_for('take_test', test_code=cert['code'])) }}" target="_blank" class="cert-card" title="Start {{ cert['name'] }}">
                    {% endif %}
                        <div class="cert-icon">
                             <img src="{{ url_for('image_file', filename=cert.get('image', 'cloud_logo_new.png')) }}" alt="{{ cert['name'] }}">
                        </div>
                    </a>
                {% endfor %}
                
                {% if current_category.value is not none %}
                    </div> <!-- Close last list -->
                    </div> <!-- Close last section -->
                {% endif %}
                
            {% else %}
                <div style="text-align:center; padding:40px; color:#64748b;">
                    <p>No specific certifications listed for this module yet.</p>
                </div>
            {% endif %}
        </div>
        """
        return render_page_func(html, active="skill-analyzer", module=module)

    @app.route("/skill-analyzer/take-test/<test_code>")
    def take_test(test_code):
        # Map test codes to their backend modules
        # For now, we only have the AWS Cloud Practitioner one fully built
        import importlib
        
        # Mapping logic (could be moved to a dict if it grows)
        module_path = None
        
        # AWS
        if test_code in ['CLF-C01', 'CLF-C02']:
            module_path = 'SkillAnalyzer.Skill_test.cloud_devops_test.AWS.aws_cloud_practitioner'
        elif test_code == 'SAA-C03':
            module_path = 'SkillAnalyzer.Skill_test.cloud_devops_test.AWS.aws_solutions_architect'
        # Add others as they are built...
        
        if module_path:
            try:
                mod = importlib.import_module(module_path)
                importlib.reload(mod)
                if hasattr(mod, 'render'):
                    # Exam Mode: Render directly without site layout
                    from flask import render_template_string
                    return render_template_string(mod.render())
            except Exception as e:
                import traceback
                tb = traceback.format_exc()
                error_html = f"""
                <!doctype html>
                <html lang="en">
                <head><title>Error</title>
                <style>body{{margin:0;padding:40px;text-align:center;font-family:sans-serif;background-color:#0ea5e9;background-image:linear-gradient(180deg,#38bdf8 0%,#bae6fd 100%);color:#fff;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;}} pre{{background:rgba(0,0,0,0.2);padding:20px;border-radius:10px;text-align:left;max-width:800px;overflow:auto;}}</style>
                </head>
                <body><h1>Error Loading Test</h1><p>We encountered an issue loading the exam module.</p><pre>{tb}</pre></body></html>
                """
                from flask import render_template_string
                return render_template_string(error_html)
        
        fallback_html = f"""
        <!doctype html>
        <html lang="en">
        <head><title>Test Not Available</title>
        <style>body{{margin:0;padding:40px;text-align:center;font-family:sans-serif;background-color:#0ea5e9;background-image:linear-gradient(180deg,#38bdf8 0%,#bae6fd 100%);color:#fff;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;}}</style>
        </head>
        <body><h1>Test Not Available</h1><p>The practice test for <strong>{test_code}</strong> is currently being initialized.</p><p>Please check back soon!</p></body></html>
        """
        from flask import render_template_string
        return render_template_string(fallback_html)
