install:
	@poetry install


publish:
	@poetry publish -r testpypi


make_lint:
	@poetry run flake8 brain_games

.PHONY: install publish make_lint
