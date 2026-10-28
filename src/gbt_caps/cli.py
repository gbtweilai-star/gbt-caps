"""``gbt-caps`` CLI — query 341 capability specs from a terminal.

    gbt-caps stats                     totals and per-domain rollup
    gbt-caps list                      every bit, one line each
    gbt-caps list --gated              only the ones that need a human
    gbt-caps domain engine             one domain
    gbt-caps show vision_loop          full spec for one bit
    gbt-caps show vision_loop --json   machine-readable
    gbt-caps search 授权 --limit 10     full-text search
    gbt-caps check                     contract validation, exit 1 on error
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional

from . import __version__, spec


def _json(obj) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=False))


def cmd_stats(args: argparse.Namespace) -> int:
    s = spec.stats()
    if args.json:
        _json(s)
        return 0
    print(f"caps     {s['caps']}")
    print(f"domains  {s['domains']}")
    print(f"gated    {s['gated_by_safety_flag']}  (safe: false — needs a human)")
    print(f"multi-op {s['multi_op']}  (description enumerates operations)")
    print(f"params   {s['needs_params']}")
    print(f"external {s['needs_external']}")
    src = s.get("source") or {}
    if src.get("file"):
        print(f"source   {src['file']}  sha256 {str(src.get('sha256', ''))[:12]}")
    print()
    for d, info in sorted(s["per_domain"].items(), key=lambda x: (-x[1]["caps"], x[0])):
        print(f"  {d:<14} {info['caps']:>3} caps · {info['gated']:>2} gated · {info['multi_op']:>3} multi-op")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    caps = spec.gated_caps() if args.gated else spec.all_caps()
    if args.domain:
        caps = [c for c in caps if c.domain == args.domain]
    if args.json:
        _json([c.as_dict() for c in caps])
        return 0
    for c in caps:
        print(str(c))
    print(f"\n{len(caps)} capability bit(s)")
    return 0


def cmd_domains(args: argparse.Namespace) -> int:
    s = spec.stats()
    if args.json:
        _json(s["per_domain"])
        return 0
    for d, info in sorted(s["per_domain"].items(), key=lambda x: (-x[1]["caps"], x[0])):
        print(f"{d:<14} {info['caps']:>3}")
    print(f"\n{s['domains']} domains · {s['caps']} caps")
    return 0


def cmd_domain(args: argparse.Namespace) -> int:
    caps = spec.by_domain(args.name)
    if not caps:
        print(f"error: unknown domain {args.name!r}; known: {', '.join(spec.domains())}",
              file=sys.stderr)
        return 2
    if args.json:
        _json([c.as_dict() for c in caps])
        return 0
    print(f"# {args.name} · {len(caps)} bits\n")
    for c in caps:
        print(f"  {str(c)}")
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    try:
        cap = spec.lookup(args.name)
    except spec.UnknownCap as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        _json(cap.as_dict())
        return 0
    print(f"{cap.name}")
    print(f"  domain     {cap.domain}")
    print(f"  handler    {cap.handler or '—'}")
    print(f"  safe       {str(cap.safe).lower()}" + ("" if cap.safe else "   ← needs a human"))
    print(f"  external   {str(cap.external).lower()}")
    print(f"  params     {', '.join(cap.params) or '—'}")
    if cap.params_hint:
        print(f"  hint       {cap.params_hint}")
    print(f"  shape      {'multi-op' if cap.multi_op else 'single action'}")
    if cap.ops:
        print(f"  ops        {' / '.join(cap.ops)}")
    print()
    print(cap.desc or "(no description)")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    hits = spec.search(args.query, domain=args.domain, limit=args.limit)
    if args.json:
        _json([c.as_dict() for c in hits])
        return 0
    for c in hits:
        print(f"{str(c)}\n    {c.summary}")
    print(f"\n{len(hits)} hit(s)")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    issues = spec.validate()
    bad = [i for i in issues if i["level"] == "error"]
    warns = [i for i in issues if i["level"] == "warn"]
    if args.json:
        _json(issues)
    else:
        for i in issues:
            print(f"{i['level']:<5} {i['code']:<32} {i['detail']}")
        head = "ok" if not bad else "FAILED"
        print(f"\n{head} · {spec.stats()['caps']} caps · "
              f"{len(bad)} error(s) · {len(warns)} warning(s)")
    return 1 if bad else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="gbt-caps",
        description="Query the 341-bit capability atlas.",
        epilog="Specs live in caps/<domain>/<name>.md; this CLI reads the same snapshot.",
    )
    p.add_argument("--version", action="version", version=f"gbt-caps {__version__}")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    sub = p.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", default=argparse.SUPPRESS,
                        help=argparse.SUPPRESS)

    s = sub.add_parser("stats", parents=[common], help="totals and per-domain rollup")
    s.set_defaults(func=cmd_stats)

    ls = sub.add_parser("list", parents=[common], help="list capability bits")
    ls.add_argument("--gated", action="store_true", help="only safe: false bits")
    ls.add_argument("--domain", default=None, help="restrict to one domain")
    ls.set_defaults(func=cmd_list)

    ds = sub.add_parser("domains", parents=[common], help="list domains")
    ds.set_defaults(func=cmd_domains)

    d = sub.add_parser("domain", parents=[common], help="list one domain's bits")
    d.add_argument("name")
    d.set_defaults(func=cmd_domain)

    sh = sub.add_parser("show", parents=[common], help="show one capability spec")
    sh.add_argument("name")
    sh.set_defaults(func=cmd_show)

    se = sub.add_parser("search", parents=[common], help="full-text search")
    se.add_argument("query")
    se.add_argument("--domain", default=None)
    se.add_argument("--limit", type=int, default=20)
    se.set_defaults(func=cmd_search)

    ck = sub.add_parser("check", parents=[common], help="validate the snapshot contract")
    ck.set_defaults(func=cmd_check)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
