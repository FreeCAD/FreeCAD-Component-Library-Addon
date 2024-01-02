# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
# |																|
# |             Copyright 2023 - 2023, Amulya Paritosh			|
# |																|
# |  This file is part of Component Library Plugin for FreeCAD.	|
# |																|
# |               This file was created as a part of				|
# |              Google Summer Of Code Program - 2023			|
# |																|
# --------------------------------------------------------------

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
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
from PySide6.QtGui import (
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
from PySide6.QtWidgets import (
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
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1411, 898)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navigationWidget = QWidget(self.frame)
        self.navigationWidget.setObjectName("navigationWidget")
        self.verticalLayout_2 = QVBoxLayout(self.navigationWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.browseButton = QPushButton(self.navigationWidget)
        self.browseButton.setObjectName("browseButton")

        self.verticalLayout_2.addWidget(self.browseButton)

        self.LocalButton = QPushButton(self.navigationWidget)
        self.LocalButton.setObjectName("LocalButton")

        self.verticalLayout_2.addWidget(self.LocalButton)

        self.uploadButton = QPushButton(self.navigationWidget)
        self.uploadButton.setObjectName("uploadButton")

        self.verticalLayout_2.addWidget(self.uploadButton)

        self.verticalLayout.addWidget(self.navigationWidget)

        self.verticalSpacer = QSpacerItem(
            20, 767, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.notificationArea = QVBoxLayout()
        self.notificationArea.setObjectName("notificationArea")

        self.verticalLayout.addLayout(self.notificationArea)

        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.browseButton.setText(
            QCoreApplication.translate("MainWindow", "Browse Components", None)
        )
        self.LocalButton.setText(
            QCoreApplication.translate("MainWindow", "Manage Local Components", None)
        )
        self.uploadButton.setText(
            QCoreApplication.translate("MainWindow", "Upload Component", None)
        )

    # retranslateUi
