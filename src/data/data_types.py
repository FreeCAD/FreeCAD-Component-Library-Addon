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

from enum import Enum


class DTypes(Enum):
    """
    An Enum representing different data types.
    """

    COMPONENT = "component"
    FILE = "file"
    LICENSE = "license"
    METADATA = "metadata"
    TAG = "tag"
    ATTRIBUTE = "attribute"


class FileTypes(Enum):
    """
    An Enum representing different file types.
    """

    STL = "stl"
    FCSTD = "fcstd"
    FCSTD1 = "fcstd1"
    STEP = "step"
    STP = "stp"
