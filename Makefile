delmigrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

startmigrations:
	python manage.py makemigrations
	python manage.py migrate

resetdb:
	dropdb kala
	createdb kala

resetmigrations: delmigrations resetdb startmigrations