# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sh3ll\Desktop\YaAmp\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background: white;')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBack.setText("")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("icons/back.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(self.icon)
        self.buttonBack.setObjectName("buttonBack")
        self.gridLayout.addWidget(self.buttonBack, 1, 2, 1, 1)
        self.iconVolume = QtWidgets.QLabel(self.centralwidget)
        self.iconVolume.setTextFormat(QtCore.Qt.PlainText)
        self.iconVolume.setObjectName("iconVolume")
        self.gridLayout.addWidget(self.iconVolume, 1, 0, 1, 1)
        self.buttonNext = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonNext.setText("")
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap("icons/next.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(self.icon1)
        self.buttonNext.setObjectName("buttonNext")
        self.gridLayout.addWidget(self.buttonNext, 1, 3, 1, 1)
        self.buttonPlay = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonPlay.setText("")
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("icons/play-button.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(self.icon2)
        self.buttonPlay.setObjectName("buttonPlay")
        self.gridLayout.addWidget(self.buttonPlay, 1, 4, 1, 1)
        self.icon3 = QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap("icons/pause.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        spacerItem = QtWidgets.QSpacerItem(120, 1,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.volSlider = QtWidgets.QSlider(self.centralwidget)
        self.volSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volSlider.setObjectName("volSlider")
        self.gridLayout.addWidget(self.volSlider, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.currentTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentTimeLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.currentTimeLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.currentTimeLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.currentTimeLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.gridLayout_2.addWidget(self.currentTimeLabel, 0, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.fullTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.fullTimeLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.fullTimeLabel.setObjectName("fullTimeLabel")
        self.gridLayout_2.addWidget(self.fullTimeLabel, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(60, 0))
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.listTracks = QtWidgets.QListWidget(self.centralwidget,
                                      itemDoubleClicked
                                      =self.DoubleClickPlay)
        self.listTracks.setObjectName("listTracks")
        self.listTracks.setStyleSheet('background: #d4d4d4;')
        self.verticalLayout_2.addWidget(self.listTracks)
        self.verticalLayout_2.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 21))
        self.menubar.setObjectName("menubar")
        self.menufdsfsd = QtWidgets.QMenu(self.menubar)
        self.menufdsfsd.setObjectName("menufdsfsd")
        self.menuStyles = QtWidgets.QMenu(self.menufdsfsd)
        self.menuStyles.setObjectName("menuStyles")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.StyleBlack = QtWidgets.QAction(MainWindow)
        self.StyleBlack.setObjectName("StyleBlack")
        self.StyleDefault = QtWidgets.QAction(MainWindow)
        self.StyleDefault.setObjectName("StyleDefault")
        self.StyleOrange = QtWidgets.QAction(MainWindow)
        self.StyleOrange.setObjectName("StyleOrange")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menuStyles.addAction(self.StyleDefault)
        self.menuStyles.addAction(self.StyleBlack)
        self.menuStyles.addAction(self.StyleOrange)
        self.menufdsfsd.addAction(self.menuStyles.menuAction())
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menufdsfsd.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Стили написанные вручную

    def style_default(self):
        self.centralwidget.setStyleSheet('background: white; color: black;')
        self.menubar.setStyleSheet('background: white; color:black;')
        self.listTracks.setStyleSheet('background: #d4d4d4;')
        self.icon.addPixmap(QtGui.QPixmap("icons/back.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(self.icon)
        self.icon1.addPixmap(QtGui.QPixmap("icons/next.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(self.icon1)
        self.icon2.addPixmap(QtGui.QPixmap("icons/play-button.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(self.icon2)
        self.icon3.addPixmap(QtGui.QPixmap("icons/pause.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconLabel = QtGui.QPixmap(
            'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/volume.png')
        self.iconVolume.setPixmap(self.iconLabel)

    def style_black(self):
        self.centralwidget.setStyleSheet('background: #282829; color: #fff;')
        self.listTracks.setStyleSheet('background: #1a1a1a;')
        self.icon.addPixmap(QtGui.QPixmap("icons/back_white.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(self.icon)
        self.icon1.addPixmap(QtGui.QPixmap("icons/next_white.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(self.icon1)
        self.icon2.addPixmap(QtGui.QPixmap("icons/play-button_white.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(self.icon2)
        self.icon3.addPixmap(QtGui.QPixmap("icons/pause_white.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconLabel = QtGui.QPixmap(
            'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/volume_white.png')
        self.iconVolume.setPixmap(self.iconLabel)
        self.menubar.setStyleSheet('background: #282829; color: white;')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "miniWinamp"))
        self.iconVolume.setText(_translate("MainWindow", "icon"))
        self.currentTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.fullTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.menufdsfsd.setTitle(_translate("MainWindow", "Стили"))
        self.menuStyles.setTitle(_translate("MainWindow", "Styles/Стили"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.StyleBlack.setText(_translate("MainWindow", "Тёмный"))
        self.StyleDefault.setText(
            _translate("MainWindow", "Светлый (по умолчанию)"))
        self.StyleOrange.setText(_translate("MainWindow", "Оранжевый"))
        self.action_3.setText(_translate("MainWindow", "Открыть"))
