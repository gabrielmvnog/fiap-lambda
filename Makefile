install:
	@poetry install

lint:
	@poetry run ruff check src/

test:
	@poetry run pytest tests/

terraform-init:
	@terraform init

terraform-plan:
	@terraform plan

.PHONY: install test lint terraform-plan terraform-init
