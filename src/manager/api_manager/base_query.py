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

from abc import ABC, abstractproperty
from typing import Any, Union

QueryParam = Union[Any, str]


class ComponentQueryInterface(ABC):
    """
    Abstract Base Class for component query interface.

    Attributes
    ----------
    page : QueryParam
        Abstract property representing the page number or query parameter for pagination.
    page_size : QueryParam
        Abstract property representing the page size or query parameter for pagination.
    search_str : QueryParam
        Abstract property representing the search key or query parameter for searching components.
    sort_by : QueryParam
        Abstract property representing the sort key or query parameter for sorting components.
    sort_ord : QueryParam
        Abstract property representing the sort order or query parameter for sorting components.
    file_types : QueryParam
        Abstract property representing the file types or query parameter for filtering components by file types.
    tags : QueryParam
        Abstract property representing the tags or query parameter for filtering components by tags.
    columns : QueryParam
        Abstract property representing the columns or query parameter for selecting specific columns in the result.
    """

    @abstractproperty
    def page(self) -> QueryParam:
        """Abstract property representing the page number or query parameter for pagination."""
        ...

    @abstractproperty
    def page_size(self) -> QueryParam:
        """Abstract property representing the page size or query parameter for pagination."""
        ...

    @abstractproperty
    def search_str(self) -> QueryParam:
        """Abstract property representing the search key or query parameter for searching components."""
        ...

    @abstractproperty
    def sort_by(self) -> QueryParam:
        """Abstract property representing the sort key or query parameter for sorting components."""
        ...

    @abstractproperty
    def sort_ord(self) -> QueryParam:
        """Abstract property representing the sort order or query parameter for sorting components."""
        ...

    @abstractproperty
    def file_types(self) -> QueryParam:
        """Abstract property representing the file types or query parameter for filtering components by file types."""
        ...

    @abstractproperty
    def tags(self) -> QueryParam:
        """Abstract property representing the tags or query parameter for filtering components by tags."""
        ...

    @abstractproperty
    def columns(self) -> QueryParam:
        """Abstract property representing the columns or query parameter for selecting specific columns in the result."""
        ...
