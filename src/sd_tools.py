#!/bin/env python

import os
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QDialog, QFileDialog, QPixmap, QCheckBox, QTableWidgetItem
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QBasicTimer, QThread, QString, QStringList
from ui_main import Ui_MainWindow
import ui_dnw
import ui_about
import ui_sdpartition
import commands
import time
import thread

from xml.dom import minidom
#from xml.dom.DOMImplementation import implementation
#import xml.sax.writer
#import xml.utils

class SD_dnw(QDialog, ui_dnw.Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.progressBar.setValue(0)
		self.createTable()
		self.addBtn.clicked.connect(self.do_add)
		self.saveBtn.clicked.connect(self.do_save)
		self.execBtn.clicked.connect(self.do_exec)
		self.do_loadxml()
		self.execThreadStart = 0
	
	def createTable(self):
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(4)
		self.tableWidget.setHorizontalHeaderLabels(QStringList([" ", "cmd", "args", "file"]))
		#self.tableWidget.resizeColumnsToContents()
	
	def execThread(self, cmd):
		print "exec thread start "
		if self.execThreadStart == 1:
			return

		self.execThreadStart = 1
		output = commands.getoutput(cmd)
		self.execThreadStart = 0
		print output

		print "exec thread exit "
		return

	def do_exec(self):
		cmd = ''
		for row in range(self.tableWidget.rowCount()):
			if self.tableWidget.item(row, 0).checkState() == QtCore.Qt.Checked:
				cmd += self.tableWidget.cellWidget(row, 1).currentText() + " " + self.tableWidget.item(row, 2).text() + " " + self.tableWidget.item(row, 3).text() + " && "

		cmd += " sync"
		print str(cmd)
		thread.start_new_thread(self.execThread, (str(cmd), ))
		#self.execThreadStart = 1
		return 	

	@pyqtSlot()
	def do_add(self):
		#print "do_add() \n"
		row = self.tableWidget.rowCount()
		self.tableWidget.setRowCount(row + 1)
		#ckBox = QTableWidgetItem("select %d" %row)
		ckBox = QTableWidgetItem("Active")
		ckBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
		ckBox.setCheckState(QtCore.Qt.Unchecked)
		self.tableWidget.setItem(row, 0, ckBox)

		cbBox = QtGui.QComboBox()
		cbBox.addItem("dnw")
		cbBox.addItem("fastboot")
		self.tableWidget.setCellWidget(row, 1, cbBox)

		self.tableWidget.setItem(row, 2, QTableWidgetItem(QString("0x00000000")))
		self.tableWidget.setItem(row, 3, QTableWidgetItem(QString("./uboot.bin")))

	def do_additem(self, cmd, args, filename):
		row = self.tableWidget.rowCount()
		self.tableWidget.setRowCount(row + 1)
		#ckBox = QTableWidgetItem("select %d" %row)
		ckBox = QTableWidgetItem("Active")
		ckBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
		ckBox.setCheckState(QtCore.Qt.Unchecked)
		self.tableWidget.setItem(row, 0, ckBox)

		cbBox = QtGui.QComboBox()
		cbBox.addItem("dnw")
		cbBox.addItem("fastboot")
		if cmd == "fastboot":
			cbBox.setCurrentIndex(1)
		else:
			cbBox.setCurrentIndex(0)
		self.tableWidget.setCellWidget(row, 1, cbBox)

		self.tableWidget.setItem(row, 2, QTableWidgetItem(QString(args)))
		self.tableWidget.setItem(row, 3, QTableWidgetItem(QString(filename)))
	

	def do_loadxml(self):
		if os.path.exists("cmdstore.xml"):
			dom = minidom.parse("cmdstore.xml")
			root = dom.documentElement
			nodelist = root.getElementsByTagName('cmd')
			for item in nodelist:
				#print item.nodeName

				child_1 = item.getElementsByTagName("cmdname")
				#print child_1[0].nodeName + ":" + child_1[0].childNodes[0].nodeValue
				#print child_1[0].attributes['path'].name + "=" + child_1[0].attributes['path'].value
				
				child_2 = item.getElementsByTagName("args")
				#print child_2[0].nodeName + ":" + child_2[0].childNodes[0].nodeValue

				child_3 = item.getElementsByTagName("file")
				#print child_3[0].nodeName + ":" + child_3[0].childNodes[0].nodeValue
				self.do_additem(child_1[0].childNodes[0].nodeValue, child_2[0].childNodes[0].nodeValue, child_3[0].childNodes[0].nodeValue)
			return 
		else:
			pass

	def do_save(self):
		#dom = minidom.parse("cmdstroe.xml")
		#root = dom.documentElement

		doc = minidom.Document()
		cmdstore = doc.createElement("cmdstore")
		cmdstore.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
		cmdstore.setAttribute('xsi:noNamespaceSchemaLocation','cmdstore.xsd')
		doc.appendChild(cmdstore)

		for row in range(self.tableWidget.rowCount()):
			cmd = doc.createElement("cmd")
			#cmd.setAttribute("path", "/usr/bin")
			#cmd_text = doc.createTextNode("dnw")
			#cmd.appendChild(cmd_text)
			cmdstore.appendChild(cmd)

			cmdname = doc.createElement("cmdname")
			cmdname.setAttribute("path", str("/usr/bin"))
			cmdname_text = doc.createTextNode(str(self.tableWidget.cellWidget(row, 1).currentText()))
			cmdname.appendChild(cmdname_text)
			cmd.appendChild(cmdname)

			args = doc.createElement("args")
			#args.setAttribute("path", "/usr/bin")
			args_text = doc.createTextNode(str(self.tableWidget.item(row, 2).text()))
			args.appendChild(args_text)
			cmd.appendChild(args)

			filepath = doc.createElement("file")
			filepath_text = doc.createTextNode(str(self.tableWidget.item(row, 3).text()))
			filepath.appendChild(filepath_text)
			cmd.appendChild(filepath)

			f = open("cmdstore.xml", 'w')
			#f.write(doc.toprettyxml(indent = ''))
			f.write(doc.toxml())
			f.close()

class SD_about(QDialog, ui_about.Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)

class SD_partition(QDialog, ui_sdpartition.Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.label.setPixmap(QPixmap("./sdpartition.jpg"))	

class msgThread(QThread):
	updated = pyqtSignal(QString)
	def run(self):
		self.updated.emit(QString(self.msg))

#class SD_tool(QMainWindow, Ui_MainWindow, threading.Thread):
#class SD_tool(QMainWindow, Ui_MainWindow, QThread):
class SD_tool(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		#threading.Thread.__init__(self)
		self.setupUi(self)

		self.burnBtn.setDisabled(True)
		self.progressBar.setValue(0)

		#self.dev_table = ["sda", "sdb", "sdc", "sdd", "sde", \
		self.dev_table = ["sdX", "sdb", "sdc", "sdd", "sde", \
				"sdf", "sdg", "sdh", "sdi", "sdj", "sdk"]
		self.timer = QBasicTimer()
		self.step = 0
		self.isRun = False
		self.msg = msgThread(self)
		self.msg.updated.connect(self.showMsgSlot)

		self.action_Dnw.triggered.connect(self.do_dnw)
		self.action_About.triggered.connect(self.do_about)
		self.actionSd_partition.triggered.connect(self.do_sdpartiton)
		self.scanBtn.clicked.connect(self.do_scan)
		self.burnBtn.clicked.connect(self.do_burn)
		self.fileBtn.clicked.connect(self.do_file)
		self.devBox.currentIndexChanged.connect(self.do_indexChanged)

	@pyqtSlot(QString)
	def showMsgSlot(self, msg):
		self.msgBox.insertPlainText(msg + "\n")

	def showMsg(self, msg):
		self.msg.msg = msg
		self.msg.start()
		#self.msgBox.insertPlainText(msg + "\n")
		#pass

	def processThread(self):
	#def run(self):
		self.isRun = True
		bl1_size = 8192
		#bl1_position = 1
		#uboot_position = 49
		#print "processThread start ... \n"
		#self.burnBtn.setDisabled(True)
		#self.devBox.setDisabled(True)
		#self.scanBtn.setDisabled(True)
		#self.fileBox.setDisabled(True)
		if(os.path.exists(self.fileBox.text())):
			file_uboot = open(self.fileBox.text(), "rb")
			#print "open uboot\n"
			try:
				bl1_buf = file_uboot.read(bl1_size)
				#print "read uboot\n"
			finally:
				#print "close uboot\n"
				file_uboot.flush()
				file_uboot.close()

			#print "open bl1\n"
			file_bl1 = open("/tmp/tmp_bl1_8k.bin", "wb")
			try:
				#print "write bl1\n"
				file_bl1.write(bl1_buf)
			finally:
				#print "close bl1\n"
				file_bl1.flush()
				file_bl1.close()

			self.burn_bl1 = "dd iflag=dsync oflag=dsync if=/tmp/tmp_bl1_8k.bin of=" + self.devBox.currentText() +  " seek=1"
			self.burn_uboot = "dd iflag=dsync oflag=dsync if=" + self.fileBox.text() + " of=" + self.devBox.currentText()  + " seek=49"

			#print "run burn bl1\n"
			#self.msgBox.insertPlainText(self.burn_bl1 + "\n")
			output = commands.getoutput(str(self.burn_bl1))
			#self.msgBox.insertPlainText(output.decode("utf8") + "\n")
			self.showMsg(output.decode("utf8"))
			#print output
			time.sleep(1)

			#print "run burn uboot\n"
			#self.msgBox.insertPlainText(self.burn_uboot + "\n")
			output = commands.getoutput(str(self.burn_uboot))
			#self.msgBox.insertPlainText(output.decode("utf8") + "\n")
			self.showMsg(output.decode("utf8"))
			#print output
			time.sleep(2)

			#self.msgBox.insertPlainText("sync\n")
			output = commands.getoutput(str("sync"))
			#self.msgBox.insertPlainText(output.decode("utf8") + "\n")
			self.showMsg(output.decode("utf8"))
			#print output
			time.sleep(5)

		self.isRun = False
		thread.exit_thread()
		return
			
	def timerEvent(self, e):
		if self.step == 99:
			if self.isRun :
				self.step = 0
				self.progressBar.setValue(self.step)
				#print "is Run... \n"
				return
		if self.step >= 100:
			self.timer.stop()
			self.showMsg( "burn Finished\n")

			self.devBox.setDisabled(False)
			self.scanBtn.setDisabled(False)
			self.fileBox.setDisabled(False)
			self.burnBtn.setDisabled(False)
			self.exitBtn.setDisabled(False)
			self.fileBtn.setDisabled(False)
			return
		self.step = self.step + 1
		self.progressBar.setValue(self.step)

	@pyqtSlot()
	def do_file(self):
		#file_img = QFileDialog(self)
		#file_img.setWindowTitle("file")
		#file_img.setNameFilters([self.tr("Binary File (*.bin)"), self.tr("All File (*)")])
		#file_img.setDefaultSuffix(".bin")
		#if(file_img.exec_()):
		#	print file_img.
		file_img = QFileDialog.getOpenFileName(self, "File Open", "./", "*.bin")
		#if(os.path.exists(file_img)):
		if(len(file_img) > 0):
			self.showMsg("use image is " + file_img + "\n")
			self.fileBox.setText(file_img)
			if(self.devBox.count() > 0):
				self.burnBtn.setDisabled(False)
		self.progressBar.setValue(0)

	@pyqtSlot(int)
	def do_indexChanged(self, idx):
		self.msgBox.clear()
		dev = self.devBox.currentText()	
		self.showMsg( "use " + dev + " device\n")
		self.progressBar.setValue(0)

	
	@pyqtSlot()
	def do_scan(self):
		count = self.devBox.count()
		#for j in range(0, count):
		#	self.devBox.removeItem(count - 1 - j)
		if count > 0:
			self.devBox.clear()
		for i in range(0, len(self.dev_table)):
			#print self.dev_table[i]
			#self.devBox.addItems("/dev/" + self.dev_table[i])
			dev = "/dev/" + self.dev_table[i]
			if(os.path.exists(dev)):
				self.devBox.addItem(dev)
		self.devBox.setCurrentIndex(self.devBox.count() - 1)
		if(self.fileBox.text().length() > 0):
			self.burnBtn.setDisabled(False)
		self.progressBar.setValue(0)

	@pyqtSlot()
	def do_burn(self):
		#dev = self.devBox.currentText()	
		#self.msgBox.insertPlainText( "use " + dev + " device\n")

		if(os.path.exists(self.fileBox.text())):
			#thread.start_new(self.processThread, ())
			thread.start_new_thread(self.processThread, ())
			#self.start()
			self.timer.start(100, self)

			#os.system(str(burn_bl1))
			#status, output = commands.getstatusoutput(str(burn_bl1 + "&& " + burn_uboot + " && sync"))
			#os.system(burn_uboot)
			#os.system("sync")
			#loop = True
			#while loop:
			#	if(status == 0):
			#		loop = False
			#	#else:
			#	time.sleep(5)
			#	loop = False
			#		#print "loop ... \n"

		self.devBox.setDisabled(True)
		self.scanBtn.setDisabled(True)
		self.fileBox.setDisabled(True)
		self.burnBtn.setDisabled(True)
		self.exitBtn.setDisabled(True)
		self.fileBtn.setDisabled(True)

	@pyqtSlot()
	def do_dnw(self):
		dialog = SD_dnw()
		dialog.exec_()	

	@pyqtSlot()
	def do_sdpartiton(self):
		dialog = SD_partition()
		dialog.exec_()	

	@pyqtSlot()
	def do_about(self):
		dialog = SD_about()
		dialog.exec_()	
		

def main():
	app = QApplication(sys.argv)
	window = SD_tool()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
