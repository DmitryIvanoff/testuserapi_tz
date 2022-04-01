from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


UserModel = get_user_model()


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        if email is None:
            return None
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            return user
