import json
from typing import List, Type, TypeVar


class APIResponse:
    def __init__(self, session, request_response):
        self.session = session
        self.raw_response = request_response
        self.status_code = request_response.status_code

    DataClass = TypeVar("DataClass")

    def _accepted_fields_for(self, dataclass):
        accepted_fields = list(dataclass.__fields__.keys())
        uid_remap = {field[:-4]: field for field in accepted_fields if field.endswith("_uid")}
        accepted_fields.extend(uid_remap.keys())
        return accepted_fields, uid_remap

    def _to_dataclass(self, dataclass, data):
        return dataclass(session=self.session, _persisted=True, **data)

    def to_dataclass(self, dataclass: Type[DataClass]) -> DataClass:
        try:
            json_response = self.raw_response.json()
            if not isinstance(json_response, dict):
                raise RuntimeError(
                    f"Response format does not match expected format for {dataclass.__name__}"
                )
            return self._to_dataclass(dataclass, json_response)
        except Exception as e:
            self.parse_and_raise_exception(e)

    def to_dataclasses(self, dataclass: Type[DataClass]) -> List[DataClass]:
        try:
            json_response = self.raw_response.json()
            if not isinstance(json_response, list):
                raise RuntimeError(
                    f"Response format does not match expected format for {dataclass.__name__}"
                )
            return [self._to_dataclass(dataclass, data) for data in json_response]
        except Exception as e:
            self.parse_and_raise_exception(e)

    def parse_and_raise_exception(self, e):
        # TODO: Update after fix license
        message = ""
        try:
            response_data = json.loads(self.raw_response.content)["data"]
            r2 = response_data.replace(
                "Error getting cohort metrics: ReverseRpcError: GetCohortMetric@RhinoHealthDev: ",
                "",
            )
            error_data = json.loads(r2)
            message = error_data.get("message", error_data)
        except:
            pass
        raise Exception(
            f"Failed to parse response\nStatus is {self.raw_response.status_code}, Error: {message}, Content is {self.raw_response.content}\nException is {e}"
        )
