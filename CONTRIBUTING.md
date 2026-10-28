# Contributing

The most useful contribution to this repo is **not** a hand-edited spec page.

## The one rule

`caps/**` is generated. Editing a page by hand will be overwritten and will fail
`tools/build_atlas.py --check` in CI. Change the data, then regenerate:

```bash
# 1. change the source registry (or the snapshot directly, for a doc fix)
$EDITOR src/gbt_caps/data/registry.json

# 2. regenerate
python tools/build_atlas.py

# 3. prove it is reproducible and coherent
python tools/build_atlas.py --check
python -m gbt_caps check
python -m pytest -q
```

## Adding a capability

Add one entry to `caps` and to the right domain in `domains`, then bump `totals`.
`gbt-caps check` will tell you if you missed a spot — it verifies that the domain
index is a partition of the capability set and that every count agrees with the
data.

```json
"my_cap": {
  "name": "my_cap",
  "domain": "tools",
  "desc": "what it does, in one or two sentences",
  "handler": "my_cap",
  "safe": true,
  "external": false,
  "requires_params": false,
  "params": [],
  "params_hint": "",
  "multi_op": false,
  "ops_hint": "",
  "ops": []
}
```

Then add `"my_cap"` to `domains.tools.caps` (keep it sorted), increment
`domains.tools.count` and `totals.caps`, and run `make atlas test`.

## What makes a good description

The description is the page's **用途** section, quoted verbatim. Write it for
someone who has never seen the codebase:

- lead with what it is, not with who asked for it;
- name the failure it prevents, if it prevents one;
- if it dispatches to several operations, enumerate them — the exporter reads
  `op=a/b/c` slash lists and will mark the bit multi-op automatically;
- do not claim behaviour you cannot point at.

## What gets rejected

- A spec page edited by hand instead of regenerated.
- A capability whose description is a restatement of its name.
- A new `safe: false` bit with no explanation of what a human is being asked to
  approve.
- Silence about a known limitation. The 168 warnings in `gbt-caps check` are
  there because we publish what we find.

## Tests

```bash
make test     # 57 tests: atlas integrity, validator mutations, CLI, exporter
```

`tests/test_validate.py` is the interesting one: every validation rule has a
mutation that trips it, so a rule that stops working turns a test red instead of
quietly passing everything.
