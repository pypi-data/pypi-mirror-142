import pytest
import json, base64
from aiohttp import web

from aiohttp.test_utils import TestClient

from rmlab_http_client import (
    HTTPClientApiKey,
    HTTPClientBasic,
    HTTPClientJWT,
    HTTPClientJWTRenewable,
    HTTPClientPublic,
)
from rmlab_errors import (
    ClientError,
    ExpiredSessionError,
    ExpiredTokenError,
    ForbiddenError,
    error_handler,
    exception_to_http_code,
)

# ---- Public resource


async def server_public(request):

    try:

        assert request.method == "POST"

        data = await request.json()

        if data["request-data"] == "correct":

            response = {"resource-key": "resource-value"}

            return web.Response(
                status=200,
                content_type="application/json",
                body=json.dumps(response).encode(),
            )

        else:

            raise ClientError("Emulating a client error")

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

        return web.Response(**resp_payload)


async def test_public(aiohttp_client):

    app = web.Application()
    app.router.add_route("POST", "/public_resource", server_public)
    client: TestClient = await aiohttp_client(app)

    # ---- Test correct case
    data = {"request-data": "correct"}

    async with HTTPClientPublic(
        address="http://" + client.host + ":" + str(client.port)
    ) as http_client:

        resp_data = await http_client.submit_request(
            resource="/public_resource", verb="post", data=data, return_type="json"
        )

    assert "resource-key" in resp_data
    assert resp_data["resource-key"] == "resource-value"

    # ---- Test failure case
    data = {"request-data": "incorrect"}

    with pytest.raises(ClientError):

        async with HTTPClientPublic(
            address="http://" + client.host + ":" + str(client.port)
        ) as http_client:

            resp_data = await http_client.submit_request(
                resource="/public_resource", verb="post", data=data, return_type="json"
            )


# ---- JWT resource


async def server_jwt_get_resource(request):

    assert request.method == "GET"
    auth_content = request.headers["Authorization"]
    assert "Bearer mock-jwt" in auth_content

    return web.Response(
        status=200,
        content_type="application/json",
        body=json.dumps({"resource-key": "resource-value"}).encode(),
    )


async def test_jwt(aiohttp_client):

    app = web.Application()
    app.router.add_route("GET", "/jwt_resource", server_jwt_get_resource)
    client: TestClient = await aiohttp_client(app)

    async with HTTPClientJWT(
        address="http://" + client.host + ":" + str(client.port), jwt="mock-jwt"
    ) as http_client:

        resp = await http_client.submit_request(
            resource="/jwt_resource", verb="get", return_type="json"
        )
        assert "resource-key" in resp
        assert resp["resource-key"] == "resource-value"


# ---- Basic auth resource


async def server_basic_resource(request):

    try:

        assert request.method == "GET"
        auth_content = request.headers["Authorization"]
        assert "Basic " in auth_content
        cred = base64.b64decode(auth_content[auth_content.find(" ") + 1 :]).decode(
            "utf-8"
        )

        if cred != "mock-basic":
            raise ForbiddenError("Wrong credentials")
        else:
            return web.Response(
                status=200,
                content_type="application/json",
                body=json.dumps({"resource-key": "resource-value"}).encode(),
            )

    except Exception as exc:
        return web.Response(
            status=exception_to_http_code(exc),
            content_type="application/json",
            body=json.dumps(error_handler(exc)).encode(),
        )


async def test_basic_auth(aiohttp_client):

    app = web.Application()
    app.router.add_route("GET", "/basic_resource", server_basic_resource)
    client: TestClient = await aiohttp_client(app)

    # ---- Test correct behavior
    async with HTTPClientBasic(
        address="http://" + client.host + ":" + str(client.port), auth_data="mock-basic"
    ) as key_client:

        resp = await key_client.submit_request(
            resource="/basic_resource", verb="get", return_type="json"
        )

        assert "resource-key" in resp
        assert resp["resource-key"] == "resource-value"

    # ---- Test failure
    with pytest.raises(ForbiddenError):

        async with HTTPClientBasic(
            address="http://" + client.host + ":" + str(client.port),
            auth_data="incorrect",
        ) as key_client:

            await key_client.submit_request(
                resource="/basic_resource", verb="get", return_type="json"
            )


