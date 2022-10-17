# RUN DOCKER
1. docker-compose up

# RUN MIGRATES
2. docker-compose exec web python manage.py migrate

# CREATE SUPER USER
3. docker-compose exec web python manage.py createsuperuser

# ENDPOINTS 

    admin/
    api/token/ [name='token_obtain_pair']
    api/token/refresh/ [name='token_refresh']
    base/ api/ ^users/$ [name='users-list']
    base/ api/ ^users/(?P<pk>[^/.]+)/$ [name='users-detail']
    base/ api/ ^posts/$ [name='posts-list']
    base/ api/ ^posts/(?P<pk>[^/.]+)/$ [name='posts-detail']
    swagger(P<format>\.json|\.yaml)$ [name='schema-json']
    swagger/ [name='schema-swagger-ui']
    redoc/ [name='schema-redoc']

