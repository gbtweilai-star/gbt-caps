"""Regression tests for the AST exporter — including the two bugs it had."""

from __future__ import annotations

import ast
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from export_registry import (  # noqa: E402
    LiteralError,
    collect_tables,
    detect_multi_op,
    literal,
    normalize,
)


def parse_expr(src: str):
    return ast.parse(src, mode="eval").body


def test_literal_constant_and_containers():
    assert literal(parse_expr("'a'")) == "a"
    assert literal(parse_expr("[1, 2]")) == [1, 2]
    assert literal(parse_expr("(1, 2)")) == (1, 2)
    assert literal(parse_expr("{'k': 1}")) == {"k": 1}
    assert literal(parse_expr("-3")) == -3


def test_literal_string_concatenation():
    assert literal(parse_expr("'a' 'b'")) == "ab"
    assert literal(parse_expr("'a' + 'b'")) == "ab"


def test_literal_percent_formatting():
    """Bug #1: a '%d'-formatted desc used to raise and silently drop the table."""
    assert literal(parse_expr("'上限 %d 轮' % 3")) == "上限 3 轮"


def test_literal_fstring_with_constants():
    assert literal(parse_expr("f'a{1}b'")) == "a1b"


def test_literal_refuses_calls():
    with pytest.raises(LiteralError):
        literal(parse_expr("dict(a=1)"))


def test_literal_refuses_non_string_concat():
    with pytest.raises(LiteralError):
        literal(parse_expr("1 + 2"))


def test_collect_tables_skips_unparsable():
    tree = ast.parse("A = {'x': 1}\nB = some_call()\nC = 3\n")
    tables = collect_tables(tree)
    assert tables == {"A": {"x": 1}, "C": 3}


def test_detect_multi_op_ignores_loop_equals():
    """Bug #2: `"op=" in text` also matched `loop=` / `desktop=`."""
    multi, _, ops = detect_multi_op({"desc": "轮次上限 3，到顶如实报；loop=1 表示一次"}, {})
    assert multi is False
    assert ops == []


def test_detect_multi_op_reads_op_assignment():
    multi, _, _ = detect_multi_op({"desc": "op=tick/history/status"}, {})
    assert multi is True


def test_detect_multi_op_reads_slash_lists():
    multi, _, ops = detect_multi_op(
        {"desc": "房间空间：create/enter/define_plan/get_plan/frame/gate"}, {})
    assert multi is True
    assert ops[:2] == ["create", "enter"]


def test_detect_multi_op_from_params():
    multi, hint, _ = detect_multi_op({"desc": "触手"}, {"params": ["action"],
                                                         "hint": "触手能力名"})
    assert multi is True and hint == "触手能力名"


def test_normalize_shapes_and_totals():
    benign = {
        "one": {"domain": "d", "desc": "single", "handler": "one", "safe": True},
        "two": {"domain": "d", "desc": "op=a/b/c", "handler": "two", "safe": False,
                "external": True},
    }
    snap = normalize(benign, {"two": {"params": ["target"], "hint": "目标"}}, "x.py", "0" * 64)
    assert snap["totals"]["caps"] == 2
    assert snap["totals"]["domains"] == 1
    assert snap["totals"]["gated_by_safety_flag"] == 1
    assert snap["totals"]["needs_external"] == 1
    assert snap["caps"]["two"]["params"] == ["target"]
    assert snap["caps"]["two"]["requires_params"] is True
    assert snap["caps"]["one"]["requires_params"] is False
    assert snap["domains"]["d"]["caps"] == ["one", "two"]
