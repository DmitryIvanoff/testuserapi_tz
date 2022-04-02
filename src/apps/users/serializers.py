from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from apps.users.models import User, Color
from django.db import transaction


class UserColorField(serializers.CharField, serializers.RelatedField):
    def __init__(self, *args, **kwargs):
        self.format = kwargs.pop('format', 'hex')
        self.queryset = kwargs.pop('queryset', Color.objects.all())
        super(UserColorField, self).__init__(max_length=18, *args, **kwargs)

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        data = super().to_internal_value(data)
        self.run_validators(data)
        Color(color=data).clean_fields()
        obj, _ = queryset.get_or_create(color=data)
        return obj

    def to_representation(self, value: Color):
        return str(value.color)


class UserSerializer(serializers.ModelSerializer):
    favourite_colors = UserColorField(many=True)

    @transaction.atomic()
    def create(self, validated_data):
        return super().create(validated_data)

    @transaction.atomic()
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = User
        model_fields = (
            "email",
            "first_name",
            "last_name",
            "sex",
            'favourite_colors'
        )
        fields = model_fields
        queryset = User.objects.only(*model_fields).prefetch_related('favourite_colors')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        model_fields = ("email",)
        fields = model_fields
        queryset = User.objects.only(*model_fields)


