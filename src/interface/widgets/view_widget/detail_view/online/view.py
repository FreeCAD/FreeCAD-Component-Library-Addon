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

from enum import Enum, auto
from pathlib import Path


from PySide2.QtCore import Slot
from PySide2.QtWidgets import QProgressBar, QWidget

from ......manager import ManagerInterface, OnlineRepoManager
from ......logging import logger
from ....component import ComponentItem
from ....state_push_button import StatefulPushButton
from ..base_detail_view import BaseDetailedView


class DownloadStates(Enum):
    """
    Represents the different states of a download.

    Attributes:
        AVAILABLE: The download is available.
        IN_PROGRESS: The download is in progress.
        FINISHED: The download has finished.
    """

    AVAILABLE = auto()
    IN_PROGRESS = auto()
    FINISHED = auto()


class OnlineDetailedView(BaseDetailedView):
    """
    Detailed view Widget of an online component.
    """

    manager: OnlineRepoManager

    def __init__(self, parent: QWidget) -> None:
        """
        Initialises the OnlineDetailedView.

        Parameters
        ----------
        parent : QWidget
            parent widget of OnlineDetailedView.
        """
        super().__init__(parent)

        self.setupUi()
        self.setupSignals()

    def setupUi(self) -> None:
        """
        Setup all the ui elements.
        Called in __init__
        """
        super().setupUi()

        self.downloadPushButton = StatefulPushButton(self)
        self.addControlWidget(self.downloadPushButton)

    def setupSignals(self) -> None:
        """
        Setup all the signal connections.
        Called in __init__
        """
        self.downloadPushButton.register_state(
            DownloadStates.AVAILABLE, self.downloadButton_click, "Download", True
        )
        self.downloadPushButton.register_state(
            DownloadStates.IN_PROGRESS, None, "Downloading...", False
        )
        self.downloadPushButton.register_state(
            DownloadStates.FINISHED, self.removeButton_click, "Remove", True
        )

        self.ui.filetypeComboBox.currentTextChanged.connect(
            self.update_download_button_state
        )

    def setupManager(self, manager: ManagerInterface) -> None:
        """
        Sets up the manager for the OnlineDetailedView.

        Parameters
        ----------
        manager : ManagerInterface
            An instance of the manager interface.

        Returns
        -------
        None
        """
        super().setupManager(manager)

    def updateContent(self, comp_item: ComponentItem) -> None:
        """
        Updates the component data with the new component item.

        Parameters
        ----------
        comp_item : ComponentItem
            component to display.
        """
        super().updateContent(comp_item)
        self.update_download_button_state()

    @Slot()
    def downloadButton_click(self) -> None:
        """
        Slot for download button click.
        Starts the file download and add a progressbar for it.
        """
        file = self.current_file()
        if file is None:
            return

        # Add a progress bar for the file being downloaded
        self.files_on_download[file.id] = QProgressBar()
        self.topLevelWidget().add_notification_widget(self.files_on_download[file.id])
        self.downloadPushButton.setState(DownloadStates.IN_PROGRESS)

        # Start the component download process
        downloader = self.manager.download_component(
            self.component,
            file.type,
        )
        downloader.downloadProgress.connect(self.__update_download_progress)
        downloader.finished.connect(self.component_downloaded)
        logger.debug("Download started...")

    @Slot(int, int)
    def __update_download_progress(
        self, bytes_received: bytes, total_bytes: bytes
    ) -> None:
        """
        Slot method to update the download progress

        Parameters
        ----------
        bytes_received : bytes
            bytes downloaded
        total_bytes : bytes
            total bytes to download
        """
        file = self.current_file()
        if file is None:
            return

        # Update the progress bar's maximum and current values based on the download progress
        self.files_on_download[file.id].setMaximum(total_bytes)
        self.files_on_download[file.id].setValue(bytes_received)

    @Slot(Path)
    def component_downloaded(self, filepath: Path) -> None:
        """
        Slot method to handle component download completion.
        Removes the file from files_on_download dictionary and updates the file state.

        Parameters
        ----------
        filepath : Path
            Path of file that got downloaded

        Returns
        -------
        None
        """
        file = self.current_file()
        if file is None:
            return

        self.downloadPushButton.setState(DownloadStates.FINISHED)
        file.exists = True  # Mark the file as existing (downloaded successfully)
        self.topLevelWidget().remove_notification_widget(
            self.files_on_download[file.id]
        )
        self.files_on_download.pop(
            file.id
        )  # Remove the file id and progress bar from the files_on_download dictionary

        logger.debug("Download Successful!")
        logger.debug("file at: {filepath}")

    def is_file_on_download(self) -> bool:
        """
        Check if a file is currently being downloaded

        Returns
        -------
        bool
            Return True if the file is currently being downloaded (exists in files_on_download)
        """
        file = self.current_file()
        return (file is not None) and (file.id in self.files_on_download)

    @Slot(str)
    def update_download_button_state(self) -> None:
        """
        Updates the download button state based on the selected file type.
        File will be made available for downloaded if it is not present in the Local storage.
        File will be made removeable if it is present in Local storage.

        Returns
        -------
        None
        """
        if self.is_file_on_download():
            self.downloadPushButton.setState(DownloadStates.IN_PROGRESS)

        elif self.current_file().exists:
            # ! This produces an error when current_file() returns None
            self.downloadPushButton.setState(DownloadStates.FINISHED)
        else:
            self.downloadPushButton.setState(DownloadStates.AVAILABLE)

    @Slot()
    def removeButton_click(self) -> None:
        """
        Slot for remove button. Removes file from Local storage.

        Returns
        -------
        None
        """
        self.manager.remove_file(self.component, self.current_file().type)
        self.downloadPushButton.setState(DownloadStates.AVAILABLE)
        # ! SOME errors are occuring
