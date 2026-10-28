#!/usr/bin/env python3
"""Export a capability registry to a portable JSON snapshot — by parsing, never importing.

Why AST instead of ``import caps_registry``:

* importing a framework package runs module-level side effects (creating stores,
  reading env, opening sockets) — a documentation tool must not do that;
* the registry is a data table, and data tables can be read statically;
* it works on a machine that does not have the framework's dependencies installed.

Usage::

    python tools/export_registry.py path/to/caps_registry.py -o src/gbt_caps/data/registry.json
    python tools/export_registry.py path/to/caps_registry.py --check    # drift check only

``ast.literal_eval`` is not enough: ``desc`` fields are built with ``"a" + "b"``
string concatenation, which raises ``ValueError: malformed node or string``. So we
walk the tree ourselves and evaluate only the node types a data table can contain.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1


class LiteralError(TypeError):
    """A node type that cannot appear in a literal data table."""


def literal(node: ast.AST) -> Any:
    """Evaluate a literal-ish AST node without executing anything.

    Supports exactly what a data table can contain: constants, containers, string
    concatenation, ``%``-formatting of a literal string, and negation. Anything
    else is refused rather than guessed.
    """
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Dict):
        return {literal(k): literal(v) for k, v in zip(node.keys, node.values)}
    if isinstance(node, ast.List):
        return [literal(e) for e in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(literal(e) for e in node.elts)
    if isinstance(node, ast.Set):
        return {literal(e) for e in node.elts}
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left, right = literal(node.left), literal(node.right)
        if isinstance(left, str) and isinstance(right, str):
            return left + right
        raise LiteralError("only string + string concatenation is supported")
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
        # '... %d ...' % 3 — a literal format string applied to literal arguments.
        template, args = literal(node.left), literal(node.right)
        if isinstance(template, str) and isinstance(args, (str, int, float, tuple)):
            try:
                return template % (args,)
            except (TypeError, ValueError) as exc:
                raise LiteralError(f"bad %-format: {exc}") from exc
        raise LiteralError("only str % literal is supported")
    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant):
                parts.append(str(value.value))
            elif isinstance(value, ast.FormattedValue) and value.format_spec is None:
                parts.append(str(literal(value.value)))
            else:
                raise LiteralError("f-string with non-constant parts")
        return "".join(parts)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        operand = literal(node.operand)
        if isinstance(operand, (int, float)):
            return -operand
    raise LiteralError(f"unsupported node {type(node).__name__}")


def collect_tables(tree: ast.Module) -> dict:
    """Every module-level ``NAME = <literal>`` assignment."""
    tables = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name):
                try:
                    tables[target.id] = literal(node.value)
                except LiteralError:
                    continue
    return tables


_OP_ASSIGN = re.compile(r"(?<![A-Za-z])op\s*=")
_SLASH_LIST = re.compile(r"\b[a-z][a-z0-9_]{1,}(?:/[a-z][a-z0-9_]{1,}){2,}\b")


def detect_multi_op(entry: dict, param_meta: dict) -> tuple:
    """A bit is "multi-op" when one name dispatches to several operations.

    Three signals, all textual and all cheap to verify by eye:

    * the parameter contract asks for an ``op`` / ``action`` argument;
    * the description writes ``op=...`` (matched with a left word boundary — a
      naive ``"op=" in text`` also fires on ``loop=`` and ``desktop=``);
    * the description enumerates operations as a slash list, e.g.
      ``create/enter/define_plan/get_plan``.

    Returns ``(is_multi_op, hint, ops)`` where ``ops`` is the enumerated list when
    one was found, else ``[]``. This is a *reading of the text*, not a fact from
    the registry — the generated docs say so.
    """
    hint = (str(param_meta.get("hint") or "") + " " + str(entry.get("params_hint") or "")).strip()
    desc = str(entry.get("desc") or "")
    params = [str(p) for p in (list(param_meta.get("params") or []) + list(entry.get("params") or []))]
    blob = f"{hint} {desc}"

    ops: list = []
    found = _SLASH_LIST.search(blob)
    if found:
        ops = found.group(0).split("/")

    multi = (
        bool(_OP_ASSIGN.search(blob))
        or any(p in ("op", "action") for p in params)
        or len(ops) >= 3
    )
    return multi, hint, ops


def normalize(benign: dict, param_required: dict, source_name: str,
              source_sha: str) -> dict:
    caps = {}
    for name in sorted(benign):
        entry = benign[name] if isinstance(benign[name], dict) else {}
        meta = param_required.get(name) or {}
        params = list(meta.get("params") or entry.get("params") or [])
        hint = str(meta.get("hint") or entry.get("params_hint") or "")
        multi_op, ops_hint, ops = detect_multi_op(entry, meta)
        caps[name] = {
            "name": name,
            "domain": str(entry.get("domain") or "unclassified"),
            "desc": str(entry.get("desc") or "").strip(),
            "handler": str(entry.get("handler") or ""),
            "safe": bool(entry.get("safe", True)),
            "external": bool(entry.get("external")),
            "requires_params": bool(params),
            "params": params,
            "params_hint": hint,
            "multi_op": multi_op,
            "ops_hint": ops_hint,
            "ops": ops,
        }

    domains: dict = {}
    for cap in caps.values():
        d = domains.setdefault(cap["domain"], {"name": cap["domain"], "count": 0,
                                               "caps": []})
        d["count"] += 1
        d["caps"].append(cap["name"])

    return {
        "schema": SCHEMA_VERSION,
        "source": {"file": source_name, "sha256": source_sha},
        "totals": {
            "caps": len(caps),
            "domains": len(domains),
            "gated_by_safety_flag": sum(1 for c in caps.values() if not c["safe"]),
            "needs_external": sum(1 for c in caps.values() if c["external"]),
            "needs_params": sum(1 for c in caps.values() if c["requires_params"]),
            "multi_op": sum(1 for c in caps.values() if c["multi_op"]),
        },
        "domains": {k: {"count": v["count"], "caps": sorted(v["caps"])}
                    for k, v in sorted(domains.items())},
        "caps": caps,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Export a caps registry via AST.")
    ap.add_argument("registry", type=Path, help="path to caps_registry.py")
    ap.add_argument("-o", "--out", type=Path, default=None, help="output JSON path")
    ap.add_argument("--check", action="store_true",
                    help="compare against --out and exit 1 on drift")
    args = ap.parse_args(argv)

    raw = args.registry.read_bytes()
    tree = ast.parse(raw.decode("utf-8"))
    tables = collect_tables(tree)
    benign = tables.get("BENIGN_CAPS")
    if not isinstance(benign, dict):
        print("error: BENIGN_CAPS not found as a literal dict", file=sys.stderr)
        return 2

    snapshot = normalize(benign, tables.get("PARAM_REQUIRED") or {},
                         args.registry.name, hashlib.sha256(raw).hexdigest())

    if args.check:
        if args.out is None or not args.out.exists():
            print("error: --check needs an existing -o file", file=sys.stderr)
            return 2
        current = json.loads(args.out.read_text(encoding="utf-8"))
        a = current.get("caps", {})
        b = snapshot["caps"]
        added = sorted(set(b) - set(a))
        removed = sorted(set(a) - set(b))
        changed = sorted(k for k in set(a) & set(b) if a[k] != b[k])
        if added or removed or changed:
            print(f"drift: +{len(added)} -{len(removed)} ~{len(changed)}", file=sys.stderr)
            for label, names in (("added", added), ("removed", removed), ("changed", changed)):
                if names:
                    print(f"  {label}: {', '.join(names[:20])}", file=sys.stderr)
            return 1
        print(f"no drift · {len(b)} caps")
        return 0

    text = json.dumps(snapshot, ensure_ascii=False, indent=1, sort_keys=False) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        t = snapshot["totals"]
        print(f"wrote {args.out} · {t['caps']} caps / {t['domains']} domains")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
