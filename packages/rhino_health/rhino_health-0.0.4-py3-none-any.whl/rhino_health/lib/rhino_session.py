from typing import Optional

from rhino_health.lib.constants import ApiEnvironment
from rhino_health.lib.rest_api.error_handler import ErrorHandler
from rhino_health.lib.rest_api.rhino_authenticator import RhinoAuthenticator
from rhino_health.lib.rest_handler import RequestDataType, RestHandler
from rhino_health.lib.rhino_client import RhinoClient, SDKVersion


class RhinoSession(RhinoClient):
    def __init__(
        self,
        username: str,
        password: str,
        rhino_api_url: str = ApiEnvironment.PROD_API_URL,
        sdk_version: str = SDKVersion.STABLE,
    ):
        super().__init__(rhino_api_url, sdk_version)
        self.authenticator = RhinoAuthenticator(self.api_url, username, password)
        self.login()
        self.rest_adapter = RestHandler(
            session=self,
            base_url=self.api_url,
            adapters={
                self.authenticator.__class__.__name__: self.authenticator,
                ErrorHandler.__class__.__name__: ErrorHandler(),
            },
        )

    def login(self):
        self.authenticator.authenticate()

    def switch_user(self, username, password):
        new_authenticator = RhinoAuthenticator(self.api_url, username, password)
        self.login()
        self.authenticator = new_authenticator
        self.rest_adapter.adapters[self.authenticator.__class__.__name__] = self.authenticator

    # These are just remappings for now until we need more complex stuff in future
    def get(self, url: str, params: Optional[dict] = None, adapter_kwargs: Optional[dict] = None):
        return self.rest_adapter.get(url=url, params=params, adapter_kwargs=adapter_kwargs)

    def post(
        self,
        url: str,
        data: RequestDataType,
        params: Optional[dict] = None,
        adapter_kwargs: dict = None,
    ):
        return self.rest_adapter.post(
            url=url, data=data, params=params, adapter_kwargs=adapter_kwargs
        )
