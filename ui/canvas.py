from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QPainterPath
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
            QGraphicsView.NoDrag
        )

#zoom seviyesi
        self.zoom = 1.0

#zoom sınırları
        self.min_zoom = 0.2
        self.max_zoom = 5.0

#çizim durumu
        self.drawing = False

#çizgi yolu
        self.path = None

#aktif çizgi
        self.current_item = None

#aktif araç
        self.tool = "pen"

#renk
        self.current_color = "#000000"

#kalem boyutu
        self.base_size = 3

#basınç
        self.pressure = 1.0


    def createPen(self):
#kalem oluştur
        pen = QPen(
            QColor(self.current_color)
        )

        pen.setWidthF(
            self.base_size * self.pressure
        )

        pen.setCapStyle(
            Qt.RoundCap
        )

        pen.setJoinStyle(
            Qt.RoundJoin
        )

        return pen


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


    def mousePressEvent(self, event):
#sol tuş
        if event.button() == Qt.LeftButton:

#silgi
            if self.tool == "eraser":

                pos = self.mapToScene(
                    event.position().toPoint()
                )

                item = self.scene.itemAt(
                    pos,
                    self.transform()
                )

                if item:
                    self.scene.removeItem(item)

                return


#kalem
            self.drawing = True

            pos = self.mapToScene(
                event.position().toPoint()
            )

            self.path = QPainterPath()

            self.path.moveTo(
                pos
            )

            self.current_item = self.scene.addPath(
                self.path,
                self.createPen()
            )

        else:
            super().mousePressEvent(event)


    def mouseMoveEvent(self, event):
#silgi
        if self.tool == "eraser":

            pos = self.mapToScene(
                event.position().toPoint()
            )

            item = self.scene.itemAt(
                pos,
                self.transform()
            )

            if item:
                self.scene.removeItem(item)

            return


#çizim
        if self.drawing:

            pos = self.mapToScene(
                event.position().toPoint()
            )

            self.path.lineTo(
                pos
            )

            self.current_item.setPath(
                self.path
            )

            self.scene.update()

        else:
            super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
#çizim bitişi
        if event.button() == Qt.LeftButton:

            self.drawing = False

            self.path = None

        else:
            super().mouseReleaseEvent(event)


    def tabletEvent(self, event):
#tablet basıncı
        self.pressure = event.pressure()

        if self.pressure <= 0:
            self.pressure = 1.0

        event.accept()


    def setColor(self, color):
#renk değiştir
        self.current_color = color


    def setEraser(self):
#silgi modu
        self.tool = "eraser"


    def setPen(self):
#kalem modu
        self.tool = "pen"
