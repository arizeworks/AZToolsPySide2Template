# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PySide2Template.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(526, 445)
        MainWindow.setStyleSheet(u"QDialog {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"QFrame {\n"
"	border-style: None;\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"	border: None;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"	color: white;\n"
"	background-color: rgb(127, 127, 127);\n"
"}\n"
"QTabBar::tab:!selected{\n"
"	color: rgb(95%, 95%, 95%);\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"#tab_INI,\n"
"#tab_DEV,\n"
"#tab_FILE,\n"
"#tab_IO,\n"
"#tab_TRANS,\n"
"#tab_OBJ,\n"
"#tab_GEO,\n"
"#tab_CS,\n"
"#tab_UV,\n"
"#tab_MT,\n"
"#tab_WT,\n"
"#tab_PLUGIN {\n"
"	background-color: rgb(30%, 30%, 30%);\n"
"}\n"
"#frame_Current,\n"
"#frame_L1,#frame_L2,#frame_L3,#frame_L4,#frame_L5,#frame_L6,#frame_L7,#frame_L8,\n"
"#frame_R1,#frame_R2,#frame_R3,#frame_R4,#frame_R5,#frame_R6,#frame_R7,#frame_R8 {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(95%, 95%, 95%);\n"
"	border: None;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(40%, 40%, 40%);\n"
"}\n"
"QPushButton::ho"
                        "ver{\n"
"	background-color: rgb(20%, 20%, 20%);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(226, 123, 13);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(95%, 95%, 95%);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: rgb(95%, 95%, 95%);\n"
"	border: black;\n"
"	background-color: rgb(15%, 15%, 15%);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: rgb(95%, 95%, 95%);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_Header = QFrame(self.centralwidget)
        self.frame_Header.setObjectName(u"frame_Header")
        self.frame_Header.setMinimumSize(QSize(0, 50))
        self.frame_Header.setMaximumSize(QSize(16777215, 50))
        self.frame_Header.setStyleSheet(u"background-color: rgb(226, 123, 13);\n"
"")
        self.frame_Header.setFrameShape(QFrame.StyledPanel)
        self.frame_Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_Header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_189 = QFrame(self.frame_Header)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_116.setSpacing(4)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame_189)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_116.addWidget(self.label)

        self.pushButton_menu = QPushButton(self.frame_189)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_menu.setSizePolicy(sizePolicy)
        self.pushButton_menu.setMinimumSize(QSize(0, 0))
        self.pushButton_menu.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../../../../../../../.designer/backup/icons/Arize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_menu.setIcon(icon)
        self.pushButton_menu.setIconSize(QSize(48, 48))

        self.horizontalLayout_116.addWidget(self.pushButton_menu)


        self.horizontalLayout_2.addWidget(self.frame_189, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_Header)

        self.frame_Main = QFrame(self.centralwidget)
        self.frame_Main.setObjectName(u"frame_Main")
        self.frame_Main.setStyleSheet(u"#frame_Main { background-color:rgb(77, 77, 77);}")
        self.frame_Main.setFrameShape(QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_Main)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton = QPushButton(self.frame_Main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.verticalLayout_8.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_Main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AZTools PySide2 Template", None))
        self.pushButton_menu.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

