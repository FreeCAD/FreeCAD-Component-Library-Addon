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

import contextlib

from PySide2.QtWidgets import QMainWindow, QWidget

from src.data.datadef import Component
from src.interface.widgets.component.item import ComponentItem

from ... import manager
from ...manager.api_manager.cms_api import CMSApi
from ...manager.api_manager.exceptions import Connection_Error
from ...logging import logger

from ..widgets import ComponentUploadWidget, UserWidget
from ..widgets.view_widget import LocalDetailedView, OnlineDetailedView
from ..widgets.view_widget.grid_view.view import GridView
from .Ui_window import Ui_MainWindow


class AddonWindow(QMainWindow):

    def __init__(self, parent=None) -> None:
        """
        Initialize the widget. This is the entry point for the class. You can override this if you want to do something other than setup the GUI and set up some things that are specific to the widget

        Args:
            parent: The parent of the widget
        """
        super().__init__(parent=parent)

        self.repo_manager = manager.OnlineRepoManager()
        self.local_manager = manager.LocalStorageManager()
        self.auth_manager = manager.Authentication_Manager()

        self.widgetStack = []

        self.show()

        self.ui = Ui_MainWindow()
        self.setupUi()
        self.setupSignals()
        self.setupManagers(self.repo_manager, self.local_manager)

        self.ui.stackedWidget.setCurrentWidget(self.onlineGridView)

        try:
            CMSApi().check_server_connection()
            self.upload_widget.populate_suggestions()
            self.onlineGridView.initial_load()
        except Connection_Error:
            logger.error(
                "API Connection failed. Please check your internet connection."
            )
            self.upload_widget.setDisabled(True)

        self.localGridView.initial_load()

        with contextlib.suppress(ValueError):
            self.auth_manager.persistent_login()

    def setupUi(self):
        """
        Setup the UI to work with the data. Called by __init__.
        """
        self.ui.setupUi(self)

        self.onlineGridView = GridView(self)
        self.onlineDetailView = OnlineDetailedView(self)
        self.localGridView = GridView(self)
        self.localDetailView = LocalDetailedView(self)
        self.upload_widget = ComponentUploadWidget(self, self.repo_manager)
        self.user_widget = UserWidget(self, self.auth_manager.user)

        self.ui.stackedWidget.insertWidget(0, self.onlineGridView)
        self.ui.stackedWidget.insertWidget(1, self.onlineDetailView)
        self.ui.stackedWidget.insertWidget(2, self.localGridView)
        self.ui.stackedWidget.insertWidget(3, self.localDetailView)
        self.ui.stackedWidget.insertWidget(4, self.upload_widget)
        self.ui.stackedWidget.insertWidget(5, self.user_widget)

        self.onlineGridView.detailView = self.onlineDetailView
        self.localGridView.detailView = self.localDetailView

    def setupSignals(self):
        """
        Setup the signals that need to be connected to the UI. Called by __init__.
        """
        self.ui.browseButton.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.onlineGridView)
        )
        self.ui.uploadButton.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.upload_widget)
        )
        self.ui.LocalButton.clicked.connect(self.display_local_components)
        self.ui.userPushButton.clicked.connect(self.show_user)

        self.auth_manager.session_update.connect(self.user_updated)

    def setupManagers(
        self,
        repo_manager: manager.OnlineRepoManager,
        local_manager: manager.LocalStorageManager,
    ):
        """
        Sets up the managers for the online and offline views.

        Parameters
        ----------
        repo_manager : OnlineRepoManager
            The manager for the online views.
        local_manager : LocalStorageManager
            The manager for the offline views.
        """
        self.onlineGridView.setupManager(repo_manager)
        self.onlineDetailView.setupManager(repo_manager)

        self.localGridView.setupManager(local_manager)
        self.localDetailView.setupManager(local_manager)

    def display_local_components(self):
        """
        Display locally installed components to the user.
        """
        self.local_manager.request_components()
        self.ui.stackedWidget.setCurrentWidget(self.localGridView)

    def toLastWidget(self):
        """
        Switch to the last widget in the stack. This is useful when you want to switch back to a grid view from any detailed view.
        """
        self.ui.stackedWidget.setCurrentWidget(self.widgetStack.pop())

    def uploadButton_clicked(self):
        """
        Create a component using the ComponentUploadDialog and OnlineRepoManager.
        """
        self.ui.stackedWidget.setCurrentWidget(self.upload_widget)

    def add_notification_widget(self, notification: QWidget):
        """
        Add a widget to the notification area. This is a convenience method for adding widgets to the notification area.
        This is mainly used for the download progress bar.

        Parameters
        ----------
        notification : QWidget
            The QWidget to add to the notification area
        """
        self.ui.notificationArea.addWidget(notification)

    def remove_notification_widget(self, notification: QWidget):
        """
        Remove a widget from the notification area. This is a convenience method for removing widgets from the notification area.
        This is mainly used for the download progress bar.

        Parameters
        ----------
        notification : QWidget
            The QWidget to remove from the notification area
        """
        logger.debug("Removing notification widget: {notification}")
        self.ui.notificationArea.removeWidget(notification)
        self.ui.notificationArea.update()

    def user_updated(self):
        if self.auth_manager.user is not None:
            self.ui.userPushButton.setText(self.auth_manager.user.username)
            self.user_widget.update_user(self.auth_manager.user)
        else:
            self.ui.userPushButton.setText("Login")

    def show_user(self):
        """
        Show the user widget to the user.
        """
        if self.auth_manager.user is not None:
            # if self.user_widget is None:
            #     self.user_widget = UserWidget(self, self.auth_manager.user)
            #     self.ui.stackedWidget.insertWidget(5, self.user_widget)

            self.ui.stackedWidget.setCurrentWidget(self.user_widget)
        else:
            self.auth_manager.login()
            if self.auth_manager.user is not None:
                self.user_updated()
                self.show_user()

    # def show_user_component(self, component: Component):
    #     """
    #     Show the detailed view of a component to the user.

    #     Parameters
    #     ----------
    #     component : Component
    #         The component to show the details of
    #     """
    #     component_item = ComponentItem(self.onlineDetailView, component)
    #     self.onlineDetailView.updateContent(component_item)
    #     self.widgetStack.append(self.onlineGridView)
    #     self.ui.stackedWidget.setCurrentWidget(self.onlineDetailView)
