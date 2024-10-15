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

from ..base_query import ComponentQueryInterface


class LocalComponentQuery(ComponentQueryInterface):
    ...


# Implementation of the ComponentQueryInterface for querying components locally.

# It will have similar properties and setters as the RepoComponentQuery class, but with different logic
# for querying components locally instead of from a remote repository.
