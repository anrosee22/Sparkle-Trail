# Sparkle-Trail
✨ Sparkle Trail Cursor (Windows) ✨

A custom animated sparkle trail that follows your mouse in real time on Windows.  
Built with Python using `pywin32` and GDI to draw soft pastel sparkles that give your desktop a magical cyber aesthetic.

---

📁 What’s Included

- `sparkle_trail.py` – Main script that draws the sparkle trail under your cursor
- `toggle_trail.py` – A simple toggle to start/stop the sparkle effect
- `toggle_trail.spec` – PyInstaller config to turn `toggle_trail.py` into a .exe
- `sparkle_lilac.png`, `sparkle_mint.png`, `sparkle_pink.png`, `sparkle_yellow.png` – Sparkle images used for animation
- `sparkle.ico` – Optional icon for packaged app

---

🧠 How It Works

- Tracks the mouse position using Windows API (`win32api.GetCursorPos`)
- Draws a small sparkle image at each position with transparency
- Quickly fades older sparkles to create a trailing effect
- `toggle_trail.py` checks if the sparkle script is running and starts or kills it

---

💻 Requirements

- Windows OS  
- Python 3.x  
- `pywin32` package

You **do not need to install anything manually** if you just want to run the `.exe` (see below).  

If you're using the Python script:
**pip install pywin32**

---

🚀 How to Use

Clone this repo or download the files.

Open a terminal and navigate to the folder.

Run this command to start the Sparkle Trail:
**python sparkle_trail.py**

To toggle it on/off using the controller script:
**python toggle_trail.py**

---

⚙️ Optional: Build .exe for Easy Toggling
If you want a standalone .exe to toggle the sparkle effect:

Install PyInstaller:
**pip install pyinstaller**

Build the executable:
**pyinstaller toggle_trail.spec**

The .exe will be created inside the dist/ folder.
Double-click to toggle the sparkle trail like magic ✨

---

🎨 Customization:

Replace sparkle images with your own (.png with transparency)

Modify colors or add animation frames

Edit sparkle_trail.py to change trail speed, size, fade timing, etc.

