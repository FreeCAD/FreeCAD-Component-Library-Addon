# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'component_form.ui'
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
    QComboBox,
    QDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from src.interface.widgets import AttributeList, FileItem, FileList, TagBar


class Ui_ComponentCreationForm(object):
    def setupUi(self, ComponentCreationForm):
        if not ComponentCreationForm.objectName():
            ComponentCreationForm.setObjectName("ComponentCreationForm")
        ComponentCreationForm.resize(686, 871)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            ComponentCreationForm.sizePolicy().hasHeightForWidth()
        )
        ComponentCreationForm.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ComponentCreationForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.componentNameWidget = QWidget(ComponentCreationForm)
        self.componentNameWidget.setObjectName("componentNameWidget")
        sizePolicy.setHeightForWidth(
            self.componentNameWidget.sizePolicy().hasHeightForWidth()
        )
        self.componentNameWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.componentNameWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.componentNameLabel = QLabel(self.componentNameWidget)
        self.componentNameLabel.setObjectName("componentNameLabel")

        self.horizontalLayout_3.addWidget(self.componentNameLabel)

        self.componentNameInput = QLineEdit(self.componentNameWidget)
        self.componentNameInput.setObjectName("componentNameInput")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.componentNameInput.sizePolicy().hasHeightForWidth()
        )
        self.componentNameInput.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(18)
        self.componentNameInput.setFont(font)

        self.horizontalLayout_3.addWidget(self.componentNameInput)

        self.verticalLayout.addWidget(self.componentNameWidget)

        self.metadataWidget = QWidget(ComponentCreationForm)
        self.metadataWidget.setObjectName("metadataWidget")
        sizePolicy.setHeightForWidth(
            self.metadataWidget.sizePolicy().hasHeightForWidth()
        )
        self.metadataWidget.setSizePolicy(sizePolicy)
        self.metadataWidget.setMouseTracking(False)
        self.metadataWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gridLayout = QGridLayout(self.metadataWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.authorLabel = QLabel(self.metadataWidget)
        self.authorLabel.setObjectName("authorLabel")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.authorLabel.sizePolicy().hasHeightForWidth())
        self.authorLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.authorLabel, 1, 0, 1, 1)

        self.maintainerInput = QLineEdit(self.metadataWidget)
        self.maintainerInput.setObjectName("maintainerInput")
        sizePolicy1.setHeightForWidth(
            self.maintainerInput.sizePolicy().hasHeightForWidth()
        )
        self.maintainerInput.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        self.maintainerInput.setFont(font1)

        self.gridLayout.addWidget(self.maintainerInput, 2, 1, 1, 1)

        self.mainteinerLabel = QLabel(self.metadataWidget)
        self.mainteinerLabel.setObjectName("mainteinerLabel")
        sizePolicy.setHeightForWidth(
            self.mainteinerLabel.sizePolicy().hasHeightForWidth()
        )
        self.mainteinerLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mainteinerLabel, 2, 0, 1, 1)

        self.licenseInput = QComboBox(self.metadataWidget)
        self.licenseInput.setObjectName("licenseInput")
        sizePolicy1.setHeightForWidth(
            self.licenseInput.sizePolicy().hasHeightForWidth()
        )
        self.licenseInput.setSizePolicy(sizePolicy1)
        self.licenseInput.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.licenseInput, 4, 1, 1, 1)

        self.tagsWidget = TagBar(self.metadataWidget)
        self.tagsWidget.setObjectName("tagsWidget")
        sizePolicy1.setHeightForWidth(self.tagsWidget.sizePolicy().hasHeightForWidth())
        self.tagsWidget.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.tagsWidget, 3, 1, 1, 1)

        self.licenseLabel = QLabel(self.metadataWidget)
        self.licenseLabel.setObjectName("licenseLabel")
        sizePolicy.setHeightForWidth(self.licenseLabel.sizePolicy().hasHeightForWidth())
        self.licenseLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.licenseLabel, 4, 0, 1, 1)

        self.tagsLabel = QLabel(self.metadataWidget)
        self.tagsLabel.setObjectName("tagsLabel")
        sizePolicy2.setHeightForWidth(self.tagsLabel.sizePolicy().hasHeightForWidth())
        self.tagsLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.tagsLabel, 3, 0, 1, 1)

        self.authorInput = QLineEdit(self.metadataWidget)
        self.authorInput.setObjectName("authorInput")
        sizePolicy1.setHeightForWidth(self.authorInput.sizePolicy().hasHeightForWidth())
        self.authorInput.setSizePolicy(sizePolicy1)
        self.authorInput.setFont(font1)

        self.gridLayout.addWidget(self.authorInput, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.metadataWidget)

        self.compLabel = QLabel(ComponentCreationForm)
        self.compLabel.setObjectName("compLabel")
        sizePolicy1.setHeightForWidth(self.compLabel.sizePolicy().hasHeightForWidth())
        self.compLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.compLabel)

        self.componentFiles = FileList(ComponentCreationForm)
        self.componentFiles.setObjectName("componentFiles")
        sizePolicy1.setHeightForWidth(
            self.componentFiles.sizePolicy().hasHeightForWidth()
        )
        self.componentFiles.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.componentFiles)

        self.thumbLabel = QLabel(ComponentCreationForm)
        self.thumbLabel.setObjectName("thumbLabel")
        sizePolicy1.setHeightForWidth(self.thumbLabel.sizePolicy().hasHeightForWidth())
        self.thumbLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.thumbLabel)

        self.thumbnailFile = FileItem(ComponentCreationForm)
        self.thumbnailFile.setObjectName("thumbnailFile")
        sizePolicy1.setHeightForWidth(
            self.thumbnailFile.sizePolicy().hasHeightForWidth()
        )
        self.thumbnailFile.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.thumbnailFile)

        self.descriptionLabel = QLabel(ComponentCreationForm)
        self.descriptionLabel.setObjectName("descriptionLabel")
        sizePolicy.setHeightForWidth(
            self.descriptionLabel.sizePolicy().hasHeightForWidth()
        )
        self.descriptionLabel.setSizePolicy(sizePolicy)
        self.descriptionLabel.setMaximumSize(QSize(16777213, 16777215))

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.descriptionInput = QPlainTextEdit(ComponentCreationForm)
        self.descriptionInput.setObjectName("descriptionInput")
        sizePolicy1.setHeightForWidth(
            self.descriptionInput.sizePolicy().hasHeightForWidth()
        )
        self.descriptionInput.setSizePolicy(sizePolicy1)
        self.descriptionInput.setFont(font1)

        self.verticalLayout.addWidget(self.descriptionInput)

        self.attributesLabel = QLabel(ComponentCreationForm)
        self.attributesLabel.setObjectName("attributesLabel")
        sizePolicy.setHeightForWidth(
            self.attributesLabel.sizePolicy().hasHeightForWidth()
        )
        self.attributesLabel.setSizePolicy(sizePolicy)
        self.attributesLabel.setMaximumSize(QSize(16777213, 16777215))

        self.verticalLayout.addWidget(self.attributesLabel)

        self.attributesList = AttributeList(ComponentCreationForm)
        self.attributesList.setObjectName("attributesList")
        sizePolicy.setHeightForWidth(
            self.attributesList.sizePolicy().hasHeightForWidth()
        )
        self.attributesList.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.attributesList)

        self.bottomWidget = QWidget(ComponentCreationForm)
        self.bottomWidget.setObjectName("bottomWidget")
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.bottomWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addWidget(self.bottomWidget)

        self.retranslateUi(ComponentCreationForm)

        QMetaObject.connectSlotsByName(ComponentCreationForm)
    # setupUi

    def retranslateUi(self, ComponentCreationForm):
        ComponentCreationForm.setWindowTitle(
            QCoreApplication.translate("ComponentCreationForm", "Dialog", None)
        )
        self.componentNameLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:18pt;">Component Name</span></p></body></html>',
                None,
            )
        )
        self.componentNameInput.setInputMask("")
        self.componentNameInput.setPlaceholderText(
            QCoreApplication.translate(
                "ComponentCreationForm", "name of the component", None
            )
        )
        self.authorLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">Author:</span></p></body></html>',
                None,
            )
        )
        self.maintainerInput.setPlaceholderText(
            QCoreApplication.translate(
                "ComponentCreationForm", "maintailer@email.com", None
            )
        )
        self.mainteinerLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">Maintainer:</span></p></body></html>',
                None,
            )
        )
        self.licenseLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">License:</span></p></body></html>',
                None,
            )
        )
        self.tagsLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">Tags</span></p></body></html>',
                None,
            )
        )
        self.authorInput.setPlaceholderText(
            QCoreApplication.translate(
                "ComponentCreationForm", "author@email.com", None
            )
        )
        self.compLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">Component Files</span></p></body></html>',
                None,
            )
        )
        self.thumbLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">Thumbnail File</span></p></body></html>',
                None,
            )
        )
        self.descriptionLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">Description</span></p></body></html>',
                None,
            )
        )
        self.descriptionInput.setPlaceholderText(
            QCoreApplication.translate(
                "ComponentCreationForm", "a short description about the component", None
            )
        )
        self.attributesLabel.setText(
            QCoreApplication.translate(
                "ComponentCreationForm",
                '<html><head/><body><p><span style=" font-size:12pt;">Attributes</span></p></body></html>',
                None,
            )
        )
    # retranslateUi
