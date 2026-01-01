from flask import url_for, session, render_template_string
import json

def render():
    user_info = session.get('user_info', {'name': 'Candidate'})
    
    # 65 Questions for SAA-C03
    # We define the first 10 Real Questions, then generate placeholders to reach 65.
    
    questions_list = [
            {
                "id": 1,
                "question": "A company wants to host a web application on EC2 instances behind an Application Load Balancer. The app needs to be highly available and resilient to AZ failures. Which architecture meets these requirements?",
                "options": [
                    "Launch EC2 instances in a single AZ and enable Auto Scaling.",
                    "Launch EC2 instances in multiple AZs and configure the ALB to route traffic to them.",
                    "Launch EC2 instances in multiple AZs and use Route 53 to load balance.",
                    "Use a single EC2 instance with a large instance type in one AZ."
                ],
                "correct": 1,
                "category": "Architecture",
                "explanation": "ALB distributes traffic across multiple targets (EC2) in multiple Availability Zones, ensuring high availability."
            },
            {
                "id": 2,
                "question": "A solution architect needs to design a storage solution for a data lake that will store petabytes of data. The data will be accessed infrequently but must be retrieved immediately when needed. Which storage class is most cost-effective?",
                "options": [
                    "S3 Standard",
                    "S3 Intelligent-Tiering",
                    "S3 Standard-IA",
                    "S3 Glacier Deep Archive"
                ],
                "correct": 2,
                "category": "Storage",
                "explanation": "S3 Standard-IA is for data accessed infrequently but requires rapid access when needed. Glacier is cheaper but has retrieval delay."
            },
            {
                "id": 3,
                "question": "A company requires a relational database that supports a high volume of read traffic. The database must be fully managed and support automatic failover. Which solution should be used?",
                "options": [
                    "Install MySQL on EC2 instances with EBS replication.",
                    "Use Amazon RDS for MySQL with Read Replicas and Multi-AZ enabled.",
                    "Use Amazon DynamoDB with DynamoDB Accelerator (DAX).",
                    "Use Amazon Redshift for transaction processing."
                ],
                "correct": 1,
                "category": "Database",
                "explanation": "Amazon RDS Multi-AZ provides failover, and Read Replicas handle high read traffic."
            },
            {
                "id": 4,
                "question": "A team needs to decouple a monolithic application into microservices using a message queue. The order of messages must be preserved strictly. Which service should they use?",
                "options": [
                    "Amazon SQS Standard Queue",
                    "Amazon SNS",
                    "Amazon SQS FIFO Queue",
                    "Amazon Kinesis Data Streams"
                ],
                "correct": 2,
                "category": "App Integration",
                "explanation": "SQS FIFO (First-In-First-Out) queues preserve the exact order of messages."
            },
            {
                "id": 5,
                "question": "An application needs to store user session data. The data must be accessible with single-digit millisecond latency. Which AWS service is best suited?",
                "options": [
                    "Amazon S3",
                    "Amazon RDS",
                    "Amazon DynamoDB",
                    "Amazon EFS"
                ],
                "correct": 2,
                "category": "Database",
                "explanation": "DynamoDB provides single-digit millisecond latency at any scale and is ideal for key-value session data."
            },
            {
                "id": 6,
                "question": "A company needs to analyze log data stored in S3 using standard SQL queries without loading it into a database. Which service should they use?",
                "options": [
                    "Amazon Redshift",
                    "Amazon Athena",
                    "Amazon QuickSight",
                    "Amazon EMR"
                ],
                "correct": 1,
                "category": "Analytics",
                "explanation": "Amazon Athena allows you to query data directly in S3 using SQL."
            },
            {
                "id": 7,
                "question": "Which AWS service can be used to monitor the performance of an application running on EC2 instances and set alarms?",
                "options": [
                    "AWS CloudTrail",
                    "Amazon CloudWatch",
                    "AWS Config",
                    "AWS Systems Manager"
                ],
                "correct": 1,
                "category": "Management",
                "explanation": "CloudWatch monitors resources and applications, collects metrics, and handles alarms."
            },
            {
                "id": 8,
                "question": "A company requires a file system that is accessible from multiple EC2 instances across multiple Availability Zones concurrently. Which service should be used?",
                "options": [
                    "Amazon EBS",
                    "Amazon EFS",
                    "Amazon S3",
                    "Instance Store"
                ],
                "correct": 1,
                "category": "Storage",
                "explanation": "Amazon EFS provides a scalable file system for Linux-based workloads that can be accessed by multiple instances across AZs."
            },
            {
                "id": 9,
                "question": "You need to store objects that must be immutable (cannot be overwritten or deleted) for a fixed amount of time for compliance. What should you use?",
                "options": [
                    "S3 Versioning",
                    "S3 Object Lock",
                    "S3 Lifecycle Policies",
                    "S3 Encryption"
                ],
                "correct": 1,
                "category": "Security",
                "explanation": "S3 Object Lock prevents objects from being deleted or overwritten effectively making them immutable."
            },
            {
                "id": 10,
                "question": "A company needs to distribute static content globally with low latency. Which service should they use?",
                "options": [
                    "Amazon Route 53",
                    "Amazon CloudFront",
                    "AWS Global Accelerator",
                    "Amazon S3 Transfer Acceleration"
                ],
                "correct": 1,
                "category": "Network",
                "explanation": "Amazon CloudFront is a CDN that caches static content at Edge Locations closer to users."
            }
    ]
    
    # Fill remaining questions to reach 65
    topics = ["Amazon EC2 Auto Scaling", "Amazon S3 Glacier", "Amazon RDS Multi-AZ", "AWS Transit Gateway", "AWS IAM Roles", "Amazon DynamoDB Streams", "AWS Lambda", "Amazon CloudFront", "AWS Shield", "Amazon Aurora"];
    for i in range(11, 66):
        topic = topics[i % len(topics)]
        questions_list.append({
            "id": i,
            "question": f"Scenario {i}: A company is designing a highly available architecture. The solution requires the use of {topic} to handle unpredictable traffic spikes and ensure data durability. Which configuration meets these requirements?",
            "options": [
                f"Configure {topic} with a standard retention policy.", 
                f"Deploy {topic} across multiple Availability Zones with automatic failover.", 
                f"Use {topic} in a single region to minimize latency.", 
                f"Integrate {topic} with on-premises legacy systems."
            ],
            "correct": 1,
            "category": "Architecture",
            "explanation": f"Deploying {topic} across multiple AZs ensures high availability and resilience."
        })

    EXAM_INFO = {
        "title": "AWS Certified Solutions Architect – Associate",
        "code": "SAA-C03",
        "duration_minutes": 130,
        "passing_score": 72,
        "total_questions": 65,
        "questions": questions_list
    }

    exam_json = json.dumps(EXAM_INFO)
    user_name = user_info.get('name', 'Candidate')

    # This template is cloned from aws_cloud_practitioner.py logic (CLF-C02)
    # Applied to SAA-C03 data.
    
    HTML_TEMPLATE = """
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        :root {
            --primary: #FF9900; /* AWS Orange */
            --primary-dark: #FF9900; 
            --bg-glass: rgba(255, 255, 255, 0.95);
            --text-dark: #232F3E; /* AWS Dark Blue */
            --text-light: #5d6c7b;
            --success: #10b981;
            --error: #ef4444;
        }

        .test-interface-wrapper {
            font-family: 'Outfit', sans-serif;
            max-width: 1000px;
            margin: 40px auto;
            color: var(--text-dark);
            position: relative;
        }

        /* --- Header / Timer Bar --- */
        .test-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #232F3E;
            color: #fff;
            padding: 15px 30px;
            border-radius: 16px 16px 0 0;
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.3);
            position: sticky;
            top: 20px;
            z-index: 50;
        }
        
        .test-title h2 { margin: 0; font-size: 1.2rem; font-weight: 600; letter-spacing: 0.5px; }
        .test-title span { font-size: 0.9rem; opacity: 0.8; font-weight: 400; }

        .timer-box {
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(255,255,255,0.1);
            padding: 8px 16px;
            border-radius: 8px;
            font-variant-numeric: tabular-nums;
            font-weight: 700;
            font-size: 1.1rem;
            color: #FF9900;
            border: 1px solid rgba(255, 153, 0, 0.3);
        }
        
        /* --- Main Content Area --- */
        .test-body {
            background: #fff;
            border: 1px solid #e2e8f0;
            border-top: none;
            border-radius: 0 0 16px 16px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
            min-height: 400px;
            position: relative;
        }

        /* Progress Bar */
        .progress-container {
            margin-bottom: 30px;
        }
        .progress-labels {
            display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-light); margin-bottom: 8px;
        }
        .progress-track {
            height: 8px;
            background: #f1f5f9;
            border-radius: 4px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #FF9900, #F58536);
            width: 0%;
            transition: width 0.4s ease;
        }

        /* Question Card */
        .question-card {
            animation: fadeIn 0.4s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .q-header {
            font-size: 1.1rem;
            color: var(--text-light);
            margin-bottom: 10px;
            font-weight: 600;
        }
        
        .q-text {
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 30px;
            line-height: 1.4;
            color: #1a202c;
        }

        /* Options */
        .options-grid {
            display: grid;
            gap: 15px;
        }

        .option-btn {
            display: flex;
            align-items: center;
            padding: 18px 25px;
            background: #f8fafc;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 1.05rem;
            color: #475569;
            text-align: left;
            position: relative;
        }

        .option-btn:hover {
            border-color: #cbd5e1;
            background: #f1f5f9;
        }

        .option-btn.selected {
            border-color: #FF9900;
            background: #fff7ed; /* light orange tint */
            color: #c2410c;
        }
        
        .option-marker {
            width: 24px;
            height: 24px;
            border: 2px solid #cbd5e1;
            border-radius: 50%;
            margin-right: 15px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .option-btn.selected .option-marker {
            border-color: #FF9900;
            background: #FF9900;
        }
        
        .option-btn.selected .option-marker::after {
            content: '';
            width: 8px;
            height: 8px;
            background: #fff;
            border-radius: 50%;
        }

        /* Footer / Navigation */
        .test-footer {
            margin-top: 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #f1f5f9;
            padding-top: 30px;
        }

        .btn {
            padding: 12px 30px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s;
            border: none;
        }
        
        .btn-secondary {
            background: #f1f5f9;
            color: #64748b;
        }
        .btn-secondary:hover { background: #e2e8f0; }

        .btn-primary {
            background: #232F3E;
            color: #fff;
        }
        .btn-primary:hover {
            background: #374151;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        /* Results Modal */
        .modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(8px);
            display: flex; justify-content: center; align-items: center;
            z-index: 1000;
            opacity: 0; visibility: hidden;
            transition: all 0.3s ease;
        }
        .modal-overlay.active { opacity: 1; visibility: visible; }
        
        .result-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 24px;
            text-align: center;
            max-width: 900px; /* Wider */
            width: 95%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            border: 1px solid rgba(255,255,255,0.8);
            transform: scale(0.95);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .modal-overlay.active .result-card { transform: scale(1); }
        
        .result-header {
            display: flex; flex-direction: column; align-items: center; margin-bottom: 20px;
        }

        .score-circle {
            width: 120px; height: 120px;
            border-radius: 50%;
            background: conic-gradient(#0ea5e9 0%, #e2e8f0 0%); /* Dynamic updated via JS */
            margin: 0 auto 10px;
            display: flex; align-items: center; justify-content: center;
            position: relative;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
        .score-circle::before {
            content: '';
            position: absolute; width: 100px; height: 100px;
            background: #fff; border-radius: 50%;
        }
        .score-val {
            position: relative; font-size: 2.2rem; font-weight: 800; color: #0284c7; z-index: 2;
        }

        .result-body {
            display: flex;
            flex-wrap: wrap;
            gap: 25px;
            justify-content: center;
            align-items: flex-start;
            margin-bottom: 25px;
        }
        .chart-container {
            flex: 1;
            min-width: 320px;
            max-width: 450px;
            background: white;
            padding: 15px;
            border-radius: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        #skill-summary {
            flex: 1;
            min-width: 300px;
            text-align: left;
            background: white;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            max-height: 400px;
            overflow-y: auto;
        }
        
        /* Skill Items */
        .skill-item {
            display: flex; justify-content: space-between; align-items: center;
            padding: 8px 0; border-bottom: 1px solid #f1f5f9;
        }
        .skill-item:last-child { border-bottom: none; }
        .skill-name { font-weight: 500; color: #475569; font-size: 0.9rem; }
        .skill-val { font-weight: 600; font-size: 0.9rem; }
        
        .action-buttons {
             display: flex;
             justify-content: center;
             gap: 10px;
             flex-wrap: wrap;
             margin: 0 auto;
        }
        .action-buttons .btn {
            min-width: 140px;
             flex: 1;
             max-width: 200px;
        }

    </style>

    <div class="test-interface-wrapper">
        <!-- Header -->
        <div class="test-header">
            <div class="test-title">
                <h2>{{ exam.title }}</h2>
                <span>{{ exam.code }} | Practice Exam</span>
            </div>
            <div class="timer-box">
                <span id="timer-display">130:00</span>
            </div>
        </div>

        <!-- Body -->
        <div class="test-body">
            
            <!-- Progress -->
            <div class="progress-container">
                <div class="progress-labels">
                    <span id="q-counter">Question 1 of {{ exam.total_questions }}</span>
                    <span>Progress</span>
                </div>
                <div class="progress-track">
                    <div id="progress-bar" class="progress-fill" style="width: 0%"></div>
                </div>
            </div>

            <!-- Question Container -->
            <div id="question-container" class="question-card">
                <!-- Injected via JS -->
            </div>

            <!-- Footer -->
            <div class="test-footer">
                <button class="btn btn-secondary" onclick="prevQuestion()" id="btn-prev" disabled>Previous</button>
                <button class="btn btn-primary" onclick="nextQuestion()" id="btn-next">Next Question</button>
            </div>
        </div>
    </div>

    <!-- Result Modal -->
    <div class="modal-overlay" id="result-modal">
        <div class="result-card">
            <h2 style="margin-top:0; color:#1e293b;">Exam Completed!</h2>
            <div class="result-header">
                <div class="score-circle" id="score-circle">
                    <!-- Note: JS updates gradient background -->
                    <span class="score-val" id="score-val">0%</span>
                </div>
                <div id="score-msg" style="font-weight:800; font-size:1.8rem; margin-bottom:5px; color:#1e293b;"></div>
                <p style="color:#64748b; margin:0;">Here is your detailed performance breakdown.</p>
            </div>
            
            <div class="result-body">
                <div class="chart-container">
                    <canvas id="skillChart"></canvas>
                </div>
                <div id="skill-summary">
                    <!-- JS Injected Content -->
                </div>
            </div>
            
            <div class="action-buttons">
                <button class="btn btn-primary" onclick="window.location.reload()">Retake Exam</button>
                <button class="btn btn-secondary" onclick="window.history.back()">Exit</button>
                <button class="btn btn-info" onclick="downloadCertificate()" style="background-color:#3b82f6; color:white;">Download Certificate 🎖️</button>
                <button class="btn btn-success" onclick="downloadExamPaper()" style="background-color:#10b981; color:white;">Download Report 📄</button>
            </div>
        </div>
    </div>

    <script>
        const EXAM_DATA = {{ exam_json|safe }};
        let currentQ = 0;
        let answers = new Array(EXAM_DATA.questions.length).fill(null);
        let timeLeft = EXAM_DATA.duration_minutes * 60; // in seconds
        let finalScore = 0;


        // Timer Logic
        function startTimer() {
            const display = document.getElementById('timer-display');
            const timer = setInterval(() => {
                if (timeLeft <= 0) {
                    clearInterval(timer);
                    submitExam();
                    return;
                }
                timeLeft--;
                const m = Math.floor(timeLeft / 60);
                const s = timeLeft % 60;
                display.textContent = `${m}:${s < 10 ? '0' : ''}${s}`;
            }, 1000);
        }

        function renderQuestion(idx) {
            const q = EXAM_DATA.questions[idx];
            const container = document.getElementById('question-container');
            
            // Build Options HTML
            let optionsHtml = '<div class="options-grid">';
            q.options.forEach((opt, i) => {
                const isSelected = answers[idx] === i ? 'selected' : '';
                optionsHtml += `
                    <div class="option-btn ${isSelected}" onclick="selectOption(${i})">
                        <div class="option-marker"></div>
                        <span>${opt}</span>
                    </div>
                `;
            });
            optionsHtml += '</div>';

            container.innerHTML = `
                <div class="q-header">Question ${idx + 1}</div>
                <div class="q-text">${q.question}</div>
                ${optionsHtml}
            `;

            // Update UI state
            document.getElementById('q-counter').textContent = `Question ${idx + 1} of ${EXAM_DATA.questions.length}`;
            document.getElementById('progress-bar').style.width = `${((idx + 1) / EXAM_DATA.questions.length) * 100}%`;
            
            document.getElementById('btn-prev').disabled = idx === 0;
            document.getElementById('btn-next').textContent = idx === EXAM_DATA.questions.length - 1 ? 'Finish & Submit' : 'Next Question';
        }

        function selectOption(optIdx) {
            answers[currentQ] = optIdx;
            renderQuestion(currentQ); // Re-render to update selected style
        }

        function nextQuestion() {
            if (currentQ < EXAM_DATA.questions.length - 1) {
                currentQ++;
                renderQuestion(currentQ);
            } else {
                submitExam();
            }
        }

        function prevQuestion() {
            if (currentQ > 0) {
                currentQ--;
                renderQuestion(currentQ);
            }
        }

        function submitExam() {
            // Calculate Score
            let correct = 0;
            EXAM_DATA.questions.forEach((q, i) => {
                if (answers[i] === q.correct) correct++;
            });
            
            const scorePct = Math.round((correct / EXAM_DATA.questions.length) * 100);
            finalScore = scorePct;

            
            // Show Result
            document.getElementById('result-modal').classList.add('active');
            document.getElementById('score-val').textContent = `${scorePct}%`;
            
            const msg = document.getElementById('score-msg');
            const circle = document.getElementById('score-circle');
            
            // Update Circle Gradient
            circle.style.background = `conic-gradient(${scorePct >= 72 ? '#10b981' : '#ef4444'} ${scorePct}%, #e2e8f0 ${scorePct}%)`;
            
            if (scorePct >= 72) {
                msg.textContent = "Congratulations! You Passed.";
                msg.style.color = "#10b981";
            } else {
                msg.textContent = "Keep practicing. You got this!";
                msg.style.color = "#ef4444";
            }
            
            startSkillAnalysis();
        }

        function startSkillAnalysis() {
            // Calculate Category Scores
            const categories = {};
            EXAM_DATA.questions.forEach((q, i) => {
                const cat = q.category || "General";
                if (!categories[cat]) categories[cat] = { total: 0, correct: 0 };
                categories[cat].total++;
                if (answers[i] === q.correct) categories[cat].correct++;
            });

            const labels = Object.keys(categories);
            const data = labels.map(l => Math.round((categories[l].correct / categories[l].total) * 100));

            // Render Radar Chart
            const ctx = document.getElementById('skillChart').getContext('2d');
            
            new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Skill Proficiency (%)',
                        data: data,
                        fill: true,
                        backgroundColor: 'rgba(255, 153, 0, 0.2)',
                        borderColor: '#FF9900',
                        pointBackgroundColor: '#FF9900',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: '#FF9900'
                    }]
                },
                options: {
                    elements: { line: { borderWidth: 3 } },
                    scales: { r: { min: 0, max: 100, ticks: { stepSize: 20 } } }
                }
            });

            // Summary Text
            let summaryHTML = "<strong>Skill Breakdown</strong>";
            labels.forEach((l, i) => {
                const score = data[i];
                let qual = score >= 80 ? "Strong" : (score >= 50 ? "Average" : "Weak");
                let color = score >= 80 ? "#10b981" : (score >= 50 ? "#f59e0b" : "#ef4444");
                summaryHTML += `
                <div class="skill-item">
                    <span class="skill-name">${l}</span>
                    <span class="skill-val" style="color:${color}">${score}% (${qual})</span>
                </div>`;
            });
            document.getElementById('skill-summary').innerHTML = summaryHTML;
        }

        function downloadCertificate() {
            if (finalScore < 72) {
                alert("You must pass the exam (72%+) to download the certificate.");
                return;
            }
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/skill-analyzer/download-certificate';
            
            const fields = {
                'exam_code': 'SAA-C03',
                'score': finalScore,
                'passed': true // verified by check above
            };
            
            for (const key in fields) {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = key;
                input.value = fields[key];
                form.appendChild(input);
            }
            
            document.body.appendChild(form);
            form.submit();
            document.body.removeChild(form);
        }

        function downloadExamPaper() {
            let correct = 0;
            const questionData = EXAM_DATA.questions.map((q, i) => {
                if (answers[i] === q.correct) correct++;
                return {
                    question: q.question,
                    options: q.options,
                    user_idx: answers[i],
                    correct_idx: q.correct,
                    explanation: q.explanation
                };
            });
            const scorePct = Math.round((correct / EXAM_DATA.questions.length) * 100);
            finalScore = scorePct; // Update global score

            // Capture the graph image from canvas
            // Use try-catch for canvas data retrieval
            let graphImg = null;
            try {
                const chartCanvas = document.getElementById('skillChart');
                graphImg = chartCanvas ? chartCanvas.toDataURL('image/png') : null;
            } catch(e) {
                console.error("Graph capture failed", e);
            }
            const summaryText = document.getElementById('skill-summary').innerText;

            const payload = {
                user_name: {{ user_name|tojson }}, 
                exam_title: EXAM_DATA.title,
                score: scorePct,
                passed: scorePct >= 72,
                questions: questionData,
                graph_image: graphImg,
                skill_summary: summaryText
            };

            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/skill-analyzer/download-result';
            
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'exam_data';
            input.value = JSON.stringify(payload);
            
            form.appendChild(input);
            document.body.appendChild(form);
            form.submit();
        }

        // Init
        renderQuestion(0);
        startTimer();

    </script>
    """
    
    return render_template_string(HTML_TEMPLATE, exam=EXAM_INFO, exam_json=exam_json, user_name=user_name)
