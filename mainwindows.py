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
        self.open_file = QtWidgets.QPushButton(Form)
        self.open_file.setGeometry(QtCore.QRect(700, 460, 111, 41))
        self.open_file.setObjectName("open_file")
        self.file_list = QtWidgets.QListWidget(Form)
        self.file_list.setGeometry(QtCore.QRect(700, 10, 241, 441))
        self.file_list.setObjectName("file_list")
        self.prev_image = QtWidgets.QPushButton(Form)
        self.prev_image.setGeometry(QtCore.QRect(20, 580, 85, 27))
        self.prev_image.setObjectName("prev_image")
        self.next_image = QtWidgets.QPushButton(Form)
        self.next_image.setGeometry(QtCore.QRect(450, 580, 85, 27))
        self.next_image.setObjectName("next_image")
        self.check_box = QtWidgets.QComboBox(Form)
        self.check_box.setGeometry(QtCore.QRect(700, 510, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_box.setFont(font)
        self.check_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.check_box.setAutoFillBackground(False)
        self.check_box.setObjectName("check_box")
        self.check_box.addItem("")
        self.check_box.addItem("")
        self.check_box.addItem("")
        self.check_box.addItem("")
        self.open_magnifier = QtWidgets.QPushButton(Form)
        self.open_magnifier.setGeometry(QtCore.QRect(830, 460, 111, 41))
        self.open_magnifier.setObjectName("open_magnifier")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open_file.setText(_translate("Form", "openDir"))
        self.prev_image.setText(_translate("Form", "prev"))
        self.next_image.setText(_translate("Form", "next"))
        self.check_box.setItemText(0, _translate("Form", "car"))
        self.check_box.setItemText(1, _translate("Form", "dog"))
        self.check_box.setItemText(2, _translate("Form", "person"))
        self.check_box.setItemText(3, _translate("Form", "logo"))
        self.open_magnifier.setText(_translate("Form", "Magnifier"))

