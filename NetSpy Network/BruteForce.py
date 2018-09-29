# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BruteForce.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os
import SystemDetails
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

    def __init__(self):
        self.message=QtGui.QMessageBox()
        self.obj=QtGui.QFileDialog()

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
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.startButton = QtGui.QPushButton(self.scanner)
        self.startButton.setGeometry(QtCore.QRect(30, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semibold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255,255 );}"))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.startButton.clicked.connect(self.start_scan)

        self.stopButton = QtGui.QPushButton(self.scanner)
        self.stopButton.setGeometry(QtCore.QRect(180, 390, 91, 31))
        self.stopButton.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 0,0 );}"))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))

        self.stopButton.clicked.connect(self.stop_scan)
        self.label = QtGui.QLabel(self.scanner)
        self.label.setGeometry(QtCore.QRect(40, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color:#ddd;\n"
"color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.Smtp = QtGui.QLineEdit(self.scanner)
        self.Smtp.setGeometry(QtCore.QRect(200, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Smtp.setFont(font)
        self.Smtp.setStyleSheet(_fromUtf8("QLineEdit{background-color: #808098;\n"
"font: 12pt \"Georgia\";\n"
"color: #eee;\n"
"border-radius:5px;}\n"
""))
        self.Smtp.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Smtp.setObjectName(_fromUtf8("Smtp"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.scanner)
        self.plainTextEdit.setGeometry(QtCore.QRect(450, 50, 291, 341))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(752, 431))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet(_fromUtf8("QPlainTextEdit{border-radius:15px;\n"
"border: 1px solid grey;}\n"
""))
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.upload_button = QtGui.QPushButton(self.scanner)
        self.upload_button.setGeometry(QtCore.QRect(90, 290, 101, 31))
        self.upload_button.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255,255 );}"))
        self.upload_button.setObjectName(_fromUtf8("upload_button"))
        self.upload_button.clicked.connect(self.upload_file_function)
        self.upload_button.setStatusTip("Upload Password File ")
        self.logButton = QtGui.QPushButton(self.scanner)
        self.logButton.setGeometry(QtCore.QRect(600, 430, 91, 31))
        self.logButton.setStyleSheet(_fromUtf8("QPushButton{color: rgb(25, 25, 25);\n"
"border:1px solid Black;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(0,250,0);}"))
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.logButton.clicked.connect(self.log_function)
        self.logButton.setStatusTip("Save To Current Directory")
        self.label_2 = QtGui.QLabel(self.scanner)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background-color:#ddd;\n"
"color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scanner)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background-color:#ddd;\n"
"color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Email = QtGui.QLineEdit(self.scanner)
        self.Email.setGeometry(QtCore.QRect(200, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Email.setFont(font)
        self.Email.setStyleSheet(_fromUtf8("QLineEdit{background-color: #808098;\n"
"font: 12pt \"Georgia\";\n"
"color: #eee;\n"
"border-radius:5px;}\n"
""))
        self.Email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Email.setObjectName(_fromUtf8("Email"))
        self.port = QtGui.QLineEdit(self.scanner)
        self.port.setGeometry(QtCore.QRect(200, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.port.setFont(font)
        self.port.setStyleSheet(_fromUtf8("QLineEdit{background-color: #808098;\n"
"font: 12pt \"Georgia\";\n"
"color: #eee;\n"
"border-radius:5px;}\n"
""))
        self.port.setInputMethodHints(QtCore.Qt.ImhNone)
        self.port.setObjectName(_fromUtf8("port"))
        self.label_4 = QtGui.QLabel(self.scanner)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("background-color:#ddd;\n"
"color: rgb(25, 25, 25);\n"
"border-radius:5px;\n"
""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/brute.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.scanner, icon1, _fromUtf8(""))
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
        self.actionNew_Scan.triggered.connect(self.new_attack)
        self.actionLoad_Scan = QtGui.QAction(MainWindow)
        self.actionLoad_Scan.setObjectName(_fromUtf8("actionLoad_Scan"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setStatusTip("Exit")
        self.actionExit.triggered.connect(self.exit)
        self.actionSQL_Attacker = QtGui.QAction(MainWindow)
        self.actionSQL_Attacker.setObjectName(_fromUtf8("actionSQL_Attacker"))
        self.actionBrute_Force = QtGui.QAction(MainWindow)
        self.actionBrute_Force.setObjectName(_fromUtf8("actionBrute_Force"))
        self.actionSystem_Properties = QtGui.QAction(MainWindow)
        self.actionSystem_Properties.setObjectName(_fromUtf8("actionSystem_Properties"))
        self.actionSystem_Properties.setStatusTip("System Details")
        self.actionSystem_Properties.triggered.connect(self.system_prop)
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("signal1(QTabWidget)")), self.tabWidget.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.centralwidget.setStatusTip("Brute Force Application")

    def new_attack(self):
        self.port.clear()
        self.Email.clear()
        self.Smtp.clear()
        self.plainTextEdit.clear()

    def exit(self):
        sys.exit()

    def stop_scan(self):
        print "stop Called"

    def log_function(self):
        print "Log Called"

    def upload_file_function(self):
        self.path = os.getcwd()
        self.file_ = QtGui.QFileDialog.getOpenFileName(self.obj, 'Multiple File', self.path, '*.txt')
        self.password_file_handler()

    def password_file_handler(self):

        f = open(self.file_, 'rb')
        lines = f.readlines()
        self.list_password = lines

    def start_scan(self):
        if len(self.Smtp.text())!=0 and len(self.Email.text())!=0 and len(self.port.text())!=0:
            print 'Start Scaning'
        else:
            QtGui.QMessageBox.information(self.message,"Please Enter Input Correctly","Input Error Can Not BruteForce ")

    def system_prop(self):
        self.system_prop = QtGui.QWidget()
        self.sys = SystemDetails.Ui_system()
        self.sys.setupUi(self.system_prop)
        self.system_prop.show()




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.label.setText(_translate("MainWindow", "  Enter SMTP Server :", None))
        self.Smtp.setPlaceholderText(_translate("MainWindow", "        Smtp server", None))
        self.upload_button.setText(_translate("MainWindow", "UpLoad File", None))
        self.logButton.setText(_translate("MainWindow", "Save Log", None))
        self.label_2.setText(_translate("MainWindow", "    Enter SMTP Port :", None))
        self.label_3.setText(_translate("MainWindow", "      Enter Email :", None))
        self.Email.setPlaceholderText(_translate("MainWindow", "             Email", None))
        self.port.setPlaceholderText(_translate("MainWindow", "              Port", None))
        self.label_4.setText(_translate("MainWindow", "      Please Upload Password List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scanner), _translate("MainWindow", "Brute Force", None))
        self.menuMain.setTitle(_translate("MainWindow", "Main", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuProperties.setTitle(_translate("MainWindow", "Properties", None))
        self.actionNew_Scan.setText(_translate("MainWindow", "New Start", None))
        self.actionNew_Scan.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionLoad_Scan.setText(_translate("MainWindow", "Load Results", None))
        self.actionLoad_Scan.setShortcut(_translate("MainWindow", "Ctrl+L", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSQL_Attacker.setText(_translate("MainWindow", "SQL Attacker", None))
        self.actionBrute_Force.setText(_translate("MainWindow", "Scanner", None))
        self.actionSystem_Properties.setText(_translate("MainWindow", "System Properties", None))
        self.actionHow_To_Use.setText(_translate("MainWindow", "How To Use ?", None))
        self.actionHow_To_Use.setShortcut(_translate("MainWindow", "Ctrl+F1", None))

import icons_rc
