test:
	pipenv run pytest --capture=no --cov=pyreleaser_io tests/

package:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

clean:
	rm dist/*

dev_env:
	pip3 install -e .
