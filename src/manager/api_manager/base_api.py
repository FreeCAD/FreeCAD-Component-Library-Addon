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

from abc import abstractmethod

from PySide2.QtNetwork import QNetworkReply

from ...utils import ABCQObject


class ApiInterface(ABCQObject):
    """
    An abstract base class representing the interface for API operations.
    """

    @abstractmethod
    def create(self, *args, **kwargs) -> QNetworkReply:
        """
        Abstract method for creating a new resource.

        Returns
        -------
        QNetworkReply
            The network reply object.
        """

    @abstractmethod
    def read(self, *args, **kwargs) -> QNetworkReply:
        """
        Abstract method for reading a resource.

        Returns
        -------
        QNetworkReply
            The network reply object.
        """

    @abstractmethod
    def update(self, *args, **kwargs) -> QNetworkReply:
        """
        Abstract method for updating a resource.

        Returns
        -------
        QNetworkReply
            The network reply object.
        """

    @abstractmethod
    def delete(self, *args, **kwargs) -> QNetworkReply:
        """
        Abstract method for deleting a resource.

        Returns
        -------
        QNetworkReply
            The network reply object.
        """
