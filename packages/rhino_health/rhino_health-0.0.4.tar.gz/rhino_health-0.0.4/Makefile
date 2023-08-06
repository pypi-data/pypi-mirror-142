format:
	python -m black .
	python -m isort .

lint:
	python -m black --check --diff .
	python -m isort --check --diff .

test:
	pytest

build:
	rm -f ./dist/*.whl
	flit build --format wheel

.PHONY: lint format test

publish:
	./dist/publish.sh
