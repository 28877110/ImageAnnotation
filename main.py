#coding:utf-8
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap, QPen
from PyQt5.QtWidgets import QFileDialog
from mainwindows import Ui_Form
import sys
import os
import json
from fun import filefun

class mywindow(QtWidgets.QWidget,Ui_Form):
    paintwidth = 580
    paintheight = 620

    def __init__(self):
        super(mywindow,self).__init__()
        self.startpointx = 0
        self.startpointy = 0
        self.endpointx = 0
        self.endpointy = 0
        self.mImgList = []
        self.filePath = None
        self.filejson = None
        self.setupUi(self)
        self.open_image.clicked.connect(self.openImage)
        self.open_file.clicked.connect(self.openfileImage)
        self.file_list.itemDoubleClicked.connect(self.fileitemDoubleClicked)
        self.next_image.clicked.connect(self.nextImageClicked)
        self.prev_image.clicked.connect(self.prevImageClicked)
        self.check_box.activated[str].connect(self.onActivate)

    def mousePressEvent(self,ev):
        pos = ev.pos()
        self.startpointx = pos.x()
        if self.startpointx > self.paintheight:
            self.startpointx =self.paintheight
        self.startpointy = pos.y()
        if self.startpointy >self.paintwidth:
            self.startpointy = self.paintwidth
        print(self.startpointx)

    def mouseMoveEvent(self, ev):
        pos = ev.pos()
        self.endpointx = pos.x()
        if self.endpointx >self.paintheight:
            self.endpointx = self.paintheight
        self.endpointy = pos.y()
        if self.endpointy >self.paintwidth:
            self.endpointy = self.paintwidth
        self.repaint()

    def mouseReleaseEvent(self, ev):
        # pos = ev.pos()
        # self.endpointx = pos.x()
        # self.endpointy = pos.y()
        # 记录文件中
        print(self.startpointx,self.startpointy,self.endpointx,self.endpointy)
        print('文件路径 %s ' % self.filePath)
        print(self.check_box.currentText())
        newname = filefun.filetypetojson(self.filePath)
        self.filejson[self.check_box.currentText()] = {'startpointx':self.startpointx,'startpointy':self.startpointx,'endpointx':self.endpointx,'endpointy':self.endpointy}
        filefun.saveJsonToFile(newname,self.filejson)
        print(self.filejson)


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.filePath is not None:
            painter.drawPixmap(0, 0,QPixmap(self.filePath).scaled(self.paintheight,self.paintwidth,Qt.KeepAspectRatio))
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawLine(self.startpointx, self.startpointy, self.startpointx, self.endpointy)
        painter.drawLine(self.startpointx, self.startpointy, self.endpointx, self.startpointy)
        painter.drawLine(self.endpointx, self.startpointy, self.endpointx, self.endpointy)
        painter.drawLine(self.startpointx, self.endpointy, self.endpointx, self.endpointy)
        painter.end()

    def loadImage(self,imgName):
        self.startpointx = 0
        self.startpointy = 0
        self.endpointx = 0
        self.endpointy = 0
        self.filePath = imgName
        index = self.mImgList.index(imgName)
        fileWidgetItem = self.file_list.item(index)
        fileWidgetItem.setSelected(True)
        print(self.filePath)
        #Todo
        #加入读取json文件，加入原有的标记
        newname = filefun.filetypetojson(self.filePath)
        self.filejson = filefun.readJsonInFile(newname)
        if self.check_box.currentText() in self.filejson :
            self.startpointx = self.filejson[self.check_box.currentText()]['startpointx']
            self.startpointy = self.filejson[self.check_box.currentText()]['startpointy']
            self.endpointx = self.filejson[self.check_box.currentText()]['endpointx']
            self.endpointy = self.filejson[self.check_box.currentText()]['endpointy']
        #png = QtGui.QPixmap(imgName)
        self.repaint()

    def openImage(self):
        imgName,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        self.loadImage(imgName)


    def scanAllImages(self, folderPath):
        extensions = ['.jpeg', '.jpg', '.png', '.bmp']
        images = []

        for root, dirs, files in os.walk(folderPath):
            for file in files:
                if file.lower().endswith(tuple(extensions)):
                    relativePath = os.path.join(root, file)
                    print(relativePath)
                    images.append(relativePath)
        images.sort(key=lambda x: x.lower())
        return images

    def openfileImage(self):
        self.file_list.clear()
        self.mImgList.clear()
        imgName = QFileDialog.getExistingDirectory()
        iamges = self.scanAllImages(imgName)
        self.file_list.addItems(iamges)
        self.mImgList= iamges


    def fileitemDoubleClicked(self,item = None):
        currIndex = self.mImgList.index(item.text())
        print(currIndex)
        if currIndex < len(self.mImgList):
            filename = self.mImgList[currIndex]
            if filename:
                self.loadImage(filename)

    def nextImageClicked(self):
        currIndex = 0
        if self.mImgList:
            filename = self.mImgList[0]
        if self.filePath is not None:
            currIndex = self.mImgList.index(self.filePath)
        if currIndex + 1 < len(self.mImgList):
            filename = self.mImgList[currIndex + 1]
        print(filename)
        if self.filePath is not None:
            self.loadImage(filename)

    def prevImageClicked(self):
        currIndex = 0
        if self.mImgList :
            filename = self.mImgList[0]
        if self.filePath is not None:
            currIndex = self.mImgList.index(self.filePath)
        if currIndex - 1 >= 0:
            filename = self.mImgList[currIndex - 1]
        if self.filePath is not None:
            self.loadImage(filename)

    def onActivate(self):
        if self.filePath is not None:
            currIndex = self.mImgList.index(self.filePath)
        if currIndex + 1 < len(self.mImgList):
            filename = self.mImgList[currIndex]
        if self.filePath is not None:
            self.loadImage(filename)



if "__main__" == __name__:
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())