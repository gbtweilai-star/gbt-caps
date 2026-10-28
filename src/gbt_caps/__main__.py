"""Allow ``python -m gbt_caps ...`` as an alias for the ``gbt-caps`` script."""

from __future__ import annotations

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
