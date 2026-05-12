import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WaterTracker(QMainWindow):

    def __init__(self):
        super().__init__()

        # Starting value
        self.glasses = 0

        self.initUI()

    def initUI(self):

        self.setWindowTitle("💧 Water Tracker")
        self.setGeometry(300, 300, 400, 350)

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # ================= TITLE =================
        title = QLabel("💧 DAILY WATER TRACKER 💧")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #2196F3;
            padding: 10px;
        """)

        layout.addWidget(title)

        # ================= EMOJI LABEL =================
        self.glasses_label = QLabel("✨ 0 ✨")

        self.glasses_label.setAlignment(Qt.AlignCenter)

        self.glasses_label.setStyleSheet("""
            font-size: 36px;
            padding: 20px;
        """)

        layout.addWidget(self.glasses_label)

        # ================= COUNT LABEL =================
        self.count_label = QLabel("📊 0 / 8 glasses")

        self.count_label.setAlignment(Qt.AlignCenter)

        self.count_label.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
        """)

        layout.addWidget(self.count_label)

        # ================= BUTTONS =================
        button_layout = QHBoxLayout()

        self.add_btn = QPushButton("➕ Add Water")

        self.add_btn.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
        """)

        self.reset_btn = QPushButton("🔄 Reset")

        self.reset_btn.setStyleSheet("""
            background-color: #f44336;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
        """)

        # Connect Buttons
        self.add_btn.clicked.connect(self.add_water)
        self.reset_btn.clicked.connect(self.reset_water)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.reset_btn)

        layout.addLayout(button_layout)

        # ================= MESSAGE LABEL =================
        self.message_label = QLabel("💙 Start drinking water!")

        self.message_label.setAlignment(Qt.AlignCenter)

        self.message_label.setStyleSheet("""
            font-size: 14px;
            color: #2196F3;
            padding: 10px;
        """)

        layout.addWidget(self.message_label)

        # ================= PROGRESS BAR =================
        self.progress = QProgressBar()

        self.progress.setMaximum(8)

        self.progress.setValue(0)

        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid gray;
                border-radius: 5px;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #4CAF50;
            }
        """)

        layout.addWidget(self.progress)

    # ==================================================
    # TASK 1: ADD WATER
    # ==================================================

    def add_water(self):

        # HINT:
        # Increase glasses count by 1

        pass

    # ==================================================
    # TASK 2: RESET WATER
    # ==================================================

    def reset_water(self):

        # HINT:
        # Set glasses back to 0

        pass

    # ==================================================
    # TASK 3: UPDATE DISPLAY
    # ==================================================

    def update_display(self):

        # ================= COUNT LABEL =================

        # HINT:
        # Show current glasses count

        # Example:
        # 📊 3 / 8 glasses

        pass

        # ================= PROGRESS BAR =================

        # HINT:
        # Update progress bar value

        pass

        # ================= EMOJI DISPLAY =================

        # HINT:
        # Show 🥤 emoji based on count

        # Example:
        # 🥤🥤🥤

        pass

        # ================= MOTIVATION MESSAGE =================

        # HINT:
        # Use if-elif-else

        # 8 or more:
        # "🎉 Excellent Hydration!"

        # 5 or more:
        # "👍 Keep Going!"

        # Otherwise:
        # "💧 Drink More Water!"

        pass


# ================= MAIN PROGRAM =================

app = QApplication(sys.argv)

window = WaterTracker()
window.show()

sys.exit(app.exec_())
