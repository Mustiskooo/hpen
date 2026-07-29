from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView


class InfiniteCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        #sonsuz hissi için büyük alan
        self.scene.setSceneRect(
            -10000,
            -10000,
            20000,
            20000
        )

        #canvas rengi
        self.setBackgroundBrush(
            QBrush(QColor("#FCFCFC"))
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


    def wheelEvent(self, event):
        #zoom değeri
        zoom_factor = 1.15

        if event.angleDelta().y() > 0:
            self.zoom *= zoom_factor

            self.scale(
                zoom_factor,
                zoom_factor
            )

        else:
            self.zoom /= zoom_factor

            self.scale(
                1 / zoom_factor,
                1 / zoom_factor
            )
