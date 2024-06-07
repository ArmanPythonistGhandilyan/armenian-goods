from django.contrib import admin
from django.urls import include, path

from api.v1.apps.shops.apis.rest import MyApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/", include("api.urls")),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
    path("api/", MyApiView.as_view(), name="my_task_api"),
    path("", MyApiView.as_view(), name="my_task_api"),
]
