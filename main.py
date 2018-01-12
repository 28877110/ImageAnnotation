#coding:utf-8
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog
from mainwindows import Ui_Form
import sys
import os

class mywindow(QtWidgets.QWidget,Ui_Form):

    def __init__(self):
        super(mywindow,self).__init__()
        self.scene =QtWidgets.QGraphicsScene()
        self.scene.addText("haskdhsjkhfjksdhkfhasdjkfhaslkfhkasgdkl")
        self.scene.setSceneRect(0,0,100,200)
        self.mImgList = []
        self.filePath = None
        self.setupUi(self)
        self.open_image.clicked.connect(self.openImage)
        self.open_file.clicked.connect(self.openfileImage)
        self.file_list.itemDoubleClicked.connect(self.fileitemDoubleClicked)
        self.next_image.clicked.connect(self.nextImageClicked)
        self.prev_image.clicked.connect(self.prevImageClicked)

    def loadImage(self,imgName):
        self.filePath = imgName
        index = self.mImgList.index(imgName)
        fileWidgetItem = self.file_list.item(index)
        fileWidgetItem.setSelected(True)

        png = QtGui.QPixmap(imgName).scaled(self.show_label.width(), self.show_label.height())
        self.show_label.setPixmap(png)

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


if "__main__" == __name__:
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())