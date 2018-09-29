# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sys_details.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import subprocess
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

class Ui_system(object):
    def setupUi(self, system):
        system.setObjectName(_fromUtf8("system"))
        system.resize(660, 552)
        font = QtGui.QFont()
        font.setPointSize(10)
        system.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/vm-green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        system.setWindowIcon(icon)
        system.setStyleSheet(_fromUtf8("background-color: rgb(27, 27, 27);\n"
"color: rgb(212, 212, 212);"))
        self.plainTextEdit = QtGui.QPlainTextEdit(system)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 60, 601, 471))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(system)
        self.label.setGeometry(QtCore.QRect(300, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(system)
        QtCore.QMetaObject.connectSlotsByName(system)

        self.output=subprocess.check_output('systeminfo',shell=True)
        self.output.encode('utf-8')
        self.plainTextEdit.clear();
        self.plainTextEdit.appendPlainText(self.output);


    def retranslateUi(self, system):
        system.setWindowTitle(_translate("system", "System Details", None))
        self.plainTextEdit.setPlainText(_translate("system"," ", None))
        self.label.setText(_translate("system", "System Details", None))

import icons_rc
