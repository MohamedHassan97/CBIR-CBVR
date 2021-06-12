# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from DB_image import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1203, 908)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(490, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(80, 60, 1041, 761))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 861, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2_1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2_1.setFont(font)
        self.pushButton_2_1.setObjectName("pushButton_2_1")
        self.horizontalLayout.addWidget(self.pushButton_2_1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(280, 80, 300, 200))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(200, 340, 591, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.pushButton_2_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2_2.setGeometry(QtCore.QRect(500, 840, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2_2.setFont(font)
        self.pushButton_2_2.setObjectName("pushButton_2_2")
        self.pushButton_2_1.clicked.connect(self.checkpath)
        self.pushButton_2_2.clicked.connect(self.checkPhotos)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def checkpath(self):
        image_path = self.lineEdit_2.text()
        if os.path.isfile(image_path):
            self.label.setPixmap(QtGui.QPixmap(image_path).scaled(300, 200, QtCore.Qt.KeepAspectRatio))
    def checkPhotos(self):
        data = data_base()
        image_path = self.lineEdit_2.text()
        if os.path.isfile(image_path):
            Mode=self.comboBox_2.currentText()
           
            if (Mode=="Histogram"):
                pathes = get_histogram(image_path, data)
                self.label_7.setPixmap(QtGui.QPixmap(pathes[0]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_3.setPixmap(QtGui.QPixmap(pathes[1]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_4.setPixmap(QtGui.QPixmap(pathes[2]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_5.setPixmap(QtGui.QPixmap(pathes[3]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_6.setPixmap(QtGui.QPixmap(pathes[4]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                
                ##### 7ot code el Histogram hna ###########   
            
            elif (Mode=="Color layout"):
                pathes = get_layout(image_path, data)
                self.label_7.setPixmap(QtGui.QPixmap(pathes[0]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_3.setPixmap(QtGui.QPixmap(pathes[1]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_4.setPixmap(QtGui.QPixmap(pathes[2]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_5.setPixmap(QtGui.QPixmap(pathes[3]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                self.label_6.setPixmap(QtGui.QPixmap(pathes[4]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                
               
                ##### 7ot code el Color Layout hna ###########            Note : htrg3 el 5 swar fe file forth_window
                
            elif (Mode=="average"):
                    pathes = get_mean_color(image_path, data)
                    self.label_7.setPixmap(QtGui.QPixmap(pathes[0]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                    self.label_3.setPixmap(QtGui.QPixmap(pathes[1]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                    self.label_4.setPixmap(QtGui.QPixmap(pathes[2]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                    self.label_5.setPixmap(QtGui.QPixmap(pathes[3]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                    self.label_6.setPixmap(QtGui.QPixmap(pathes[4]).scaled(150, 100, QtCore.Qt.KeepAspectRatio))
                
            
                ##### 7ot code el average hna ########### 
            

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_2.setItemText(0, _translate("Form", "Histogram"))
        self.comboBox_2.setItemText(1, _translate("Form", "Color layout"))
        self.comboBox_2.setItemText(2, _translate("Form", "average"))
        self.label_2.setText(_translate("Form", "Image Path"))
        self.pushButton_2_1.setText(_translate("Form", "Show image"))
        self.label_3.setText(_translate("Form", " "))
        self.label_4.setText(_translate("Form", " "))
        self.label_7.setText(_translate("Form", " "))
        self.label_5.setText(_translate("Form", " "))
        self.label_6.setText(_translate("Form", " "))
        self.pushButton_2_2.setText(_translate("Form", "submit"))


