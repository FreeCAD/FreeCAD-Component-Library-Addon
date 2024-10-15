# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_UserWidget(object):
    def setupUi(self, UserWidget):
        if not UserWidget.objectName():
            UserWidget.setObjectName(u"UserWidget")
        UserWidget.resize(736, 753)
        self.verticalLayout = QVBoxLayout(UserWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(UserWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usernameLabel = QLabel(self.frame_3)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout.addWidget(self.usernameLabel)

        self.horizontalSpacer = QSpacerItem(511, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.authPushButtom = QPushButton(self.frame_3)
        self.authPushButtom.setObjectName(u"authPushButtom")

        self.horizontalLayout.addWidget(self.authPushButtom)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.profilePhotoLabel = QLabel(self.frame_4)
        self.profilePhotoLabel.setObjectName(u"profilePhotoLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.profilePhotoLabel.sizePolicy().hasHeightForWidth())
        self.profilePhotoLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.profilePhotoLabel)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.displayNameLabel = QLabel(self.frame_5)
        self.displayNameLabel.setObjectName(u"displayNameLabel")
        sizePolicy.setHeightForWidth(self.displayNameLabel.sizePolicy().hasHeightForWidth())
        self.displayNameLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.displayNameLabel)

        self.emailLabel = QLabel(self.frame_5)
        self.emailLabel.setObjectName(u"emailLabel")
        sizePolicy.setHeightForWidth(self.emailLabel.sizePolicy().hasHeightForWidth())
        self.emailLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.emailLabel)


        self.horizontalLayout_2.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(UserWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.componentsLabel = QLabel(self.frame_2)
        self.componentsLabel.setObjectName(u"componentsLabel")
        sizePolicy.setHeightForWidth(self.componentsLabel.sizePolicy().hasHeightForWidth())
        self.componentsLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.componentsLabel)

        self.componentsLlistWidget = QListWidget(self.frame_2)
        self.componentsLlistWidget.setObjectName(u"componentsLlistWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.componentsLlistWidget.sizePolicy().hasHeightForWidth())
        self.componentsLlistWidget.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.componentsLlistWidget)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(UserWidget)

        QMetaObject.connectSlotsByName(UserWidget)
    # setupUi

    def retranslateUi(self, UserWidget):
        UserWidget.setWindowTitle(QCoreApplication.translate("UserWidget", u"Form", None))
        self.usernameLabel.setText(QCoreApplication.translate("UserWidget", u"TextLabel", None))
        self.authPushButtom.setText(QCoreApplication.translate("UserWidget", u"PushButton", None))
        self.profilePhotoLabel.setText(QCoreApplication.translate("UserWidget", u"profilepic", None))
        self.displayNameLabel.setText(QCoreApplication.translate("UserWidget", u"TextLabel", None))
        self.emailLabel.setText(QCoreApplication.translate("UserWidget", u"TextLabel", None))
        self.componentsLabel.setText(QCoreApplication.translate("UserWidget", u"TextLabel", None))
    # retranslateUi

