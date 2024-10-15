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

from __future__ import annotations

from enum import Enum
from typing import Union

from PySide2.QtCore import QSize
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QWidget


class Star(QLabel):
    """
    Custom QLabel representing a star.
    """

    class State(Enum):
        """
        Enum class to represent star states (filled or empty).
        """

        Empty = "src/interface/resources/emptystar.png"
        Filled = "src/interface/resources/filledstar.png"

    def __init__(self, parent):
        """
        Constructor to initialize the Star.
        """
        super().__init__(parent)
        self.setFixedSize(QSize(15, 15))
        self.setScaledContents(True)
        self.state = None
        self.setState(self.State.Empty)
        self.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum,
        )

    def setState(self, state: Star.State):
        """
        Method to set the state of the star.

        Parameters
        ----------
        state : Star.State
            The state to set for the star.
        """
        if self.state == state:
            return
        self.state = state
        self.setPixmap(QPixmap(state.value))


class StarRating(QWidget):
    """
    Custom QWidget class to represent a star rating system.
    """

    def __init__(
        self,
        parent: Union[QWidget, None] = None,
        default_value: float = 0,
        max_value: int = 5,
    ) -> None:
        """
        Constructor to initialize the StarRating.

        Parameters
        ----------
        parent : QWidget or None, optional
            The parent widget, by default None.
        default_value : float, optional
            The default rating value, by default 0.
        max_value : int, optional
            The maximum rating value, by default 5.
        """
        super().__init__(parent)
        self.value: float = default_value
        self.max_value: int = max_value
        self.setupUi()

    def setupUi(self):
        """
        Method to setup the user interface elements.
        """
        self.hbox_layout = QHBoxLayout()
        self.setLayout(self.hbox_layout)
        self.value_label = QLabel()
        self.value_label.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum,
        )
        self.hbox_layout.addWidget(self.value_label)
        for i in range(1, self.max_value + 1):
            star = Star(self)
            if i <= self.value:
                star.setState(Star.State.Filled)
            self.hbox_layout.addWidget(star)

    def setRating(self, rating: float):
        """
        Method to set the star rating value.

        Parameters
        ----------
        rating : float
            The rating value to set.
        """
        self.value = rating
        self.value_label.setNum(self.value)
        for i in range(1, self.hbox_layout.count()):
            star: Star = self.hbox_layout.itemAt(i).widget()
            if i <= self.value:
                star.setState(Star.State.Filled)
            else:
                star.setState(Star.State.Empty)
