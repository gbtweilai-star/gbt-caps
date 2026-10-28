# Changelog

All notable changes are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · SemVer.

## [Unreleased]

### Added

- **`ACCEPTANCE.md` / `ACCEPTANCE.zh-CN.md`** — an acceptance run over all 341
  bits, one subprocess each, empty payload, 90s cap. Headline: **307 pass,
  34 real defects**. The 34 are itemised per bit rather than summarised away:
  31 dispatch targets the registry calls implemented but which are absent from the
  tree, 2 bits that return nothing within 300s, and 1 bit whose `TypeError` leaks
  out labelled `user_error`.
- **A guardrail verified in both directions.** All 12 enforced scopes are walked
  through deny-without-grant → hand-written ledger line → allow → burn-or-reuse.
  The test runs on a temporary ledger; the real `store/auth_grants.jsonl` is never
  written to. Result: 12/12, `ai_can_grant = False`.
- **`acceptance.json`** — the same readings, machine-readable, one object per bit.

### Changed

- The Chinese README's "why not one repository per capability" section is gone.
  It argued against something that now exists — 341 repositories are live and
  listed in `REPOS.md`. The section now explains what the atlas is *for* once the
  repos exist: an index, a review surface, and the single snapshot every one of
  the 342 test suites pins to. Leaving the old argument in place would have meant
  the documentation contradicting the artifacts.

## [0.1.0] — 2026-10-28

First release. A 235 KB capability dict became a readable, checkable atlas.

### Added

- **341 spec pages** at `caps/<domain>/<name>.md`, one per capability bit, each
  with six fixed sections: 用途 / 使用方式 / 参数 / 返回 / 边界与注意 / 出处.
- **30 domain indexes** plus `caps/INDEX.md` covering every bit.
- **`gbt_caps` library** — `lookup` (with near-miss suggestions), `get`,
  `by_domain`, `search` (scoped, ordered), `gated_caps`, `stats`, `validate`.
- **`gbt-caps` CLI** — `stats`, `list [--gated] [--domain]`, `domains`, `domain`,
  `show [--json]`, `search`, `check`. Exit code 1 when the contract has errors.
- **Contract validator** — 11 checks over the snapshot (naming, descriptions,
  domain partition, count agreement, `requires_params` ↔ `params`, shared
  handlers). Errors fail; warnings inform.
- **`tools/export_registry.py`** — reads a `caps_registry.py` **by AST, never by
  import**, so documenting a framework does not execute it. Supports the literal
  forms a data table actually uses, including `'… %d …' % 3` formatting, and
  refuses calls instead of guessing.
- **`tools/build_atlas.py`** — deterministic page generation with `--check` to
  prove the tree reproduces byte-for-byte.
- **57 tests**, including mutation tests that prove each validation rule has
  teeth, and two regressions for real exporter bugs: `%`-formatting crashing the
  parse, and `"op=" in text` matching `loop=` / `desktop=`.

### Findings published, not fixed

`gbt-caps check` reports **168 warnings, 0 errors** against the registry this
atlas describes — descriptions that enumerate operations while registering no
`op` parameter, and handlers serving several names. They are visible in the atlas
rather than tidied away upstream.

### Notes

- Python 3.9 – 3.13, no runtime dependencies.
- The upstream registry declares **341** capability bits across **30** domains.
  Numbers elsewhere saying 348 count something else; the AST does not lie.
