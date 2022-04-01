from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        model_fields = (
            "email",
            "first_name",
            "last_name",
            "sex",
        )
        fields = model_fields
        queryset = User.objects.only(*model_fields)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        model_fields = ("email",)
        fields = model_fields
        queryset = User.objects.only(*model_fields)
