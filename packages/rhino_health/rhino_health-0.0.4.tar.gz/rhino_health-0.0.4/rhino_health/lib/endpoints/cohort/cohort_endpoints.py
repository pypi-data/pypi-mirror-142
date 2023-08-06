import json

from rhino_health.lib.endpoints.cohort.cohort_dataclass import Cohort, FutureCohort
from rhino_health.lib.endpoints.endpoint import Endpoint
from rhino_health.lib.metrics.base_metric import MetricResponse


class CohortEndpoints(Endpoint):
    @property
    def cohort_data_class(self):
        return Cohort

    def get_cohort(self, cohort_uid: str):
        return self.session.get(f"/cohorts/{cohort_uid}").to_dataclass(self.cohort_data_class)


class CohortFutureEndpoints(CohortEndpoints):
    @property
    def cohort_data_class(self):
        return FutureCohort

    # def add_cohort(session: RhinoSession, cohort_data: CohortCreateData = None):
    #     """
    #     NOT OFFICIALLY SUPPORTED/COMPLETE YET, also no current supported way to send cohort data over remote
    #     (import location has to be on the on-prem instance)
    #     """
    #     payload_data = cohort_data.__dict__
    #     create_data = {k: v for k, v in payload_data.items() if k in []}
    #     import_data = {k: v for k, v in payload_data.items() if k in []}
    #     newly_created_cohort = session.post("/cohorts/", create_data).to_dataclass(Cohort)
    #     return session.post(f"/cohorts/{newly_created_cohort.uid}/import", import_data)

    def export_cohort(self, cohort_uid: str, output_location: str, output_format: str) -> Cohort:
        """
        Sends a export cohort request to the ON-PREM instance holding the specified COHORT_UID.
        The file will be exported to OUTPUT_LOCATION on the on-prem instance in OUTPUT_FORMAT
        :param session:
        :param cohort_uid:
        :param output_location:
        :param output_format:
        :return: TODO
        """
        return self.session.get(
            f"/cohorts/{cohort_uid}/export",
            params={"output_location": output_location, "output_format": output_format},
        )

    def sync_cohort_info(self, cohort_uid: str):
        """
        Initializes a data sync from the relevant on-prem instance for the provided COHORT_UID
        """
        # TODO: what should this return value be?
        return self.session.get(f"/cohorts/{cohort_uid}/info")

    def remove_cohort(self, cohort_uid: str):
        # TODO What should the return be
        return self.session.post(f"/cohorts/{cohort_uid}/remove", {})

    def get_cohort_metric(self, cohort_uid: str, metric_configuration):
        return self.session.post(
            f"/cohorts/{cohort_uid}/metric/", metric_configuration.data()
        ).to_dataclass(MetricResponse)
