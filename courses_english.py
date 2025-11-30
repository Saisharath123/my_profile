# courses_english.py
# Spoken English & Corporate Etiquette module content
# Exposes: render() -> HTML string

LOCAL_CLOUD_IMG = "/mnt/data/51BC2F46-B035-4EC2-8054-C3A2697D6723.jpeg"

def render():
    return f"""
    <div style="display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start;">
      <div style="flex:0 0 420px; max-width:100%;">
        <img src="{LOCAL_CLOUD_IMG}" alt="english" style="width:100%;height:340px;object-fit:cover;border-radius:12px;box-shadow:0 12px 36px rgba(2,6,23,0.06);">
      </div>

      <div style="flex:1;min-width:260px;">
        <h1 style="margin-top:0;">Spoken English & Corporate Etiquette</h1>

        <p style="color:#6b7280;font-weight:700;font-size:15px;">
          Improve fluency, confidence and workplace communication — tailored for technical professionals.
        </p>

        <hr style="margin:18px 0;border:none;border-top:1px solid #e5e7eb;">

        <h2>🗣 Speaking & Pronunciation</h2>
        <ul style="line-height:1.6;font-weight:700;color:#374151;">
          <li>Pronunciation drills & phonetics tips</li>
          <li>Sentence stress, intonation and natural speech</li>
          <li>Fluency practice via roleplay and mock interviews</li>
        </ul>

        <h2 style="margin-top:12px;">🤝 Corporate Etiquette</h2>
        <ul style="line-height:1.6;font-weight:700;color:#374151;">
          <li>Email & meeting etiquette for global teams</li>
          <li>Presentation structure & storytelling for technical demos</li>
          <li>Interview strategies, group discussion and HR rounds</li>
        </ul>

        <h2 style="margin-top:12px;">🧪 Practice Sessions</h2>
        <ol style="line-height:1.6;font-weight:700;color:#374151;">
          <li>Weekly speaking challenges and feedback</li>
          <li>Mock interview with real-time corrections</li>
          <li>Recorded sessions for self-review and improvement</li>
        </ol>

        <div style="margin-top:14px;">
          <a class="btn" href="/contact">Contact / Enroll</a>
        </div>

        <p style="margin-top:12px;">
          <a href="/courses" style="text-decoration:underline;color:#0b5ed7;font-weight:800;">⬅ Back to Courses</a>
        </p>
      </div>
    </div>
    """

