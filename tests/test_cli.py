from __future__ import annotations

import json

from gbt_caps.cli import main


def run(capsys, *argv):
    code = main(list(argv))
    out, err = capsys.readouterr()
    return code, out, err


def test_stats(capsys):
    code, out, _ = run(capsys, "stats")
    assert code == 0
    assert "341" in out
    assert "gated" in out


def test_stats_json(capsys):
    code, out, _ = run(capsys, "stats", "--json")
    payload = json.loads(out)
    assert payload["caps"] == 341
    assert len(payload["per_domain"]) == 30


def test_list_is_complete(capsys):
    code, out, _ = run(capsys, "list")
    assert code == 0
    assert "341 capability bit(s)" in out


def test_list_gated_only(capsys):
    code, out, _ = run(capsys, "list", "--gated")
    assert code == 0
    assert "79 capability bit(s)" in out
    assert "gated" in out


def test_list_by_domain(capsys):
    code, out, _ = run(capsys, "list", "--domain", "vision", "--json")
    payload = json.loads(out)
    assert code == 0 and payload and all(c["domain"] == "vision" for c in payload)


def test_domains(capsys):
    code, out, _ = run(capsys, "domains")
    assert code == 0 and "30 domains" in out


def test_domain(capsys):
    code, out, _ = run(capsys, "domain", "engine")
    assert code == 0 and "engine" in out


def test_domain_unknown(capsys):
    code, _, err = run(capsys, "domain", "nope")
    assert code == 2 and "unknown domain" in err


def test_show(capsys):
    code, out, _ = run(capsys, "show", "vision_loop")
    assert code == 0
    assert "vision_loop" in out and "needs a human" in out


def test_show_json(capsys):
    code, out, _ = run(capsys, "show", "vision_loop", "--json")
    payload = json.loads(out)
    assert code == 0 and payload["domain"] == "vision"


def test_show_unknown_suggests(capsys):
    code, _, err = run(capsys, "show", "vision_lop")
    assert code == 2
    assert "did you mean" in err


def test_search(capsys):
    code, out, _ = run(capsys, "search", "DAG")
    assert code == 0 and "hit(s)" in out


def test_search_json_limit(capsys):
    code, out, _ = run(capsys, "search", "授权", "--limit", "5", "--json")
    payload = json.loads(out)
    assert code == 0 and len(payload) <= 5


def test_check_passes(capsys):
    code, out, _ = run(capsys, "check")
    assert code == 0
    assert "0 error(s)" in out


def test_check_json(capsys):
    code, out, _ = run(capsys, "check", "--json")
    assert code == 0
    assert [i for i in json.loads(out) if i["level"] == "error"] == []
