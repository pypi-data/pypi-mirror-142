from typing import List, Optional

from rhino_health.lib.endpoints.dataschema.dataschema_dataclass import Dataschema, FutureDataschema
from rhino_health.lib.endpoints.endpoint import Endpoint


class DataschemaEndpoints(Endpoint):
    @property
    def dataschema_data_class(self):
        return Dataschema

    def get_dataschemas(self, datasceham_uids: Optional[List[str]] = None) -> List[Dataschema]:
        """
        TODO
        """
        if not datasceham_uids:
            return self.session.get("/dataschemas/").to_dataclasses(self.dataschema_data_class)
        else:
            return [
                self.session.get(f"/dataschemas/{dataschema_uid}/").to_dataclass(
                    self.dataschema_data_class
                )
                for dataschema_uid in datasceham_uids
            ]


class DataschemaFutureEndpoints(DataschemaEndpoints):
    @property
    def dataschema_data_class(self):
        return FutureDataschema

    def create_dataschema(self, dataschema):
        return self.session.post("/dataschemas", dataschema.create_data)

    def get_dataschema_csv(self, dataschema_uid: str):
        return self.session.get(f"/dataschemas/{dataschema_uid}/export_to_csv")

    def remove_dataschema(self, dataschema_uid: str):
        return self.session.post(f"/dataschemas/{dataschema_uid}/remove")
