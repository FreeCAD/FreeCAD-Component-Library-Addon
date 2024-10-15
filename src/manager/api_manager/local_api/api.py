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
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Iterable, List, Union

from ....config import Config
from ....data import Component, FileTypes
from ....utils import singleton
from ..base_api import ApiInterface
from .storage_adapter import ComponentData, ComponentDataDict, LocalData, LocalDataComp


@singleton
class LocalApi(ApiInterface):
    """
    A class representing a local API interface for CRUD operations on components.
    """

    def create(self, component: Component, filetype: FileTypes) -> None:
        """
        Create a new component in the local storage.

        Args
        ----
        component : Component
            The component to be created.
        filetype : FileTypes
            The type of file associated with the component.

        Returns
        -------
        None
        """

        self._handle_component_data_creation(component, filetype)
        self._handle_local_data_creation(component, filetype)

    def _handle_component_data_creation(
        self, component: Component, filetype: FileTypes
    ) -> None:
        """
        Handle the creation of component data.

        Args
        ----
        component : Component
            The component to be created.
        filetype : FileTypes
            The type of file associated with the component.

        Returns
        -------
        None
        """

        comp_name: str = component.metadata.name

        with ComponentData(self.metadata_path(comp_name)) as existing_data:

            if existing_data.id == "":
                existing_data.id = component.id
                existing_data.metadata = deepcopy(component.metadata)
                existing_data.license = component.license
                existing_data.tags = component.tags

            existing_data.files[filetype] = deepcopy(component.files[filetype])
            existing_data.files[filetype].url = (
                (self.component_path(comp_name) / f"{comp_name}.{filetype.value}")
                .absolute()
                .as_uri()
            )

            if component.metadata.thumbnail is not None:
                existing_data.metadata.thumbnail = (
                    (
                        self.component_path(comp_name)
                        / f"thumbnail{Path(component.metadata.thumbnail).suffix}"
                    )
                    .absolute()
                    .as_uri()
                )

    def _handle_local_data_creation(
        self, component: Component, filetype: FileTypes
    ) -> None:
        """
        Handle the creation of local data.

        Args
        ----
        component : Component
            The component for which local data is being created.
        filetype : FileTypes
            The type of file associated with the component.

        Returns
        -------
        None
        """

        comp_name: str = component.metadata.name

        with LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
            local_data["components"].add(comp_name)
            local_data["filetypes"].setdefault(filetype.value, set()).add(comp_name)

            for tag in component.tags:
                local_data["tags"].setdefault(tag.label, set()).add(comp_name)

    def read(self) -> Dict[str, Any]:
        """
        Read the component data from the local storage.

        Returns
        -------
        dict
            A dictionary containing the component data.

        Example
        -------
        api = LocalApi()
        data = api.read()
        """
        data = {
            "items": [],
            "page": 0,
            "per_page": 18,
            "total": 0,
        }
        for path in Config.LOCAL_COMPONENT_PATH.iterdir():
            if not path.is_dir():
                continue
            with open(path / "metadata.json", "r", encoding="utf-8") as metadata:
                data["items"].append(json.load(metadata))
            data["total"] += 1
            data["page"] = data["total"] // data["per_page"] + 1

        return data

    def update(self): ...

    def delete(
        self, component: Component, filetypes: Union[Iterable[FileTypes], FileTypes]
    ) -> None:
        """
        Delete the component and associated files from the local storage.

        Args
        ----
        component : Component
            The component to be deleted.
        filetypes : Iterable[FileTypes]|FileTypes
            The type(s) of files associated with the component.

        Returns
        -------
        None
        """

        comp_name = component.metadata.name
        component_path = self.component_path(comp_name)
        remove_component = False

        with ComponentData(self.metadata_path(comp_name)) as comp_data, LocalData(
            Config.LOCAL_COMPONENT_PATH
        ) as local_data:
            if isinstance(filetypes, FileTypes):
                filetypes = [filetypes]
            for filetype in filetypes:
                comp_data.files.pop(filetype)
                local_data["filetypes"][filetype.value].remove(comp_name)
                (component_path / f"{comp_name}.{filetype.value}").unlink()

            if not any(
                comp_data.files.values()
            ):  # checking if there are no files present
                remove_component = True
                local_data["components"].remove(comp_name)
                for comp_list in local_data["tags"].values():
                    with contextlib.suppress(KeyError):
                        comp_list.remove(comp_name)

        if remove_component:
            shutil.rmtree(component_path)

    @classmethod
    def component_path(cls, component_name: str) -> Path:
        """
        Get the path to the component directory.

        Args
        ----
        component_name : str
            The name of the component.

        Returns
        -------
        Path
            The path to the component directory.
        """

        return Config.LOCAL_COMPONENT_PATH / component_name

    @classmethod
    def metadata_path(cls, component_name: str) -> Path:
        """
        Get the path to the metadata file for a component.

        Args
        ----
        component_name : str
            The name of the component.

        Returns
        -------
        Path
            The path to the metadata file.
        """
        return cls.component_path(component_name) / "metadata.json"

    @classmethod
    def file_path(cls, component_name: str, file_type: FileTypes) -> Path:
        return (
            cls.component_path(component_name) / f"{component_name}.{file_type.value}"
        )

    def get_tags(self) -> List[Dict[str, str]]:
        """
        Get the tags from the local data.

        Returns
        -------
        List[Dict[str, str]]
            A list of dictionaries containing the tags.
        """
        with LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
            return [{"label": tag} for tag in local_data["tags"].keys()]
