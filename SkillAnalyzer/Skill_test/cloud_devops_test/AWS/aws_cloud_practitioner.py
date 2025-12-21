
# aws_cloud_practitioner.py
# Backend Content & Interface for AWS Certified Cloud Practitioner (CLF-C01) Practice Test

from flask import url_for
import json

EXAM_INFO = {
    "title": "AWS Certified Cloud Practitioner",
    "code": "CLF-C01",
    "description": "Validate your overall understanding of the AWS Cloud platform.",
    "duration_minutes": 90,
    "questions": [
        {
            "id": 1,
            "question": "Which AWS service is used to deploy and manage applications in the cloud without worrying about the infrastructure?",
            "options": [
                "Amazon EC2",
                "AWS Elastic Beanstalk",
                "AWS Lambda",
                "Amazon RDS"
            ],
            "correct": 1,
            "explanation": "AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services. You simply upload your code and Elastic Beanstalk automatically handles the deployment."
        },
        {
            "id": 2,
            "question": "What is the primary benefit of using AWS Regions?",
            "options": [
                "To reduce the cost of services",
                "To improved data security and compliance",
                "To allow for global data replication automatically",
                "To ensure lower latency for end-users"
            ],
            "correct": 3,
            "explanation": "Regions allow you to deploy applications closer to your end-users to reduce latency."
        },
        {
            "id": 3,
            "question": "Which service should a company use to monitor the health and performance of their AWS resources?",
            "options": [
                "AWS CloudTrail",
                "Amazon CloudWatch",
                "AWS Config",
                "Amazon Inspector"
            ],
            "correct": 1,
            "explanation": "Amazon CloudWatch provides monitoring for applications, responding to system-wide performance changes, optimizing resource utilization, and getting a unified view of operational health."
        },
        {
            "id": 4,
            "question": "A company requires a durable storage solution for static content (images, videos) that can be accessed from a website. Which service meets this requirement?",
            "options": [
                "Amazon EBS",
                "Amazon S3",
                "Amazon EFS",
                "Amazon Glacier"
            ],
            "correct": 1,
            "explanation": "Amazon Simple Storage Service (S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. It is ideal for static web content."
        },
        {
            "id": 5,
            "question": "Which AWS pricing model allows you to pay for compute capacity by the hour or second with no long-term commitments?",
            "options": [
                "Reserved Instances",
                "Spot Instances",
                "On-Demand Instances",
                "Savings Plans"
            ],
            "correct": 2,
            "explanation": "On-Demand Instances let you pay for compute capacity by the hour or second with no long-term commitments."
        }
    ]
}

