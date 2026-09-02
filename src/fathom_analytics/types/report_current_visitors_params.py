# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReportCurrentVisitorsParams"]


class ReportCurrentVisitorsParams(TypedDict, total=False):
    site_id: Required[str]
    """
    The `id` of the site.
    Example: `CDBUGS`
    """

    detailed: bool
    """Set to `true` for a detailed breakdown of pages and referrers. Otherwise you'll only get a count."""
