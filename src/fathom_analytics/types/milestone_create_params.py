# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MilestoneCreateParams"]


class MilestoneCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the milestone (up to 30 characters)."""

    milestone_date: Required[str]
    """The date of the milestone in `YYYY-MM-DD` format."""
