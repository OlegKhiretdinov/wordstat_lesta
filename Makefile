dev:
	poetry run flask --app word_stat.app run --debug

lint:
	poetry run flake8 word_stat
