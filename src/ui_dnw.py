# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dnw.ui'
#
# Created: Wed May 14 11:42:56 2014
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.exitBtn = QtGui.QPushButton(Dialog)
        self.exitBtn.setGeometry(QtCore.QRect(290, 260, 93, 27))
        self.exitBtn.setObjectName("exitBtn")
        self.execBtn = QtGui.QPushButton(Dialog)
        self.execBtn.setGeometry(QtCore.QRect(180, 260, 93, 27))
        self.execBtn.setObjectName("execBtn")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 260, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.addBtn = QtGui.QPushButton(Dialog)
        self.addBtn.setGeometry(QtCore.QRect(300, 20, 93, 27))
        self.addBtn.setObjectName("addBtn")
        self.delBtn = QtGui.QPushButton(Dialog)
        self.delBtn.setGeometry(QtCore.QRect(300, 60, 93, 27))
        self.delBtn.setObjectName("delBtn")
        self.upBtn = QtGui.QPushButton(Dialog)
        self.upBtn.setGeometry(QtCore.QRect(300, 110, 93, 27))
        self.upBtn.setObjectName("upBtn")
        self.downBtn = QtGui.QPushButton(Dialog)
        self.downBtn.setGeometry(QtCore.QRect(300, 150, 93, 27))
        self.downBtn.setObjectName("downBtn")
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.saveBtn = QtGui.QPushButton(Dialog)
        self.saveBtn.setGeometry(QtCore.QRect(290, 220, 93, 27))
        self.saveBtn.setObjectName("saveBtn")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.exitBtn, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.exitBtn.setText(QtGui.QApplication.translate("Dialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.execBtn.setText(QtGui.QApplication.translate("Dialog", "Exec", None, QtGui.QApplication.UnicodeUTF8))
        self.addBtn.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.delBtn.setText(QtGui.QApplication.translate("Dialog", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.upBtn.setText(QtGui.QApplication.translate("Dialog", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downBtn.setText(QtGui.QApplication.translate("Dialog", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBtn.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))

