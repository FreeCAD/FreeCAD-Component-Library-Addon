# Copyright (c) 2023 Amulya Paritosh
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import FreeCAD
import FreeCADGui


class ComponentLibraryWorkbench(Workbench):
    def __init__(self):
        FreeCAD.Console.PrintLog("Logging Test here\n")
        FreeCAD.Console.PrintWarning("Warning Logging Test here\n")
        FreeCAD.Console.PrintError("Error Logging Test here\n")

        self.__class__.Icon = FreeCAD.getResourceDir() + ""
        self.__class__.MenuText = "ComponentLibrary"
        self.__class__.ToolTip = "ComponentLibrary workbench"

    def Initialize(self) -> None:
        from src import Window

        plugin = Window()

    def Activated(self):
        ...

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(ComponentLibraryWorkbench())
