install:
	@poetry install


publish:
	@poetry publish -r testpypi


lint:
	@poetry run flake8 brain_games


update_test:
	@pip uninstall Ivanich_spb_brain_games&&\
	pip install --user --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple Ivanich_spb_brain_games


.PHONY: install publish lint
