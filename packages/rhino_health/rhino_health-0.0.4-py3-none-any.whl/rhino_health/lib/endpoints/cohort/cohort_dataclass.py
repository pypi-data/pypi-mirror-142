from typing import Any, Optional

from rhino_health.lib.dataclass import RhinoBaseModel


class Cohort(RhinoBaseModel):
    uid: str
    name: str
    description: str
    base_version_uid: Optional[str]
    version: int
    date_added: str
    num_cases: int
    cohort_info: Optional[dict]
    import_status: str
    project_uid: str
    _project: Any = None
    workgroup_uid: str
    data_schema_uid: str
    data_schema_info: dict

    @property
    def project(self):
        if self._project:
            return self._project
        if self.project_uid:
            self._project = self.session.project.get_projects([self.project_uid])[0]
            return self._project
        else:
            return None


class FutureCohort(Cohort):
    _workgroup: Any = None
    _data_schema: Any = None

    def create(self):
        if self._persisted:
            raise RuntimeError("Cohort has already been created")
        created_cohort = self.session.cohort.create_cohort(self)
        return created_cohort

    def get_metric(self, metric_configuration):
        """
        Call the Rhino Cloud API with the metric
        Then Cloud API use gRPC -> on-prem where the cohort raw data exists
        On on-prem we will run the sklearn metric function with the provided arguments on the raw cohort data
        on-prem will perform k-anonymization, and return data to Cloud API
        TODO: How we support multiple instance
        :param metric:
        :return:
        """
        return self.session.cohort.get_cohort_metric(self.uid, metric_configuration)

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
