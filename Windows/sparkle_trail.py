import sys
import time
import ctypes
import os
from random import randint, choice
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QTimer, QPoint
from pynput.mouse import Controller

# === CONFIG ===
SPARKLE_IMAGES = [
    "sparkle_pink.png",
    "sparkle_mint.png",
    "sparkle_lilac.png",
    "sparkle_yellow.png"
]

SPARKLE_LIFESPAN = 1.2
TRAIL_LENGTH = 60

# === SPARKLE CLASS (now with image!)
class Sparkle:
    def __init__(self, pos, pixmap):
        self.pos = pos
        self.timestamp = time.time()
        self.pixmap = pixmap

class SparkleTrail(QWidget):
    def __init__(self):
        super().__init__()

        self.sparkles = []
        self.mouse = Controller()
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        self.sparkle_pixmaps = [
            QPixmap(os.path.join(base_path, img)) for img in SPARKLE_IMAGES
        ]

        # Transparent fullscreen always-on-top window
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.showFullScreen()
        self.make_click_through()

        self.setFocusPolicy(Qt.StrongFocus)  # Ensures widget receives key events
        self.setFocus()


        # Sparkle animation loop
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_sparkles)
        self.timer.start(30)

    def make_click_through(self):
        hwnd = int(self.winId())
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x80000
        WS_EX_TRANSPARENT = 0x20
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT)

    def update_sparkles(self):
        now = time.time()
        self.sparkles = [s for s in self.sparkles if now - s.timestamp < SPARKLE_LIFESPAN]

        x, y = self.mouse.position

        # Trail appears to the right and further down
        base_x = x + 22
        base_y = y + 35

        # Add multiple sparkles with random spread
        for _ in range(4):
            offset = QPoint(base_x + randint(-6, 6), base_y + randint(-6, 6))
            pixmap = choice(self.sparkle_pixmaps)
            self.sparkles.append(Sparkle(offset, pixmap))

        if len(self.sparkles) > TRAIL_LENGTH:
            self.sparkles = self.sparkles[-TRAIL_LENGTH:]

        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        now = time.time()

        for sparkle in self.sparkles:
            age = now - sparkle.timestamp
            opacity = max(0, (1 - age / SPARKLE_LIFESPAN) ** 1.5)
            painter.setOpacity(opacity)
            scaled = sparkle.pixmap.scaled(8, 8, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(sparkle.pos - QPoint(4, 4), scaled)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()

# === RUN ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SparkleTrail()
    sys.exit(app.exec_())
