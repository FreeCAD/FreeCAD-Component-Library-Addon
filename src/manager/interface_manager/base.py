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

from PySide6.QtCore import Signal

from ...api import ApiInterface, ComponentQueryInterface
from ...utils import ABCQObject
from ..page_manager import PageStates


class ManagerInterface(ABCQObject):
    """
    Abstract class for managenent of APIs. It abstracts the interactions with the API.
    """

    component_loaded: Signal
    api: ApiInterface
    page_states: PageStates
    query: ComponentQueryInterface

    def reload_page(self):
        """
        Method to reload the current page.
        """

    def next_page(self):
        """
        Method to load the next page of data.
        """

    def prev_page(self):
        """
        Method to load the previous page of data.
        """

    def search(self, search_str: str):
        """
        Method to search for components using the given search_str.

        Parameters
        ----------
        search_str : str
            the component name to search
        """

    def sort(self, /, by: str, order: str):
        """
        Method to sort components based on the given criteria.

        Parameters
        ----------
        by : str
            the value by which to sort
        order : str
            sorting order
        """

    def filter(self, /, filetypes: list[str], tags: list[str]):
        """
        Method to filter components based on filetypes and tags.

        Parameters
        ----------
        filetypes : list[str]
            filetypes to filter
        tags : list[str]
            tags to filter
        """
