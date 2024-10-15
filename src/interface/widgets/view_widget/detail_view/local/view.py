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

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QPushButton, QWidget

from ......manager import LocalStorageManager, ManagerInterface
from ..base_detail_view import BaseDetailedView


class LocalDetailedView(BaseDetailedView):
    """
    Detailed view Widget of an localy present component.
    """

    manager: LocalStorageManager

    def __init__(self, parent: QWidget) -> None:
        """
        Initialises the OnlineDetailedView.

        Parameters
        ----------
        parent : QWidget
            parent widget of OnlineDetailedView.
        """
        super().__init__(parent)

        self.setupUi()
        self.setupSignals()

    def setupUi(self) -> None:
        """
        Setup all the ui elements.
        Called in __init__
        """
        super().setupUi()

        self.removePushButton = QPushButton(self)
        self.removePushButton.setText("Remove")
        self.addControlWidget(self.removePushButton)

    def setupSignals(self) -> None:
        """
        Setup all the signal connections.
        Called in __init__
        """
        self.removePushButton.clicked.connect(self.remove)

    def setupManager(self, manager: ManagerInterface) -> None:
        """
        Sets up the manager for the OnlineDetailedView.

        Parameters
        ----------
        manager : ManagerInterface
            An instance of the manager interface.

        Returns
        -------
        None
        """
        super().setupManager(manager)

    @Slot()
    def remove(self) -> None:
        """
                Remove the file fromt he locak storage.

        Returns
        -------
        None
        """
        self.manager.remove_file(self.component, self.current_file().type)
        self.ui.filetypeComboBox.removeItem(self.ui.filetypeComboBox.currentIndex())
        if self.ui.filetypeComboBox.count() == 0:
            self.backPushButton_click()
        self.parent().parent().localGridView.components_response_handler()
