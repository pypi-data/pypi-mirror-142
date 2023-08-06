# RMLab HTTP Client

Small python module wrapping a HTTP client based on `asyncio`, providing several utilities required on RMLab server:

* Basic/token authentication.

* Token refresh.

* State polling and result fetching of long-running asynchronous operations.

* Custom error handling unified for client and server.

## Installation

```
pip install rmlab-http-client
```

## Requirements

* python 3.9+
* aiohttp 3.8.1

## License

This package is offered under a [MIT License](LICENSE).