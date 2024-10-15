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
## Form generated from reading UI file 'items_view.ui'
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
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from src.interface.widgets import CheckableComboBox, GridItemWidget, TagBar


class Ui_gridView(object):
    def setupUi(self, gridView):
        if not gridView.objectName():
            gridView.setObjectName("gridView")
        gridView.resize(1136, 816)
        self.verticalLayout = QVBoxLayout(gridView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleFrame = QFrame(gridView)
        self.titleFrame.setObjectName("titleFrame")
        self.titleFrame.setMaximumSize(QSize(16777215, 51))
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.searchWidget = QWidget(self.titleFrame)
        self.searchWidget.setObjectName("searchWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.searchWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchLabel = QLabel(self.searchWidget)
        self.searchLabel.setObjectName("searchLabel")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLabel.sizePolicy().hasHeightForWidth())
        self.searchLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.searchLabel)

        self.searchLineEdit = QLineEdit(self.searchWidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.searchLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.searchLineEdit.setSizePolicy(sizePolicy1)
        self.searchLineEdit.setMinimumSize(QSize(0, 35))
        self.searchLineEdit.setStyleSheet("border: 0px ;\n" "")

        self.horizontalLayout_2.addWidget(self.searchLineEdit)

        self.horizontalLayout_7.addWidget(self.searchWidget)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.sortWidget = QWidget(self.titleFrame)
        self.sortWidget.setObjectName("sortWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.sortWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sortLabel = QLabel(self.sortWidget)
        self.sortLabel.setObjectName("sortLabel")
        sizePolicy.setHeightForWidth(self.sortLabel.sizePolicy().hasHeightForWidth())
        self.sortLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.sortLabel)

        self.sortComboBox = QComboBox(self.sortWidget)
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.setObjectName("sortComboBox")

        self.horizontalLayout_4.addWidget(self.sortComboBox)

        self.horizontalLayout_7.addWidget(self.sortWidget)

        self.orderWidget = QWidget(self.titleFrame)
        self.orderWidget.setObjectName("orderWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.orderWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.orderLabel = QLabel(self.orderWidget)
        self.orderLabel.setObjectName("orderLabel")
        sizePolicy.setHeightForWidth(self.orderLabel.sizePolicy().hasHeightForWidth())
        self.orderLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.orderLabel)

        self.orderComboBox = QComboBox(self.orderWidget)
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.setObjectName("orderComboBox")

        self.horizontalLayout_3.addWidget(self.orderComboBox)

        self.horizontalLayout_7.addWidget(self.orderWidget)

        self.fileTypeWidget = QWidget(self.titleFrame)
        self.fileTypeWidget.setObjectName("fileTypeWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.fileTypeWidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.fileTypeLabel = QLabel(self.fileTypeWidget)
        self.fileTypeLabel.setObjectName("fileTypeLabel")
        sizePolicy.setHeightForWidth(
            self.fileTypeLabel.sizePolicy().hasHeightForWidth()
        )
        self.fileTypeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fileTypeLabel)

        self.fileTypeComboBox = CheckableComboBox(self.fileTypeWidget)
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.setObjectName("fileTypeComboBox")
        self.fileTypeComboBox.setMinimumSize(QSize(106, 0))
        self.fileTypeComboBox.setEditable(False)

        self.horizontalLayout_11.addWidget(self.fileTypeComboBox)

        self.horizontalLayout_7.addWidget(self.fileTypeWidget)

        self.verticalLayout.addWidget(self.titleFrame)

        self.titleFrame_2 = QFrame(gridView)
        self.titleFrame_2.setObjectName("titleFrame_2")
        self.titleFrame_2.setMaximumSize(QSize(16777215, 51))
        self.titleFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.titleFrame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tagBarWidget = QWidget(self.titleFrame_2)
        self.tagBarWidget.setObjectName("tagBarWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.tagBarWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tagBarLabel = QLabel(self.tagBarWidget)
        self.tagBarLabel.setObjectName("tagBarLabel")
        sizePolicy.setHeightForWidth(self.tagBarLabel.sizePolicy().hasHeightForWidth())
        self.tagBarLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.tagBarLabel)

        self.tagBar = TagBar(self.tagBarWidget)
        self.tagBar.setObjectName("tagBar")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tagBar.sizePolicy().hasHeightForWidth())
        self.tagBar.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.tagBar)

        self.horizontalLayout_8.addWidget(self.tagBarWidget)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.titleFrame_2)

        self.scrollArea = QScrollArea(gridView)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContentItemsWidget = GridItemWidget()
        self.scrollAreaContentItemsWidget.setObjectName("scrollAreaContentItemsWidget")
        self.scrollAreaContentItemsWidget.setGeometry(QRect(0, 0, 1120, 651))
        self.scrollArea.setWidget(self.scrollAreaContentItemsWidget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.bottomBar = QWidget(gridView)
        self.bottomBar.setObjectName("bottomBar")
        self.horizontalLayout = QHBoxLayout(self.bottomBar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevButton = QPushButton(self.bottomBar)
        self.prevButton.setObjectName("prevButton")

        self.horizontalLayout.addWidget(self.prevButton)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pageLable = QLabel(self.bottomBar)
        self.pageLable.setObjectName("pageLable")

        self.horizontalLayout.addWidget(self.pageLable)

        self.bottomBarSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.bottomBarSpacer)

        self.nextButton = QPushButton(self.bottomBar)
        self.nextButton.setObjectName("nextButton")

        self.horizontalLayout.addWidget(self.nextButton)

        self.verticalLayout.addWidget(self.bottomBar)

        self.retranslateUi(gridView)

        QMetaObject.connectSlotsByName(gridView)

    # setupUi

    def retranslateUi(self, gridView):
        gridView.setWindowTitle(QCoreApplication.translate("gridView", "Form", None))
        self.searchLabel.setText(QCoreApplication.translate("gridView", "Search", None))
        self.sortLabel.setText(QCoreApplication.translate("gridView", "sort", None))
        self.sortComboBox.setItemText(
            0, QCoreApplication.translate("gridView", "Name", None)
        )
        self.sortComboBox.setItemText(
            1, QCoreApplication.translate("gridView", "Created", None)
        )
        self.sortComboBox.setItemText(
            2, QCoreApplication.translate("gridView", "Updated", None)
        )
        self.sortComboBox.setItemText(
            3, QCoreApplication.translate("gridView", "Rating", None)
        )

        self.orderLabel.setText(QCoreApplication.translate("gridView", "order", None))
        self.orderComboBox.setItemText(
            0, QCoreApplication.translate("gridView", "ascending", None)
        )
        self.orderComboBox.setItemText(
            1, QCoreApplication.translate("gridView", "descending", None)
        )

        self.fileTypeLabel.setText(
            QCoreApplication.translate("gridView", "filetype", None)
        )
        self.fileTypeComboBox.setItemText(
            0, QCoreApplication.translate("gridView", "step", None)
        )
        self.fileTypeComboBox.setItemText(
            1, QCoreApplication.translate("gridView", "fcstd", None)
        )
        self.fileTypeComboBox.setItemText(
            2, QCoreApplication.translate("gridView", "fcstd1", None)
        )
        self.fileTypeComboBox.setItemText(
            3, QCoreApplication.translate("gridView", "stl", None)
        )
        self.fileTypeComboBox.setItemText(
            4, QCoreApplication.translate("gridView", "stp", None)
        )

        self.tagBarLabel.setText(QCoreApplication.translate("gridView", "Tags", None))
        self.prevButton.setText(QCoreApplication.translate("gridView", "Prev", None))
        self.pageLable.setText(QCoreApplication.translate("gridView", "0 / 0", None))
        self.nextButton.setText(QCoreApplication.translate("gridView", "Next", None))

    # retranslateUi
