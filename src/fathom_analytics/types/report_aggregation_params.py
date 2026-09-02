# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReportAggregationParams"]


class ReportAggregationParams(TypedDict, total=False):
    entity: Required[Literal["pageview", "event"]]
    """The entity you want to report on. Events are treated separately from pageviews. Supported values: `pageview` and `event`."""

    entity_id: str
    """
    When `entity` is `pageview`, this is the `id` of the site you want to aggregate on. When `entity` is `event`, do not pass a goal code here. Use `site_id` and `entity_name` instead. Pageview usage is unchanged.
    
    **Required when entity is "pageview".**
    """

    site_id: str
    """
    The `id` of the site the event belongs to.
    
    **Required when entity is "event" and entity_id is omitted.**
    """

    entity_name: str
    """
    The name of the event you want to report on. Example: `purchase`.
    
    **Required when entity is "event" and entity_id is omitted.**
    """

    aggregates: Required[str]
    """
    The aggregates you wish to include, separated by a comma.
    
    Supported values for **pageview** entities: `visits`, `uniques`, `pageviews`, `avg_duration` and `bounce_rate`. The difference between "visits" and "uniques" is that visits are unique site visits whilst uniques are unique page visits.
    
    Supported values for **event** entities: `conversions`, `unique_conversions` and `value` (value is returned in cents).
    """

    date_grouping: Literal["hour", "day", "month", "year"]
    """By default, we don't do any date grouping and return total aggregations. Override this with `hour`, `day`, `month` or `year`. Note: `hour` grouping is only supported for date ranges of up to 7 days."""

    field_grouping: str
    """The fields you want to group by, separated by a comma (e.g. `hostname,pathname`). Supported values: `hostname`, `pathname`, `entry_page`, `exit_page`, `referrer_hostname`, `referrer_pathname`, `referrer_source`, `browser`, `country_code`, `city`, `state`, `region`, `device_type`, `operating_system`, `utm_campaign`, `utm_content`, `utm_medium`, `utm_source`, `utm_term`, `keyword` and `ref`."""

    sort_by: str
    """
    The field you want to sort by, in the format `field:asc|desc`. You can use any field present in `aggregates` or `field_grouping`. When using `date_grouping`, you can also sort by `timestamp:asc` or `timestamp:desc`.
    Example: `pageviews:desc`
    """

    date_from: str
    """Timestamp (e.g. `2022-04-01 15:31:00`). Should match the timezone you're reporting in. Defaults to the entity's first recorded data."""

    date_to: str
    """Timestamp (e.g. `2022-04-01 15:31:00`). Should match the timezone you're reporting in. Default: now."""

    timezone: str
    """**Deprecated.** We now report using each site's configured timezone by default. If provided, this [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) overrides the site's timezone for this request. We'll be removing this parameter in the future."""

    limit: int
    """
    Optional integer from `1` to `1000` inclusive.
    
    **Default.** When `field_grouping` is set and you omit `limit`, we return at most 500 rows. When `field_grouping` is omitted, there is no default row cap. `date_grouping` alone does not trigger the 500 default.
    
    **Maximum.** A `limit` above 1000 returns HTTP 400 with an `errors.limit` validation message. There is no pagination on this endpoint, so you cannot walk past 1000 grouped rows with a cursor. Narrow the result with `filters` and/or a shorter `date_from` / `date_to`, then issue more requests.
    """

    filters: str
    """A JSON-encoded array of filter objects. See the filtering reference below for the full list of supported properties and operators. Each filter's `value` must be a string."""
