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

from PySide2.QtCore import QFile, QIODevice, QUrl, QUrlQuery
from PySide2.QtNetwork import QHttpMultiPart, QHttpPart, QNetworkRequest

from .query import RepoComponentQuery
from ....logging import logger


class ComponentRequest(QNetworkRequest):
    """
    Extends QNetworkRequest. Special Request for Components
    """

    endpoint: str = "component"

    def __init__(
        self, state: Union[RepoComponentQuery, None] = None, *args, **kwargs
    ) -> None:
        """
        Initializes the ComponentRequest object.
        """
        super().__init__(*args, **kwargs)
        self.setUrl(self.endpoint)
        if isinstance(state, RepoComponentQuery):
            self.from_states(state)

    def from_states(self, state: RepoComponentQuery) -> None:
        """
        Constructs a URL query based on the provided 'RepoComponentQuery' state and sets the URL of the request.

        Args
        ----
        state : RepoComponentQuery
            The state object containing the query parameters.

        Returns
        -------
        None
        """

        query_list: List[str] = [
            state.page,
            state.page_size,
            state.search_str,
            state.sort_by,
            state.sort_ord,
            state.file_types,
            state.tags,
            state.columns,
        ]
        query = QUrlQuery()
        query.setQuery("&".join(item for item in query_list if item))

        url: QUrl = self.url()
        url.setQuery(query)
        self.setUrl(url)


def construct_multipart(data: dict) -> QHttpMultiPart:
    """
    Constructs a multipart form data object for creation of a Component.

    Args
    ----
    data : dict
        The data dictionary containing the file and text parts.

    Returns
    -------
    QHttpMultiPart
        The constructed multipart form data object.

    Example
    -------
    data = {
        "files": {
            "file1": "/path/to/file1",
            "file2": ["/path/to/file2", "/path/to/file3"]
        },
        "text1": "value1",
        "text2": ["value2", "value3"]
    }
    multipart = construct_multipart(data)
    """
    multi_part = QHttpMultiPart(QHttpMultiPart.ContentType.FormDataType)

    # Append file parts to the multi-part form data
    for field, val in data.pop("files").items():
        if not isinstance(val, (list, tuple, set)):
            val = [val]
        for filepath in val:
            if not filepath:
                continue
            multi_part.append(construct_file_part(field, filepath))

    # Append text parts to the multi-part form data
    for field, value in data.items():
        if isinstance(value, (list, tuple, set)):
            value = ",".join(value)
        multi_part.append(construct_text_parts(field, value))

    return multi_part


def construct_text_parts(field, value) -> QHttpPart:
    """
    Constructs a text part for the multipart form data.

    Args
    ----
    field : str
        The field name of the text part.
    value : Any
        The value of the text part.

    Returns
    -------
    QHttpPart
        The constructed text part.

    Example
    -------
    field = "text_field"
    value = "Hello, world!"
    text_part = construct_text_parts(field, value)
    """
    post_part = QHttpPart()
    post_part.setHeader(
        QNetworkRequest.KnownHeaders.ContentDispositionHeader,
        f'form-data; name="{field}"',
    )
    post_part.setBody(str(value).encode())
    return post_part


def construct_file_part(field, filepath) -> QHttpPart:
    """
    Constructs a file part for the multipart form data.

    Args
    ----
    field : str
        The field name of the file part.
    filepath : str
        The path to the file.

    Returns
    -------
    QHttpPart | None
        The constructed file part if the file is successfully opened in read-only mode, None otherwise.
    """

    logger.debug(f"File path: {filepath}")
    file = QFile(filepath)
    # if not file.open(QIODevice.OpenModeFlag.ReadOnly):
    #     print(f"File not found: {filepath}")
    file = open(filepath, "rb")
    post_part = QHttpPart()
    post_part.setHeader(
        QNetworkRequest.KnownHeaders.ContentDispositionHeader,
        f'form-data; name="{field}"; filename="{file.name}"',
    )
    # post_part.setBodyDevice(file)
    post_part.setBody(file.read())
    return post_part
