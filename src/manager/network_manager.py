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

from functools import lru_cache
from typing import List, Tuple

import certifi
from PySide2.QtCore import Slot
from PySide2.QtNetwork import (
    QNetworkAccessManager,
    QNetworkReply,
    QNetworkRequest,
    QSsl,
    QSslCertificate,
    QSslConfiguration,
    QSslSocket,
)
from PySide2.QtWidgets import QMessageBox

from ..logging import logger


@Slot(QNetworkReply)
def when_finished(reply: QNetworkReply) -> None:
    """
    Executes the when_finished function for a QNetworkReply object finished signal is emitted.
    This function handles different network error scenarios and prints relevant information based on the error code.

    Parameters
    ----------
    reply : QNetworkReply
        The QNetworkReply object representing the network request.
    """

    er: QNetworkReply.NetworkError = reply.error()

    if er == QNetworkReply.NetworkError.NoError:
        pass
    # logger.debug(f"{reply.url()} : {reply.readAll().data().decode()}")

    elif er == QNetworkReply.NetworkError.ProtocolUnknownError:
        logger.debug("Blank URL passed!")

    elif er == QNetworkReply.NetworkError.ConnectionRefusedError:
        msg = QMessageBox()
        msg.setWindowTitle("ConnectionRefusedError")
        msg.setText(
            f"Connection to {reply.url().toString()} was refused!\nSee if the server is running."
        )
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec_()

    else:
        # If there is any other network error, print the error code and error string along with the URL
        logger.warning(f"{reply.url()} : {reply.errorString()}")


#
@lru_cache
def get_network_access_manager() -> Tuple[QNetworkAccessManager, QSslConfiguration]:
    """
    Retrieves the network access manager and SSL configuration for making network requests.
    Function result is cached for subsequent calls with the same arguments for ensuring Singleton

    Returns
    -------
    tuple[QNetworkAccessManager, QSslConfiguration]
        A tuple containing the network access manager and SSL configuration.
    """
    qcerts: List[QSslCertificate] = QSslCertificate.fromPath(
        certifi.where(),
        QSsl.EncodingFormat.Pem,
        QSslCertificate.PatternSyntax.Wildcard,
    )

    sslConfig: QSslConfiguration = QSslConfiguration.defaultConfiguration()
    sslConfig.setProtocol(QSsl.SslProtocol.TlsV1_0)
    sslConfig.setPeerVerifyDepth(1)
    sslConfig.setPeerVerifyMode(QSslSocket.PeerVerifyMode.VerifyPeer)
    sslConfig.setCaCertificates(qcerts)

    network_access_manager = QNetworkAccessManager()
    network_access_manager.finished.connect(when_finished)

    return network_access_manager, sslConfig
