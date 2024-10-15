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
from typing import Any, Dict, cast

from PySide2.QtCore import QObject, Signal, Slot, SignalInstance
from PySide2.QtNetwork import QNetworkReply

from ....logging import logger


class CMSReply(QObject):
    """
    Represents a CMS reply object.
    Custom QObject class to handle network replies and emit signals with parsed data.
    """

    finished = cast(
        SignalInstance, Signal(dict)
    )  # Signal to be emitted when the reply is finished, with the parsed data as an argument

    def __init__(self, reply: QNetworkReply, parent) -> None:
        super().__init__(parent)
        self.reply: QNetworkReply = reply
        self.reply.finished.connect(self.response_serializer)

    # @Slot()
    def response_serializer(self) -> None:
        """
        Slot method to handle the network reply and parse the JSON data.

        This method checks if there was an error in the network reply.
        If there is no error, it reads the raw data from the network reply, decodes it as UTF-8, and parses it as JSON.
        If the parsed data is a list, it converts it to a dictionary using the 'id' field as the key.
        Finally, it emits the 'finished' signal with the parsed data and deletes the network reply.

        Returns
        -------
        None
        """

        # Check if there was an error in the network reply
        if self.reply.error() != QNetworkReply.NetworkError.NoError:
            logger.warning(f"{self.reply.url()}: {self.reply.errorString()}")

        # Read the raw data from the network reply and decode it as UTF-8 as parse as JSON
        raw_data: str = self.reply.readAll().data().decode("utf-8")
        self.data = self.parse_json(raw_data)

        # If the parsed data is a list, convert it to a dictionary using the 'id' field as the key
        if isinstance(self.data, list):
            self.data = {item.get("id"): item for item in self.data}

        self.finished.emit(self.data)
        self.reply.deleteLater()

    @staticmethod
    def parse_json(data: str) -> Dict[Any, Any]:
        """
        Parses JSON data.

        Args
        ----
        data : str
            The JSON data to be parsed.

        Returns
        -------
        dict
            The parsed JSON data as a dictionary. If the JSON data cannot be decoded, an empty dictionary is returned.
        """

        try:
            parsed_json: dict = json.loads(data)
        except json.decoder.JSONDecodeError:
            parsed_json = dict()
        return parsed_json
