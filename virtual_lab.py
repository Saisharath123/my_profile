# virtual_lab.py
# Backend configuration for Virtual Linux Lab

LAB_CONFIG = {
    "hostname": "linux-vm",
    "user": "student",
    "initial_path": "~",
    "file_system": {
        "~": ["Documents", "Downloads", "scripts", "notes.txt"],
        "~/scripts": ["backup.sh", "server_start.sh"],
        "~/Documents": ["project_plan.pdf", "budget.xlsx"]
    },
    "help_text": "Available commands: ls, cd, pwd, whoami, clear, cat, echo. (Simulation Mode)",
    "welcome_message": "Cloud-with-Sai Virtual Linux Environment v1.0",
}
