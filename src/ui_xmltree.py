# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xmltree.ui'
#
# Created: Fri May 16 14:20:13 2014
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
        Dialog.resize(400, 300)
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(30, 30, 256, 192))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.addBtn = QtGui.QPushButton(Dialog)
        self.addBtn.setGeometry(QtCore.QRect(310, 30, 80, 23))
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        self.delBtn = QtGui.QPushButton(Dialog)
        self.delBtn.setGeometry(QtCore.QRect(310, 70, 80, 23))
        self.delBtn.setObjectName(_fromUtf8("delBtn"))
        self.propBtn = QtGui.QPushButton(Dialog)
        self.propBtn.setGeometry(QtCore.QRect(310, 130, 80, 23))
        self.propBtn.setObjectName(_fromUtf8("propBtn"))
        self.saveBtn = QtGui.QPushButton(Dialog)
        self.saveBtn.setGeometry(QtCore.QRect(310, 190, 80, 23))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.exitBtn = QtGui.QPushButton(Dialog)
        self.exitBtn.setGeometry(QtCore.QRect(310, 230, 80, 23))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(310, 100, 85, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.loadBtn = QtGui.QPushButton(Dialog)
        self.loadBtn.setGeometry(QtCore.QRect(310, 160, 80, 23))
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.exitBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.addBtn.setText(_translate("Dialog", "Add", None))
        self.delBtn.setText(_translate("Dialog", "del", None))
        self.propBtn.setText(_translate("Dialog", "property", None))
        self.saveBtn.setText(_translate("Dialog", "Save", None))
        self.exitBtn.setText(_translate("Dialog", "Exit", None))
        self.checkBox.setText(_translate("Dialog", "Multi-root", None))
        self.loadBtn.setText(_translate("Dialog", "Load", None))

