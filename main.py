import sys

from PySide6.QtWidgets import QApplication

from ui.canvas_window import CanvasWindow
from ui.notch import NotchWindow


def main():
#uygulama
    app = QApplication(sys.argv)

#canvas
    canvas = CanvasWindow()
    canvas.show()

#notch
    notch = NotchWindow()

#canvas ile bağlantı
    notch.canvas = canvas

#notch'u göster
    notch.show()

#uygulamayı başlat
    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()