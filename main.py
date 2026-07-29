import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class HPen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("h-pen")
        self.resize(1600, 900)

        self.setStyleSheet("""
        QMainWindow{
            background:#18181B;
        }

        QWidget{
            color:#F4F4F5;
            font-size:14px;
            font-family:Segoe UI;
        }

        QFrame#sidebar{
            background:#202127;
            border-right:1px solid #34353B;
        }

        QFrame#toolbar{
            background:#27272A;
            border-bottom:1px solid #34353B;
        }

        QFrame#canvas{
            background:white;
            border-radius:12px;
        }

        QPushButton{
            background:transparent;
            border:none;
            padding:8px;
            border-radius:8px;
        }

        QPushButton:hover{
            background:#34353B;
        }
        """)

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0,0,0,0)
        root.setSpacing(0)

#sidebar
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(80)

        side_layout = QVBoxLayout(sidebar)
        side_layout.setContentsMargins(12,20,12,20)

        logo = QLabel("✏")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("font-size:30px;")

        side_layout.addWidget(logo)

        for text in ["🏠","📁","⭐","⚙"]:
            btn = QPushButton(text)
            btn.setFixedHeight(42)
            side_layout.addWidget(btn)

        side_layout.addStretch()

        root.addWidget(sidebar)
#sağ :3
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0,0,0,0)
        right_layout.setSpacing(0)
#toolbar
        toolbar = QFrame()
        toolbar.setObjectName("toolbar")
        toolbar.setFixedHeight(60)

        tb = QHBoxLayout(toolbar)
        tb.setContentsMargins(20,0,20,0)

        tb.addWidget(QLabel("h-pen"))

        tb.addStretch()

        undo_btn = QPushButton("↶")
        redo_btn = QPushButton("↷")
        pen_btn = QPushButton("✏")
        eraser_btn = QPushButton("🧽")
        zoom_btn = QPushButton("🔍")

        tb.addWidget(undo_btn)
        tb.addWidget(redo_btn)
        tb.addWidget(pen_btn)
        tb.addWidget(eraser_btn)
        tb.addWidget(zoom_btn)

        right_layout.addWidget(toolbar)

#canvas alanı
      
        canvas_area = QWidget()
        canvas_layout = QVBoxLayout(canvas_area)
        canvas_layout.setContentsMargins(30,30,30,30)

        from ui.canvas import InfiniteCanvas
        
        canvas = InfiniteCanvas()

#kalem butonu
        pen_btn.clicked.connect(
            canvas.setPen
        )

#silgi butonu
        eraser_btn.clicked.connect(
            canvas.setEraser
        )

        canvas_layout.addWidget(canvas)
        right_layout.addWidget(canvas_area)

        root.addWidget(right)


app = QApplication(sys.argv)

window = HPen()
window.show()

sys.exit(app.exec())
