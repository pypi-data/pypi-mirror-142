import logging, base64, io
from typing import Any, Mapping, Optional, Union
import aiohttp

from rmlab_errors import (
    ClientError,
    ExpiredTokenError,
    HTTPRequestError,
    TimeoutError,
    UnknownError,
    UnreachableError,
    make_errors_from_json,
    http_code_to_exception,
)

_FileType = io.BufferedReader


def _preformat_file_upload(
    data: Mapping[str, Any], file: _FileType
) -> aiohttp.FormData:
    """Creates a form data object from arguments, possibly appending a file.

    Args:
        data (Mapping[str, Any]): Data key to data value
        file (_FileType): A file object opened as `read/binary`

    Returns:
        aiohttp.FormData: Form data object appendable to the http request.
    """

    form_data = aiohttp.FormData()

    form_data.add_field("file", file, filename=file.name)

    for k, v in data.items():
        form_data.add_field(name=k, value=v)

    return form_data


class _HTTPClientBase(object):
    """Base class for HTTP clients handling different auth methods"""

    def __init__(self, *, address: str):
        """Initializes instance

        Args:
            address (str): Resource endpoint
        """

        self._address: str = address
        self._session: aiohttp.ClientSession = None  # To be set in derived class
        self._verb2coro = dict()

    async def __aenter__(self):

        assert self._session is not None

        return self

    async def __aexit__(self, exc_ty, exc_val, tb):

        if not self._session.closed:
            await self._session.close()

        if exc_ty is not None:
            logging.error(f"HTTPClientBase context manager got error {exc_ty}. Re-raising")
            # Return None or False => re-raise
        else:
            return True

    async def submit_request(
        self,
        *,
        resource: Optional[str] = "",
        verb: Optional[str] = "get",
        data: Optional[Mapping[str, Any]] = None,
        file: Optional[_FileType] = None,
        return_type: Optional[str] = None,
        timeout: Optional[int] = 30,
    ) -> Optional[dict]:
        """Submits the http request to the server.

        Args:
            resource (Optional[str], optional): Resource endpoint. Defaults to "".
            verb (Optional[str], optional): HTTP method (`get`, `post`, `put`, `delete`, ...). Defaults to "get".
            data (Optional[Mapping[str, Any]], optional): Request data payload. Defaults to None.
            file (Optional[_FileType], optional): File object payload. Defaults to None.
            return_type (Optional[str], optional): Format of the returned object (`json`). Defaults to None.
            timeout (Optional[int], optional): Request timeout in seconds. Defaults to 30.

        Raises:
            ValueError: If verb is not `post` when a file object is not None
            ValueError: If file object has the wrong format (must be opened as `read/binary`)
            err_obj: Any error returned from the server, regardless it is a client or a server error.

        Returns:
            Any: The result of the http request (a `json` object if `return_type` is `json`, or `None` otherwise).
        """

        url = self._address + resource

        err_obj = None

        if data is None:
            data = dict()

        if file is not None and isinstance(file, _FileType):
            if verb != "post":
                raise ValueError(f"Expected `post` verb when a file is passed")
            payload_args = {"data": _preformat_file_upload(data, file)}
        elif file is not None:
            raise ValueError(f"Expected type of file `{_FileType}`, got `{type(file)}`")
        else:
            payload_args = {"json": data}

        async with getattr(self._session, verb.lower())(
            url, **payload_args, timeout=timeout
        ) as resp:

            resp: aiohttp.ClientResponse

            if 400 <= resp.status:

                if resp.content_type == "application/json":

                    resp_json = await resp.json()

                    if "errors" in resp_json:
                        err_obj = make_errors_from_json(*resp_json["errors"])
                    else:
                        resp_txt = await resp.text()
                        err_obj = UnknownError(resp_txt)
                else:
                    text = await resp.text()
                    err_obj = http_code_to_exception(
                        resp.status, text, HTTPRequestError
                    )

            elif return_type == "json":
                return await resp.json()

        if err_obj is not None:
            raise err_obj


