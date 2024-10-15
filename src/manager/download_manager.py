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

from pathlib import Path
from typing import cast

from PySide2.QtCore import QFile, QIODevice, QObject, QUrl, Signal, Slot, SignalInstance
from PySide2.QtGui import QImage
from PySide2.QtNetwork import QNetworkReply, QNetworkRequest

from .network_manager import get_network_access_manager
from ..logging import logger


class FileDownloader(QObject):
    """
    FileDownloader Handles downloading of files/components (any resource) ans saves it locally.
    """

    finished = cast(
        SignalInstance, Signal(Path)
    )  # Signal emitted when the download is finished.
    error = cast(
        SignalInstance, Signal(QNetworkReply.NetworkError)
    )  # Signal emitted when there's an error during download.

    network_access_manager, sslConfig = get_network_access_manager()

    def __init__(self, url: str, save_path: Path, filename: str) -> None:
        """
        __init__ FileDownloader initializer

        Args:
            url (str): url of the resource to be downloaded
            save_path (Path): the destination of the the file to be saved
            filename (str): name by which the resource will be saved
        """
        super().__init__()

        self.url = QUrl(url)
        save_path.mkdir(exist_ok=True)
        self.filename: str = filename
        self.filepath = save_path / self.filename

        request = QNetworkRequest(self.url)
        self.reply: QNetworkReply = self.network_access_manager.get(request)
        self.reply.finished.connect(lambda: self.__downloaded(self.reply))
        self.downloadProgress = self.reply.downloadProgress

    @Slot(QNetworkReply)
    def __downloaded(self, reply: QNetworkReply):
        """Slot to handle the download completion and saving the downloaded file."""
        if reply.error() != QNetworkReply.NetworkError.NoError:
            logger.warning(f"{reply.url()}: {reply.error()}")
            self.error.emit(reply.error())

        file = QFile(str(self.filepath))

        if file.open(QIODevice.OpenModeFlag.WriteOnly):
            file.write(reply.readAll())

        file.close()

        self.finished.emit(self.filepath)

        reply.deleteLater()
        self.deleteLater()


class ImageLoader(QObject):
    """
    ImageLoader Downloads the image but does not save it at some location but serialises it as QImage.
    """

    LOADING_THUMBNAIL_PATH = "src/interface/resources/loading.jpeg"
    DEFAULT_THUMBNAIL_PATH = "src/interface/resources/default.png"

    finished = cast(
        SignalInstance, Signal(QImage)
    )  # Signal emitted when the image is loaded.

    network_access_manager, sslConfig = get_network_access_manager()

    def __init__(self, parent=None):
        super().__init__(parent)

    def start_download(self, url: QUrl):
        """
        start_download makes the request for downloading the image.

        Args:
            url (QUrl): url of the image.
        """
        reply: QNetworkReply = self.network_access_manager.get(QNetworkRequest(url))
        reply.finished.connect(lambda: self.handle_finished(reply))

    def handle_finished(self, reply: QNetworkReply):
        """
        handle_finished Method to handle the finished download and emit the loaded image.

        Args:
            reply (QNetworkReply): the reply object of the request.
        """
        image = self.load_image_from_reply(reply)

        if image.isNull():
            logger.warning("Unable to load image from the reply.")
            return

        self.finished.emit(image)

        reply.deleteLater()

    def load_image_from_reply(self, reply: QNetworkReply) -> QImage:
        """
        load_image_from_reply Method to load an image from the network reply.

        Args:
            reply (QNetworkReply): the reply from which the image is to be loaded.

        Returns:
            QImage: serialised QImage.
        """
        image = QImage()

        if reply.error() == QNetworkReply.NetworkError.ProtocolUnknownError:
            default_thumbnail_file = QFile(self.DEFAULT_THUMBNAIL_PATH)

            if default_thumbnail_file.open(QIODevice.OpenModeFlag.ReadOnly):
                content = default_thumbnail_file.readAll()
                default_thumbnail_file.close()
                image.loadFromData(content)

        elif reply.error() == QNetworkReply.NetworkError.NoError:
            image.loadFromData(reply.readAll())

        return image
