# Changelog

All notable changes are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · SemVer.

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
