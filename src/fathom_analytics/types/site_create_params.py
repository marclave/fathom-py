# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SiteCreateParams"]


class SiteCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The name of the website. Any string (up to 255 characters) is acceptable, and it doesn't have to match the website URL.
    Example: `Daffy's Website`
    """

    sharing: Literal["none", "private", "public"]
    """The sharing configuration. Supported values are `none`, `private` or `public`."""

    share_password: str
    """
    When sharing is set to `private`, you must also send a password to access the site with (up to 255 characters).
    
    **Required if sharing is private.**
    """

    timezone: str
    """The site's reporting timezone as a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g. `America/New_York`). If omitted, the site inherits your account's default timezone."""

    multi_domain: bool
    """Set to `true` to allow this site to track multiple domains."""

    multi_domain_option: Literal["combined", "separate"]
    """
    How multi-domain data is grouped. Supported values are `combined` (report all domains together) or `separate` (report each domain individually).
    
    **Required if multi_domain is true.**
    """
