from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `fathom_analytics.resources` module.

    This is used so that we can lazily import `fathom_analytics.resources` only when
    needed *and* so that users can just import `fathom_analytics` and reference `fathom_analytics.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("fathom_analytics.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
