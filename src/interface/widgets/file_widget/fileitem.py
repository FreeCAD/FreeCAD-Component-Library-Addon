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
from typing import List

from PySide2.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class FileItem(QFrame):
    """
    Custom QFrame class to represent an item for a file in the list.
    """

    def __init__(self, parent=None, dir="") -> None:
        """
        Constructor to initialize the FileItem.
        """
        super().__init__(parent)
        self.filepath = ""
        self.dir = dir

        layout = QHBoxLayout()
        self.choose_file_btn = QPushButton("Choose File")
        self.choose_file_btn.clicked.connect(self.open_file_dialog)

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        layout.addWidget(self.choose_file_btn)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def open_file_dialog(self):
        """
        Method to open a file dialog and set the filepath.
        """
        self.filepath, _ = QFileDialog.getOpenFileName(
            self,
            "Select Files",
            dir=self.dir,
        )
        if self.filepath:
            self.label.setText(Path(self.filepath).name)


class FileList(QWidget):
    """
    Custom QWidget class to represent a list of files.
    """

    def __init__(self, parent=None) -> None:
        """
        Constructor to initialize the FileList.
        """
        super().__init__(parent)
        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.add_file_btn = QPushButton("Add File")
        self.add_file_btn.clicked.connect(self.add_file)

        self.dir = ""

        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_file_btn)
        self.setLayout(layout)

    def add_file(self):
        """
        Method to add a new file to the list.
        """
        file_widget = FileItem(dir=self.dir)

        cb = QPushButton("X")
        cb.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        file_widget.layout().addWidget(cb)
        itemN = QListWidgetItem()
        itemN.setSizeHint(file_widget.sizeHint())

        file_widget.choose_file_btn.click()

        cb.clicked.connect(lambda: self.remove_item(itemN))

        self.list_widget.addItem(itemN)
        self.list_widget.setItemWidget(itemN, file_widget)

    def remove_item(self, item: QListWidgetItem):
        """
        Method to remove a file from the list.
        """
        self.list_widget.takeItem(self.list_widget.row(item))

    @property
    def filepaths(self) -> List[str]:
        """
        Property to get the list of filepaths currently in the list.
        """
        return [
            self.list_widget.itemWidget(self.list_widget.item(i)).filepath
            for i in range(self.list_widget.count())
        ]
