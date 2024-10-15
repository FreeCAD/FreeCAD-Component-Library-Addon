# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attributes_list_widget.ui'
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
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from src.interface.widgets import AttributeListView


class Ui_AttributeList(object):
    def setupUi(self, AttributeList):
        if not AttributeList.objectName():
            AttributeList.setObjectName("AttributeList")
        AttributeList.resize(664, 301)
        self.horizontalLayout = QHBoxLayout(AttributeList)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.attributeListView = AttributeListView(AttributeList)
        self.attributeListView.setObjectName("attributeListView")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.attributeListView.sizePolicy().hasHeightForWidth()
        )
        self.attributeListView.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.attributeListView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.keyLineEdit = QLineEdit(AttributeList)
        self.keyLineEdit.setObjectName("keyLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.keyLineEdit.sizePolicy().hasHeightForWidth())
        self.keyLineEdit.setSizePolicy(sizePolicy1)
        self.keyLineEdit.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.keyLineEdit, 0, 1, 1, 1)

        self.keyLabel = QLabel(AttributeList)
        self.keyLabel.setObjectName("keyLabel")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.keyLabel.sizePolicy().hasHeightForWidth())
        self.keyLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.keyLabel, 0, 0, 1, 1)

        self.valueLabel = QLabel(AttributeList)
        self.valueLabel.setObjectName("valueLabel")
        sizePolicy2.setHeightForWidth(self.valueLabel.sizePolicy().hasHeightForWidth())
        self.valueLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.valueLabel, 1, 0, 1, 1)

        self.valueLineEdit = QLineEdit(AttributeList)
        self.valueLineEdit.setObjectName("valueLineEdit")
        sizePolicy1.setHeightForWidth(
            self.valueLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.valueLineEdit.setSizePolicy(sizePolicy1)
        self.valueLineEdit.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.valueLineEdit, 1, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.addPushButton = QPushButton(AttributeList)
        self.addPushButton.setObjectName("addPushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.addPushButton.sizePolicy().hasHeightForWidth()
        )
        self.addPushButton.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.addPushButton)

        self.line = QFrame(AttributeList)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.removePushButton = QPushButton(AttributeList)
        self.removePushButton.setObjectName("removePushButton")
        sizePolicy3.setHeightForWidth(
            self.removePushButton.sizePolicy().hasHeightForWidth()
        )
        self.removePushButton.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.removePushButton)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(AttributeList)

        QMetaObject.connectSlotsByName(AttributeList)

    # setupUi

    def retranslateUi(self, AttributeList):
        AttributeList.setWindowTitle(
            QCoreApplication.translate("AttributeList", "Form", None)
        )
        self.keyLabel.setText(QCoreApplication.translate("AttributeList", "Key:", None))
        self.valueLabel.setText(
            QCoreApplication.translate("AttributeList", "Value:", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("AttributeList", "Add Attribute", None)
        )
        self.removePushButton.setText(
            QCoreApplication.translate("AttributeList", "Remove", None)
        )

    # retranslateUi
