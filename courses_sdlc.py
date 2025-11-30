# courses_sdlc.py
# SDLC & Release Management module content
# Exposes: render() -> HTML string

LOCAL_CLOUD_IMG = "/mnt/data/51BC2F46-B035-4EC2-8054-C3A2697D6723.jpeg"

def render():
    return f"""
    <div style="display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start;">
      <div style="flex:0 0 420px; max-width:100%;">
        <img src="{LOCAL_CLOUD_IMG}" alt="sdlc" style="width:100%;height:340px;object-fit:cover;border-radius:12px;box-shadow:0 12px 36px rgba(2,6,23,0.06);">
      </div>

      <div style="flex:1;min-width:260px;">
        <h1 style="margin-top:0;">SDLC & Release Management</h1>

        <p style="color:#6b7280;font-weight:700;font-size:15px;">
          Structured development lifecycle, release pipelines and QA practices for stable production delivery.
        </p>

        <hr style="margin:18px 0;border:none;border-top:1px solid #e5e7eb;">

        <h2>📐 SDLC Phases</h2>
        <ul style="line-height:1.6;font-weight:700;color:#374151;">
          <li>Requirements elicitation & stakeholder alignment</li>
          <li>Architecture & system design considerations</li>
          <li>Development best practices & code quality</li>
          <li>Testing strategies: unit, integration, E2E & automation</li>
          <li>Deployment strategies & rollback planning</li>
        </ul>

        <h2 style="margin-top:12px;">🔁 Release & Change Management</h2>
        <ul style="line-height:1.6;font-weight:700;color:#374151;">
          <li>Release pipelines, gating and approvals</li>
          <li>Feature toggles, canaries and blue-green deployments</li>
          <li>Post-deploy monitoring and SLO/SLI basics</li>
        </ul>

        <h2 style="margin-top:12px;">🧪 Labs & Templates</h2>
        <ol style="line-height:1.6;font-weight:700;color:#374151;">
          <li>Define a release checklist and runbook</li>
          <li>Automate release notes and changelog generation</li>
          <li>Simulate rollback scenarios and incident playbooks</li>
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

