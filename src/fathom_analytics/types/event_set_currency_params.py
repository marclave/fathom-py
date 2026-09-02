# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventSetCurrencyParams"]


class EventSetCurrencyParams(TypedDict, total=False):
    name: Required[str]
    """
    The name of the event (up to 255 characters).
    Example: `Purchase early access`
    """

    currency: Required[
        Literal[
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
    ]
    """The currency used for any value attached to this event's completions."""
