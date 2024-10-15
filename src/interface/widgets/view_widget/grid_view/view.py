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

from functools import wraps
from typing import Callable, List

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget

from .....data import DTypes
from .....manager import ManagerInterface, OnlineRepoManager
from .....manager.page_manager import PageStates
from ...overlay import LoadingOverlay
from ..base_view import BaseView
from ..detail_view.base_detail_view import BaseDetailedView
from .Ui_grid_view import Ui_gridView


class GridView(BaseView):
    """
    This is the GridView for browsing the components.
    """

    manager: OnlineRepoManager

    def __init__(self, parent: QWidget) -> None:
        """
        Constructor for the GridView class

        Parameters
        ----------
        parent : QWidget
            Parent of GridView object
        """
        super().__init__(parent)

        self.ui = Ui_gridView()
        self.detailView: BaseDetailedView = None

        self.setupUi()
        self.setupSignals()

    def setupUi(self) -> None:
        """
        Setup all the ui elements.
        Called in __init__
        """
        self.ui.setupUi(self)

        self.loading_overlay = LoadingOverlay(self.ui.scrollArea)
        self.ui.fileTypeComboBox.make_pre_checked()  # initialy all the filetypes are filtred on searches

    def setupSignals(self) -> None:
        """
        Setup all the signal connections.
        Called in __init__
        """
        self.ui.searchLineEdit.returnPressed.connect(self.search_enter_pressed)
        self.ui.nextButton.clicked.connect(self.nextButtonclicked)
        self.ui.prevButton.clicked.connect(self.prevButtonclicked)
        self.ui.sortComboBox.currentTextChanged.connect(self.sortComboBox_change)
        self.ui.orderComboBox.currentTextChanged.connect(self.ordCombBox_change)
        self.ui.fileTypeComboBox.selectionUpdated.connect(self.fileTypeComboBox_change)
        self.ui.tagBar.tags_edited.connect(self.tagBar_tag_edited)

    def setupManager(self, manager: ManagerInterface) -> None:
        """
        Sets up the manager for the OnlineDetailedView.

        Parameters
        ----------
        manager : ManagerInterface
            An instance of the manager interface.

        Returns
        -------
        None
        """
        super().setupManager(manager)

        self.manager.component_loaded.connect(self.components_response_handler)
        self.manager.page_states.enable_next.connect(self.ui.nextButton.setEnabled)
        self.manager.page_states.enable_prev.connect(self.ui.prevButton.setEnabled)

    def updateContent(self, page: PageStates) -> None:
        """
        Updates the content of the view with the given page data.

        Parameters
        ----------
        page : PageStates
            The page data to update the view with.

        Returns
        -------
        None
        """

        self.ui.scrollAreaContentItemsWidget.repopulate(page.data)
        self.ui.pageLable.setText(f"{page.page_no} / {page.total_pages}")
        self.loading_overlay.loading = False

    def loading(func: Callable):
        """
        Decorator that sets the loading overlay to True before executing the decorated function.

        Parameters
        ----------
        func : Callable
            The function to be decorated.

        Returns
        -------
        Callable
            The decorated function.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            self, *args = args
            self.loading_overlay.loading = True
            self.ui.scrollArea.verticalScrollBar().setValue(
                0
            )  # reset the vertical scrollbar position
            return func(self, *args, **kwargs)

        return wrapper

    @Slot()
    def components_response_handler(self) -> None:
        """
        Slot function that handles the response from the components.

        Parameters
        ----------
        self : View
            The View instance.

        Returns
        -------
        None
        """
        self.updateContent(self.manager.page_states)

    @loading
    def initial_load(self) -> None:
        """
        Load the data for the first time with the base search
        """
        self.manager.reload_page()
        self.ui.tagBar.set_suggestions(self.manager.load_from_db(DTypes.TAG))

    @loading
    @Slot()
    def nextButtonclicked(self) -> None:
        """
        Request loading the next page of data
        """
        self.manager.next_page()

    @loading
    @Slot()
    def prevButtonclicked(self) -> None:
        """
        Request loading the previous page of data
        """
        self.manager.prev_page()

    @loading
    @Slot()
    def search_enter_pressed(self) -> None:
        """
        Perform search with the entered text from searchLineEdit
        """
        self.manager.search(self.ui.searchLineEdit.text())

    @loading
    @Slot(str)
    def sortComboBox_change(self, value: str) -> None:
        """
        Perform sorting based on the selected value and the orderComboBox's current text
        """
        self.manager.sort(
            by=value,
            order=self.ui.orderComboBox.currentText(),
        )

    @loading
    @Slot(str)
    def ordCombBox_change(self, value: str) -> None:
        """
        Perform sorting based on the sortComboBox's current text and the selected value
        """
        self.manager.sort(
            by=self.ui.sortComboBox.currentText(),
            order=value,
        )

    @loading
    @Slot(list)
    def fileTypeComboBox_change(self, checked_items: List[str]) -> None:
        """
        Perform filtering based on checked filetypes and tags from tagBar
        """
        self.manager.filter(
            filetypes=checked_items,
            tags=self.ui.tagBar.tags,
        )

    @loading
    @Slot()
    def tagBar_tag_edited(self, tags: List[str]) -> None:
        """
        Update the manager's query tags and perform filtering based on filetypes and tags
        """
        self.manager.query.tags = tags
        self.manager.filter(
            filetypes=self.ui.fileTypeComboBox.checked_items(),
            tags=tags,
        )
