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

from typing import Union

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QPushButton, QMessageBox

from .....data import Component, File, FileTypes
from .....logging import logger
from ...component import ComponentItem
from ...thumbnail import Thumbnail
from .Ui_detailed_widget import Ui_detailedWidget
from ..base_view import BaseView


class BaseDetailedView(BaseView):
    """
    Base class for the detailed view of a component
    """

    files_on_download = {}
    thumbnail: Thumbnail = None
    component: Component = None

    def __init__(self, parent: Union[QWidget, None] = None) -> None:
        """
        Constructor for the BaseDetailedView class.

        Args
        ----
        parent : QWidget | None, optional
            The parent widget. Defaults to None.

        Returns
        -------
        None

        Example
        -------
        view = BaseDetailedView(parent_widget)
        """
        super().__init__(parent)
        self.ui = Ui_detailedWidget()

    def setupUi(self) -> None:
        """
        Constructor for the BaseDetailedView class.

        Returns
        -------
        None
        """
        self.ui.setupUi(self)
        self.ui.backPushButton.clicked.connect(self.backPushButton_click)
        self.ui.tagsWidget.set_editable(False)
        self.addToDocumentButton = QPushButton("Add to Document", self)
        self.addToDocumentButton.setDisabled(True)
        self.addControlWidget(self.addToDocumentButton)

        self.addToDocumentButton.clicked.connect(self.addToDocumentButton_click)

    @Slot()
    def backPushButton_click(self) -> None:
        """
        Handle the click event of the back button.

        Returns
        -------
        None
        """

        self.topLevelWidget().toLastWidget()

    def addControlWidget(self, widget: QWidget) -> None:
        """
        Add a control widget to the control area in the detailed view.

        Args
        ----
        widget : QWidget
            The widget to be added.

        Returns
        -------
        None
        """

        self.ui.controlArea.addWidget(widget)

    def removeControlWidget(self, widget: QWidget) -> None:
        """
        Remove a control widget from the control area in the detailed view.

        Args
        ----
        widget : QWidget
            The widget to be removed.

        Returns
        -------
        None
        """

        self.ui.controlArea.removeWidget(widget)

    def addProgressWidget(self, widget: QWidget) -> None:
        """
        Add a progress widget to the processes area in the detailed view.

        Args
        ----
        widget : QWidget
            The widget to be added.

        Returns
        -------
        None
        """

        self.ui.processesArea.addWidget(widget)

    def current_file(self) -> Union[File, None]:
        """
        Get the current file selected in the filetypeComboBox.

        Returns
        -------
        File or None
            The current file selected, or None if no file is selected.
        """

        txt = self.ui.filetypeComboBox.currentText()
        # TODO : Check why txt produces empty string
        logger.debug(f"{txt=}")
        logger.debug(f"{FileTypes(txt)=}")
        logger.debug(f"{self.component.files=}")
        if txt and FileTypes(txt):
            return self.component.files.get(FileTypes(txt))
        # ! should not return None. Investigate

    def _update_component(self, component: Component) -> None:
        self.component = component

        # self._update_thumbnail(comp_item.ui.thumbnail)
        if self.thumbnail is not None:
            self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

        self.thumbnail = Thumbnail(self, component.metadata.thumbnail)
        self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)
        self._update_filetype_combobox()

        self.ui.componentLabel.setText(self.component.metadata.name)
        self.ui.descriptionLabel.setText(self.component.metadata.description)
        self.ui.authorValue.setText(self.component.metadata.author)
        self.ui.maintainerValue.setText(self.component.metadata.maintainer)
        self.ui.createdValue.setText(self.component.metadata.created_at)
        self.ui.updatedValue.setText(self.component.metadata.updated_at)
        self.ui.ratingWidget.setRating(self.component.metadata.rating)
        self.ui.licenceValue.setText(self.component.license.fullname)
        self.ui.AttributeListView.update_attributes(self.component.attributes)
        self.ui.tagsWidget.clear()
        for tag in self.component.tags:
            self.ui.tagsWidget.add_tag_to_bar(tag.label)

        if self.current_file().exists:
            self.addToDocumentButton.setDisabled(False)

    def updateContent(self, comp_item: ComponentItem) -> None:
        """
        Update the content of the detailed view with the information from the given ComponentItem.

        Args
        ----
        comp_item : ComponentItem
            The ComponentItem containing the component information.

        Returns
        -------
        None
        """

        self.component = comp_item.component

        self._update_thumbnail(comp_item.ui.thumbnail)
        self._update_filetype_combobox()

        self.ui.componentLabel.setText(self.component.metadata.name)
        self.ui.descriptionLabel.setText(self.component.metadata.description)
        self.ui.authorValue.setText(self.component.metadata.author)
        self.ui.maintainerValue.setText(self.component.metadata.maintainer)
        self.ui.createdValue.setText(self.component.metadata.created_at)
        self.ui.updatedValue.setText(self.component.metadata.updated_at)
        self.ui.ratingWidget.setRating(self.component.metadata.rating)
        self.ui.licenceValue.setText(self.component.license.fullname)
        self.ui.AttributeListView.update_attributes(self.component.attributes)
        self.ui.tagsWidget.clear()
        for tag in self.component.tags:
            self.ui.tagsWidget.add_tag_to_bar(tag.label)

        if self.current_file().exists:
            self.addToDocumentButton.setDisabled(False)

    @Slot()
    def addToDocumentButton_click(self):
        file = self.current_file()
        if file is None:
            return
        try:
            file_path = self.manager.insert_in_active_freecad_doc(
                self.component, file.type
            )
        except ValueError as e:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("No Active Document")
            dlg.setText(
                "No Active Document found. Do you want to create a new document and then insert into it?"
            )
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec_()

            if button == QMessageBox.Yes:
                file_path = self.manager.insert_in_new_freecad_doc(
                    self.component, file.type
                )
            else:
                return

        logger.debug(f"{file_path=}")

    def _update_thumbnail(self, thumbnail_widget) -> None:
        """
        Update the thumbnail widget in the detailed view.

        Args
        ----
        thumbnail_widget : QWidget
            The widget to be used as the new thumbnail.

        Returns
        -------
        None
        """

        if self.thumbnail is not None:
            self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

        self.thumbnail = Thumbnail.from_existing(self, thumbnail_widget)
        self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

    def _update_filetype_combobox(self) -> None:
        """
        Update the filetype combobox in the detailed view.

        Returns
        -------
        None
        """

        self.ui.filetypeComboBox.clear()
        for file in self.component.files:
            self.ui.filetypeComboBox.addItem(file.value)
        self.ui.filetypeComboBox.setCurrentIndex(0)
