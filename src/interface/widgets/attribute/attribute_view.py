from typing import Iterable, List

from PySide2.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QSizePolicy,
    QWidget,
)

from ....data.datadef import Attribute


class AttributeView(QWidget):
    def __init__(self, parent: QWidget, attribute: Attribute) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.attribute = attribute

        self.key = QLabel(attribute.key)
        self.key.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.value = QLabel(attribute.value)
        self.value.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum
        )

        layout = QHBoxLayout()
        layout.addWidget(self.key)
        layout.addWidget(self.value)
        self.setLayout(layout)


class AttributeListView(QListWidget):

    attributes: List[Attribute] = []

    def add_attribute_view(self, attribute_view: AttributeView):
        itemN = QListWidgetItem()
        # itemN.setSizeHint(attribute_view.sizeHint())

        self.addItem(itemN)
        self.setItemWidget(itemN, attribute_view)

    def __add_attribute(self, attribute: Attribute):
        attr = AttributeView(self, attribute)
        self.add_attribute_view(attr)
        self.attributes.append(attribute)

    def append_attribute(self, attribute: Attribute):
        attr = AttributeView(self, attribute)
        self.add_attribute_view(attr)
        self.attributes.append(attribute)

    def update_attributes(self, attributes: Iterable[Attribute]):
        self.clear()
        self.attributes = attributes
        for attr in attributes:
            self.__add_attribute(attr)

    def remove_attribute(self, attribute: Attribute):
        self.attributes.remove(attribute)
        self.update_attributes(self.attributes)
