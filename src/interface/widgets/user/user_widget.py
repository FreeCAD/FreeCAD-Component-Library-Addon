from typing import cast, Union
from PySide2.QtWidgets import (
    QWidget,
)
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt, QUrl, Signal, SignalInstance

from src.interface.widgets.component.item import ComponentItem

from ....data.datadef import User, Component
from .Ui_user_widget import Ui_UserWidget
from ....manager.download_manager import ImageLoader


class UserWidget(QWidget):
    # component_selected = cast(SignalInstance, Signal(Component))

    def __init__(self, parent: QWidget, user: Union[User, None]) -> None:
        super().__init__(parent)

        self.parent = parent
        self.user = user if user else User.empty_user()

        self.ui = Ui_UserWidget()
        self.ui.setupUi(self)
        self.ui.authPushButtom.setText("Logout")
        self.ui.authPushButtom.clicked.connect(self.logout)

        self.ui.usernameLabel.setText(self.user.username)
        self.ui.displayNameLabel.setText(self.user.name)
        self.ui.emailLabel.setText(self.user.email)
        self.ui.componentsLlistWidget.addItems(
            [comp.metadata.name for comp in self.user.components]
        )
        # emit a signal whne a component is selected
        self.ui.componentsLlistWidget.itemClicked.connect(self.show_user_component)
        #     lambda item: self.component_selected.emit(
        #         next(
        #             comp
        #             for comp in user.components
        #             if comp.metadata.name == item.text()
        #         )
        #     )
        # )

        self.image_loader = ImageLoader()
        self.image_loader.finished.connect(self.loadImage)
        self.image_loader.start_download(QUrl.fromUserInput(self.user.avatar_url))

    def loadImage(self, image: QImage):
        self.ui.profilePhotoLabel.setPixmap(
            QPixmap(image).scaled(
                self.ui.profilePhotoLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

    def logout(self):
        self.parent.auth_manager.logout()
        self.parent.display_grid_view()
        self.parent.user_updated()
        self.close()

    def update_user(self, user: User):
        self.user = user
        self.ui.usernameLabel.setText(user.username)
        self.ui.displayNameLabel.setText(user.name)
        self.ui.emailLabel.setText(user.email)
        self.ui.componentsLlistWidget.clear()
        self.ui.componentsLlistWidget.addItems(
            [comp.metadata.name for comp in user.components]
        )
        self.image_loader.start_download(QUrl.fromUserInput(self.user.avatar_url))
        # self.show()
        # self.parent.user_updated()
        # self.parent.display_user_view()

    def show_user_component(self, item):
        component = next(
            comp for comp in self.user.components if comp.metadata.name == item.text()
        )
        # component_item = ComponentItem(self.parent.onlineDetailView, component)
        self.parent.onlineDetailView._update_component(component)
        self.parent.widgetStack.append(self.parent.user_widget)
        self.parent.ui.stackedWidget.setCurrentWidget(self.parent.onlineDetailView)
