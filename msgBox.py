# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sh3ll\Desktop\miniwinAmp\msgBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MsgBox_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 117)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textmsg = QtWidgets.QLabel(self.centralwidget)
        self.textmsg.setGeometry(QtCore.QRect(110, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.textmsg.setFont(font)
        self.textmsg.setObjectName("textmsg")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(140, 50, 131, 41))
        self.pushButton_close.setObjectName("pushButton_close")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textmsg.setText(_translate("MainWindow", "В вашем плейлисте нет треков."))
        self.pushButton_close.setText(_translate("MainWindow", "Закрыть"))
