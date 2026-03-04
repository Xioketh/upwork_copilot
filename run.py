# run.py
import os
import subprocess

if __name__ == "__main__":
    # Ensure you are running this from the root 'upwork_copilot' directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(current_dir, "ui", "app.py")
    
    subprocess.run(["streamlit", "run", app_path])