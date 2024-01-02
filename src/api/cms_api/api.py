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

from typing import Any

from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QNetworkRequest

from src.config.config import Config

from ...network import get_network_access_manager
from ...utils import singleton
from ..base_api import ApiInterface
from .replies import CMSReply


@singleton
class CMSApi(ApiInterface):
    """
    A singleton class representing the Component Management System API.
    """

    network_access_manager, sslConfig = get_network_access_manager()

    BASEURL: str = Config.API_URL + "/api"

    def __init__(self) -> None:
        """
        Initializes an instance of CMSApi.

        Returns
        -------
        None
        """

        super().__init__()

    def prepare_api_request(self, request: QNetworkRequest) -> None:
        """
        Prepares the API request by setting the absolute path and SSL configuration.

        Args
        ----
        request : QNetworkRequest
            The network request object.

        Returns
        -------
        None
        """

        absolute_path: str = f"{self.BASEURL}/{request.url().toString()}"
        request.setUrl(QUrl.fromUserInput(absolute_path))
        request.setSslConfiguration(self.sslConfig)

    def read(self, request: QNetworkRequest) -> CMSReply:
        """
        Performs a read operation on the API.

        Args
        ----
        request : QNetworkRequest
            The network request object.

        Returns
        -------
        CMSReply
            The CMS reply object.
        """

        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.get(request), self)

    def create(self, request: QNetworkRequest, data: Any) -> CMSReply:
        """
        Performs a create operation on the API.

        Args
        ----
        request : QNetworkRequest
            The network request object.
        data : Any
            The data to be sent in the request.

        Returns
        -------
        CMSReply
            The CMS reply object.
        """

        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.post(request, data), self)

    def update(self, request: QNetworkRequest, data: bytes) -> CMSReply:
        """
        Performs an update operation on the API.

        Args
        ----
        request : QNetworkRequest
            The network request object.
        data : bytes
            The data to be sent in the request.

        Returns
        -------
        CMSReply
            The CMS reply object.
        """

        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.put(request, data), self)

    def delete(self, request: QNetworkRequest) -> CMSReply:
        """
        Performs a delete operation on the API.

        Args
        ----
        request : QNetworkRequest
            The network request object.

        Returns
        -------
        CMSReply
            The CMS reply object.
        """

        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.deleteResource(request), self)
