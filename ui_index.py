# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DESTOP.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 660)
        MainWindow.setMinimumSize(QSize(750, 660))
        MainWindow.setMaximumSize(QSize(750, 660))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 751, 662))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.layoutWidget2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(60, 660))
        self.widget.setMaximumSize(QSize(60, 660))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	height:25px;\n"
"	border:none;\n"
"}")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AboutIcon = QPushButton(self.widget)
        self.AboutIcon.setObjectName(u"AboutIcon")
        icon = QIcon()
        icon.addFile(u":/icons/About.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/AboutClick.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.AboutIcon.setIcon(icon)
        self.AboutIcon.setIconSize(QSize(26, 26))
        self.AboutIcon.setCheckable(True)
        self.AboutIcon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.AboutIcon)

        self.ExitIcon = QPushButton(self.widget)
        self.ExitIcon.setObjectName(u"ExitIcon")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/ExitClick.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ExitIcon.setIcon(icon1)
        self.ExitIcon.setIconSize(QSize(26, 26))
        self.ExitIcon.setCheckable(True)
        self.ExitIcon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ExitIcon)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.IconLogo = QLabel(self.widget)
        self.IconLogo.setObjectName(u"IconLogo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconLogo.sizePolicy().hasHeightForWidth())
        self.IconLogo.setSizePolicy(sizePolicy)
        self.IconLogo.setMinimumSize(QSize(40, 40))
        self.IconLogo.setMaximumSize(QSize(40, 40))
        self.IconLogo.setPixmap(QPixmap(u":/icons/Icon.png"))
        self.IconLogo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.IconLogo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ControlPanelIcon = QPushButton(self.widget)
        self.ControlPanelIcon.setObjectName(u"ControlPanelIcon")
        icon2 = QIcon()
        icon2.addFile(u":/icons/ControlPanel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/ControlPanelClick.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ControlPanelIcon.setIcon(icon2)
        self.ControlPanelIcon.setIconSize(QSize(26, 26))
        self.ControlPanelIcon.setCheckable(True)
        self.ControlPanelIcon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ControlPanelIcon)

        self.DashboardIcon = QPushButton(self.widget)
        self.DashboardIcon.setObjectName(u"DashboardIcon")
        self.DashboardIcon.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/Dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/DashboardClick.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.DashboardIcon.setIcon(icon3)
        self.DashboardIcon.setIconSize(QSize(26, 26))
        self.DashboardIcon.setCheckable(True)
        self.DashboardIcon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.DashboardIcon)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 260, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget)

        self.widget_2 = QWidget(self.layoutWidget2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(85, 660))
        self.widget_2.setMaximumSize(QSize(85, 660))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"	\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	color: rgb(47, 92, 175);\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.FullLogo = QLabel(self.widget_2)
        self.FullLogo.setObjectName(u"FullLogo")
        self.FullLogo.setMaximumSize(QSize(70, 40))
        self.FullLogo.setPixmap(QPixmap(u":/icons/Logo.png"))
        self.FullLogo.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.FullLogo)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ControlPanelButton = QPushButton(self.widget_2)
        self.ControlPanelButton.setObjectName(u"ControlPanelButton")
        self.ControlPanelButton.setMinimumSize(QSize(0, 30))
        self.ControlPanelButton.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.ControlPanelButton.setFont(font)
        self.ControlPanelButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}")

        self.verticalLayout_9.addWidget(self.ControlPanelButton)

        self.DashboardButton = QPushButton(self.widget_2)
        self.DashboardButton.setObjectName(u"DashboardButton")
        self.DashboardButton.setEnabled(True)
        self.DashboardButton.setMinimumSize(QSize(0, 30))
        self.DashboardButton.setMaximumSize(QSize(16777215, 30))
        self.DashboardButton.setFont(font)
        self.DashboardButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}")

        self.verticalLayout_9.addWidget(self.DashboardButton)


        self.verticalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_2 = QSpacerItem(20, 265, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 7)
        self.AboutButton = QPushButton(self.widget_2)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setMinimumSize(QSize(0, 30))
        self.AboutButton.setMaximumSize(QSize(16777215, 30))
        self.AboutButton.setFont(font)
        self.AboutButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}")

        self.verticalLayout_3.addWidget(self.AboutButton)

        self.QuitButton = QPushButton(self.widget_2)
        self.QuitButton.setObjectName(u"QuitButton")
        self.QuitButton.setMinimumSize(QSize(0, 30))
        self.QuitButton.setMaximumSize(QSize(16777215, 30))
        self.QuitButton.setFont(font)
        self.QuitButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}")
        self.QuitButton.setIconSize(QSize(12, 20))

        self.verticalLayout_3.addWidget(self.QuitButton)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_12.addWidget(self.widget_2)

        self.stackedWidget = QStackedWidget(self.layoutWidget2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QSize(600, 660))
        self.stackedWidget.setMaximumSize(QSize(600, 660))
        font1 = QFont()
        font1.setKerning(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(235, 241, 255);\n"
"}")
        self.ControlPanelPage = QWidget()
        self.ControlPanelPage.setObjectName(u"ControlPanelPage")
        self.widget_4 = QWidget(self.ControlPanelPage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 600, 55))
        self.widget_4.setMinimumSize(QSize(600, 55))
        self.widget_4.setMaximumSize(QSize(600, 55))
        self.widget_4.setStyleSheet(u"QWidget{\n"
"	\n"
"	\n"
"	background-color: rgb(47, 92, 175);\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, -1, -1, -1)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.label_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.gridLayoutWidget = QWidget(self.ControlPanelPage)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 110, 481, 261))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(18)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.PowerButton = QPushButton(self.gridLayoutWidget)
        self.PowerButton.setObjectName(u"PowerButton")
        self.PowerButton.setEnabled(False)
        self.PowerButton.setMinimumSize(QSize(250, 250))
        self.PowerButton.setMaximumSize(QSize(250, 250))
        icon4 = QIcon()
        icon4.addFile(u":/icons/Off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/On.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.PowerButton.setIcon(icon4)
        self.PowerButton.setIconSize(QSize(250, 250))
        self.PowerButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.PowerButton, 0, 0, 1, 1)

        self.PowerDisclaimer = QTextBrowser(self.gridLayoutWidget)
        self.PowerDisclaimer.setObjectName(u"PowerDisclaimer")
        self.PowerDisclaimer.setStyleSheet(u"QTextBrowser {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.PowerDisclaimer, 0, 1, 1, 1)

        self.StatusIndicator = QTextBrowser(self.ControlPanelPage)
        self.StatusIndicator.setObjectName(u"StatusIndicator")
        self.StatusIndicator.setGeometry(QRect(10, 570, 581, 81))
        self.StatusIndicator.setStyleSheet(u"QTextBrowser {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.widget1 = QWidget(self.ControlPanelPage)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(50, 409, 481, 71))
        self.verticalLayout_7 = QVBoxLayout(self.widget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.CamerasComboBox = QComboBox(self.widget1)
        self.CamerasComboBox.setObjectName(u"CamerasComboBox")
        self.CamerasComboBox.setStyleSheet(u"QComboBox {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: black;\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: black;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.CamerasComboBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.CameraConfirm = QPushButton(self.widget1)
        self.CameraConfirm.setObjectName(u"CameraConfirm")
        self.CameraConfirm.setMinimumSize(QSize(0, 20))
        self.CameraConfirm.setMaximumSize(QSize(16777215, 29))
        self.CameraConfirm.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.CameraConfirm)

        self.stackedWidget.addWidget(self.ControlPanelPage)
        self.ModulationPage = QWidget()
        self.ModulationPage.setObjectName(u"ModulationPage")
        self.widget_5 = QWidget(self.ModulationPage)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 600, 55))
        self.widget_5.setMinimumSize(QSize(600, 55))
        self.widget_5.setMaximumSize(QSize(600, 55))
        self.widget_5.setStyleSheet(u"QWidget{\n"
"	\n"
"	\n"
"	background-color: rgb(47, 92, 175);\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(12, -1, -1, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.ModulationTitle = QLabel(self.widget_5)
        self.ModulationTitle.setObjectName(u"ModulationTitle")
        self.ModulationTitle.setFont(font2)
        self.ModulationTitle.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_12.addWidget(self.ModulationTitle)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalSpacer_8 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.label_9 = QLabel(self.ModulationPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(110, 170, 401, 211))
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"QLabel {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.ModulationPage)
        self.DashboardPage = QWidget()
        self.DashboardPage.setObjectName(u"DashboardPage")
        self.widget_6 = QWidget(self.DashboardPage)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 0, 600, 55))
        self.widget_6.setMinimumSize(QSize(600, 55))
        self.widget_6.setMaximumSize(QSize(600, 55))
        self.widget_6.setStyleSheet(u"QWidget{\n"
"	\n"
"	\n"
"	background-color: rgb(47, 92, 175);\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(12, -1, -1, -1)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.DashboardTitle = QLabel(self.widget_6)
        self.DashboardTitle.setObjectName(u"DashboardTitle")
        self.DashboardTitle.setFont(font2)
        self.DashboardTitle.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_14.addWidget(self.DashboardTitle)


        self.horizontalLayout_9.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalSpacer_9 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_9.addLayout(self.verticalLayout_15)

        self.gridLayoutWidget_2 = QWidget(self.DashboardPage)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(40, 60, 531, 611))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Graph_2 = QWidget(self.gridLayoutWidget_2)
        self.Graph_2.setObjectName(u"Graph_2")
        self.Graph_2.setMinimumSize(QSize(400, 180))
        self.Graph_2.setMaximumSize(QSize(400, 180))

        self.gridLayout_3.addWidget(self.Graph_2, 1, 0, 1, 1)

        self.Graph = QWidget(self.gridLayoutWidget_2)
        self.Graph.setObjectName(u"Graph")
        self.Graph.setMinimumSize(QSize(400, 180))
        self.Graph.setMaximumSize(QSize(400, 180))

        self.gridLayout_3.addWidget(self.Graph, 0, 0, 1, 1)

        self.Graph_3 = QWidget(self.gridLayoutWidget_2)
        self.Graph_3.setObjectName(u"Graph_3")
        self.Graph_3.setMinimumSize(QSize(400, 180))
        self.Graph_3.setMaximumSize(QSize(400, 180))

        self.gridLayout_3.addWidget(self.Graph_3, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.DashboardPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.widget_7 = QWidget(self.SettingsPage)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 0, 600, 55))
        self.widget_7.setMinimumSize(QSize(600, 55))
        self.widget_7.setMaximumSize(QSize(600, 55))
        self.widget_7.setStyleSheet(u"QWidget{\n"
"	\n"
"	\n"
"	background-color: rgb(47, 92, 175);\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(12, -1, -1, -1)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.SettingsTitle = QLabel(self.widget_7)
        self.SettingsTitle.setObjectName(u"SettingsTitle")
        self.SettingsTitle.setFont(font2)
        self.SettingsTitle.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_16.addWidget(self.SettingsTitle)


        self.horizontalLayout_10.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalSpacer_10 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer_10)


        self.horizontalLayout_10.addLayout(self.verticalLayout_17)

        self.textBrowser_3 = QTextBrowser(self.SettingsPage)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(10, 580, 581, 71))
        self.textBrowser_3.setStyleSheet(u"QTextBrowser {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayoutWidget = QWidget(self.SettingsPage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 80, 541, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label)

        self.CameraComboBox = QComboBox(self.horizontalLayoutWidget)
        self.CameraComboBox.setObjectName(u"CameraComboBox")
        self.CameraComboBox.setStyleSheet(u"QComboBox {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.CameraComboBox)

        self.RefreshCameraButton = QPushButton(self.horizontalLayoutWidget)
        self.RefreshCameraButton.setObjectName(u"RefreshCameraButton")
        self.RefreshCameraButton.setMinimumSize(QSize(70, 0))
        self.RefreshCameraButton.setMaximumSize(QSize(70, 16777215))
        self.RefreshCameraButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.RefreshCameraButton)

        self.label_2 = QLabel(self.SettingsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 281, 16))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.SettingsPage)
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.AboutTitleBar = QWidget(self.AboutPage)
        self.AboutTitleBar.setObjectName(u"AboutTitleBar")
        self.AboutTitleBar.setGeometry(QRect(0, 0, 600, 55))
        self.AboutTitleBar.setMinimumSize(QSize(600, 55))
        self.AboutTitleBar.setMaximumSize(QSize(600, 55))
        self.AboutTitleBar.setStyleSheet(u"QWidget{\n"
"	\n"
"	\n"
"	background-color: rgb(47, 92, 175);\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.AboutTitleBar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(12, -1, -1, -1)
        self.AboutTitleLayout = QVBoxLayout()
        self.AboutTitleLayout.setObjectName(u"AboutTitleLayout")
        self.AboutTitle = QLabel(self.AboutTitleBar)
        self.AboutTitle.setObjectName(u"AboutTitle")
        self.AboutTitle.setFont(font2)
        self.AboutTitle.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.AboutTitleLayout.addWidget(self.AboutTitle)


        self.horizontalLayout_11.addLayout(self.AboutTitleLayout)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalSpacer_11 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_19.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_11.addLayout(self.verticalLayout_19)

        self.AboutText = QTextBrowser(self.AboutPage)
        self.AboutText.setObjectName(u"AboutText")
        self.AboutText.setGeometry(QRect(30, 110, 531, 341))
        self.AboutText.setStyleSheet(u"QTextBrowser {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.textBrowser_4 = QTextBrowser(self.AboutPage)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(10, 580, 581, 71))
        self.textBrowser_4.setStyleSheet(u"QTextBrowser {\n"
"	\n"
"	background-color: rgb(233, 239, 253);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.stackedWidget.addWidget(self.AboutPage)

        self.horizontalLayout_12.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AboutIcon.setText("")
        self.ExitIcon.setText("")
        self.IconLogo.setText("")
        self.ControlPanelIcon.setText("")
        self.DashboardIcon.setText("")
        self.FullLogo.setText("")
        self.ControlPanelButton.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.DashboardButton.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.AboutButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.QuitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.PowerButton.setText("")
        self.PowerDisclaimer.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click this button to turn on DESTOP.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Remember to select your camera before you turn on DESTOP.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">DESTOP will dynamically change to help you blink more.</span></p></body></html>", None))
        self.StatusIndicator.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">STATUS: Starting up / Loading...</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Camera", None))
        self.CameraConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirm Camera Choice", None))
        self.ModulationTitle.setText(QCoreApplication.translate("MainWindow", u"Modulation", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.DashboardTitle.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.SettingsTitle.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DESTOP / Build V2.1 / nthRev - Siddhant Bajaj</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.RefreshCameraButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select the camera used for bliink detection:", None))
        self.AboutTitle.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.AboutText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">DESTOP is a computer application that dynamically modifies your screen to help you blink more and improve your eye health! </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Control Panel:</span></p>\n"
"<p style=\"-q"
                        "t-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The Control Panel is the menu for using and turning on DESTOP.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Dashboard:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">DESTOP automatically detects and plots your blink patterns and trends into graphs for you to see. You can look at your blink frequency relative to the healthy target, blink duration concentrations, and compare it to DESTOP's screen modifications!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">DESTOP is a solo-developed project. If you have any feedback, you can submit it at:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px"
                        "; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">https://forms.gle/t2XcmxSZWdKp9UzCA</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DESTOP / Build V2.1 / nthRev - Siddhant Bajaj</p></body></html>", None))
    # retranslateUi

