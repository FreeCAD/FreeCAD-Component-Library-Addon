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

from typing import cast, List
from PySide2.QtCore import Qt, Signal, SignalInstance
from PySide2.QtGui import QStandardItem
from PySide2.QtWidgets import QComboBox


class CheckableComboBox(QComboBox):
    """
    Custom QComboBox that supports checkable items.
    """

    selectionUpdated = cast(SignalInstance, Signal(list))

    def __init__(self, parent=None):
        """
        Constructor to initialize the CheckableComboBox.
        """
        super().__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self._changed = False
        self._last_checked_items = []

    def handleItemPressed(self, index):
        """
        Method to handle item presses and toggle the check state.
        """
        item: QStandardItem = self.model().itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)
        self._changed = True

    def hidePopup(self):
        """
        Override the hidePopup method to emit the selectionUpdated signal.
        """
        if not self._changed:
            super().hidePopup()
            if self._last_checked_items != self.checked_items():
                self._last_checked_items = self.checked_items()
                self.selectionUpdated.emit(self.checked_items())
        self._changed = False

    def itemChecked(self, index):
        """
        Method to check if a specific item is checked.

        Parameters
        ----------
        index : int
            The index of the item.

        Returns
        -------
        bool
            True if the item is checked, False otherwise.
        """
        item: QStandardItem = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.CheckState.Checked

    def setItemChecked(self, index, checked=True):
        """
        Method to set the check state of a specific item.

        Parameters
        ----------
        index : int
            The index of the item.
        checked : bool, optional
            Whether to check the item or not, by default True.
        """
        item: QStandardItem = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(Qt.CheckState.Checked)
        else:
            item.setCheckState(Qt.CheckState.Unchecked)

    def checked_items(self):
        """
        Method to get a list of checked item texts.

        Returns
        -------
        list of str
            A list of checked item texts.
        """
        checkedItems: List[str] = []
        for i in range(self.count()):
            item: QStandardItem = self.model().item(i, 0)
            if item.checkState() == Qt.CheckState.Checked:
                checkedItems.append(item.text())
        return checkedItems

    def index_is_checked(self, index):
        """
        Method to check if a specific index is checked.

        Parameters
        ----------
        index : int
            The index of the item.

        Returns
        -------
        bool
            True if the item at the given index is checked, False otherwise.
        """
        item: QStandardItem = self.model().item(index, 0)
        return item.checkState() == Qt.CheckState.Checked

    def make_pre_checked(self):
        """
        Method to set all items as checked initially.
        """
        for i in range(self.count()):
            item: QStandardItem = self.model().item(i, 0)
            if item.checkState() == Qt.CheckState.Checked:
                continue
            item.setCheckState(Qt.CheckState.Checked)
        self._last_checked_items = self.checked_items()
