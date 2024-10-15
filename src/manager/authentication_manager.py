import json
from typing import Any, Dict, List, Optional, cast

import dotenv
from PySide2.QtCore import QObject, Signal, SignalInstance
from PySide2.QtNetwork import QNetworkRequest

from src.data.data_types import DTypes
from src.data.factory import DataFactory
from src.manager.api_manager.cms_api.api import CMSApi


from ..config import Config
from ..data import User
from ..logging import logger
from ..interface.dialogs.authentication import Authentication_Dialog
from .network_manager import get_network_access_manager


class Authentication_Manager(QObject):
    user: Optional[User] = None
    session_update = cast(SignalInstance, Signal())

    network_manager, sslConfig = get_network_access_manager()

    def __init__(self) -> None:
        super().__init__()

    def persistent_login(self):
        if not Config.GITHUB_ACCESS_TOKEN:
            logger.warning(
                "Persistent login failed. No access token found in the environment."
            )
            return

        request: QNetworkRequest = QNetworkRequest(f"{Config.API_URL}/api/auth/github")
        request.setRawHeader(
            "X-Access-Token".encode("utf-8"),
            str(Config.GITHUB_ACCESS_TOKEN).encode("utf-8"),
        )
        self.jwt_auth_reply = self.network_manager.get(request)
        self.jwt_auth_reply.finished.connect(self.handle_jwt_auth_response)

    def handle_jwt_auth_response(self):
        raw_json_str = self.jwt_auth_reply.readAll().data().decode("utf-8")
        logger.debug(f"{raw_json_str=}")
        if not raw_json_str:
            jwt_token = None
        else:
            jwt_token = json.loads(raw_json_str)["jwt"]
        Config.JWT_TOKEN = jwt_token

        logger.debug(f"{jwt_token=}")
        self.get_user_data(Config.GITHUB_ACCESS_TOKEN)

    def login(self) -> None:
        dialog = Authentication_Dialog()
        dialog.auth_complete.connect(self.get_user_data)
        dialog.exec()

    def logout(self) -> None:
        self.user = None
        Config.GITHUB_ACCESS_TOKEN = None
        dotenv.set_key(".env", "GITHUB_ACCESS_TOKEN", "")
        self.session_update.emit()

    def is_authentic(self) -> bool:
        return self.user is not None

    def get_user_data(self, access_token: str):
        if not access_token:
            raise ValueError("The request token has to be supplied!")

        user_data_request = QNetworkRequest("https://api.github.com/user")
        user_data_request.setRawHeader(
            b"Authorization", f"token {access_token}".encode()
        )
        self.user_data_reply = self.network_manager.get(user_data_request)
        self.user_data_reply.finished.connect(self.handle_user_data_response)

    def handle_user_data_response(self):
        raw_json_str = self.user_data_reply.readAll().data().decode("utf-8")
        user_data = json.loads(raw_json_str)

        logger.debug(f"users: {user_data}")
        if user_data is None or "login" not in user_data:
            logger.info(f"user authentication failed: Bad Credentials")
            return

        self.user = User(
            username=user_data["login"],
            name=user_data["name"],
            email=user_data["email"],
            avatar_url=user_data["avatar_url"],
            components=[],
        )
        self.session_update.emit()

        logger.debug(f"{self.user=}")
        self.get_user_components()

    def get_user_components(self):
        request = QNetworkRequest("component/user")

        user_component_reply = CMSApi().read(request)
        user_component_reply.finished.connect(self.get_user_components_callback)

    def get_user_components_callback(self, json_data: Dict[str, Any]):
        components = DataFactory.load_many(list(json_data.values()), DTypes.COMPONENT)
        self.user.components = components
        self.session_update.emit()
