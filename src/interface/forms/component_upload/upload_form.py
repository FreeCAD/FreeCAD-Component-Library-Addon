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

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QPushButton

from ....data import DTypes
from ....manager import OnlineRepoManager
from ..Ui_component_form import Ui_ComponentCreationForm


class ComponetUploadDialog(QDialog):
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

        # Set suggestions for tags and licenses using the OnlineRepoManager.
        self.ui.tagsWidget.set_suggestions(self.manager.load_from_db(DTypes.TAG))
        self.ui.licenseInput.addItems(
            (license.fullname for license in self.manager.load_from_db(DTypes.LICENSE))
        )

    def pack_data(self) -> dict[str, Any]:
        """
        Pack the data entered in the form.

        Returns
        -------
        dict[str, Any]
            A dictionary containing the packed data with the following keys:

        Example
        -------
        dialog = ComponentUploadDialog()
        data = dialog.pack_data()
        print(data)
        """
        return {
            "author": self.ui.authorInput.text(),
            "description": self.ui.descriptionInput.toPlainText(),
            "license_id": next(
                (
                    lis.id
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
        self.manager.create_component(self.pack_data())

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
        print(result)
        """

        instance = cls(parent, manager)
        return instance.exec()
