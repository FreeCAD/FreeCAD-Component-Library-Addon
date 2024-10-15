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

from dataclasses import dataclass, field
from typing import Any, Dict, List, Union, cast

from PySide2.QtCore import QObject, Signal, SignalInstance

from .api_manager.local_api.storage_adapter import LocalData
from ..config import Config
from ..data import Component, DataFactory, DTypes


@dataclass
class PageStates(QObject):
    """
    PageStates This class manages the page states and the data of the page.
    Including pagination and signals for next/prev page buttons.
    """

    enable_next = cast(
        SignalInstance, Signal(bool)
    )  # Signal to enable or disable the next page button.
    enable_prev = cast(
        SignalInstance, Signal(bool)
    )  # Signal to enable or disable the previous page button.

    data: List[Component] = field(default_factory=list)
    total_items: int = 0
    page_no: int = 0
    total_pages = 0
    size: int = 18
    next_page: Union[int, None] = None
    prev_page: Union[int, None] = None

    def __init__(self, *args, **kwargs):
        super(QObject, self).__init__()
        super().__init__(*args, **kwargs)

    def load_page(self, json_response: Dict[str, Any]):
        """
        Load page data from JSON response and calculate pagination.

        Parameters
        ----------
        json_response : Dict[str, Any]
            the response forn the API.
        """
        self.load_page_data(json_response)
        self.calculate_pagination()  # TODO: Calculate pagination and emit signals.

    def load_page_data(self, json_response: Dict[str, Any]) -> None:
        """
        Loads the page data and states

        Parameters
        ----------
        json_response : Dict[str, Any]
            the response from API
        """
        self.data: List[Component] = DataFactory.load_many(
            data_list=json_response.get("items", []), dtype=DTypes.COMPONENT
        )
        self.update_existing_comps(self.data)

        self.total_items = json_response.get("total", 0)
        self.page_no = json_response.get("page", 1)
        self.size = json_response.get("per_page", 18)

    def update_existing_comps(self, components: List[Component]) -> None:
        """
        Update the existing components with file existence information.

        Parameters
        ----------
        components : List[Component]
            list of the serialised components recieved from he API
        """
        with LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
            for component in components:
                self.update_existing_files_for_component(component, local_data)

    def update_existing_files_for_component(
        self, component: Component, local_data
    ) -> None:
        """
        Update the existing files for a component with their existence status.

        It checks if the file already exists in the local system or not and updates its status.

        Parameters
        ----------
        component : Component
            a component object to be updates
        local_data : dict
            an object that contains the local data information.(present in the LocalAPI)
        """
        for file in component.files:
            existing_comps = local_data["filetypes"].get(file.value, set())
            component.files[file].exists = component.metadata.name in existing_comps

    def calculate_pagination(self) -> None:
        """Calculate the pagination and emit signals to enable/disable next and previous buttons."""
        self.total_pages = (self.total_items + self.size - 1) // self.size

        if self.page_no == 1:
            self.prev_page = None
            self.enable_prev.emit(False)  # Disable previous page button.
        else:
            self.prev_page = self.page_no - 1
            self.enable_prev.emit(True)  # Enable previous page button.

        if (self.total_items - (self.page_no * self.size)) < 0:
            self.next_page = None
            self.enable_next.emit(False)  # Disable next page button.
        else:
            self.next_page = self.page_no + 1
            self.enable_next.emit(True)  # Enable next page button.
