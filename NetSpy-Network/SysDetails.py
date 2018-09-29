# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sys_details.ui'
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

class Ui_system(object):
    def setupUi(self, system):
        system.setObjectName(_fromUtf8("system"))
        system.resize(803, 587)
        system.setMinimumSize(QtCore.QSize(803, 587))
        system.setMaximumSize(QtCore.QSize(803, 587))
        font = QtGui.QFont()
        font.setPointSize(10)
        system.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/vm-green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        system.setWindowIcon(icon)
        system.setStyleSheet(_fromUtf8("background-color: rgb(27, 27, 27);\n"
"color: rgb(212, 212, 212);"))
        self.details = QtGui.QPlainTextEdit(system)
        self.details.setGeometry(QtCore.QRect(30, 60, 751, 491))
        self.details.setMinimumSize(QtCore.QSize(751, 491))
        self.details.setMaximumSize(QtCore.QSize(751, 491))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.details.setFont(font)
        self.details.setReadOnly(True)
        self.details.setOverwriteMode(False)
        self.details.setBackgroundVisible(False)
        self.details.setObjectName(_fromUtf8("details"))
        self.label = QtGui.QLabel(system)
        self.label.setGeometry(QtCore.QRect(340, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(system)
        QtCore.QMetaObject.connectSlotsByName(system)

    def retranslateUi(self, system):
        system.setWindowTitle(_translate("system", "System Details", None))
        self.details.setPlainText(_translate("system", "hi i am hassn khlaid and i will love to usre py qt for develpoment of my small scsle applications ", None))
        self.label.setText(_translate("system", "System Details", None))

import icons_rc
