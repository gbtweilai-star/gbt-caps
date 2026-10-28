.PHONY: help test check atlas export build clean install

PY ?= python

help:
	@echo "make test     run the test suite (57 tests)"
	@echo "make check    atlas reproducible + registry contract clean"
	@echo "make atlas    regenerate caps/** from registry.json"
	@echo "make export   regenerate registry.json from a caps_registry.py"
	@echo "make build    build sdist + wheel into dist/"
	@echo "make clean    remove caches and build artefacts"

test:
	$(PY) -m pytest -q

check:
	$(PY) tools/build_atlas.py --check
	$(PY) -m gbt_caps check

atlas:
	$(PY) tools/build_atlas.py

export:
	@test -n "$(REGISTRY)" || (echo "usage: make export REGISTRY=path/to/caps_registry.py" && exit 2)
	$(PY) tools/export_registry.py "$(REGISTRY)" -o src/gbt_caps/data/registry.json
	$(PY) tools/build_atlas.py

install:
	$(PY) -m pip install -e ".[dev]"

build:
	$(PY) -m pip install -q build && $(PY) -m build

clean:
	rm -rf build dist *.egg-info .pytest_cache
	find . -name __pycache__ -type d -exec rm -rf {} +
