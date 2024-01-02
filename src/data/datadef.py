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
from dataclasses import InitVar, dataclass, field
from importlib import metadata
from typing import Any, Literal, TypedDict

from .data_types import DTypes, FileTypes
from .factory import DataFactory


@dataclass(kw_only=True)
class _Data(DataFactory, dtype=None):
    """
    Represents a data object with optional attributes.
    This Class is not suposed to be initialized directly, but is a base for the main DataClases.
    """

    dtype: InitVar[DTypes | None] = None
    id: str = None
    created_at: str = None
    updated_at: str = None

    def __post_init__(self, *args, **kwargs):
        ...


@dataclass(kw_only=True)
class File(_Data, dtype=DTypes.FILE):
    """
    File class represents a file with metadata.

    Parameters
    ----------
    _Data : class
        The base class for data objects.
    dtype : DTypes
        The data type of the file.
    metadata_id : str, optional
        The ID of the metadata.
    updated_at : str, optional
        The timestamp of when the file was last updated.
    size : int, optional
        The size of the file.
    url : str, optional
        The URL of the file.
    type : FileTypes, optional
        The type of the file.
    exists : bool, optional
        Indicates whether the file exists.

    Raises
    ------
    AttributeError
        If the type attribute is not in the expected format.

    Examples
    --------
    file = File()
    file.metadata_id = "123"
    file.updated_at = "2022-01-01"
    file.size = 1024
    file.url = "https://example.com/file.txt"
    file.type = FileTypes.IMAGE
    file.exists = True
    """

    metadata_id: str = None
    updated_at: str = None
    size: int = 0
    url: str = None
    type: FileTypes = field(default=None)
    exists: bool = False

    def __post_init__(self, *args, **kwargs):
        # the data from api has type as dict but in local it is string
        try:
            self.type = FileTypes(self.type.get("name"))
        except AttributeError:
            self.type = FileTypes(self.type)


@dataclass(kw_only=True)
class License(_Data, dtype=DTypes.LICENSE):
    """
    License class represents a license with metadata.

    Parameters
    ----------
    _Data : class
        The base class for data objects.
    dtype : DTypes
        The data type of the license.
    identifier : str, optional
        The identifier of the license.
    fullname : str, optional
        The full name of the license.
    license_page : str, optional
        The URL of the license page.
    fsf_free : bool, optional
        Indicates whether the license is FSF free.
    osi_approved : bool, optional
        Indicates whether the license is OSI approved.

    Examples
    --------
    license = License()
    license.identifier = "MIT"
    license.fullname = "MIT License"
    license.license_page = "https://opensource.org/licenses/MIT"
    license.fsf_free = True
    license.osi_approved = True
    """

    identifier: str = None
    fullname: str = None
    license_page: str = None
    fsf_free: bool = False
    osi_approved: bool = False


@dataclass(kw_only=True)
class Metadata(_Data, dtype=DTypes.METADATA):
    """
    Metadata class represents metadata information.

    Parameters
    ----------
    _Data : class
        The base class for data objects.
    dtype : DTypes
        The data type of the metadata.
    license_id : str, optional
        The ID of the license.
    name : str, optional
        The name of the metadata.
    author : str, optional
        The author of the metadata.
    maintainer : str, optional
        The maintainer of the metadata.
    description : str, optional
        The description of the metadata.
    rating : float, optional
        The rating of the metadata.
    thumbnail : str, optional
        The URL of the thumbnail.
    version : str, optional
        The version of the metadata.

    Examples
    --------
    metadata = Metadata()
    metadata.license_id = "MIT"
    metadata.name = "Component Library"
    metadata.author = "John Doe"
    metadata.maintainer = "Jane Smith"
    metadata.description = "A library for managing components."
    metadata.rating = 4.5
    metadata.thumbnail = "https://example.com/thumbnail.png"
    metadata.version = "1.0.0"
    """

    license_id: str = None
    name: str = None
    author: str = None
    maintainer: str = None
    description: str = None
    rating: float = 0
    thumbnail: str = None
    version: str = None


@dataclass(kw_only=True)
class Tag(_Data, dtype=DTypes.TAG):
    """
    Tag class represents a tag.

    Parameters
    ----------
    _Data : class
        The base class for data objects.
    dtype : DTypes
        The data type of the tag.
    label : str, optional
        The label of the tag.

    Examples
    --------
    tag = Tag()
    tag.label = "Python"
    """

    label: str = ""


