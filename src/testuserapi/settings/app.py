# Application definition
ROOT_URLCONF = "testuserapi.urls"

WSGI_APPLICATION = "testuserapi.wsgi.application"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Static files
MEDIA_URL = "/media/"
MEDIA_ROOT = "/var/testuserapi/media/"

STATIC_URL = "/static/"
STATIC_ROOT = "/var/testuserapi/static/"

# 100mb
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100

FILE_UPLOAD_PERMISSIONS = 0o644
