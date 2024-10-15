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

from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, cast

from PySide2.QtCore import QEventLoop, Signal, Slot, SignalInstance
from PySide2.QtNetwork import QNetworkRequest

from ..api_manager.cms_api import (
    CMSApi,
    CMSReply,
    ComponentRequest,
    RepoComponentQuery,
    construct_multipart,
)
from ..api_manager.local_api import LocalApi
from ...config import Config
from ...data import Component, DataFactory, DTypes, FileTypes, SerialisedDataType
from ..download_manager import FileDownloader
from ..page_manager import PageStates
from .base import ManagerInterface
from ...logging import logging

class OnlineRepoManager(ManagerInterface):
    """
    Manager for interaction with the Component Management System API(online repository)

    """

    component_loaded = cast(SignalInstance, Signal())
    api: CMSApi

    query: RepoComponentQuery = RepoComponentQuery()
    page_states = PageStates()

    def __init__(self) -> None:
        """
        Initialize the OnlineRepoManager
        """
        super().__init__()
        self.api = CMSApi()
        self.local = LocalApi()

    def request_components(self) -> CMSReply:
        """
        Request components from the Component Management System API

        Returns
        -------
        CMSReply
            network reply from API
        """
        reply: CMSReply = self.api.read(ComponentRequest(self.query))
        reply.finished.connect(self.__component_response_handler)
        return reply

    def reload_page(self) -> CMSReply:
        """
        Reloads page and updates content according to current query

        Returns
        -------
        CMSReply
            network reply from API
        """
        self.query.page = 1
        return self.request_components()

    def next_page(self) -> CMSReply:
        """
        Go to the next page

        Returns
        -------
        CMSReply
            network reply from API
        """
        self.query.page = self.page_states.next_page
        return self.request_components()

    def prev_page(self) -> CMSReply:
        """
        Go to previous page

        Returns
        -------
        CMSReply
            network reply from API
        """
        self.query.page = self.page_states.prev_page
        return self.request_components()

    def search(self, search_str: str) -> CMSReply:
        """
        Search a component in the Component Management System API

        Parameters
        ----------
        search_str : str
            name of component to search

        Returns
        -------
        CMSReply
            network reply from API
        """
        self.query.search_str = search_str
        self.query.sort_ord = "descending"
        return self.reload_page()

    def sort(self, /, by: str, order: str) -> CMSReply:
        """
        Sorts the components by given field and order of sorting

        Parameters
        ----------
        by : str
            field to sort with
        order : str
            order of sorting

        Returns
        -------
        CMSReply
            network reply from API
        """
        self.query.sort_by = by
        self.query.sort_ord = order
        return self.reload_page()

    def filter(self, /, filetypes: List[str], tags: List[str]) -> CMSReply:
        """
        Filters the components by filetype and tags

        Parameters
        ----------
        filetypes : List[str]
            filetypes to filter with
        tags : List[str]
            tags to filter with

        Returns
        -------
        CMSReply
            network reply from API
        """
        self.query.file_types = filetypes
        self.query.tags = tags
        return self.reload_page()

    def download_component(
        self, component: Component, filetype: FileTypes
    ) -> FileDownloader:
        """
        Download a component from the Component Management System API to the Local.

        Parameters
        ----------
        component : Component
            component to download
        filetype : FileTypes
            type of file to download

        Returns
        -------
        FileDownloader
            A downloader object containing all relevant download information.
        """
        file = component.files.get(filetype)
        if file is None:
            raise FileNotFoundError()

        component_path = self.local.component_path(component.metadata.name)

        component_downloader = FileDownloader(
            file.url,
            component_path,
            f"{component.metadata.name}.{file.type.value}",
        )

        if component.metadata.thumbnail and not any(
            path.match("thumbnail.*") for path in component_path.glob("thumbnail.*")
        ):
            FileDownloader(
                component.metadata.thumbnail,
                component_path,
                f"thumbnail{Path(component.metadata.thumbnail).suffix}",
            )

        self.local.create(component, filetype)

        return component_downloader

    def create_component(self, data: dict) -> CMSReply:
        """
        Create a component. This is a POST request.

        Parameters
        ----------
        data : dict
            post data

        Returns
        -------
        CMSReply | None
            CMSReply contains the reply of created component.
            None if multi_part is not valid
        """
        multi_part = construct_multipart(data)

        # if not multi_part:
        #     return

        request = ComponentRequest()
        logging.debug(f"{Config.JWT_TOKEN}")
        request.setRawHeader("Token".encode(), Config.JWT_TOKEN.encode())
        request.setRawHeader(
            "X-Access-Token".encode(), Config.GITHUB_ACCESS_TOKEN.encode()
        )
        reply = self.api.create(request, multi_part)
        multi_part.setParent(reply)
        return reply

    @lru_cache
    def load_from_db(self, dtype: DTypes) -> List[SerialisedDataType]:
        """
        Load data from the database

        Parameters
        ----------
        dtype : DTypes
            Data type to load

        Returns
        -------
        List[SerialisedDataType]|None
            serialised data from db
        """
        return DataFactory.load_many(DbDataLoader(dtype).data, dtype)

    @Slot(dict)
    def __component_response_handler(self, json_data: Dict[str, Any]) -> None:
        """
        Handles what happens when the API responds with data

        Parameters
        ----------
        json_data : Dict[str, Any]
            The response json dict.
        """
        self.page_states.load_page(json_data)
        self.query.page = self.page_states.page_no
        self.query.page_size = self.page_states.size
        self.component_loaded.emit()

    def remove_file(self, component: Component, filetype: FileTypes) -> None:
        """
        Remove a file associated with a component from Local storage

        Parameters
        ----------
        component : Component
            component to remove to remove from
        filetype : FileTypes
            the type of file to remove from a component
        """
        self.local.delete(component, filetype)


class DbDataLoader:
    """
    This class is for loading data from Component Management System Database
    """

    def __init__(self, dtype: DTypes) -> None:
        """
        Initialize the DbDataLoader to load data.

        Parameters
        ----------
        dtype : DTypes
            Data Type to load.
        """
        reply: CMSReply = CMSApi().read(QNetworkRequest(self.get_route(dtype)))
        loop = QEventLoop(parent=reply)
        reply.finished.connect(loop.quit)
        loop.exec_()
        self.data: list = reply.data.get("items", [])

    @staticmethod
    def get_route(dtype: DTypes) -> str:
        """
        Gives the relative route of the api to get a data type.

        Parameters
        ----------
        dtype : DTypes
            Data Type to load.

        Returns
        -------
        str
            relative route.
        """
        if dtype == DTypes.TAG:
            return "tag"
        elif dtype == DTypes.LICENSE:
            return "license"
        else:
            return ""
