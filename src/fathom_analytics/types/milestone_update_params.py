# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MilestoneUpdateParams"]


class MilestoneUpdateParams(TypedDict, total=False):
    site_id: Required[str]
    """
    The ID of the site. This is the same string you use in your tracking code.
    Example: `CDBUGS`
    """

    name: Required[str]
    """The name of the milestone (up to 30 characters)."""

    milestone_date: Required[str]
    """The date of the milestone in `YYYY-MM-DD` format."""
