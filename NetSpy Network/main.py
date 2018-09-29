# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import scanner
import about
import BruteForce
import Netspy_ui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Firstpage(object):

    def scanner(self):
        self.scanner=QtGui.QMainWindow()
        self.scan=scanner.Ui_MainWindow()
        self.scan.setupUi(self.scanner)
        MainPage.hide()
        self.scanner.show()

    def aboutshow(self):
        self.about_ob=QtGui.QWidget()
        self.ab=about.Ui_Form()
        self.ab.setupUi(self.about_ob)
        self.about_ob.show()

    def bruteforce(self):
        self.brute_obj=QtGui.QMainWindow()
        self.brute=BruteForce.Ui_MainWindow()
        self.brute.setupUi(self.brute_obj)
        MainPage.hide()
        self.brute_obj.show()

    def net_spy(self):
        self.netspy_obj=QtGui.QMainWindow()
        self.netspy=Netspy_ui.Ui_MainWindow()
        self.netspy.setupUi(self.netspy_obj)
        MainPage.hide()
        self.netspy_obj.show()
    
    
    def setupUi(self, Firstpage):
        Firstpage.setObjectName(_fromUtf8("Firstpage"))
        Firstpage.resize(733, 425)
        Firstpage.setMinimumSize(QtCore.QSize(732, 425))
        Firstpage.setMaximumSize(QtCore.QSize(733, 425))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/network.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Firstpage.setWindowIcon(icon)
        Firstpage.setStyleSheet(_fromUtf8("background-color: rgb(24, 24, 24);"))
        self.pushButton = QtGui.QPushButton(Firstpage)
        self.pushButton.setGeometry(QtCore.QRect(50, 130, 121, 51))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid white;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.scanner)


        
        self.pushButton_2 = QtGui.QPushButton(Firstpage)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 130, 121, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid white;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_2.clicked.connect(self.bruteforce)
        
        self.pushButton_3 = QtGui.QPushButton(Firstpage)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 130, 121, 51))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid white;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);}"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Firstpage)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 130, 121, 51))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton{color: rgb(255, 255, 255);\n"
"border:1px solid white;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);}"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton_4.clicked.connect(self.net_spy)
        self.commandLinkButton = QtGui.QCommandLinkButton(Firstpage)
        self.commandLinkButton.setGeometry(QtCore.QRect(590, 360, 261, 61))
        self.commandLinkButton.setStyleSheet(_fromUtf8("QCommandLinkButton{\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QCommandLinkButton :hover{\n"
"background-color:#808080;}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/about_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(36, 36))
        self.commandLinkButton.setAutoDefault(True)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.clicked.connect(self.aboutshow)
        self.retranslateUi(Firstpage)
        QtCore.QMetaObject.connectSlotsByName(Firstpage)

    def retranslateUi(self, Firstpage):
        Firstpage.setWindowTitle(_translate("Firstpage", "NetSpy", None))
        self.pushButton.setText(_translate("Firstpage", "IP Scanner", None))
        self.pushButton_2.setText(_translate("Firstpage", "Brute Force", None))
        self.pushButton_3.setText(_translate("Firstpage", "SQL Attack", None))
        self.pushButton_4.setText(_translate("Firstpage", "NetSpy", None))
        self.commandLinkButton.setText(_translate("Firstpage", "ABOUT US", None))

import icons_rc

if __name__=="__main__":
    import sys
    app=QtGui.QApplication(sys.argv)
    MainPage=QtGui.QWidget()
    firstpage=Ui_Firstpage()
    firstpage.setupUi(MainPage)
    MainPage.show()
    sys.exit(app.exec_())

    
