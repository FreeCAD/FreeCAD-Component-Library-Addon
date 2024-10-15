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

from typing import List, Union

from ..base_query import ComponentQueryInterface


class RepoComponentQuery(ComponentQueryInterface):
    """
    Implementation of the ComponentQueryInterface for querying components in a repository.

    Stores all the Query states for CMS API
    """

    def __init__(self) -> None:
        """
        Initializes the query parameters with default values or None.
        """
        self.__page: Union[int, None] = 1
        self.__page_size: Union[int, None] = 18
        self.__search_str: Union[str, None] = None
        self.__sort_by: Union[str, None] = "name"
        self.__sort_ord: Union[str, None] = "asc"
        self.__file_types: Union[List[str], None] = None
        self.__tags: Union[List[str], None] = None
        self.__columns: Union[List[str], None] = None

    @property
    def page(self) -> str:
        return "" if self.__page is None else f"page={self.__page}"

    @page.setter
    def page(self, value: Union[int, None]) -> None:
        self.__page = value

    @property
    def page_size(self) -> str:
        return "" if self.__page_size is None else f"page_size={self.__page_size}"

    @page_size.setter
    def page_size(self, value: Union[int, None]) -> None:
        self.__page_size = value

    @property
    def search_str(self) -> str:
        return "" if self.__search_str is None else f"search_str={self.__search_str}"

    @search_str.setter
    def search_str(self, value: Union[str, None]) -> None:
        self.__search_str = value

    @property
    def sort_by(self) -> str:
        return "" if self.__sort_by is None else f"sort_by={self.__sort_by}"

    @sort_by.setter
    def sort_by(self, value: Union[str, None]) -> None:
        # Converting values to be compatible with the API
        if value in ("Name", "Rating"):
            value = value.lower()
        elif value == "Created":
            value = "created_at"
        elif value == "Updated":
            value = "updated_at"
        else:
            raise ValueError("Invalid value for sort_by property.")
        self.__sort_by = value

    @property
    def sort_ord(self) -> str:
        return "" if self.__sort_ord is None else f"sort_ord={self.__sort_ord}"

    @sort_ord.setter
    def sort_ord(self, value: Union[str, None]) -> None:
        # Converting values to be compatible with the API
        if value is None:
            pass
        elif value.lower() == "ascending":
            value = "asc"
        elif value.lower() == "descending":
            value = "desc"
        else:
            raise ValueError("Invalid value for sort_ord property.")
        self.__sort_ord = value

    @property
    def file_types(self) -> str:
        if self.__file_types is None or len(self.__file_types) == 0:
            return ""
        return "&".join(
            f"file_types%5B%5D={ft.replace(' ', '%20')}" for ft in self.__file_types
        )

    @file_types.setter
    def file_types(self, value: Union[List[str], None]) -> None:
        if value is not None:
            value = [v.strip() for v in value if v]
        self.__file_types = value

    @property
    def tags(self) -> str:
        if self.__tags is None or len(self.__tags) == 0:
            return ""
        return "&".join(f"tags%5B%5D={t.replace(' ', '%20')}" for t in self.__tags)

    @tags.setter
    def tags(self, value: Union[List[str], None]) -> None:
        if value is not None:
            value = [v.strip() for v in value if v]
        self.__tags = value

    @property
    def columns(self) -> str:
        if self.__columns is None or len(self.__columns) == 0:
            return ""
        return "&".join(
            f"columns%5B%5D={t.replace(' ', '%20')}" for t in self.__columns
        )

    @columns.setter
    def columns(self, value: Union[List[str], None]) -> None:
        if value is not None:
            value = [v.strip() for v in value if v]
        self.__columns = value
