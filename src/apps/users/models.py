from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField

from apps.users.managers import TestUserAPIUserManager


class Color(models.Model):
    color = ColorField(primary_key=True)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')


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
    favourite_colors = models.ManyToManyField(Color, related_name='users', blank=True)

