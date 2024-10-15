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

from pathlib import Path
from typing import Optional


class Config:
    """
    Class to store all the configurations.
    """

    API_URL: str
    LOCAL_COMPONENT_PATH: Path

    GITHUB_OAUTH_CLIENT_ID: Optional[str]
    GITHUB_ACCESS_TOKEN: Optional[str]
    JWT_TOKEN: Optional[str]
