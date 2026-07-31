from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from ui.canvas import InfiniteCanvas


class CanvasWindow(QWidget):
    def __init__(self):
        super().__init__()

#pencere ayarları
        self.setWindowFlags(
            Qt.FramelessWindowHint
        )

#pencere başlığı
        self.setWindowTitle(
            "h-pen"
        )

        self.resize(
            1600,
            900
        )

#minimum boyut
        self.setMinimumSize(
            800,
            500
        )

#stil
        self.setStyleSheet("""
        QWidget{
            background:#18181B;
        }
        """)

#layout
        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        layout.setSpacing(
            0
        )

#canvas
        self.canvas = InfiniteCanvas()

        layout.addWidget(
            self.canvas
        )