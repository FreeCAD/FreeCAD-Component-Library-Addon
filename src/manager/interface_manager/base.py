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

from typing import List, cast

from PySide2.QtCore import Signal, SignalInstance

import FreeCAD
import FreeCADGui

from src.data.data_types import FileTypes
from src.data.datadef import Component

from ..api_manager import ApiInterface, ComponentQueryInterface, local_api
from ...utils import ABCQObject
from ..page_manager import PageStates


class ManagerInterface(ABCQObject):
    """
    Abstract class for managenent of APIs. It abstracts the interactions with the API.
    """

    component_loaded: cast(SignalInstance, Signal)
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

    def filter(self, /, filetypes: List[str], tags: List[str]):
        """
        Method to filter components based on filetypes and tags.

        Parameters
        ----------
        filetypes : List[str]
            filetypes to filter
        tags : List[str]
            tags to filter
        """

    def insert_in_active_freecad_doc(self, component: Component, filetype: FileTypes):
        file_path = local_api.LocalApi().file_path(component.metadata.name, filetype)
        current_document = FreeCAD.activeDocument()
        if current_document is None:
            raise ValueError("No active document found.")
        FreeCADGui.insert(str(file_path), current_document.Name)
        return file_path

    def insert_in_new_freecad_doc(self, component: Component, filetype: FileTypes):
        FreeCAD.newDocument()
        file_path = self.insert_in_active_freecad_doc(component, filetype)
        return file_path
