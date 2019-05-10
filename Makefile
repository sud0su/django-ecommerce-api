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
# docker exec -ti django-ecommerce-api_app_1 /bin/sh
build:
	docker-compose build --force-rm

sync: up
	docker-compose exec app python manage.py makemigrations
	docker-compose exec app python manage.py migrate --noinput

superuser: up
	docker-compose exec app python manage.py createsuperuser

collectstatic: up
	docker-compose exec app python manage.py collectstatic

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs --follow

shell:
	docker-compose exec app python manage.py shell

psql:
	docker-compose exec db psql --username=djangoecommerce --dbname=django_ecommerce

# production
build-prod:
	docker-compose -f docker-compose.prod.yml build --force-rm

sync-prod: up-prod
	docker-compose -f docker-compose.prod.yml exec app python manage.py makemigrations
	docker-compose -f docker-compose.prod.yml exec app python manage.py migrate --noinput

superuser-prod: up-prod
	docker-compose -f docker-compose.prod.yml exec app python manage.py createsuperuser

psql-prod:
	docker-compose exec db psql --username=djangoecommerce --dbname=django_ecommerce_prod

up-prod:
	docker-compose -f docker-compose.prod.yml up -d

down-prod:
	docker-compose -f docker-compose.prod.yml down

logs-prod:
	docker-compose -f docker-compose.prod.yml logs --follow