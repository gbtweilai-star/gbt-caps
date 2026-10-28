# gbt-caps

**341 capability specs for an AI agent framework — one file each, machine-checkable, zero dependencies.**

![specs](https://img.shields.io/badge/capability%20specs-341-2f6f4e)
![domains](https://img.shields.io/badge/domains-30-2f6f4e)
![deps](https://img.shields.io/badge/runtime%20deps-0-blue)
![python](https://img.shields.io/badge/python-3.9%20%E2%80%933.13-blue)
![tests](https://img.shields.io/badge/tests-57%20passing-brightgreen)
![license](https://img.shields.io/badge/license-MIT-black)

```bash
pip install gbt-caps
gbt-caps stats
```

```
caps     341
domains  30
gated    79  (safe: false — needs a human)
multi-op 171  (description enumerates operations)
params   29
external 5
source   caps_registry.py  sha256 1c85007b73b9

  creation        54 caps · 22 gated ·  43 multi-op
  system          51 caps ·  5 gated ·  29 multi-op
  llm             41 caps ·  8 gated ·  20 multi-op
  security        29 caps ·  9 gated ·   9 multi-op
  mind            19 caps ·  1 gated ·  11 multi-op
  pipeline        18 caps ·  0 gated ·   1 multi-op
  tentacle        18 caps ·  5 gated ·   9 multi-op
  ...
```

---

## What this is

An agent framework grew **341 distinct capabilities** — `vision_loop`, `wf_define`,
`osint_scan`, `deploy_publish`, `room_space`, `tentacle`, and 335 more, across 30
domains. They were declared in one 235 KB Python dict, which is a fine place to
*store* a capability and a terrible place to *explain* one.

This repository is that dict, opened up:

- **341 spec pages**, one per capability, at `caps/<domain>/<name>.md`
- **30 domain indexes**, plus a full `INDEX.md`
- **a snapshot** (`src/gbt_caps/data/registry.json`) any tool can read
- **a query CLI and API** — `lookup`, `by_domain`, `search`, `stats`
- **a contract validator** that finds where the registry contradicts itself

Every page states what the bit does, how to call it, what it takes, what it will
not do, and where the claim came from. Nothing is invented: the description is
quoted verbatim, the flags are the registry's own, and anything derived is
labelled as derived.

## What this is not

- **Not the implementation.** The bits are implemented by the upstream framework.
  This repo is the contract layer — the part you can read, diff, validate and
  publish without shipping 600 files of someone's application.
- **Not 341 importable functions.** There is no `import gbt_caps; vision_loop()`.
  See [why not one repository per capability](#why-not-one-repository-per-capability).
- **Not auto-generated slop.** The generator is 300 lines you can read, the tests
  fail if a page drifts from the data, and `--check` proves the tree reproduces
  byte-for-byte.

---

## 30 seconds

```bash
$ gbt-caps show vision_loop
vision_loop
  domain     vision
  handler    vision_loop
  safe       false   ← needs a human
  external   false
  params     —
  shape      multi-op
  ops        look / hear / speak / think / act / verify / loop / status

**原生四觉闭环**（主人令 2026-10-09：「她的视觉每次都要跟手分开去使用传统的**瞎子操作**…
```

```bash
$ gbt-caps list --gated
actioncam                    video           [gated; multi-op]
anatomy_figures              creation        [gated; multi-op]
anim_fix                     creation        [gated; multi-op]
art_brief                    creation        [gated; multi-op]
...
79 capability bit(s)
```

```bash
$ gbt-caps domain engine
# engine · 10 bits

$ gbt-caps search 授权 --limit 5
$ gbt-caps check
```

Python:

```python
from gbt_caps import lookup, by_domain, search, gated_caps, stats

lookup("vision_loop").gated            # True — the registry does not mark it safe
lookup("vision_lop")                   # UnknownCap: did you mean vision_loop?
[c.name for c in by_domain("engine")]  # 10 bits
len(gated_caps())                      # 79
stats()["per_domain"]["creation"]      # {'caps': 54, 'gated': 22, 'multi_op': 43}
search("DAG", domain="engine")         # full-text, scoped
```

---

## How it is organised

```
caps/
  README.md                 # 30 domains, counts, entry points
  INDEX.md                  # all 341, grouped by domain
  vision/
    README.md               # the domain: 5 bits, which are gated
    vision_loop.md          # one capability, six sections
    ...
src/gbt_caps/
  spec.py                   # load, lookup, search, validate
  cli.py                    # gbt-caps
  data/registry.json        # the snapshot everything is built from
tools/
  export_registry.py        # caps_registry.py -> registry.json  (AST, never imports)
  build_atlas.py            # registry.json -> caps/**           (deterministic)
```

Every spec page has the same six sections, so you can diff two capabilities or
grep across all 341:

| Section | What it answers |
|---|---|
| **用途** | What this bit is for — the registry's own words, verbatim |
| **使用方式** | How to query the spec, and how to call the bit |
| **参数** | Required inputs, or an explicit statement that there are none |
| **返回** | The contract: `ok` + `gbt_stamp`; the rest is implementation |
| **边界与注意** | `safe: false`? `external`? multi-op with no `op`? Fail-closed rules |
| **出处** | Source file, domain, handler, snapshot schema, source sha256 |

---

## The validator is the point

Publishing 341 pages is easy. Keeping them true is the hard part, so the repo
carries two guarantees.

**1. The tree is reproducible.** `build_atlas.py --check` regenerates every page in
memory and compares bytes. Hand-edit a page and the check fails.

```bash
$ python tools/build_atlas.py --check
atlas up to date · 373 files
```

**2. The data is coherent.** `gbt-caps check` runs 11 contract checks over the
snapshot — snake_case names, non-empty descriptions, the domain index must be a
partition, counts must agree with totals, `requires_params` must imply `params`.

```bash
$ gbt-caps check
warn  shared_handler            handler 'dh_rig' serves 5 names: ['anim_audit', ...]
warn  multi_op_without_selector voice_studio reads as multi-op but declares no op/action parameter
...
ok · 341 caps · 0 error(s) · 168 warning(s)
```

**Those 168 warnings are the interesting part.** They are places where the source
registry's prose and its parameter contracts disagree — a description that
enumerates eight operations while registering no `op` argument, or one handler
quietly serving five names. The atlas found them; we published them instead of
tidying them away. Each one is checkable by opening the page it points at.

---

## Domains

| Domain | Caps | Gated | Multi-op | | Domain | Caps | Gated | Multi-op |
|---|---:|---:|---:|---|---|---:|---:|---:|
| `creation` | 54 | 22 | 43 | | `devour` | 5 | 0 | 1 |
| `system` | 51 | 5 | 29 | | `vision` | 5 | 1 | 4 |
| `llm` | 41 | 8 | 20 | | `finance` | 4 | 0 | 0 |
| `security` | 29 | 9 | 9 | | `longrun` | 4 | 0 | 0 |
| `mind` | 19 | 1 | 11 | | `voice` | 4 | 0 | 2 |
| `pipeline` | 18 | 0 | 1 | | `automation` | 2 | 1 | 2 |
| `tentacle` | 18 | 5 | 9 | | `brain` | 2 | 0 | 0 |
| `recon` | 17 | 6 | 10 | | `collab` | 2 | 1 | 2 |
| `video` | 14 | 9 | 6 | | `desktop` | 2 | 1 | 1 |
| `data` | 12 | 3 | 7 | | `device` | 2 | 0 | 0 |
| `engine` | 10 | 1 | 2 | | `infra` | 2 | 0 | 1 |
| `tools` | 9 | 2 | 7 | | `project` | 2 | 0 | 1 |
| `integration` | 7 | 4 | 2 | | `social` | 2 | 0 | 1 |
| | | | | | `comms` | 1 | 0 | 0 |
| | | | | | `framework` | 1 | 0 | 0 |
| | | | | | `image_video` | 1 | 0 | 0 |
| | | | | | `life` | 1 | 0 | 0 |

Full table with per-domain pages: [`caps/README.md`](caps/README.md) ·
[`caps/INDEX.md`](caps/INDEX.md)

---

## Regenerating for your own registry

Both tools are generic — point them at any `caps_registry.py` shaped like this:

```python
BENIGN_CAPS = {
    "my_cap": {"domain": "mine", "desc": "what it does", "handler": "my_cap", "safe": True},
}
PARAM_REQUIRED = {"my_cap": {"params": ["target"], "hint": "what to target"}}
```

```bash
python tools/export_registry.py path/to/caps_registry.py -o src/gbt_caps/data/registry.json
python tools/build_atlas.py
python tools/build_atlas.py --check     # reproducible?
gbt-caps check                          # coherent?
```

The exporter **parses, never imports** — importing a framework package runs its
module-level side effects, which a documentation tool has no business doing. It
evaluates only what a data table can contain, and refuses anything else rather
than guessing:

```python
literal("'上限 %d 轮' % 3")   # '上限 3 轮'      ← %-formatting is supported
literal("dict(a=1)")          # LiteralError    ← calls are refused
```

---

## Why not one repository per capability

341 repos with one file each is not open source, it is a directory listing. Three
concrete reasons this repo is the shape it is:

1. **Discoverability.** GitHub indexes repositories and topics, not directories
   inside them. 341 near-empty repos would rank for nothing and trip spam
   heuristics; one repo with 341 documented pages ranks for all of it.
2. **Reviewability.** A change to the contract should be one diff a human can
   read. Split across 341 repos it becomes 341 pull requests nobody will audit.
3. **Truth maintenance.** The value here is `--check`: the pages *cannot* drift
   from the data. That guarantee needs one tree and one generator.

The collections that do well on this platform — curated skill libraries, spec
repos, integration catalogues — all take this shape: many individually
addressable artifacts, one index, one contract, one CI run.

---

## Install & develop

```bash
pip install gbt-caps           # library + CLI
python -m gbt_caps stats       # same thing without the console script
```

```bash
git clone https://github.com/gbtweilai-star/gbt-caps
cd gbt-caps
pip install -e ".[dev]"
make test        # 57 tests, no network
make check       # atlas reproducible + contract clean
```

Python 3.9 – 3.13 · Linux, macOS, Windows · no runtime dependencies.

## Related

- [`consent-gate`](https://github.com/gbtweilai-star/consent-gate) — the permission
  gate for the 79 bits marked `safe: false`. The agent can ask; only a human can grant.
- [`GBTxiaotudouV8-Commander`](https://github.com/gbtweilai-star/GBTxiaotudouV8-Commander) —
  the framework these capabilities belong to.

## License

MIT. Spec text is reproduced from the upstream registry, which is also MIT.

---

**中文说明：[README.zh-CN.md](README.zh-CN.md)**
