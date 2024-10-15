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

from typing import Any, List, Union, cast

from PySide2.QtCore import Signal, SignalInstance

from src.data.factory import DataFactory

from ..api_manager.local_api import LocalApi, LocalComponentQuery
from ...data import Component, DTypes, FileTypes, SerialisedDataType
from ..page_manager import PageStates
from .base import ManagerInterface


class LocalStorageManager(ManagerInterface):
    """
    Manager for the local Storage and functions. Abstracts the interaction with the LocalAPI.
    """

    component_loaded = cast(SignalInstance, Signal())
    api: LocalApi

    page_states = PageStates()

    def __init__(self) -> None:
        """
        Initialize the LocalStorageManager
        """
        super().__init__()
        self.api = LocalApi()

    def request_components(self):
        """
        Request components from the API using the current query
        """
        components = self.api.read()
        self.page_states.load_page(components)
        self.component_loaded.emit()  # Emit signal after components are loaded.

    def reload_page(self):
        """
        Reloads page and updates content according to current query
        """
        return self.request_components()

    def load_from_db(self, dtype: DTypes) -> Union[List[SerialisedDataType], None]:
        """
        Load data from the Local database

        Parameters
        ----------
        dtype : DTypes
            Data type to load

        Returns
        -------
        List[SerialisedDataType]|None
            serialised data from db
        """

        if dtype == DTypes.TAG:
            return DataFactory.load_many(self.api.get_tags(), dtype)

    def remove_file(self, component: Component, filetype: FileTypes):
        """
        Remove a file associated with a component from Local storage

        Parameters
        ----------
        component : Component
            component to remove to remove from
        filetype : FileTypes
            the type of file to remove from a component
        """
        self.api.delete(component, filetype)
