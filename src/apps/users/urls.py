from django.urls import (
    include,
    path,
)
from rest_framework.routers import SimpleRouter

from apps.users.views import *


router = SimpleRouter()
router.register("users", UserView, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
