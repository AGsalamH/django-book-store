all: makemigrations migrate run

run:
	@echo "Running the server ..."
	@python3 manage.py runserver

makemigrations:
	@echo "Making migrations ..."
	@python3 manage.py makemigrations

migrate:
	@echo "Performing migrations ..."
	@python3 manage.py migrate

requirements:
	pip3 freeze > requirements.txt

superuser:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell
