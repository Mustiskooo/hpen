from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView


class InfiniteCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

#tablet desteği
        self.setAttribute(
            Qt.WA_TabletTracking,
            True
        )

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

#sonsuz hissi için büyük alan
        self.scene.setSceneRect(
            -10000,
            -10000,
            20000,
            20000
        )

#render
        self.setRenderHint(
            QPainter.Antialiasing
        )

#scrollbar gizleme
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )
        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

#pan
        self.setDragMode(
            QGraphicsView.ScrollHandDrag
        )

#zoom seviyesi
        self.zoom = 1.0

#zoom sınırları
        self.min_zoom = 0.2
        self.max_zoom = 5.0


    def wheelEvent(self, event):
#zoom değeri
        zoom_factor = 1.15

        if event.angleDelta().y() > 0:

            if self.zoom < self.max_zoom:
                self.zoom *= zoom_factor

                self.scale(
                    zoom_factor,
                    zoom_factor
                )

        else:

            if self.zoom > self.min_zoom:
                self.zoom /= zoom_factor

                self.scale(
                    1 / zoom_factor,
                    1 / zoom_factor
                )


    def drawBackground(self, painter, rect):
#kağıt rengi
        painter.fillRect(
            rect,
            QColor("#FFFFFF")
        )

#kare boyutu
        grid_size = 40

#çizgi rengi
        pen = QPen(
            QColor("#222222")
        )

        pen.setWidthF(0.8)

        painter.setPen(pen)

#görünen alan
        left = int(rect.left())
        right = int(rect.right())
        top = int(rect.top())
        bottom = int(rect.bottom())

#dikey çizgiler
        x = left - (left % grid_size)

        while x < right:
            painter.drawLine(
                x,
                top,
                x,
                bottom
            )

            x += grid_size

#yatay çizgiler
        y = top - (top % grid_size)

        while y < bottom:
            painter.drawLine(
                left,
                y,
                right,
                y
            )

            y += grid_size
