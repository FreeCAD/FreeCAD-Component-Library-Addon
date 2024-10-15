# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from src.interface.widgets import Thumbnail


class Ui_ComponentItemView(object):
    def setupUi(self, ComponentItemView):
        if not ComponentItemView.objectName():
            ComponentItemView.setObjectName(u"ComponentItemView")
        ComponentItemView.resize(350, 275)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ComponentItemView.sizePolicy().hasHeightForWidth())
        ComponentItemView.setSizePolicy(sizePolicy)
        ComponentItemView.setMinimumSize(QSize(350, 275))
        ComponentItemView.setMaximumSize(QSize(500, 400))
        self.verticalLayout = QVBoxLayout(ComponentItemView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ComponentItemView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.thumbnail = Thumbnail(self.frame)
        self.thumbnail.setObjectName(u"thumbnail")
        self.verticalLayout_2 = QVBoxLayout(self.thumbnail)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addWidget(self.thumbnail)

        self.bottomPanel = QWidget(self.frame)
        self.bottomPanel.setObjectName(u"bottomPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bottomPanel.sizePolicy().hasHeightForWidth())
        self.bottomPanel.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.bottomPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.componentLabel = QLabel(self.bottomPanel)
        self.componentLabel.setObjectName(u"componentLabel")

        self.horizontalLayout.addWidget(self.componentLabel)


        self.verticalLayout_3.addWidget(self.bottomPanel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ComponentItemView)

        QMetaObject.connectSlotsByName(ComponentItemView)
    # setupUi

    def retranslateUi(self, ComponentItemView):
        ComponentItemView.setWindowTitle(QCoreApplication.translate("ComponentItemView", u"item_view", None))
        self.componentLabel.setText(QCoreApplication.translate("ComponentItemView", u"Component Label", None))
    # retranslateUi
