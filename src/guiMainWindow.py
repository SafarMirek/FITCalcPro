# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiDesign.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(400, 600)
        mainWindow.setMaximumSize(QSize(400, 600))
        mainWindow.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 401, 451))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.xpowery = QPushButton(self.layoutWidget)
        self.xpowery.setObjectName(u"xpowery")
        self.xpowery.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xpowery.sizePolicy().hasHeightForWidth())
        self.xpowery.setSizePolicy(sizePolicy)
        self.xpowery.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setPointSize(20)
        self.xpowery.setFont(font)
        self.xpowery.setAutoFillBackground(False)
        self.xpowery.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.xpowery.setFlat(True)

        self.gridLayout.addWidget(self.xpowery, 0, 0, 1, 1)

        self.yrootx = QPushButton(self.layoutWidget)
        self.yrootx.setObjectName(u"yrootx")
        self.yrootx.setEnabled(True)
        sizePolicy.setHeightForWidth(self.yrootx.sizePolicy().hasHeightForWidth())
        self.yrootx.setSizePolicy(sizePolicy)
        self.yrootx.setMaximumSize(QSize(60, 60))
        self.yrootx.setFont(font)
        self.yrootx.setAutoFillBackground(False)
        self.yrootx.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.yrootx.setFlat(True)

        self.gridLayout.addWidget(self.yrootx, 0, 1, 1, 1)

        self.twopowerx = QPushButton(self.layoutWidget)
        self.twopowerx.setObjectName(u"twopowerx")
        self.twopowerx.setEnabled(True)
        sizePolicy.setHeightForWidth(self.twopowerx.sizePolicy().hasHeightForWidth())
        self.twopowerx.setSizePolicy(sizePolicy)
        self.twopowerx.setMaximumSize(QSize(60, 60))
        self.twopowerx.setFont(font)
        self.twopowerx.setAutoFillBackground(False)
        self.twopowerx.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.twopowerx.setFlat(True)

        self.gridLayout.addWidget(self.twopowerx, 0, 2, 1, 1)

        self.tworootx = QPushButton(self.layoutWidget)
        self.tworootx.setObjectName(u"tworootx")
        self.tworootx.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tworootx.sizePolicy().hasHeightForWidth())
        self.tworootx.setSizePolicy(sizePolicy)
        self.tworootx.setMaximumSize(QSize(60, 60))
        self.tworootx.setFont(font)
        self.tworootx.setAutoFillBackground(False)
        self.tworootx.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.tworootx.setFlat(True)

        self.gridLayout.addWidget(self.tworootx, 0, 3, 1, 1)

        self.factorial = QPushButton(self.layoutWidget)
        self.factorial.setObjectName(u"factorial")
        self.factorial.setEnabled(True)
        sizePolicy.setHeightForWidth(self.factorial.sizePolicy().hasHeightForWidth())
        self.factorial.setSizePolicy(sizePolicy)
        self.factorial.setMaximumSize(QSize(60, 60))
        self.factorial.setFont(font)
        self.factorial.setAutoFillBackground(False)
        self.factorial.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.factorial.setFlat(True)

        self.gridLayout.addWidget(self.factorial, 0, 4, 1, 1)

        self.invertor = QPushButton(self.layoutWidget)
        self.invertor.setObjectName(u"invertor")
        self.invertor.setEnabled(True)
        sizePolicy.setHeightForWidth(self.invertor.sizePolicy().hasHeightForWidth())
        self.invertor.setSizePolicy(sizePolicy)
        self.invertor.setMaximumSize(QSize(60, 60))
        self.invertor.setFont(font)
        self.invertor.setAutoFillBackground(False)
        self.invertor.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.invertor.setFlat(True)

        self.gridLayout.addWidget(self.invertor, 1, 0, 1, 1)

        self.sin = QPushButton(self.layoutWidget)
        self.sin.setObjectName(u"sin")
        self.sin.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sin.sizePolicy().hasHeightForWidth())
        self.sin.setSizePolicy(sizePolicy)
        self.sin.setMaximumSize(QSize(60, 60))
        self.sin.setFont(font)
        self.sin.setAutoFillBackground(False)
        self.sin.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.sin.setFlat(True)

        self.gridLayout.addWidget(self.sin, 1, 1, 1, 1)

        self.cos = QPushButton(self.layoutWidget)
        self.cos.setObjectName(u"cos")
        self.cos.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cos.sizePolicy().hasHeightForWidth())
        self.cos.setSizePolicy(sizePolicy)
        self.cos.setMaximumSize(QSize(60, 60))
        self.cos.setFont(font)
        self.cos.setAutoFillBackground(False)
        self.cos.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.cos.setFlat(True)

        self.gridLayout.addWidget(self.cos, 1, 2, 1, 1)

        self.tan = QPushButton(self.layoutWidget)
        self.tan.setObjectName(u"tan")
        self.tan.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tan.sizePolicy().hasHeightForWidth())
        self.tan.setSizePolicy(sizePolicy)
        self.tan.setMaximumSize(QSize(60, 60))
        self.tan.setFont(font)
        self.tan.setAutoFillBackground(False)
        self.tan.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.tan.setFlat(True)

        self.gridLayout.addWidget(self.tan, 1, 3, 1, 1)

        self.pi = QPushButton(self.layoutWidget)
        self.pi.setObjectName(u"pi")
        self.pi.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pi.sizePolicy().hasHeightForWidth())
        self.pi.setSizePolicy(sizePolicy)
        self.pi.setMaximumSize(QSize(60, 60))
        self.pi.setFont(font)
        self.pi.setAutoFillBackground(False)
        self.pi.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.pi.setFlat(True)

        self.gridLayout.addWidget(self.pi, 1, 4, 1, 1)

        self.seven = QPushButton(self.layoutWidget)
        self.seven.setObjectName(u"seven")
        self.seven.setEnabled(True)
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setMaximumSize(QSize(60, 60))
        self.seven.setFont(font)
        self.seven.setAutoFillBackground(False)
        self.seven.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.seven.setFlat(True)

        self.gridLayout.addWidget(self.seven, 2, 0, 1, 1)

        self.eight = QPushButton(self.layoutWidget)
        self.eight.setObjectName(u"eight")
        self.eight.setEnabled(True)
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setMaximumSize(QSize(60, 60))
        self.eight.setFont(font)
        self.eight.setAutoFillBackground(False)
        self.eight.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.eight.setFlat(True)

        self.gridLayout.addWidget(self.eight, 2, 1, 1, 1)

        self.nine = QPushButton(self.layoutWidget)
        self.nine.setObjectName(u"nine")
        self.nine.setEnabled(True)
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setMaximumSize(QSize(60, 60))
        self.nine.setFont(font)
        self.nine.setAutoFillBackground(False)
        self.nine.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.nine.setFlat(True)

        self.gridLayout.addWidget(self.nine, 2, 2, 1, 1)

        self.ac = QPushButton(self.layoutWidget)
        self.ac.setObjectName(u"ac")
        self.ac.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ac.sizePolicy().hasHeightForWidth())
        self.ac.setSizePolicy(sizePolicy)
        self.ac.setMaximumSize(QSize(60, 60))
        self.ac.setFont(font)
        self.ac.setAutoFillBackground(False)
        self.ac.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.ac.setFlat(True)

        self.gridLayout.addWidget(self.ac, 2, 3, 1, 1)

        self.delete = QPushButton(self.layoutWidget)
        self.delete.setObjectName(u"del")
        self.delete.setEnabled(True)
        sizePolicy.setHeightForWidth(self.delete.sizePolicy().hasHeightForWidth())
        self.delete.setSizePolicy(sizePolicy)
        self.delete.setMaximumSize(QSize(60, 60))
        self.delete.setFont(font)
        self.delete.setAutoFillBackground(False)
        self.delete.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.delete.setFlat(True)

        self.gridLayout.addWidget(self.delete, 2, 4, 1, 1)

        self.four = QPushButton(self.layoutWidget)
        self.four.setObjectName(u"four")
        self.four.setEnabled(True)
        sizePolicy.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy)
        self.four.setMaximumSize(QSize(60, 60))
        self.four.setFont(font)
        self.four.setAutoFillBackground(False)
        self.four.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.four.setFlat(True)

        self.gridLayout.addWidget(self.four, 3, 0, 1, 1)

        self.five = QPushButton(self.layoutWidget)
        self.five.setObjectName(u"five")
        self.five.setEnabled(True)
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setMaximumSize(QSize(60, 60))
        self.five.setFont(font)
        self.five.setAutoFillBackground(False)
        self.five.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.five.setFlat(True)

        self.gridLayout.addWidget(self.five, 3, 1, 1, 1)

        self.six = QPushButton(self.layoutWidget)
        self.six.setObjectName(u"six")
        self.six.setEnabled(True)
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setMaximumSize(QSize(60, 60))
        self.six.setFont(font)
        self.six.setAutoFillBackground(False)
        self.six.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.six.setFlat(True)

        self.gridLayout.addWidget(self.six, 3, 2, 1, 1)

        self.times = QPushButton(self.layoutWidget)
        self.times.setObjectName(u"times")
        self.times.setEnabled(True)
        sizePolicy.setHeightForWidth(self.times.sizePolicy().hasHeightForWidth())
        self.times.setSizePolicy(sizePolicy)
        self.times.setMaximumSize(QSize(60, 60))
        self.times.setFont(font)
        self.times.setAutoFillBackground(False)
        self.times.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.times.setFlat(True)

        self.gridLayout.addWidget(self.times, 3, 3, 1, 1)

        self.devide = QPushButton(self.layoutWidget)
        self.devide.setObjectName(u"devide")
        self.devide.setEnabled(True)
        sizePolicy.setHeightForWidth(self.devide.sizePolicy().hasHeightForWidth())
        self.devide.setSizePolicy(sizePolicy)
        self.devide.setMaximumSize(QSize(60, 60))
        self.devide.setFont(font)
        self.devide.setAutoFillBackground(False)
        self.devide.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.devide.setFlat(True)

        self.gridLayout.addWidget(self.devide, 3, 4, 1, 1)

        self.one = QPushButton(self.layoutWidget)
        self.one.setObjectName(u"one")
        self.one.setEnabled(True)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setMaximumSize(QSize(60, 60))
        self.one.setFont(font)
        self.one.setAutoFillBackground(False)
        self.one.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.one.setFlat(True)

        self.gridLayout.addWidget(self.one, 4, 0, 1, 1)

        self.two = QPushButton(self.layoutWidget)
        self.two.setObjectName(u"two")
        self.two.setEnabled(True)
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setMaximumSize(QSize(60, 60))
        self.two.setFont(font)
        self.two.setAutoFillBackground(False)
        self.two.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.two.setFlat(True)

        self.gridLayout.addWidget(self.two, 4, 1, 1, 1)

        self.three = QPushButton(self.layoutWidget)
        self.three.setObjectName(u"three")
        self.three.setEnabled(True)
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setMaximumSize(QSize(60, 60))
        self.three.setFont(font)
        self.three.setAutoFillBackground(False)
        self.three.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.three.setFlat(True)

        self.gridLayout.addWidget(self.three, 4, 2, 1, 1)

        self.plus = QPushButton(self.layoutWidget)
        self.plus.setObjectName(u"plus")
        self.plus.setEnabled(True)
        sizePolicy.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy)
        self.plus.setMaximumSize(QSize(60, 60))
        self.plus.setFont(font)
        self.plus.setAutoFillBackground(False)
        self.plus.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.plus.setFlat(True)

        self.gridLayout.addWidget(self.plus, 4, 3, 1, 1)

        self.minus = QPushButton(self.layoutWidget)
        self.minus.setObjectName(u"minus")
        self.minus.setEnabled(True)
        sizePolicy.setHeightForWidth(self.minus.sizePolicy().hasHeightForWidth())
        self.minus.setSizePolicy(sizePolicy)
        self.minus.setMaximumSize(QSize(60, 60))
        self.minus.setFont(font)
        self.minus.setAutoFillBackground(False)
        self.minus.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.minus.setFlat(True)

        self.gridLayout.addWidget(self.minus, 4, 4, 1, 1)

        self.comma = QPushButton(self.layoutWidget)
        self.comma.setObjectName(u"comma")
        self.comma.setEnabled(True)
        sizePolicy.setHeightForWidth(self.comma.sizePolicy().hasHeightForWidth())
        self.comma.setSizePolicy(sizePolicy)
        self.comma.setMaximumSize(QSize(60, 60))
        self.comma.setFont(font)
        self.comma.setAutoFillBackground(False)
        self.comma.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.comma.setFlat(True)

        self.gridLayout.addWidget(self.comma, 5, 0, 1, 1)

        self.zero = QPushButton(self.layoutWidget)
        self.zero.setObjectName(u"zero")
        self.zero.setEnabled(True)
        sizePolicy.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setMaximumSize(QSize(60, 60))
        self.zero.setFont(font)
        self.zero.setAutoFillBackground(False)
        self.zero.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.zero.setFlat(True)

        self.gridLayout.addWidget(self.zero, 5, 1, 1, 1)

        self.Ans = QPushButton(self.layoutWidget)
        self.Ans.setObjectName(u"Ans")
        self.Ans.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Ans.sizePolicy().hasHeightForWidth())
        self.Ans.setSizePolicy(sizePolicy)
        self.Ans.setMaximumSize(QSize(60, 60))
        self.Ans.setFont(font)
        self.Ans.setAutoFillBackground(False)
        self.Ans.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.Ans.setFlat(True)

        self.gridLayout.addWidget(self.Ans, 5, 2, 1, 1)

        self.equals = QPushButton(self.layoutWidget)
        self.equals.setObjectName(u"equals")
        self.equals.setEnabled(True)
        sizePolicy.setHeightForWidth(self.equals.sizePolicy().hasHeightForWidth())
        self.equals.setSizePolicy(sizePolicy)
        self.equals.setMaximumSize(QSize(60, 60))
        self.equals.setFont(font)
        self.equals.setAutoFillBackground(False)
        self.equals.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(20,20,20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200,200,200);\n"
