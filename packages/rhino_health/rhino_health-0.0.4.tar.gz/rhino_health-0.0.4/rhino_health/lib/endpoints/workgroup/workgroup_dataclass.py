from typing import List

from rhino_health.lib.dataclass import RhinoBaseModel

# TODO


class Workgroup(RhinoBaseModel):
    uid: str
    name: str
    org_name: str
    users: "List[User]"
    admins: "List[User]"


class FutureWorkgroup(Workgroup):
    users: "List[FutureUser]"
    admins: "List[FutureUser]"
    pass


from rhino_health.lib.endpoints.user.user_dataclass import FutureUser, User

Workgroup.update_forward_refs()
FutureWorkgroup.update_forward_refs()
