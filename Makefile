.PHONY: dist

dist:
	mkdir -p dist
	rm -rf dist/*
	python setup.py sdist

publish: dist
	twine upload dist/*
