"""Altair Smartworks Edge Compute Platform.

This module provides the connections and basic class for Altair Smartworks
Edge Compute Platform. Provides a wrapper for the ECP API, telemetry connection
and publish data and drier connection to receive updates. It also provides a base
Thing class that contains the basic functions to update attributes and properties,
execute methods and send telemetry data using the function or creating a task
that execute every provide time.
"""

from .action import ActionRequest
from .api import EdgeApi
from .credentials import EdgeCredentials
from .driver import Driver
from .event import EventRequest
from .health import EdgeServiceHealth
from .label import Label
from .telemetry import Telemetry
from .thing import BaseThing, Thing, ThingProperty, ThingAction
