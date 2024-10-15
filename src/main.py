import logging
import os
from pathlib import Path
from dotenv import load_dotenv

from .utils import module_setup
from .config import Config


def independent_local_dev_app():
    load_dotenv(override=True)
    module_setup()

    from .logging import logger

    logger.setLevel(logging.DEBUG)

    Config.API_URL = "http://127.0.0.1:5000"
    Config.LOCAL_COMPONENT_PATH = Path("local_storage")
    Config.GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID", None)
    Config.GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    Config.JWT_TOKEN = None

    return __make_addon_window()


def freecad_local_dev_app():
    load_dotenv(override=True)

    import FreeCAD
    from .logging import logger

    logger.setLevel(logging.DEBUG)

    Config.API_URL = "http://127.0.0.1:5000"
    Config.LOCAL_COMPONENT_PATH = (
        Path(FreeCAD.ConfigGet("UserAppData")) / "ComponentLibrary"
    )
    Config.LOCAL_COMPONENT_PATH.mkdir(exist_ok=True)
    Config.GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID", None)
    Config.GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    Config.JWT_TOKEN = None

    return __make_addon_window()


def __make_addon_window():
    from .interface.main import AddonWindow

    return AddonWindow()
