# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ..types import milestone_list_params, milestone_create_params, milestone_update_params

__all__ = ["MilestonesResource", "AsyncMilestonesResource"]


class MilestonesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MilestonesResourceWithRawResponse:
        return MilestonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MilestonesResourceWithStreamingResponse:
        return MilestonesResourceWithStreamingResponse(self)

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
        Return a list of all milestones this site owns. Milestones are sorted by `created_at` ascending to allow you to paginate with ease.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A list of milestone objects.

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
            client.milestones.list(
                site_id="CDBUGS",
                limit=10,
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/sites/{site_id}/milestones", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "starting_after": starting_after, "ending_before": ending_before},
                    milestone_list_params.MilestoneListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def create(
        self,
        site_id: str,
        *,
        name: str,
        milestone_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a milestone. Returns HTTP `201 Created` on success.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** A milestone object.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the milestone (up to 30 characters).
            milestone_date: The date of the milestone in `YYYY-MM-DD` format.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.milestones.create(
                site_id="CDBUGS",
                name="Website Redesign Launch",
                milestone_date="2024-01-15",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/sites/{site_id}/milestones", **{"site_id": site_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "milestone_date": milestone_date,
                },
                milestone_create_params.MilestoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        milestone_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Return a single milestone.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A milestone object.

        Args:
            milestone_id: The `id` (UUID) of the milestone you wish to retrieve.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.milestones.retrieve(
                site_id="CDBUGS",
                milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if milestone_id is None or (isinstance(milestone_id, str) and not milestone_id):
            raise ValueError(f"Expected a non-empty value for `milestone_id` but received {milestone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/sites/{site_id}/milestones/{milestone_id}", **{"site_id": site_id, "milestone_id": milestone_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        milestone_id: str,
        *,
        site_id: str,
        name: str,
        milestone_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a milestone. Both `name` and `milestone_date` are required.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** A milestone object.

        Args:
            milestone_id: The `id` (UUID) of the milestone you wish to update.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the milestone (up to 30 characters).
            milestone_date: The date of the milestone in `YYYY-MM-DD` format.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.milestones.update(
                site_id="CDBUGS",
                milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
                name="Website Redesign Launch v2",
                milestone_date="2024-01-20",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if milestone_id is None or (isinstance(milestone_id, str) and not milestone_id):
            raise ValueError(f"Expected a non-empty value for `milestone_id` but received {milestone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/sites/{site_id}/milestones/{milestone_id}", **{"site_id": site_id, "milestone_id": milestone_id}
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "milestone_date": milestone_date,
                },
                milestone_update_params.MilestoneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        milestone_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a milestone. Careful: you can't undo this, and neither can we.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

        Args:
            milestone_id: The `id` (UUID) of the milestone you wish to delete.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.milestones.delete(
                site_id="CDBUGS",
                milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if milestone_id is None or (isinstance(milestone_id, str) and not milestone_id):
            raise ValueError(f"Expected a non-empty value for `milestone_id` but received {milestone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/sites/{site_id}/milestones/{milestone_id}", **{"site_id": site_id, "milestone_id": milestone_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMilestonesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMilestonesResourceWithRawResponse:
        return AsyncMilestonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMilestonesResourceWithStreamingResponse:
        return AsyncMilestonesResourceWithStreamingResponse(self)

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
        Return a list of all milestones this site owns. Milestones are sorted by `created_at` ascending to allow you to paginate with ease.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A list of milestone objects.

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
            await client.milestones.list(
                site_id="CDBUGS",
                limit=10,
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/sites/{site_id}/milestones", **{"site_id": site_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "starting_after": starting_after, "ending_before": ending_before},
                    milestone_list_params.MilestoneListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def create(
        self,
        site_id: str,
        *,
        name: str,
        milestone_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a milestone. Returns HTTP `201 Created` on success.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** A milestone object.

        Args:
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the milestone (up to 30 characters).
            milestone_date: The date of the milestone in `YYYY-MM-DD` format.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.milestones.create(
                site_id="CDBUGS",
                name="Website Redesign Launch",
                milestone_date="2024-01-15",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/sites/{site_id}/milestones", **{"site_id": site_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "milestone_date": milestone_date,
                },
                milestone_create_params.MilestoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        milestone_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Return a single milestone.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** A milestone object.

        Args:
            milestone_id: The `id` (UUID) of the milestone you wish to retrieve.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.milestones.retrieve(
                site_id="CDBUGS",
                milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if milestone_id is None or (isinstance(milestone_id, str) and not milestone_id):
            raise ValueError(f"Expected a non-empty value for `milestone_id` but received {milestone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/sites/{site_id}/milestones/{milestone_id}", **{"site_id": site_id, "milestone_id": milestone_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        milestone_id: str,
        *,
        site_id: str,
        name: str,
        milestone_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a milestone. Both `name` and `milestone_date` are required.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** A milestone object.

        Args:
            milestone_id: The `id` (UUID) of the milestone you wish to update.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            name: The name of the milestone (up to 30 characters).
            milestone_date: The date of the milestone in `YYYY-MM-DD` format.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.milestones.update(
                site_id="CDBUGS",
                milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
                name="Website Redesign Launch v2",
                milestone_date="2024-01-20",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if milestone_id is None or (isinstance(milestone_id, str) and not milestone_id):
            raise ValueError(f"Expected a non-empty value for `milestone_id` but received {milestone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/sites/{site_id}/milestones/{milestone_id}", **{"site_id": site_id, "milestone_id": milestone_id}
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "milestone_date": milestone_date,
                },
                milestone_update_params.MilestoneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        milestone_id: str,
        *,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a milestone. Careful: you can't undo this, and neither can we.

        **Permissions:** Requires write access to the site (`manage:{site_id}`).

        **Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

        Args:
            milestone_id: The `id` (UUID) of the milestone you wish to delete.
            site_id: The ID of the site. This is the same string you use in your tracking code.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.milestones.delete(
                site_id="CDBUGS",
                milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
            )
            ```
        """
        if site_id is None or (isinstance(site_id, str) and not site_id):
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if milestone_id is None or (isinstance(milestone_id, str) and not milestone_id):
            raise ValueError(f"Expected a non-empty value for `milestone_id` but received {milestone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/sites/{site_id}/milestones/{milestone_id}", **{"site_id": site_id, "milestone_id": milestone_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MilestonesResourceWithRawResponse:
    def __init__(self, milestones: MilestonesResource) -> None:
        self._milestones = milestones

        self.list = to_raw_response_wrapper(
            milestones.list,
        )
        self.create = to_raw_response_wrapper(
            milestones.create,
        )
        self.retrieve = to_raw_response_wrapper(
            milestones.retrieve,
        )
        self.update = to_raw_response_wrapper(
            milestones.update,
        )
        self.delete = to_raw_response_wrapper(
            milestones.delete,
        )


class AsyncMilestonesResourceWithRawResponse:
    def __init__(self, milestones: AsyncMilestonesResource) -> None:
        self._milestones = milestones

        self.list = async_to_raw_response_wrapper(
            milestones.list,
        )
        self.create = async_to_raw_response_wrapper(
            milestones.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            milestones.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            milestones.update,
        )
        self.delete = async_to_raw_response_wrapper(
            milestones.delete,
        )


class MilestonesResourceWithStreamingResponse:
    def __init__(self, milestones: MilestonesResource) -> None:
        self._milestones = milestones

        self.list = to_streamed_response_wrapper(
            milestones.list,
        )
        self.create = to_streamed_response_wrapper(
            milestones.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            milestones.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            milestones.update,
        )
        self.delete = to_streamed_response_wrapper(
            milestones.delete,
        )


class AsyncMilestonesResourceWithStreamingResponse:
    def __init__(self, milestones: AsyncMilestonesResource) -> None:
        self._milestones = milestones

        self.list = async_to_streamed_response_wrapper(
            milestones.list,
        )
        self.create = async_to_streamed_response_wrapper(
            milestones.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            milestones.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            milestones.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            milestones.delete,
        )
