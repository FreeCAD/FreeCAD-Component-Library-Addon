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

from functools import partial
from typing import Sequence, cast, List

from PySide2.QtCore import Qt, Signal, SignalInstance
from PySide2.QtWidgets import (
    QCompleter,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)

from ....data import Tag


class TagBar(QWidget):
    """
    Custom QWidget class to manage tags using a tag bar.
    """

    tags_edited = cast(SignalInstance, Signal(list))

    def __init__(self, parent):
        """
        Constructor to initialize the TagBar.
        """
        super(TagBar, self).__init__()
        self.setParent(parent)

        self.setWindowTitle("Tag Bar")

        self.tags: List[str] = []

        self.h_layout = QHBoxLayout()
        self.h_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.h_layout)

        self.line_edit = QLineEdit()
        self.line_edit.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum,
        )

        self.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum,
        )

        self.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setContentsMargins(0, 0, 0, 0)

        self.refresh()
        self.setupUi()
        self.show()

    def setupUi(self):
        """
        Method to setup the UI elements.
        """
        self.line_edit.returnPressed.connect(self.create_tags)

    def create_tags(self):
        """
        Method to create tags from user input in the line edit.
        """
        new_tags = [tag for tag in self.line_edit.text().split(", ") if tag]

        self.line_edit.setText("")

        self.tags.extend(new_tags)
        self.tags = list(set(self.tags))
        self.tags.sort(key=lambda x: x.lower())

        self.refresh()

    def refresh(self):
        """
        Method to refresh the tag bar with the current tags.
        """
        for i in reversed(range(self.h_layout.count())):
            self.h_layout.itemAt(i).widget().setParent(None)

        for tag in self.tags:
            self.add_tag_to_bar(tag)

        self.h_layout.addWidget(self.line_edit)
        self.line_edit.setFocus()

    def add_tag_to_bar(self, text):
        """
        Method to add a tag to the tag bar.

        Parameters
        ----------
        text : str
            The tag text to be added.
        """
        tag = QFrame()
        tag.setStyleSheet("border:1px solid rgb(192, 192, 192); border-radius: 4px;")
        tag.setContentsMargins(0, 0, 0, 0)
        tag.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Minimum,
        )

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(10)

        tag.setLayout(hbox)

        label = QLabel(text)
        label.setStyleSheet("border:0px")
        label.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Minimum,
        )
        hbox.addWidget(label)

        x_button = QPushButton("x")
        x_button.setFixedSize(20, 20)
        x_button.setStyleSheet("border:0px; font-weight:bold")
        x_button.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Minimum,
        )
        x_button.clicked.connect(partial(self.delete_tag, text))
        hbox.addWidget(x_button)

        self.h_layout.addWidget(tag)
        self.tags_edited.emit(self.tags)

    def delete_tag(self, tag_name):
        """
        Method to delete a tag from the tag bar.

        Parameters
        ----------
        tag_name : str
            The name of the tag to be deleted.
        """
        self.tags.remove(tag_name)
        self.refresh()
        self.tags_edited.emit(self.tags)

    def set_suggestions(self, tag_list: Sequence[Tag]):
        """
        Method to set tag suggestions for the line edit.

        Parameters
        ----------
        tag_list : Sequence[Tag]
            The list of tag suggestions to set.
        """
        tagsCompleter = QCompleter([tag.label for tag in tag_list])
        tagsCompleter.activated.connect(self.create_tags)
        tagsCompleter.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.line_edit.setCompleter(tagsCompleter)

    def set_editable(self, editable: bool):
        self.line_edit.setVisible(editable)
        self.line_edit.setEnabled(editable)

    def clear(self):
        self.tags.clear()
        self.refresh()
