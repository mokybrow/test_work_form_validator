SOURCE_DIR_API=form_validator_api

run:
	poetry run python -m $(SOURCE_DIR_API)

script:
	poetry run python -m script_test