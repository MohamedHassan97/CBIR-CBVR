# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from windowTwo import Ui_Form
from third_Window_Modified import Ui_Form2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(290, 140, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(36)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(310, 390, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(24)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setObjectName("pushButton_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_1.clicked.connect(self.secondscr)        
    def secondscr(self):
        #code the 2nd screen here
         
         typee=self.comboBox_1.currentText()
         if (typee=="Image"):
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.Form)
            self.Form.show()   
         else:
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form2()
            self.ui.setupUi2(self.Form)
            self.Form.show()
            
           
    
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_1.setCurrentText(_translate("MainWindow", "Image"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "Image"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Video"))
        self.pushButton_1.setText(_translate("MainWindow", "Submit"))
   

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

