# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SiteUpdateParams"]


class SiteUpdateParams(TypedDict, total=False):
    name: str
    """The name of the website (up to 255 characters)."""

    sharing: Literal["none", "private", "public"]
    """The sharing configuration. Supported values are `none`, `private` or `public`."""

    share_password: str
    """
    When sharing is set to `private`, you must also send a password to access the site with (up to 255 characters).
    
    **Required if sharing is private.**
    """

    timezone: str
    """The site's reporting timezone as a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g. `America/New_York`). Reporting for this site will use this timezone."""

    multi_domain: bool
    """Set to `true` to allow this site to track multiple domains."""

    multi_domain_option: Literal["combined", "separate"]
    """
    How multi-domain data is grouped: `combined` or `separate`.
    
    **Required if multi_domain is true.**
    """
