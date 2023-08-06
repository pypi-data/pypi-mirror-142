import os, logging
from typing import Any, List, Mapping, Optional, Union

from rmlab_errors import LogicError
from rmlab_http_client import (
    AsyncClient,
    HTTPClientBasic,
    HTTPClientJWTRenewable,
    HTTPClientJWT,
)
from rmlab._api.endpoints import (
    ApiEndpoints,
    ApiEndpointsLimits,
    BaseURL,
    ResourceUserLogin,
    ResourceGetEndpoints,
)

from rmlab._version import __version__

_Logger = logging.getLogger(__name__)

_ServicesType = List[str]
_ScenariosType = Mapping[int, str]

_UndefinedCredentials: Mapping[str, Union[str, _ServicesType, _ScenariosType]] = {
    "access_token": None,
    "refresh_token": None,
    "services": None,
    "scenarios": None,
    "username": None,
    "workgroup": None,
}


class APIBaseInternal:
    """Asynchronous context manager providing internal initialization, login and API server calls to derived classes."""

    def __init__(
        self,
        workgroup: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        """Initializes APIBaseInternal instance.

        Args:
            workgroup: (str, optional): Workgroup name. Defaults to None.
                If none, expects `RMLAB_WORKGROUP` environment variable definition.
            user (str, optional): User name. Defaults to None.
                If none, expects `RMLAB_USERNAME` environment variable definition.
            password (str, optional): Password. Defaults to None.
                If none, expects `RMLAB_PASSWORD` environment variable definition..

        Raises:
            AuthenticationError: If user or password are not defined.
        """

        if any([arg is None for arg in [workgroup, username, password]]):

            try:
                workgroup = os.environ["RMLAB_WORKGROUP"]
                username = os.environ["RMLAB_USERNAME"]
                password = os.environ["RMLAB_PASSWORD"]

            except KeyError:

                raise ValueError(
                    f"`RMLAB_WORKGROUP` / `RMLAB_USERNAME` / `RMLAB_PASSWORD` are undefined"
                )

        # Prepare login data to be used at __aenter__
        self._login_data = {
            "workgroup": workgroup,
            "username": username,
            "password": password,
            "version": __version__,
        }

        self._credentials = _UndefinedCredentials

        self._api_endpoints = ApiEndpoints()
        self._url_api = os.environ.get("RMLAB_URL_API") or BaseURL
        self._url_auth = os.environ.get("RMLAB_URL_AUTH") or BaseURL

    @property
    def _auth_data(self):
        return ":".join(self._login_data.values())

    @property
    def _workgroup(self):
        return self._credentials["workgroup"]

    @property
    def scenarios(self):
        return [int(sc_id) for sc_id in self._credentials["scenarios"].keys()]

    async def __aenter__(self):
        """Context manager asynchronous enter. Log in and credentials initialization.

        Returns:
            APIBaseInternal: This instance.
        """
        """"""

        login_client = AsyncClient(
            HTTPClientBasic,
            timeout_seconds=120,
            op_address=self._url_auth,
            op_basic=self._auth_data,
            address=self._url_auth,
            auth_data=self._auth_data,
        )

        _Logger.debug("Logging-in...")

        self._credentials = await login_client.submit_request(
            resource=ResourceUserLogin, verb="post", return_type="json"
        )

        async with HTTPClientJWT(
            address=self._url_api, jwt=self._credentials["access_token"]
        ) as client:

            resp = await client.submit_request(
                resource="/" + self._credentials["workgroup"] + ResourceGetEndpoints,
                return_type="json",
            )

            endpoints_json = resp["endpoints"]
            endpoints_limits_json = resp["endpoints_limits"]

        self._api_endpoints = ApiEndpoints(**endpoints_json)
        self._api_endpoints_limits = ApiEndpointsLimits(**endpoints_limits_json)

        _Logger.debug("Logged-in")

        return self

    async def __aexit__(self, exc_ty, exc_val, exc_tb):
        """Context manager asynchronous exit. Re-raise any error"""

        try:

            async with HTTPClientBasic(
                address=self._url_auth, auth_data=self._auth_data
            ) as logout_client:

                await logout_client.submit_request(
                    resource="/auth/user/logout", verb="post"
                )

            self._credentials = _UndefinedCredentials

            self._api_endpoints = ApiEndpoints()

        except Exception:
            # Do not propagate exceptions due to log-out
            pass

        # Do not handle other exceptions here, return None to re-raise

    async def _submit_call(self, is_async: Optional[bool] = False, **kwargs) -> Any:
        """Performs API call to server, forwarding keyword arguments.

        Args:
            is_async (Optional[bool], optional): Whether the resource is asynchronousor not. Defaults to False.

        Raises:
            LogicError: If credentials are not defined

        Returns:
            Any: The response of the API call.
        """

        if not is_async:

            # Synchronous API call

            if (
                self._credentials["access_token"] is None
                or self._credentials["refresh_token"] is None
            ):
                raise LogicError(f"Cannot submit API call, credentials undefined")

            async with HTTPClientJWTRenewable(
                address=self._url_api,
                access_jwt=self._credentials["access_token"],
                auth_address=self._url_auth,
                refresh_jwt=self._credentials["refresh_token"],
            ) as client:

                return await client.submit_request(**kwargs)

        else:

            # Asynchronous API call

            async with AsyncClient(
                HTTPClientJWTRenewable,
                op_address=self._url_api,
                op_jwt=self._credentials["access_token"],
                address=self._url_api,
                access_jwt=self._credentials["access_token"],
                auth_address=self._url_auth,
                refresh_jwt=self._credentials["refresh_token"],
            ) as async_client:

                return await async_client.submit_request(**kwargs)
