install-requirements:
	pip install -r requirements.txt

test: lint test-python

lint:
	flake8

test-python:
	py.test tests

