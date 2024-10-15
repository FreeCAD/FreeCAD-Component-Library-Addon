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

from PySide2.QtWidgets import QWidget

from ....data import Component
from .Ui_item_view import Ui_ComponentItemView


class ComponentItem(QWidget):
    """
    Custom QWidget representing an item in a component view.
    """

    def __init__(self, parent: QWidget, component: Component) -> None:
        """
        Constructor to initialize the ComponentItem.
        """
        super().__init__(parent)
        self.ui = Ui_ComponentItemView()
        self.ui.setupUi(self)
        self.component: Component = component
        self.setupItem()

    def setupItem(self):
        """
        Method to set up the item's content.
        """
        self.ui.componentLabel.setText(self.component.metadata.name)
        self.ui.thumbnail.setupThumbnail(self.component.metadata.thumbnail)

    @property
    def parentGrigView(self):
        return self.parent().parent().parent().parent()

    def mousePressEvent(self, event) -> None:
        self.topLevelWidget().widgetStack.append(self.parentGrigView)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        posMouse = event.pos()
        if self.rect().contains(posMouse):
            self.parentGrigView.detailView.updateContent(self)
            self.topLevelWidget().ui.stackedWidget.setCurrentWidget(
                self.parentGrigView.detailView
            )
