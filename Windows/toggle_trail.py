import os
import signal
import subprocess
import psutil
import sys
import time
import tempfile
import shutil

SCRIPT_NAME = "sparkle_trail.py"
PYTHON_EXECUTABLE = "pythonw"  # Prevent console window

def is_trail_running():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and SCRIPT_NAME in ' '.join(proc.info['cmdline']):
                return proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

def start_trail():
    try:
        # Extract bundled trail to temp folder
        base_path = sys._MEIPASS if hasattr(sys, "_MEIPASS") else os.path.dirname(__file__)
        temp_dir = tempfile.mkdtemp()
        trail_path = os.path.join(temp_dir, SCRIPT_NAME)

        shutil.copy(os.path.join(base_path, SCRIPT_NAME), trail_path)
        for img in ["sparkle_pink.png", "sparkle_mint.png", "sparkle_lilac.png", "sparkle_yellow.png"]:
            shutil.copy(os.path.join(base_path, img), os.path.join(temp_dir, img))

        subprocess.Popen(
            [PYTHON_EXECUTABLE, trail_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.DETACHED_PROCESS
        )

    except Exception:
        pass  # Silently ignore errors

def stop_trail(pid):
    try:
        os.kill(pid, signal.SIGTERM)
    except Exception:
        pass  # Silently ignore errors

def main():
    pid = is_trail_running()
    if pid:
        stop_trail(pid)
    else:
        start_trail()

if __name__ == "__main__":
    main()
