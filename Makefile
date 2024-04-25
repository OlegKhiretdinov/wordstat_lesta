dev:
	poetry run flask --app word_stat.app run --debug

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:8000 word_stat:app

lint:
	poetry run flake8 word_stat
