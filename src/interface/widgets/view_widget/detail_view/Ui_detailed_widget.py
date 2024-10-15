# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailed_widget.ui'
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
    QAbstractScrollArea,
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from src.interface.widgets import AttributeListView, StarRating, TagBar


class Ui_detailedWidget(object):
    def setupUi(self, detailedWidget):
        if not detailedWidget.objectName():
            detailedWidget.setObjectName("detailedWidget")
        detailedWidget.resize(975, 673)
        self.verticalLayout = QVBoxLayout(detailedWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topArea = QWidget(detailedWidget)
        self.topArea.setObjectName("topArea")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topArea.sizePolicy().hasHeightForWidth())
        self.topArea.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.topArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backPushButton = QPushButton(self.topArea)
        self.backPushButton.setObjectName("backPushButton")

        self.horizontalLayout.addWidget(self.backPushButton)

        self.separator = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.separator)

        self.controlArea = QHBoxLayout()
        self.controlArea.setObjectName("controlArea")

        self.horizontalLayout.addLayout(self.controlArea)

        self.filetypeComboBox = QComboBox(self.topArea)
        self.filetypeComboBox.setObjectName("filetypeComboBox")

        self.horizontalLayout.addWidget(self.filetypeComboBox)

        self.verticalLayout.addWidget(self.topArea)

        self.componentnameWidget = QWidget(detailedWidget)
        self.componentnameWidget.setObjectName("componentnameWidget")
        sizePolicy.setHeightForWidth(
            self.componentnameWidget.sizePolicy().hasHeightForWidth()
        )
        self.componentnameWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.componentnameWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.componentLabel = QLabel(self.componentnameWidget)
        self.componentLabel.setObjectName("componentLabel")
        sizePolicy.setHeightForWidth(
            self.componentLabel.sizePolicy().hasHeightForWidth()
        )
        self.componentLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.componentLabel)

        self.verticalLayout.addWidget(self.componentnameWidget)

        self.thumbnailArea = QScrollArea(detailedWidget)
        self.thumbnailArea.setObjectName("thumbnailArea")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.thumbnailArea.sizePolicy().hasHeightForWidth()
        )
        self.thumbnailArea.setSizePolicy(sizePolicy1)
        self.thumbnailArea.setMinimumSize(QSize(0, 200))
        self.thumbnailArea.setMaximumSize(QSize(16777215, 300))
        self.thumbnailArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.thumbnailArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.thumbnailArea.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored
        )
        self.thumbnailArea.setWidgetResizable(True)
        self.thumbnailareaWidget = QWidget()
        self.thumbnailareaWidget.setObjectName("thumbnailareaWidget")
        self.thumbnailareaWidget.setGeometry(QRect(0, 0, 953, 190))
        sizePolicy1.setHeightForWidth(
            self.thumbnailareaWidget.sizePolicy().hasHeightForWidth()
        )
        self.thumbnailareaWidget.setSizePolicy(sizePolicy1)
        self.thumbnailareaWidget.setMinimumSize(QSize(0, 100))
        self.thumbnailareaWidget.setMaximumSize(QSize(16777215, 500))
        self.thumbnailareaWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.thumbnailAreaHorizontalLayout = QHBoxLayout(self.thumbnailareaWidget)
        self.thumbnailAreaHorizontalLayout.setObjectName(
            "thumbnailAreaHorizontalLayout"
        )
        self.thumbnailArea.setWidget(self.thumbnailareaWidget)

        self.verticalLayout.addWidget(self.thumbnailArea)

        self.tagsWidget = TagBar(detailedWidget)
        self.tagsWidget.setObjectName("tagsWidget")
        sizePolicy.setHeightForWidth(self.tagsWidget.sizePolicy().hasHeightForWidth())
        self.tagsWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tagsWidget)

        self.descriptionWidget = QWidget(detailedWidget)
        self.descriptionWidget.setObjectName("descriptionWidget")
        sizePolicy.setHeightForWidth(
            self.descriptionWidget.sizePolicy().hasHeightForWidth()
        )
        self.descriptionWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.descriptionWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.descriptionLabel = QLabel(self.descriptionWidget)
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.horizontalLayout_2.addWidget(self.descriptionLabel)

        self.verticalLayout.addWidget(self.descriptionWidget)

        self.attributeArea = QWidget(detailedWidget)
        self.attributeArea.setObjectName("attributeArea")
        sizePolicy.setHeightForWidth(
            self.attributeArea.sizePolicy().hasHeightForWidth()
        )
        self.attributeArea.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.attributeArea)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.metadataWidget = QWidget(self.attributeArea)
        self.metadataWidget.setObjectName("metadataWidget")
        self.gridLayout = QGridLayout(self.metadataWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.authorFrame = QFrame(self.metadataWidget)
        self.authorFrame.setObjectName("authorFrame")
        self.authorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.authorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.authorFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.authorLabel = QLabel(self.authorFrame)
        self.authorLabel.setObjectName("authorLabel")
        self.authorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.authorLabel)

        self.authorValue = QLabel(self.authorFrame)
        self.authorValue.setObjectName("authorValue")
        self.authorValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.authorValue)

        self.gridLayout.addWidget(self.authorFrame, 0, 1, 1, 1)

        self.licenceFrame = QFrame(self.metadataWidget)
        self.licenceFrame.setObjectName("licenceFrame")
        self.licenceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.licenceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.licenceFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.licenceLabel = QLabel(self.licenceFrame)
        self.licenceLabel.setObjectName("licenceLabel")
        self.licenceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.licenceLabel)

        self.licenceValue = QLabel(self.licenceFrame)
        self.licenceValue.setObjectName("licenceValue")
        self.licenceValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.licenceValue)

        self.gridLayout.addWidget(self.licenceFrame, 0, 4, 1, 1)

        self.maintainerFrame = QFrame(self.metadataWidget)
        self.maintainerFrame.setObjectName("maintainerFrame")
        self.maintainerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.maintainerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.maintainerFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.maintainerLabel = QLabel(self.maintainerFrame)
        self.maintainerLabel.setObjectName("maintainerLabel")
        self.maintainerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.maintainerLabel)

        self.maintainerValue = QLabel(self.maintainerFrame)
        self.maintainerValue.setObjectName("maintainerValue")
        self.maintainerValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.maintainerValue)

        self.gridLayout.addWidget(self.maintainerFrame, 0, 2, 1, 1)

        self.updatedFrame = QFrame(self.metadataWidget)
        self.updatedFrame.setObjectName("updatedFrame")
        self.updatedFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.updatedFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.updatedFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.updatedLabel = QLabel(self.updatedFrame)
        self.updatedLabel.setObjectName("updatedLabel")
        self.updatedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.updatedLabel)

        self.updatedValue = QLabel(self.updatedFrame)
        self.updatedValue.setObjectName("updatedValue")
        self.updatedValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.updatedValue)

        self.gridLayout.addWidget(self.updatedFrame, 1, 2, 1, 1)

        self.ratingFrame = QFrame(self.metadataWidget)
        self.ratingFrame.setObjectName("ratingFrame")
        self.ratingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ratingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ratingFrame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ratingLabel = QLabel(self.ratingFrame)
        self.ratingLabel.setObjectName("ratingLabel")
        self.ratingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.ratingLabel)

        self.ratingWidget = StarRating(self.ratingFrame)
        self.ratingWidget.setObjectName("ratingWidget")

        self.verticalLayout_8.addWidget(self.ratingWidget)

        self.gridLayout.addWidget(self.ratingFrame, 1, 4, 1, 1)

        self.createdFrame = QFrame(self.metadataWidget)
        self.createdFrame.setObjectName("createdFrame")
        self.createdFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.createdFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.createdFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.createdLabel = QLabel(self.createdFrame)
        self.createdLabel.setObjectName("createdLabel")
        self.createdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.createdLabel)

        self.createdValue = QLabel(self.createdFrame)
        self.createdValue.setObjectName("createdValue")
        self.createdValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.createdValue)

        self.gridLayout.addWidget(self.createdFrame, 1, 1, 1, 1)

        self.horizontalLayout_3.addWidget(self.metadataWidget)

        self.scrollArea = QScrollArea(self.attributeArea)
        self.scrollArea.setObjectName("scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 461, 126))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AttributeListView = AttributeListView(self.scrollAreaWidgetContents)
        self.AttributeListView.setObjectName("AttributeListView")
        sizePolicy1.setHeightForWidth(
            self.AttributeListView.sizePolicy().hasHeightForWidth()
        )
        self.AttributeListView.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.AttributeListView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.attributeArea)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.retranslateUi(detailedWidget)

        QMetaObject.connectSlotsByName(detailedWidget)
    # setupUi

    def retranslateUi(self, detailedWidget):
        detailedWidget.setWindowTitle(
            QCoreApplication.translate("detailedWidget", "Form", None)
        )
        self.backPushButton.setText(
            QCoreApplication.translate("detailedWidget", "Back", None)
        )
        self.componentLabel.setText(
            QCoreApplication.translate("detailedWidget", "Component_Name", None)
        )
        self.descriptionLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                "Here is a way to improve your vocabulary. Check out the words for the day and a small quiz to work up your mind.",
                None,
            )
        )
        self.authorLabel.setText(
            QCoreApplication.translate("detailedWidget", "Author", None)
        )
        self.authorValue.setText(
            QCoreApplication.translate("detailedWidget", "TextLabel", None)
        )
        self.licenceLabel.setText(
            QCoreApplication.translate("detailedWidget", "Licence", None)
        )
        self.licenceValue.setText(
            QCoreApplication.translate("detailedWidget", "TextLabel", None)
        )
        self.maintainerLabel.setText(
            QCoreApplication.translate("detailedWidget", "Maintainer", None)
        )
        self.maintainerValue.setText(
            QCoreApplication.translate("detailedWidget", "TextLabel", None)
        )
        self.updatedLabel.setText(
            QCoreApplication.translate("detailedWidget", "Updated_on ", None)
        )
        self.updatedValue.setText(
            QCoreApplication.translate("detailedWidget", "TextLabel", None)
        )
        self.ratingLabel.setText(
            QCoreApplication.translate("detailedWidget", "Rating", None)
        )
        self.createdLabel.setText(
            QCoreApplication.translate("detailedWidget", "Created_on", None)
        )
        self.createdValue.setText(
            QCoreApplication.translate("detailedWidget", "TextLabel", None)
        )
    # retranslateUi
