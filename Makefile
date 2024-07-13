.PHONY: dist venv

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install setuptools wheel twine

dist:
	mkdir -p dist
	rm -rf dist/*
	python setup.py sdist

publish: dist
	twine upload dist/*
