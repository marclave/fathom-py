# Fathom Analytics Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Account`](#account)
  - [Get account](#get-account)
  - [Get token](#get-token)
- [`Sites`](#sites)
  - [List sites](#list-sites)
  - [Create site](#create-site)
  - [Get site](#get-site)
  - [Update site](#update-site)
  - [Delete site](#delete-site)
  - [Wipe site](#wipe-site)
- [`Events`](#events)
  - [List events](#list-events)
  - [Delete event](#delete-event)
  - [Create event](#create-event)
  - [Set event currency](#set-event-currency)
  - [Get event](#get-event)
  - [Update event](#update-event)
  - [Delete event](#delete-event-1)
  - [Wipe event](#wipe-event)
- [`Milestones`](#milestones)
  - [List milestones](#list-milestones)
  - [Create milestone](#create-milestone)
  - [Get milestone](#get-milestone)
  - [Update milestone](#update-milestone)
  - [Delete milestone](#delete-milestone)
- [`Reports`](#reports)
  - [Aggregation](#aggregation)
  - [Current visitors](#current-visitors)

## Setup

```python
import os

from fathom_analytics import FathomAnalyticsAPI

client = FathomAnalyticsAPI(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

## `Account`

Information about the account and token behind your API key.

### Get account

Retrieve information about the account that owns the API key.

**Permissions:** Requires a token with full account access (the `*` scope).

**Returns:** An account object.

```python
client.account.list()
```

### Get token

Retrieve metadata about the API token used to make the request, including its name, permissions (abilities), token-format version and timestamps. Your secret token value is never returned.

**Permissions:** Any valid API token.

**Returns:** A token object.

```python
client.account.list_token()
```

## `Sites`

Create and manage the sites in your Fathom account.

### List sites

Return a list of all sites this API key owns. Sites are sorted by `created_at` ascending to allow you to paginate with ease.

**Permissions:** Requires read access to all sites (`all-sites-readonly`) or full account access.

**Returns:** A list of site objects.

| Direction | Type |
| --- | --- |
| Request | [`SiteListParams`](./src/fathom_analytics/types/site_list_params.py) |

```python
client.sites.list(
    limit=10,
)
```

### Create site

Create a site.

**Permissions:** Requires full account access (`*`).

**Returns:** A site object.

| Direction | Type |
| --- | --- |
| Request | [`SiteCreateParams`](./src/fathom_analytics/types/site_create_params.py) |

```python
client.sites.create(
    name="Bugs Bunny Portfolio",
    sharing="none",
    multi_domain=False,
)
```

### Get site

Return a single site.

**Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

**Returns:** A site object.

```python
client.sites.retrieve(
    site_id="CDBUGS",
)
```

### Update site

Update a site. Send only the fields you want to change.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

**Returns:** A site object.

| Direction | Type |
| --- | --- |
| Request | [`SiteUpdateParams`](./src/fathom_analytics/types/site_update_params.py) |

```python
client.sites.update(
    site_id="CDBUGS",
)
```

### Delete site

Delete a site. Careful: you can't undo this, and neither can we.

**Permissions:** Requires full account access (`*`).

**Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

```python
client.sites.delete(
    site_id="CDBUGS",
)
```

### Wipe site

Previously wiped all pageviews and event completions from a website. This endpoint is no longer available.

```python
client.sites.wipe(
    site_id="CDBUGS",
)
```

## `Events`

Manage events for a site.

### List events

Return a list of all events this site owns. Events are sorted by `created_at` ascending to allow you to paginate with ease.

**Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

**Returns:** A list of event objects.

> **The id field is going away:** Each event still returns an `id` (the old goal code). We are removing that field on 24 September 2026. Identify events by `name` instead.

> The `currency` field is returned as `null` on list responses. Set it with [Set event currency](#set-event-currency).

| Direction | Type |
| --- | --- |
| Request | [`EventListParams`](./src/fathom_analytics/types/event_list_params.py) |

```python
client.events.list(
    site_id="CDBUGS",
    limit=10,
)
```

### Delete event

Delete an event by its name. If more than one event row shares the name, they are treated as one event and every matching row is deleted.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

**Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

| Direction | Type |
| --- | --- |
| Request | [`EventDeleteByNameParams`](./src/fathom_analytics/types/event_delete_by_name_params.py) |

```python
client.events.delete_by_name(
    site_id="CDBUGS",
    name="Purchase early access",
)
```

### Create event

Previously created an event. This endpoint is no longer available.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

| Direction | Type |
| --- | --- |
| Request | [`EventCreateParams`](./src/fathom_analytics/types/event_create_params.py) |

```python
client.events.create(
    site_id="CDBUGS",
    name="Purchase early access",
    currency="dollar",
)
```

### Set event currency

Set the currency of an event by its name. Use this instead of updating an event by its goal code. If more than one event row shares the name, they are treated as one event and every matching row is updated.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

**Returns:** Returns an updated object on success. Otherwise, this call returns an error.

| Direction | Type |
| --- | --- |
| Request | [`EventSetCurrencyParams`](./src/fathom_analytics/types/event_set_currency_params.py) |

```python
client.events.set_currency(
    site_id="CDBUGS",
    name="Purchase early access",
    currency="pound",
)
```

### Get event

Previously returned a single event by its goal code. This endpoint is no longer available.

**Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

```python
client.events.retrieve(
    site_id="CDBUGS",
    event_id="ABCDEFGH",
)
```

### Update event

Previously updated an event by its goal code. This endpoint is no longer available.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

| Direction | Type |
| --- | --- |
| Request | [`EventUpdateParams`](./src/fathom_analytics/types/event_update_params.py) |

```python
client.events.update(
    site_id="CDBUGS",
    event_id="ABCDEFGH",
)
```

### Delete event

Previously deleted an event by its goal code. This endpoint is no longer available.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

```python
client.events.delete(
    site_id="CDBUGS",
    event_id="ABCDEFGH",
)
```

### Wipe event

Previously wiped all completion data belonging to an event. This endpoint is no longer available.

```python
client.events.wipe(
    site_id="CDBUGS",
    event_id="ABCDEFGH",
)
```

## `Milestones`

Annotate your reports with important dates.

### List milestones

Return a list of all milestones this site owns. Milestones are sorted by `created_at` ascending to allow you to paginate with ease.

**Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

**Returns:** A list of milestone objects.

| Direction | Type |
| --- | --- |
| Request | [`MilestoneListParams`](./src/fathom_analytics/types/milestone_list_params.py) |

```python
client.milestones.list(
    site_id="CDBUGS",
    limit=10,
)
```

### Create milestone

Create a milestone. Returns HTTP `201 Created` on success.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

**Returns:** A milestone object.

| Direction | Type |
| --- | --- |
| Request | [`MilestoneCreateParams`](./src/fathom_analytics/types/milestone_create_params.py) |

```python
client.milestones.create(
    site_id="CDBUGS",
    name="Website Redesign Launch",
    milestone_date="2024-01-15",
)
```

### Get milestone

Return a single milestone.

**Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

**Returns:** A milestone object.

```python
client.milestones.retrieve(
    site_id="CDBUGS",
    milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
)
```

### Update milestone

Update a milestone. Both `name` and `milestone_date` are required.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

**Returns:** A milestone object.

| Direction | Type |
| --- | --- |
| Request | [`MilestoneUpdateParams`](./src/fathom_analytics/types/milestone_update_params.py) |

```python
client.milestones.update(
    site_id="CDBUGS",
    milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
    name="Website Redesign Launch v2",
    milestone_date="2024-01-20",
)
```

### Delete milestone

Delete a milestone. Careful: you can't undo this, and neither can we.

**Permissions:** Requires write access to the site (`manage:{site_id}`).

**Returns:** Returns a deleted object on success. Otherwise, this call returns an error.

```python
client.milestones.delete(
    site_id="CDBUGS",
    milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
)
```

## `Reports`

Custom reports across your traffic, events and sources.

### Aggregation

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

| Direction | Type |
| --- | --- |
| Request | [`ReportAggregationParams`](./src/fathom_analytics/types/report_aggregation_params.py) |

```python
client.reports.aggregation(
    entity="pageview",
    aggregates="pageviews",
)
```

### Current visitors

Returns the total number of current visitors on a site. The detailed view also returns the top 150 pages and top 150 referrers.

**Permissions:** Requires read access to the site (`all-sites-readonly`, `read:{site_id}` or `manage:{site_id}`).

**Returns:** The current visitor count, with an optional detailed breakdown.

| Direction | Type |
| --- | --- |
| Request | [`ReportCurrentVisitorsParams`](./src/fathom_analytics/types/report_current_visitors_params.py) |

```python
client.reports.current_visitors(
    site_id="CDBUGS",
    detailed=False,
)
```
