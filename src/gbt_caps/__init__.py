"""``gbt-caps`` — the capability atlas of a 341-bit agent framework, as a library.

    from gbt_caps import lookup, by_domain, search, stats, validate

    lookup("vision_loop").gated          # True  → needs a human signature
    [c.name for c in by_domain("engine")]  # 10 bits
    len(search("授权"))                   # full-text over desc + name + handler
    stats()["caps"]                      # 341
    validate()                           # [] when the snapshot is coherent

The snapshot is data, not code: nothing here imports the framework that
implements the bits, so the atlas works on a machine with none of it installed.
"""

from __future__ import annotations

from .spec import (
    CapSpec,
    UnknownCap,
    all_caps,
    by_domain,
    domains,
    errors,
    gated_caps,
    get,
    lookup,
    search,
    snapshot,
    stats,
    validate,
)

__version__ = "0.1.0"

__all__ = [
    "CapSpec",
    "UnknownCap",
    "all_caps",
    "by_domain",
    "domains",
    "errors",
    "gated_caps",
    "get",
    "lookup",
    "search",
    "snapshot",
    "stats",
    "validate",
    "__version__",
]
