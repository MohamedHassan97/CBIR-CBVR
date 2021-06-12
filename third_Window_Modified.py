# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirdWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, subprocess
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
from DB_video import *
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
        self.sim_vid1 = QtWidgets.QLabel(Form)
        self.sim_vid1.setGeometry(QtCore.QRect(100, 390, 47, 13))
        self.sim_vid1.setObjectName("sim_vid1")
        self.sim_vid2 = QtWidgets.QLabel(Form)
        self.sim_vid2.setGeometry(QtCore.QRect(250, 390, 47, 13))
        self.sim_vid2.setObjectName("sim_vid2")
        self.sim_vid3 = QtWidgets.QLabel(Form)
        self.sim_vid3.setGeometry(QtCore.QRect(410, 390, 47, 13))
        self.sim_vid3.setObjectName("sim_vid3")
        self.sim_vid4 = QtWidgets.QLabel(Form)
        self.sim_vid4.setGeometry(QtCore.QRect(560, 390, 47, 13))
        self.sim_vid4.setObjectName("sim_vid4")
        self.sim_vid5 = QtWidgets.QLabel(Form)
        self.sim_vid5.setGeometry(QtCore.QRect(720, 390, 47, 13))
        self.sim_vid5.setObjectName("sim_vid5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 280, 751, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.path_vid1 = QtWidgets.QLabel(self.widget)
        self.path_vid1.setObjectName("path_vid1")
        self.horizontalLayout_2.addWidget(self.path_vid1)
        self.path_vid2 = QtWidgets.QLabel(self.widget)
        self.path_vid2.setObjectName("path_vid2")
        self.horizontalLayout_2.addWidget(self.path_vid2)
        self.path_vid3 = QtWidgets.QLabel(self.widget)
        self.path_vid3.setObjectName("path_vid3")
        self.horizontalLayout_2.addWidget(self.path_vid3)
        self.path_vid4 = QtWidgets.QLabel(self.widget)
        self.path_vid4.setObjectName("path_vid4")
        self.horizontalLayout_2.addWidget(self.path_vid4)
        self.path_vid5 = QtWidgets.QLabel(self.widget)
        self.path_vid5.setObjectName("path_vid5")
        self.horizontalLayout_2.addWidget(self.path_vid5)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(90, 150, 761, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_vid1 = QtWidgets.QPushButton(self.widget1)
        self.btn_vid1.setObjectName("btn_vid1")
        self.horizontalLayout_3.addWidget(self.btn_vid1)
        self.btn_vid2 = QtWidgets.QPushButton(self.widget1)
        self.btn_vid2.setObjectName("btn_vid2")
        self.horizontalLayout_3.addWidget(self.btn_vid2)
        self.btn_vid3 = QtWidgets.QPushButton(self.widget1)
        self.btn_vid3.setObjectName("btn_vid3")
        self.horizontalLayout_3.addWidget(self.btn_vid3)
        self.btn_vid4 = QtWidgets.QPushButton(self.widget1)
        self.btn_vid4.setObjectName("btn_vid4")
        self.horizontalLayout_3.addWidget(self.btn_vid4)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btn_vid1.clicked.connect(self.video_one)
        self.btn_vid2.clicked.connect(self.video_two)
        self.btn_vid3.clicked.connect(self.video_three)
        self.btn_vid4.clicked.connect(self.video_four)
        self.pushButton_6.clicked.connect(self.video_five)
        self.pushButton_3.clicked.connect(self.checkpath2)
    def checkpath2(self):
        video_path = self.lineEdit_3.text()
        result = get_output(get_docs("cbv"), video_path)
        if os.path.isfile(video_path):
            self.path_1 = result[0][0]
            self.path_2 = result[1][0]
            self.path_3 = result[2][0]
            self.path_4 = result[3][0]
            self.path_5 = result[4][0]

            self.sim_vid1.setText(str(result[0][1]))
            self.sim_vid2.setText(str(result[1][1]))
            self.sim_vid3.setText(str(result[2][1]))
            self.sim_vid4.setText(str(result[3][1]))
            self.sim_vid5.setText(str(result[4][1]))
            
            # self.vid1.setPixmap(QtGui.QPixmap("1.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            # self.vid2.setPixmap(QtGui.QPixmap("2.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            # self.vid3.setPixmap(QtGui.QPixmap("3.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            # self.vid4.setPixmap(QtGui.QPixmap("4.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))
            # self.vid5.setPixmap(QtGui.QPixmap("5.jpg").scaled(200, 150, QtCore.Qt.KeepAspectRatio))    
    def video_one(self):
        path = self.path_1
        open_file(path)
    def video_two(self):
        path=self.path_2
        open_file(path)
    def video_three(self):
            path=self.path_3
            open_file(path)
    def video_four(self):
        path=self.path_4
        open_file(path)
    def video_five(self):
        path=self.path_5
        open_file(path)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Search"))
        self.label_3.setText(_translate("Form", "Video path"))
        self.sim_vid1.setText(_translate("Form", " "))
        self.sim_vid2.setText(_translate("Form", " "))
        self.sim_vid3.setText(_translate("Form", " "))
        self.sim_vid4.setText(_translate("Form", " "))
        self.sim_vid5.setText(_translate("Form", " "))
        self.path_vid1.setText(_translate("Form", " "))
        self.path_vid2.setText(_translate("Form", " "))
        self.path_vid3.setText(_translate("Form", " "))
        self.path_vid4.setText(_translate("Form", " "))
        self.path_vid5.setText(_translate("Form", " "))
        self.btn_vid1.setText(_translate("Form", "video_1"))
        self.btn_vid2.setText(_translate("Form", "video_2"))
        self.btn_vid3.setText(_translate("Form", "video_3"))
        self.btn_vid4.setText(_translate("Form", "video_4"))
        self.pushButton_6.setText(_translate("Form", "video_5"))



