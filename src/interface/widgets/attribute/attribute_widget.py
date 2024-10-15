from PySide2.QtWidgets import QWidget

from ....data.datadef import Attribute
from ....logging import logger
from .attribute_view import AttributeView
from .Ui_attributes_list_widget import Ui_AttributeList


class AttributeList(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.ui = Ui_AttributeList()
        self.ui.setupUi(self)

        self.ui.addPushButton.clicked.connect(self.add_attribute)
        self.ui.removePushButton.clicked.connect(self.remove_attribute)

    def add_attribute(self):
        attribute = Attribute(
            key=self.ui.keyLineEdit.text(), value=self.ui.valueLineEdit.text()
        )
        attribute_view = AttributeView(self.ui.attributeListView, attribute)
        self.ui.attributeListView.add_attribute_view(attribute_view)
        self.ui.attributeListView.attributes.append(attribute)
        self.ui.keyLineEdit.clear()
        self.ui.valueLineEdit.clear()
        self.ui.keyLineEdit.setFocus()

    def remove_attribute(self):
        current_item = self.ui.attributeListView.currentItem()
        # logger.debug(f"{current_item=}")
        if current_item is None:
            return
        attribute_view = self.ui.attributeListView.itemWidget(current_item)
        # logger.debug(f"{attribute_view.attribute=}")
        self.ui.attributeListView.remove_attribute(attribute_view.attribute)
