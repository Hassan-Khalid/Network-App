# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(787, 575)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(787, 575))
        MainWindow.setMaximumSize(QtCore.QSize(787, 575))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/vm-green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow {background-color: rgb(0, 170, 255);}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 787, 575))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(781, 551))
        self.tabWidget.setMaximumSize(QtCore.QSize(787, 577))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Pakistan))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.scanner = QtGui.QWidget()
        self.scanner.setObjectName(_fromUtf8("scanner"))
        self.listView = QtGui.QListView(self.scanner)
        self.listView.setGeometry(QtCore.QRect(0, 0, 782, 505))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMinimumSize(QtCore.QSize(782, 505))
        self.listView.setMaximumSize(QtCore.QSize(782, 505))
        self.listView.setFrameShadow(QtGui.QFrame.Plain)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton = QtGui.QPushButton(self.scanner)
        self.pushButton.setGeometry(QtCore.QRect(560, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semibold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255,255 );}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.scanner)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 30, 91, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 0,0 );}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.scanner)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scanner)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.scanner)
        self.lineEdit.setGeometry(QtCore.QRect(112, 79, 151, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("QLineEdit{background-color: #ddd;\n"
"font: 12pt \"Georgia\";\n"
"color: Black;\n"
"border-radius:5px;}\n"
""))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.scanner)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 29, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8("QLineEdit{background-color: #808098;\n"
"font: 12pt \"Georgia\";\n"
"color: #eee;\n"
"border-radius:5px;}\n"
""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.scanner)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 130, 761, 341))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(761, 341))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(761, 341))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.scanner)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 30, 101, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255,255 );}"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_5 = QtGui.QPushButton(self.scanner)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 80, 91, 31))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(0,250,0);}"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/details.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.scanner, icon1, _fromUtf8(""))
        self.Ports = QtGui.QWidget()
        self.Ports.setObjectName(_fromUtf8("Ports"))
        self.tableWidget = QtGui.QTableWidget(self.Ports)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 781, 490))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(781, 490))
        self.tableWidget.setMaximumSize(QtCore.QSize(0, 0))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 2, item)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/ports.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Ports, icon2, _fromUtf8(""))
        self.vulnerability = QtGui.QWidget()
        self.vulnerability.setObjectName(_fromUtf8("vulnerability"))
        self.pushButton_4 = QtGui.QPushButton(self.vulnerability)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 150, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius:20px;"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/ver.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.vulnerability, icon3, _fromUtf8(""))
        self.About = QtGui.QWidget()
        self.About.setObjectName(_fromUtf8("About"))
        self.textBrowser = QtGui.QTextBrowser(self.About)
        self.textBrowser.setGeometry(QtCore.QRect(150, 60, 461, 381))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/about_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.About, icon4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName(_fromUtf8("menuMain"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuProperties = QtGui.QMenu(self.menubar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuProperties.sizePolicy().hasHeightForWidth())
        self.menuProperties.setSizePolicy(sizePolicy)
        self.menuProperties.setObjectName(_fromUtf8("menuProperties"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Scan = QtGui.QAction(MainWindow)
        self.actionNew_Scan.setObjectName(_fromUtf8("actionNew_Scan"))
        self.actionLoad_Scan = QtGui.QAction(MainWindow)
        self.actionLoad_Scan.setObjectName(_fromUtf8("actionLoad_Scan"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSQL_Attacker = QtGui.QAction(MainWindow)
        self.actionSQL_Attacker.setObjectName(_fromUtf8("actionSQL_Attacker"))
        self.actionBrute_Force = QtGui.QAction(MainWindow)
        self.actionBrute_Force.setObjectName(_fromUtf8("actionBrute_Force"))
        self.actionSystem_Properties = QtGui.QAction(MainWindow)
        self.actionSystem_Properties.setObjectName(_fromUtf8("actionSystem_Properties"))
        self.actionHow_To_Use = QtGui.QAction(MainWindow)
        self.actionHow_To_Use.setObjectName(_fromUtf8("actionHow_To_Use"))
        self.menuMain.addAction(self.actionNew_Scan)
        self.menuMain.addAction(self.actionLoad_Scan)
        self.menuMain.addAction(self.actionSave)
        self.menuMain.addAction(self.actionExit)
        self.menuTools.addAction(self.actionSQL_Attacker)
        self.menuTools.addAction(self.actionBrute_Force)
        self.menuHelp.addAction(self.actionHow_To_Use)
        self.menuProperties.addAction(self.actionSystem_Properties)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuProperties.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("signal1(QTabWidget)")), self.tabWidget.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Start Scan", None))
        self.pushButton_2.setText(_translate("MainWindow", "Stop Scan", None))
        self.label.setText(_translate("MainWindow", "Target IP :", None))
        self.label_2.setText(_translate("MainWindow", "Arugments :", None))
        self.pushButton_3.setText(_translate("MainWindow", "UpLoad File", None))
        self.pushButton_5.setText(_translate("MainWindow", "Save Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scanner), _translate("MainWindow", "Scanner", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Port No", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Details", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "0", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "0", None))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "0", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "0", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "0", None))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "0", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ports), _translate("MainWindow", "Ports", None))
        self.pushButton_4.setText(_translate("MainWindow", "Updated Soon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vulnerability), _translate("MainWindow", "Vulnerability", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#191919\">\n"
"<p align=\"center\" style=\" margin-top:20px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; color:#ffffff;\">Email:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">HassanKhalid50@gmail.com<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; color:#ffffff;\">LinkedIn:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">Hassan khalid</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; color:#ffffff;\">Website:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:11pt; font-weight:600; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">www.Blackmambainc.com</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; color:#ffffff;\">Find Us:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">Office :<br />G-37 Commercial Area Baawalpur, Pakistan<br />Head Office :<br />Air Line Society Main Bolivard Johar Town Lahore,Pakistan </span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("MainWindow", "About", None))
        self.menuMain.setTitle(_translate("MainWindow", "Main", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuProperties.setTitle(_translate("MainWindow", "Properties", None))
        self.actionNew_Scan.setText(_translate("MainWindow", "New Scan", None))
        self.actionNew_Scan.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionLoad_Scan.setText(_translate("MainWindow", "Load Scan", None))
        self.actionLoad_Scan.setShortcut(_translate("MainWindow", "Ctrl+L", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSQL_Attacker.setText(_translate("MainWindow", "SQL Attacker", None))
        self.actionBrute_Force.setText(_translate("MainWindow", "Brute Force", None))
        self.actionSystem_Properties.setText(_translate("MainWindow", "System Properties", None))
        self.actionHow_To_Use.setText(_translate("MainWindow", "How To Use ?", None))
        self.actionHow_To_Use.setShortcut(_translate("MainWindow", "Ctrl+F1", None))

import icons_rc



    
