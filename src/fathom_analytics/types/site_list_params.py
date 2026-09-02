# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SiteListParams"]


class SiteListParams(TypedDict, total=False):
    limit: int
    """A limit on the number of objects to be returned, between 1 and 100."""

    starting_after: str
    """A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For example, if you make a list request and receive 10 objects ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` to fetch the next page."""

    ending_before: str
    """A cursor for use in pagination, working in the opposite direction to `starting_after`. `ending_before` is an object ID that defines your place in the list."""
