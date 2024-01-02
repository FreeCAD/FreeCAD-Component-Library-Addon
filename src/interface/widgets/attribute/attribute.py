from typing import Iterable

from PySide6.QtWidgets import QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QWidget

from ....data.datadef import Attribute


class Attribute(QWidget):
    def __init__(self, parent: QWidget, attribute: Attribute) -> None:
        super().__init__(parent)
        self.key = QLabel(attribute.key)
        self.value = QLabel(attribute.value)
        layout = QHBoxLayout()
        layout.addWidget(self.key)
        layout.addWidget(self.value)
        self.setLayout(layout)


class AttributeList(QListWidget):
    def _add_attribute(self, attribute: Attribute):
        attr = Attribute(self, attribute)
        itemN = QListWidgetItem()
        itemN.setSizeHint(attr.sizeHint())

        self.addItem(itemN)
        self.setItemWidget(itemN, attr)

    def update_attributes(self, attributes: Iterable[Attribute]):
        self.clear()
        for attr in attributes:
            self._add_attribute(attr)
