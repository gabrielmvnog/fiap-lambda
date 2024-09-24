install:
	@poetry install

lint:
	@poetry run ruff check lambda/src/

test:
	@poetry run pytest lambda/tests/

terraform-init:
	@terraform -chdir=terraform init

terraform-plan:
	@terraform -chdir=terraform plan

.PHONY: install test lint terraform-plan terraform-init
