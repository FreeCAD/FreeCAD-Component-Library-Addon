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

import contextlib
from enum import Enum
from typing import Union

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QPushButton


class StatefulPushButton(QPushButton):
    """
    Custom QPushButton class that manages different button states.
    """

    def __init__(self, parent=None) -> None:
        """
        Constructor to initialize the StatefulPushButton.
        """
        super().__init__(parent)
        self.states = {}

    def register_state(
        self, state: Enum, slot: Union[Slot, None], text: str, enable: bool
    ):
        """
        Register a button state along with its properties.

        Parameters
        ----------
        state : Enum
            The state to register.
        slot : Slot or None
            Slot (function) to be connected when this state is active. Can be None.
        text : str
            Text to be displayed on the button when this state is active.
        enable : bool
            Enable or disable the button when this state is active.
        """
        self.states[state] = {
            "slot": slot,
            "text": text,
            "enable": enable,
        }

    def setState(self, state: Enum) -> None:
        """
        Set the button state based on the provided Enum value.

        Parameters
        ----------
        state : Enum
            The state to set for the button.
        """
        if state not in self.states:
            raise ValueError(f"{state} not registered!")

        state_data = self.states[state]

        self.setText(state_data["text"])
        for key, value in self.states.items():
            if key == state:
                continue
            with contextlib.suppress(Exception):
                self.clicked.disconnect(value["slot"])

        if state_data["slot"]:
            self.clicked.connect(state_data["slot"])

        self.setEnabled(state_data["enable"])
