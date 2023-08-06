"""Altair Smartworks Edge Compute Platform health services.

This script contains the class that represents an Altair Smartworks Edge Compute
Platform health services report. It contains the name and key of the services as
well as its status and same util datetimes.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, NoReturn, Union, ClassVar


class EdgeServiceHealth:
    """Represent the status and health of a service"""

    class Status(Enum):
        """Represent the different status of a service"""

        START = 'start'
        UP = 'up'
        SLEEP = 'sleep'
        DOWN = 'down'

    EDGE_DATETIME_FORMAT: ClassVar[str] = '%Y-%m-%dT%H:%M:%SZ'

    _PARSE_EDGE_KEYS: ClassVar[dict[str, str]] = {
        'gitSha': 'git_sha',
        'buildDate': 'built',
        'lastUpdate': 'updated'
    }

    @classmethod
    def _parse_ecp_dict(cls, ecp_service_health_dict: dict[str, Any]) -> dict[str, Any]:
        """Parse the dict returned by the ECP API into correct keys and values for the class.

        :param ecp_service_health_dict: Dict from ECP API.
        :return: The dict with correct keys and values for the class.
        """

        ecp_service_health_dict['status'] = cls.Status[ecp_service_health_dict.pop('status').upper()]
        for old_key, new_key in cls._PARSE_EDGE_KEYS.items():
            if old_key in ecp_service_health_dict:
                ecp_service_health_dict[new_key] = ecp_service_health_dict.pop(old_key)
        return ecp_service_health_dict

    @classmethod
    def from_ecp_dict(cls, ecp_service_health_dict: dict[str, Any]) -> EdgeServiceHealth:
        """Convert the dict from the ECP API into the class.

        :param ecp_service_health_dict: Service health dict from the ECP API.
        :return: EdgeServiceHealth object with the data from the edge_api_edge_service_health_dict.
        """

        ecp_service_health_dict = cls._parse_ecp_dict(
            ecp_service_health_dict)
        return cls(**ecp_service_health_dict)

    def __init__(self, key: str, name: str, version: str,
                 *,
                 status: EdgeServiceHealth.Status, git_sha: str,
                 built: Union[str, datetime], registered: Union[str, datetime],
                 updated: Union[str, datetime]) -> NoReturn:
        """
        :param key: Service key.
        :param name: Service name.
        :param version: Service version deployed.
        :param status: Service health status.
        :param git_sha: Service build git SHA.
        :param built: Service build datetime in '%Y-%m-%dT%H:%M:%SZ' format.
        :param registered: Service registered datetime in '%Y-%m-%dT%H:%M:%SZ' format.
        :param updated: Service updated datetime in '%Y-%m-%dT%H:%M:%SZ' format.
        """

        if isinstance(built, str):
            built = datetime.strptime(built, self.EDGE_DATETIME_FORMAT)
        if isinstance(registered, str):
            registered = datetime.strptime(registered, self.EDGE_DATETIME_FORMAT)
        if isinstance(updated, str):
            updated = datetime.strptime(updated, self.EDGE_DATETIME_FORMAT)

        self._key = key
        self._name = name
        self._version = version
        self._status = status
        self._git_sha = git_sha
        self._built = built
        self._registered = registered
        self._updated = updated

    @property
    def key(self) -> str:
        """Service key."""

        return self._key

    @property
    def name(self) -> str:
        """Service name."""

        return self._name

    @property
    def version(self) -> str:
        """Service version."""

        return self._version

    @property
    def status(self) -> Status:
        """Service health status."""

        return self._status

    @property
    def git_sha(self) -> str:
        """Service build git SHA."""

        return self._git_sha

    @property
    def built(self) -> datetime:
        """Service built datetime in '%Y-%m-%dT%H:%M:%SZ' format."""

        return self._built

    @property
    def registered(self) -> datetime:
        """Service registered datetime in '%Y-%m-%dT%H:%M:%SZ' format."""

        return self._registered

    @property
    def updated(self) -> datetime:
        """Service updated datetime in '%Y-%m-%dT%H:%M:%SZ' format."""

        return self._updated

    def __eq__(self, other: Any):
        if not isinstance(other, EdgeServiceHealth):
            return False
        return self._key == other._key

    def __hash__(self):
        return hash(self._key)

    def __str__(self) -> str:
        return f"{self._name}: {self._key} {self._version} {self._status.value} {self._built} " \
               f"{self._registered} {self._updated}"
