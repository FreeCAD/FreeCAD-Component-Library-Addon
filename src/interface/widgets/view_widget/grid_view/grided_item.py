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

from typing import List

from PySide2.QtWidgets import QGridLayout, QWidget

from .....data import Component
from ...component import ComponentItem


class GridItemWidget(QWidget):
    """
    Custom QWidget class to display a grid of ComponentItem widgets.
    """

    def __init__(self) -> None:
        """
        Constructor to initialize the GridItemWidget.
        """
        super().__init__()
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.__MAX_COL = 3
        self.__cur_row = 0
        self.__cur_col = 0

    def reset(self):
        """
        Method to reset the grid by removing all widgets and resetting indices.
        """
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().deleteLater()
        self.__MAX_COL = 3
        self.__cur_row = 0
        self.__cur_col = 0

    def repopulate(self, components: List[Component]):
        """
        Method to repopulate the grid with a new list of components.

        Parameters
        ----------
        components : list of Component
            The list of components to populate the grid with.
        """
        self.reset()
        self.populate(components)

    def populate(self, components: List[Component]):
        """
        Method to populate the grid with a list of components.

        Parameters
        ----------
        components : list of Component
            The list of components to populate the grid with.
        """
        for data in components:
            component = ComponentItem(self, data)
            self.addItem(component)

    def __next_row(self):
        """
        Method to calculate the next row index for the grid.

        Returns
        -------
        int
            The next row index.
        """
        self.__cur_row = self.__cur_col // self.__MAX_COL
        return self.__cur_row

    def __next_col(self):
        """
        Method to calculate the next column index for the grid.

        Returns
        -------
        int
            The next column index.
        """
        self.__cur_col += 1
        return (self.__cur_col - 1) % self.__MAX_COL

    def addItem(self, item: ComponentItem):
        """
        Method to add a ComponentItem widget to the grid.

        Parameters
        ----------
        item : ComponentItem
            The ComponentItem widget to be added.
        """
        self.grid.addWidget(item, self.__next_row(), self.__next_col())
