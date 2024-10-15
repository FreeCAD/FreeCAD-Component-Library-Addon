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

from PySide2.QtCore import QEventLoop, QUrl
from PySide2.QtNetwork import QNetworkReply, QNetworkRequest

from ....config import Config
from ...network_manager import get_network_access_manager
from ....utils import singleton
from ..base_api import ApiInterface
from ..exceptions import Connection_Error
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

    @staticmethod
    def check_server_connection() -> None:
        request = QNetworkRequest()
        request.setUrl(QUrl.fromUserInput(CMSApi().BASEURL))
        reply: QNetworkReply = CMSApi().network_access_manager.get(request)

        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()

        if reply.error() == QNetworkReply.NetworkError.ConnectionRefusedError:
            raise Connection_Error()

    @staticmethod
    def prepare_api_request(request: QNetworkRequest) -> None:
        """
        Prepares the API request by setting the absolute path and SSL Configuration.

        Args
        ----
        request : QNetworkRequest
            The network request object.

        Returns
        -------
        None
        """

        absolute_path: str = f"{CMSApi().BASEURL}/{request.url().toString()}"
        request.setUrl(QUrl.fromUserInput(absolute_path))
        request.setSslConfiguration(CMSApi().sslConfig)
        # request.setRawHeader(
        #     "Auth-Token".encode("utf-8"),
        #     str(Config.GITHUB_ACCESS_TOKEN).encode("utf-8"),
        # )
        request.setRawHeader(
            "JWT".encode("utf-8"),
            str(Config.JWT_TOKEN).encode("utf-8"),
        )

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
