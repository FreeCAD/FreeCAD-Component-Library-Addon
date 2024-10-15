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

from typing import Any, Dict

from PySide2.QtCore import Slot
from PySide2.QtNetwork import QNetworkReply
from PySide2.QtWidgets import QDialog, QMessageBox, QPushButton, QWidget

from ....data import DTypes
from ....manager import OnlineRepoManager
from ....config import Config
from .Ui_component_form import Ui_ComponentCreationForm


class ComponentUploadWidget(QWidget):
    """
    Dialog for input fields of data for creating a Component.
    """

    def __init__(self, parent, manager: OnlineRepoManager) -> None:
        """
        Initialize the ComponentUploadDialog.

        Args
        ----
        parent : QWidget
            The parent widget.
        manager : OnlineRepoManager
            The manager for online repository operations.

        Returns
        -------
        None

        Example
        -------
        parent_widget = QWidget()
        manager = OnlineRepoManager()
        dialog = ComponentUploadDialog(parent_widget, manager)
        """
        super().__init__(parent)

        self.ui = Ui_ComponentCreationForm()
        self.manager = manager

        self.setupUi()

    def setupUi(self) -> None:
        """
        Set up the user interface of the dialog.

        Returns
        -------
        None
        """

        self.ui.setupUi(self)

        # Create "Create" and "Discard" buttons and connect their click events.
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.on_create_button_clicked)
        self.discard_button = QPushButton("Discard")
        self.discard_button.clicked.connect(self.close)

        # Add the buttons to the bottom widget layout.
        self.ui.bottomWidget.layout().addWidget(self.create_button)
        self.ui.bottomWidget.layout().addWidget(self.discard_button)

        self.ui.componentFiles.dir = str(Config.LOCAL_COMPONENT_PATH)
        self.ui.thumbnailFile.dir = str(Config.LOCAL_COMPONENT_PATH)

    def populate_suggestions(self):
        """
        Populate the suggestions for tags and licenses using the OnlineRepoManager.

        Returns
        -------
        None
        """
        self.ui.tagsWidget.set_suggestions(self.manager.load_from_db(DTypes.TAG))
        self.ui.licenseInput.addItems(
            (license.fullname for license in self.manager.load_from_db(DTypes.LICENSE))
        )

    @property
    def packed_data(self) -> Dict[str, Any]:
        """
        Pack the data entered in the form.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the packed data with the following keys:

        Example
        -------
        dialog = ComponentUploadDialog()
        data = dialog.pack_data()
        """
        return {
            "author": self.ui.authorInput.text(),
            "description": self.ui.descriptionInput.toPlainText(),
            "license_id": next(
                (
                    lis.id.replace("-", "")
                    for lis in self.manager.load_from_db(DTypes.LICENSE)
                    if lis.fullname == self.ui.licenseInput.currentText()
                )
            ),
            "maintainer": self.ui.maintainerInput.text(),
            "name": self.ui.componentNameInput.text(),
            "tags": self.ui.tagsWidget.tags,
            "version": "0",
            "repository": "test-repo",
            "branch": "main",
            "files": {
                "component_files": self.ui.componentFiles.filepaths,
                "thumbnail_image": self.ui.thumbnailFile.filepath,
            },
        }

    @Slot()
    def on_create_button_clicked(self) -> None:
        """
        Handle the "Create" button click event.
        Slot to handle the "Create" button click event.

        Returns
        -------
        None
        """

        # Pack the data and create the component using the OnlineRepoManager.
        self.cms_reply = self.manager.create_component(self.packed_data)
        self.cms_reply.finished.connect(self.handle_cms_reply)

    def handle_cms_reply(self) -> None:
        """
        Handle the CMS reply.
        Slot to handle the CMS reply.

        Args
        ----
        cms_reply : tuple
            The tuple containing the CMS reply.

        Returns
        -------
        None
        """

        if self.cms_reply.reply.error() == QNetworkReply.NetworkError.NoError:
            self.on_succesful_component_creation()
        else:
            self.on_exception_in_component_creation(self.cms_reply.reply)

    def on_exception_in_component_creation(self, reply: QNetworkReply) -> None:
        err_msg = QMessageBox(self)
        err_msg.setWindowTitle(str(reply.error()))
        # TODO: proper error message returned from the server is not visible
        err_msg.setText(str(reply.error()))
        err_msg.setIcon(QMessageBox.Icon.Critical)
        err_msg.exec_()

    def on_succesful_component_creation(self):
        success_msg = QMessageBox(self)
        success_msg.setWindowTitle("Success")
        success_msg.setText("Component created successfully!")
        success_msg.setIcon(QMessageBox.Icon.Information)
        success_msg.exec_()
        # self.close()

    @classmethod
    def create_component(cls, parent, manager: OnlineRepoManager) -> int:
        """
        Create and execute the ComponentUploadDialog.
        Class method to create and execute the ComponentUploadDialog.

        Args
        ----
        parent : QWidget
            The parent widget.
        manager : OnlineRepoManager
            The manager for online repository operations.

        Returns
        -------
        int
            The result of executing the dialog.

        Example
        -------
        parent_widget = QWidget()
        manager = OnlineRepoManager()
        result = ComponentUploadDialog.create_component(parent_widget, manager)
        """

        instance = cls(parent, manager)
        return instance.exec()
