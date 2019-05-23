# Set variables to pass
DOCKER_HOST := $(DOCKER_HOST)
DOCKER_HOST_IP := `docker run --net=host codenvy/che-ip:nightly`

test-up:
	unset DJANGO_LB_HOST_IP; \
	export DJANGO_LB_HOST_IP=$(DOCKER_HOST_IP); \
	echo DJANGO will be available at the following address http://$$DJANGO_LB_HOST_IP; \
	echo If you want to run it on localhost then remember to add this line "localhost $$DJANGO_LB_HOST_IP" to /etc/hosts; \
	docker-compose up -d --build

# development
# got into images
## docker exec -ti django-ecommerce-api_app_1 /bin/sh
build:
	docker-compose build --force-rm

up:
	docker-compose up -d

cmd: up
	docker-compose exec app python manage.py $(CMD)

create: up
	docker-compose exec app python manage.py startapp $(APP)

sync: up
	docker-compose exec app python manage.py makemigrations
	docker-compose exec app python manage.py migrate --noinput

superuser: up
	docker-compose exec app python manage.py createsuperuser

collectstatic: up
	docker-compose exec app python manage.py collectstatic

stop:
	docker-compose stop

reset:
	docker-compose down -v

logs:
	docker-compose logs --follow

shell:
	docker-compose exec app python manage.py shell

psql:
	docker-compose exec db psql --username=djangoecommerce --dbname=django_ecommerce

sass:
	sass --watch frontend/djangotemplates/assets/scss/main.scss frontend/djangotemplates/assets/css/main.css

# production
build-prod:
	docker-compose -f docker-compose.prod.yml build --force-rm

sync-prod:
	docker-compose -f docker-compose.prod.yml exec app python manage.py makemigrations
	docker-compose -f docker-compose.prod.yml exec app python manage.py migrate --noinput

superuser-prod:
	docker-compose -f docker-compose.prod.yml exec app python manage.py createsuperuser

psql-prod:
	docker-compose exec db psql --username=djangoecommerce --dbname=django_ecommerce_prod

up-prod:
	docker-compose -f docker-compose.prod.yml up -d

stop-prod:
	docker-compose -f docker-compose.prod.yml stop

reset-prod:
	docker-compose -f docker-compose.prod.yml down -v

logs-prod:
	docker-compose -f docker-compose.prod.yml logs --follow