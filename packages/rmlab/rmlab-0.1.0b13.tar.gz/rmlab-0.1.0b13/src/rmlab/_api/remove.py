from rmlab._api.base import APIBaseInternal
from rmlab._data.enums import (
    DataRemoveKind,
)


class APIRemoveInternal(APIBaseInternal):
    """Interface to remove data from server."""

    async def _remove_data(self, scen_id: int, kind: DataRemoveKind) -> None:
        """Remove some or all the data of a scenario.

        Args:
            scen_id (int): Scenario ID.
            kind (DataRemoveKind): Type of removal.
        """

        await self._submit_call(
            resource=self._api_endpoints.data_reset,
            verb="post",
            data={"scen_id": str(scen_id), "kind": kind.value},
        )
