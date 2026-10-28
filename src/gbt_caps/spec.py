"""Spec objects and the query surface over the capability registry snapshot.

The snapshot is a plain JSON file committed at ``data/registry.json``. Nothing
here imports the framework the capabilities belong to — the atlas is readable on
a machine that has no part of that framework installed.
"""

from __future__ import annotations

import difflib
import json
import re
from dataclasses import dataclass, field
from functools import lru_cache
from importlib import resources
from typing import Dict, Iterable, List, Optional, Sequence

SNAKE = re.compile(r"^[a-z][a-z0-9_]*$")


class UnknownCap(KeyError):
    """Raised by :func:`lookup` for a name that is not in the registry."""

    def __init__(self, name: str, suggestions: Sequence[str] = ()) -> None:
        self.name = name
        self.suggestions = list(suggestions)
        msg = f"no capability named {name!r}"
        if self.suggestions:
            msg += "; did you mean: " + ", ".join(self.suggestions)
        super().__init__(msg)


@dataclass(frozen=True)
class CapSpec:
    """One capability bit, exactly as the registry declares it."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: List[str] = field(default_factory=list)
    params_hint: str = ""
    multi_op: bool = False
    ops_hint: str = ""
    ops: List[str] = field(default_factory=list)

    @property
    def gated(self) -> bool:
        """True when the registry does *not* mark this bit safe."""
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description — for one-line listings."""
        head = self.desc.split("：")[0].split("。")[0]
        return (head or self.desc)[:80]

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops_hint": self.ops_hint,
            "ops": list(self.ops),
        }

    def __str__(self) -> str:  # pragma: no cover - convenience
        flags = []
        if self.gated:
            flags.append("gated")
        if self.multi_op:
            flags.append("multi-op")
        if self.params:
            flags.append("params:" + ",".join(self.params))
        tail = f"  [{'; '.join(flags)}]" if flags else ""
        return f"{self.name:<28} {self.domain:<14}{tail}"


def _raw() -> dict:
    text = resources.files("gbt_caps").joinpath("data/registry.json").read_text(encoding="utf-8")
    return json.loads(text)


@lru_cache(maxsize=1)
def snapshot() -> dict:
    """The whole snapshot, parsed once."""
    return _raw()


@lru_cache(maxsize=1)
def _index() -> Dict[str, CapSpec]:
    out = {}
    for name, row in snapshot()["caps"].items():
        out[name] = CapSpec(
            name=row["name"],
            domain=row["domain"],
            desc=row["desc"],
            handler=row["handler"],
            safe=bool(row["safe"]),
            external=bool(row["external"]),
            requires_params=bool(row["requires_params"]),
            params=list(row.get("params") or []),
            params_hint=row.get("params_hint") or "",
            multi_op=bool(row.get("multi_op")),
            ops_hint=row.get("ops_hint") or "",
            ops=list(row.get("ops") or []),
        )
    return out


def all_caps() -> List[CapSpec]:
    """Every capability bit, sorted by name."""
    return [_index()[k] for k in sorted(_index())]


def lookup(name: str) -> CapSpec:
    """One capability by exact name. Raises :class:`UnknownCap` with near misses."""
    idx = _index()
    if name in idx:
        return idx[name]
    close = difflib.get_close_matches(name, list(idx), n=5, cutoff=0.6)
    raise UnknownCap(name, close)


def get(name: str, default: Optional[CapSpec] = None) -> Optional[CapSpec]:
    """Like :func:`lookup` but returns ``default`` instead of raising."""
    try:
        return lookup(name)
    except UnknownCap:
        return default


def domains() -> List[str]:
    return sorted(snapshot()["domains"])


def by_domain(domain: str) -> List[CapSpec]:
    """Every bit in one domain. Unknown domains return an empty list."""
    idx = _index()
    return [idx[n] for n in snapshot()["domains"].get(domain, {}).get("caps", []) if n in idx]


def search(query: str, *, domain: Optional[str] = None,
           limit: Optional[int] = None) -> List[CapSpec]:
    """Case-insensitive substring search over name, description and handler."""
    q = query.strip().lower()
    if not q:
        return []
    hits = []
    for cap in all_caps():
        if domain and cap.domain != domain:
            continue
        haystack = " ".join((cap.name, cap.desc, cap.handler, cap.params_hint)).lower()
        if q in haystack:
            hits.append(cap)
    hits.sort(key=lambda c: (not c.name.lower().startswith(q), c.name))
    return hits[:limit] if limit else hits


