"""Altair Smartworks Edge Compute Platform request action.

This script contains the class that represents an Altair Smartworks Edge Compute
Platform action event. The action is function that can be call for a certain Thing
and this is the representation of this request like turn_light_on and contains the
data send and the status as well as the datatime when it was requested and completed.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, NoReturn, Optional, Union, ClassVar


class ActionRequest:
    """Represent the status of a request of a Thing action"""

    class Status(Enum):
        """Enum to specify the ActionRequest status"""

        PENDING = 'pending'
        RECEIVED = 'received'
        COMPLETED = 'completed'
        ERROR = 'error'

    EDGE_DATETIME_FORMAT: ClassVar[str] = '%Y-%m-%dT%H:%M:%SZ'

    _PARSE_EDGE_KEYS: ClassVar[dict[str, str]] = {
        'timeRequested': 'requested',
        'timeCompleted': 'completed',
        'input': 'action_input'
    }

    @classmethod
    def _parse_ecp_dict(cls, ecp_action_request_dict: dict[str, Any]) -> dict[str, Any]:
        """Parse the dict returned by the ECP API into correct keys and values for the class.

        :param ecp_action_request_dict: Dict from ECP API.
        :return: The dict with correct keys and values for the class.
        """

        href = ecp_action_request_dict['href'].split('/')
        ecp_action_request_dict['uid'] = href[-1]
        ecp_action_request_dict['thing_id'] = href[1]
        ecp_action_request_dict['status'] = cls.Status[ecp_action_request_dict.pop('status').upper()]
        for old_key, new_key in cls._PARSE_EDGE_KEYS.items():
            if old_key in ecp_action_request_dict:
                ecp_action_request_dict[new_key] = ecp_action_request_dict.pop(old_key)
        return ecp_action_request_dict

    @classmethod
    def from_ecp_dict(cls, key: str,
                      ecp_action_request_dict: dict[str, Any]) -> ActionRequest:
        """Convert the dict from the ECP API into the class.

        :param key: Action key.
        :param ecp_action_request_dict: Action dict from the ECP API.
        :return: ActionRequest object with the data from the edge_api_action_request_response_dict.
        """

        ecp_action_request_dict = cls._parse_ecp_dict(
            ecp_action_request_dict)
        return cls(key, **ecp_action_request_dict)

    def __init__(self, key: str, uid: str, thing_id: str,
                 *,
                 href: str, status: Status,
                 action_input: Any,
                 requested: Union[str, datetime], completed: Optional[Union[str, datetime]] = None) -> NoReturn:
        """
        :param key: Action key.
        :param uid: Action ID.
        :param thing_id: Thing ID which has the action key.
        :param href: Href of the execution.
        :param status: Status of the action request.
        :param action_input: The input data that sent to the action at the request execution.
        :param requested: Datetime when the action was requested in '%Y-%m-%dT%H:%M:%SZ' format.
        :param completed: Datetime when the action was completed or None if not completed in
        '%Y-%m-%dT%H:%M:%SZ' format.
        """

        if isinstance(requested, str):
            requested = datetime.strptime(requested, self.EDGE_DATETIME_FORMAT)
        if isinstance(completed, str):
            completed = datetime.strptime(completed, self.EDGE_DATETIME_FORMAT)

        self._key = key
        self._uid = uid
        self._thing_id = thing_id
        self._href = href
        self._status = status
        self._action_input = action_input
        self._requested = requested
        self._completed = completed

    @property
    def key(self) -> str:
        """Action key"""

        return self._key

    @property
    def uid(self) -> str:
        """Action request ID."""

        return self._uid

    @property
    def thing_id(self) -> str:
        """Thing ID which has the action."""

        return self._thing_id

    @property
    def href(self) -> str:
        """Href of the action."""

        return self._href

    @property
    def status(self) -> Status:
        """Status of the action request."""

        return self._status

    @property
    def action_input(self) -> Any:
        """Input data from the action request."""

        return self._action_input

    @property
    def requested(self) -> datetime:
        """Datetime when the action was requested."""

        return self._requested

    @property
    def completed(self) -> datetime:
        """Datetime when the action was completed in '%Y-%m-%dT%H:%M:%SZ' format."""

        return self._completed

    def is_completed(self) -> bool:
        """Check if the action is completed

        :return: True if the action is completed and False in other case.
        """

        return self._completed is not None

    def __eq__(self, other: Any):
        if not isinstance(other, ActionRequest):
            return False
        return self._href == other._href

    def __hash__(self):
        return hash(self._href)

    def __str__(self) -> str:
        return f"{self._key}: {self._uid} {self._href} {self._status} {self._action_input}"
