from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
)


class NotchWindow(QWidget):
    def __init__(self):
        super().__init__()

#pencere ayarları
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        self.setFixedSize(
            520,
            60
        )

#stil
        self.setStyleSheet("""
        QWidget{
            background:rgba(39,39,42,235);
            border:1px solid #3F3F46;
            border-radius:20px;
        }

        QPushButton{
            background:transparent;
            border:none;
            color:white;
            font-size:18px;
            padding:8px;
            border-radius:10px;
        }

        QPushButton:hover{
            background:#3F3F46;
        }
        """)

#layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(
            12,
            8,
            12,
            8
        )

#butonlar
        for icon in [
            "🖥",
            "✏",
            "🧽",
            "🎨",
            "📂",
            "💾",
            "↶",
            "↷",
            "⚙"
        ]:
            layout.addWidget(
                QPushButton(icon)
            )

#sürükleme
        self.dragging = False


        self.dragPos = QPoint()
    def mousePressEvent(self, event):
#taşımaya başla
        if event.button() == Qt.LeftButton:
            self.dragging = True

            self.dragPos = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )


    def mouseMoveEvent(self, event):
#taşı
        if self.dragging:
            self.move(
                event.globalPosition().toPoint()
                - self.dragPos
            )


    def mouseReleaseEvent(self, event):
#taşımayı bitir
        self.dragging = False