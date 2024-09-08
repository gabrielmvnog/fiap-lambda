install:
	@poetry install

test:
	@poetry run pytest tests/

.PHONY: install test
