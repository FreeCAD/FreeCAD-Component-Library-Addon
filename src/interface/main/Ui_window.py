# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide2.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1411, 898)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navigationWidget = QWidget(self.frame)
        self.navigationWidget.setObjectName(u"navigationWidget")
        self.verticalLayout_2 = QVBoxLayout(self.navigationWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.browseButton = QPushButton(self.navigationWidget)
        self.browseButton.setObjectName(u"browseButton")

        self.verticalLayout_2.addWidget(self.browseButton)

        self.LocalButton = QPushButton(self.navigationWidget)
        self.LocalButton.setObjectName(u"LocalButton")

        self.verticalLayout_2.addWidget(self.LocalButton)

        self.uploadButton = QPushButton(self.navigationWidget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.verticalLayout_2.addWidget(self.uploadButton)


        self.verticalLayout.addWidget(self.navigationWidget)

        self.verticalSpacer = QSpacerItem(20, 767, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.notificationArea = QVBoxLayout()
        self.notificationArea.setObjectName(u"notificationArea")

        self.verticalLayout.addLayout(self.notificationArea)

        self.userPushButton = QPushButton(self.frame)
        self.userPushButton.setObjectName(u"userPushButton")

        self.verticalLayout.addWidget(self.userPushButton)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse Components", None))
        self.LocalButton.setText(QCoreApplication.translate("MainWindow", u"Manage Local Components", None))
        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"Upload Component", None))
        self.userPushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi
