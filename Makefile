install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py
	nbqa black *.ipynb

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	nbqa ruff *.ipynb
	ruff check *.py

test:
	python -m pytest -vv --cov=lib test_*.py
	python -m pytest --nbval *.ipynb