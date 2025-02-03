SCRIPT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: help
.DEFAULT_GOAL=help
help:  ## help for this Makefile
	@grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: py3_10
py3_10:  ## run python 3.10 examples
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py3.10 uv run --directory py3.10 python py3.10.py

.PHONY: py3_11
py3_11:  ## run python 3.11 examples
	# UV_PROJECT_ENVIRONMENT=~/.cache/venv/py3.11 uv run --directory py3.11 python units_lib.py
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py3.11 uv run --directory py3.11 python py3.11.py

.PHONY: py3_12
py3_12:  ## run python 3.12 examples
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py3.12 uv run --directory py3.12 python py3.12.py

.PHONY: py3_13
py3_13:  ## run python 3.13 examples
	UV_PROJECT_ENVIRONMENT=~/.cache/venv/py3.13 uv run --directory py3.13 python py3.13.py

.PHONY: nvim
nvim:  ## run nvim in a Python env
	uv run -p 3.13 nvim -S Session.vim

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
