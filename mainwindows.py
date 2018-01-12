# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(957, 622)
        self.show_label = QtWidgets.QLabel(Form)
        self.show_label.setGeometry(QtCore.QRect(260, 10, 631, 571))
        self.show_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.show_label.setText("")
        self.show_label.setTextFormat(QtCore.Qt.RichText)
        self.show_label.setScaledContents(False)
        self.show_label.setObjectName("show_label")
        self.open_image = QtWidgets.QPushButton(Form)
        self.open_image.setGeometry(QtCore.QRect(20, 470, 85, 27))
        self.open_image.setObjectName("open_image")
        self.open_file = QtWidgets.QPushButton(Form)
        self.open_file.setGeometry(QtCore.QRect(130, 470, 85, 27))
        self.open_file.setObjectName("open_file")
        self.file_list = QtWidgets.QListWidget(Form)
        self.file_list.setGeometry(QtCore.QRect(10, 10, 241, 441))
        self.file_list.setObjectName("file_list")
        self.prev_image = QtWidgets.QPushButton(Form)
        self.prev_image.setGeometry(QtCore.QRect(260, 590, 85, 27))
        self.prev_image.setObjectName("prev_image")
        self.next_image = QtWidgets.QPushButton(Form)
        self.next_image.setGeometry(QtCore.QRect(810, 590, 85, 27))
        self.next_image.setObjectName("next_image")
        self.check_box = QtWidgets.QComboBox(Form)
        self.check_box.setGeometry(QtCore.QRect(20, 523, 201, 31))
        self.check_box.setObjectName("check_box")
        self.check_box.addItem("")
        self.check_box.addItem("")
        self.check_box.addItem("")
        self.check_box.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open_image.setText(_translate("Form", "打开图片"))
        self.open_file.setText(_translate("Form", "打开文件夹"))
        self.prev_image.setText(_translate("Form", "前一张"))
        self.next_image.setText(_translate("Form", "后一张"))
        self.check_box.setItemText(0, _translate("Form", "人"))
        self.check_box.setItemText(1, _translate("Form", "狗"))
        self.check_box.setItemText(2, _translate("Form", "车"))
        self.check_box.setItemText(3, _translate("Form", "车标"))

