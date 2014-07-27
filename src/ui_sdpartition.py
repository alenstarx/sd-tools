# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sdpartition.ui'
#
# Created: Tue May 13 10:33:27 2014
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 123, 581, 121))
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 103))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("Dialog", "SD卡一块的大小为512B，第一块为保留块，紧接着的8K存放BL1，所以BL1烧写的起始块标号为1，这也就是第二条烧写命令中seek=1的来源了；接下来存放环境变量，有的资料中将环境变量与BL1文件总称为BL1文件，不过这是的BL1文件就不再是8K大小了，而是加上环境变量的大小共24K了，也就是48块；之后存放BL2文件，也就是uboot.bin，起始块标号49。最后的部分是我们自己的其他使用拷贝空间了。", None, QtGui.QApplication.UnicodeUTF8))