class HTTPClientPublic(_HTTPClientBase):
    """Simple HTTP Client context without auth"""

    def __init__(self, *, address: str):
        """Initializes instance.

        Args:
            address (str): Public resource endpoint
        """

        super(HTTPClientPublic, self).__init__(address=address)

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client for public resources.

        Returns:
            HTTPClientPublic: This client instance.
        """

        self._session = aiohttp.ClientSession(raise_for_status=False)

        return await super(HTTPClientPublic, self).__aenter__()


class HTTPClientBasic(_HTTPClientBase):
    """Simple HTTP Client context with basic auth"""

    def __init__(self, *, address: str, auth_data: str):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the basic auth
            auth_data (str): Basic authentication data
        """

        super(HTTPClientBasic, self).__init__(address=address)

        self._auth_data = base64.b64encode(auth_data.encode()).decode("utf-8")

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client session
        for resources behind basic auth.

        Returns:
            HTTPClientBasic: This client instance.
        """

        auth_headers = {"Authorization": "Basic " + self._auth_data}

        self._session = aiohttp.ClientSession(
            headers=auth_headers, raise_for_status=False
        )

        return await super(HTTPClientBasic, self).__aenter__()


class HTTPClientApiKey(_HTTPClientBase):
    """HTTP Client context requring api key auth"""

    def __init__(self, *, address: str, api_key: str):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the api key
            api_key (str): API key
        """

        super(HTTPClientApiKey, self).__init__(address=address)

        self._api_key = api_key

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client session
        for resources behind a API key.

        Returns:
            HTTPClientApiKey: This client instance.
        """

        auth_headers = {"X-Api-Key": self._api_key}

        self._session = aiohttp.ClientSession(
            headers=auth_headers, raise_for_status=False
        )

        return await super(HTTPClientApiKey, self).__aenter__()


class HTTPClientJWT(_HTTPClientBase):
    """HTTP Client context requring jwt auth"""

    def __init__(self, *, address: str, jwt: str):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the access token
            jwt (str): Access token
        """

        super(HTTPClientJWT, self).__init__(address=address)

        self._jwt = jwt

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client session
        for resources behind JWT auth.

        Returns:
            HTTPClientJWT: This client instance.
        """

        auth_headers = {"Authorization": "Bearer " + self._jwt}

        self._session = aiohttp.ClientSession(
            headers=auth_headers, raise_for_status=False
        )
        
        return await super(HTTPClientJWT, self).__aenter__()


class HTTPClientJWTRenewable:
    """HTTP Client context requring jwt auth, recovers at expiration given a refresh token"""

    def __init__(
        self, *, address: str, access_jwt: str, auth_address: str, refresh_jwt: str
    ):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the access token
            access_jwt (str): Access token
            auth_address (str): Address to submit the token refresh request
            refresh_jwt (str): Refresh token
        """

        # super(HTTPClientJWTRenewable, self).__init__(address=address, jwt=access_jwt)
        
        self._access_jwt = access_jwt

        self._request_address = address
        self._auth_address = auth_address
        self._refresh_jwt = refresh_jwt
        self._retry = False

    async def __aenter__(self):
        """Initializes asynchronous context manager for resources behind expiration-aware JWT auth.

        Returns:
            HTTPClientJWTRenewable: This client instance.
        """

        self._retry = True
        
        return self


    async def __aexit__(self, exc_ty, exc_val, tb):
        
        if exc_ty is not None:
            logging.error(f"HTTPClientJWTRenewable context manager got error {exc_ty}. Re-raising")
            # Return None or False => re-raise
        else:
            return True
    

    async def submit_request(self, **kwargs) -> Any:
        """Submits a synchronous request, forwarding `kwargs`to a client with JWT auth.
        If access token is expired, a new one is requested from the refresh token,
        and the request is re-submitted.

        Returns:
            Any: The result of the synchronous request.
        """

        while self._retry:

            try:

                if self._retry:
                    self._retry = False  # Don't let it retry in general
                    
                async with HTTPClientJWT(address=self._request_address, jwt=self._access_jwt) as jwt_client:
                    
                    return await jwt_client.submit_request(**kwargs)

            except ExpiredTokenError:

                async with HTTPClientJWT(
                    address=self._auth_address, jwt=self._refresh_jwt
                ) as auth_client:

                    auth_resp = await auth_client.submit_request(
                        verb="post", return_type="json"
                    )

                # Re-set credentials
                self._refresh_jwt = auth_resp["refresh_token"]
                self._access_jwt = auth_resp["access_token"]
                
                self._retry = True


import asyncio


