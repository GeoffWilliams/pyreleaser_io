test:
	pipenv run pytest --capture=no --cov=pyreleaser_io tests/

package:
	python setup.py sdist bdist_wheel

upload:
	python -m twine upload dist/*

clean:
	rm dist/*

dev_env:
	pip install -e .
