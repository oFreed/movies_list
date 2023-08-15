from rest_framework import routers
from .views import MovieViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register("", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
