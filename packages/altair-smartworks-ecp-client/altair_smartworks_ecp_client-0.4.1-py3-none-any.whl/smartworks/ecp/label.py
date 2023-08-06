"""Altair Smartworks Edge Compute Platform label

This script contains the class that represents an Altair Smartworks Edge Compute
Platform Label.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, NoReturn, Optional, Union, ClassVar, Pattern


class Label:
    """Class that represent a Thing Label

    :var val_regex: Optional regular expression that is used to validate the property value in telemetry data.
    :var conversion_data: Represent the conversion between values in enum label.
    None if conversion_opts is not ConversionOption.ENUM
    """

    class ConversionOption(Enum):
        """Enum that represent the conversion options of a Label"""

        CELSIUS_TO_FAHRENHEIT = 'CELSIUS_TO_FAHRENHEIT'
        FAHRENHEIT_TO_CELSIUS = 'FAHRENHEIT_TO_CELSIUS'
        MULTIPLY_BY_1000 = 'MULTIPLY_BY_1000'
        DIVIDE_BY_1000 = 'DIVIDE_BY_1000'
        ENUM = 'ENUM'

    _PARSE_EDGE_KEYS: ClassVar[dict[str, str]] = {
        'labelId': 'uid',
        'validationRegex': 'val_regex',
        'conversionOption': 'conversion_opts',
        'conversionData': 'conversion_data'
    }

    @classmethod
    def _parse_ecp_dict(cls, ecp_label_dict: dict[str, Any]) -> dict[str, Any]:
        """Parse the dict returned by the ECP API into correct keys and values for the class.

        :param ecp_label_dict: Dict from ECP API.
        :return: The dict with correct keys and values for the class.
        """
        for old_key, new_key in cls._PARSE_EDGE_KEYS.items():
            if old_key in ecp_label_dict:
                ecp_label_dict[new_key] = ecp_label_dict.pop(old_key)
        return ecp_label_dict

    @classmethod
    def from_ecp_dict(cls, ecp_label_dict: dict[str, Any]) -> Label:
        """Convert the dict from the ECP API into the class.

        :param ecp_label_dict: Action dict from the ECP API.
        :return: ActionRequest object with the data from the edge_api_label_dict.
        """
        ecp_label_dict = cls._parse_ecp_dict(
            ecp_label_dict)
        return cls(**ecp_label_dict)

    def __init__(self,
                 name: str,
                 uid: Optional[str] = None,
                 *,
                 val_regex: Optional[Pattern] = None,
                 conversion_opts: Union[ConversionOption, str] = None,
                 conversion_data: Optional[dict[str, Any]] = None):
        """
        :param name: Label name.
        :param uid: Label ID.
        :param val_regex: Optional regular expression that is used to validate the property value in telemetry data.
        :param conversion_opts: The conversion that will be applied.
        :param conversion_data: This is used to supply the options for the ENUM option.
        """
        if isinstance(conversion_opts, str):
            conversion_opts = Label.ConversionOption[conversion_opts]

        self._name = name
        self._uid = uid
        self.val_regex = val_regex
        self._conversion_opts = conversion_opts
        self.conversion_data = conversion_data if conversion_opts == self.ConversionOption.ENUM and \
                                                  conversion_data is not None else {}

    @property
    def name(self) -> str:
        """Label name"""

        return self._name

    @property
    def uid(self) -> str:
        """Label ID"""

        return self._uid

    def __eq__(self, other: Any):
        if not isinstance(other, Label):
            return False
        return self._uid == other._uid

    def __hash__(self):
        return hash(self._uid)

    def __str__(self) -> str:
        return f"{self._name}: {self._uid} {self.val_regex} {self._conversion_opts.value} {self.conversion_data}"

    def to_ecp_dict(self) -> dict[str, Any]:
        """Convert to Altair Smartworks ECP dict format."""

        return {
            'name': self._name,
            'validationRegex': self.val_regex,
            'conversionOption': self._conversion_opts.value,
            'conversionData': self.conversion_data
        }

    def on_update(self, edge_api_label_dict: dict[str, Any]) -> NoReturn:
        """Call this method to update the attributes from a dict returned by the Edge.

        :param edge_api_label_dict: dict with the attributes. Equal attributes will be omitted.
        """
        for key, value in self._parse_ecp_dict(edge_api_label_dict).items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)  # Only change if it is different
