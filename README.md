# Fathom Analytics API

This library provides convenient access to the Fathom Analytics API from Python.

The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](./api.md)
- [Async](#async)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install fathom-analytics
```

<br />

## Usage

```python
import os

from fathom_analytics import fathom

client = fathom(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)

client.account.list()
```

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`Asyncfathom`) exposing the same resource tree with `await`.

```python
import asyncio

from fathom_analytics import Asyncfathom


async def main() -> None:
    client = Asyncfathom()
    await client.account.list()


asyncio.run(main())
```

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `string \| provider` | - | Authenticate with a personal API token created at https://app.usefathom.com/api, sent as `Authorization: Bearer <token>`. Defaults to BEARER_AUTH. |

Declared schemes:

- `bearerAuth` bearer token

<br />

## Errors

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from fathom_analytics import APIStatusError

try:
    client.account.list()
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

Documented error statuses: `400`, `401`, `410`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from fathom_analytics import fathom

client = fathom(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `str \| None` | `os.environ.get("BEARER_AUTH")` | Authenticate with a personal API token created at https://app.usefathom.com/api, sent as `Authorization: Bearer <token>`. |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `FATHOM_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `fathom_analytics` logger.

<br />

## Requirements

- Python 3.8 or newer

Powered by Scalar.
