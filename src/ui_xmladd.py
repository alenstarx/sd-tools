# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml_add.ui'
#
# Created: Fri May 16 14:17:40 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 147)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 110, 151, 31))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.nameEdt = QtGui.QLineEdit(Dialog)
        self.nameEdt.setGeometry(QtCore.QRect(130, 20, 231, 23))
        self.nameEdt.setObjectName(_fromUtf8("nameEdt"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 24, 57, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(30, 60, 85, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.valueEdt = QtGui.QLineEdit(Dialog)
        self.valueEdt.setEnabled(True)
        self.valueEdt.setGeometry(QtCore.QRect(130, 80, 231, 23))
        self.valueEdt.setObjectName(_fromUtf8("valueEdt"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 57, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Name : ", None))
        self.checkBox.setText(_translate("Dialog", "is Node", None))
        self.label_2.setText(_translate("Dialog", "Value :", None))

