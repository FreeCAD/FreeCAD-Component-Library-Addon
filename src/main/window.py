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

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QWidget

from ..interface.forms import ComponetUploadDialog
from ..interface.views import GridView, LocalDetailedView, OnlineDetailedView
from ..interface.widgets import ComponentItem
from ..manager import LocalStorageManager, OnlineRepoManager
from .Ui_window import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self, parent=None) -> None:
        """
        Initialize the widget. This is the entry point for the class. You can override this if you want to do something other than setup the GUI and set up some things that are specific to the widget

        Args:
            parent: The parent of the widget
        """
        super().__init__(parent=parent)

        self.repo_manager = OnlineRepoManager()
        self.local_manager = LocalStorageManager()
        self.widgetStack = []

        self.show()

        self.ui = Ui_MainWindow()
        self.setupUi()
        self.setupSignals()
        self.setupManagers(self.repo_manager, self.local_manager)
        self.display_grid_view()

    def setupUi(self):
        """
        Setup the UI to work with the data. Called by __init__.
        """
        self.ui.setupUi(self)

        self.onlineGridView = GridView(self)
        self.onlineDetailView = OnlineDetailedView(self)
        self.localGridView = GridView(self)
        self.localDetailView = LocalDetailedView(self)

        self.ui.stackedWidget.insertWidget(0, self.onlineGridView)
        self.ui.stackedWidget.insertWidget(1, self.onlineDetailView)
        self.ui.stackedWidget.insertWidget(2, self.localGridView)
        self.ui.stackedWidget.insertWidget(3, self.localDetailView)

        self.onlineGridView.detailView = self.onlineDetailView
        self.localGridView.detailView = self.localDetailView

    def setupSignals(self):
        """
        Setup the signals that need to be connected to the UI. Called by __init__.
        """
        self.ui.browseButton.clicked.connect(self.display_grid_view)
        self.ui.uploadButton.clicked.connect(self.uploadButton_clicked)
        self.ui.LocalButton.clicked.connect(self.display_local_components)

    def setupManagers(
        self, repo_manager: OnlineRepoManager, local_manager: LocalStorageManager
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

    def display_detail_view(self, item: ComponentItem, grid_view: GridView):
        """
        Display the detail view.

        Parameters
        ----------
        item : ComponentItem
            The ComponentItem that has to be displayed
        grid_view : GridView
            The GridView that contains the component
        """
        grid_view.detailView.updateContent(item)
        self.ui.stackedWidget.setCurrentWidget(grid_view.detailView)

    def display_local_components(self):
        """
        Display locally installed components to the user.
        """
        self.local_manager.request_components()
        self.ui.stackedWidget.setCurrentWidget(self.localGridView)

    @Slot()
    def display_grid_view(self):
        """
        Display the grid view in the stacked widget. This is called when the user clicks on the back button from any detailed view.
        """
        self.ui.stackedWidget.setCurrentWidget(self.onlineGridView)

    @Slot()
    def toLastWidget(self):
        """
        Switch to the last widget in the stack. This is useful when you want to switch back to a grid view from any detailed view.
        """
        self.ui.stackedWidget.setCurrentWidget(self.widgetStack.pop())

    @Slot()
    def uploadButton_clicked(self):
        """
        Create a component using the ComponetUploadDialog and OnlineRepoManager.
        """
        data = ComponetUploadDialog.create_component(self, self.repo_manager)
        print(data)

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
