#!/usr/bin/env python3
"""Generate the capability atlas from ``registry.json``.

One file per capability, plus a domain index and a full index. Everything is
derived from the snapshot — nothing is hand-written per capability, so the docs
cannot drift from the data. If a claim is not in the snapshot, it is not in the
page.

Usage::

    python tools/build_atlas.py                 # write caps/**
    python tools/build_atlas.py --check         # fail if caps/** is stale
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "src" / "gbt_caps" / "data" / "registry.json"
CAPS_DIR = ROOT / "caps"

SECTION_ORDER = ["用途", "使用方式", "参数", "返回", "边界与注意", "出处"]


def load(path: Path = REGISTRY) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# per-capability page
# --------------------------------------------------------------------------- #

def _param_rows(cap: dict) -> str:
    if not cap["params"]:
        if cap["multi_op"]:
            ops = cap.get("ops") or []
            listing = "、".join(f"`{o}`" for o in ops[:12]) if ops else "见「用途」"
            return ("注册表**没有**为这一位登记入参契约，但它是多操作形态："
                    f"实际调用要带 `op` / `action` 选择分支（描述里枚举的是 {listing}）。\n\n"
                    "这是数据源里的一处不一致——规格照实呈现，不做猜测。\n")
        return ("该位不要求入参，空调用即可成立。若实现需要更多上下文，"
                "按描述里的说明补 `payload`。\n")
    rows = ["| 参数 | 必填 | 说明 |", "|---|---|---|"]
    hint = cap.get("params_hint") or ""
    for p in cap["params"]:
        rows.append(f"| `{p}` | 是 | {hint or '见「用途」描述'} |")
    return "\n".join(rows) + "\n"


def _example_payload(cap: dict) -> str:
    pairs = [f"{p!r}: ..." for p in cap["params"]]
    if cap["multi_op"] and not any(p in ("op", "action") for p in cap["params"]):
        pairs.insert(0, "'op': '<见描述>'")
    return "{" + ", ".join(pairs) + "}"


def _shape_line(cap: dict) -> str:
    if not cap["multi_op"]:
        return "一位一动作"
    ops = cap.get("ops") or []
    if ops:
        return "一位多操作（描述中枚举：" + " / ".join(f"`{o}`" for o in ops[:12]) + "）"
    return "一位多操作（入参含 `op` / `action` 选择器）"


def _boundaries(cap: dict) -> str:
    out = []
    if cap["safe"]:
        out.append("- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。"
                   "`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。")
    else:
        out.append("- 注册表把它标为 `safe: false`：属于**要人签字的动作**。"
                   "按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。")
    if cap["external"]:
        out.append("- 声明了 `external`：会触达外部服务或外部模块，需要凭据 / 网络，"
                   "且可能产生费用。缺依赖时应如实报缺口，而不是静默降级。")
    if cap["multi_op"]:
        out.append("- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。")
    if cap["requires_params"]:
        out.append("- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。")
    if not out:
        out.append("- 无附加约束。")
    return "\n".join(out) + "\n"


def render_cap(cap: dict, meta: dict) -> str:
    sha = str(meta.get("source", {}).get("sha256", ""))[:12]
    params = ", ".join(f"`{p}`" for p in cap["params"]) or "无"
    lines = [
        f"# `{cap['name']}`",
        "",
        "| 项目 | 值 |",
        "|---|---|",
        f"| 域 | [`{cap['domain']}`](./README.md) |",
        f"| 安全标记 | `safe: {str(cap['safe']).lower()}` |",
        f"| 外部依赖 | {'需要（见「用途」）' if cap['external'] else '无'} |",
        f"| 入参 | {params} |",
        f"| 形态 | {_shape_line(cap)} |",
        f"| 处理器 | `{cap['handler'] or '未登记'}` |",
        "",
        "## 用途",
        "",
        cap["desc"] or "（注册表未提供描述）",
        "",
        "## 使用方式",
        "",
        "### 1. 查规格（本仓，无需任何依赖）",
        "",
        "```python",
        "from gbt_caps import lookup",
        "",
        f'spec = lookup("{cap["name"]}")',
        "print(spec.desc)",
        "print(spec.params, spec.safe)",
        "```",
        "",
        "```bash",
        f"gbt-caps show {cap['name']}          # 本页内容的终端版",
        f"gbt-caps show {cap['name']} --json   # 给程序用",
        "```",
        "",
        "### 2. 真正调用（需要装上实现该位的框架）",
        "",
        "本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：",
        "",
        "```python",
        "from gbt_allinone import run_task",
        "",
        f'result = run_task("{cap["name"]}", {_example_payload(cap)})',
        "```",
        "",
        "## 参数",
        "",
        _param_rows(cap),
        "## 返回",
        "",
        "统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。"
        "业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。",
        "",
        "## 边界与注意",
        "",
        _boundaries(cap),
        "## 出处",
        "",
        f"- 注册表：`{meta.get('source', {}).get('file', 'caps_registry.py')}` · 域 `{cap['domain']}` · "
        f"handler `{cap['handler'] or '—'}`",
        f"- 快照 schema `{meta.get('schema')}` · 源文件 sha256 前 12 位 `{sha}`",
        "- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。",
        "",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# domain index and full index
# --------------------------------------------------------------------------- #

def render_domain(domain: str, info: dict, caps: dict, meta: dict) -> str:
    names = info["caps"]
    gated = [n for n in names if not caps[n]["safe"]]
    multi = [n for n in names if caps[n]["multi_op"]]
    need = [n for n in names if caps[n]["requires_params"]]
    lines = [
        f"# 域 `{domain}`",
        "",
        f"**{info['count']} 位能力** · 需授权 {len(gated)} · 多操作 {len(multi)} · 需入参 {len(need)}",
        "",
        "| 能力位 | 安全 | 形态 | 入参 | 一句话 |",
        "|---|---|---|---|---|",
    ]
    for n in names:
        c = caps[n]
        one = (c["desc"].split("：")[0] or c["desc"])[:38].replace("|", "\\|")
        lines.append(
            f"| [`{n}`](./{n}.md) | {'safe' if c['safe'] else '**gated**'} "
            f"| {'多操作' if c['multi_op'] else '单动作'} "
            f"| {', '.join(c['params']) or '—'} | {one} |"
        )
    lines += ["", f"返回上级索引：[`caps/`](../README.md)", ""]
    return "\n".join(lines)


def render_caps_readme(meta: dict) -> str:
    caps = meta["caps"]
    domains = meta["domains"]
    t = meta["totals"]
    lines = [
        "# 能力图集 · 341 位",
        "",
        f"**{t['caps']} 位能力 / {t['domains']} 个域** · 需授权 {t['gated_by_safety_flag']} · "
        f"多操作 {t['multi_op']} · 需入参 {t['needs_params']} · 触达外部 {t['needs_external']}",
        "",
        "每位能力一份独立规格文件，可单独引用、单独查询、单独校验。"
        "全部文件由 `tools/build_atlas.py` 从 `src/gbt_caps/data/registry.json` 生成。",
        "",
        "| 域 | 能力位 | 需授权 | 多操作 | 入口 |",
        "|---|---|---|---|---|",
    ]
    for d, info in sorted(domains.items(), key=lambda x: (-x[1]["count"], x[0])):
        names = info["caps"]
        gated = sum(1 for n in names if not caps[n]["safe"])
        multi = sum(1 for n in names if caps[n]["multi_op"])
        lines.append(f"| `{d}` | {info['count']} | {gated} | {multi} | [进入](./{d}/README.md) |")
    lines += [
        "",
        "## 怎么用",
        "",
        "```bash",
        "gbt-caps list                      # 341 位一览",
        "gbt-caps domain vision             # 某个域的全部能力位",
        "gbt-caps show vision_loop          # 单份规格",
        "gbt-caps search 授权               # 全文检索",
        "gbt-caps check                     # 契约自检",
        "```",
        "",
        "Python：",
        "",
        "```python",
        "from gbt_caps import all_caps, lookup, by_domain, search",
        "",
        "len(all_caps())            # 341",
        'lookup("vision_loop").safe  # True',
        'by_domain("engine")        # 该域的全部规格',
        'search("DAG")              # 命中的能力位',
        "```",
        "",
        "完整清单：[`INDEX.md`](./INDEX.md)",
        "",
    ]
    return "\n".join(lines)


def render_index(meta: dict) -> str:
    caps = meta["caps"]
    lines = [
        "# 全量索引 · 341 位",
        "",
        "按域分组，`gated` = `safe: false`（需人工授权）。",
        "",
    ]
    for d, info in sorted(meta["domains"].items()):
        lines += [f"## `{d}` · {info['count']} 位", ""]
        for n in info["caps"]:
            c = caps[n]
            flags = []
            if not c["safe"]:
                flags.append("gated")
            if c["multi_op"]:
                flags.append("multi-op")
            if c["params"]:
                flags.append("params:" + ",".join(c["params"]))
            tag = f" `{'` `'.join(flags)}`" if flags else ""
            one = c["desc"].split("：")[0][:56].replace("|", "\\|")
            lines.append(f"- [`{n}`](./{d}/{n}.md){tag} — {one}")
        lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# driver
# --------------------------------------------------------------------------- #

def build(meta: dict, out_dir: Path = CAPS_DIR) -> dict:
    """Write the atlas. Returns ``{relative_path: content}`` for --check."""
    caps = meta["caps"]
    files = {"README.md": render_caps_readme(meta), "INDEX.md": render_index(meta)}
    for d, info in meta["domains"].items():
        files[f"{d}/README.md"] = render_domain(d, info, caps, meta)
        for n in info["caps"]:
            files[f"{d}/{n}.md"] = render_cap(caps[n], meta)

    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in files.items():
        p = out_dir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return files


def check(meta: dict, out_dir: Path = CAPS_DIR) -> int:
    files = {"README.md": render_caps_readme(meta), "INDEX.md": render_index(meta)}
    for d, info in meta["domains"].items():
        files[f"{d}/README.md"] = render_domain(d, info, meta["caps"], meta)
        for n in info["caps"]:
            files[f"{d}/{n}.md"] = render_cap(meta["caps"][n], meta)

    stale, missing = [], []
    for rel, content in files.items():
        p = out_dir / rel
        if not p.exists():
            missing.append(rel)
        elif p.read_text(encoding="utf-8") != content:
            stale.append(rel)

    on_disk = {p.relative_to(out_dir).as_posix() for p in out_dir.rglob("*.md")}
    orphan = sorted(on_disk - set(files))

    if stale or missing or orphan:
        print(f"atlas out of date: {len(stale)} stale · {len(missing)} missing · "
              f"{len(orphan)} orphan", file=sys.stderr)
        for label, names in (("stale", stale), ("missing", missing), ("orphan", orphan)):
            if names:
                print(f"  {label}: {', '.join(sorted(names)[:8])}", file=sys.stderr)
        return 1
    print(f"atlas up to date · {len(files)} files")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build the capability atlas.")
    ap.add_argument("--check", action="store_true", help="verify caps/** matches the registry")
    ap.add_argument("--registry", type=Path, default=REGISTRY)
    args = ap.parse_args(argv)

    meta = load(args.registry)
    if args.check:
        return check(meta)
    files = build(meta)
    t = meta["totals"]
    print(f"wrote {len(files)} files · {t['caps']} caps / {t['domains']} domains")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
