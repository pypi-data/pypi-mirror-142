"""Python API bindings for Manticore endpoints in the MATE REST API."""

from __future__ import annotations

from typing import Any, Dict, Iterator

from mate_common.models.manticore import MantiserveTaskInformation
from mate_rest_client.common import Routes


class ManticoreRoutes(Routes):
    """An adapter for interactions with Manticore endpoints."""

    def iter(self, **kwargs: Dict[str, Any]) -> Iterator[MantiserveTaskInformation]:
        """Yields each `MantiserveTaskInformation` currently available."""
        resp = self._client.get("/api/v1/manticore/tasks", params=dict(**kwargs, detail=True))
        infos = resp.json()
        for info in infos:
            yield MantiserveTaskInformation(**info)

    def __iter__(self) -> Iterator[MantiserveTaskInformation]:
        """Yields each `MantiserveTaskInformation` currently available."""
        yield from self.iter()
