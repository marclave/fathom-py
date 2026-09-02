---
name: fathom-analytics-api-python-sdk
description: "Python SDK for Fathom Analytics API. Use when writing Python code that calls Fathom Analytics API with the fathom-analytics package: installing it, constructing and authenticating the client, and calling API operations."
---

# Fathom Analytics API Python SDK

Generated Python client for Fathom Analytics API, published as `fathom-analytics`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install fathom-analytics
```

## Client setup and authentication

```python
import os

from fathom_analytics import FathomAnalyticsAPI

client = FathomAnalyticsAPI(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `bearer_auth` (env: `BEARER_AUTH`) — Authenticate with a personal API token created at https://app.usefathom.com/api, sent as `Authorization: Bearer <token>`.

## Calling operations

```python
import os

from fathom_analytics import FathomAnalyticsAPI

client = FathomAnalyticsAPI(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)

client.account.list()
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](../../../api.md) before writing a call.

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from fathom_analytics import APIStatusError

try:
    client.account.list()
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](../../../README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](../../../api.md) — complete catalogue of every operation with request and response types.
