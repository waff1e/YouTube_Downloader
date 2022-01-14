# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoDownloader2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from worker import Worker
from PyQt5.QtCore import pyqtSlot


class Ui_Dialog(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.videoList = []
        self.path = None
        self.isSetPath = False
        
    @pyqtSlot(str)
    def completeNotification(self, title):
        QtWidgets.QMessageBox.about(self, 'Complemet!', f'{title}의 다운로드가 완료되었습니다.')
        self.videoList.clear()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(236, 79)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_path = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_path.setAutoDefault(False)
        self.btn_path.setObjectName("btn_path")
        self.horizontalLayout.addWidget(self.btn_path)
        self.btn_download = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_download.setAutoDefault(False)
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout.addWidget(self.btn_download)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 221, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btn_add = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_add.setAutoDefault(False)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_2.addWidget(self.btn_add)

        self.retranslateUi(Dialog)
        self.btn_path.clicked.connect(self.setPath) # type: ignore
        self.btn_download.clicked.connect(self.download) # type: ignore
        self.btn_add.clicked.connect(self.addVideo) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Youtube Downloader"))
        self.btn_path.setText(_translate("Dialog", "Path"))
        self.btn_download.setText(_translate("Dialog", "Download"))
        self.btn_add.setText(_translate("Dialog", "Add"))

    def setPath(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory()
        self.isSetPath = True
	
    def addVideo(self):
        if not(self.lineEdit.text() == ''):
            self.videoList.insert(0, self.lineEdit.text())
            self.lineEdit.clear()
            self.worker = Worker(self.path, self.videoList)
            self.worker.finished.connect(self.completeNotification)

    def download(self):
        if self.isSetPath and len(self.videoList) > 0:
            self.worker.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())