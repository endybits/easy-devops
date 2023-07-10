install:
	python3 -m pip install -U pip && \
	pip install -r requirements.txt
	export PYTHONPATH=.

lint:
	pylint --disable=R,C app

tests:
	python -m pytest -vv -cov=app.tests