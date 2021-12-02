bot:
	python bot.py

requirements:
	pip install -r requirements-dev.txt

start: requirements bot

mypy:
	mypy bot.py

flake8:
	flake8 .

isort:
	isort .

check: isort flake8
