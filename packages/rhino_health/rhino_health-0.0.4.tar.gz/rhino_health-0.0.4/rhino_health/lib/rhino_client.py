from rhino_health.lib.constants import ApiEnvironment
from rhino_health.lib.endpoints.cohort.cohort_endpoints import (
    CohortEndpoints,
    CohortFutureEndpoints,
)
from rhino_health.lib.endpoints.dataschema.dataschema_endpoints import (
    DataschemaEndpoints,
    DataschemaFutureEndpoints,
)
from rhino_health.lib.endpoints.project.project_endpoints import (
    ProjectEndpoints,
    ProjectFutureEndpoints,
)
from rhino_health.lib.utils import url_for


class EndpointTypes:
    PROJECT = "project"
    COHORT = "cohort"
    DATASCHEMA = "dataschema"


class SDKVersion:
    STABLE = "0.1"
    PREVIEW = "1.0"


VERSION_TO_CLOUD_API = {SDKVersion.STABLE: "v1", SDKVersion.PREVIEW: "v1"}


VERSION_TO_ENDPOINTS = {
    SDKVersion.STABLE: {
        EndpointTypes.PROJECT: ProjectEndpoints,
        EndpointTypes.COHORT: CohortEndpoints,
        EndpointTypes.DATASCHEMA: DataschemaEndpoints,
    },
    SDKVersion.PREVIEW: {
        EndpointTypes.PROJECT: ProjectFutureEndpoints,
        EndpointTypes.COHORT: CohortFutureEndpoints,
        EndpointTypes.DATASCHEMA: DataschemaFutureEndpoints,
    },
}


class RhinoClient:
    """
    Convenience mapping of endpoints to
    """

    def __init__(
        self, rhino_api_url: str = ApiEnvironment.PROD_API_URL, sdk_version: str = SDKVersion.STABLE
    ):
        self.rhino_api_url = rhino_api_url
        self.sdk_version = sdk_version
        if sdk_version not in VERSION_TO_ENDPOINTS.keys():
            raise ValueError(
                "The api version you specified is not supported in this version of the SDK"
            )
        self.project: ProjectEndpoints = VERSION_TO_ENDPOINTS[sdk_version][EndpointTypes.PROJECT](
            self
        )
        self.cohort: CohortEndpoints = VERSION_TO_ENDPOINTS[sdk_version][EndpointTypes.COHORT](self)
        self.dataschema: DataschemaEndpoints = VERSION_TO_ENDPOINTS[sdk_version][
            EndpointTypes.DATASCHEMA
        ](self)
        self.api_url = url_for(self.rhino_api_url, VERSION_TO_CLOUD_API[sdk_version])
