# Copyright (c) 2023 Amulya Paritosh
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import FreeCAD
import FreeCADGui


class ComponentLibraryWorkbench(Workbench):

    def __init__(self):
        self.__class__.MenuText = "ComponentLibrary"
        self.__class__.ToolTip = "ComponentLibrary workbench"

    def Initialize(self) -> None:
        from src.main import freecad_local_dev_app

        self.addon = freecad_local_dev_app()
        self.addon.show()

    def Activated(self):
        self.addon.show()

    def Deactivated(self):
        self.addon.hide()

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(ComponentLibraryWorkbench())
