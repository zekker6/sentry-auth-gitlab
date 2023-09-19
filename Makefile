.PHONY: dist

test:
	pip install -e .
	pip install "file://`pwd`#egg=sentry-auth-gitlab[tests]"
	py.test -x

dist:
	mkdir -p dist
	rm -rf dist/*
	python setup.py sdist

publish: dist
	twine upload dist/*