# ---- Api key resource


async def server_key_resource(request):

    try:

        assert request.method == "GET"
        auth_content = request.headers["X-Api-Key"]

        if auth_content == "incorrect":
            raise ForbiddenError("Wrong API key")
        else:
            return web.Response(
                status=200,
                content_type="application/json",
                body=json.dumps({"resource-key": "resource-value"}).encode(),
            )

    except Exception as exc:
        return web.Response(
            status=exception_to_http_code(exc),
            content_type="application/json",
            body=json.dumps(error_handler(exc)).encode(),
        )


async def test_api_key(aiohttp_client):

    app = web.Application()
    app.router.add_route("GET", "/key_resource", server_key_resource)
    client: TestClient = await aiohttp_client(app)

    # ---- Test correct behavior
    async with HTTPClientApiKey(
        address="http://" + client.host + ":" + str(client.port), api_key="api-key"
    ) as key_client:

        resp = await key_client.submit_request(
            resource="/key_resource", verb="get", return_type="json"
        )

        assert "resource-key" in resp
        assert resp["resource-key"] == "resource-value"

    # ---- Test failure
    with pytest.raises(ForbiddenError):

        async with HTTPClientApiKey(
            address="http://" + client.host + ":" + str(client.port),
            api_key="incorrect",
        ) as key_client:

            await key_client.submit_request(
                resource="/key_resource", verb="get", return_type="json"
            )


# ---- Token refreshing


async def server_jwt_resource(request):

    try:

        assert request.method == "GET"
        auth_content = request.headers["Authorization"]
        assert "Bearer " in auth_content

        if "expired" in auth_content:

            raise ExpiredTokenError("Access token is expired")

        else:

            resp_data = {"resource-key": "resource-value"}

            return web.Response(
                status=200,
                content_type="application/json",
                body=json.dumps(resp_data).encode(),
            )

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

        return web.Response(**resp_payload)


async def server_jwt_refresh(request):

    resp_payload = {}

    try:

        assert request.method == "POST"

        auth_content = request.headers["Authorization"]
        assert "Bearer " in auth_content

        if "expired" in auth_content:
            raise ExpiredSessionError("Refresh token is expired")
        else:

            resp_payload = {
                "status": 200,
                "content_type": "application/json",
                "body": json.dumps(
                    {"access_token": "new-access", "refresh_token": "new-refresh"}
                ).encode(),
            }

    except ExpiredSessionError as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }
    finally:

        return web.Response(**resp_payload)


async def test_refresh(aiohttp_client):

    app = web.Application()
    app.router.add_route("GET", "/jwt_resource", server_jwt_resource)
    app.router.add_route("POST", "/refresh", server_jwt_refresh)

    # ---- Test implicit token renewal
    client: TestClient = await aiohttp_client(app)
    addr = "http://" + client.host + ":" + str(client.port)
    async with HTTPClientJWTRenewable(
        address=addr,
        access_jwt="expired-jwt",
        auth_address=addr + "/refresh",
        refresh_jwt="refresh-jwt",
    ) as client:

        res = await client.submit_request(
            resource="/jwt_resource", verb="get", return_type="json"
        )

        assert "resource-key" in res
        assert res["resource-key"] == "resource-value"

    # ---- Test implicit token renewal fail of refresh token also expired
    with pytest.raises(ExpiredSessionError):

        client: TestClient = await aiohttp_client(app)
        addr = "http://" + client.host + ":" + str(client.port)
        async with HTTPClientJWTRenewable(
            address=addr,
            access_jwt="expired-jwt",
            auth_address=addr + "/refresh",
            refresh_jwt="expired-jwt",
        ) as client:

            res = await client.submit_request(
                resource="/jwt_resource", verb="get", return_type="json"
            )
