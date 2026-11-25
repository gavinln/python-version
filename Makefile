SCRIPT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: help
.DEFAULT_GOAL=help
help:  ## help for this Makefile
	@grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

versions-bak := 310 311 312 313 314

versions := 313

.PHONY: $(versions)

.PHONY: py310
py310: 310 ## run python 3.10 examples
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py$< uv run -p $< --directory py$< python py$<.py

.PHONY: py311
py311: 311 ## run python 3.11 examples
	# UV_PROJECT_ENVIRONMENT=~/.cache/venv/py3.11 uv run --directory py3.11 python units_lib.py
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py$< uv run -p $< --directory py$< python py$<.py

.PHONY: py312
py312: 312 ## run python 3.12 examples
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py$< uv run -p $< --directory py$< python py$<.py

.PHONY: py313
py313: 313 ## run python 3.13 examples
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py$< uv run -p $< --directory py$< python py$<.py

.PHONY: py314
py314: 314 ## run python 3.14 examples
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py$< uv run -p $< --directory py$< python py$<.py

.PHONY: nvim
nvim:  ## run nvim in a Python env
	uv run -p 3.13 nvim -S Session.vim

.PHONY: lint
lint: ## lint files to run static check
	$(foreach ver, $(versions), \
		ruff check --target-version py$(ver) py$(ver)/py$(ver).py)

.PHONY: fix-lint
fix-lint: ## fix lint errors
	$(foreach ver, $(versions), \
		ruff check --target-version py$(ver) --fix py$(ver) py$(ver)/py$(ver).py)

.PHONY: black
black:  ## run black to format python code
	black -l 79 $(SCRIPT_DIR)/py3.10
	black -l 79 $(SCRIPT_DIR)/py3.11
	black -l 79 $(SCRIPT_DIR)/py3.12
	black -l 79 $(SCRIPT_DIR)/py3.13

.PHONY: clean
clean:
	find . -name '.pytest_cache' -type d -exec rm -rf '{}' +
	find . -name '__pycache__' -type d -exec rm -rf '{}' +
	find . -name '.ruff_cache' -type d -exec rm -rf '{}' +