def gated_caps() -> List[CapSpec]:
    """Bits the registry marks ``safe: false`` — the ones that need a human."""
    return [c for c in all_caps() if c.gated]


def stats() -> dict:
    """Snapshot totals plus a per-domain rollup."""
    snap = snapshot()
    per_domain = {
        d: {
            "caps": info["count"],
            "gated": sum(1 for n in info["caps"] if not snap["caps"][n]["safe"]),
            "multi_op": sum(1 for n in info["caps"] if snap["caps"][n]["multi_op"]),
        }
        for d, info in snap["domains"].items()
    }
    return {**snap["totals"], "source": snap.get("source", {}), "per_domain": per_domain}


# --------------------------------------------------------------------------- #
# contract validation — the part that earns its keep in CI
# --------------------------------------------------------------------------- #

def validate(snap: Optional[dict] = None) -> List[dict]:
    """Check a snapshot against the atlas' own contract.

    Returns a list of ``{"level": "error"|"warn", "code": ..., "detail": ...}``.
    An empty list means the snapshot is coherent. Every check is something a
    human can verify by looking at the data — no heuristics about behaviour.
    """
    snap = snap or snapshot()
    caps = snap.get("caps", {})
    issues: List[dict] = []

    def err(code: str, detail: str) -> None:
        issues.append({"level": "error", "code": code, "detail": detail})

    def warn(code: str, detail: str) -> None:
        issues.append({"level": "warn", "code": code, "detail": detail})

    declared = snap.get("domains", {})
    counted: Dict[str, int] = {}
    for name, row in caps.items():
        if not SNAKE.match(name):
            err("bad_name", f"{name!r} is not snake_case")
        if not str(row.get("desc") or "").strip():
            err("missing_desc", f"{name} has no description")
        if not row.get("domain"):
            err("missing_domain", f"{name} has no domain")
        if row.get("multi_op") and not any(p in ("op", "action") for p in row.get("params") or []):
            warn("multi_op_without_selector",
                 f"{name} reads as multi-op but declares no op/action parameter")
        if row.get("requires_params") and not row.get("params"):
            err("params_flag_without_params", f"{name} sets requires_params but lists none")
        if row.get("params") and not str(row.get("params_hint") or "").strip():
            warn("params_without_hint", f"{name} declares params with no hint")
        counted[row.get("domain", "")] = counted.get(row.get("domain", ""), 0) + 1

    for domain, n in counted.items():
        got = declared.get(domain, {}).get("count")
        if got != n:
            err("domain_count_mismatch", f"{domain}: index says {got}, registry has {n}")
        listed = set(declared.get(domain, {}).get("caps") or [])
        actual = {k for k, v in caps.items() if v.get("domain") == domain}
        if listed != actual:
            missing = sorted(actual - listed)[:5]
            extra = sorted(listed - actual)[:5]
            err("domain_membership_mismatch",
                f"{domain}: missing={missing} extra={extra}")

    for domain in declared:
        if domain not in counted:
            err("empty_domain", f"{domain} is indexed but has no caps")

    totals = snap.get("totals", {})
    if totals.get("caps") != len(caps):
        err("total_mismatch", f"totals.caps={totals.get('caps')} but {len(caps)} entries")
    if totals.get("domains") != len(declared):
        err("total_domains_mismatch",
            f"totals.domains={totals.get('domains')} but {len(declared)} domains")

    # A handler shared by two names is legitimate (aliases) but worth surfacing.
    seen: Dict[str, List[str]] = {}
    for name, row in caps.items():
        h = str(row.get("handler") or "")
        if h:
            seen.setdefault(h, []).append(name)
    for handler, names in seen.items():
        if len(names) > 1:
            warn("shared_handler", f"handler {handler!r} serves {len(names)} names: {names[:5]}")

    return issues


def errors(snap: Optional[dict] = None) -> List[dict]:
    return [i for i in validate(snap) if i["level"] == "error"]
