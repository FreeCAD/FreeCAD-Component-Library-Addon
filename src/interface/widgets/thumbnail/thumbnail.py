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

from __future__ import annotations

from typing import Union

from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QLabel, QSizePolicy, QWidget

from ....manager.download_manager import ImageLoader


class Thumbnail(QLabel):
    """
    Custom QLabel class for displaying image thumbnails.
    """

    def __init__(self, parent: QWidget, url: Union[str, None] = None) -> None:
        """
        Constructor to initialize the Thumbnail.

        Parameters
        ----------
        parent : QWidget
            The parent widget.
        url : str or None, optional
            The URL of the image, by default None.
        """
        super().__init__(parent)

        self._raw_image = None

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        # self.setScaledContents(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setPixmap(
            QPixmap(ImageLoader.LOADING_THUMBNAIL_PATH).scaled(
                self.size(),
                aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
                mode=Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.downloader = ImageLoader()
        self.downloader.finished.connect(self.loadImage)
        if url:
            self.setupThumbnail(url)

    def setupThumbnail(self, url_str: str):
        """
        Method to start downloading the image from the provided URL.

        Parameters
        ----------
        url_str : str
            The URL of the image to download.
        """
        self.downloader.start_download(QUrl.fromUserInput(url_str))

    def loadImage(self, image: QImage):
        """
        Method to display the downloaded image as the thumbnail.

        Parameters
        ----------
        image : QImage
            The downloaded image.
        """
        self._raw_image: QImage = image
        self.setPixmap(
            QPixmap(image).scaled(
                self.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

    @staticmethod
    def from_existing(parent, thumbnail: Thumbnail) -> Thumbnail:
        """
        Static method to create a new Thumbnail from an existing Thumbnail's pixmap.

        Parameters
        ----------
        parent : QWidget
            The parent widget.
        thumbnail : Thumbnail
            The existing Thumbnail instance.

        Returns
        -------
        Thumbnail
            A new Thumbnail instance with the same pixmap as the existing thumbnail.
        """
        new_thumbnail = Thumbnail(parent)
        new_thumbnail.setPixmap(
            thumbnail.pixmap().scaled(
                thumbnail.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        # new_thumbnail.loadImage(thumbnail._raw_image)
        return new_thumbnail
