install:
	poetry install

test:
	poetry run pytest

pytestinstall:
	pip install pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

build: check
	poetry build