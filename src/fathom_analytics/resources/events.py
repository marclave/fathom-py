# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types import (
    event_list_params,
    event_delete_by_name_params,
    event_create_params,
    event_set_currency_params,
    event_update_params,
)

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        site_id: str,
        *,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        ending_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Return a list of all events this site owns. Events are sorted by `created_at` ascending to allow you to paginate with ease.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A list of event objects.

        > **The id field is going away:** Each event still returns an `id` (the old goal code). We are removing that field on 24 September 2026. Identify events by `name` instead.

        > The `currency` field is returned as `null` on list responses. Set it with [Set event currency](#set-event-currency).

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            limit: A limit on the number of objects to be returned, between 1 and 100.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For example, if you make a list request and receive 10 objects ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` to fetch the next page.
            ending_before: A cursor for use in pagination, working in the opposite direction to `starting_after`. `ending_before` is an object ID that defines your place in the list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.events.list(
                site_id="CDBUGS",
                limit=10,
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/sites/{site_id}/events", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "starting_after": starting_after, "ending_before": ending_before},
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def delete_by_name(
        self,
        site_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an event by its name. If more than one event row shares the name, they are treated as one event and every matching row is deleted.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event you wish to delete.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.events.delete_by_name(
                site_id="CDBUGS",
                name="Purchase early access",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/sites/{site_id}/events", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, event_delete_by_name_params.EventDeleteByNameParams),
            ),
            cast_to=NoneType,
        )

    def create(
        self,
        site_id: str,
        *,
        name: str,
        currency: Literal[
            "dollar",
            "pound",
            "euro",
            "yuan",
            "peso",
            "shekel",
            "yen",
            "won",
            "hryvnia",
            "franc",
            "rupee",
            "integer",
            "none",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously created an event. This endpoint is no longer available.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event (up to 255 characters).
            currency: The currency used for any value attached to this event's completions. If omitted, defaults to `dollar`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. Track the event on your site, then use [List events](#list-events) and [Set event currency](#set-event-currency).

        Example:
            ```python
            client.events.create(
                site_id="CDBUGS",
                name="Purchase early access",
                currency="dollar",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._post(
            path_template("/sites/{site_id}/events", **{"site_id": site_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "currency": currency,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def set_currency(
        self,
        site_id: str,
        *,
        name: str,
        currency: Literal[
            "dollar",
            "pound",
            "euro",
            "yuan",
            "peso",
            "shekel",
            "yen",
            "won",
            "hryvnia",
            "franc",
            "rupee",
            "integer",
            "none",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set the currency of an event by its name. Use this instead of updating an event by its goal code. If more than one event row shares the name, they are treated as one event and every matching row is updated.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** Returns an updated object on success. Otherwise, this call returns an error.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event (up to 255 characters).
            currency: The currency used for any value attached to this event's completions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.events.set_currency(
                site_id="CDBUGS",
                name="Purchase early access",
                currency="pound",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/sites/{site_id}/events/currency", **{"site_id": site_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "currency": currency,
                },
                event_set_currency_params.EventSetCurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        event_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously returned a single event by its goal code. This endpoint is no longer available.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        Args:
            event_id: The `id` (tracking code) of the event, as returned when the event was created.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. Use [List events](#list-events).

        Example:
            ```python
            client.events.retrieve(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/sites/{site_id}/events/{event_id}", **{"site_id": site_id, "event_id": event_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update(
        self,
        event_id: str,
        *,
        site_id: str,
        name: str | Omit = omit,
        currency: Literal[
            "dollar",
            "pound",
            "euro",
            "yuan",
            "peso",
            "shekel",
            "yen",
            "won",
            "hryvnia",
            "franc",
            "rupee",
            "integer",
            "none",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously updated an event by its goal code. This endpoint is no longer available.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        Args:
            event_id: The `id` (tracking code) of the event you wish to update.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event (up to 255 characters).
            currency: The currency used for any value attached to this event's completions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. To change an event's currency, use [Set event currency](#set-event-currency).

        Example:
            ```python
            client.events.update(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._post(
            path_template("/sites/{site_id}/events/{event_id}", **{"site_id": site_id, "event_id": event_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "currency": currency,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete(
        self,
        event_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously deleted an event by its goal code. This endpoint is no longer available.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        Args:
            event_id: The `id` (tracking code) of the event you wish to delete.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. To delete an event, use [Delete event](#delete-event-by-name) with the event name.

        Example:
            ```python
            client.events.delete(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._delete(
            path_template("/sites/{site_id}/events/{event_id}", **{"site_id": site_id, "event_id": event_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def wipe(
        self,
        event_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously wiped all completion data belonging to an event. This endpoint is no longer available.

        Args:
            event_id: The `id` (tracking code) of the event.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint has been retired and now returns `410 Gone`. It is no longer possible to wipe an event's completion data via the API.

        Example:
            ```python
            client.events.wipe(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._delete(
            path_template("/sites/{site_id}/events/{event_id}/data", **{"site_id": site_id, "event_id": event_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        site_id: str,
        *,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        ending_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Return a list of all events this site owns. Events are sorted by `created_at` ascending to allow you to paginate with ease.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A list of event objects.

        > **The id field is going away:** Each event still returns an `id` (the old goal code). We are removing that field on 24 September 2026. Identify events by `name` instead.

        > The `currency` field is returned as `null` on list responses. Set it with [Set event currency](#set-event-currency).

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            limit: A limit on the number of objects to be returned, between 1 and 100.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For example, if you make a list request and receive 10 objects ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` to fetch the next page.
            ending_before: A cursor for use in pagination, working in the opposite direction to `starting_after`. `ending_before` is an object ID that defines your place in the list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.events.list(
                site_id="CDBUGS",
                limit=10,
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/sites/{site_id}/events", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "starting_after": starting_after, "ending_before": ending_before},
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_by_name(
        self,
        site_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an event by its name. If more than one event row shares the name, they are treated as one event and every matching row is deleted.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event you wish to delete.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.events.delete_by_name(
                site_id="CDBUGS",
                name="Purchase early access",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/sites/{site_id}/events", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, event_delete_by_name_params.EventDeleteByNameParams),
            ),
            cast_to=NoneType,
        )

    async def create(
        self,
        site_id: str,
        *,
        name: str,
        currency: Literal[
            "dollar",
            "pound",
            "euro",
            "yuan",
            "peso",
            "shekel",
            "yen",
            "won",
            "hryvnia",
            "franc",
            "rupee",
            "integer",
            "none",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously created an event. This endpoint is no longer available.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event (up to 255 characters).
            currency: The currency used for any value attached to this event's completions. If omitted, defaults to `dollar`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. Track the event on your site, then use [List events](#list-events) and [Set event currency](#set-event-currency).

        Example:
            ```python
            await client.events.create(
                site_id="CDBUGS",
                name="Purchase early access",
                currency="dollar",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._post(
            path_template("/sites/{site_id}/events", **{"site_id": site_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "currency": currency,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def set_currency(
        self,
        site_id: str,
        *,
        name: str,
        currency: Literal[
            "dollar",
            "pound",
            "euro",
            "yuan",
            "peso",
            "shekel",
            "yen",
            "won",
            "hryvnia",
            "franc",
            "rupee",
            "integer",
            "none",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set the currency of an event by its name. Use this instead of updating an event by its goal code. If more than one event row shares the name, they are treated as one event and every matching row is updated.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** Returns an updated object on success. Otherwise, this call returns an error.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event (up to 255 characters).
            currency: The currency used for any value attached to this event's completions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.events.set_currency(
                site_id="CDBUGS",
                name="Purchase early access",
                currency="pound",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/sites/{site_id}/events/currency", **{"site_id": site_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "currency": currency,
                },
                event_set_currency_params.EventSetCurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        event_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously returned a single event by its goal code. This endpoint is no longer available.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        Args:
            event_id: The `id` (tracking code) of the event, as returned when the event was created.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. Use [List events](#list-events).

        Example:
            ```python
            await client.events.retrieve(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/sites/{site_id}/events/{event_id}", **{"site_id": site_id, "event_id": event_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update(
        self,
        event_id: str,
        *,
        site_id: str,
        name: str | Omit = omit,
        currency: Literal[
            "dollar",
            "pound",
            "euro",
            "yuan",
            "peso",
            "shekel",
            "yen",
            "won",
            "hryvnia",
            "franc",
            "rupee",
            "integer",
            "none",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously updated an event by its goal code. This endpoint is no longer available.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        Args:
            event_id: The `id` (tracking code) of the event you wish to update.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the event (up to 255 characters).
            currency: The currency used for any value attached to this event's completions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. To change an event's currency, use [Set event currency](#set-event-currency).

        Example:
            ```python
            await client.events.update(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._post(
            path_template("/sites/{site_id}/events/{event_id}", **{"site_id": site_id, "event_id": event_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "currency": currency,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete(
        self,
        event_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously deleted an event by its goal code. This endpoint is no longer available.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        Args:
            event_id: The `id` (tracking code) of the event you wish to delete.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint is no longer available. To delete an event, use [Delete event](#delete-event-by-name) with the event name.

        Example:
            ```python
            await client.events.delete(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._delete(
            path_template("/sites/{site_id}/events/{event_id}", **{"site_id": site_id, "event_id": event_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def wipe(
        self,
        event_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously wiped all completion data belonging to an event. This endpoint is no longer available.

        Args:
            event_id: The `id` (tracking code) of the event.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint has been retired and now returns `410 Gone`. It is no longer possible to wipe an event's completion data via the API.

        Example:
            ```python
            await client.events.wipe(
                site_id="CDBUGS",
                event_id="ABCDEFGH",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if event_id is None or (isinstance(event_id, str) and not event_id):
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._delete(
            path_template("/sites/{site_id}/events/{event_id}/data", **{"site_id": site_id, "event_id": event_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.delete_by_name = to_raw_response_wrapper(
            events.delete_by_name,
        )
        self.create = to_raw_response_wrapper(
            events.create,
        )
        self.set_currency = to_raw_response_wrapper(
            events.set_currency,
        )
        self.retrieve = to_raw_response_wrapper(
            events.retrieve,
        )
        self.update = to_raw_response_wrapper(
            events.update,
        )
        self.delete = to_raw_response_wrapper(
            events.delete,
        )
        self.wipe = to_raw_response_wrapper(
            events.wipe,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.delete_by_name = async_to_raw_response_wrapper(
            events.delete_by_name,
        )
        self.create = async_to_raw_response_wrapper(
            events.create,
        )
        self.set_currency = async_to_raw_response_wrapper(
            events.set_currency,
        )
        self.retrieve = async_to_raw_response_wrapper(
            events.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            events.update,
        )
        self.delete = async_to_raw_response_wrapper(
            events.delete,
        )
        self.wipe = async_to_raw_response_wrapper(
            events.wipe,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.delete_by_name = to_streamed_response_wrapper(
            events.delete_by_name,
        )
        self.create = to_streamed_response_wrapper(
            events.create,
        )
        self.set_currency = to_streamed_response_wrapper(
            events.set_currency,
        )
        self.retrieve = to_streamed_response_wrapper(
            events.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            events.update,
        )
        self.delete = to_streamed_response_wrapper(
            events.delete,
        )
        self.wipe = to_streamed_response_wrapper(
            events.wipe,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.delete_by_name = async_to_streamed_response_wrapper(
            events.delete_by_name,
        )
        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
        self.set_currency = async_to_streamed_response_wrapper(
            events.set_currency,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            events.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            events.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            events.delete,
        )
        self.wipe = async_to_streamed_response_wrapper(
            events.wipe,
        )
