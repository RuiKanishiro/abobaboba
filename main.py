import sys
import math

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPainter, QPolygonF, QColor, QPixmap
from PyQt6.QtCore import QPointF, QRectF
from PyQt6 import uic
from random import randint


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.index = 0
        self.do_paint = False
        self.label = QLabel()
        self.canvas = QPixmap(1000, 1000)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.resize(1000, 1000)
        self.pixmap = QPixmap
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            a = randint(20, 100)
            x = randint(0, 600)
            y = randint(0, 500)
            qp.setBrush(QColor(255, 233, 0))
            qp.drawEllipse(QPointF(x, y), a, a)
            qp.end()
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.update()


def except_hook(cls, exceptation, traceback):
    sys.__excepthook__(cls, exceptation, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())