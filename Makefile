install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py
	nbqa black *.ipynb

lint:
	nbqa ruff *.ipynb
	ruff check *.py

test:
	python -m pytest -vv --cov=lib test_*.py
	python -m pytest --nbval *.ipynb

add_commit_push:
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add pairplot.png boxplots.png Statistics_report.md; \
		git commit -m "Add generated plot image"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi


update_readme:
	cat report.md >> README.md
	git add README.md
	git commit -m "merge readmes"
	git push  