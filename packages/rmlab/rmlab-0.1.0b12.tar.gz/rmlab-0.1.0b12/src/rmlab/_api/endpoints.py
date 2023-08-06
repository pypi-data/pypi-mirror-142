"""Module providing base URLs and endpoints dataclass.
"""

from dataclasses import dataclass

BaseURL = "https://rmlab.net"

ResourceUserLogin = "/auth/user/login"
ResourceGetEndpoints = "/api/endpoints"


@dataclass
class ApiEndpoints:
    """Dataclass to store API endpoints. Initialized after after login."""

    summary: str = str(None)
    data_bounded: str = str(None)
    data_unbounded: str = str(None)
    data_unbounded_ids: str = str(None)
    data_unbounded_fields: str = str(None)
    data_flight: str = str(None)
    data_flight_post: str = str(None)
    data_airline_locations: str = str(None)
    data_reset: str = str(None)
    operation_trigger: str = str(None)
    operation_checkpoint: str = str(None)


@dataclass
class ApiEndpointsLimits:
    """Dataclass to store request limits of some API endpoints. Initialized after login."""

    data_unbounded_fields: int = 100
    data_flight: int = 100
    data_flight_post: int = 100
