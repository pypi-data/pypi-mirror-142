from typing import Any, List

from rhino_health.lib.dataclass import RhinoBaseModel


class User(RhinoBaseModel):
    uid: str
    full_name: str
    primary_workgroup_uid: str
    workgroups_uids: List[str]


class FutureUser(User):
    _primary_workgroup: Any
    _workgroups: Any

    def primary_workgroup(self):
        if not self._primary_workgroup:
            raise NotImplementedError
        return self._primary_workgroup

    def workgroups(self):
        if not self._workgroups:
            raise NotImplementedError
        return self._workgroups
