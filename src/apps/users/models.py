from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import TestUserAPIUserManager


# Create your models here.


class User(AbstractUser):
    objects = TestUserAPIUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(_("email address"), primary_key=True)

    MALE = "M"
    FEMALE = "F"
    SEX_CHOICES = ((MALE, _("male")), (FEMALE, _("female")))

    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)

    creation_dt = models.DateTimeField(auto_now_add=True)
