from django.urls import path, include 
from rest_framework.routers import SimpleRouter
from cinema import views

router = SimpleRouter()
router.register(r'users', views.UserViewSet, basename="users"),
router.register(r'post', views.PostViewSet, basename="post")

urlpatterns = [
    path("api/", include(router.urls))
]
