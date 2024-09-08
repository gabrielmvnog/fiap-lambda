install:
	@poetry install

lint:
	@poetry run ruff check src/

test:
	@poetry run pytest tests/

.PHONY: install test lint
