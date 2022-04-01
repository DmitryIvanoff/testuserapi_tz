REST_FRAMEWORK = {
    # filters
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.OrderingFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    # schema
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # throttling
    "DEFAULT_THROTTLE_RATES": {"anon": "100/day", "user": "1000/day"},
    # pagination
    "DEFAULT_PAGINATION_CLASS": "testuserapi.common.pagination.TestUserAPIPagination",
    "PAGE_SIZE": 25,
}
