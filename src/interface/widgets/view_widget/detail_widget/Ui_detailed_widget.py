# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailed_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.interface.widgets import (AttributeList, StarRating, TagBar)

class Ui_detailedWidget(object):
    def setupUi(self, detailedWidget):
        if not detailedWidget.objectName():
            detailedWidget.setObjectName(u"detailedWidget")
        detailedWidget.resize(975, 673)
        self.verticalLayout = QVBoxLayout(detailedWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topArea = QWidget(detailedWidget)
        self.topArea.setObjectName(u"topArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topArea.sizePolicy().hasHeightForWidth())
        self.topArea.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.topArea)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backPushButton = QPushButton(self.topArea)
        self.backPushButton.setObjectName(u"backPushButton")

        self.horizontalLayout.addWidget(self.backPushButton)

        self.separator = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.separator)

        self.controlArea = QHBoxLayout()
        self.controlArea.setObjectName(u"controlArea")

        self.horizontalLayout.addLayout(self.controlArea)

        self.filetypeComboBox = QComboBox(self.topArea)
        self.filetypeComboBox.setObjectName(u"filetypeComboBox")

        self.horizontalLayout.addWidget(self.filetypeComboBox)


        self.verticalLayout.addWidget(self.topArea)

        self.componentnameWidget = QWidget(detailedWidget)
        self.componentnameWidget.setObjectName(u"componentnameWidget")
        sizePolicy.setHeightForWidth(self.componentnameWidget.sizePolicy().hasHeightForWidth())
        self.componentnameWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.componentnameWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.componentLabel = QLabel(self.componentnameWidget)
        self.componentLabel.setObjectName(u"componentLabel")
        sizePolicy.setHeightForWidth(self.componentLabel.sizePolicy().hasHeightForWidth())
        self.componentLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.componentLabel)


        self.verticalLayout.addWidget(self.componentnameWidget)

        self.thumbnailArea = QScrollArea(detailedWidget)
        self.thumbnailArea.setObjectName(u"thumbnailArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.thumbnailArea.sizePolicy().hasHeightForWidth())
        self.thumbnailArea.setSizePolicy(sizePolicy1)
        self.thumbnailArea.setMinimumSize(QSize(0, 200))
        self.thumbnailArea.setMaximumSize(QSize(16777215, 300))
        self.thumbnailArea.setLayoutDirection(Qt.LeftToRight)
        self.thumbnailArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.thumbnailArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.thumbnailArea.setWidgetResizable(True)
        self.thumbnailareaWidget = QWidget()
        self.thumbnailareaWidget.setObjectName(u"thumbnailareaWidget")
        self.thumbnailareaWidget.setGeometry(QRect(0, 0, 953, 190))
        sizePolicy1.setHeightForWidth(self.thumbnailareaWidget.sizePolicy().hasHeightForWidth())
        self.thumbnailareaWidget.setSizePolicy(sizePolicy1)
        self.thumbnailareaWidget.setMinimumSize(QSize(0, 100))
        self.thumbnailareaWidget.setMaximumSize(QSize(16777215, 500))
        self.thumbnailareaWidget.setLayoutDirection(Qt.LeftToRight)
        self.thumbnailAreaHorizontalLayout = QHBoxLayout(self.thumbnailareaWidget)
        self.thumbnailAreaHorizontalLayout.setObjectName(u"thumbnailAreaHorizontalLayout")
        self.thumbnailArea.setWidget(self.thumbnailareaWidget)

        self.verticalLayout.addWidget(self.thumbnailArea)

        self.tagsWidget = TagBar(detailedWidget)
        self.tagsWidget.setObjectName(u"tagsWidget")
        sizePolicy.setHeightForWidth(self.tagsWidget.sizePolicy().hasHeightForWidth())
        self.tagsWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tagsWidget)

        self.descriptionWidget = QWidget(detailedWidget)
        self.descriptionWidget.setObjectName(u"descriptionWidget")
        sizePolicy.setHeightForWidth(self.descriptionWidget.sizePolicy().hasHeightForWidth())
        self.descriptionWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.descriptionWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.descriptionLabel = QLabel(self.descriptionWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.horizontalLayout_2.addWidget(self.descriptionLabel)


        self.verticalLayout.addWidget(self.descriptionWidget)

        self.attributeArea = QWidget(detailedWidget)
        self.attributeArea.setObjectName(u"attributeArea")
        sizePolicy.setHeightForWidth(self.attributeArea.sizePolicy().hasHeightForWidth())
        self.attributeArea.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.attributeArea)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.metadataWidget = QWidget(self.attributeArea)
        self.metadataWidget.setObjectName(u"metadataWidget")
        self.gridLayout = QGridLayout(self.metadataWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.authorFrame = QFrame(self.metadataWidget)
        self.authorFrame.setObjectName(u"authorFrame")
        self.authorFrame.setFrameShape(QFrame.StyledPanel)
        self.authorFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.authorFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.authorLabel = QLabel(self.authorFrame)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.authorLabel)

        self.authorValue = QLabel(self.authorFrame)
        self.authorValue.setObjectName(u"authorValue")
        self.authorValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.authorValue)


        self.gridLayout.addWidget(self.authorFrame, 0, 1, 1, 1)

        self.licenceFrame = QFrame(self.metadataWidget)
        self.licenceFrame.setObjectName(u"licenceFrame")
        self.licenceFrame.setFrameShape(QFrame.StyledPanel)
        self.licenceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.licenceFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.licenceLabel = QLabel(self.licenceFrame)
        self.licenceLabel.setObjectName(u"licenceLabel")
        self.licenceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.licenceLabel)

        self.licenceValue = QLabel(self.licenceFrame)
        self.licenceValue.setObjectName(u"licenceValue")
        self.licenceValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.licenceValue)


        self.gridLayout.addWidget(self.licenceFrame, 0, 4, 1, 1)

        self.maintainerFrame = QFrame(self.metadataWidget)
        self.maintainerFrame.setObjectName(u"maintainerFrame")
        self.maintainerFrame.setFrameShape(QFrame.StyledPanel)
        self.maintainerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.maintainerFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.maintainerLabel = QLabel(self.maintainerFrame)
        self.maintainerLabel.setObjectName(u"maintainerLabel")
        self.maintainerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.maintainerLabel)

        self.maintainerValue = QLabel(self.maintainerFrame)
        self.maintainerValue.setObjectName(u"maintainerValue")
        self.maintainerValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.maintainerValue)


        self.gridLayout.addWidget(self.maintainerFrame, 0, 2, 1, 1)

        self.updatedFrame = QFrame(self.metadataWidget)
        self.updatedFrame.setObjectName(u"updatedFrame")
        self.updatedFrame.setFrameShape(QFrame.StyledPanel)
        self.updatedFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.updatedFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.updatedLabel = QLabel(self.updatedFrame)
        self.updatedLabel.setObjectName(u"updatedLabel")
        self.updatedLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.updatedLabel)

        self.updatedValue = QLabel(self.updatedFrame)
        self.updatedValue.setObjectName(u"updatedValue")
        self.updatedValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.updatedValue)


        self.gridLayout.addWidget(self.updatedFrame, 1, 2, 1, 1)

        self.ratingFrame = QFrame(self.metadataWidget)
        self.ratingFrame.setObjectName(u"ratingFrame")
        self.ratingFrame.setFrameShape(QFrame.StyledPanel)
        self.ratingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ratingFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ratingLabel = QLabel(self.ratingFrame)
        self.ratingLabel.setObjectName(u"ratingLabel")
        self.ratingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ratingLabel)

        self.ratingWidget = StarRating(self.ratingFrame)
        self.ratingWidget.setObjectName(u"ratingWidget")

        self.verticalLayout_8.addWidget(self.ratingWidget)


        self.gridLayout.addWidget(self.ratingFrame, 1, 4, 1, 1)

        self.createdFrame = QFrame(self.metadataWidget)
        self.createdFrame.setObjectName(u"createdFrame")
        self.createdFrame.setFrameShape(QFrame.StyledPanel)
        self.createdFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.createdFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.createdLabel = QLabel(self.createdFrame)
        self.createdLabel.setObjectName(u"createdLabel")
        self.createdLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.createdLabel)

        self.createdValue = QLabel(self.createdFrame)
        self.createdValue.setObjectName(u"createdValue")
        self.createdValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.createdValue)


        self.gridLayout.addWidget(self.createdFrame, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.metadataWidget)

        self.scrollArea = QScrollArea(self.attributeArea)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 461, 126))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.attributeList = AttributeList(self.scrollAreaWidgetContents)
        self.attributeList.setObjectName(u"attributeList")
        sizePolicy1.setHeightForWidth(self.attributeList.sizePolicy().hasHeightForWidth())
        self.attributeList.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.attributeList)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.attributeArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(detailedWidget)

        QMetaObject.connectSlotsByName(detailedWidget)
    # setupUi

    def retranslateUi(self, detailedWidget):
        detailedWidget.setWindowTitle(QCoreApplication.translate("detailedWidget", u"Form", None))
        self.backPushButton.setText(QCoreApplication.translate("detailedWidget", u"Back", None))
        self.componentLabel.setText(QCoreApplication.translate("detailedWidget", u"Component_Name", None))
        self.descriptionLabel.setText(QCoreApplication.translate("detailedWidget", u"Here is a way to improve your vocabulary. Check out the words for the day and a small quiz to work up your mind.", None))
        self.authorLabel.setText(QCoreApplication.translate("detailedWidget", u"Author", None))
        self.authorValue.setText(QCoreApplication.translate("detailedWidget", u"TextLabel", None))
        self.licenceLabel.setText(QCoreApplication.translate("detailedWidget", u"Licence", None))
        self.licenceValue.setText(QCoreApplication.translate("detailedWidget", u"TextLabel", None))
        self.maintainerLabel.setText(QCoreApplication.translate("detailedWidget", u"Maintainer", None))
        self.maintainerValue.setText(QCoreApplication.translate("detailedWidget", u"TextLabel", None))
        self.updatedLabel.setText(QCoreApplication.translate("detailedWidget", u"Updated_on ", None))
        self.updatedValue.setText(QCoreApplication.translate("detailedWidget", u"TextLabel", None))
        self.ratingLabel.setText(QCoreApplication.translate("detailedWidget", u"Rating", None))
        self.createdLabel.setText(QCoreApplication.translate("detailedWidget", u"Created_on", None))
        self.createdValue.setText(QCoreApplication.translate("detailedWidget", u"TextLabel", None))
    # retranslateUi

