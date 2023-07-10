install:
	python3 -m pip install -U pip && \
	pip install -r requirements.txt
	export PYTHONPATH=.