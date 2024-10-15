import json
from typing import cast
from urllib.parse import parse_qs, urlparse

import dotenv
from PySide2.QtCore import QUrl, Signal, SignalInstance
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QDialog, QVBoxLayout

from ...config import Config
from ...logging import logger

class Authentication_Dialog(QDialog):
    auth_complete = cast(SignalInstance, Signal(str))
    auth_scope: str = "repo"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitHub OAuth Login")
        self.setGeometry(100, 100, 800, 600)

        self.web_view = QWebEngineView()
        self.web_view.loadFinished.connect(self.handleLoadFinished)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        self.setLayout(layout)

        self.load_html = False

        self.start_github_oauth()

    def start_github_oauth(self):
        self.web_view.setUrl(
            QUrl(
                f"https://github.com/login/oauth/authorize?client_id={Config.GITHUB_OAUTH_CLIENT_ID}&scope={self.auth_scope}&prompt=consent"
            )
        )

    def handleLoadFinished(self, ok):
        curr_url = self.web_view.page().url()
        logger.debug(f"{curr_url=}")
        query = parse_qs(urlparse(curr_url.toString()).query)

        if ok and (curr_url.hasQuery()) and ("code" in query):
            self.web_view.page().runJavaScript(
                "document.documentElement.outerHTML", 0, self.handleHtml
            )

    def handleHtml(self, html: str):
        logger.debug(html)
        json_str = "{" + html.split("{", 1)[1].rsplit("}", 1)[0] + "}"
        logger.debug(json_str)

        response_data: dict = json.loads(json_str)

        Config.GITHUB_ACCESS_TOKEN = response_data.get("github_auth_token", "")
        dotenv.set_key(".env", "GITHUB_ACCESS_TOKEN", Config.GITHUB_ACCESS_TOKEN)

        Config.JWT_TOKEN = response_data.get("jwt", "")

        self.auth_complete.emit(Config.GITHUB_ACCESS_TOKEN)

        self.web_view.deleteLater()
        self.deleteLater()
