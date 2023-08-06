"""Rhino Health Python SDK."""

__version__ = "0.0.4"

import rhino_health.lib.metrics
from rhino_health.lib.constants import ApiEnvironment
from rhino_health.lib.rhino_client import SDKVersion
from rhino_health.lib.rhino_session import RhinoSession


def login(
    username, password, rhino_api_url=ApiEnvironment.PROD_API_URL, sdk_version=SDKVersion.PREVIEW
):
    """
    :param username: string username
    :param password: string password
    :param rhino_api_url: Optional, default PROD_API_URL.
    from rhino_health import LOCALHOST_API_URL, PROD_API_URL, PROD_API_URL
    :param sdk_version Which version of the SDK you are running
    :return:
    """
    return RhinoSession(username, password, rhino_api_url, sdk_version)
