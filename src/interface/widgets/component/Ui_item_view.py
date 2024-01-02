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
## Form generated from reading UI file 'item_view.ui'
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
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from src.interface.widgets import Thumbnail


class Ui_ComponentItemView(object):
    def setupUi(self, ComponentItemView):
        if not ComponentItemView.objectName():
            ComponentItemView.setObjectName("ComponentItemView")
        ComponentItemView.resize(350, 275)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ComponentItemView.sizePolicy().hasHeightForWidth())
        ComponentItemView.setSizePolicy(sizePolicy)
        ComponentItemView.setMinimumSize(QSize(350, 275))
        ComponentItemView.setMaximumSize(QSize(500, 400))
        self.verticalLayout = QVBoxLayout(ComponentItemView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(ComponentItemView)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.thumbnail = Thumbnail(self.frame)
        self.thumbnail.setObjectName("thumbnail")
        self.verticalLayout_2 = QVBoxLayout(self.thumbnail)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout_3.addWidget(self.thumbnail)

        self.bottomPanel = QWidget(self.frame)
        self.bottomPanel.setObjectName("bottomPanel")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bottomPanel.sizePolicy().hasHeightForWidth())
        self.bottomPanel.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.bottomPanel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.componentLabel = QLabel(self.bottomPanel)
        self.componentLabel.setObjectName("componentLabel")

        self.horizontalLayout.addWidget(self.componentLabel)

        self.pushButton = QPushButton(self.bottomPanel)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout_3.addWidget(self.bottomPanel)

        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(ComponentItemView)

        QMetaObject.connectSlotsByName(ComponentItemView)

    # setupUi

    def retranslateUi(self, ComponentItemView):
        ComponentItemView.setWindowTitle(
            QCoreApplication.translate("ComponentItemView", "item_view", None)
        )
        self.componentLabel.setText(
            QCoreApplication.translate("ComponentItemView", "Component Label", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("ComponentItemView", "Download", None)
        )

    # retranslateUi
