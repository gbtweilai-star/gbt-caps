from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

import gbt_caps
from gbt_caps import spec

ROOT = Path(__file__).resolve().parent.parent
CAPS = ROOT / "caps"
SECTIONS = ["## 用途", "## 使用方式", "## 参数", "## 返回", "## 边界与注意", "## 出处"]


@pytest.fixture(scope="module")
def snap():
    return spec.snapshot()


def test_snapshot_shape(snap):
    assert snap["schema"] == 1
    assert snap["totals"]["caps"] == len(snap["caps"])
    assert snap["totals"]["domains"] == len(snap["domains"])
    assert len(snap["caps"]) == 341
    assert len(snap["domains"]) == 30


def test_every_domain_count_matches(snap):
    for domain, info in snap["domains"].items():
        actual = [n for n, c in snap["caps"].items() if c["domain"] == domain]
        assert info["count"] == len(actual), domain
        assert sorted(actual) == info["caps"], domain


def test_domain_membership_is_partition(snap):
    seen = []
    for info in snap["domains"].values():
        seen.extend(info["caps"])
    assert sorted(seen) == sorted(snap["caps"]), "domain index is not a partition"


def test_every_cap_has_a_page(snap):
    for name, cap in snap["caps"].items():
        page = CAPS / cap["domain"] / f"{name}.md"
        assert page.exists(), f"missing page for {name}"


def test_every_page_maps_back_to_a_cap(snap):
    known = {(c["domain"], n) for n, c in snap["caps"].items()}
    for page in CAPS.rglob("*.md"):
        if page.name in ("README.md", "INDEX.md"):
            continue
        key = (page.parent.name, page.stem)
        assert key in known, f"orphan page {page.relative_to(CAPS)}"


def test_pages_are_not_empty_and_have_all_sections(snap):
    for name, cap in snap["caps"].items():
        text = (CAPS / cap["domain"] / f"{name}.md").read_text(encoding="utf-8")
        assert len(text) > 400, f"{name} page looks empty ({len(text)} chars)"
        for section in SECTIONS:
            assert section in text, f"{name} missing section {section}"
        assert f"# `{name}`" in text


def test_page_states_the_verbatim_description(snap):
    for name, cap in snap["caps"].items():
        if not cap["desc"]:
            continue
        text = (CAPS / cap["domain"] / f"{name}.md").read_text(encoding="utf-8")
        assert cap["desc"][:60] in text, f"{name} does not quote its own description"


def test_domain_indexes_list_their_members(snap):
    for domain, info in snap["domains"].items():
        text = (CAPS / domain / "README.md").read_text(encoding="utf-8")
        assert f"# 域 `{domain}`" in text
        for name in info["caps"]:
            assert f"[`{name}`](./{name}.md)" in text, f"{domain} index misses {name}"


def test_top_level_index_covers_everything(snap):
    text = (CAPS / "INDEX.md").read_text(encoding="utf-8")
    for name in snap["caps"]:
        assert f"[`{name}`]" in text, f"INDEX.md misses {name}"


def test_atlas_is_reproducible():
    """Regenerating from the snapshot must not change a byte."""
    import subprocess
    import sys

    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_atlas.py"), "--check"],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr


def test_counts_in_headline_are_not_hand_written():
    """The number on the cover must equal the number in the data."""
    text = (CAPS / "README.md").read_text(encoding="utf-8")
    n = len(spec.all_caps())
    assert re.search(rf"{n} 位能力", text) or f"{n} 位" in text
    top = (ROOT / "README.md").read_text(encoding="utf-8")
    assert str(n) in top


def test_no_placeholder_text_in_pages():
    bad = ("TODO", "TBD", "FIXME", "<placeholder>", "lorem ipsum")
    for page in CAPS.rglob("*.md"):
        text = page.read_text(encoding="utf-8").lower()
        for token in bad:
            assert token.lower() not in text, f"{page.name} contains {token!r}"


def test_lookup_and_errors():
    cap = spec.lookup("vision_loop")
    assert cap.domain == "vision" and cap.gated
    with pytest.raises(spec.UnknownCap) as exc:
        spec.lookup("vision_lop")
    assert "vision_loop" in exc.value.suggestions
    assert spec.get("nope_not_real") is None


def test_search_is_scoped_and_ordered():
    hits = spec.search("DAG")
    assert hits and all("dag" in (c.desc + c.name + c.handler).lower() for c in hits)
    assert spec.search("DAG", domain="engine")
    assert all(c.domain == "engine" for c in spec.search("DAG", domain="engine"))
    assert spec.search("   ") == []


def test_stats_agree_with_snapshot():
    s = spec.stats()
    assert s["caps"] == len(spec.all_caps())
    assert s["gated_by_safety_flag"] == len(spec.gated_caps())
    assert sum(v["caps"] for v in s["per_domain"].values()) == s["caps"]


def test_gated_caps_are_the_unsafe_ones():
    assert all(not c.safe for c in spec.gated_caps())
    assert len(spec.gated_caps()) == 79


def test_validate_is_clean_on_the_shipped_snapshot():
    issues = spec.validate()
    assert spec.errors() == [], spec.errors()
    assert isinstance(issues, list)
