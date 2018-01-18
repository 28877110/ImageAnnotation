#coding:utf-8
import sys
from magnifierui import Ui_Form
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QPixmap, QPen, QScreen, QCursor
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore

class magnifier(Ui_Form,QtWidgets.QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.mouseX = 0
        self.mouseY = 0
        self.setMouseTracking(True)
        self.grabMouse()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        print(QCursor.pos())
        a = QtGui.QGuiApplication.primaryScreen().grabWindow(0,QCursor.pos().x(),QCursor.pos().y(),200,200)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPixmap(0, 0,a)
        painter.end()

    def mouseMoveEvent(self, QMouseEvent):
        self.repaint()


if "__main__" == __name__:
    app = QtWidgets.QApplication(sys.argv)
    window = magnifier()
    window.show()
    app.installEventFilter(window)
    sys.exit(app.exec_())