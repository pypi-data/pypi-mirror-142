from collections import defaultdict
import json, asyncio, random, logging
from typing import List, Mapping
import pytest

from aiohttp import web
from aiohttp.test_utils import TestClient
from rmlab_errors import (
    ClientError,
    error_handler,
    exception_to_http_code,
    RuntimeError,
    ClientError,
    TimeoutError,
    ExpiredSessionError,
)

from rmlab_http_client import (
    HTTPClientBasic,
    HTTPClientPublic,
    HTTPClientJWT,
    HTTPClientApiKey,
    HTTPClientJWTRenewable,
    AsyncClient,
)

_EventsLog: Mapping[str, List[str]] = defaultdict(list)
_Tasks: Mapping[str, asyncio.Task] = dict()

logging.basicConfig(level=logging.DEBUG)


async def async_task(data: dict, operation_id: str):

    mock_events = ["a", "b", "c"]

    _EventsLog[operation_id].append("started")

    for mock_event in mock_events:
        await asyncio.sleep(1)
        print(f"Mock event {mock_event}")
        _EventsLog[operation_id].append("processing-" + mock_event)

    if data["request-data"] == "correct":
        _EventsLog[operation_id].append("success")
    else:
        _EventsLog[operation_id].append("failure")


async def server_operation_status(request):

    resp_payload = dict()

    try:

        assert request.method == "GET"
        operation_id = request.match_info["operation_id"]

        auth_content = request.headers["Authorization"]
        assert "Bearer mock-jwt" in auth_content

        resp_data = {
            "status": _EventsLog[operation_id][-1]
            if _EventsLog[operation_id][-1] == "success"
            or _EventsLog[operation_id][-1] == "failure"
            else "pending"
        }

        resp_payload = {
            "status": 200,
            "content_type": "application/json",
            "body": json.dumps(resp_data).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

    finally:

        return web.Response(**resp_payload)


async def server_operation_result(request):

    resp_payload = dict()

    try:

        assert request.method == "GET"
        operation_id = request.match_info["operation_id"]

        status = (
            _EventsLog[operation_id][-1]
            if _EventsLog[operation_id][-1] == "success"
            or _EventsLog[operation_id][-1] == "failure"
            else "pending"
        )

        if status == "pending":
            raise ClientError(f"Cannot fetch result of pending operation")
        elif status == "success":
            resp_payload = {
                "status": 200,
                "content_type": "application/json",
                "body": json.dumps(
                    {"async-resource-key": "async-resource-value"}
                ).encode(),
            }
        elif status == "failure":
            # Does not matter the exception type, but be different than ClientError
            raise RuntimeError(f"Async operation failed")

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

    finally:

        del _EventsLog[operation_id]

        # if not _Tasks[operation_id].done():
        #   _Tasks[operation_id].cancel()

        del _Tasks[operation_id]

        return web.Response(**resp_payload)


async def server_public(request):

    resp_payload = dict()

    try:

        assert request.method == "POST"

        data = await request.json()

        operation_id = str(random.randint(1000, 9999))

        task = asyncio.get_running_loop().create_task(async_task(data, operation_id))

        _EventsLog[operation_id].append("created")
        _Tasks[operation_id] = task

        resp_payload = {
            "status": 202,
            "content_type": "application/json",
            "body": json.dumps(
                {
                    "op_id": operation_id,
                    "poll_endpoint": "/async_op/status/",
                    "result_endpoint": "/async_op/result/",
                }
            ).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }
    finally:

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


async def case_async(
    aiohttp_client, ClientType, data, expect_exception, timeout, **client_kwargs
):

    app = web.Application()
    app.router.add_route("POST", "/async_public_op", server_public)
    app.router.add_route(
        "GET", "/async_op/status/{operation_id}", server_operation_status
    )
    app.router.add_route(
        "GET", "/async_op/result/{operation_id}", server_operation_result
    )
    app.router.add_route("POST", "/refresh", server_jwt_refresh)
    client: TestClient = await aiohttp_client(app)

    addr = "http://" + client.host + ":" + str(client.port)

    if "auth_address" in client_kwargs:
        client_kwargs["auth_address"] = addr + client_kwargs["auth_address"]

    if expect_exception is None:

        async with AsyncClient(
            ClientType,
            timeout_seconds=timeout,
            poll_seconds=0.2,
            op_address=addr,
            op_jwt="mock-jwt",
            address=addr,
            **client_kwargs,
        ) as async_client:

          resp_data = await async_client.submit_request(
              resource="/async_public_op", verb="post", data=data, return_type="json"
          )

        assert "async-resource-key" in resp_data
        assert resp_data["async-resource-key"] == "async-resource-value"

    else:

        with pytest.raises(expect_exception):

            async with AsyncClient(
                ClientType,
                timeout_seconds=timeout,
                poll_seconds=0.2,
                op_address=addr,
                op_jwt="mock-jwt",
                address=addr,
                **client_kwargs,
            ) as async_client:

              resp_data = await async_client.submit_request(
                  resource="/async_public_op", verb="post", data=data, return_type="json"
              )


async def test_async_public_correct(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientPublic,
        data={"request-data": "correct"},
        expect_exception=None,
        timeout=4,
    )


async def test_async_public_failure(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientPublic,
        data={"request-data": "incorrect"},
        expect_exception=RuntimeError,
        timeout=4,
    )


async def test_async_public_timeout(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientPublic,
        data={"request-data": "correct"},
        expect_exception=TimeoutError,
        timeout=1,
    )

    await case_async(
        aiohttp_client,
        HTTPClientPublic,
        data={"request-data": "incorrect"},
        expect_exception=TimeoutError,
        timeout=1,
    )


async def test_async_basic_correct(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientBasic,
        data={"request-data": "correct"},
        expect_exception=None,
        timeout=4,
        auth_data="mock-basic",
    )


async def test_async_basic_failure(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientBasic,
        data={"request-data": "incorrect"},
        expect_exception=RuntimeError,
        timeout=4,
        auth_data="mock-basic",
    )


async def test_async_basic_timeout(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientBasic,
        data={"request-data": "correct"},
        expect_exception=TimeoutError,
        timeout=1,
        auth_data="mock-basic",
    )

    await case_async(
        aiohttp_client,
        HTTPClientBasic,
        data={"request-data": "incorrect"},
        expect_exception=TimeoutError,
        timeout=1,
        auth_data="mock-basic",
    )


async def test_async_jwt_correct(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientJWT,
        data={"request-data": "correct"},
        expect_exception=None,
        timeout=4,
        jwt="mock-jwt",
    )


async def test_async_jwt_failure(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientJWT,
        data={"request-data": "incorrect"},
        expect_exception=RuntimeError,
        timeout=4,
        jwt="mock-jwt",
    )


async def test_async_jwt_timeout(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientJWT,
        data={"request-data": "correct"},
        expect_exception=TimeoutError,
        timeout=1,
        jwt="mock-jwt",
    )

    await case_async(
        aiohttp_client,
        HTTPClientJWT,
        data={"request-data": "incorrect"},
        expect_exception=TimeoutError,
        timeout=1,
        jwt="mock-jwt",
    )


async def test_async_key_correct(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientApiKey,
        data={"request-data": "correct"},
        expect_exception=None,
        timeout=4,
        api_key="mock-key",
    )


async def test_async_key_failure(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientApiKey,
        data={"request-data": "incorrect"},
        expect_exception=RuntimeError,
        timeout=4,
        api_key="mock-key",
    )


async def test_async_key_timeout(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientApiKey,
        data={"request-data": "correct"},
        expect_exception=TimeoutError,
        timeout=1,
        api_key="mock-key",
    )

    await case_async(
        aiohttp_client,
        HTTPClientApiKey,
        data={"request-data": "incorrect"},
        expect_exception=TimeoutError,
        timeout=1,
        api_key="mock-key",
    )


async def test_async_jwt_renew_correct(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientJWTRenewable,
        data={"request-data": "correct"},
        expect_exception=None,
        timeout=4,
        access_jwt="expired-jwt",
        auth_address="/refresh",
        refresh_jwt="refresh-jwt",
    )


async def test_async_jwt_renew_failure(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientJWTRenewable,
        data={"request-data": "incorrect"},
        expect_exception=RuntimeError,
        timeout=4,
        access_jwt="expired-jwt",
        auth_address="/refresh",
        refresh_jwt="refresh-jwt",
    )


async def test_async_jwt_renew_timeout(aiohttp_client):

    await case_async(
        aiohttp_client,
        HTTPClientJWTRenewable,
        data={"request-data": "correct"},
        expect_exception=TimeoutError,
        timeout=1,
        access_jwt="expired-jwt",
        auth_address="/refresh",
        refresh_jwt="refresh-jwt",
    )

    await case_async(
        aiohttp_client,
        HTTPClientJWTRenewable,
        data={"request-data": "incorrect"},
        expect_exception=TimeoutError,
        timeout=1,
        access_jwt="expired-jwt",
        auth_address="/refresh",
        refresh_jwt="refresh-jwt",
    )
