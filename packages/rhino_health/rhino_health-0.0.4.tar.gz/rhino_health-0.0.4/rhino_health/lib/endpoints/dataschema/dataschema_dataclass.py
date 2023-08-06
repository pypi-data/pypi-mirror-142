import csv
import io
from typing import Any, List, Optional

from rhino_health.lib.dataclass import RhinoBaseModel

# class SchemaVariables:
#     def __init__(self, raw_data):
#         self.raw_data = raw_data
#         fieldnames, parsed_data = self.parse_data(raw_data)
#         self.fieldnames = fieldnames
#         self.parsed_data = parsed_data
#
#     def parse_data(self, raw_data):
#         pass  # TODO
#
#     def to_csv(self, csvfile):
#         with csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
#
#             writer.writeheader()
#             for row in self.parsed_data:
#                 writer.writerow(row)
#
#             csvfile.close()
#             return csvfile


class Dataschema(RhinoBaseModel):
    uid: Optional[str]
    name: str
    description: str
    base_version_uid: Optional[str]

    version: int
    date_added: str
    # schema_variables: SchemaVariables
    num_cohorts: int
    admins: "List[User]"

    # def __init__(self, schema_variables, **data):
    #     self.schema_variables = SchemaVariables(schema_variables)
    #     super().__init__(**data)


class FutureDataschema(Dataschema):
    admins: "List[FutureUser]"
    _base_version: Optional[Dataschema] = None
    project_uids: List[str]
    _projects: Any = None  # TODO
    primary_workgroup_uid: str
    _primary_workgroup: Any = None  # TODO

    # @property
    # def create_data(self):
    #     data = self.dict(["name", "description", "base_version_uid"])
    #     data["primary_workgroup"] = self.primary_workgroup_uid
    #     data["projects"] = self.project_uids
    #     data["schema_variables"] = self.schema_variables.to_csv(io.StringIO()).splitlines()
    #     return data

    # def create(self):
    #     if self._persisted or self.uid:
    #         raise RuntimeError("Dataschema has already been created")
    #     created_cohort = self.session.cohort.create_dataschema(self)
    #     return created_cohort

    def delete(self):
        if not self._persisted or not self.uid:
            raise RuntimeError("Dataschema has already been deleted")

        self.session.dataschema.remove_dataschema(self.uid)
        self._persisted = False
        self.uid = None
        return self

    # TODO: No existing endpoint for this
    # @property
    # def workgroup(self):
    #     raise NotImplementedError
    #     if self._workgroup:
    #         return self._workgroup
    #     if self.workgroup_uid:
    #         self._workgroup = self.session.workgroup.get_workgroups([self.workgroup_uid])[0]
    #         return self._workgroup
    #     else:
    #         return None


from rhino_health.lib.endpoints.user.user_dataclass import FutureUser, User

Dataschema.update_forward_refs()
FutureDataschema.update_forward_refs()
