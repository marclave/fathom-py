# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EventDeleteByNameParams"]


class EventDeleteByNameParams(TypedDict, total=False):
    name: Required[str]
    """
    The name of the event you wish to delete.
    Example: `Purchase early access`
    """
