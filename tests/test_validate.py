"""The validator must have teeth — so every check gets a mutation that trips it."""

from __future__ import annotations

import copy

import pytest

from gbt_caps import spec


def mini():
    """A tiny but coherent snapshot."""
    caps = {
        "alpha": {"name": "alpha", "domain": "d1", "desc": "does a thing",
                  "handler": "h1", "safe": True, "external": False,
                  "requires_params": False, "params": [], "params_hint": "",
                  "multi_op": False, "ops_hint": "", "ops": []},
        "beta": {"name": "beta", "domain": "d1", "desc": "does another thing",
                 "handler": "h2", "safe": False, "external": False,
                 "requires_params": False, "params": [], "params_hint": "",
                 "multi_op": False, "ops_hint": "", "ops": []},
    }
    return {
        "schema": 1,
        "source": {"file": "x.py", "sha256": "0" * 64},
        "totals": {"caps": 2, "domains": 1, "gated_by_safety_flag": 1,
                   "needs_external": 0, "needs_params": 0, "multi_op": 0},
        "domains": {"d1": {"count": 2, "caps": ["alpha", "beta"]}},
        "caps": caps,
    }


def codes(snap):
    return [i["code"] for i in spec.validate(snap)]


def test_mini_snapshot_is_clean():
    assert spec.validate(mini()) == []


def test_bad_name():
    s = mini()
    s["caps"]["Bad Name"] = dict(s["caps"]["alpha"], name="Bad Name")
    s["domains"]["d1"]["caps"].append("Bad Name")
    s["domains"]["d1"]["count"] = 3
    s["totals"]["caps"] = 3
    assert "bad_name" in codes(s)


def test_missing_desc():
    s = mini()
    s["caps"]["alpha"]["desc"] = "   "
    assert "missing_desc" in codes(s)


def test_missing_domain():
    s = mini()
    s["caps"]["alpha"]["domain"] = ""
    assert "missing_domain" in codes(s)


def test_domain_count_mismatch():
    s = mini()
    s["domains"]["d1"]["count"] = 5
    assert "domain_count_mismatch" in codes(s)


def test_domain_membership_mismatch():
    s = mini()
    s["domains"]["d1"]["caps"] = ["alpha"]
    assert "domain_membership_mismatch" in codes(s)


def test_empty_domain():
    s = mini()
    s["domains"]["ghost"] = {"count": 0, "caps": []}
    s["totals"]["domains"] = 2
    assert "empty_domain" in codes(s)


def test_total_mismatch():
    s = mini()
    s["totals"]["caps"] = 99
    assert "total_mismatch" in codes(s)


def test_params_flag_without_params():
    s = mini()
    s["caps"]["alpha"]["requires_params"] = True
    assert "params_flag_without_params" in codes(s)


def test_params_without_hint_is_a_warning():
    s = mini()
    s["caps"]["alpha"]["params"] = ["target"]
    s["caps"]["alpha"]["requires_params"] = True
    issues = spec.validate(s)
    assert [i for i in issues if i["code"] == "params_without_hint"]
    assert spec.errors(s) == []


def test_multi_op_without_selector_is_a_warning():
    s = mini()
    s["caps"]["alpha"]["multi_op"] = True
    issues = spec.validate(s)
    assert [i for i in issues if i["code"] == "multi_op_without_selector"]
    assert spec.errors(s) == []


def test_shared_handler_is_a_warning():
    s = mini()
    s["caps"]["beta"]["handler"] = "h1"
    issues = spec.validate(s)
    assert [i for i in issues if i["code"] == "shared_handler"]
    assert spec.errors(s) == []


def test_errors_only_returns_errors():
    s = mini()
    s["caps"]["beta"]["handler"] = "h1"          # warning
    s["caps"]["alpha"]["desc"] = ""             # error
    assert [i["code"] for i in spec.errors(s)] == ["missing_desc"]
