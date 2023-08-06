from enum import Enum

import requests

from rhino_health.lib.rest_api.api_response import APIResponse
from rhino_health.lib.utils import url_for


class APIRequest:
    class RequestStatus(Enum):
        PENDING = "pending"
        SUCCESS = "success"
        FAILED = "failed"
        RETRY = "retry"

    def __init__(self, session, method, base_url, url, params, data):
        self.session = session
        self.method = method
        self.base_url = base_url
        self.url = url
        self.params = params or {}
        self.data = data
        self.headers = {}
        self.request_status = self.__class__.RequestStatus.PENDING
        self.request_count = 0

    def make_request(self) -> APIResponse:
        url = url_for(self.base_url, self.url)
        raw_response = requests.request(
            method=self.method, url=url, params=self.params, data=self.data, headers=self.headers
        )
        self.request_count += 1
        return APIResponse(self.session, raw_response)

    @property
    def pending(self):
        return self.request_status in [
            self.__class__.RequestStatus.PENDING,
            self.__class__.RequestStatus.RETRY,
        ]
