from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps.shops.apis.rest import ShopsAPI

router = DefaultRouter()
router.register(r"shops", ShopsAPI, basename="shop")


urlpatterns = [
    path("", include(router.urls)),
]
