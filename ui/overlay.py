from PySide6.QtCore import (
    Qt,
    QRect,
    QPoint,
)

from PySide6.QtGui import (
    QColor,
    QPainter,
    QPen,
)

from PySide6.QtWidgets import (
    QWidget,
)


class ScreenOverlay(QWidget):
    def __init__(self):
        super().__init__()

#pencere ayarları
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

#tam ekran
        self.showFullScreen()

#fare takibi
        self.setMouseTracking(
            True
        )

#başlangıç
        self.startPoint = QPoint()
        self.endPoint = QPoint()

        self.selecting = False


    def paintEvent(self, event):
#çizim
        painter = QPainter(self)

#arka plan
        painter.fillRect(
            self.rect(),
            QColor(0, 0, 0, 120)
        )

#seçim kutusu
        if self.selecting:

            rect = QRect(
                self.startPoint,
                self.endPoint
            )

            painter.setPen(
                QPen(
                    QColor("#4F8EF7"),
                    2
                )
            )

            painter.drawRect(
                rect.normalized()
            )


    def mousePressEvent(self, event):
#başla
        if event.button() == Qt.LeftButton:

            self.selecting = True

            self.startPoint = event.pos()
            self.endPoint = event.pos()

            self.update()


    def mouseMoveEvent(self, event):
#güncelle
        if self.selecting:

            self.endPoint = event.pos()

            self.update()


    def mouseReleaseEvent(self, event):
#bitir
        self.selecting = False

        self.endPoint = event.pos()

        self.update()


    def keyPressEvent(self, event):
#esc
        if event.key() == Qt.Key_Escape:
            self.close()