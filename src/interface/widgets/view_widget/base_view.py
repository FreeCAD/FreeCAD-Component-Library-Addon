from abc import abstractmethod
from typing import Any

from ....manager import ManagerInterface
from ....utils import ABCQWidget


class BaseView(ABCQWidget):
    @abstractmethod
    def setupUi(self): ...

    @abstractmethod
    def setupSignals(self): ...

    @abstractmethod
    def updateContent(self, content: Any): ...

    def setupManager(self, manager: ManagerInterface):
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
        self.manager: ManagerInterface = manager
