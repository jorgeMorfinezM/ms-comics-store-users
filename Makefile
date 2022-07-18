app_name = ms_n-layered-ddd_template

check:
	@git add .
	@pre-commit

test:
	@pytest -vv
