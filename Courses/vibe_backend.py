from flask import url_for

def render():
    """
    Renders the detail page for Vibe Coding & Context Engineering.
    """
    return f"""
    <div style="max-width:900px; margin:0 auto; padding:20px;">
        <div style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); border-radius:16px; padding:40px; color:white; margin-bottom:30px; position:relative; overflow:hidden;">
            <div style="position:relative; z-index:2;">
                <h1 style="font-size:36px; font-weight:800; margin:0 0 10px 0;">Vibe Coding & Context Engineering</h1>
                <p style="font-size:18px; opacity:0.9; max-width:600px;">Master the art of building AI-driven web applications with modern frameworks and context-aware engineering.</p>
            </div>
            <!-- Decorative circle -->
            <div style="position:absolute; right:-50px; top:-50px; width:200px; height:200px; border-radius:50%; background:rgba(255,255,255,0.1);"></div>
        </div>

        <div style="display:grid; grid-template-columns: 2fr 1fr; gap:30px;">
            <div style="background:white; border-radius:12px; padding:24px; box-shadow:0 4px 12px rgba(0,0,0,0.05); border:1px solid #e5e7eb;">
                <h2 style="color:#111827; margin-top:0;">Course Overview</h2>
                <p style="color:#4b5563; line-height:1.6;">
                    In this comprehensive module, you will learn how to leverage Artificial Intelligence to build sophisticated web applications. 
                    We focus on "Context Engineering" — the skill of effectively structuring information for LLMs to generate high-quality code and content.
                </p>
                
                <h3 style="color:#111827;">Key Topics</h3>
                <ul style="color:#4b5563; line-height:1.6; padding-left:20px;">
                    <li>AI-Assisted Full Stack Development</li>
                    <li>Context Engineering Patterns</li>
                    <li>Integrating LLM APIs (Gemini, OpenAI)</li>
                    <li>Building "Vibe-Coded" UIs with Tailwind & React/Flask</li>
                    <li>Automated Code Generation Workflows</li>
                </ul>
            </div>

            <div style="display:flex; flex-direction:column; gap:20px;">
                <div style="background:white; border-radius:12px; padding:24px; box-shadow:0 4px 12px rgba(0,0,0,0.05); border:1px solid #e5e7eb;">
                    <h3 style="color:#111827; margin-top:0; font-size:18px;">Course Details</h3>
                    <div style="display:flex; justify-content:space-between; margin-bottom:12px; font-size:14px;">
                        <span style="color:#6b5563;">Level:</span>
                        <span style="font-weight:600; color:#111827;">Intermediate</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:12px; font-size:14px;">
                        <span style="color:#6b5563;">Duration:</span>
                        <span style="font-weight:600; color:#111827;">3 Weeks</span>
                    </div>
                    <div style="margin-top:20px;">
                        <a href="{url_for('contact')}" style="display:block; width:100%; text-align:center; background:#4f46e5; color:white; padding:12px; border-radius:8px; text-decoration:none; font-weight:600;">Enroll / Contact</a>
                    </div>
                </div>
            </div>
        </div>
        
        <div style="margin-top:30px;">
             <a href="{url_for('courses')}" style="color:#4f46e5; text-decoration:none; font-weight:600;">&larr; Back to Courses</a>
        </div>
    </div>
    """
