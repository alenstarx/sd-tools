#!/bin/env python
import sys
from PyQt4 import QtGui, QtCore
import ui_xmltree
import ui_xmladd

class xmladd(QtGui.QDialog, ui_xmladd.Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.valueEdt.setEnabled(False)
        self.checkBox.clicked.connect(self.do_check)
    
    def do_check(self):
        if self.checkBox.isChecked():
            self.valueEdt.setEnabled(True)

class xmlcreator(QtGui.QDialog, ui_xmltree.Ui_Dialog): 
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.root = None
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderLabels(['name'])
        self.addBtn.clicked.connect(self.do_add)
        self.delBtn.clicked.connect(self.do_del)
        self.saveBtn.clicked.connect(self.do_save)
        self.loadBtn.clicked.connect(self.do_load)
    
    def newItem(self, parent, name):
        item = QtGui.QTreeWidgetItem(parent, [name])
        #item.setData(column, QtCore.Qt.UserRole, data)
        return item
        
    def do_add(self):
        item = None
        currentItem = self.treeWidget.currentItem()
        #print currentItem
        #print self.treeWidget.topLevelItemCount()
        if currentItem == None and self.treeWidget.topLevelItemCount() == 0:
            currentItem = self.treeWidget
        if currentItem == None and self.treeWidget.topLevelItemCount() != 0:
            print "not parent Node"
            return

        dialog = xmladd()
        if dialog.exec_():
            if self.root == None:
                #print dialog.nameEdt.text()
                #self.root = self.newItem(self.treeWidget.invisibleRootItem(), dialog.nameEdt.text())
                self.root = QtGui.QTreeWidgetItem(currentItem)
                self.root.setText(0, dialog.nameEdt.text())
                self.root.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
                self.treeWidget.addTopLevelItem(self.root)
                item = self.root
                item.setExpanded (True)
            else:
                item = QtGui.QTreeWidgetItem(currentItem)
                item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
                item.setText(0, dialog.nameEdt.text())
                item.setExpanded (True)
                
            if dialog.checkBox.isChecked():
                #print dialog.valueEdt.text()
                #item.setText(1, dialog.valueEdt.text())
                item.setData(0, QtCore.Qt.UserRole, dialog.valueEdt.text())
        dialog.destroy()
        pass

    def do_del(self):
        pass

    def do_save(self):
        pass

    def do_load(self):
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    window = xmlcreator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
