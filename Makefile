install:
	@poetry install


publish:
	@poetry publish -r testpypi


make_lint:
	@poetry run flake8 brain_games


update_test:
	pip install --user --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple Ivanich_spb_brain_games


.PHONY: install publish make_lint
