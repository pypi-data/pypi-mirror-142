"""Altair Smartworks Edge Compute Platform request event.

This script contains the class that represents an Altair Smartworks Edge Compute
Platform request event. The request event is data structure that save data like
logs, errors or events like is raining.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, NoReturn, Union, ClassVar


class EventRequest:
    """Represent q event of a Thing"""

    EDGE_DATETIME_FORMAT: ClassVar[str] = '%Y-%m-%dT%H:%M:%SZ'

    _PARSE_EDGE_KEYS: ClassVar[dict[str, str]] = {
        'timestamp': 'created',
    }

    @classmethod
    def _parse_ecp_dict(cls, ecp_event_dict: dict[str, Any]) -> dict[str, Any]:
        """Parse the dict returned by the ECP API into correct keys and values for the class.

        :param ecp_event_dict: Dict from ECP API.
        :return: The dict with correct keys and values for the class.
        """
        href = ecp_event_dict['href']
        ecp_event_dict['uid'] = href[-1]
        ecp_event_dict['thing_id'] = href[1]
        ecp_event_dict['timestamp'] = ecp_event_dict.pop('timestamp')
        for old_key, new_key in cls._PARSE_EDGE_KEYS.items():
            if old_key in ecp_event_dict:
                ecp_event_dict[new_key] = ecp_event_dict.pop(old_key)
        return ecp_event_dict

    @classmethod
    def from_ecp_dict(cls, key: str,
                      ecp_event_dict: dict[str, Any]) -> EventRequest:
        """Convert the dict from the ECP API into the class.

        :param key: Event key.
        :param ecp_event_dict: Action dict from the ECP API.
        :return: ActionRequest object with the data from the edge_api_event_request_response_dict.
        """
        ecp_event_dict = cls._parse_ecp_dict(
            ecp_event_dict)
        return cls(key, **ecp_event_dict)

    def __init__(self, key: str, uid: str, thing_id: str,
                 *,
                 href: str,
                 data: Any,
                 created: Union[str, datetime]) -> NoReturn:
        """
        :param key: Event key.
        :param uid: Event ID.
        :param thing_id: Thing ID which has the event.
        :param href: href for the event request.
        :param data: data of the event.
        :param created: Datetime when the event is created in '%Y-%m-%dT%H:%M:%SZ' format.
        """
        if isinstance(created, str):
            created = datetime.strptime(created, self.EDGE_DATETIME_FORMAT)

        self._key = key
        self._uid = uid
        self._thing_id = thing_id
        self._href = href
        self._data = data
        self._created = created

    @property
    def key(self) -> str:
        """Event key."""

        return self._key

    @property
    def uid(self) -> str:
        """Event request ID."""

        return self._uid

    @property
    def thing_id(self) -> str:
        """Thing ID which has the event."""

        return self._thing_id

    @property
    def href(self) -> str:
        """href for the event request."""

        return self._href

    @property
    def data(self) -> Any:
        """Data from the event."""

        return self._data

    @property
    def created(self) -> datetime:
        """Datetime when the event was created in '%Y-%m-%dT%H:%M:%SZ' format."""

        return self._created

    def __eq__(self, other: Any):
        if not isinstance(other, EventRequest):
            return False
        return self._href == other._href

    def __hash__(self):
        return hash(self._href)

    def __str__(self) -> str:
        return f"{self._key}: {self._uid} {self._href} {self._data}"
