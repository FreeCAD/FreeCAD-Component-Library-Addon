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

import json
from pathlib import Path
from typing import Any, Dict, List, Set, TypedDict

from src.data.datadef import DataJsonEncoder

from ....data import Component, DataFactory, DTypes
from ....utils import singleton

LocalDataComp = Set[
    str
]  # Type alias for a set of strings representing components in local data


class LocalDataDict(TypedDict):
    """
    Dictionary type for storing local data.

    Attributes
    ----------
    components : LocalDataComp
        The components stored locally.
    tags : Dict[str, LocalDataComp]
        The tags associated with the components.
    filetypes : Dict[str, LocalDataComp]
        The file types associated with the components.
    """

    components: LocalDataComp
    tags: Dict[str, LocalDataComp]
    filetypes: Dict[str, LocalDataComp]


class SetJsonEncoder(json.JSONEncoder):
    """
    Custom JSON encoder that handles encoding of sets.
    """

    def default(self, obj):
        """
        Overrides the default method of the JSONEncoder class to handle encoding of sets.

        Args
        ----
        obj : Any
            The object to be encoded.

        Returns
        -------
        Any
            The encoded object. If the object is a set, it is converted to a list before encoding. Otherwise, the default encoding behavior is used.
        """

        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


class SetJSONDecoder(json.JSONDecoder):
    """
    Custom JSON decoder that converts lists back to sets for specific keys.
    """

    def __init__(self) -> None:
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d: dict) -> Dict[Any, Any]:
        """
        Converts lists back to sets for specific keys in the input dictionary.

        Args
        ----
        self : Any
            The SetJSONDecoder instance.
        d : dict
            The input dictionary.

        Returns
        -------
        Dict[Any, Any]
            The modified dictionary with lists converted to sets for specific keys.
        """

        f = {}
        for key, value in d.items():
            if isinstance(value, list):
                value = set(
                    value
                )  # Convert lists back to sets for keys that should be sets
            f[key] = value
        return f


@singleton
class LocalData:
    """
    Singleton class for managing local data storage.

    This manages the data.json file.
    data.json contains all the information of the components present in local storage, their filetype and tags association
    """

    def __init__(self, storage_path: Path) -> None:
        """
        Initializes the LocalData object.

        Args
        ----
        storage_path : Path
            The path to the storage directory.

        Returns
        -------
        None
        """

        storage_path.mkdir(exist_ok=True)  # If the folder does not exixt, create it.
        self.DATA_PATH = storage_path / "data.json"
        if not self.DATA_PATH.exists():
            self.__reset_data()  # If data file does not exist, create it with default values

    def __enter__(self) -> LocalDataDict:
        """
        Context manager method used to enter the context and read data from the JSON file.

        Returns
        -------
        LocalDataDict
            The loaded data from the JSON file.

        Raises
        ------
        FileNotFoundError
            If the data file does not exist.

        Example
        -------
        with LocalData(storage_path) as data:
        """
        # Load data from the JSON file using SetJSONDecoder for loading lists as set
        with self.DATA_PATH.open("r", encoding="utf-8") as file:
            self.data: LocalDataDict = json.load(file, cls=SetJSONDecoder)
            return self.data

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        """
        Context manager method used to exit the context and write data to the JSON file.

        Args
        ----
        exc_type : Type[BaseException]
            The type of the exception raised, if any.
        exc_value : BaseException
            The exception raised, if any.
        exc_tb : TracebackType
            The traceback of the exception raised, if any.

        Returns
        -------
        None

        Example
        -------
        with LocalData(storage_path) as data:
            data["key"] = "value"
        """

        # Write data back to the JSON file using SetJsonEncoder for loading lists as set
        with self.DATA_PATH.open("w", encoding="utf-8") as file:
            json.dump(self.data, file, cls=SetJsonEncoder, indent=4)

    def __reset_data(self) -> None:
        """
        Resets the data file with default values.

        Args
        ----
        self : Any
            The LocalData instance.

        Returns
        -------
        None
        """

        with self.DATA_PATH.open("w", encoding="utf-8") as file:
            # Initialize the data file with default empty lists and dictionaries
            json.dump(
                {
                    "components": [],
                    "tags": {},
                    "filetypes": {},
                },
                file,
                indent=4,
            )


class ComponentDataDict(TypedDict):
    """
    Type hint for the dictionary structure of component data.

    Attributes
    ----------
    files : Dict[str, Dict[str, Any]]
        The files associated with the component.
    id : str
        The ID of the component.
    license : Dict[str, Any]
        The license information of the component.
    metadata : Dict[str, Any]
        The metadata of the component.
    tags : List[Dict[str, Any]]
        The tags associated with the component.

    """

    files: Dict[str, Dict[str, Any]]
    id: str
    license: Dict[str, Any]
    metadata: Dict[str, Any]
    tags: List[Dict[str, Any]]


class ComponentData:
    """
    Class for managing component data.
    It handles the metadata.json file for individual components.
    """

    def __init__(self, component_data_path: Path) -> None:
        """
        Initializes the ComponentData object.

        Args
        ----
        component_data_path : Path
            The path to the component data file.

        Returns
        -------
        None
        """

        self.data_path: Path = component_data_path
        self.data_path.touch(exist_ok=True)

    def __enter__(self) -> Component:
        """
        Context manager method used to enter the context and retrieve existing component data.

        Returns
        -------
        Component
            The existing component data.

        Raises
        ------
        json.JSONDecodeError
            If the existing data cannot be decoded from JSON.

        Example
        -------
        with ComponentData(component_data_path) as data:
        """

        with self.data_path.open("r", encoding="utf-8") as file:
            try:
                self.existing_data: Component = DataFactory.create(
                    dtype=DTypes.COMPONENT, **json.load(file)
                )
            except json.JSONDecodeError:
                self.existing_data: Component = DataFactory.create(
                    dtype=DTypes.COMPONENT, **self._default_dict()
                )
        return self.existing_data

    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        Context manager method used to exit the context and write component data to the file.

        Args
        ----
        exc_type : Type[BaseException]
            The type of the exception raised, if any.
        exc_value : BaseException
            The exception raised, if any.
        exc_tb : TracebackType
            The traceback of the exception raised, if any.

        Returns
        -------
        None
        """

        with self.data_path.open("w", encoding="utf-8") as file:
            json.dump(self.existing_data, file, indent=4, cls=DataJsonEncoder)

    def _default_dict(self):
        """
        Returns the default dictionary for component data.

        Returns
        -------
        dict
            The default dictionary for component data.
        """

        return {
            "files": {},
            "id": "",
            "license": {},
            "metadata": {},
            "tags": [],
        }
