# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Netspy.ui'
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
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 641)
        MainWindow.setMaximumSize(QtCore.QSize(800, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/network.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"background-color: rgb(0, 147, 221);}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 80, 801, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 90, 20, 471))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(430, 10, 81, 31))
        self.start.setStyleSheet(_fromUtf8("QPushButton{background-color: rgb(85, 170, 255);\n"
"    color: rgb(0, 40, 90);\n"
"font-size:12px;\n"
"border-radius:5px;\n"
"font-family:Georgial;\n"
"border:1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(221, 198, 103);}"))
        self.start.setObjectName(_fromUtf8("start"))
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(430, 50, 81, 31))
        self.stop.setStyleSheet(_fromUtf8("QPushButton{background-color: rgb(85, 170, 255);\n"
"color:white;\n"
"font-size:12px;\n"
"border-radius:5px;\n"
"font-family:Georgial;\n"
"border:1px solid grey;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"background-color: rgb(188, 0, 0);\n"
"color: rgb(,220,30);}"))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(120, 90, 671, 471))
        self.tabWidget.setMinimumSize(QtCore.QSize(671, 471))
        self.tabWidget.setMaximumSize(QtCore.QSize(671, 471))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Details = QtGui.QWidget()
        self.Details.setObjectName(_fromUtf8("Details"))
        self.listView = QtGui.QListView(self.Details)
        self.listView.setGeometry(QtCore.QRect(0, 0, 661, 441))
        self.listView.setMinimumSize(QtCore.QSize(661, 441))
        self.listView.setMaximumSize(QtCore.QSize(661, 441))
        self.listView.setObjectName(_fromUtf8("listView"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/details.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Details, icon1, _fromUtf8(""))
        self.Ports = QtGui.QWidget()
        self.Ports.setObjectName(_fromUtf8("Ports"))
        self.tableWidget = QtGui.QTableWidget(self.Ports)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 671, 441))
        self.tableWidget.setMinimumSize(QtCore.QSize(671, 441))
        self.tableWidget.setMaximumSize(QtCore.QSize(671, 441))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/ports.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Ports, icon2, _fromUtf8(""))
        self.vulnerability = QtGui.QWidget()
        self.vulnerability.setObjectName(_fromUtf8("vulnerability"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/ver.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.vulnerability, icon3, _fromUtf8(""))
        self.BruteForce = QtGui.QWidget()
        self.BruteForce.setObjectName(_fromUtf8("BruteForce"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/brute.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.BruteForce, icon4, _fromUtf8(""))
        self.SQLAttack = QtGui.QWidget()
        self.SQLAttack.setObjectName(_fromUtf8("SQLAttack"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/sqlmap.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.SQLAttack, icon5, _fromUtf8(""))
        self.About = QtGui.QWidget()
        self.About.setObjectName(_fromUtf8("About"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/about_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.About, icon6, _fromUtf8(""))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(530, 0, 271, 91))
        self.textBrowser.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Raised)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 181, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("QLineEdit{background-color: #808080;\n"
"font: 12pt \"Georgia\";\n"
"color: #eee;\n"
"border-radius:5px;}\n"
""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 81, 31))
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"    font: 11pt \"Cambria\";\n"
"\n"
"color: rgb(255, 255, 255);}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.uploadfile = QtGui.QPushButton(self.centralwidget)
        self.uploadfile.setGeometry(QtCore.QRect(290, 10, 91, 31))
        self.uploadfile.setStyleSheet(_fromUtf8("QPushButton{background-color: rgb(85, 170, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"border : 1px solid;\n"
"color:white;\n"
"\n"
"border-radius:5px;\n"
"font: 75 8pt \"MS Sans Serif\";\n"
";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(85, 85, 255);\n"
"\n"
"color: rgb(221, 198, 103);}"))
        self.uploadfile.setObjectName(_fromUtf8("uploadfile"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 50, 181, 31))
        self.lineEdit_2.setStyleSheet(_fromUtf8("QLineEdit{background-color: #808080;\n"
"font: 12pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:5px;}\n"
""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 31))
        self.label_2.setStyleSheet(_fromUtf8("QLabel{\n"
"    font: 11pt \"Cambria\";\n"
"\n"
"color: rgb(255, 255, 255);}"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(290, 50, 91, 31))
        self.lcdNumber.setMinimumSize(QtCore.QSize(91, 31))
        self.lcdNumber.setMaximumSize(QtCore.QSize(91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft New Tai Lue"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet(_fromUtf8("color: rgb(127, 0, 0);\n"
"border-color:red;\n"
"border:1px Solid Blue;"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.tableWidget1 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget1.setEnabled(True)
        self.tableWidget1.setGeometry(QtCore.QRect(0, 90, 121, 471))
        self.tableWidget1.setMinimumSize(QtCore.QSize(121, 471))
        self.tableWidget1.setMaximumSize(QtCore.QSize(121, 471))
        self.tableWidget1.setAcceptDrops(False)
        self.tableWidget1.setAutoFillBackground(False)
        self.tableWidget1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget1.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget1.setTabKeyNavigation(False)
        self.tableWidget1.setProperty("showDropIndicator", False)
        self.tableWidget1.setDragDropOverwriteMode(False)
        self.tableWidget1.setAlternatingRowColors(True)
        self.tableWidget1.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.tableWidget1.setShowGrid(True)
        self.tableWidget1.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget1.setObjectName(_fromUtf8("tableWidget1"))
        self.tableWidget1.setColumnCount(1)
        self.tableWidget1.setRowCount(7)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 155))
        self.tableWidget1.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(89, 187, 55))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 570, 91, 31))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{background-color: #eee;\n"
"font: 10pt \"Georgia\";\n"
"color: rgb(255, 85, 0);\n"
"border-radius:5px;}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(139, 139, 139);\n"
"color:white;l}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.blackmamba = QtGui.QCommandLinkButton(self.centralwidget)
        self.blackmamba.setGeometry(QtCore.QRect(10, 560, 171, 61))
        self.blackmamba.setMinimumSize(QtCore.QSize(171, 61))
        self.blackmamba.setMaximumSize(QtCore.QSize(171, 61))
        self.blackmamba.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.blackmamba.setFont(font)
        self.blackmamba.setWhatsThis(_fromUtf8(""))
        self.blackmamba.setAccessibleName(_fromUtf8(""))
        self.blackmamba.setAccessibleDescription(_fromUtf8(""))
        self.blackmamba.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.blackmamba.setText(_fromUtf8("Black Mamba Inc."))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Working Html Projects/blm.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blackmamba.setIcon(icon7)
        self.blackmamba.setIconSize(QtCore.QSize(36, 32))
        self.blackmamba.setObjectName(_fromUtf8("blackmamba"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName(_fromUtf8("menuMain"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setMaximumSize(QtCore.QSize(800, 600))
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuSystem_Details = QtGui.QMenu(self.menubar)
        self.menuSystem_Details.setObjectName(_fromUtf8("menuSystem_Details"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Scan = QtGui.QAction(MainWindow)
        self.actionNew_Scan.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.actionNew_Scan.setObjectName(_fromUtf8("actionNew_Scan"))
        self.actionSave_Scan = QtGui.QAction(MainWindow)
        self.actionSave_Scan.setObjectName(_fromUtf8("actionSave_Scan"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionReport_Bug = QtGui.QAction(MainWindow)
        self.actionReport_Bug.setObjectName(_fromUtf8("actionReport_Bug"))
        self.actionFeed_back = QtGui.QAction(MainWindow)
        self.actionFeed_back.setObjectName(_fromUtf8("actionFeed_back"))
        self.actionBrute_Force = QtGui.QAction(MainWindow)
        self.actionBrute_Force.setObjectName(_fromUtf8("actionBrute_Force"))
        self.actionSQLMAP = QtGui.QAction(MainWindow)
        self.actionSQLMAP.setObjectName(_fromUtf8("actionSQLMAP"))
        self.actionContact_US = QtGui.QAction(MainWindow)
        self.actionContact_US.setObjectName(_fromUtf8("actionContact_US"))
        self.actionVulnerability = QtGui.QAction(MainWindow)
        self.actionVulnerability.setObjectName(_fromUtf8("actionVulnerability"))
        self.menuMain.addAction(self.actionNew_Scan)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionSave_Scan)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionExit)
        self.menuTools.addAction(self.actionBrute_Force)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionSQLMAP)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionVulnerability)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuHelp.addAction(self.actionFeed_back)
        self.menuAbout.addAction(self.actionContact_US)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuSystem_Details.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NetSpy", None))
        self.start.setText(_translate("MainWindow", "Start Scan", None))
        self.stop.setText(_translate("MainWindow", "Stop Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Details), _translate("MainWindow", "Details", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ports), _translate("MainWindow", "Ports", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vulnerability), _translate("MainWindow", "Vulnerability", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BruteForce), _translate("MainWindow", "Brute Force", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SQLAttack), _translate("MainWindow", "SQL Attack", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("MainWindow", "About", None))
        self.label.setText(_translate("MainWindow", "   Target IP :", None))
        self.uploadfile.setText(_translate("MainWindow", "Upload TextFile", None))
        self.label_2.setText(_translate("MainWindow", "   Args :", None))
        item = self.tableWidget1.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget1.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tableWidget1.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.tableWidget1.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4", None))
        item = self.tableWidget1.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5", None))
        item = self.tableWidget1.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6", None))
        item = self.tableWidget1.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7", None))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hosts", None))
        self.pushButton.setText(_translate("MainWindow", "Save Log", None))
        self.menuMain.setTitle(_translate("MainWindow", "Main", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuSystem_Details.setTitle(_translate("MainWindow", "System Details", None))
        self.actionNew_Scan.setText(_translate("MainWindow", "New Scan", None))
        self.actionSave_Scan.setText(_translate("MainWindow", "Save Scan", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionReport_Bug.setText(_translate("MainWindow", "Report Bug", None))
        self.actionFeed_back.setText(_translate("MainWindow", "Feed back", None))
        self.actionBrute_Force.setText(_translate("MainWindow", "Brute Force", None))
        self.actionSQLMAP.setText(_translate("MainWindow", "SQLMAP", None))
        self.actionContact_US.setText(_translate("MainWindow", "Contact US", None))
        self.actionVulnerability.setText(_translate("MainWindow", "Vulnerability", None))

import icons_rc
