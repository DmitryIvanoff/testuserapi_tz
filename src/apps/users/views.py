from django.db.models import QuerySet
from rest_framework import (
    generics,
    viewsets,
)

from apps.users.models import User
from apps.users.serializers import (
    UserListSerializer,
    UserSerializer,
)


class UserView(
    viewsets.ModelViewSet,
):
    serializer_class = UserSerializer
    serializer_class_list = UserListSerializer
    queryset = UserSerializer.Meta.queryset
    queryset_list = UserListSerializer.Meta.queryset
    ordering = ("creation_dt",)
    lookup_field = 'email'
    lookup_value_regex = '[^/]+'

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializer_class_list
        return super(UserView, self).get_serializer_class()

    def get_queryset(self) -> QuerySet[User]:
        if self.action == "list":
            return self.queryset_list.all()
        return super(UserView, self).get_queryset()
