from api.v1.urls import router as v1_router
from django.urls import include, path
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView


class APIVersionsView(APIView):
    def get(self, request, *args, **kwargs):
        versions = {
            "v1": request.build_absolute_uri("v1/"),
            "v2": request.build_absolute_uri("v2/"),
        }
        return Response(versions)


urlpatterns = [
    path(
        "",
        APIVersionsView.as_view(),
    ),
    path("v1/", include(v1_router.urls)),
    # other version here
]
