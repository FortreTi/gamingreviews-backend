# RUN DOCKER
1. docker-compose up

# RUN MIGRATES
2. docker-compose exec web python manage.py migrate

# CREATE SUPER USER
3. docker-compose exec web python manage.py createsuperuser


