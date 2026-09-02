# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError, fathomError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import account, sites, events, milestones, reports
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.sites import SitesResource, AsyncSitesResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.milestones import MilestonesResource, AsyncMilestonesResource
    from .resources.reports import ReportsResource, AsyncReportsResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = ["fathom", "Asyncfathom", "Client", "AsyncClient", "Timeout", "Transport", "ProxiesTypes", "RequestOptions"]


class fathom(SyncAPIClient):
    # client options
    bearer_auth: str

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous fathom client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise fathomError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        if base_url is None:
            base_url = os.environ.get("FATHOM_BASE_URL")
        if base_url is None:
            base_url = "https://api.usefathom.com/v1"
        custom_headers_env = os.environ.get("FATHOM_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def account(self) -> "AccountResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AccountResource
        return AccountResource(self)

    @cached_property
    def sites(self) -> "SitesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sites import SitesResource
        return SitesResource(self)

    @cached_property
    def events(self) -> "EventsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.events import EventsResource
        return EventsResource(self)

    @cached_property
    def milestones(self) -> "MilestonesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.milestones import MilestonesResource
        return MilestonesResource(self)

    @cached_property
    def reports(self) -> "ReportsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import ReportsResource
        return ReportsResource(self)

    @cached_property
    def with_raw_response(self) -> fathomWithRawResponse:
        return fathomWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> fathomWithStreamedResponse:
        return fathomWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_auth_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_auth to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class Asyncfathom(AsyncAPIClient):
    # client options
    bearer_auth: str

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Asyncfathom client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise fathomError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        if base_url is None:
            base_url = os.environ.get("FATHOM_BASE_URL")
        if base_url is None:
            base_url = "https://api.usefathom.com/v1"
        custom_headers_env = os.environ.get("FATHOM_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def account(self) -> "AsyncAccountResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AsyncAccountResource
        return AsyncAccountResource(self)

    @cached_property
    def sites(self) -> "AsyncSitesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sites import AsyncSitesResource
        return AsyncSitesResource(self)

    @cached_property
    def events(self) -> "AsyncEventsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.events import AsyncEventsResource
        return AsyncEventsResource(self)

    @cached_property
    def milestones(self) -> "AsyncMilestonesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.milestones import AsyncMilestonesResource
        return AsyncMilestonesResource(self)

    @cached_property
    def reports(self) -> "AsyncReportsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import AsyncReportsResource
        return AsyncReportsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncfathomWithRawResponse:
        return AsyncfathomWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncfathomWithStreamedResponse:
        return AsyncfathomWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_auth_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_auth to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class fathomWithRawResponse:
    _client: fathom

    def __init__(self, client: fathom) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AccountResourceWithRawResponse
        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def sites(self) -> sites.SitesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sites import SitesResourceWithRawResponse
        return SitesResourceWithRawResponse(self._client.sites)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.events import EventsResourceWithRawResponse
        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def milestones(self) -> milestones.MilestonesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.milestones import MilestonesResourceWithRawResponse
        return MilestonesResourceWithRawResponse(self._client.milestones)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import ReportsResourceWithRawResponse
        return ReportsResourceWithRawResponse(self._client.reports)


class AsyncfathomWithRawResponse:
    _client: Asyncfathom

    def __init__(self, client: Asyncfathom) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AsyncAccountResourceWithRawResponse
        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def sites(self) -> sites.AsyncSitesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sites import AsyncSitesResourceWithRawResponse
        return AsyncSitesResourceWithRawResponse(self._client.sites)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.events import AsyncEventsResourceWithRawResponse
        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def milestones(self) -> milestones.AsyncMilestonesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.milestones import AsyncMilestonesResourceWithRawResponse
        return AsyncMilestonesResourceWithRawResponse(self._client.milestones)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import AsyncReportsResourceWithRawResponse
        return AsyncReportsResourceWithRawResponse(self._client.reports)


class fathomWithStreamedResponse:
    _client: fathom

    def __init__(self, client: fathom) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AccountResourceWithStreamingResponse
        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def sites(self) -> sites.SitesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sites import SitesResourceWithStreamingResponse
        return SitesResourceWithStreamingResponse(self._client.sites)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.events import EventsResourceWithStreamingResponse
        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def milestones(self) -> milestones.MilestonesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.milestones import MilestonesResourceWithStreamingResponse
        return MilestonesResourceWithStreamingResponse(self._client.milestones)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import ReportsResourceWithStreamingResponse
        return ReportsResourceWithStreamingResponse(self._client.reports)


class AsyncfathomWithStreamedResponse:
    _client: Asyncfathom

    def __init__(self, client: Asyncfathom) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AsyncAccountResourceWithStreamingResponse
        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def sites(self) -> sites.AsyncSitesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.sites import AsyncSitesResourceWithStreamingResponse
        return AsyncSitesResourceWithStreamingResponse(self._client.sites)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.events import AsyncEventsResourceWithStreamingResponse
        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def milestones(self) -> milestones.AsyncMilestonesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.milestones import AsyncMilestonesResourceWithStreamingResponse
        return AsyncMilestonesResourceWithStreamingResponse(self._client.milestones)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import AsyncReportsResourceWithStreamingResponse
        return AsyncReportsResourceWithStreamingResponse(self._client.reports)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = fathom
AsyncClient = Asyncfathom