class AsyncClient:
    """Wrapper over a client context to provide status polling and result fetching
    of a long-running asynchronous operation"""

    def __init__(
        self,
        base_class: Union[
            HTTPClientPublic,
            HTTPClientBasic,
            HTTPClientApiKey,
            HTTPClientJWT,
            HTTPClientJWTRenewable,
        ],
        *,
        timeout_seconds: int = 600,
        poll_seconds: int = 10,
        op_address: str,
        op_jwt: Optional[str] = None,
        op_basic: Optional[str] = None,
        **kwargs,
    ):
        """Initializes an async client wrapper

        Args:
            base_class (Union[HTTPClientPublic, HTTPClientBasic, HTTPClientApiKey, HTTPClientJWT, HTTPClientJWTRenewable]): Wrapped synchronous client
            op_address (str): Base address to poll asynchronous operation status and fetch its result.
            timeout_seconds (int, optional): Timeout in seconds to await for the asynchronous operation to finish. Defaults to 600.
            poll_seconds (int, optional): Poll frequency in seconds. Defaults to 10.
            op_jwt (Optional[str], optional): JWT to access the asynchronous operation endpoint, if required. Defaults to None.
            op_basic (Optional[str], optional): Basic auth string to access the asynchronous operation endpoint, if required. Defaults to None.

        Raises:
            ValueError: _description_
            UnreachableError: _description_
        """

        self._req_base_class = base_class
        self._base_kwargs = kwargs

        self._timeout_seconds = timeout_seconds
        self._poll_seconds = poll_seconds

        if op_jwt and op_basic:
            raise ValueError(
                f"Enabling of `op_jwt` and `op_basic` is mutually exclusive"
            )

        if op_jwt is None and op_basic is None:
            self._poll_op_client = HTTPClientPublic
            self._poll_op_args = {"address": op_address}
        elif op_jwt is not None:
            self._poll_op_client = HTTPClientJWT
            self._poll_op_args = {"address": op_address, "jwt": op_jwt}
        elif op_basic is not None:
            self._poll_op_client = HTTPClientBasic
            self._poll_op_args = {"address": op_address, "auth_data": op_basic}
        else:
            raise UnreachableError("While defining op poll arguments")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_ty, exc_val, tb):
        
        if exc_ty is not None:
            logging.error(f"AsyncClient context manager got error {exc_ty}. Re-raising")
            # Return None or False => re-raise
        else:
            return True

    async def submit_request(self, **req_kwargs) -> Any:
        """Submits an asynchronous request, polling the status and fetching the result when finished

        Raises:
            ClientError: If first response does not have the expected format of an async operation response.
            TimeoutError: If asynchronous operation has not finished after the timeout.

        Returns:
            Any: The result of the asynchronous request.
        """

        passed_seconds = 0
        return_type = None

        async with self._req_base_class(**self._base_kwargs) as client:

            if "return_type" in req_kwargs:
                return_type = req_kwargs.pop("return_type")

            async_resp = await client.submit_request(**req_kwargs, return_type="json")

            if not all(
                req_key in async_resp
                for req_key in ["op_id", "poll_endpoint", "result_endpoint"]
            ):
                raise ClientError(
                    "Unexpected async operation response. Is this an async endpoint?"
                )

            async_op_id, poll_endpoint, result_endpoint = (
                str(async_resp["op_id"]),
                async_resp["poll_endpoint"],
                async_resp["result_endpoint"],
            )

        # Short sleep before poll, in case this op lasts much less than 10 seconds, so we return sooner
        await asyncio.sleep(1)

        while passed_seconds < self._timeout_seconds:

            async with self._poll_op_client(**self._poll_op_args) as poll_op_client:

                resp = await poll_op_client.submit_request(
                    resource=poll_endpoint + async_op_id,
                    verb="get",
                    return_type="json",
                )

            if resp["status"] == "pending":

                logging.debug(
                    f"Awaiting for pending operation {async_op_id}. {passed_seconds} / {self._timeout_seconds}"
                )

                await asyncio.sleep(self._poll_seconds)

                passed_seconds += self._poll_seconds

            else:

                async with self._poll_op_client(**self._poll_op_args) as result_op_client:

                    result = await result_op_client.submit_request(
                        resource=result_endpoint + async_op_id,
                        verb="get",
                        return_type="json",
                    )

                if return_type:
                    # We are neglecting the return_type value, only caring whether it is None
                    # Result will always return a json object (dict,list...). We could handle different
                    # return types here in the future if we are interested in more return types other than json objs
                    return result
                else:
                    return

        raise TimeoutError(f"While awaiting for operation `{async_op_id}`")
