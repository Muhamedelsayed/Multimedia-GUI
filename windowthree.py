# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirdWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
class Ui_Form2(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(969, 697)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 570, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 60, 711, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 140, 891, 381))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.vid3 = QtWidgets.QLabel(self.widget)
        self.vid3.setObjectName("vid3")
        self.gridLayout.addWidget(self.vid3, 0, 4, 1, 1)
        self.vid1 = QtWidgets.QLabel(self.widget)
        self.vid1.setObjectName("vid1")
        self.gridLayout.addWidget(self.vid1, 0, 0, 1, 1)
        self.vid4 = QtWidgets.QLabel(self.widget)
        self.vid4.setObjectName("vid4")
        self.gridLayout.addWidget(self.vid4, 1, 1, 1, 1)
        self.vid5 = QtWidgets.QLabel(self.widget)
        self.vid5.setObjectName("vid5")
        self.gridLayout.addWidget(self.vid5, 1, 3, 1, 1)
        self.vid2 = QtWidgets.QLabel(self.widget)
        self.vid2.setObjectName("vid2")
        self.gridLayout.addWidget(self.vid2, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_3.clicked.connect(self.checkpath2)
        
    def checkpath2(self):
        image_path = self.lineEdit_3.text()
        if os.path.isfile(image_path):
            
            self.vid1.setPixmap(QtGui.QPixmap("1.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            self.vid2.setPixmap(QtGui.QPixmap("2.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            self.vid3.setPixmap(QtGui.QPixmap("3.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            self.vid4.setPixmap(QtGui.QPixmap("4.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            self.vid5.setPixmap(QtGui.QPixmap("5.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Search"))
        self.label_3.setText(_translate("Form", "Video path"))
        self.vid3.setText(_translate("Form", "TextLabel"))
        self.vid1.setText(_translate("Form", "TextLabel"))
        self.vid4.setText(_translate("Form", "TextLabel"))
        self.vid5.setText(_translate("Form", "TextLabel"))
        self.vid2.setText(_translate("Form", "TextLabel"))



