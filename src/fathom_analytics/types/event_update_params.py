# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventUpdateParams"]


class EventUpdateParams(TypedDict, total=False):
    site_id: Required[str]
    """
    The ID of the site. This is the same string you use in your tracking code.
    Example: `CDBUGS`
    """

    name: str
    """The name of the event (up to 255 characters)."""

    currency: Literal[
        "dollar",
        "pound",
        "euro",
        "yuan",
        "peso",
        "shekel",
        "yen",
        "won",
        "hryvnia",
        "franc",
        "rupee",
        "integer",
        "none",
    ]
    """The currency used for any value attached to this event's completions."""
