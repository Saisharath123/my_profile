
import sys
import os
import importlib

# Add the root to sys.path
sys.path.append(r"c:\Users\HP\Desktop\my_profile")

module_path = 'SkillAnalyzer.Skill_test.cloud_devops_test.AWS.aws_cloud_practitioner'

print(f"Attempting to import: {module_path}")

try:
    mod = importlib.import_module(module_path)
    print("Import successful!")
    if hasattr(mod, 'render'):
        print("render() function found.")
    else:
        print("render() function NOT found.")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()