"	color: rgb(30, 30, 30);\n"
"}")
        self.equals.setFlat(True)

        self.gridLayout.addWidget(self.equals, 5, 3, 1, 1)

        self.guide = QPushButton(self.layoutWidget)
        self.guide.setObjectName(u"guide")
        self.guide.setEnabled(True)
        sizePolicy.setHeightForWidth(self.guide.sizePolicy().hasHeightForWidth())
        self.guide.setSizePolicy(sizePolicy)
        self.guide.setMaximumSize(QSize(60, 60))
        self.guide.setFont(font)
        self.guide.setAutoFillBackground(False)
        self.guide.setStyleSheet(u"QPushButton {\n"
"	border: 1px;\n"
"	background-color: rgb(160,160,160);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50,50,50);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.guide.setFlat(True)

        self.gridLayout.addWidget(self.guide, 5, 4, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 441, 133))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 100))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255,255,255)\n"
"}")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setMargin(15)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(400, 100))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255,255,255)\n"
"}")
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2.setMargin(15)

        self.verticalLayout.addWidget(self.label_2)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 23))
        self.menuasd = QMenu(self.menubar)
        self.menuasd.setObjectName(u"menuasd")
        self.menuasd.setStyleSheet(u"QMenu {\n"
"	color: rgb(255,255,255);\n"
"}")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuasd.menuAction())

        self.retranslateUi(mainWindow)

        self.xpowery.setDefault(False)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"FitCalcPro", None))
        self.xpowery.setText(QCoreApplication.translate("mainWindow", u"x\u02b8", None))
        self.yrootx.setText(QCoreApplication.translate("mainWindow", u"\u02b8\u221ax", None))
        self.twopowerx.setText(QCoreApplication.translate("mainWindow", u"x\u00b2", None))
        self.tworootx.setText(QCoreApplication.translate("mainWindow", u"\u00b2\u221ax", None))
        self.factorial.setText(QCoreApplication.translate("mainWindow", u"n!", None))
        self.invertor.setText(QCoreApplication.translate("mainWindow", u"+/-", None))
        self.sin.setText(QCoreApplication.translate("mainWindow", u"sin", None))
        self.cos.setText(QCoreApplication.translate("mainWindow", u"cos", None))
        self.tan.setText(QCoreApplication.translate("mainWindow", u"tan", None))
        self.pi.setText(QCoreApplication.translate("mainWindow", u"\u03c0", None))
        self.seven.setText(QCoreApplication.translate("mainWindow", u"7", None))
        self.eight.setText(QCoreApplication.translate("mainWindow", u"8", None))
        self.nine.setText(QCoreApplication.translate("mainWindow", u"9", None))
        self.ac.setText(QCoreApplication.translate("mainWindow", u"AC", None))
        self.delete.setText(QCoreApplication.translate("mainWindow", u"DEL", None))
        self.four.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.five.setText(QCoreApplication.translate("mainWindow", u"5", None))
        self.six.setText(QCoreApplication.translate("mainWindow", u"6", None))
        self.times.setText(QCoreApplication.translate("mainWindow", u"x", None))
        self.devide.setText(QCoreApplication.translate("mainWindow", u"/", None))
        self.one.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.two.setText(QCoreApplication.translate("mainWindow", u"2", None))
        self.three.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.plus.setText(QCoreApplication.translate("mainWindow", u"+", None))
        self.minus.setText(QCoreApplication.translate("mainWindow", u"-", None))
        self.comma.setText(QCoreApplication.translate("mainWindow", u",", None))
        self.zero.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.Ans.setText(QCoreApplication.translate("mainWindow", u"Ans", None))
        self.equals.setText(QCoreApplication.translate("mainWindow", u"=", None))
        self.guide.setText(QCoreApplication.translate("mainWindow", u"???", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Zadejte p\u0159\u00edklad", None))
        self.menuasd.setTitle(QCoreApplication.translate("mainWindow", u"N\u00e1pov\u011bda", None))
    # retranslateUi
