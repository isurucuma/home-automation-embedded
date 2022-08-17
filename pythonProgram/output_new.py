# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUCorik.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 450))
        MainWindow.setMaximumSize(QSize(700, 450))
        MainWindow.setWindowOpacity(0.980000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(-40, -90, 800, 600))
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setStyleSheet(u"background-color: rgb(42, 42, 42);\n"
"border-radius:20px;")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Plain)
        self.frame = QFrame(self.mainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(570, 340, 151, 161))
        self.frame.setStyleSheet(u"background-color: rgb(80, 64, 90);\n"
"border-radius:10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lightsBtn3 = QPushButton(self.frame)
        self.lightsBtn3.setObjectName(u"lightsBtn3")
        self.lightsBtn3.setGeometry(QRect(50, 120, 51, 31))
        self.lightsBtn3.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.lightsBtn3.setCheckable(True)
        self.lightsBtn1 = QPushButton(self.frame)
        self.lightsBtn1.setObjectName(u"lightsBtn1")
        self.lightsBtn1.setGeometry(QRect(50, 40, 51, 31))
        self.lightsBtn1.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.lightsBtn1.setCheckable(True)
        self.lightsBtn2 = QPushButton(self.frame)
        self.lightsBtn2.setObjectName(u"lightsBtn2")
        self.lightsBtn2.setGeometry(QRect(50, 80, 51, 31))
        self.lightsBtn2.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.lightsBtn2.setCheckable(True)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 0, 71, 41))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 700 14pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.frame_2 = QFrame(self.mainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(410, 170, 311, 151))
        self.frame_2.setStyleSheet(u"background-color: rgb(72, 98, 107);\n"
"border-radius:10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 55, 121, 20))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(221, 221, 221);")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 100, 121, 20))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(221, 221, 221);")
        self.humidLabel = QLabel(self.frame_2)
        self.humidLabel.setObjectName(u"humidLabel")
        self.humidLabel.setGeometry(QRect(190, 100, 51, 20))
        sizePolicy.setHeightForWidth(self.humidLabel.sizePolicy().hasHeightForWidth())
        self.humidLabel.setSizePolicy(sizePolicy)
        self.humidLabel.setFont(font1)
        self.humidLabel.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(221, 221, 221);")
        self.tempLabel = QLabel(self.frame_2)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(190, 55, 61, 21))
        sizePolicy.setHeightForWidth(self.tempLabel.sizePolicy().hasHeightForWidth())
        self.tempLabel.setSizePolicy(sizePolicy)
        self.tempLabel.setFont(font1)
        self.tempLabel.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(221, 221, 221);")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 0, 91, 41))
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.frame_3 = QFrame(self.mainFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 280, 331, 221))
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 90, 66);\n"
"border-radius:10px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 10, 121, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.timeEdit_11 = QTimeEdit(self.frame_3)
        self.timeEdit_11.setObjectName(u"timeEdit_11")
        self.timeEdit_11.setGeometry(QRect(80, 80, 81, 22))
        self.timeEdit_11.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border-radius:2px;")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 80, 51, 20))
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(221, 221, 221);")
        self.timeEdit_12 = QTimeEdit(self.frame_3)
        self.timeEdit_12.setObjectName(u"timeEdit_12")
        self.timeEdit_12.setGeometry(QRect(180, 80, 81, 22))
        self.timeEdit_12.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border-radius:2px;")
        self.timerBtn1 = QPushButton(self.frame_3)
        self.timerBtn1.setObjectName(u"timerBtn1")
        self.timerBtn1.setGeometry(QRect(280, 80, 41, 21))
        self.timerBtn1.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.timerBtn1.setCheckable(True)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 120, 51, 20))
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(221, 221, 221);")
        self.timerBtn2 = QPushButton(self.frame_3)
        self.timerBtn2.setObjectName(u"timerBtn2")
        self.timerBtn2.setGeometry(QRect(280, 120, 41, 21))
        self.timerBtn2.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.timerBtn2.setCheckable(True)
        self.timeEdit_22 = QTimeEdit(self.frame_3)
        self.timeEdit_22.setObjectName(u"timeEdit_22")
        self.timeEdit_22.setGeometry(QRect(180, 120, 81, 22))
        self.timeEdit_22.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border-radius:2px;")
        self.timeEdit_21 = QTimeEdit(self.frame_3)
        self.timeEdit_21.setObjectName(u"timeEdit_21")
        self.timeEdit_21.setGeometry(QRect(80, 120, 81, 22))
        self.timeEdit_21.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border-radius:2px;")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 160, 51, 20))
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(221, 221, 221);")
        self.timerBtn3 = QPushButton(self.frame_3)
        self.timerBtn3.setObjectName(u"timerBtn3")
        self.timerBtn3.setGeometry(QRect(280, 160, 41, 21))
        self.timerBtn3.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.timerBtn3.setCheckable(True)
        self.timeEdit_32 = QTimeEdit(self.frame_3)
        self.timeEdit_32.setObjectName(u"timeEdit_32")
        self.timeEdit_32.setGeometry(QRect(180, 160, 81, 22))
        self.timeEdit_32.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border-radius:2px;")
        self.timeEdit_31 = QTimeEdit(self.frame_3)
        self.timeEdit_31.setObjectName(u"timeEdit_31")
        self.timeEdit_31.setGeometry(QRect(80, 160, 81, 22))
        self.timeEdit_31.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border-radius:2px;")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 50, 31, 20))
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(210, 50, 31, 20))
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.frame_4 = QFrame(self.mainFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(60, 170, 331, 91))
        self.frame_4.setStyleSheet(u"background-color: rgb(131, 57, 58);\n"
"border-radius:10px")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 10, 201, 41))
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 60, 201, 20))
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_11 = QLabel(self.mainFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 110, 411, 41))
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"font: 700 16pt \"Calibri\";\n"
"background-color: rgb(98, 98, 73);\n"
"color: rgb(221, 221, 221);\n"
"border-radius:10px;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.frame_5 = QFrame(self.mainFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(410, 340, 151, 161))
        self.frame_5.setStyleSheet(u"background-color: rgb(62, 84, 121);\n"
"border-radius:10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.tempSetBtn3 = QPushButton(self.frame_5)
        self.tempSetBtn3.setObjectName(u"tempSetBtn3")
        self.tempSetBtn3.setGeometry(QRect(100, 120, 41, 21))
        self.tempSetBtn3.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.tempSetBtn3.setCheckable(True)
        self.tempSetBtn1 = QPushButton(self.frame_5)
        self.tempSetBtn1.setObjectName(u"tempSetBtn1")
        self.tempSetBtn1.setGeometry(QRect(100, 40, 41, 21))
        self.tempSetBtn1.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.tempSetBtn1.setCheckable(True)
        self.tempSetBtn2 = QPushButton(self.frame_5)
        self.tempSetBtn2.setObjectName(u"tempSetBtn2")
        self.tempSetBtn2.setGeometry(QRect(100, 80, 41, 21))
        self.tempSetBtn2.setStyleSheet(u"color: rgb(249, 228, 245);\n"
"background-color: rgb(44, 43, 31);\n"
"border-radius:10px;\n"
"")
        self.tempSetBtn2.setCheckable(True)
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 0, 111, 41))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"font: 700 14pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.tempOnDial = QDial(self.frame_5)
        self.tempOnDial.setObjectName(u"tempOnDial")
        self.tempOnDial.setGeometry(QRect(0, 40, 41, 51))
        self.tempOnDial.setMinimum(12)
        self.tempOnDial.setMaximum(45)
        self.tempOffDial = QDial(self.frame_5)
        self.tempOffDial.setObjectName(u"tempOffDial")
        self.tempOffDial.setGeometry(QRect(0, 90, 41, 61))
        self.tempOffDial.setMinimum(12)
        self.tempOffDial.setMaximum(45)
        self.tempOffLbl = QLabel(self.frame_5)
        self.tempOffLbl.setObjectName(u"tempOffLbl")
        self.tempOffLbl.setGeometry(QRect(50, 110, 31, 20))
        sizePolicy1.setHeightForWidth(self.tempOffLbl.sizePolicy().hasHeightForWidth())
        self.tempOffLbl.setSizePolicy(sizePolicy1)
        self.tempOffLbl.setFont(font2)
        self.tempOffLbl.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.tempOnLbl = QLabel(self.frame_5)
        self.tempOnLbl.setObjectName(u"tempOnLbl")
        self.tempOnLbl.setGeometry(QRect(50, 60, 31, 20))
        sizePolicy1.setHeightForWidth(self.tempOnLbl.sizePolicy().hasHeightForWidth())
        self.tempOnLbl.setSizePolicy(sizePolicy1)
        self.tempOnLbl.setFont(font2)
        self.tempOnLbl.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 40, 31, 20))
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"font: 700 10pt \"Calibri\";\n"
"color: rgb(221, 221, 221);")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 90, 31, 20))
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"font: 700 10pt \"Calibri\";\n"
"color: rgb(221, 221, 221);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.frame_2.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.label_11.raise_()
        self.frame_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.lightsBtn1.clicked.connect(self.humidLabel.update)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Portable Home Automation System", None))
        self.lightsBtn3.setText(QCoreApplication.translate("MainWindow", u"Lights 3", None))
        self.lightsBtn1.setText(QCoreApplication.translate("MainWindow", u"Lights 1", None))
        self.lightsBtn2.setText(QCoreApplication.translate("MainWindow", u"Lights 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.humidLabel.setText(QCoreApplication.translate("MainWindow", u"25%", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"30 deg", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Timer Control", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lights 1", None))
        self.timerBtn1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Lights 2", None))
        self.timerBtn2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Lights 3", None))
        self.timerBtn3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"EMBEDDED SYSTEMS PROJECT", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GROUP A3", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PORTABLE HOME AUTOMATION SYSTEM", None))
        self.tempSetBtn3.setText(QCoreApplication.translate("MainWindow", u"Set 3", None))
        self.tempSetBtn1.setText(QCoreApplication.translate("MainWindow", u"Set 1", None))
        self.tempSetBtn2.setText(QCoreApplication.translate("MainWindow", u"Set 2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Temp control", None))
        self.tempOffLbl.setText(QCoreApplication.translate("MainWindow", u"12 C", None))
        self.tempOnLbl.setText(QCoreApplication.translate("MainWindow", u"12 C", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi

