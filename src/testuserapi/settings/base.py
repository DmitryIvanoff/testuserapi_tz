# Default primary key field type
import os


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "changeme")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", True)

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "testuserapi.common.auth.backends.EmailAuthBackend",
]
