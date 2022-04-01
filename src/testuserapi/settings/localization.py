import os

from testuserapi.settings import BASE_DIR


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ru-RU"
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ("ru", "Russian"),
    ("en", "English"),
)
