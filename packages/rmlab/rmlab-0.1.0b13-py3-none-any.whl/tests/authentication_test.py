import os, pytest
from dataclasses import dataclass
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from rmlab_http_client import AsyncClient, HTTPClientBasic
from rmlab._api.base import APIBaseInternal
from rmlab._api.endpoints import BaseURL
from rmlab_errors import AuthenticationError
from rmlab._version import __version__

import os


@dataclass
class TestLoginData:
    workgroup: str
    username: str
    password: str


@dataclass
class TestBaseURLs:
    api: str
    auth: str


@pytest.fixture
def base_urls():

    return TestBaseURLs(
        api=os.environ.get("RMLAB_URL_API") or BaseURL,
        auth=os.environ.get("RMLAB_URL_AUTH") or BaseURL,
    )


@pytest.fixture
def login_data():

    return TestLoginData(
        workgroup=os.environ["RMLAB_WORKGROUP"],
        username=os.environ["RMLAB_USERNAME"],
        password=os.environ["RMLAB_PASSWORD"],
    )


def test_web_is_up(base_urls):

    headers = {"User-Agent": "Mozilla/5.0"}

    if BaseURL in base_urls.api:
        # Expect correct html response
        assert urlopen(Request(base_urls.api, headers=headers)).getcode() == 200
        assert urlopen(Request(base_urls.auth, headers=headers)).getcode() == 200
    else:
        # Testing/Dev API only. Expect not found (404) response since '/' resource is not defined
        with pytest.raises(HTTPError):
            urlopen(Request(base_urls.api, headers=headers))
            urlopen(Request(base_urls.auth, headers=headers))


async def test_log_in_out(login_data, base_urls):

    auth_data = ":".join(list(login_data.__dict__.values()) + [__version__])

    login_client = AsyncClient(
        HTTPClientBasic,
        timeout_seconds=180,
        op_address=base_urls.auth,
        op_basic=auth_data,
        address=base_urls.auth,
        auth_data=auth_data,
    )

    login_resp = await login_client.submit_request(
        resource="/auth/user/login", verb="post", return_type="json"
    )

    assert "access_token" in login_resp
    assert "refresh_token" in login_resp
    assert "services" in login_resp
    assert "scenarios" in login_resp
    assert "username" in login_resp
    assert "workgroup" in login_resp

    async with HTTPClientBasic(
        address=base_urls.auth, auth_data=auth_data
    ) as logout_client:

        logout_resp = await logout_client.submit_request(
            resource="/auth/user/logout", verb="post"
        )

        assert logout_resp is None


async def test_session_args(login_data):

    async with APIBaseInternal(**login_data.__dict__):
        pass


async def test_session_env_vars(login_data):

    async with APIBaseInternal():
        pass


async def test_session_fail(login_data):

    with pytest.raises(AuthenticationError):
        async with APIBaseInternal(
            workgroup="wrong-workgroup", username="wrong-user", password="wrong-pwd"
        ):
            pass
