#coding:utf-8
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QCursor

from magnifier.magnifierui import Ui_Form


class magnifier(Ui_Form,QtWidgets.QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.mouseX = 0
        self.mouseY = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showImg)
        self.startImg()


    def startImg(self):
        print("start")
        self.timer.start(100)

    def showImg(self):
        self.repaint()

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        print(QCursor.pos())
        a = QtGui.QGuiApplication.primaryScreen().grabWindow(0,QCursor.pos().x()-50,QCursor.pos().y()-50,100,100)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPixmap(0, 0,a.scaled(a.width()*5,a.height()*5, Qt.KeepAspectRatio))
        painter.end()