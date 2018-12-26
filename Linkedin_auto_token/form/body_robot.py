# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
# from PyQt5 import QtWebKitWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.display = QtWidgets.QTextEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(20, 20, 421, 681))
        self.display.setObjectName("display")
        self.display.setReadOnly(True)

        self.web_display = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.web_display.setGeometry(QtCore.QRect(470, 20, 511, 441))
        self.web_display.setUrl(QtCore.QUrl("about:blank"))
        self.web_display.setObjectName("web_display")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(650, 480, 202, 208))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btn_connect = QtWidgets.QPushButton(self.widget)
        self.btn_connect.setMinimumSize(QtCore.QSize(200, 100))
        self.btn_connect.setMaximumSize(QtCore.QSize(200, 100))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)

        self.btn_connect.setFont(font)
        self.btn_connect.setObjectName("btn_connect")
        self.verticalLayout.addWidget(self.btn_connect)
        self.btn_get_token = QtWidgets.QPushButton(self.widget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.btn_get_token.sizePolicy().hasHeightForWidth())
        
        self.btn_get_token.setSizePolicy(sizePolicy)
        self.btn_get_token.setMinimumSize(QtCore.QSize(200, 100))
        self.btn_get_token.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_get_token.setFont(font)
        self.btn_get_token.setObjectName("btn_get_token")
        self.verticalLayout.addWidget(self.btn_get_token)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_connect.setText(_translate("MainWindow", "Connect Linkedid"))
        self.btn_get_token.setText(_translate("MainWindow", "Start robot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