@dataclass(kw_only=True)
class Attribute(_Data, dtype=DTypes.ATTRIBUTE):
    key: str = ""
    value: str = ""
    metadata_id: str = ""


@dataclass(kw_only=True)
class Component(DataFactory, dtype=DTypes.COMPONENT):
    """
    Component class represents a component.

    Parameters
    ----------
    DataFactory : class
        The factory class for creating data objects.
    dtype : DTypes
        The data type of the component.
    id : str, optional
        The ID of the component.
    metadata : Metadata, optional
        The metadata of the component.
    files : dict[FileTypes, File], optional
        The files associated with the component.
    license : License, optional
        The license of the component.
    tags : list[Tag], optional
        The tags associated with the component.

    Methods
    -------
    __post_init__(*args, **kwargs)
        Post-initialization method for Component objects.
    serialize(base_info=False)
        Serializes the component.

    Returns
    -------
    dict
        The serialized component.

    Examples
    --------
    component = Component()
    component.id = "123"
    component.metadata = Metadata()
    component.metadata.name = "Component Library"
    component.files = {FileTypes.CODE: File()}
    component.license = License()
    component.license.identifier = "MIT"
    component.tags = [Tag(label="Python")]
    component.serialize()
    """

    dtype: InitVar[DTypes | None] = None
    id: str = ""
    metadata: Metadata = None
    files: dict[FileTypes, File] = field(default_factory=dict)
    license: License = None
    tags: list[Tag] = field(default_factory=list)
    attributes: list[Attribute] = field(default_factory=list)

    def __post_init__(self, *args, **kwargs):
        """
        Post-initialization method for Component objects.

        This method is called after the initialization of a Component object. It performs additional setup and data processing.
        It initialize the files, license & tags from JSON-dict to Corresponding dataclasses.

        Parameters
        ----------
        self : Component
            The Component object.

        Returns
        -------
        None

        Examples
        --------
        component = Component()
        component.__post_init__()
        """
        self.metadata = DataFactory.create(dtype=DTypes.METADATA, **self.metadata)

        # files object from api is a list and in local it is a dict
        if isinstance(self.files, list):
            self.files = {
                file.type: file
                for file in DataFactory.load_many(
                    data_list=self.files, dtype=DTypes.FILE
                )
            }
        elif isinstance(self.files, dict):
            self.files = {
                file.type: file
                for file in DataFactory.load_many(
                    data_list=list(self.files.values()), dtype=DTypes.FILE
                )
            }
        self.license = DataFactory.create(dtype=DTypes.LICENSE, **self.license)
        self.tags = DataFactory.load_many(data_list=self.tags, dtype=DTypes.TAG)
        self.attributes = DataFactory.load_many(
            data_list=self.attributes, dtype=DTypes.ATTRIBUTE
        )

    def serialize(self) -> dict[str, Any]:
        """
        Post-initialization method for Component objects.

        This method is called after the initialization of a Component object. It performs additional setup and data processing. It serializes the files, license, and tags from a JSON dictionary to corresponding dataclasses.
        It serialises the files, license & tags objects to JSON-dict.

        Parameters
        ----------
        self : Component
            The Component object.

        Returns
        -------
        None

        Examples
        --------
        component = Component()
        component.__post_init__()
        """

        original_files = self.files
        self.files = {key.value: value for key, value in self.files.items()}
        data = super().serialize()
        self.files = original_files
        return data


class DataJsonEncoder(json.JSONEncoder):
    """
    DataJsonEncoder class is a custom JSON encoder that handles serialization of specific data objects.

    Parameters
    ----------
    obj : Any
        The object to be serialized.

    Returns
    -------
    Union[dict[str, Any], Any, Literal['stl', 'fcstd', 'fcstd1', 'step', 'stp']]
        The serialized object.
    """

    def default(
        self, obj: Any
    ) -> dict[str, Any] | Any | Literal["stl", "fcstd", "fcstd1", "step", "stp"]:
        """
        Serializes the given object based on its type.

        Parameters
        ----------
        obj : Any
            The object to be serialized.

        Returns
        -------
        Union[dict[str, Any], Any, Literal['stl', 'fcstd', 'fcstd1', 'step', 'stp']]
            The serialized object.

        """

        if isinstance(obj, (Component, Metadata, File, License, Tag)):
            return obj.serialize()
        if isinstance(obj, FileTypes):
            return obj.value
        return json.JSONEncoder.default(self, obj)


SerialisedDataType = Component | Tag | Metadata | License | File