def render():
    """
    Renders the Timer-based MCQ Interface.
    """
    exam_json = json.dumps(EXAM_INFO)
    
    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        :root {{
            --primary: #FF9900; /* AWS Orange */
            --primary-dark: #FF9900; 
            --bg-glass: rgba(255, 255, 255, 0.95);
            --text-dark: #232F3E; /* AWS Dark Blue */
            --text-light: #5d6c7b;
            --success: #10b981;
            --error: #ef4444;
        }}

        .test-interface-wrapper {{
            font-family: 'Outfit', sans-serif;
            max-width: 1000px;
            margin: 40px auto;
            color: var(--text-dark);
            position: relative;
        }}

        /* --- Header / Timer Bar --- */
        .test-header {{
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
        }}
        
        .test-title h2 {{ margin: 0; font-size: 1.2rem; font-weight: 600; letter-spacing: 0.5px; }}
        .test-title span {{ font-size: 0.9rem; opacity: 0.8; font-weight: 400; }}

        .timer-box {{
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
        }}
        
        /* --- Main Content Area --- */
        .test-body {{
            background: #fff;
            border: 1px solid #e2e8f0;
            border-top: none;
            border-radius: 0 0 16px 16px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
            min-height: 400px;
            position: relative;
        }}

        /* Progress Bar */
        .progress-container {{
            margin-bottom: 30px;
        }}
        .progress-labels {{
            display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-light); margin-bottom: 8px;
        }}
        .progress-track {{
            height: 8px;
            background: #f1f5f9;
            border-radius: 4px;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #FF9900, #F58536);
            width: 0%;
            transition: width 0.4s ease;
        }}

        /* Question Card */
        .question-card {{
            animation: fadeIn 0.4s ease;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .q-header {{
            font-size: 1.1rem;
            color: var(--text-light);
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .q-text {{
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 30px;
            line-height: 1.4;
            color: #1a202c;
        }}

        /* Options */
        .options-grid {{
            display: grid;
            gap: 15px;
        }}

        .option-btn {{
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
        }}

        .option-btn:hover {{
            border-color: #cbd5e1;
            background: #f1f5f9;
        }}

        .option-btn.selected {{
            border-color: #FF9900;
            background: #fff7ed; /* light orange tint */
            color: #c2410c;
        }}
        
        .option-marker {{
            width: 24px;
            height: 24px;
            border: 2px solid #cbd5e1;
            border-radius: 50%;
            margin-right: 15px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .option-btn.selected .option-marker {{
            border-color: #FF9900;
            background: #FF9900;
        }}
        
        .option-btn.selected .option-marker::after {{
            content: '';
            width: 8px;
            height: 8px;
            background: #fff;
            border-radius: 50%;
        }}

        /* Footer / Navigation */
        .test-footer {{
            margin-top: 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #f1f5f9;
            padding-top: 30px;
        }}

        .btn {{
            padding: 12px 30px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s;
            border: none;
        }}
        
        .btn-secondary {{
            background: #f1f5f9;
            color: #64748b;
        }}
        .btn-secondary:hover {{ background: #e2e8f0; }}

        .btn-primary {{
            background: #232F3E;
            color: #fff;
        }}
        .btn-primary:hover {{
            background: #374151;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        
        /* Results Modal */
        .modal-overlay {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(5px);
            display: flex; justify-content: center; align-items: center;
            z-index: 1000;
            opacity: 0; visibility: hidden;
            transition: all 0.3s;
        }}
        .modal-overlay.active {{ opacity: 1; visibility: visible; }}
        
        .result-card {{
            background: #fff;
            padding: 50px;
            border-radius: 24px;
            text-align: center;
            max-width: 500px;
            width: 90%;
            transform: scale(0.95);
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}
        .modal-overlay.active .result-card {{ transform: scale(1); }}
        
        .score-circle {{
            width: 120px; height: 120px;
            border-radius: 50%;
            background: conic-gradient(var(--primary) 0%, #e2e8f0 0%);
            margin: 0 auto 30px;
            display: flex; align-items: center; justify-content: center;
            position: relative;
        }}
        .score-circle::before {{
            content: '';
            position: absolute; width: 100px; height: 100px;
            background: #fff; border-radius: 50%;
        }}
        .score-val {{
            position: relative; font-size: 2.5rem; font-weight: 800; color: #1e293b;
        }}
        .score-label {{ position: relative; font-size: 0.9rem; color: #64748b; margin-top:-5px;}}

    </style>

    <div class="test-interface-wrapper">
        <!-- Header -->
        <div class="test-header">
            <div class="test-title">
                <h2>AWS Certified Cloud Practitioner</h2>
                <span>CLF-C01 | Practice Exam</span>
            </div>
            <div class="timer-box">
                <span id="timer-display">90:00</span>
            </div>
        </div>

        <!-- Body -->
        <div class="test-body">
            
            <!-- Progress -->
            <div class="progress-container">
                <div class="progress-labels">
                    <span id="q-counter">Question 1 of 5</span>
                    <span>Progress</span>
                </div>
                <div class="progress-track">
                    <div id="progress-bar" class="progress-fill" style="width: 20%"></div>
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
            <p style="color:#64748b;">Here is your performance summary.</p>
            
            <div class="score-circle" id="score-circle">
                <div style="display:flex; flex-direction:column;">
                    <span class="score-val" id="score-val">0%</span>
                </div>
            </div>
            
            <div id="score-msg" style="font-weight:600; font-size:1.2rem; margin-bottom:30px;">
                <!-- Pass/Fail msg -->
            </div>
            
            <button class="btn btn-primary" onclick="window.location.reload()" style="width:100%">Retake Exam</button>
            <button class="btn btn-secondary" onclick="window.history.back()" style="width:100%; margin-top:10px;">Exit</button>
        </div>
    </div>

    <script>
        const EXAM_DATA = {exam_json};
        let currentQ = 0;
        let answers = new Array(EXAM_DATA.questions.length).fill(null);
        let timeLeft = EXAM_DATA.duration_minutes * 60; // in seconds

        // Timer Logic
        function startTimer() {{
            const display = document.getElementById('timer-display');
            const timer = setInterval(() => {{
                if (timeLeft <= 0) {{
                    clearInterval(timer);
                    submitExam();
                    return;
                }}
                timeLeft--;
                const m = Math.floor(timeLeft / 60);
                const s = timeLeft % 60;
                display.textContent = `${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
            }}, 1000);
        }}

        function renderQuestion(idx) {{
            const q = EXAM_DATA.questions[idx];
            const container = document.getElementById('question-container');
            
            // Build Options HTML
            let optionsHtml = '<div class="options-grid">';
            q.options.forEach((opt, i) => {{
                const isSelected = answers[idx] === i ? 'selected' : '';
                optionsHtml += `
                    <div class="option-btn ${{isSelected}}" onclick="selectOption(${{i}})">
                        <div class="option-marker"></div>
                        <span>${{opt}}</span>
                    </div>
                `;
            }});
            optionsHtml += '</div>';

            container.innerHTML = `
                <div class="q-header">Question ${{idx + 1}}</div>
                <div class="q-text">${{q.question}}</div>
                ${{optionsHtml}}
            `;

            // Update UI state
            document.getElementById('q-counter').textContent = `Question ${{idx + 1}} of ${{EXAM_DATA.questions.length}}`;
            document.getElementById('progress-bar').style.width = `${{((idx + 1) / EXAM_DATA.questions.length) * 100}}%`;
            
            document.getElementById('btn-prev').disabled = idx === 0;
            document.getElementById('btn-next').textContent = idx === EXAM_DATA.questions.length - 1 ? 'Finish & Submit' : 'Next Question';
        }}

        function selectOption(optIdx) {{
            answers[currentQ] = optIdx;
            renderQuestion(currentQ); // Re-render to update selected style
        }}

        function nextQuestion() {{
            if (currentQ < EXAM_DATA.questions.length - 1) {{
                currentQ++;
                renderQuestion(currentQ);
            }} else {{
                submitExam();
            }}
        }}

        function prevQuestion() {{
            if (currentQ > 0) {{
                currentQ--;
                renderQuestion(currentQ);
            }}
        }}

        function submitExam() {{
            // Calculate Score
            let correct = 0;
            EXAM_DATA.questions.forEach((q, i) => {{
                if (answers[i] === q.correct) correct++;
            }});
            
            const scorePct = Math.round((correct / EXAM_DATA.questions.length) * 100);
            
            // Show Result
            document.getElementById('result-modal').classList.add('active');
            document.getElementById('score-val').textContent = `${{scorePct}}%`;
            
            const msg = document.getElementById('score-msg');
            const circle = document.getElementById('score-circle');
            
            // Update Circle Gradient
            circle.style.background = `conic-gradient(${{scorePct >= 70 ? '#10b981' : '#ef4444'}} ${{scorePct}}%, #e2e8f0 ${{scorePct}}%)`;
            
            if (scorePct >= 70) {{
                msg.textContent = "Congratulations! You Passed.";
                msg.style.color = "#10b981";
            }} else {{
                msg.textContent = "Keep practicing. You got this!";
                msg.style.color = "#ef4444";
            }}
        }}

        // Init
        renderQuestion(0);
        startTimer();

    </script>
    """
