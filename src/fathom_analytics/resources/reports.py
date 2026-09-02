# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types import report_aggregation_params, report_current_visitors_params

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self)

    def aggregation(
        self,
        *,
        entity: Literal["pageview", "event"],
        entity_id: str | Omit = omit,
        site_id: str | Omit = omit,
        entity_name: str | Omit = omit,
        aggregates: str,
        date_grouping: Literal["hour", "day", "month", "year"] | Omit = omit,
        field_grouping: str | Omit = omit,
        sort_by: str | Omit = omit,
        date_from: str | Omit = omit,
        date_to: str | Omit = omit,
        timezone: str | Omit = omit,
        limit: int | Omit = omit,
        filters: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Build a custom report. Group and filter on the fields you care about.

        **Permissions:** Requires read access to the relevant site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** Returns an array of objects. The properties of each object vary based on the aggregates and groupings you've asked for. All numeric values are returned as strings.

        > This API endpoint is only accurate on data from March 2021 onwards. Before then, we did not tie browser, country, pathname, etc. together, so we have no way to offer this advanced filtering on that data.

        > Grouped reports (`field_grouping`) default to 500 rows unless you set `limit`. The maximum is 1000, and this endpoint has no pagination. BI tools such as Looker Studio / Data Studio that fire many aggregations at once will hit the [concurrency cap](/api/v1/rate-limits), not the row cap. Space those requests, cache one extract per period, or raise the API plan.

        > **Goal codes are no longer available:** Reporting on an event by its goal code (`entity_id` with `entity=event`) is no longer available. Report on events using `site_id` and `entity_name` instead. Pageview reporting, where `entity_id` is the site `id`, is unaffected.

        #### Filtering

        Filters are supplied as a JSON array. Each filter is an object with a `property`, an `operator` and a string `value`. You can add as many filters as you like; see the examples in the code panel.

        We support the following operators:

        - `is`: exact match
        - `is not`: everything except an exact match
        - `is like`: contains the term (supports wildcards `*`)
        - `is not like`: does not contain the term
        - `matching`: matches a regular expression (regex) pattern
        - `not matching`: does not match a regex pattern

        **Operator availability depends on the field.** Text-style fields support all six operators; categorical fields support only `is` and `is not`:

        - **All six operators:** `domain`, `hostname`, `pathname`, `entry_page`, `exit_page`, `referrer_hostname`, `referrer_pathname`, `referrer_source`, `ref`, `utm_campaign`, `utm_source`, `utm_medium`, `utm_content`, `utm_term`
        - **`is` / `is not` only:** `device_type`, `operating_system`, `browser`, `country_code`, `city`, `state`, `region`

        Note: `domain` can be filtered on but not grouped by, while `keyword` can be grouped by but not filtered on.

        ##### Entry and exit pages

        `entry_page` is the pathname of the first pageview in a visit. `exit_page` is the pathname of the last pageview before the visitor leaves. Both are session-level fields. They mirror the Entry Pages and Exit Pages reports on your dashboard and work for both `field_grouping` and `filters`.

        When you filter by `entry_page`, only visits that *entered* on that page are included. A visitor who lands on `/home` and later views `/pricing` is excluded by `{"property": "entry_page", "operator": "is", "value": "/pricing"}`, but included when filtering on `pathname` instead.

        ##### Regex examples

        With `matching` / `not matching` you can build sophisticated filters:

        - `^/(about|contact|pricing)$`: match only /about, /contact and /pricing
        - `^/(about|contact|pricing)`: match paths starting with those
        - `^/blog/\d{4}/\d{2}/`: match blog URLs like /blog/2025/07/my-post
        - `^/products/[^/]+/$`: match product category pages

        Args:
            entity: The entity you want to report on. Events are treated separately from pageviews. Supported values: `pageview` and `event`.
            entity_id: When `entity` is `pageview`, this is the `id` of the site you want to aggregate on. When `entity` is `event`, do not pass a goal code here. Use `site_id` and `entity_name` instead. Pageview usage is unchanged.
            site_id: The `id` of the site the event belongs to.
            entity_name: The name of the event you want to report on. Example: `purchase`.
            aggregates: The aggregates you wish to include, separated by a comma.
            date_grouping: By default, we don't do any date grouping and return total aggregations. Override this with `hour`, `day`, `month` or `year`. Note: `hour` grouping is only supported for date ranges of up to 7 days.
            field_grouping: The fields you want to group by, separated by a comma (e.g. `hostname,pathname`). Supported values: `hostname`, `pathname`, `entry_page`, `exit_page`, `referrer_hostname`, `referrer_pathname`, `referrer_source`, `browser`, `country_code`, `city`, `state`, `region`, `device_type`, `operating_system`, `utm_campaign`, `utm_content`, `utm_medium`, `utm_source`, `utm_term`, `keyword` and `ref`.
            sort_by: The field you want to sort by, in the format `field:asc|desc`. You can use any field present in `aggregates` or `field_grouping`. When using `date_grouping`, you can also sort by `timestamp:asc` or `timestamp:desc`.
            date_from: Timestamp (e.g. `2022-04-01 15:31:00`). Should match the timezone you're reporting in. Defaults to the entity's first recorded data.
            date_to: Timestamp (e.g. `2022-04-01 15:31:00`). Should match the timezone you're reporting in. Default: now.
            timezone: **Deprecated.** We now report using each site's configured timezone by default. If provided, this [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) overrides the site's timezone for this request. We'll be removing this parameter in the future.
            limit: Optional integer from `1` to `1000` inclusive.
            filters: A JSON-encoded array of filter objects. See the filtering reference below for the full list of supported properties and operators. Each filter's `value` must be a string.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            client.reports.aggregation(
                entity="pageview",
                aggregates="pageviews",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/aggregations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity": entity,
                        "entity_id": entity_id,
                        "site_id": site_id,
                        "entity_name": entity_name,
                        "aggregates": aggregates,
                        "date_grouping": date_grouping,
                        "field_grouping": field_grouping,
                        "sort_by": sort_by,
                        "date_from": date_from,
                        "date_to": date_to,
                        "timezone": timezone,
                        "limit": limit,
                        "filters": filters,
                    },
                    report_aggregation_params.ReportAggregationParams,
                ),
            ),
            cast_to=NoneType,
        )

    def current_visitors(
        self,
        *,
        site_id: str,
        detailed: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns the total number of current visitors on a site. The detailed view also returns the top 150 pages and top 150 referrers.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** The current visitor count, with an optional detailed breakdown.

        Args:
            site_id: The `id` of the site.
            detailed: Set to `true` for a detailed breakdown of pages and referrers. Otherwise you'll only get a count.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Simple

        Example:
            ```python
            client.reports.current_visitors(
                site_id="CDBUGS",
                detailed=False,
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/current_visitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"site_id": site_id, "detailed": detailed},
                    report_current_visitors_params.ReportCurrentVisitorsParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self)

    async def aggregation(
        self,
        *,
        entity: Literal["pageview", "event"],
        entity_id: str | Omit = omit,
        site_id: str | Omit = omit,
        entity_name: str | Omit = omit,
        aggregates: str,
        date_grouping: Literal["hour", "day", "month", "year"] | Omit = omit,
        field_grouping: str | Omit = omit,
        sort_by: str | Omit = omit,
        date_from: str | Omit = omit,
        date_to: str | Omit = omit,
        timezone: str | Omit = omit,
        limit: int | Omit = omit,
        filters: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Build a custom report. Group and filter on the fields you care about.

        **Permissions:** Requires read access to the relevant site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** Returns an array of objects. The properties of each object vary based on the aggregates and groupings you've asked for. All numeric values are returned as strings.

        > This API endpoint is only accurate on data from March 2021 onwards. Before then, we did not tie browser, country, pathname, etc. together, so we have no way to offer this advanced filtering on that data.

        > Grouped reports (`field_grouping`) default to 500 rows unless you set `limit`. The maximum is 1000, and this endpoint has no pagination. BI tools such as Looker Studio / Data Studio that fire many aggregations at once will hit the [concurrency cap](/api/v1/rate-limits), not the row cap. Space those requests, cache one extract per period, or raise the API plan.

        > **Goal codes are no longer available:** Reporting on an event by its goal code (`entity_id` with `entity=event`) is no longer available. Report on events using `site_id` and `entity_name` instead. Pageview reporting, where `entity_id` is the site `id`, is unaffected.

        #### Filtering

        Filters are supplied as a JSON array. Each filter is an object with a `property`, an `operator` and a string `value`. You can add as many filters as you like; see the examples in the code panel.

        We support the following operators:

        - `is`: exact match
        - `is not`: everything except an exact match
        - `is like`: contains the term (supports wildcards `*`)
        - `is not like`: does not contain the term
        - `matching`: matches a regular expression (regex) pattern
        - `not matching`: does not match a regex pattern

        **Operator availability depends on the field.** Text-style fields support all six operators; categorical fields support only `is` and `is not`:

        - **All six operators:** `domain`, `hostname`, `pathname`, `entry_page`, `exit_page`, `referrer_hostname`, `referrer_pathname`, `referrer_source`, `ref`, `utm_campaign`, `utm_source`, `utm_medium`, `utm_content`, `utm_term`
        - **`is` / `is not` only:** `device_type`, `operating_system`, `browser`, `country_code`, `city`, `state`, `region`

        Note: `domain` can be filtered on but not grouped by, while `keyword` can be grouped by but not filtered on.

        ##### Entry and exit pages

        `entry_page` is the pathname of the first pageview in a visit. `exit_page` is the pathname of the last pageview before the visitor leaves. Both are session-level fields. They mirror the Entry Pages and Exit Pages reports on your dashboard and work for both `field_grouping` and `filters`.

        When you filter by `entry_page`, only visits that *entered* on that page are included. A visitor who lands on `/home` and later views `/pricing` is excluded by `{"property": "entry_page", "operator": "is", "value": "/pricing"}`, but included when filtering on `pathname` instead.

        ##### Regex examples

        With `matching` / `not matching` you can build sophisticated filters:

        - `^/(about|contact|pricing)$`: match only /about, /contact and /pricing
        - `^/(about|contact|pricing)`: match paths starting with those
        - `^/blog/\d{4}/\d{2}/`: match blog URLs like /blog/2025/07/my-post
        - `^/products/[^/]+/$`: match product category pages

        Args:
            entity: The entity you want to report on. Events are treated separately from pageviews. Supported values: `pageview` and `event`.
            entity_id: When `entity` is `pageview`, this is the `id` of the site you want to aggregate on. When `entity` is `event`, do not pass a goal code here. Use `site_id` and `entity_name` instead. Pageview usage is unchanged.
            site_id: The `id` of the site the event belongs to.
            entity_name: The name of the event you want to report on. Example: `purchase`.
            aggregates: The aggregates you wish to include, separated by a comma.
            date_grouping: By default, we don't do any date grouping and return total aggregations. Override this with `hour`, `day`, `month` or `year`. Note: `hour` grouping is only supported for date ranges of up to 7 days.
            field_grouping: The fields you want to group by, separated by a comma (e.g. `hostname,pathname`). Supported values: `hostname`, `pathname`, `entry_page`, `exit_page`, `referrer_hostname`, `referrer_pathname`, `referrer_source`, `browser`, `country_code`, `city`, `state`, `region`, `device_type`, `operating_system`, `utm_campaign`, `utm_content`, `utm_medium`, `utm_source`, `utm_term`, `keyword` and `ref`.
            sort_by: The field you want to sort by, in the format `field:asc|desc`. You can use any field present in `aggregates` or `field_grouping`. When using `date_grouping`, you can also sort by `timestamp:asc` or `timestamp:desc`.
            date_from: Timestamp (e.g. `2022-04-01 15:31:00`). Should match the timezone you're reporting in. Defaults to the entity's first recorded data.
            date_to: Timestamp (e.g. `2022-04-01 15:31:00`). Should match the timezone you're reporting in. Default: now.
            timezone: **Deprecated.** We now report using each site's configured timezone by default. If provided, this [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) overrides the site's timezone for this request. We'll be removing this parameter in the future.
            limit: Optional integer from `1` to `1000` inclusive.
            filters: A JSON-encoded array of filter objects. See the filtering reference below for the full list of supported properties and operators. Each filter's `value` must be a string.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful response

        Example:
            ```python
            await client.reports.aggregation(
                entity="pageview",
                aggregates="pageviews",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/aggregations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity": entity,
                        "entity_id": entity_id,
                        "site_id": site_id,
                        "entity_name": entity_name,
                        "aggregates": aggregates,
                        "date_grouping": date_grouping,
                        "field_grouping": field_grouping,
                        "sort_by": sort_by,
                        "date_from": date_from,
                        "date_to": date_to,
                        "timezone": timezone,
                        "limit": limit,
                        "filters": filters,
                    },
                    report_aggregation_params.ReportAggregationParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def current_visitors(
        self,
        *,
        site_id: str,
        detailed: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns the total number of current visitors on a site. The detailed view also returns the top 150 pages and top 150 referrers.

        **Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

        **Returns:** The current visitor count, with an optional detailed breakdown.

        Args:
            site_id: The `id` of the site.
            detailed: Set to `true` for a detailed breakdown of pages and referrers. Otherwise you'll only get a count.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Simple

        Example:
            ```python
            await client.reports.current_visitors(
                site_id="CDBUGS",
                detailed=False,
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/current_visitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"site_id": site_id, "detailed": detailed},
                    report_current_visitors_params.ReportCurrentVisitorsParams,
                ),
            ),
            cast_to=NoneType,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.aggregation = to_raw_response_wrapper(
            reports.aggregation,
        )
        self.current_visitors = to_raw_response_wrapper(
            reports.current_visitors,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.aggregation = async_to_raw_response_wrapper(
            reports.aggregation,
        )
        self.current_visitors = async_to_raw_response_wrapper(
            reports.current_visitors,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.aggregation = to_streamed_response_wrapper(
            reports.aggregation,
        )
        self.current_visitors = to_streamed_response_wrapper(
            reports.current_visitors,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.aggregation = async_to_streamed_response_wrapper(
            reports.aggregation,
        )
        self.current_visitors = async_to_streamed_response_wrapper(
            reports.current_visitors,
        )
