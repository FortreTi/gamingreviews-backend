from django.urls import path, include 
from rest_framework.routers import SimpleRouter
from users.views import UserViewSet
from post.views import PostViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename="users"),
router.register(r'posts', PostViewSet, basename="posts"),

urlpatterns = [
    path("api/", include(router.urls))
]

