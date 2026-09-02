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
from ..types import site_list_params, site_create_params, site_update_params

__all__ = ["SitesResource", "AsyncSitesResource"]


class SitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SitesResourceWithRawResponse:
        return SitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitesResourceWithStreamingResponse:
        return SitesResourceWithStreamingResponse(self)

    def list(
        self,
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
        Return a list of all sites this API key owns. Sites are sorted by `created_at` ascending to allow you to paginate with ease.

        **Permissions:** Requires read access to all sites (`all-sites-readonly`) or full account access.

        **Returns:** A list of site objects.

        Args:
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
            client.sites.list(
                limit=10,
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/sites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "starting_after": starting_after, "ending_before": ending_before},
                    site_list_params.SiteListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def create(
        self,
        *,
        name: str,
        sharing: Literal["none", "private", "public"] | Omit = omit,
        share_password: str | Omit = omit,
        timezone: str | Omit = omit,
        multi_domain: bool | Omit = omit,
        multi_domain_option: Literal["combined", "separate"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a site.

        **Permissions:** Requires full account access (`*`).

        **Returns:** A site object.

        Args:
            name: The name of the website. Any string (up to 255 characters) is acceptable, and it doesn't have to match the website URL.
            sharing: The sharing configuration. Supported values are `none`, `private` or `public`.
            share_password: When sharing is set to `private`, you must also send a password to access the site with (up to 255 characters).
            timezone: The site's reporting timezone as a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g. `America/New_York`). If omitted, the site inherits your account's default timezone.
            multi_domain: Set to `true` to allow this site to track multiple domains.
            multi_domain_option: How multi-domain data is grouped. Supported values are `combined` (report all domains together) or `separate` (report each domain individually).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.sites.create(
                name="Bugs Bunny Portfolio",
                sharing="none",
                multi_domain=False,
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/sites",
            body=maybe_transform(
                {
                    "name": name,
                    "sharing": sharing,
                    "share_password": share_password,
                    "timezone": timezone,
                    "multi_domain": multi_domain,
                    "multi_domain_option": multi_domain_option,
                },
                site_create_params.SiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        site_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Return a single site.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A site object.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.sites.retrieve(
                site_id="CDBUGS",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/sites/{site_id}", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        site_id: str,
        *,
        name: str | Omit = omit,
        sharing: Literal["none", "private", "public"] | Omit = omit,
        share_password: str | Omit = omit,
        timezone: str | Omit = omit,
        multi_domain: bool | Omit = omit,
        multi_domain_option: Literal["combined", "separate"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a site. Send only the fields you want to change.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** A site object.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the website (up to 255 characters).
            sharing: The sharing configuration. Supported values are `none`, `private` or `public`.
            share_password: When sharing is set to `private`, you must also send a password to access the site with (up to 255 characters).
            timezone: The site's reporting timezone as a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g. `America/New_York`). Reporting for this site will use this timezone.
            multi_domain: Set to `true` to allow this site to track multiple domains.
            multi_domain_option: How multi-domain data is grouped: `combined` or `separate`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.sites.update(
                site_id="CDBUGS",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/sites/{site_id}", **{"site_id": site_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "sharing": sharing,
                    "share_password": share_password,
                    "timezone": timezone,
                    "multi_domain": multi_domain,
                    "multi_domain_option": multi_domain_option,
                },
                site_update_params.SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        site_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a site. Careful: you can't undo this, and neither can we.

        **Permissions:** Requires full account access (`*`).

        **Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.sites.delete(
                site_id="CDBUGS",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/sites/{site_id}", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def wipe(
        self,
        site_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously wiped all pageviews and event completions from a website. This endpoint is no longer available.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint has been retired and now returns `410 Gone`. It is no longer possible to wipe a site's data via the API.

        Example:
            ```python
            client.sites.wipe(
                site_id="CDBUGS",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._delete(
            path_template("/sites/{site_id}/data", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSitesResourceWithRawResponse:
        return AsyncSitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitesResourceWithStreamingResponse:
        return AsyncSitesResourceWithStreamingResponse(self)

    async def list(
        self,
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
        Return a list of all sites this API key owns. Sites are sorted by `created_at` ascending to allow you to paginate with ease.

        **Permissions:** Requires read access to all sites (`all-sites-readonly`) or full account access.

        **Returns:** A list of site objects.

        Args:
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
            await client.sites.list(
                limit=10,
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/sites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "starting_after": starting_after, "ending_before": ending_before},
                    site_list_params.SiteListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def create(
        self,
        *,
        name: str,
        sharing: Literal["none", "private", "public"] | Omit = omit,
        share_password: str | Omit = omit,
        timezone: str | Omit = omit,
        multi_domain: bool | Omit = omit,
        multi_domain_option: Literal["combined", "separate"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a site.

        **Permissions:** Requires full account access (`*`).

        **Returns:** A site object.

        Args:
            name: The name of the website. Any string (up to 255 characters) is acceptable, and it doesn't have to match the website URL.
            sharing: The sharing configuration. Supported values are `none`, `private` or `public`.
            share_password: When sharing is set to `private`, you must also send a password to access the site with (up to 255 characters).
            timezone: The site's reporting timezone as a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g. `America/New_York`). If omitted, the site inherits your account's default timezone.
            multi_domain: Set to `true` to allow this site to track multiple domains.
            multi_domain_option: How multi-domain data is grouped. Supported values are `combined` (report all domains together) or `separate` (report each domain individually).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.sites.create(
                name="Bugs Bunny Portfolio",
                sharing="none",
                multi_domain=False,
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/sites",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "sharing": sharing,
                    "share_password": share_password,
                    "timezone": timezone,
                    "multi_domain": multi_domain,
                    "multi_domain_option": multi_domain_option,
                },
                site_create_params.SiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        site_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Return a single site.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A site object.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.sites.retrieve(
                site_id="CDBUGS",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/sites/{site_id}", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        site_id: str,
        *,
        name: str | Omit = omit,
        sharing: Literal["none", "private", "public"] | Omit = omit,
        share_password: str | Omit = omit,
        timezone: str | Omit = omit,
        multi_domain: bool | Omit = omit,
        multi_domain_option: Literal["combined", "separate"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a site. Send only the fields you want to change.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** A site object.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the website (up to 255 characters).
            sharing: The sharing configuration. Supported values are `none`, `private` or `public`.
            share_password: When sharing is set to `private`, you must also send a password to access the site with (up to 255 characters).
            timezone: The site's reporting timezone as a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g. `America/New_York`). Reporting for this site will use this timezone.
            multi_domain: Set to `true` to allow this site to track multiple domains.
            multi_domain_option: How multi-domain data is grouped: `combined` or `separate`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.sites.update(
                site_id="CDBUGS",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/sites/{site_id}", **{"site_id": site_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "sharing": sharing,
                    "share_password": share_password,
                    "timezone": timezone,
                    "multi_domain": multi_domain,
                    "multi_domain_option": multi_domain_option,
                },
                site_update_params.SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        site_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a site. Careful: you can't undo this, and neither can we.

        **Permissions:** Requires full account access (`*`).

        **Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.sites.delete(
                site_id="CDBUGS",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/sites/{site_id}", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def wipe(
        self,
        site_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Previously wiped all pageviews and event completions from a website. This endpoint is no longer available.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: This endpoint has been retired and now returns `410 Gone`. It is no longer possible to wipe a site's data via the API.

        Example:
            ```python
            await client.sites.wipe(
                site_id="CDBUGS",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._delete(
            path_template("/sites/{site_id}/data", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SitesResourceWithRawResponse:
    def __init__(self, sites: SitesResource) -> None:
        self._sites = sites

        self.list = to_raw_response_wrapper(
            sites.list,
        )
        self.create = to_raw_response_wrapper(
            sites.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sites.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sites.update,
        )
        self.delete = to_raw_response_wrapper(
            sites.delete,
        )
        self.wipe = to_raw_response_wrapper(
            sites.wipe,
        )


class AsyncSitesResourceWithRawResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
        self._sites = sites

        self.list = async_to_raw_response_wrapper(
            sites.list,
        )
        self.create = async_to_raw_response_wrapper(
            sites.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sites.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sites.update,
        )
        self.delete = async_to_raw_response_wrapper(
            sites.delete,
        )
        self.wipe = async_to_raw_response_wrapper(
            sites.wipe,
        )


class SitesResourceWithStreamingResponse:
    def __init__(self, sites: SitesResource) -> None:
        self._sites = sites

        self.list = to_streamed_response_wrapper(
            sites.list,
        )
        self.create = to_streamed_response_wrapper(
            sites.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sites.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sites.update,
        )
        self.delete = to_streamed_response_wrapper(
            sites.delete,
        )
        self.wipe = to_streamed_response_wrapper(
            sites.wipe,
        )


class AsyncSitesResourceWithStreamingResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
        self._sites = sites

        self.list = async_to_streamed_response_wrapper(
            sites.list,
        )
        self.create = async_to_streamed_response_wrapper(
            sites.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sites.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sites.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            sites.delete,
        )
        self.wipe = async_to_streamed_response_wrapper(
            sites.wipe,
        )
