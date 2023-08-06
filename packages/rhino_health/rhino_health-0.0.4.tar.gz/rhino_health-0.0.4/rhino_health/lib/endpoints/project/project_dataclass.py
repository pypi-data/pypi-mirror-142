from typing import Any, Dict, List, cast

from rhino_health.lib.dataclass import RhinoBaseModel

# TODO: Actually finish dataclasses and make this usable
from rhino_health.lib.endpoints.user.user_dataclass import FutureUser, User


class Project(RhinoBaseModel):
    uid: str
    name: str
    description: str
    type: str
    slack_channel: str
    primary_workgroup_uid: str
    collaborating_workgroups_uids: List[str]
    users: List[User]
    status: Dict


class FutureProject(Project):
    users: List[FutureUser]
    _collaborating_workgroups: Any = None

    def collaborating_workgroups(self):
        if self._collaborating_workgroups:
            return self._collaborating_workgroups
        if self.collaborating_workgroups_uids:
            self._collaborating_workgroups = self.session.project.get_collaborating_workgroups(
                self.uid
            )
            return self._collaborating_workgroups
        else:
            return []

    def add_collaborator(self, collaborator_or_uid):
        from rhino_health.lib.endpoints.project.project_endpoints import ProjectFutureEndpoints

        from ..workgroup.workgroup_dataclass import Workgroup

        if isinstance(collaborator_or_uid, Workgroup):
            collaborator_or_uid = collaborator_or_uid.uid
        cast(self.session.project, ProjectFutureEndpoints).add_collaborator(
            self.uid, collaborator_or_uid
        )

    def remove_collaborator(self, collaborator_or_uid):
        from rhino_health.lib.endpoints.project.project_endpoints import ProjectFutureEndpoints

        from ..workgroup.workgroup_dataclass import Workgroup

        if isinstance(collaborator_or_uid, Workgroup):
            collaborator_or_uid = collaborator_or_uid.uid
        cast(self.session.project, ProjectFutureEndpoints).remove_collaborator(
            self.uid, collaborator_or_uid
        )

    # Add Schema
    # Local Schema from CSV
