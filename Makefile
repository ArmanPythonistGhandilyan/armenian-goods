PM = python manage.py
DEB = docker exec -it backend

#----- backend commands -----#
.PHONY: makemigrations migrate  runserver sqlmigrate
makemigrations migrate runserver sqlmigrate:
	${DEB} ${PM} $@

.PHONY: createsuperuser # creates superuser with: username="admin", password="admin", 
createsuperuser:
	${DEB} ${PM} createsuperuser --noinput 

.PHONY: pytest sh
pytest sh: 
	${DEB} $@
#--------- postgres ----------#
.PHONY: enter-postgres
enter-postgres:
	docker exec -it postgres psql -U postgres postgres
#---------- compose ----------#
.PHONY: up
up:
	docker-compose up

.PHONY: up-build
up-build:
	docker-compose up --build

down:
	docker-compose down


