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

import sys
from abc import ABC, ABCMeta
from typing import Type

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QWidget

QObjectMeta = type(QObject)
QWidgetMeta = type(QWidget)


class _ABCQObjectMeta(QObjectMeta, ABCMeta):
    ...


class _ABCQWidgetMeta(QObjectMeta, ABCMeta):
    ...


class ABCQObject(QObject, ABC, metaclass=_ABCQObjectMeta):
    ...


class ABCQWidget(QWidget, ABC, metaclass=_ABCQWidgetMeta):
    ...


def singleton(cls: Type):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def module_setup():
    add_freecad_to_path()

    try:
        import FreeCAD
        import PySide2
    except ImportError:
        try:
            import PySide6 as PySide2
        except ImportError:
            import PySide2 as PySide2

    sys.modules["PySide2"] = PySide2


# def setup_config(new_config):
#     from . import config

#     config.config = new_config


def add_freecad_to_path():
    from pathlib import Path
    import sys
    import platform
    import subprocess
    import shutil

    FREECAD_COMMANDS = ("FreeCADCmd", "freecadcmd")

    fc_command = next(
        (command for command in FREECAD_COMMANDS if shutil.which(command)), None
    )

    if not fc_command:
        print(
            f"Neither of the following commands are available: {', '.join(FREECAD_COMMANDS)}"
        )
        sys.exit(1)

    fc_home_path = subprocess.getoutput(
        f"{fc_command} --get-config AppHomePath"
    ).splitlines()[-1]

    os_name = platform.system()
    fc_path = Path(fc_home_path)

    if os_name == "Windows":
        fc_path = fc_path / "bin"
    elif os_name == "Darwin":
        fc_path = fc_path / "lib"
    elif os_name == "Linux":
        fc_path = fc_path / "lib"
    else:
        print("Unsupported OS")
        sys.exit(1)

    sys.path.append(str(fc_path))
