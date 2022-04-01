"""
reactor API URL Configuration.
"""
from django.urls import (
    include,
    path,
)
from rest_framework.routers import SimpleRouter


app_name = "api-v1"
router = SimpleRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("", include("apps.users.urls")),
]
